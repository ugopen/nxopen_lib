from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
##   Adhesive connection. Use this interface to set/get properties and parameters of the spot weld connection.  
## 
##   <br>  Created in NX12.0.0  <br> 

class Adhesive(IConnection): 
    """  Adhesive connection. Use this interface to set/get properties and parameters of the spot weld connection.  """


    ## Getter for property: (@link DiscretizationMethod NXOpen.CAE.Connections.DiscretizationMethod@endlink) DiscretizationMethod
    ##   the discretization method   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return DiscretizationMethod
    @property
    def DiscretizationMethod(self) -> DiscretizationMethod:
        """
        Getter for property: (@link DiscretizationMethod NXOpen.CAE.Connections.DiscretizationMethod@endlink) DiscretizationMethod
          the discretization method   
            
         
        """
        pass
    
    ## Setter for property: (@link DiscretizationMethod NXOpen.CAE.Connections.DiscretizationMethod@endlink) DiscretizationMethod

    ##   the discretization method   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @DiscretizationMethod.setter
    def DiscretizationMethod(self, method: DiscretizationMethod):
        """
        Setter for property: (@link DiscretizationMethod NXOpen.CAE.Connections.DiscretizationMethod@endlink) DiscretizationMethod
          the discretization method   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) DistanceFromStart
    ##   the line Discretization distance from start   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def DistanceFromStart(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) DistanceFromStart
          the line Discretization distance from start   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) DistanceToEnd
    ##   the line Discretization distance to end   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def DistanceToEnd(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) DistanceToEnd
          the line Discretization distance to end   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Height
    ##   the height value   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Height(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Height
          the height value   
            
         
        """
        pass
    
    ## Getter for property: (@link HeightType NXOpen.CAE.Connections.HeightType@endlink) HeightType
    ##   the connection height type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return HeightType
    @property
    def HeightType(self) -> HeightType:
        """
        Getter for property: (@link HeightType NXOpen.CAE.Connections.HeightType@endlink) HeightType
          the connection height type   
            
         
        """
        pass
    
    ## Setter for property: (@link HeightType NXOpen.CAE.Connections.HeightType@endlink) HeightType

    ##   the connection height type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @HeightType.setter
    def HeightType(self, heightType: HeightType):
        """
        Setter for property: (@link HeightType NXOpen.CAE.Connections.HeightType@endlink) HeightType
          the connection height type   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) LengthStep
    ##   the line Discretization length step   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def LengthStep(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) LengthStep
          the line Discretization length step   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.PhysicalMaterial NXOpen.PhysicalMaterial@endlink) Material
    ##   the connection material   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.PhysicalMaterial
    @property
    def Material(self) -> NXOpen.PhysicalMaterial:
        """
        Getter for property: (@link NXOpen.PhysicalMaterial NXOpen.PhysicalMaterial@endlink) Material
          the connection material   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.PhysicalMaterial NXOpen.PhysicalMaterial@endlink) Material

    ##   the connection material   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @Material.setter
    def Material(self, material: NXOpen.PhysicalMaterial):
        """
        Setter for property: (@link NXOpen.PhysicalMaterial NXOpen.PhysicalMaterial@endlink) Material
          the connection material   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxAngleBetweenNormals
    ##   the maximum angle of normals with the projection surface   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def MaxAngleBetweenNormals(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxAngleBetweenNormals
          the maximum angle of normals with the projection surface   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxDistCGToElemCG
    ##   the maximum distance from definition point to center of support element   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def MaxDistCGToElemCG(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxDistCGToElemCG
          the maximum distance from definition point to center of support element   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxLengthStep
    ##   the line Discretization max length step   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def MaxLengthStep(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxLengthStep
          the line Discretization max length step   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxNormalDistCGToFlanges
    ##   the maximum normal distance from definition point to center of element   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def MaxNormalDistCGToFlanges(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxNormalDistCGToFlanges
          the maximum normal distance from definition point to center of element   
            
         
        """
        pass
    
    ## Getter for property: (int) NumberOfDiscretizationPoints
    ##   the number of connections   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return int
    @property
    def NumberOfDiscretizationPoints(self) -> int:
        """
        Getter for property: (int) NumberOfDiscretizationPoints
          the number of connections   
            
         
        """
        pass
    
    ## Setter for property: (int) NumberOfDiscretizationPoints

    ##   the number of connections   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @NumberOfDiscretizationPoints.setter
    def NumberOfDiscretizationPoints(self, num: int):
        """
        Setter for property: (int) NumberOfDiscretizationPoints
          the number of connections   
            
         
        """
        pass
    
    ## Getter for property: (int) NumberOfFlanges
    ##   the number of flanges.  
    ##    When changing the number of flanges this is not applied till an update is performed by calling @link Update::DoUpdate Update::DoUpdate@endlink    
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return int
    @property
    def NumberOfFlanges(self) -> int:
        """
        Getter for property: (int) NumberOfFlanges
          the number of flanges.  
           When changing the number of flanges this is not applied till an update is performed by calling @link Update::DoUpdate Update::DoUpdate@endlink    
         
        """
        pass
    
    ## Setter for property: (int) NumberOfFlanges

    ##   the number of flanges.  
    ##    When changing the number of flanges this is not applied till an update is performed by calling @link Update::DoUpdate Update::DoUpdate@endlink    
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @NumberOfFlanges.setter
    def NumberOfFlanges(self, numberOfFlanges: int):
        """
        Setter for property: (int) NumberOfFlanges
          the number of flanges.  
           When changing the number of flanges this is not applied till an update is performed by calling @link Update::DoUpdate Update::DoUpdate@endlink    
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ProjectTolerance
    ##   the projection tolerance   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def ProjectTolerance(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ProjectTolerance
          the projection tolerance   
            
         
        """
        pass
    
    ## Getter for property: (bool) UseMaxLengthStep
    ##   the usage of max length step   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return bool
    @property
    def UseMaxLengthStep(self) -> bool:
        """
        Getter for property: (bool) UseMaxLengthStep
          the usage of max length step   
            
         
        """
        pass
    
    ## Setter for property: (bool) UseMaxLengthStep

    ##   the usage of max length step   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @UseMaxLengthStep.setter
    def UseMaxLengthStep(self, use: bool):
        """
        Setter for property: (bool) UseMaxLengthStep
          the usage of max length step   
            
         
        """
        pass
    
    ## Getter for property: (bool) UseOriginalNodesOfConnection
    ##   the usage of original nodes of connection   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return bool
    @property
    def UseOriginalNodesOfConnection(self) -> bool:
        """
        Getter for property: (bool) UseOriginalNodesOfConnection
          the usage of original nodes of connection   
            
         
        """
        pass
    
    ## Setter for property: (bool) UseOriginalNodesOfConnection

    ##   the usage of original nodes of connection   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @UseOriginalNodesOfConnection.setter
    def UseOriginalNodesOfConnection(self, use: bool):
        """
        Setter for property: (bool) UseOriginalNodesOfConnection
          the usage of original nodes of connection   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Width
    ##   the width value   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Width(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Width
          the width value   
            
         
        """
        pass
    
import NXOpen
##  Bar connection. Use this interface to set/get properties and parameters of the Bar connection.  
## 
##   <br>  Created in NX1926.0.0  <br> 

class Bar(IConnection): 
    """ Bar connection. Use this interface to set/get properties and parameters of the Bar connection.  """


    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Coefficient
    ##   the coefficient for formula defined diameter   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Coefficient(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Coefficient
          the coefficient for formula defined diameter   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Diameter
    ##   the connection diameter   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Diameter(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Diameter
          the connection diameter   
            
         
        """
        pass
    
    ## Getter for property: (@link DiameterType NXOpen.CAE.Connections.DiameterType@endlink) DiameterType
    ##   the connection diameter type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return DiameterType
    @property
    def DiameterType(self) -> DiameterType:
        """
        Getter for property: (@link DiameterType NXOpen.CAE.Connections.DiameterType@endlink) DiameterType
          the connection diameter type   
            
         
        """
        pass
    
    ## Setter for property: (@link DiameterType NXOpen.CAE.Connections.DiameterType@endlink) DiameterType

    ##   the connection diameter type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @DiameterType.setter
    def DiameterType(self, diameterType: DiameterType):
        """
        Setter for property: (@link DiameterType NXOpen.CAE.Connections.DiameterType@endlink) DiameterType
          the connection diameter type   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.PhysicalMaterial NXOpen.PhysicalMaterial@endlink) Material
    ##   the connection material   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.PhysicalMaterial
    @property
    def Material(self) -> NXOpen.PhysicalMaterial:
        """
        Getter for property: (@link NXOpen.PhysicalMaterial NXOpen.PhysicalMaterial@endlink) Material
          the connection material   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.PhysicalMaterial NXOpen.PhysicalMaterial@endlink) Material

    ##   the connection material   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @Material.setter
    def Material(self, material: NXOpen.PhysicalMaterial):
        """
        Setter for property: (@link NXOpen.PhysicalMaterial NXOpen.PhysicalMaterial@endlink) Material
          the connection material   
            
         
        """
        pass
    
    ## Getter for property: (@link NodalPairingMethod NXOpen.CAE.Connections.NodalPairingMethod@endlink) PairingMethod
    ##   the pairing method of targets   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NodalPairingMethod
    @property
    def PairingMethod(self) -> NodalPairingMethod:
        """
        Getter for property: (@link NodalPairingMethod NXOpen.CAE.Connections.NodalPairingMethod@endlink) PairingMethod
          the pairing method of targets   
            
         
        """
        pass
    
    ## Setter for property: (@link NodalPairingMethod NXOpen.CAE.Connections.NodalPairingMethod@endlink) PairingMethod

    ##   the pairing method of targets   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @PairingMethod.setter
    def PairingMethod(self, method: NodalPairingMethod):
        """
        Setter for property: (@link NodalPairingMethod NXOpen.CAE.Connections.NodalPairingMethod@endlink) PairingMethod
          the pairing method of targets   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) SearchConeAngle
    ##   the search cone angle   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def SearchConeAngle(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) SearchConeAngle
          the search cone angle   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) SearchOrientation
    ##   the pairing search orientation   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Direction
    @property
    def SearchOrientation(self) -> NXOpen.Direction:
        """
        Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) SearchOrientation
          the pairing search orientation   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) SearchOrientation

    ##   the pairing search orientation   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @SearchOrientation.setter
    def SearchOrientation(self, orientation: NXOpen.Direction):
        """
        Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) SearchOrientation
          the pairing search orientation   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) SearchRange
    ##   the search range   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def SearchRange(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) SearchRange
          the search range   
            
         
        """
        pass
    
    ## Getter for property: (str) TableFile
    ##   the table file used to compute the diameter   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return str
    @property
    def TableFile(self) -> str:
        """
        Getter for property: (str) TableFile
          the table file used to compute the diameter   
            
         
        """
        pass
    
    ## Setter for property: (str) TableFile

    ##   the table file used to compute the diameter   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @TableFile.setter
    def TableFile(self, tableFile: str):
        """
        Setter for property: (str) TableFile
          the table file used to compute the diameter   
            
         
        """
        pass
    
import NXOpen
##  Bearing connection. Use this interface to set/get properties and parameters of the Bearing connection.  
## 
##   <br>  Created in NX1953.0.0  <br> 

class Bearing(IConnection): 
    """ Bearing connection. Use this interface to set/get properties and parameters of the Bearing connection.  """


    ## Getter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) Csys
    ##   the csys   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.CoordinateSystem
    @property
    def Csys(self) -> NXOpen.CoordinateSystem:
        """
        Getter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) Csys
          the csys   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) Csys

    ##   the csys   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @Csys.setter
    def Csys(self, csys: NXOpen.CoordinateSystem):
        """
        Setter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) Csys
          the csys   
            
         
        """
        pass
    
    ## Getter for property: (@link CsysType NXOpen.CAE.Connections.CsysType@endlink) CsysType
    ##   the csys type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return CsysType
    @property
    def CsysType(self) -> CsysType:
        """
        Getter for property: (@link CsysType NXOpen.CAE.Connections.CsysType@endlink) CsysType
          the csys type   
            
         
        """
        pass
    
    ## Setter for property: (@link CsysType NXOpen.CAE.Connections.CsysType@endlink) CsysType

    ##   the csys type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @CsysType.setter
    def CsysType(self, csysType: CsysType):
        """
        Setter for property: (@link CsysType NXOpen.CAE.Connections.CsysType@endlink) CsysType
          the csys type   
            
         
        """
        pass
    
    ## Getter for property: (@link NodalPairingMethod NXOpen.CAE.Connections.NodalPairingMethod@endlink) PairingMethod
    ##   the pairing method of targets   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NodalPairingMethod
    @property
    def PairingMethod(self) -> NodalPairingMethod:
        """
        Getter for property: (@link NodalPairingMethod NXOpen.CAE.Connections.NodalPairingMethod@endlink) PairingMethod
          the pairing method of targets   
            
         
        """
        pass
    
    ## Setter for property: (@link NodalPairingMethod NXOpen.CAE.Connections.NodalPairingMethod@endlink) PairingMethod

    ##   the pairing method of targets   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @PairingMethod.setter
    def PairingMethod(self, method: NodalPairingMethod):
        """
        Setter for property: (@link NodalPairingMethod NXOpen.CAE.Connections.NodalPairingMethod@endlink) PairingMethod
          the pairing method of targets   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) SearchConeAngle
    ##   the search cone angle   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def SearchConeAngle(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) SearchConeAngle
          the search cone angle   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) SearchOrientation
    ##   the pairing search orientation   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Direction
    @property
    def SearchOrientation(self) -> NXOpen.Direction:
        """
        Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) SearchOrientation
          the pairing search orientation   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) SearchOrientation

    ##   the pairing search orientation   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @SearchOrientation.setter
    def SearchOrientation(self, orientation: NXOpen.Direction):
        """
        Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) SearchOrientation
          the pairing search orientation   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) SearchRange
    ##   the search range   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def SearchRange(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) SearchRange
          the search range   
            
         
        """
        pass
    
import NXOpen
##  Bolt connection. Use this interface to set/get properties and parameters of the spot weld connection.   <br> To obtain an instance of this object use the connection creators on the @link CAE::Connections::Folder CAE::Connections::Folder@endlink   <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class Bolt(IConnection): 
    """ Bolt connection. Use this interface to set/get properties and parameters of the spot weld connection.  """


    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Coefficient
    ##   the coefficient for formula defined diameter   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Coefficient(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Coefficient
          the coefficient for formula defined diameter   
            
         
        """
        pass
    
    ## Getter for property: (bool) DefineNutDiameter
    ##   the define nut diameter   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return bool
    @property
    def DefineNutDiameter(self) -> bool:
        """
        Getter for property: (bool) DefineNutDiameter
          the define nut diameter   
            
         
        """
        pass
    
    ## Setter for property: (bool) DefineNutDiameter

    ##   the define nut diameter   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @DefineNutDiameter.setter
    def DefineNutDiameter(self, param: bool):
        """
        Setter for property: (bool) DefineNutDiameter
          the define nut diameter   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Diameter
    ##   the connection diameter   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Diameter(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Diameter
          the connection diameter   
            
         
        """
        pass
    
    ## Getter for property: (@link DiameterType NXOpen.CAE.Connections.DiameterType@endlink) DiameterType
    ##   the connection diameter type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return DiameterType
    @property
    def DiameterType(self) -> DiameterType:
        """
        Getter for property: (@link DiameterType NXOpen.CAE.Connections.DiameterType@endlink) DiameterType
          the connection diameter type   
            
         
        """
        pass
    
    ## Setter for property: (@link DiameterType NXOpen.CAE.Connections.DiameterType@endlink) DiameterType

    ##   the connection diameter type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @DiameterType.setter
    def DiameterType(self, diameterType: DiameterType):
        """
        Setter for property: (@link DiameterType NXOpen.CAE.Connections.DiameterType@endlink) DiameterType
          the connection diameter type   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) HeadDiameter
    ##   the head diameter    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def HeadDiameter(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) HeadDiameter
          the head diameter    
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) HeadDiameterCoefficient
    ##   the head diameter coefficient   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def HeadDiameterCoefficient(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) HeadDiameterCoefficient
          the head diameter coefficient   
            
         
        """
        pass
    
    ## Getter for property: (@link HeadDiameterType NXOpen.CAE.Connections.HeadDiameterType@endlink) HeadDiameterType
    ##   the head diameter type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return HeadDiameterType
    @property
    def HeadDiameterType(self) -> HeadDiameterType:
        """
        Getter for property: (@link HeadDiameterType NXOpen.CAE.Connections.HeadDiameterType@endlink) HeadDiameterType
          the head diameter type   
            
         
        """
        pass
    
    ## Setter for property: (@link HeadDiameterType NXOpen.CAE.Connections.HeadDiameterType@endlink) HeadDiameterType

    ##   the head diameter type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @HeadDiameterType.setter
    def HeadDiameterType(self, param: HeadDiameterType):
        """
        Setter for property: (@link HeadDiameterType NXOpen.CAE.Connections.HeadDiameterType@endlink) HeadDiameterType
          the head diameter type   
            
         
        """
        pass
    
    ## Getter for property: (bool) LimitLocationEndpointsLength
    ##   the flag indicating to limit the bolt's length to the length between the location endpoints    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return bool
    @property
    def LimitLocationEndpointsLength(self) -> bool:
        """
        Getter for property: (bool) LimitLocationEndpointsLength
          the flag indicating to limit the bolt's length to the length between the location endpoints    
            
         
        """
        pass
    
    ## Setter for property: (bool) LimitLocationEndpointsLength

    ##   the flag indicating to limit the bolt's length to the length between the location endpoints    
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @LimitLocationEndpointsLength.setter
    def LimitLocationEndpointsLength(self, param: bool):
        """
        Setter for property: (bool) LimitLocationEndpointsLength
          the flag indicating to limit the bolt's length to the length between the location endpoints    
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.PhysicalMaterial NXOpen.PhysicalMaterial@endlink) Material
    ##   the connection material   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.PhysicalMaterial
    @property
    def Material(self) -> NXOpen.PhysicalMaterial:
        """
        Getter for property: (@link NXOpen.PhysicalMaterial NXOpen.PhysicalMaterial@endlink) Material
          the connection material   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.PhysicalMaterial NXOpen.PhysicalMaterial@endlink) Material

    ##   the connection material   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @Material.setter
    def Material(self, material: NXOpen.PhysicalMaterial):
        """
        Setter for property: (@link NXOpen.PhysicalMaterial NXOpen.PhysicalMaterial@endlink) Material
          the connection material   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxBoltLength
    ##   the maximum bolt length   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def MaxBoltLength(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxBoltLength
          the maximum bolt length   
            
         
        """
        pass
    
    ## Getter for property: (int) NumberOfFlanges
    ##   the number of flanges.  
    ##    When changing the number of flanges this is not applied till an update is performed by calling @link Update::DoUpdate Update::DoUpdate@endlink    
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return int
    @property
    def NumberOfFlanges(self) -> int:
        """
        Getter for property: (int) NumberOfFlanges
          the number of flanges.  
           When changing the number of flanges this is not applied till an update is performed by calling @link Update::DoUpdate Update::DoUpdate@endlink    
         
        """
        pass
    
    ## Setter for property: (int) NumberOfFlanges

    ##   the number of flanges.  
    ##    When changing the number of flanges this is not applied till an update is performed by calling @link Update::DoUpdate Update::DoUpdate@endlink    
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @NumberOfFlanges.setter
    def NumberOfFlanges(self, numberOfFlanges: int):
        """
        Setter for property: (int) NumberOfFlanges
          the number of flanges.  
           When changing the number of flanges this is not applied till an update is performed by calling @link Update::DoUpdate Update::DoUpdate@endlink    
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) NutDiameter
    ##   the nut diameter    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def NutDiameter(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) NutDiameter
          the nut diameter    
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) NutDiameterCoefficient
    ##   the nut diameter coefficient   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def NutDiameterCoefficient(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) NutDiameterCoefficient
          the nut diameter coefficient   
            
         
        """
        pass
    
    ## Getter for property: (@link NutDiameterType NXOpen.CAE.Connections.NutDiameterType@endlink) NutDiameterType
    ##   the nut diameter type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NutDiameterType
    @property
    def NutDiameterType(self) -> NutDiameterType:
        """
        Getter for property: (@link NutDiameterType NXOpen.CAE.Connections.NutDiameterType@endlink) NutDiameterType
          the nut diameter type   
            
         
        """
        pass
    
    ## Setter for property: (@link NutDiameterType NXOpen.CAE.Connections.NutDiameterType@endlink) NutDiameterType

    ##   the nut diameter type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @NutDiameterType.setter
    def NutDiameterType(self, param: NutDiameterType):
        """
        Setter for property: (@link NutDiameterType NXOpen.CAE.Connections.NutDiameterType@endlink) NutDiameterType
          the nut diameter type   
            
         
        """
        pass
    
    ## Getter for property: (@link ShankLengthDiscretizationType NXOpen.CAE.Connections.ShankLengthDiscretizationType@endlink) ShankLengthDiscretizationType
    ##   the shank length discretization type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## @return ShankLengthDiscretizationType
    @property
    def ShankLengthDiscretizationType(self) -> ShankLengthDiscretizationType:
        """
        Getter for property: (@link ShankLengthDiscretizationType NXOpen.CAE.Connections.ShankLengthDiscretizationType@endlink) ShankLengthDiscretizationType
          the shank length discretization type   
            
         
        """
        pass
    
    ## Setter for property: (@link ShankLengthDiscretizationType NXOpen.CAE.Connections.ShankLengthDiscretizationType@endlink) ShankLengthDiscretizationType

    ##   the shank length discretization type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    @ShankLengthDiscretizationType.setter
    def ShankLengthDiscretizationType(self, param: ShankLengthDiscretizationType):
        """
        Setter for property: (@link ShankLengthDiscretizationType NXOpen.CAE.Connections.ShankLengthDiscretizationType@endlink) ShankLengthDiscretizationType
          the shank length discretization type   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ShankLengthPercentage
    ##   the shank length percentage   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def ShankLengthPercentage(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ShankLengthPercentage
          the shank length percentage   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ShankLengthUser
    ##   the user specified shank length   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def ShankLengthUser(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ShankLengthUser
          the user specified shank length   
            
         
        """
        pass
    
    ## Getter for property: (str) TableFile
    ##   the table file used to compute the diameter   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return str
    @property
    def TableFile(self) -> str:
        """
        Getter for property: (str) TableFile
          the table file used to compute the diameter   
            
         
        """
        pass
    
    ## Setter for property: (str) TableFile

    ##   the table file used to compute the diameter   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @TableFile.setter
    def TableFile(self, tableFile: str):
        """
        Setter for property: (str) TableFile
          the table file used to compute the diameter   
            
         
        """
        pass
    
    ## Getter for property: (bool) UseMasterPointAsCenter
    ##   the flag to use the master point as center   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## @return bool
    @property
    def UseMasterPointAsCenter(self) -> bool:
        """
        Getter for property: (bool) UseMasterPointAsCenter
          the flag to use the master point as center   
            
         
        """
        pass
    
    ## Setter for property: (bool) UseMasterPointAsCenter

    ##   the flag to use the master point as center   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    @UseMasterPointAsCenter.setter
    def UseMasterPointAsCenter(self, param: bool):
        """
        Setter for property: (bool) UseMasterPointAsCenter
          the flag to use the master point as center   
            
         
        """
        pass
    
##  Bushing type 
##  Rectangular bushing type 
class BushingType(Enum):
    """
    Members Include: <Rectangular> <Cylindrical>
    """
    Rectangular: int
    Cylindrical: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> BushingType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


import NXOpen
import NXOpen.Fields
##  Bushing connection. Use this interface to set/get properties and parameters of the Bushing connection.  
## 
##   <br>  Created in NX12.0.0  <br> 

class Bushing(IConnection): 
    """ Bushing connection. Use this interface to set/get properties and parameters of the Bushing connection.  """


    ## Getter for property: (@link BushingType NXOpen.CAE.Connections.BushingType@endlink) BushingType
    ##   the bushing type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return BushingType
    @property
    def BushingType(self) -> BushingType:
        """
        Getter for property: (@link BushingType NXOpen.CAE.Connections.BushingType@endlink) BushingType
          the bushing type   
            
         
        """
        pass
    
    ## Setter for property: (@link BushingType NXOpen.CAE.Connections.BushingType@endlink) BushingType

    ##   the bushing type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @BushingType.setter
    def BushingType(self, bushingType: BushingType):
        """
        Setter for property: (@link BushingType NXOpen.CAE.Connections.BushingType@endlink) BushingType
          the bushing type   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) Csys
    ##   the csys   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.CoordinateSystem
    @property
    def Csys(self) -> NXOpen.CoordinateSystem:
        """
        Getter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) Csys
          the csys   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) Csys

    ##   the csys   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @Csys.setter
    def Csys(self, csys: NXOpen.CoordinateSystem):
        """
        Setter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) Csys
          the csys   
            
         
        """
        pass
    
    ## Getter for property: (@link CsysType NXOpen.CAE.Connections.CsysType@endlink) CsysType
    ##   the csys type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return CsysType
    @property
    def CsysType(self) -> CsysType:
        """
        Getter for property: (@link CsysType NXOpen.CAE.Connections.CsysType@endlink) CsysType
          the csys type   
            
         
        """
        pass
    
    ## Setter for property: (@link CsysType NXOpen.CAE.Connections.CsysType@endlink) CsysType

    ##   the csys type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @CsysType.setter
    def CsysType(self, csysType: CsysType):
        """
        Setter for property: (@link CsysType NXOpen.CAE.Connections.CsysType@endlink) CsysType
          the csys type   
            
         
        """
        pass
    
    ## Getter for property: (bool) IsMassOnBothTargets
    ##   the isMassOnBothTargets   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return bool
    @property
    def IsMassOnBothTargets(self) -> bool:
        """
        Getter for property: (bool) IsMassOnBothTargets
          the isMassOnBothTargets   
            
         
        """
        pass
    
    ## Setter for property: (bool) IsMassOnBothTargets

    ##   the isMassOnBothTargets   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @IsMassOnBothTargets.setter
    def IsMassOnBothTargets(self, isMassOnBothTargets: bool):
        """
        Setter for property: (bool) IsMassOnBothTargets
          the isMassOnBothTargets   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Mass
    ##   the mass value   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Mass(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Mass
          the mass value   
            
         
        """
        pass
    
    ## Getter for property: (@link NodalPairingMethod NXOpen.CAE.Connections.NodalPairingMethod@endlink) PairingMethod
    ##   the pairing method of targets   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NodalPairingMethod
    @property
    def PairingMethod(self) -> NodalPairingMethod:
        """
        Getter for property: (@link NodalPairingMethod NXOpen.CAE.Connections.NodalPairingMethod@endlink) PairingMethod
          the pairing method of targets   
            
         
        """
        pass
    
    ## Setter for property: (@link NodalPairingMethod NXOpen.CAE.Connections.NodalPairingMethod@endlink) PairingMethod

    ##   the pairing method of targets   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @PairingMethod.setter
    def PairingMethod(self, method: NodalPairingMethod):
        """
        Setter for property: (@link NodalPairingMethod NXOpen.CAE.Connections.NodalPairingMethod@endlink) PairingMethod
          the pairing method of targets   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RCylindricalStiffnessConstant
    ##   the R cylindrical stiffness constant   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def RCylindricalStiffnessConstant(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RCylindricalStiffnessConstant
          the R cylindrical stiffness constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RCylindricalStiffnessDynamic
    ##   the R cylindrical stiffness dynamic   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Fields.ScalarFieldWrapper
    @property
    def RCylindricalStiffnessDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RCylindricalStiffnessDynamic
          the R cylindrical stiffness dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RCylindricalStiffnessDynamic

    ##   the R cylindrical stiffness dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @RCylindricalStiffnessDynamic.setter
    def RCylindricalStiffnessDynamic(self, rDynamic: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RCylindricalStiffnessDynamic
          the R cylindrical stiffness dynamic   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RCylindricalStructuralDampingConstant
    ##   the R cylindrical structural damping constant   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def RCylindricalStructuralDampingConstant(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RCylindricalStructuralDampingConstant
          the R cylindrical structural damping constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RCylindricalStructuralDampingDynamic
    ##   the R cylindrical structural damping dynamic   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Fields.ScalarFieldWrapper
    @property
    def RCylindricalStructuralDampingDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RCylindricalStructuralDampingDynamic
          the R cylindrical structural damping dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RCylindricalStructuralDampingDynamic

    ##   the R cylindrical structural damping dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @RCylindricalStructuralDampingDynamic.setter
    def RCylindricalStructuralDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RCylindricalStructuralDampingDynamic
          the R cylindrical structural damping dynamic   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RCylindricalViscousDampingConstant
    ##   the R cylindrical viscous damping constant   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def RCylindricalViscousDampingConstant(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RCylindricalViscousDampingConstant
          the R cylindrical viscous damping constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RCylindricalViscousDampingDynamic
    ##   the R cylindrical viscous damping dynamic   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Fields.ScalarFieldWrapper
    @property
    def RCylindricalViscousDampingDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RCylindricalViscousDampingDynamic
          the R cylindrical viscous damping dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RCylindricalViscousDampingDynamic

    ##   the R cylindrical viscous damping dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @RCylindricalViscousDampingDynamic.setter
    def RCylindricalViscousDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RCylindricalViscousDampingDynamic
          the R cylindrical viscous damping dynamic   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RNonlinearCylindricalDamping
    ##   the R nonlinear cylindrical damping   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.Fields.ScalarFieldWrapper
    @property
    def RNonlinearCylindricalDamping(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RNonlinearCylindricalDamping
          the R nonlinear cylindrical damping   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RNonlinearCylindricalDamping

    ##   the R nonlinear cylindrical damping   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @RNonlinearCylindricalDamping.setter
    def RNonlinearCylindricalDamping(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RNonlinearCylindricalDamping
          the R nonlinear cylindrical damping   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RNonlinearCylindricalStiffness
    ##   the R nonlinear cylindrical stiffness   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.Fields.ScalarFieldWrapper
    @property
    def RNonlinearCylindricalStiffness(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RNonlinearCylindricalStiffness
          the R nonlinear cylindrical stiffness   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RNonlinearCylindricalStiffness

    ##   the R nonlinear cylindrical stiffness   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @RNonlinearCylindricalStiffness.setter
    def RNonlinearCylindricalStiffness(self, rDynamic: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RNonlinearCylindricalStiffness
          the R nonlinear cylindrical stiffness   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RrCylindricalStiffnessConstant
    ##   the RR cylindrical stiffness constant   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def RrCylindricalStiffnessConstant(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RrCylindricalStiffnessConstant
          the RR cylindrical stiffness constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RrCylindricalStiffnessDynamic
    ##   the RR cylindrical stiffness dynamic   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Fields.ScalarFieldWrapper
    @property
    def RrCylindricalStiffnessDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RrCylindricalStiffnessDynamic
          the RR cylindrical stiffness dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RrCylindricalStiffnessDynamic

    ##   the RR cylindrical stiffness dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @RrCylindricalStiffnessDynamic.setter
    def RrCylindricalStiffnessDynamic(self, rrDynamic: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RrCylindricalStiffnessDynamic
          the RR cylindrical stiffness dynamic   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RrCylindricalStructuralDampingConstant
    ##   the RR structural damping constant   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def RrCylindricalStructuralDampingConstant(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RrCylindricalStructuralDampingConstant
          the RR structural damping constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RrCylindricalStructuralDampingDynamic
    ##   the RR cylindrical structural damping dynamic   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Fields.ScalarFieldWrapper
    @property
    def RrCylindricalStructuralDampingDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RrCylindricalStructuralDampingDynamic
          the RR cylindrical structural damping dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RrCylindricalStructuralDampingDynamic

    ##   the RR cylindrical structural damping dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @RrCylindricalStructuralDampingDynamic.setter
    def RrCylindricalStructuralDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RrCylindricalStructuralDampingDynamic
          the RR cylindrical structural damping dynamic   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RrCylindricalViscousDampingConstant
    ##   the RR cylindrical viscous damping constant   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def RrCylindricalViscousDampingConstant(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RrCylindricalViscousDampingConstant
          the RR cylindrical viscous damping constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RrCylindricalViscousDampingDynamic
    ##   the RR cylindrical viscous damping dynamic   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Fields.ScalarFieldWrapper
    @property
    def RrCylindricalViscousDampingDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RrCylindricalViscousDampingDynamic
          the RR cylindrical viscous damping dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RrCylindricalViscousDampingDynamic

    ##   the RR cylindrical viscous damping dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @RrCylindricalViscousDampingDynamic.setter
    def RrCylindricalViscousDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RrCylindricalViscousDampingDynamic
          the RR cylindrical viscous damping dynamic   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RrNonlinearCylindricalDamping
    ##   the RR nonlinear cylindrical damping   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.Fields.ScalarFieldWrapper
    @property
    def RrNonlinearCylindricalDamping(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RrNonlinearCylindricalDamping
          the RR nonlinear cylindrical damping   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RrNonlinearCylindricalDamping

    ##   the RR nonlinear cylindrical damping   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @RrNonlinearCylindricalDamping.setter
    def RrNonlinearCylindricalDamping(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RrNonlinearCylindricalDamping
          the RR nonlinear cylindrical damping   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RrNonlinearCylindricalStiffness
    ##   the RR nonlinear cylindrical stiffness   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.Fields.ScalarFieldWrapper
    @property
    def RrNonlinearCylindricalStiffness(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RrNonlinearCylindricalStiffness
          the RR nonlinear cylindrical stiffness   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RrNonlinearCylindricalStiffness

    ##   the RR nonlinear cylindrical stiffness   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @RrNonlinearCylindricalStiffness.setter
    def RrNonlinearCylindricalStiffness(self, rrDynamic: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RrNonlinearCylindricalStiffness
          the RR nonlinear cylindrical stiffness   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RxNonlinearDamping
    ##   the RX nonlinear damping   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.Fields.ScalarFieldWrapper
    @property
    def RxNonlinearDamping(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RxNonlinearDamping
          the RX nonlinear damping   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RxNonlinearDamping

    ##   the RX nonlinear damping   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @RxNonlinearDamping.setter
    def RxNonlinearDamping(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RxNonlinearDamping
          the RX nonlinear damping   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RxNonlinearStiffness
    ##   the RX nonlinear stiffness   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.Fields.ScalarFieldWrapper
    @property
    def RxNonlinearStiffness(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RxNonlinearStiffness
          the RX nonlinear stiffness   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RxNonlinearStiffness

    ##   the RX nonlinear stiffness   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @RxNonlinearStiffness.setter
    def RxNonlinearStiffness(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RxNonlinearStiffness
          the RX nonlinear stiffness   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RxStiffnessConstant
    ##   the RX stiffness constant   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def RxStiffnessConstant(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RxStiffnessConstant
          the RX stiffness constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RxStiffnessDynamic
    ##   the RX stiffness dynamic   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Fields.ScalarFieldWrapper
    @property
    def RxStiffnessDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RxStiffnessDynamic
          the RX stiffness dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RxStiffnessDynamic

    ##   the RX stiffness dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @RxStiffnessDynamic.setter
    def RxStiffnessDynamic(self, rxDynamic: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RxStiffnessDynamic
          the RX stiffness dynamic   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RxStructuralDampingConstant
    ##   the RX structural damping constant   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def RxStructuralDampingConstant(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RxStructuralDampingConstant
          the RX structural damping constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RxStructuralDampingDynamic
    ##   the RX structural damping dynamic   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Fields.ScalarFieldWrapper
    @property
    def RxStructuralDampingDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RxStructuralDampingDynamic
          the RX structural damping dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RxStructuralDampingDynamic

    ##   the RX structural damping dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @RxStructuralDampingDynamic.setter
    def RxStructuralDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RxStructuralDampingDynamic
          the RX structural damping dynamic   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RxViscousDampingConstant
    ##   the RX viscous damping constant   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def RxViscousDampingConstant(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RxViscousDampingConstant
          the RX viscous damping constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RxViscousDampingDynamic
    ##   the RX viscous damping dynamic   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Fields.ScalarFieldWrapper
    @property
    def RxViscousDampingDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RxViscousDampingDynamic
          the RX viscous damping dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RxViscousDampingDynamic

    ##   the RX viscous damping dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @RxViscousDampingDynamic.setter
    def RxViscousDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RxViscousDampingDynamic
          the RX viscous damping dynamic   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RyNonlinearDamping
    ##   the RY nonlinear damping   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.Fields.ScalarFieldWrapper
    @property
    def RyNonlinearDamping(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RyNonlinearDamping
          the RY nonlinear damping   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RyNonlinearDamping

    ##   the RY nonlinear damping   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @RyNonlinearDamping.setter
    def RyNonlinearDamping(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RyNonlinearDamping
          the RY nonlinear damping   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RyNonlinearStiffness
    ##   the RY nonlinear stiffness   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.Fields.ScalarFieldWrapper
    @property
    def RyNonlinearStiffness(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RyNonlinearStiffness
          the RY nonlinear stiffness   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RyNonlinearStiffness

    ##   the RY nonlinear stiffness   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @RyNonlinearStiffness.setter
    def RyNonlinearStiffness(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RyNonlinearStiffness
          the RY nonlinear stiffness   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RyStiffnessConstant
    ##   the RY stiffness constant   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def RyStiffnessConstant(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RyStiffnessConstant
          the RY stiffness constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RyStiffnessDynamic
    ##   the RY stiffness dynamic   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Fields.ScalarFieldWrapper
    @property
    def RyStiffnessDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RyStiffnessDynamic
          the RY stiffness dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RyStiffnessDynamic

    ##   the RY stiffness dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @RyStiffnessDynamic.setter
    def RyStiffnessDynamic(self, ryDynamic: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RyStiffnessDynamic
          the RY stiffness dynamic   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RyStructuralDampingConstant
    ##   the RY structural damping constant   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def RyStructuralDampingConstant(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RyStructuralDampingConstant
          the RY structural damping constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RyStructuralDampingDynamic
    ##   the RY structural damping dynamic   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Fields.ScalarFieldWrapper
    @property
    def RyStructuralDampingDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RyStructuralDampingDynamic
          the RY structural damping dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RyStructuralDampingDynamic

    ##   the RY structural damping dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @RyStructuralDampingDynamic.setter
    def RyStructuralDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RyStructuralDampingDynamic
          the RY structural damping dynamic   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RyViscousDampingConstant
    ##   the RY viscous damping constant   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def RyViscousDampingConstant(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RyViscousDampingConstant
          the RY viscous damping constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RyViscousDampingDynamic
    ##   the RY viscous damping dynamic   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Fields.ScalarFieldWrapper
    @property
    def RyViscousDampingDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RyViscousDampingDynamic
          the RY viscous damping dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RyViscousDampingDynamic

    ##   the RY viscous damping dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @RyViscousDampingDynamic.setter
    def RyViscousDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RyViscousDampingDynamic
          the RY viscous damping dynamic   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RzCylindricalStiffnessConstant
    ##   the RZ cylindrical stiffness constant   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def RzCylindricalStiffnessConstant(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RzCylindricalStiffnessConstant
          the RZ cylindrical stiffness constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzCylindricalStiffnessDynamic
    ##   the RZ cylindrical stiffness dynamic   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Fields.ScalarFieldWrapper
    @property
    def RzCylindricalStiffnessDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzCylindricalStiffnessDynamic
          the RZ cylindrical stiffness dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzCylindricalStiffnessDynamic

    ##   the RZ cylindrical stiffness dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @RzCylindricalStiffnessDynamic.setter
    def RzCylindricalStiffnessDynamic(self, rzDynamic: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzCylindricalStiffnessDynamic
          the RZ cylindrical stiffness dynamic   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RzCylindricalStructuralDampingConstant
    ##   the RZ structural damping constant   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def RzCylindricalStructuralDampingConstant(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RzCylindricalStructuralDampingConstant
          the RZ structural damping constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzCylindricalStructuralDampingDynamic
    ##   the RZ cylindrical structural damping dynamic   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Fields.ScalarFieldWrapper
    @property
    def RzCylindricalStructuralDampingDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzCylindricalStructuralDampingDynamic
          the RZ cylindrical structural damping dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzCylindricalStructuralDampingDynamic

    ##   the RZ cylindrical structural damping dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @RzCylindricalStructuralDampingDynamic.setter
    def RzCylindricalStructuralDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzCylindricalStructuralDampingDynamic
          the RZ cylindrical structural damping dynamic   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RzCylindricalViscousDampingConstant
    ##   the RZ cylindrical viscous damping constant   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def RzCylindricalViscousDampingConstant(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RzCylindricalViscousDampingConstant
          the RZ cylindrical viscous damping constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzCylindricalViscousDampingDynamic
    ##   the RZ cylindrical viscous damping dynamic   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Fields.ScalarFieldWrapper
    @property
    def RzCylindricalViscousDampingDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzCylindricalViscousDampingDynamic
          the RZ cylindrical viscous damping dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzCylindricalViscousDampingDynamic

    ##   the RZ cylindrical viscous damping dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @RzCylindricalViscousDampingDynamic.setter
    def RzCylindricalViscousDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzCylindricalViscousDampingDynamic
          the RZ cylindrical viscous damping dynamic   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzNonlinearCylindricalDamping
    ##   the RZ nonlinear cylindrical damping   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.Fields.ScalarFieldWrapper
    @property
    def RzNonlinearCylindricalDamping(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzNonlinearCylindricalDamping
          the RZ nonlinear cylindrical damping   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzNonlinearCylindricalDamping

    ##   the RZ nonlinear cylindrical damping   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @RzNonlinearCylindricalDamping.setter
    def RzNonlinearCylindricalDamping(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzNonlinearCylindricalDamping
          the RZ nonlinear cylindrical damping   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzNonlinearCylindricalStiffness
    ##   the RZ nonlinear cylindrical stiffness   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.Fields.ScalarFieldWrapper
    @property
    def RzNonlinearCylindricalStiffness(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzNonlinearCylindricalStiffness
          the RZ nonlinear cylindrical stiffness   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzNonlinearCylindricalStiffness

    ##   the RZ nonlinear cylindrical stiffness   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @RzNonlinearCylindricalStiffness.setter
    def RzNonlinearCylindricalStiffness(self, rzDynamic: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzNonlinearCylindricalStiffness
          the RZ nonlinear cylindrical stiffness   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzNonlinearDamping
    ##   the RZ nonlinear damping   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.Fields.ScalarFieldWrapper
    @property
    def RzNonlinearDamping(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzNonlinearDamping
          the RZ nonlinear damping   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzNonlinearDamping

    ##   the RZ nonlinear damping   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @RzNonlinearDamping.setter
    def RzNonlinearDamping(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzNonlinearDamping
          the RZ nonlinear damping   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzNonlinearStiffness
    ##   the RZ nonlinear stiffness   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.Fields.ScalarFieldWrapper
    @property
    def RzNonlinearStiffness(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzNonlinearStiffness
          the RZ nonlinear stiffness   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzNonlinearStiffness

    ##   the RZ nonlinear stiffness   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @RzNonlinearStiffness.setter
    def RzNonlinearStiffness(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzNonlinearStiffness
          the RZ nonlinear stiffness   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RzStiffnessConstant
    ##   the RZ stiffness constant   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def RzStiffnessConstant(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RzStiffnessConstant
          the RZ stiffness constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzStiffnessDynamic
    ##   the RZ stiffness dynamic   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Fields.ScalarFieldWrapper
    @property
    def RzStiffnessDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzStiffnessDynamic
          the RZ stiffness dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzStiffnessDynamic

    ##   the RZ stiffness dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @RzStiffnessDynamic.setter
    def RzStiffnessDynamic(self, rzDynamic: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzStiffnessDynamic
          the RZ stiffness dynamic   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RzStructuralDampingConstant
    ##   the RZ structural damping constant   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def RzStructuralDampingConstant(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RzStructuralDampingConstant
          the RZ structural damping constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzStructuralDampingDynamic
    ##   the RZ structural damping dynamic   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Fields.ScalarFieldWrapper
    @property
    def RzStructuralDampingDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzStructuralDampingDynamic
          the RZ structural damping dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzStructuralDampingDynamic

    ##   the RZ structural damping dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @RzStructuralDampingDynamic.setter
    def RzStructuralDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzStructuralDampingDynamic
          the RZ structural damping dynamic   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RzViscousDampingConstant
    ##   the RZ viscous damping constant   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def RzViscousDampingConstant(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RzViscousDampingConstant
          the RZ viscous damping constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzViscousDampingDynamic
    ##   the RZ viscous damping dynamic   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Fields.ScalarFieldWrapper
    @property
    def RzViscousDampingDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzViscousDampingDynamic
          the RZ viscous damping dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzViscousDampingDynamic

    ##   the RZ viscous damping dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @RzViscousDampingDynamic.setter
    def RzViscousDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzViscousDampingDynamic
          the RZ viscous damping dynamic   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) SearchConeAngle
    ##   the search cone angle   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def SearchConeAngle(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) SearchConeAngle
          the search cone angle   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) SearchOrientation
    ##   the pairing search orientation   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Direction
    @property
    def SearchOrientation(self) -> NXOpen.Direction:
        """
        Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) SearchOrientation
          the pairing search orientation   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) SearchOrientation

    ##   the pairing search orientation   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @SearchOrientation.setter
    def SearchOrientation(self, orientation: NXOpen.Direction):
        """
        Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) SearchOrientation
          the pairing search orientation   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) SearchRange
    ##   the search range   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def SearchRange(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) SearchRange
          the search range   
            
         
        """
        pass
    
    ## Getter for property: (@link StiffnessType NXOpen.CAE.Connections.StiffnessType@endlink) StiffnessType
    ##   the stiffness type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return StiffnessType
    @property
    def StiffnessType(self) -> StiffnessType:
        """
        Getter for property: (@link StiffnessType NXOpen.CAE.Connections.StiffnessType@endlink) StiffnessType
          the stiffness type   
            
         
        """
        pass
    
    ## Setter for property: (@link StiffnessType NXOpen.CAE.Connections.StiffnessType@endlink) StiffnessType

    ##   the stiffness type   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @StiffnessType.setter
    def StiffnessType(self, oStiffnessType: StiffnessType):
        """
        Setter for property: (@link StiffnessType NXOpen.CAE.Connections.StiffnessType@endlink) StiffnessType
          the stiffness type   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) XNonlinearDamping
    ##   the X nonlinear damping   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.Fields.ScalarFieldWrapper
    @property
    def XNonlinearDamping(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) XNonlinearDamping
          the X nonlinear damping   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) XNonlinearDamping

    ##   the X nonlinear damping   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @XNonlinearDamping.setter
    def XNonlinearDamping(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) XNonlinearDamping
          the X nonlinear damping   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) XNonlinearStiffness
    ##   the X nonlinear stiffness   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.Fields.ScalarFieldWrapper
    @property
    def XNonlinearStiffness(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) XNonlinearStiffness
          the X nonlinear stiffness   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) XNonlinearStiffness

    ##   the X nonlinear stiffness   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @XNonlinearStiffness.setter
    def XNonlinearStiffness(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) XNonlinearStiffness
          the X nonlinear stiffness   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) XStiffnessConstant
    ##   the X stiffness constant   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def XStiffnessConstant(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) XStiffnessConstant
          the X stiffness constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) XStiffnessDynamic
    ##   the X stiffness dynamic   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Fields.ScalarFieldWrapper
    @property
    def XStiffnessDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) XStiffnessDynamic
          the X stiffness dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) XStiffnessDynamic

    ##   the X stiffness dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @XStiffnessDynamic.setter
    def XStiffnessDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) XStiffnessDynamic
          the X stiffness dynamic   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) XStructuralDampingConstant
    ##   the X structural damping constant   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def XStructuralDampingConstant(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) XStructuralDampingConstant
          the X structural damping constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) XStructuralDampingDynamic
    ##   the X structural damping dynamic   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Fields.ScalarFieldWrapper
    @property
    def XStructuralDampingDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) XStructuralDampingDynamic
          the X structural damping dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) XStructuralDampingDynamic

    ##   the X structural damping dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @XStructuralDampingDynamic.setter
    def XStructuralDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) XStructuralDampingDynamic
          the X structural damping dynamic   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) XViscousDampingConstant
    ##   the X viscous damping constant   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def XViscousDampingConstant(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) XViscousDampingConstant
          the X viscous damping constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) XViscousDampingDynamic
    ##   the X viscous damping dynamic   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Fields.ScalarFieldWrapper
    @property
    def XViscousDampingDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) XViscousDampingDynamic
          the X viscous damping dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) XViscousDampingDynamic

    ##   the X viscous damping dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @XViscousDampingDynamic.setter
    def XViscousDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) XViscousDampingDynamic
          the X viscous damping dynamic   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) YNonlinearDamping
    ##   the Y nonlinear damping   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.Fields.ScalarFieldWrapper
    @property
    def YNonlinearDamping(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) YNonlinearDamping
          the Y nonlinear damping   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) YNonlinearDamping

    ##   the Y nonlinear damping   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @YNonlinearDamping.setter
    def YNonlinearDamping(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) YNonlinearDamping
          the Y nonlinear damping   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) YNonlinearStiffness
    ##   the Y nonlinear stiffness   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.Fields.ScalarFieldWrapper
    @property
    def YNonlinearStiffness(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) YNonlinearStiffness
          the Y nonlinear stiffness   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) YNonlinearStiffness

    ##   the Y nonlinear stiffness   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @YNonlinearStiffness.setter
    def YNonlinearStiffness(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) YNonlinearStiffness
          the Y nonlinear stiffness   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) YStiffnessConstant
    ##   the Y stiffness constant   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def YStiffnessConstant(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) YStiffnessConstant
          the Y stiffness constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) YStiffnessDynamic
    ##   the Y stiffness dynamic   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Fields.ScalarFieldWrapper
    @property
    def YStiffnessDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) YStiffnessDynamic
          the Y stiffness dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) YStiffnessDynamic

    ##   the Y stiffness dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @YStiffnessDynamic.setter
    def YStiffnessDynamic(self, yDynamic: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) YStiffnessDynamic
          the Y stiffness dynamic   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) YStructuralDampingConstant
    ##   the Y structural damping constant   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def YStructuralDampingConstant(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) YStructuralDampingConstant
          the Y structural damping constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) YStructuralDampingDynamic
    ##   the Y structural damping dynamic   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Fields.ScalarFieldWrapper
    @property
    def YStructuralDampingDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) YStructuralDampingDynamic
          the Y structural damping dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) YStructuralDampingDynamic

    ##   the Y structural damping dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @YStructuralDampingDynamic.setter
    def YStructuralDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) YStructuralDampingDynamic
          the Y structural damping dynamic   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) YViscousDampingConstant
    ##   the Y viscous damping constant   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def YViscousDampingConstant(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) YViscousDampingConstant
          the Y viscous damping constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) YViscousDampingDynamic
    ##   the Y viscous damping dynamic   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Fields.ScalarFieldWrapper
    @property
    def YViscousDampingDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) YViscousDampingDynamic
          the Y viscous damping dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) YViscousDampingDynamic

    ##   the Y viscous damping dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @YViscousDampingDynamic.setter
    def YViscousDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) YViscousDampingDynamic
          the Y viscous damping dynamic   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ZCylindricalStiffnessConstant
    ##   the Z cylindrical stiffness constant   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def ZCylindricalStiffnessConstant(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ZCylindricalStiffnessConstant
          the Z cylindrical stiffness constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZCylindricalStiffnessDynamic
    ##   the Z cylindrical stiffness dynamic   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Fields.ScalarFieldWrapper
    @property
    def ZCylindricalStiffnessDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZCylindricalStiffnessDynamic
          the Z cylindrical stiffness dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZCylindricalStiffnessDynamic

    ##   the Z cylindrical stiffness dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @ZCylindricalStiffnessDynamic.setter
    def ZCylindricalStiffnessDynamic(self, zDynamic: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZCylindricalStiffnessDynamic
          the Z cylindrical stiffness dynamic   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ZCylindricalStructuralDampingConstant
    ##   the Z cylindrical structural damping constant   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def ZCylindricalStructuralDampingConstant(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ZCylindricalStructuralDampingConstant
          the Z cylindrical structural damping constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZCylindricalStructuralDampingDynamic
    ##   the Z cylindrical structural damping dynamic   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Fields.ScalarFieldWrapper
    @property
    def ZCylindricalStructuralDampingDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZCylindricalStructuralDampingDynamic
          the Z cylindrical structural damping dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZCylindricalStructuralDampingDynamic

    ##   the Z cylindrical structural damping dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @ZCylindricalStructuralDampingDynamic.setter
    def ZCylindricalStructuralDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZCylindricalStructuralDampingDynamic
          the Z cylindrical structural damping dynamic   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ZCylindricalViscousDampingConstant
    ##   the Z cylindrical viscous damping constant   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def ZCylindricalViscousDampingConstant(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ZCylindricalViscousDampingConstant
          the Z cylindrical viscous damping constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZCylindricalViscousDampingDynamic
    ##   the Z cylindrical viscous damping dynamic   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Fields.ScalarFieldWrapper
    @property
    def ZCylindricalViscousDampingDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZCylindricalViscousDampingDynamic
          the Z cylindrical viscous damping dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZCylindricalViscousDampingDynamic

    ##   the Z cylindrical viscous damping dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @ZCylindricalViscousDampingDynamic.setter
    def ZCylindricalViscousDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZCylindricalViscousDampingDynamic
          the Z cylindrical viscous damping dynamic   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZNonlinearCylindricalDamping
    ##   the Z nonlinear cylindrical damping   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.Fields.ScalarFieldWrapper
    @property
    def ZNonlinearCylindricalDamping(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZNonlinearCylindricalDamping
          the Z nonlinear cylindrical damping   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZNonlinearCylindricalDamping

    ##   the Z nonlinear cylindrical damping   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @ZNonlinearCylindricalDamping.setter
    def ZNonlinearCylindricalDamping(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZNonlinearCylindricalDamping
          the Z nonlinear cylindrical damping   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZNonlinearCylindricalStiffness
    ##   the Z nonlinear cylindrical stiffness   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.Fields.ScalarFieldWrapper
    @property
    def ZNonlinearCylindricalStiffness(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZNonlinearCylindricalStiffness
          the Z nonlinear cylindrical stiffness   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZNonlinearCylindricalStiffness

    ##   the Z nonlinear cylindrical stiffness   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @ZNonlinearCylindricalStiffness.setter
    def ZNonlinearCylindricalStiffness(self, zDynamic: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZNonlinearCylindricalStiffness
          the Z nonlinear cylindrical stiffness   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZNonlinearDamping
    ##   the Z nonlinear damping   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.Fields.ScalarFieldWrapper
    @property
    def ZNonlinearDamping(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZNonlinearDamping
          the Z nonlinear damping   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZNonlinearDamping

    ##   the Z nonlinear damping   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @ZNonlinearDamping.setter
    def ZNonlinearDamping(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZNonlinearDamping
          the Z nonlinear damping   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZNonlinearStiffness
    ##   the Z nonlinear stiffness   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.Fields.ScalarFieldWrapper
    @property
    def ZNonlinearStiffness(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZNonlinearStiffness
          the Z nonlinear stiffness   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZNonlinearStiffness

    ##   the Z nonlinear stiffness   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @ZNonlinearStiffness.setter
    def ZNonlinearStiffness(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZNonlinearStiffness
          the Z nonlinear stiffness   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ZStiffnessConstant
    ##   the Z stiffness constant   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def ZStiffnessConstant(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ZStiffnessConstant
          the Z stiffness constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZStiffnessDynamic
    ##   the Z stiffness dynamic   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Fields.ScalarFieldWrapper
    @property
    def ZStiffnessDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZStiffnessDynamic
          the Z stiffness dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZStiffnessDynamic

    ##   the Z stiffness dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @ZStiffnessDynamic.setter
    def ZStiffnessDynamic(self, zDynamic: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZStiffnessDynamic
          the Z stiffness dynamic   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ZStructuralDampingConstant
    ##   the Z structural damping constant   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def ZStructuralDampingConstant(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ZStructuralDampingConstant
          the Z structural damping constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZStructuralDampingDynamic
    ##   the Z structural damping dynamic   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Fields.ScalarFieldWrapper
    @property
    def ZStructuralDampingDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZStructuralDampingDynamic
          the Z structural damping dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZStructuralDampingDynamic

    ##   the Z structural damping dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @ZStructuralDampingDynamic.setter
    def ZStructuralDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZStructuralDampingDynamic
          the Z structural damping dynamic   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ZViscousDampingConstant
    ##   the Z viscous damping constant   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def ZViscousDampingConstant(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ZViscousDampingConstant
          the Z viscous damping constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZViscousDampingDynamic
    ##   the Z viscous damping dynamic   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Fields.ScalarFieldWrapper
    @property
    def ZViscousDampingDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZViscousDampingDynamic
          the Z viscous damping dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZViscousDampingDynamic

    ##   the Z viscous damping dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @ZViscousDampingDynamic.setter
    def ZViscousDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZViscousDampingDynamic
          the Z viscous damping dynamic   
            
         
        """
        pass
    
##  CAD Components Load Type 
##  Full loading of all CAD components 
class CadComponentsLoadType(Enum):
    """
    Members Include: <AllParts> <MainAssociatedPartsOnly>
    """
    AllParts: int
    MainAssociatedPartsOnly: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> CadComponentsLoadType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


import NXOpen
##  Clinch connection. Use this interface to set/get properties and parameters of the clinch connection.  
## 
##   <br>  Created in NX1847.0.0  <br> 

class Clinch(IConnection): 
    """ Clinch connection. Use this interface to set/get properties and parameters of the clinch connection.  """


    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Coefficient
    ##   the coefficient for formula defined diameter   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Coefficient(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Coefficient
          the coefficient for formula defined diameter   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Diameter
    ##   the connection diameter   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Diameter(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Diameter
          the connection diameter   
            
         
        """
        pass
    
    ## Getter for property: (@link DiameterType NXOpen.CAE.Connections.DiameterType@endlink) DiameterType
    ##   the connection diameter type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return DiameterType
    @property
    def DiameterType(self) -> DiameterType:
        """
        Getter for property: (@link DiameterType NXOpen.CAE.Connections.DiameterType@endlink) DiameterType
          the connection diameter type   
            
         
        """
        pass
    
    ## Setter for property: (@link DiameterType NXOpen.CAE.Connections.DiameterType@endlink) DiameterType

    ##   the connection diameter type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @DiameterType.setter
    def DiameterType(self, diameterType: DiameterType):
        """
        Setter for property: (@link DiameterType NXOpen.CAE.Connections.DiameterType@endlink) DiameterType
          the connection diameter type   
            
         
        """
        pass
    
    ## Getter for property: (@link DiscretizationMethod NXOpen.CAE.Connections.DiscretizationMethod@endlink) DiscretizationMethod
    ##   the discretization method   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return DiscretizationMethod
    @property
    def DiscretizationMethod(self) -> DiscretizationMethod:
        """
        Getter for property: (@link DiscretizationMethod NXOpen.CAE.Connections.DiscretizationMethod@endlink) DiscretizationMethod
          the discretization method   
            
         
        """
        pass
    
    ## Setter for property: (@link DiscretizationMethod NXOpen.CAE.Connections.DiscretizationMethod@endlink) DiscretizationMethod

    ##   the discretization method   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @DiscretizationMethod.setter
    def DiscretizationMethod(self, method: DiscretizationMethod):
        """
        Setter for property: (@link DiscretizationMethod NXOpen.CAE.Connections.DiscretizationMethod@endlink) DiscretizationMethod
          the discretization method   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) DistanceFromStart
    ##   the line Discretization distance from start   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def DistanceFromStart(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) DistanceFromStart
          the line Discretization distance from start   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) DistanceToEnd
    ##   the line Discretization distance to end   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def DistanceToEnd(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) DistanceToEnd
          the line Discretization distance to end   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Height
    ##   the height value   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Height(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Height
          the height value   
            
         
        """
        pass
    
    ## Getter for property: (@link HeightType NXOpen.CAE.Connections.HeightType@endlink) HeightType
    ##   the connection height type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return HeightType
    @property
    def HeightType(self) -> HeightType:
        """
        Getter for property: (@link HeightType NXOpen.CAE.Connections.HeightType@endlink) HeightType
          the connection height type   
            
         
        """
        pass
    
    ## Setter for property: (@link HeightType NXOpen.CAE.Connections.HeightType@endlink) HeightType

    ##   the connection height type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @HeightType.setter
    def HeightType(self, heightType: HeightType):
        """
        Setter for property: (@link HeightType NXOpen.CAE.Connections.HeightType@endlink) HeightType
          the connection height type   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) LengthStep
    ##   the line Discretization length step   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def LengthStep(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) LengthStep
          the line Discretization length step   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.PhysicalMaterial NXOpen.PhysicalMaterial@endlink) Material
    ##   the connection material   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.PhysicalMaterial
    @property
    def Material(self) -> NXOpen.PhysicalMaterial:
        """
        Getter for property: (@link NXOpen.PhysicalMaterial NXOpen.PhysicalMaterial@endlink) Material
          the connection material   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.PhysicalMaterial NXOpen.PhysicalMaterial@endlink) Material

    ##   the connection material   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @Material.setter
    def Material(self, material: NXOpen.PhysicalMaterial):
        """
        Setter for property: (@link NXOpen.PhysicalMaterial NXOpen.PhysicalMaterial@endlink) Material
          the connection material   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxAngleBetweenNormals
    ##   the maximum angle of normals with the projection surface   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def MaxAngleBetweenNormals(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxAngleBetweenNormals
          the maximum angle of normals with the projection surface   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxDistCGToElemCG
    ##   the maximum distance from definition point to center of support element   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def MaxDistCGToElemCG(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxDistCGToElemCG
          the maximum distance from definition point to center of support element   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxLengthStep
    ##   the line Discretization max length step   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def MaxLengthStep(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxLengthStep
          the line Discretization max length step   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxNormalDistCGToFlanges
    ##   the maximum normal distance from definition point to center of element   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def MaxNormalDistCGToFlanges(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxNormalDistCGToFlanges
          the maximum normal distance from definition point to center of element   
            
         
        """
        pass
    
    ## Getter for property: (int) NumberOfDiscretizationPoints
    ##   the number of connections   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return int
    @property
    def NumberOfDiscretizationPoints(self) -> int:
        """
        Getter for property: (int) NumberOfDiscretizationPoints
          the number of connections   
            
         
        """
        pass
    
    ## Setter for property: (int) NumberOfDiscretizationPoints

    ##   the number of connections   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @NumberOfDiscretizationPoints.setter
    def NumberOfDiscretizationPoints(self, num: int):
        """
        Setter for property: (int) NumberOfDiscretizationPoints
          the number of connections   
            
         
        """
        pass
    
    ## Getter for property: (int) NumberOfFlanges
    ##   the number of flanges.  
    ##    When changing the number of flanges this is not applied till an update is performed by calling @link Update::DoUpdate Update::DoUpdate@endlink    
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return int
    @property
    def NumberOfFlanges(self) -> int:
        """
        Getter for property: (int) NumberOfFlanges
          the number of flanges.  
           When changing the number of flanges this is not applied till an update is performed by calling @link Update::DoUpdate Update::DoUpdate@endlink    
         
        """
        pass
    
    ## Setter for property: (int) NumberOfFlanges

    ##   the number of flanges.  
    ##    When changing the number of flanges this is not applied till an update is performed by calling @link Update::DoUpdate Update::DoUpdate@endlink    
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @NumberOfFlanges.setter
    def NumberOfFlanges(self, numberOfFlanges: int):
        """
        Setter for property: (int) NumberOfFlanges
          the number of flanges.  
           When changing the number of flanges this is not applied till an update is performed by calling @link Update::DoUpdate Update::DoUpdate@endlink    
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ProjectTolerance
    ##   the projection tolerance   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def ProjectTolerance(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ProjectTolerance
          the projection tolerance   
            
         
        """
        pass
    
    ## Getter for property: (str) TableFile
    ##   the table file used to compute the diameter   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return str
    @property
    def TableFile(self) -> str:
        """
        Getter for property: (str) TableFile
          the table file used to compute the diameter   
            
         
        """
        pass
    
    ## Setter for property: (str) TableFile

    ##   the table file used to compute the diameter   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @TableFile.setter
    def TableFile(self, tableFile: str):
        """
        Setter for property: (str) TableFile
          the table file used to compute the diameter   
            
         
        """
        pass
    
    ## Getter for property: (bool) UseMaxLengthStep
    ##   the usage of max length step   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return bool
    @property
    def UseMaxLengthStep(self) -> bool:
        """
        Getter for property: (bool) UseMaxLengthStep
          the usage of max length step   
            
         
        """
        pass
    
    ## Setter for property: (bool) UseMaxLengthStep

    ##   the usage of max length step   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @UseMaxLengthStep.setter
    def UseMaxLengthStep(self, use: bool):
        """
        Setter for property: (bool) UseMaxLengthStep
          the usage of max length step   
            
         
        """
        pass
    
    ## Getter for property: (bool) UseOriginalNodesOfConnection
    ##   the usage of original nodes of connection   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return bool
    @property
    def UseOriginalNodesOfConnection(self) -> bool:
        """
        Getter for property: (bool) UseOriginalNodesOfConnection
          the usage of original nodes of connection   
            
         
        """
        pass
    
    ## Setter for property: (bool) UseOriginalNodesOfConnection

    ##   the usage of original nodes of connection   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @UseOriginalNodesOfConnection.setter
    def UseOriginalNodesOfConnection(self, use: bool):
        """
        Setter for property: (bool) UseOriginalNodesOfConnection
          the usage of original nodes of connection   
            
         
        """
        pass
    
import NXOpen
##  Composer connection. Use this interface to set/get properties and parameters of the spot weld connection.  
## 
##   <br>  Created in NX12.0.0  <br> 

class ComponentData(NXOpen.TaggedObject): 
    """ Composer connection. Use this interface to set/get properties and parameters of the spot weld connection.  """


    ## Getter for property: (str) ComponentName
    ##   the component name    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return str
    @property
    def ComponentName(self) -> str:
        """
        Getter for property: (str) ComponentName
          the component name    
            
         
        """
        pass
    
    ## Setter for property: (str) ComponentName

    ##   the component name    
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @ComponentName.setter
    def ComponentName(self, name: str):
        """
        Setter for property: (str) ComponentName
          the component name    
            
         
        """
        pass
    
    ## Getter for property: (str) ConnectionPointsPath
    ##   the connection points path    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return str
    @property
    def ConnectionPointsPath(self) -> str:
        """
        Getter for property: (str) ConnectionPointsPath
          the connection points path    
            
         
        """
        pass
    
    ## Setter for property: (str) ConnectionPointsPath

    ##   the connection points path    
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @ConnectionPointsPath.setter
    def ConnectionPointsPath(self, connectionPointsPath: str):
        """
        Setter for property: (str) ConnectionPointsPath
          the connection points path    
            
         
        """
        pass
    
    ## Getter for property: (str) FilePath
    ##   the file path    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return str
    @property
    def FilePath(self) -> str:
        """
        Getter for property: (str) FilePath
          the file path    
            
         
        """
        pass
    
    ## Setter for property: (str) FilePath

    ##   the file path    
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @FilePath.setter
    def FilePath(self, path: str):
        """
        Setter for property: (str) FilePath
          the file path    
            
         
        """
        pass
    
    ## Getter for property: (str) ImportedConnectionPointsPath
    ##   the imported connection points path    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return str
    @property
    def ImportedConnectionPointsPath(self) -> str:
        """
        Getter for property: (str) ImportedConnectionPointsPath
          the imported connection points path    
            
         
        """
        pass
    
    ## Setter for property: (str) ImportedConnectionPointsPath

    ##   the imported connection points path    
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @ImportedConnectionPointsPath.setter
    def ImportedConnectionPointsPath(self, importedConnPointsPath: str):
        """
        Setter for property: (str) ImportedConnectionPointsPath
          the imported connection points path    
            
         
        """
        pass
    
    ## Getter for property: (str) MeshPath
    ##   the mesh path    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return str
    @property
    def MeshPath(self) -> str:
        """
        Getter for property: (str) MeshPath
          the mesh path    
            
         
        """
        pass
    
    ## Setter for property: (str) MeshPath

    ##   the mesh path    
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @MeshPath.setter
    def MeshPath(self, meshPath: str):
        """
        Setter for property: (str) MeshPath
          the mesh path    
            
         
        """
        pass
    
    ## Getter for property: (str) RepresentationFilePath
    ##   the component representation path    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return str
    @property
    def RepresentationFilePath(self) -> str:
        """
        Getter for property: (str) RepresentationFilePath
          the component representation path    
            
         
        """
        pass
    
    ## Setter for property: (str) RepresentationFilePath

    ##   the component representation path    
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @RepresentationFilePath.setter
    def RepresentationFilePath(self, representationTypeFilePath: str):
        """
        Setter for property: (str) RepresentationFilePath
          the component representation path    
            
         
        """
        pass
    
    ## Getter for property: (str) RepresentationType
    ##   the component Representation Type    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return str
    @property
    def RepresentationType(self) -> str:
        """
        Getter for property: (str) RepresentationType
          the component Representation Type    
            
         
        """
        pass
    
    ## Setter for property: (str) RepresentationType

    ##   the component Representation Type    
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @RepresentationType.setter
    def RepresentationType(self, representationType: str):
        """
        Setter for property: (str) RepresentationType
          the component Representation Type    
            
         
        """
        pass
    
    ## Getter for property: (str) SolverType
    ##   the component Solver Type    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return str
    @property
    def SolverType(self) -> str:
        """
        Getter for property: (str) SolverType
          the component Solver Type    
            
         
        """
        pass
    
    ## Setter for property: (str) SolverType

    ##   the component Solver Type    
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @SolverType.setter
    def SolverType(self, solverType: str):
        """
        Setter for property: (str) SolverType
          the component Solver Type    
            
         
        """
        pass
    
##  composer Connection type 
##  None 
class ComposerConnectionType(Enum):
    """
    Members Include: <NotSet> <Bolt> <Spring> <Latch> <Bushing> <BumpStop> <Kinematic> <WeatherStrip> <SeamWeld> <Adhesive> <SpotWeld> <Bar>
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
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> ComposerConnectionType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


import NXOpen
##  Composer connection. Use this interface to set/get/create properties and set/get parameters of the composer.  
## 
##   <br>  Created in NX12.0.0  <br> 

class ComposerData(NXOpen.TaggedObject): 
    """ Composer connection. Use this interface to set/get/create properties and set/get parameters of the composer.  """


    ## Getter for property: (str) AssemblyName
    ##   the assembly name    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return str
    @property
    def AssemblyName(self) -> str:
        """
        Getter for property: (str) AssemblyName
          the assembly name    
            
         
        """
        pass
    
    ## Setter for property: (str) AssemblyName

    ##   the assembly name    
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @AssemblyName.setter
    def AssemblyName(self, assemblyName: str):
        """
        Setter for property: (str) AssemblyName
          the assembly name    
            
         
        """
        pass
    
    ## Getter for property: (str) ComponentUnitSystem
    ##   the component unit system    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return str
    @property
    def ComponentUnitSystem(self) -> str:
        """
        Getter for property: (str) ComponentUnitSystem
          the component unit system    
            
         
        """
        pass
    
    ## Setter for property: (str) ComponentUnitSystem

    ##   the component unit system    
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @ComponentUnitSystem.setter
    def ComponentUnitSystem(self, componentUnitSystem: str):
        """
        Setter for property: (str) ComponentUnitSystem
          the component unit system    
            
         
        """
        pass
    
    ## Getter for property: (str) InputFileDir
    ##   the input file direction    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return str
    @property
    def InputFileDir(self) -> str:
        """
        Getter for property: (str) InputFileDir
          the input file direction    
            
         
        """
        pass
    
    ## Setter for property: (str) InputFileDir

    ##   the input file direction    
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @InputFileDir.setter
    def InputFileDir(self, inputFileDir: str):
        """
        Setter for property: (str) InputFileDir
          the input file direction    
            
         
        """
        pass
    
    ## Getter for property: (str) MaterialDBDir
    ##   the material file direction    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return str
    @property
    def MaterialDBDir(self) -> str:
        """
        Getter for property: (str) MaterialDBDir
          the material file direction    
            
         
        """
        pass
    
    ## Setter for property: (str) MaterialDBDir

    ##   the material file direction    
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @MaterialDBDir.setter
    def MaterialDBDir(self, materialDBDir: str):
        """
        Setter for property: (str) MaterialDBDir
          the material file direction    
            
         
        """
        pass
    
    ## Getter for property: (str) OutputFileDir
    ##   the output file direction    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return str
    @property
    def OutputFileDir(self) -> str:
        """
        Getter for property: (str) OutputFileDir
          the output file direction    
            
         
        """
        pass
    
    ## Setter for property: (str) OutputFileDir

    ##   the output file direction    
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @OutputFileDir.setter
    def OutputFileDir(self, outputFileDir: str):
        """
        Setter for property: (str) OutputFileDir
          the output file direction    
            
         
        """
        pass
    
    ## Getter for property: (int) StartNumAxisSystems
    ##   the start axis number    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return int
    @property
    def StartNumAxisSystems(self) -> int:
        """
        Getter for property: (int) StartNumAxisSystems
          the start axis number    
            
         
        """
        pass
    
    ## Setter for property: (int) StartNumAxisSystems

    ##   the start axis number    
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @StartNumAxisSystems.setter
    def StartNumAxisSystems(self, startNumAxisSystems: int):
        """
        Setter for property: (int) StartNumAxisSystems
          the start axis number    
            
         
        """
        pass
    
    ## Getter for property: (int) StartNumNodeAndElement
    ##   the start node and element number    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return int
    @property
    def StartNumNodeAndElement(self) -> int:
        """
        Getter for property: (int) StartNumNodeAndElement
          the start node and element number    
            
         
        """
        pass
    
    ## Setter for property: (int) StartNumNodeAndElement

    ##   the start node and element number    
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @StartNumNodeAndElement.setter
    def StartNumNodeAndElement(self, startNumNodeAndElement: int):
        """
        Setter for property: (int) StartNumNodeAndElement
          the start node and element number    
            
         
        """
        pass
    
    ## Getter for property: (int) StartNumProperties
    ##   the start properties number    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return int
    @property
    def StartNumProperties(self) -> int:
        """
        Getter for property: (int) StartNumProperties
          the start properties number    
            
         
        """
        pass
    
    ## Setter for property: (int) StartNumProperties

    ##   the start properties number    
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @StartNumProperties.setter
    def StartNumProperties(self, startNumProperties: int):
        """
        Setter for property: (int) StartNumProperties
          the start properties number    
            
         
        """
        pass
    
    ##  Create component. 
    ##  @return component (@link ComponentData NXOpen.CAE.Connections.ComponentData@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    def CreateComponent(composerData: ComposerData) -> ComponentData:
        """
         Create component. 
         @return component (@link ComponentData NXOpen.CAE.Connections.ComponentData@endlink): .
        """
        pass
    
    ##  Create component. 
    ##  @return connection (@link ConnectionData NXOpen.CAE.Connections.ConnectionData@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    def CreateConnection(composerData: ComposerData) -> ConnectionData:
        """
         Create component. 
         @return connection (@link ConnectionData NXOpen.CAE.Connections.ConnectionData@endlink): .
        """
        pass
    
    ##  Gets components. 
    ##  @return components (@link ComponentData List[NXOpen.CAE.Connections.ComponentData]@endlink): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetComponents(composerData: ComposerData) -> List[ComponentData]:
        """
         Gets components. 
         @return components (@link ComponentData List[NXOpen.CAE.Connections.ComponentData]@endlink): .
        """
        pass
    
    ##  Gets connections 
    ##  @return connections (@link ConnectionData List[NXOpen.CAE.Connections.ConnectionData]@endlink): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetConnections(composerData: ComposerData) -> List[ConnectionData]:
        """
         Gets connections 
         @return connections (@link ConnectionData List[NXOpen.CAE.Connections.ConnectionData]@endlink): .
        """
        pass
    
    ##  Sets components. 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ## <param name="components"> (@link ComponentData List[NXOpen.CAE.Connections.ComponentData]@endlink) </param>
    def SetComponents(composerData: ComposerData, components: List[ComponentData]) -> None:
        """
         Sets components. 
        """
        pass
    
    ##  Sets connections 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ## <param name="connections"> (@link ConnectionData List[NXOpen.CAE.Connections.ConnectionData]@endlink) </param>
    def SetConnections(composerData: ComposerData, connections: List[ConnectionData]) -> None:
        """
         Sets connections 
        """
        pass
    
import NXOpen
##  ComposerTool.   <br> To obtain an instance of this class, refer to @link NXOpen::Session  NXOpen::Session @endlink  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class ComposerTool(NXOpen.Object): 
    """ ComposerTool.  """


    ##  CreateComposer  
    ##  @return composer (@link Composer NXOpen.CAE.Connections.Composer@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: sc_nv_comp (" Simcenter NVH Composer") OR nx_masterfem ("Finite Element Modeling") OR sc_gso_comp (" Simcenter NVH Composer") OR sc_gso_creation (" Simcenter GSO BIW Creation environment")
    def CreateComposer() -> Composer:
        """
         CreateComposer  
         @return composer (@link Composer NXOpen.CAE.Connections.Composer@endlink): .
        """
        pass
    
import NXOpen
import NXOpen.CAE
##  Composer. Use this interface to set/get/create properties and set/get parameters of the composer.  
## 
##   <br>  Created in NX12.0.0  <br> 

class Composer(NXOpen.TaggedObject): 
    """ Composer. Use this interface to set/get/create properties and set/get parameters of the composer.  """


    ## Getter for property: (@link ComposerData NXOpen.CAE.Connections.ComposerData@endlink) ComposerData
    ##   the composer data    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return ComposerData
    @property
    def ComposerData(self) -> ComposerData:
        """
        Getter for property: (@link ComposerData NXOpen.CAE.Connections.ComposerData@endlink) ComposerData
          the composer data    
            
         
        """
        pass
    
    ## Setter for property: (@link ComposerData NXOpen.CAE.Connections.ComposerData@endlink) ComposerData

    ##   the composer data    
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @ComposerData.setter
    def ComposerData(self, composerData: ComposerData):
        """
        Setter for property: (@link ComposerData NXOpen.CAE.Connections.ComposerData@endlink) ComposerData
          the composer data    
            
         
        """
        pass
    
    ## Getter for property: (@link ConnectionDBData NXOpen.CAE.Connections.ConnectionDBData@endlink) ConnectionDBData
    ##   the connection db data    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return ConnectionDBData
    @property
    def ConnectionDBData(self) -> ConnectionDBData:
        """
        Getter for property: (@link ConnectionDBData NXOpen.CAE.Connections.ConnectionDBData@endlink) ConnectionDBData
          the connection db data    
            
         
        """
        pass
    
    ## Setter for property: (@link ConnectionDBData NXOpen.CAE.Connections.ConnectionDBData@endlink) ConnectionDBData

    ##   the connection db data    
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @ConnectionDBData.setter
    def ConnectionDBData(self, connectionDBData: ConnectionDBData):
        """
        Setter for property: (@link ConnectionDBData NXOpen.CAE.Connections.ConnectionDBData@endlink) ConnectionDBData
          the connection db data    
            
         
        """
        pass
    
    ##  CheckAssemblyConnections  
    ##  @return results (List[str]): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    @staticmethod
    def CheckAssemblyConnections(composer: Composer) -> List[str]:
        """
         CheckAssemblyConnections  
         @return results (List[str]): .
        """
        pass
    
    ##  CheckAssemblyDocumentConnections  
    ##  @return results (List[str]): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ## <param name="documentName"> (str) </param>
    def CheckAssemblyDocumentConnections(composer: Composer, documentName: str) -> List[str]:
        """
         CheckAssemblyDocumentConnections  
         @return results (List[str]): .
        """
        pass
    
    ##  Create composer data. 
    ##  @return composerData (@link ComposerData NXOpen.CAE.Connections.ComposerData@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    def CreateComposerData(composer: Composer) -> ComposerData:
        """
         Create composer data. 
         @return composerData (@link ComposerData NXOpen.CAE.Connections.ComposerData@endlink): .
        """
        pass
    
    ##  Destroy the composer object 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer") OR sc_gso_creation (" Simcenter GSO BIW Creation environment") OR nx_masterfem ("Finite Element Modeling")
    @staticmethod
    def Destroy(composer: Composer) -> None:
        """
         Destroy the composer object 
        """
        pass
    
    ##  Export HardPoint To Xml 
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ## <param name="tWorkPart"> (@link NXOpen.CAE.CaePart NXOpen.CAE.CaePart@endlink) </param>
    ## <param name="tUnit"> (@link NXOpen.Unit NXOpen.Unit@endlink) </param>
    ## <param name="file"> (str) </param>
    def ExportHardPointToXml(pComposer: Composer, tWorkPart: NXOpen.CAE.CaePart, tUnit: NXOpen.Unit, file: str) -> None:
        """
         Export HardPoint To Xml 
        """
        pass
    
    ##  GetAxisFromAlias  
    ##  @return axes (@link NXOpen.CoordinateSystem List[NXOpen.CoordinateSystem]@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ## <param name="axisAlias"> (str) </param>
    def GetAxisFromAlias(composer: Composer, axisAlias: str) -> List[NXOpen.CoordinateSystem]:
        """
         GetAxisFromAlias  
         @return axes (@link NXOpen.CoordinateSystem List[NXOpen.CoordinateSystem]@endlink): .
        """
        pass
    
    ##  Get the intermediate connection representations of lumped mass connections loaded from external file.
    ##  @return oConnections (@link LMIEConnection List[NXOpen.CAE.Connections.LMIEConnection]@endlink):  The intermediate connection representations .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    @staticmethod
    def GetLumpedMassData(composer: Composer) -> List[LMIEConnection]:
        """
         Get the intermediate connection representations of lumped mass connections loaded from external file.
         @return oConnections (@link LMIEConnection List[NXOpen.CAE.Connections.LMIEConnection]@endlink):  The intermediate connection representations .
        """
        pass
    
    ##  Get MAT1 and MAT8 data from bdf file
    ##  @return listOfMaterialsDataResults (List[str]): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: sc_gso_creation (" Simcenter GSO BIW Creation environment")
    ## 
    ## <param name="inputBdfFilePath"> (str) </param>
    def GetMaterialsData(composer: Composer, inputBdfFilePath: str) -> List[str]:
        """
         Get MAT1 and MAT8 data from bdf file
         @return listOfMaterialsDataResults (List[str]): .
        """
        pass
    
    ##  GetMeshPartFromPID  
    ##  @return meshParts (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ## <param name="pid"> (int) </param>
    def GetMeshPartFromPID(composer: Composer, pid: int) -> List[NXOpen.TaggedObject]:
        """
         GetMeshPartFromPID  
         @return meshParts (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink): .
        """
        pass
    
    ##  GetMeshPartInContextFromPID  
    ##  @return meshParts (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink): .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ## <param name="tWorkPart"> (@link NXOpen.CAE.CaePart NXOpen.CAE.CaePart@endlink) </param>
    ## <param name="pid"> (int) </param>
    def GetMeshPartInContextFromPID(composer: Composer, tWorkPart: NXOpen.CAE.CaePart, pid: int) -> List[NXOpen.TaggedObject]:
        """
         GetMeshPartInContextFromPID  
         @return meshParts (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink): .
        """
        pass
    
    ##  Import HardPoint From Excel and Modify its Node Label 
    ##  @return selrecipes (@link NXOpen.CAE.SelectionRecipe List[NXOpen.CAE.SelectionRecipe]@endlink): .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: sc_gso_creation (" Simcenter GSO BIW Creation environment")
    ## 
    ## <param name="tWorkPart"> (@link NXOpen.CAE.CaePart NXOpen.CAE.CaePart@endlink) </param>
    ## <param name="file"> (str) </param>
    def ImportAndModifyHardPointLabel(pComposer: Composer, tWorkPart: NXOpen.CAE.CaePart, file: str) -> List[NXOpen.CAE.SelectionRecipe]:
        """
         Import HardPoint From Excel and Modify its Node Label 
         @return selrecipes (@link NXOpen.CAE.SelectionRecipe List[NXOpen.CAE.SelectionRecipe]@endlink): .
        """
        pass
    
    ##  Import HardPoint From Xml if does not exist and replace/update it otherwise
    ##  @return A tuple consisting of (selrecipes, updatedSelrecipes). 
    ##  - selrecipes is: @link NXOpen.CAE.SelectionRecipe List[NXOpen.CAE.SelectionRecipe]@endlink. Array of created recipe tags .
    ##  - updatedSelrecipes is: @link NXOpen.CAE.SelectionRecipe List[NXOpen.CAE.SelectionRecipe]@endlink. Array of replaced recipe tags .

    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##  I - The work part tag 
    @staticmethod
    def ImportAndUpdateHardPointFromXml(pComposer: Composer, tWorkPart: NXOpen.CAE.CaePart, file: str, isUpdate: bool) -> Tuple[List[NXOpen.CAE.SelectionRecipe], List[NXOpen.CAE.SelectionRecipe]]:
        """
         Import HardPoint From Xml if does not exist and replace/update it otherwise
         @return A tuple consisting of (selrecipes, updatedSelrecipes). 
         - selrecipes is: @link NXOpen.CAE.SelectionRecipe List[NXOpen.CAE.SelectionRecipe]@endlink. Array of created recipe tags .
         - updatedSelrecipes is: @link NXOpen.CAE.SelectionRecipe List[NXOpen.CAE.SelectionRecipe]@endlink. Array of replaced recipe tags .

        """
        pass
    
    ##  Migrate old XML format  
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ## <param name="file"> (str) </param>
    def MigrateToHardPointFile(pComposer: Composer, file: str) -> None:
        """
         Migrate old XML format  
        """
        pass
    
    ##  ReadAssemblyDefinition  
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ## <param name="filePath"> (str) </param>
    def ReadAssemblyDefinition(composer: Composer, filePath: str) -> None:
        """
         ReadAssemblyDefinition  
        """
        pass
    
    ##  ReadConnectionsDB  
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ## <param name="filePath"> (str) </param>
    def ReadConnectionsDB(composer: Composer, filePath: str) -> None:
        """
         ReadConnectionsDB  
        """
        pass
    
    ##  SearchBoltComponentAndPIDs  
    ##  @return listOfConnPIDsResults (List[str]): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ## <param name="documentName"> (str) </param>
    def SearchBoltComponentAndPIDs(composer: Composer, documentName: str) -> List[str]:
        """
         SearchBoltComponentAndPIDs  
         @return listOfConnPIDsResults (List[str]): .
        """
        pass
    
    ##  SearchPIDs  
    ##  @return A tuple consisting of (isAssemblyOpen, listOfConnPIDsResults, listOfMassPIDsResults). 
    ##  - isAssemblyOpen is: bool.
    ##  - listOfConnPIDsResults is: List[str].
    ##  - listOfMassPIDsResults is: List[str].

    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ## <param name="documentName"> (str) </param>
    @staticmethod
    def SearchPIDs(composer: Composer, documentName: str) -> Tuple[bool, List[str], List[str]]:
        """
         SearchPIDs  
         @return A tuple consisting of (isAssemblyOpen, listOfConnPIDsResults, listOfMassPIDsResults). 
         - isAssemblyOpen is: bool.
         - listOfConnPIDsResults is: List[str].
         - listOfMassPIDsResults is: List[str].

        """
        pass
    
    ##  Set the intermediate connection representations of lumped mass connections loaded from external file.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ##  The intermediate connection representations 
    def SetLumpedMassData(composer: Composer, iConnections: List[LMIEConnection]) -> None:
        """
         Set the intermediate connection representations of lumped mass connections loaded from external file.
        """
        pass
    
    ##  WriteAssemblyDefinition  
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ## <param name="filePath"> (str) </param>
    def WriteAssemblyDefinition(composer: Composer, filePath: str) -> None:
        """
         WriteAssemblyDefinition  
        """
        pass
    
import NXOpen
##  Composer connection. Use this interface to set/get properties and parameters of the spot weld connection.  
## 
##   <br>  Created in NX12.0.0  <br> 

class ConnectionData(NXOpen.TaggedObject): 
    """ Composer connection. Use this interface to set/get properties and parameters of the spot weld connection.  """


    ## Getter for property: (@link ComponentData NXOpen.CAE.Connections.ComponentData@endlink) Comp1
    ##   the comp1    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return ComponentData
    @property
    def Comp1(self) -> ComponentData:
        """
        Getter for property: (@link ComponentData NXOpen.CAE.Connections.ComponentData@endlink) Comp1
          the comp1    
            
         
        """
        pass
    
    ## Setter for property: (@link ComponentData NXOpen.CAE.Connections.ComponentData@endlink) Comp1

    ##   the comp1    
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @Comp1.setter
    def Comp1(self, comp1: ComponentData):
        """
        Setter for property: (@link ComponentData NXOpen.CAE.Connections.ComponentData@endlink) Comp1
          the comp1    
            
         
        """
        pass
    
    ## Getter for property: (@link ComponentData NXOpen.CAE.Connections.ComponentData@endlink) Comp2
    ##   the comp2    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return ComponentData
    @property
    def Comp2(self) -> ComponentData:
        """
        Getter for property: (@link ComponentData NXOpen.CAE.Connections.ComponentData@endlink) Comp2
          the comp2    
            
         
        """
        pass
    
    ## Setter for property: (@link ComponentData NXOpen.CAE.Connections.ComponentData@endlink) Comp2

    ##   the comp2    
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @Comp2.setter
    def Comp2(self, comp2: ComponentData):
        """
        Setter for property: (@link ComponentData NXOpen.CAE.Connections.ComponentData@endlink) Comp2
          the comp2    
            
         
        """
        pass
    
    ## Getter for property: (@link ComponentData NXOpen.CAE.Connections.ComponentData@endlink) Comp3
    ##   the comp3    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return ComponentData
    @property
    def Comp3(self) -> ComponentData:
        """
        Getter for property: (@link ComponentData NXOpen.CAE.Connections.ComponentData@endlink) Comp3
          the comp3    
            
         
        """
        pass
    
    ## Setter for property: (@link ComponentData NXOpen.CAE.Connections.ComponentData@endlink) Comp3

    ##   the comp3    
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @Comp3.setter
    def Comp3(self, comp3: ComponentData):
        """
        Setter for property: (@link ComponentData NXOpen.CAE.Connections.ComponentData@endlink) Comp3
          the comp3    
            
         
        """
        pass
    
    ## Getter for property: (@link ComposerConnectionType NXOpen.CAE.Connections.ComposerConnectionType@endlink) ConnectionType
    ##   the connection type    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return ComposerConnectionType
    @property
    def ConnectionType(self) -> ComposerConnectionType:
        """
        Getter for property: (@link ComposerConnectionType NXOpen.CAE.Connections.ComposerConnectionType@endlink) ConnectionType
          the connection type    
            
         
        """
        pass
    
    ## Setter for property: (@link ComposerConnectionType NXOpen.CAE.Connections.ComposerConnectionType@endlink) ConnectionType

    ##   the connection type    
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @ConnectionType.setter
    def ConnectionType(self, type: ComposerConnectionType):
        """
        Setter for property: (@link ComposerConnectionType NXOpen.CAE.Connections.ComposerConnectionType@endlink) ConnectionType
          the connection type    
            
         
        """
        pass
    
    ## Getter for property: (str) DBItem
    ##   the db item    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return str
    @property
    def DBItem(self) -> str:
        """
        Getter for property: (str) DBItem
          the db item    
            
         
        """
        pass
    
    ## Setter for property: (str) DBItem

    ##   the db item    
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @DBItem.setter
    def DBItem(self, name: str):
        """
        Setter for property: (str) DBItem
          the db item    
            
         
        """
        pass
    
    ## Getter for property: (bool) Dof1
    ##   the dof1   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return bool
    @property
    def Dof1(self) -> bool:
        """
        Getter for property: (bool) Dof1
          the dof1   
            
         
        """
        pass
    
    ## Setter for property: (bool) Dof1

    ##   the dof1   
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @Dof1.setter
    def Dof1(self, name: bool):
        """
        Setter for property: (bool) Dof1
          the dof1   
            
         
        """
        pass
    
    ## Getter for property: (bool) Dof2
    ##   the dof2   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return bool
    @property
    def Dof2(self) -> bool:
        """
        Getter for property: (bool) Dof2
          the dof2   
            
         
        """
        pass
    
    ## Setter for property: (bool) Dof2

    ##   the dof2   
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @Dof2.setter
    def Dof2(self, name: bool):
        """
        Setter for property: (bool) Dof2
          the dof2   
            
         
        """
        pass
    
    ## Getter for property: (bool) Dof3
    ##   the dof3   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return bool
    @property
    def Dof3(self) -> bool:
        """
        Getter for property: (bool) Dof3
          the dof3   
            
         
        """
        pass
    
    ## Setter for property: (bool) Dof3

    ##   the dof3   
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @Dof3.setter
    def Dof3(self, name: bool):
        """
        Setter for property: (bool) Dof3
          the dof3   
            
         
        """
        pass
    
    ## Getter for property: (bool) Dof4
    ##   the dof4   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return bool
    @property
    def Dof4(self) -> bool:
        """
        Getter for property: (bool) Dof4
          the dof4   
            
         
        """
        pass
    
    ## Setter for property: (bool) Dof4

    ##   the dof4   
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @Dof4.setter
    def Dof4(self, name: bool):
        """
        Setter for property: (bool) Dof4
          the dof4   
            
         
        """
        pass
    
    ## Getter for property: (bool) Dof5
    ##   the dof5   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return bool
    @property
    def Dof5(self) -> bool:
        """
        Getter for property: (bool) Dof5
          the dof5   
            
         
        """
        pass
    
    ## Setter for property: (bool) Dof5

    ##   the dof5   
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @Dof5.setter
    def Dof5(self, name: bool):
        """
        Setter for property: (bool) Dof5
          the dof5   
            
         
        """
        pass
    
    ## Getter for property: (bool) Dof6
    ##   the dof6   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return bool
    @property
    def Dof6(self) -> bool:
        """
        Getter for property: (bool) Dof6
          the dof6   
            
         
        """
        pass
    
    ## Setter for property: (bool) Dof6

    ##   the dof6   
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @Dof6.setter
    def Dof6(self, name: bool):
        """
        Setter for property: (bool) Dof6
          the dof6   
            
         
        """
        pass
    
    ## Getter for property: (float) ExpansionRadius1
    ##   the expansion radius1   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return float
    @property
    def ExpansionRadius1(self) -> float:
        """
        Getter for property: (float) ExpansionRadius1
          the expansion radius1   
            
         
        """
        pass
    
    ## Setter for property: (float) ExpansionRadius1

    ##   the expansion radius1   
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @ExpansionRadius1.setter
    def ExpansionRadius1(self, expansionRadius1: float):
        """
        Setter for property: (float) ExpansionRadius1
          the expansion radius1   
            
         
        """
        pass
    
    ## Getter for property: (float) ExpansionRadius2
    ##   the expansion radius2   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return float
    @property
    def ExpansionRadius2(self) -> float:
        """
        Getter for property: (float) ExpansionRadius2
          the expansion radius2   
            
         
        """
        pass
    
    ## Setter for property: (float) ExpansionRadius2

    ##   the expansion radius2   
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @ExpansionRadius2.setter
    def ExpansionRadius2(self, expansionRadius2: float):
        """
        Setter for property: (float) ExpansionRadius2
          the expansion radius2   
            
         
        """
        pass
    
    ## Getter for property: (float) ExpansionRadiusFactor1
    ##   the expansion radius factor1   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return float
    @property
    def ExpansionRadiusFactor1(self) -> float:
        """
        Getter for property: (float) ExpansionRadiusFactor1
          the expansion radius factor1   
            
         
        """
        pass
    
    ## Setter for property: (float) ExpansionRadiusFactor1

    ##   the expansion radius factor1   
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @ExpansionRadiusFactor1.setter
    def ExpansionRadiusFactor1(self, expansionRadiusFactor1: float):
        """
        Setter for property: (float) ExpansionRadiusFactor1
          the expansion radius factor1   
            
         
        """
        pass
    
    ## Getter for property: (float) ExpansionRadiusFactor2
    ##   the expansion radius factor2   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return float
    @property
    def ExpansionRadiusFactor2(self) -> float:
        """
        Getter for property: (float) ExpansionRadiusFactor2
          the expansion radius factor2   
            
         
        """
        pass
    
    ## Setter for property: (float) ExpansionRadiusFactor2

    ##   the expansion radius factor2   
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @ExpansionRadiusFactor2.setter
    def ExpansionRadiusFactor2(self, expansionRadiusFactor2: float):
        """
        Setter for property: (float) ExpansionRadiusFactor2
          the expansion radius factor2   
            
         
        """
        pass
    
    ## Getter for property: (float) FlangeSearchTolerance1
    ##   the expansion radius factor1   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return float
    @property
    def FlangeSearchTolerance1(self) -> float:
        """
        Getter for property: (float) FlangeSearchTolerance1
          the expansion radius factor1   
            
         
        """
        pass
    
    ## Setter for property: (float) FlangeSearchTolerance1

    ##   the expansion radius factor1   
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @FlangeSearchTolerance1.setter
    def FlangeSearchTolerance1(self, flangeSearchTolerance1: float):
        """
        Setter for property: (float) FlangeSearchTolerance1
          the expansion radius factor1   
            
         
        """
        pass
    
    ## Getter for property: (float) FlangeSearchTolerance2
    ##   the expansion radius factor2   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return float
    @property
    def FlangeSearchTolerance2(self) -> float:
        """
        Getter for property: (float) FlangeSearchTolerance2
          the expansion radius factor2   
            
         
        """
        pass
    
    ## Setter for property: (float) FlangeSearchTolerance2

    ##   the expansion radius factor2   
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @FlangeSearchTolerance2.setter
    def FlangeSearchTolerance2(self, flangeSearchTolerance2: float):
        """
        Setter for property: (float) FlangeSearchTolerance2
          the expansion radius factor2   
            
         
        """
        pass
    
    ## Getter for property: (str) FlangeType1
    ##   the flange type1    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return str
    @property
    def FlangeType1(self) -> str:
        """
        Getter for property: (str) FlangeType1
          the flange type1    
            
         
        """
        pass
    
    ## Setter for property: (str) FlangeType1

    ##   the flange type1    
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @FlangeType1.setter
    def FlangeType1(self, flangeType1: str):
        """
        Setter for property: (str) FlangeType1
          the flange type1    
            
         
        """
        pass
    
    ## Getter for property: (str) FlangeType2
    ##   the flange type2    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return str
    @property
    def FlangeType2(self) -> str:
        """
        Getter for property: (str) FlangeType2
          the flange type2    
            
         
        """
        pass
    
    ## Setter for property: (str) FlangeType2

    ##   the flange type2    
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @FlangeType2.setter
    def FlangeType2(self, flangeType2: str):
        """
        Setter for property: (str) FlangeType2
          the flange type2    
            
         
        """
        pass
    
    ## Getter for property: (float) HeadDiameter
    ##   the head diameter    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return float
    @property
    def HeadDiameter(self) -> float:
        """
        Getter for property: (float) HeadDiameter
          the head diameter    
            
         
        """
        pass
    
    ## Setter for property: (float) HeadDiameter

    ##   the head diameter    
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @HeadDiameter.setter
    def HeadDiameter(self, headDiameter: float):
        """
        Setter for property: (float) HeadDiameter
          the head diameter    
            
         
        """
        pass
    
    ## Getter for property: (float) LengthStep
    ##   the expansion radius factor2   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return float
    @property
    def LengthStep(self) -> float:
        """
        Getter for property: (float) LengthStep
          the expansion radius factor2   
            
         
        """
        pass
    
    ## Setter for property: (float) LengthStep

    ##   the expansion radius factor2   
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @LengthStep.setter
    def LengthStep(self, lengthStep: float):
        """
        Setter for property: (float) LengthStep
          the expansion radius factor2   
            
         
        """
        pass
    
    ## Getter for property: (str) LinePart1
    ##   the line part1    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return str
    @property
    def LinePart1(self) -> str:
        """
        Getter for property: (str) LinePart1
          the line part1    
            
         
        """
        pass
    
    ## Setter for property: (str) LinePart1

    ##   the line part1    
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @LinePart1.setter
    def LinePart1(self, linePart: str):
        """
        Setter for property: (str) LinePart1
          the line part1    
            
         
        """
        pass
    
    ## Getter for property: (str) LinePart2
    ##   the line part2    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return str
    @property
    def LinePart2(self) -> str:
        """
        Getter for property: (str) LinePart2
          the line part2    
            
         
        """
        pass
    
    ## Setter for property: (str) LinePart2

    ##   the line part2    
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @LinePart2.setter
    def LinePart2(self, linePart: str):
        """
        Setter for property: (str) LinePart2
          the line part2    
            
         
        """
        pass
    
    ## Getter for property: (float) MaximumDistanceTolerance1
    ##   the maximum distance tolerance1    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return float
    @property
    def MaximumDistanceTolerance1(self) -> float:
        """
        Getter for property: (float) MaximumDistanceTolerance1
          the maximum distance tolerance1    
            
         
        """
        pass
    
    ## Setter for property: (float) MaximumDistanceTolerance1

    ##   the maximum distance tolerance1    
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @MaximumDistanceTolerance1.setter
    def MaximumDistanceTolerance1(self, maximumDistanceTolerance1: float):
        """
        Setter for property: (float) MaximumDistanceTolerance1
          the maximum distance tolerance1    
            
         
        """
        pass
    
    ## Getter for property: (float) MaximumDistanceTolerance2
    ##   the maximum distance tolerance2    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return float
    @property
    def MaximumDistanceTolerance2(self) -> float:
        """
        Getter for property: (float) MaximumDistanceTolerance2
          the maximum distance tolerance2    
            
         
        """
        pass
    
    ## Setter for property: (float) MaximumDistanceTolerance2

    ##   the maximum distance tolerance2    
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @MaximumDistanceTolerance2.setter
    def MaximumDistanceTolerance2(self, maximumDistanceTolerance2: float):
        """
        Setter for property: (float) MaximumDistanceTolerance2
          the maximum distance tolerance2    
            
         
        """
        pass
    
    ## Getter for property: (str) Name
    ##   the assembly name    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return str
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
          the assembly name    
            
         
        """
        pass
    
    ## Setter for property: (str) Name

    ##   the assembly name    
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
          the assembly name    
            
         
        """
        pass
    
    ## Getter for property: (str) SearchType1
    ##   the search type1    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return str
    @property
    def SearchType1(self) -> str:
        """
        Getter for property: (str) SearchType1
          the search type1    
            
         
        """
        pass
    
    ## Setter for property: (str) SearchType1

    ##   the search type1    
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @SearchType1.setter
    def SearchType1(self, searchType1: str):
        """
        Setter for property: (str) SearchType1
          the search type1    
            
         
        """
        pass
    
    ## Getter for property: (str) SearchType2
    ##   the search type2    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return str
    @property
    def SearchType2(self) -> str:
        """
        Getter for property: (str) SearchType2
          the search type2    
            
         
        """
        pass
    
    ## Setter for property: (str) SearchType2

    ##   the search type2    
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @SearchType2.setter
    def SearchType2(self, searchType2: str):
        """
        Setter for property: (str) SearchType2
          the search type2    
            
         
        """
        pass
    
    ## Getter for property: (float) ShankDiameter
    ##   the shank diameter    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return float
    @property
    def ShankDiameter(self) -> float:
        """
        Getter for property: (float) ShankDiameter
          the shank diameter    
            
         
        """
        pass
    
    ## Setter for property: (float) ShankDiameter

    ##   the shank diameter    
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @ShankDiameter.setter
    def ShankDiameter(self, shankDiameter: float):
        """
        Setter for property: (float) ShankDiameter
          the shank diameter    
            
         
        """
        pass
    
    ## Getter for property: (str) WCDFile
    ##   the WCD File    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return str
    @property
    def WCDFile(self) -> str:
        """
        Getter for property: (str) WCDFile
          the WCD File    
            
         
        """
        pass
    
    ## Setter for property: (str) WCDFile

    ##   the WCD File    
    ##     
    ##  
    ## Setter License requirements: sc_gso_10 (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @WCDFile.setter
    def WCDFile(self, wcdFile: str):
        """
        Setter for property: (str) WCDFile
          the WCD File    
            
         
        """
        pass
    
    ##  Gets axis. 
    ##  @return axis (str): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetAxis(connectionData: ConnectionData) -> str:
        """
         Gets axis. 
         @return axis (str): .
        """
        pass
    
    ##  Get Components1  
    ##  @return comps (@link ComponentData List[NXOpen.CAE.Connections.ComponentData]@endlink): .
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetComponents1(connectionData: ConnectionData) -> List[ComponentData]:
        """
         Get Components1  
         @return comps (@link ComponentData List[NXOpen.CAE.Connections.ComponentData]@endlink): .
        """
        pass
    
    ##  Get Components2  
    ##  @return comps (@link ComponentData List[NXOpen.CAE.Connections.ComponentData]@endlink): .
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetComponents2(connectionData: ConnectionData) -> List[ComponentData]:
        """
         Get Components2  
         @return comps (@link ComponentData List[NXOpen.CAE.Connections.ComponentData]@endlink): .
        """
        pass
    
    ##  Invalid dof 
    ##  @return invalidDOF (List[int]): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetInvalidDOF(connectionData: ConnectionData) -> List[int]:
        """
         Invalid dof 
         @return invalidDOF (List[int]): .
        """
        pass
    
    ##  Get line / FE edge recipe1  
    ##  @return lineFEEdgeRecipe1s (List[str]): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetLineFEEdgeRecipe1(connectionData: ConnectionData) -> List[str]:
        """
         Get line / FE edge recipe1  
         @return lineFEEdgeRecipe1s (List[str]): .
        """
        pass
    
    ##  Get line / FE edge recipe2  
    ##  @return lineFEEdgeRecipe2s (List[str]): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetLineFEEdgeRecipe2(connectionData: ConnectionData) -> List[str]:
        """
         Get line / FE edge recipe2  
         @return lineFEEdgeRecipe2s (List[str]): .
        """
        pass
    
    ##  Get pID1s 
    ##  @return pID1s (List[int]): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetPID1s(connectionData: ConnectionData) -> List[int]:
        """
         Get pID1s 
         @return pID1s (List[int]): .
        """
        pass
    
    ##  Get pID2s 
    ##  @return pID2s (List[int]): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetPID2s(connectionData: ConnectionData) -> List[int]:
        """
         Get pID2s 
         @return pID2s (List[int]): .
        """
        pass
    
    ##  Get pID3s 
    ##  @return pID3s (List[int]): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetPID3s(connectionData: ConnectionData) -> List[int]:
        """
         Get pID3s 
         @return pID3s (List[int]): .
        """
        pass
    
    ##  Get point name coord1  
    ##  @return pointNameCoord1s (List[str]): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetPointNameCoord1(connectionData: ConnectionData) -> List[str]:
        """
         Get point name coord1  
         @return pointNameCoord1s (List[str]): .
        """
        pass
    
    ##  Get point name coord2  
    ##  @return pointNameCoord2s (List[str]): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetPointNameCoord2(connectionData: ConnectionData) -> List[str]:
        """
         Get point name coord2  
         @return pointNameCoord2s (List[str]): .
        """
        pass
    
    ##  Get point name coord3  
    ##  @return pointNameCoord3s (List[str]): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetPointNameCoord3(connectionData: ConnectionData) -> List[str]:
        """
         Get point name coord3  
         @return pointNameCoord3s (List[str]): .
        """
        pass
    
    ##  Sets axis. 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ## <param name="axis"> (str) </param>
    def SetAxis(connectionData: ConnectionData, axis: str) -> None:
        """
         Sets axis. 
        """
        pass
    
    ##  Set Components1  
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ## <param name="comps"> (@link ComponentData List[NXOpen.CAE.Connections.ComponentData]@endlink) </param>
    def SetComponents1(connectionData: ConnectionData, comps: List[ComponentData]) -> None:
        """
         Set Components1  
        """
        pass
    
    ##  Set Components2  
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ## <param name="comps"> (@link ComponentData List[NXOpen.CAE.Connections.ComponentData]@endlink) </param>
    def SetComponents2(connectionData: ConnectionData, comps: List[ComponentData]) -> None:
        """
         Set Components2  
        """
        pass
    
    ##  Set line / FE edge recipe1  
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ## <param name="lineFEEdgeRecipe1s"> (List[str]) </param>
    def SetLineFEEdgeRecipe1(connectionData: ConnectionData, lineFEEdgeRecipe1s: List[str]) -> None:
        """
         Set line / FE edge recipe1  
        """
        pass
    
    ##  Set line / FE edge recipe1  
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ## <param name="lineFEEdgeRecipe2s"> (List[str]) </param>
    def SetLineFEEdgeRecipe2(connectionData: ConnectionData, lineFEEdgeRecipe2s: List[str]) -> None:
        """
         Set line / FE edge recipe1  
        """
        pass
    
    ##  Set pID1s 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ## <param name="pID1s"> (List[int]) </param>
    def SetPID1s(connectionData: ConnectionData, pID1s: List[int]) -> None:
        """
         Set pID1s 
        """
        pass
    
    ##  Set pID2s 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ## <param name="pID2s"> (List[int]) </param>
    def SetPID2s(connectionData: ConnectionData, pID2s: List[int]) -> None:
        """
         Set pID2s 
        """
        pass
    
    ##  Set pID3s 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ## <param name="pID3s"> (List[int]) </param>
    def SetPID3s(connectionData: ConnectionData, pID3s: List[int]) -> None:
        """
         Set pID3s 
        """
        pass
    
    ##  Set point name coord1  
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ## <param name="pointNameCoord1s"> (List[str]) </param>
    def SetPointNameCoord1(connectionData: ConnectionData, pointNameCoord1s: List[str]) -> None:
        """
         Set point name coord1  
        """
        pass
    
    ##  Set point name coord2  
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ## <param name="pointNameCoord2s"> (List[str]) </param>
    def SetPointNameCoord2(connectionData: ConnectionData, pointNameCoord2s: List[str]) -> None:
        """
         Set point name coord2  
        """
        pass
    
    ##  Set point name coord3  
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ## <param name="pointNameCoord3s"> (List[str]) </param>
    def SetPointNameCoord3(connectionData: ConnectionData, pointNameCoord3s: List[str]) -> None:
        """
         Set point name coord3  
        """
        pass
    
import NXOpen
##  Connection DB data. Use this interface to set/get properties and parameters of the connection DB data.  
## 
##   <br>  Created in NX12.0.0  <br> 

class ConnectionDBData(NXOpen.TaggedObject): 
    """ Connection DB data. Use this interface to set/get properties and parameters of the connection DB data.  """


    ##  Gets connection DB item datas. 
    ##  @return components (@link ConnectionDBItemData List[NXOpen.CAE.Connections.ConnectionDBItemData]@endlink): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetConnectionDBItemDatas(composerData: ConnectionDBData) -> List[ConnectionDBItemData]:
        """
         Gets connection DB item datas. 
         @return components (@link ConnectionDBItemData List[NXOpen.CAE.Connections.ConnectionDBItemData]@endlink): .
        """
        pass
    
    ##  Sets connection DB item datas. 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ## <param name="components"> (@link ConnectionDBItemData List[NXOpen.CAE.Connections.ConnectionDBItemData]@endlink) </param>
    def SetConnectionDBItemDatas(composerData: ConnectionDBData, components: List[ConnectionDBItemData]) -> None:
        """
         Sets connection DB item datas. 
        """
        pass
    
import NXOpen
##  Connection DB item data. Use this interface to set/get properties and parameters of the Connection DB item data.  
## 
##   <br>  Created in NX12.0.0  <br> 

class ConnectionDBItemData(NXOpen.TaggedObject): 
    """ Connection DB item data. Use this interface to set/get properties and parameters of the Connection DB item data.  """


    ## Getter for property: (float) AdhesiveWidth
    ##   the adhesive width    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def AdhesiveWidth(self) -> float:
        """
        Getter for property: (float) AdhesiveWidth
          the adhesive width    
            
         
        """
        pass
    
    ## Getter for property: (float) Height
    ##   the height    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def Height(self) -> float:
        """
        Getter for property: (float) Height
          the height    
            
         
        """
        pass
    
    ## Getter for property: (@link HeightType NXOpen.CAE.Connections.HeightType@endlink) HeightType
    ##   the height type    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return HeightType
    @property
    def HeightType(self) -> HeightType:
        """
        Getter for property: (@link HeightType NXOpen.CAE.Connections.HeightType@endlink) HeightType
          the height type    
            
         
        """
        pass
    
    ## Getter for property: (float) Mass
    ##   the mass    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return float
    @property
    def Mass(self) -> float:
        """
        Getter for property: (float) Mass
          the mass    
            
         
        """
        pass
    
    ## Setter for property: (float) Mass

    ##   the mass    
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @Mass.setter
    def Mass(self, mass: float):
        """
        Setter for property: (float) Mass
          the mass    
            
         
        """
        pass
    
    ## Getter for property: (int) MaterialID
    ##   the material ID    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return int
    @property
    def MaterialID(self) -> int:
        """
        Getter for property: (int) MaterialID
          the material ID    
            
         
        """
        pass
    
    ## Setter for property: (int) MaterialID

    ##   the material ID    
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @MaterialID.setter
    def MaterialID(self, materialID: int):
        """
        Setter for property: (int) MaterialID
          the material ID    
            
         
        """
        pass
    
    ## Getter for property: (str) Name
    ##   the name    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return str
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
          the name    
            
         
        """
        pass
    
    ## Setter for property: (str) Name

    ##   the name    
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
          the name    
            
         
        """
        pass
    
    ## Getter for property: (float) ScrewDiameter
    ##   the screw diameter    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return float
    @property
    def ScrewDiameter(self) -> float:
        """
        Getter for property: (float) ScrewDiameter
          the screw diameter    
            
         
        """
        pass
    
    ## Setter for property: (float) ScrewDiameter

    ##   the screw diameter    
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @ScrewDiameter.setter
    def ScrewDiameter(self, screwDiameter: float):
        """
        Setter for property: (float) ScrewDiameter
          the screw diameter    
            
         
        """
        pass
    
    ## Getter for property: (float) StiffnessR
    ##   the stiffness R    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return float
    @property
    def StiffnessR(self) -> float:
        """
        Getter for property: (float) StiffnessR
          the stiffness R    
            
         
        """
        pass
    
    ## Setter for property: (float) StiffnessR

    ##   the stiffness R    
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @StiffnessR.setter
    def StiffnessR(self, stiffnessR: float):
        """
        Setter for property: (float) StiffnessR
          the stiffness R    
            
         
        """
        pass
    
    ## Getter for property: (float) StiffnessRR
    ##   the stiffness RR    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return float
    @property
    def StiffnessRR(self) -> float:
        """
        Getter for property: (float) StiffnessRR
          the stiffness RR    
            
         
        """
        pass
    
    ## Setter for property: (float) StiffnessRR

    ##   the stiffness RR    
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @StiffnessRR.setter
    def StiffnessRR(self, stiffnessRR: float):
        """
        Setter for property: (float) StiffnessRR
          the stiffness RR    
            
         
        """
        pass
    
    ## Getter for property: (float) StiffnessRS
    ##   the stiffness RS    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return float
    @property
    def StiffnessRS(self) -> float:
        """
        Getter for property: (float) StiffnessRS
          the stiffness RS    
            
         
        """
        pass
    
    ## Setter for property: (float) StiffnessRS

    ##   the stiffness RS    
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @StiffnessRS.setter
    def StiffnessRS(self, stiffnessRS: float):
        """
        Setter for property: (float) StiffnessRS
          the stiffness RS    
            
         
        """
        pass
    
    ## Getter for property: (float) StiffnessRX
    ##   the stiffness RX    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return float
    @property
    def StiffnessRX(self) -> float:
        """
        Getter for property: (float) StiffnessRX
          the stiffness RX    
            
         
        """
        pass
    
    ## Setter for property: (float) StiffnessRX

    ##   the stiffness RX    
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @StiffnessRX.setter
    def StiffnessRX(self, stiffnessRX: float):
        """
        Setter for property: (float) StiffnessRX
          the stiffness RX    
            
         
        """
        pass
    
    ## Getter for property: (float) StiffnessRY
    ##   the stiffness RY    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return float
    @property
    def StiffnessRY(self) -> float:
        """
        Getter for property: (float) StiffnessRY
          the stiffness RY    
            
         
        """
        pass
    
    ## Setter for property: (float) StiffnessRY

    ##   the stiffness RY    
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @StiffnessRY.setter
    def StiffnessRY(self, stiffnessRY: float):
        """
        Setter for property: (float) StiffnessRY
          the stiffness RY    
            
         
        """
        pass
    
    ## Getter for property: (float) StiffnessRZ
    ##   the stiffness RZ    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return float
    @property
    def StiffnessRZ(self) -> float:
        """
        Getter for property: (float) StiffnessRZ
          the stiffness RZ    
            
         
        """
        pass
    
    ## Setter for property: (float) StiffnessRZ

    ##   the stiffness RZ    
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @StiffnessRZ.setter
    def StiffnessRZ(self, stiffnessRZ: float):
        """
        Setter for property: (float) StiffnessRZ
          the stiffness RZ    
            
         
        """
        pass
    
    ## Getter for property: (float) StiffnessS
    ##   the stiffness RS    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return float
    @property
    def StiffnessS(self) -> float:
        """
        Getter for property: (float) StiffnessS
          the stiffness RS    
            
         
        """
        pass
    
    ## Setter for property: (float) StiffnessS

    ##   the stiffness RS    
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @StiffnessS.setter
    def StiffnessS(self, stiffnessS: float):
        """
        Setter for property: (float) StiffnessS
          the stiffness RS    
            
         
        """
        pass
    
    ## Getter for property: (@link ConnectionDBItemStiffnessType NXOpen.CAE.Connections.ConnectionDBItemStiffnessType@endlink) StiffnessType
    ##   the mass    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return ConnectionDBItemStiffnessType
    @property
    def StiffnessType(self) -> ConnectionDBItemStiffnessType:
        """
        Getter for property: (@link ConnectionDBItemStiffnessType NXOpen.CAE.Connections.ConnectionDBItemStiffnessType@endlink) StiffnessType
          the mass    
            
         
        """
        pass
    
    ## Setter for property: (@link ConnectionDBItemStiffnessType NXOpen.CAE.Connections.ConnectionDBItemStiffnessType@endlink) StiffnessType

    ##   the mass    
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @StiffnessType.setter
    def StiffnessType(self, stiffnessType: ConnectionDBItemStiffnessType):
        """
        Setter for property: (@link ConnectionDBItemStiffnessType NXOpen.CAE.Connections.ConnectionDBItemStiffnessType@endlink) StiffnessType
          the mass    
            
         
        """
        pass
    
    ## Getter for property: (float) StiffnessX
    ##   the stiffness X    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return float
    @property
    def StiffnessX(self) -> float:
        """
        Getter for property: (float) StiffnessX
          the stiffness X    
            
         
        """
        pass
    
    ## Setter for property: (float) StiffnessX

    ##   the stiffness X    
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @StiffnessX.setter
    def StiffnessX(self, stiffnessX: float):
        """
        Setter for property: (float) StiffnessX
          the stiffness X    
            
         
        """
        pass
    
    ## Getter for property: (float) StiffnessY
    ##   the stiffness Y    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return float
    @property
    def StiffnessY(self) -> float:
        """
        Getter for property: (float) StiffnessY
          the stiffness Y    
            
         
        """
        pass
    
    ## Setter for property: (float) StiffnessY

    ##   the stiffness Y    
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @StiffnessY.setter
    def StiffnessY(self, stiffnessY: float):
        """
        Setter for property: (float) StiffnessY
          the stiffness Y    
            
         
        """
        pass
    
    ## Getter for property: (float) StiffnessZ
    ##   the stiffness Z    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return float
    @property
    def StiffnessZ(self) -> float:
        """
        Getter for property: (float) StiffnessZ
          the stiffness Z    
            
         
        """
        pass
    
    ## Setter for property: (float) StiffnessZ

    ##   the stiffness Z    
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @StiffnessZ.setter
    def StiffnessZ(self, stiffnessZ: float):
        """
        Setter for property: (float) StiffnessZ
          the stiffness Z    
            
         
        """
        pass
    
    ##  The Dofs  
    ##  @return listOfDofs (List[int]): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetDofs(connectionDBItemData: ConnectionDBItemData) -> List[int]:
        """
         The Dofs  
         @return listOfDofs (List[int]): .
        """
        pass
    
##  connection DB item stiffness type 
##  None 
class ConnectionDBItemStiffnessType(Enum):
    """
    Members Include: <NotSet> <Rectangular> <Spherical> <Cylindrical>
    """
    NotSet: int
    Rectangular: int
    Spherical: int
    Cylindrical: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> ConnectionDBItemStiffnessType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


##  Connection type 
##  None 
class ConnectionType(Enum):
    """
    Members Include: <NotSet> <SpotWeld> <Adhesive> <Bolt> <Spring> <Rigid> <Bushing> <Damper> <Kinematic> <SeamWeld> <Sealing> <Rivet> <LumpedMass> <Clinch> <Crimp> <Bar> <Bearing>
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
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> ConnectionType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


import NXOpen
##   @brief  Location interface. This defines connection locations with common properties like coordinates.  
## 
##    <br> To obtain an instance of this object use the AddLocation creators on the Connections  <br> 
## 
##   <br>  Created in NX11.0.0  <br> 

class CoordinatesLocation(Location): 
    """ <summary> Location interface. This defines connection locations with common properties like coordinates. </summary> """


    ##  Gets the coordinates from the specified location.
    ##                 The location can be any type: coordinates, node or point.
    ##                 Its coordinates will be returned. 
    ##  @return coordinates (@link NXOpen.Point3d NXOpen.Point3d@endlink):  Location coordinates .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetCoordinates(location: CoordinatesLocation) -> NXOpen.Point3d:
        """
         Gets the coordinates from the specified location.
                        The location can be any type: coordinates, node or point.
                        Its coordinates will be returned. 
         @return coordinates (@link NXOpen.Point3d NXOpen.Point3d@endlink):  Location coordinates .
        """
        pass
    
    ##  Set the coordinates. Only for coordinates type location 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##  The location coordinates 
    def SetCoordinates(location: CoordinatesLocation, coordinates: NXOpen.Point3d) -> None:
        """
         Set the coordinates. Only for coordinates type location 
        """
        pass
    
import NXOpen
##   @brief  Location interface. This defines connection locations with common properties like coordinates.  
## 
##    <br> To obtain an instance of this object use the AddLocation creators on the Connections  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class CoordinatesSeriesLocation(Location): 
    """ <summary> Location interface. This defines connection locations with common properties like coordinates. </summary> """


    ##  Gets the coordinates from the specified location.
    ##                 The location can be any type: coordinates, node or point.
    ##                 Its coordinates will be returned. 
    ##  @return coordinates (@link NXOpen.Point3d List[NXOpen.Point3d]@endlink):  Location coordinates .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetCoordinates(location: CoordinatesSeriesLocation) -> List[NXOpen.Point3d]:
        """
         Gets the coordinates from the specified location.
                        The location can be any type: coordinates, node or point.
                        Its coordinates will be returned. 
         @return coordinates (@link NXOpen.Point3d List[NXOpen.Point3d]@endlink):  Location coordinates .
        """
        pass
    
    ##  Set the coordinates. Only for coordinates type location 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##  The location coordinates 
    def SetCoordinates(location: CoordinatesSeriesLocation, coordinates: List[NXOpen.Point3d]) -> None:
        """
         Set the coordinates. Only for coordinates type location 
        """
        pass
    
import NXOpen
##   Crimp connection. Use this interface to set/get properties and parameters of the crimp connection.  
## 
##   <br>  Created in NX1847.0.0  <br> 

class Crimp(IConnection): 
    """  Crimp connection. Use this interface to set/get properties and parameters of the crimp connection.  """


    ## Getter for property: (@link DiscretizationMethod NXOpen.CAE.Connections.DiscretizationMethod@endlink) DiscretizationMethod
    ##   the discretization method   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return DiscretizationMethod
    @property
    def DiscretizationMethod(self) -> DiscretizationMethod:
        """
        Getter for property: (@link DiscretizationMethod NXOpen.CAE.Connections.DiscretizationMethod@endlink) DiscretizationMethod
          the discretization method   
            
         
        """
        pass
    
    ## Setter for property: (@link DiscretizationMethod NXOpen.CAE.Connections.DiscretizationMethod@endlink) DiscretizationMethod

    ##   the discretization method   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @DiscretizationMethod.setter
    def DiscretizationMethod(self, method: DiscretizationMethod):
        """
        Setter for property: (@link DiscretizationMethod NXOpen.CAE.Connections.DiscretizationMethod@endlink) DiscretizationMethod
          the discretization method   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) DistanceFromStart
    ##   the line Discretization distance from start   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def DistanceFromStart(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) DistanceFromStart
          the line Discretization distance from start   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) DistanceToEnd
    ##   the line Discretization distance to end   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def DistanceToEnd(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) DistanceToEnd
          the line Discretization distance to end   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Height
    ##   the height value   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Height(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Height
          the height value   
            
         
        """
        pass
    
    ## Getter for property: (@link HeightType NXOpen.CAE.Connections.HeightType@endlink) HeightType
    ##   the connection height type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return HeightType
    @property
    def HeightType(self) -> HeightType:
        """
        Getter for property: (@link HeightType NXOpen.CAE.Connections.HeightType@endlink) HeightType
          the connection height type   
            
         
        """
        pass
    
    ## Setter for property: (@link HeightType NXOpen.CAE.Connections.HeightType@endlink) HeightType

    ##   the connection height type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @HeightType.setter
    def HeightType(self, heightType: HeightType):
        """
        Setter for property: (@link HeightType NXOpen.CAE.Connections.HeightType@endlink) HeightType
          the connection height type   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) LengthStep
    ##   the line Discretization length step   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def LengthStep(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) LengthStep
          the line Discretization length step   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.PhysicalMaterial NXOpen.PhysicalMaterial@endlink) Material
    ##   the connection material   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.PhysicalMaterial
    @property
    def Material(self) -> NXOpen.PhysicalMaterial:
        """
        Getter for property: (@link NXOpen.PhysicalMaterial NXOpen.PhysicalMaterial@endlink) Material
          the connection material   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.PhysicalMaterial NXOpen.PhysicalMaterial@endlink) Material

    ##   the connection material   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @Material.setter
    def Material(self, material: NXOpen.PhysicalMaterial):
        """
        Setter for property: (@link NXOpen.PhysicalMaterial NXOpen.PhysicalMaterial@endlink) Material
          the connection material   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxAngleBetweenNormals
    ##   the maximum angle of normals with the projection surface   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def MaxAngleBetweenNormals(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxAngleBetweenNormals
          the maximum angle of normals with the projection surface   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxDistCGToElemCG
    ##   the maximum distance from definition point to center of support element   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def MaxDistCGToElemCG(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxDistCGToElemCG
          the maximum distance from definition point to center of support element   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxLengthStep
    ##   the line Discretization max length step   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def MaxLengthStep(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxLengthStep
          the line Discretization max length step   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxNormalDistCGToFlanges
    ##   the maximum normal distance from definition point to center of element   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def MaxNormalDistCGToFlanges(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxNormalDistCGToFlanges
          the maximum normal distance from definition point to center of element   
            
         
        """
        pass
    
    ## Getter for property: (int) NumberOfDiscretizationPoints
    ##   the number of connections   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return int
    @property
    def NumberOfDiscretizationPoints(self) -> int:
        """
        Getter for property: (int) NumberOfDiscretizationPoints
          the number of connections   
            
         
        """
        pass
    
    ## Setter for property: (int) NumberOfDiscretizationPoints

    ##   the number of connections   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @NumberOfDiscretizationPoints.setter
    def NumberOfDiscretizationPoints(self, num: int):
        """
        Setter for property: (int) NumberOfDiscretizationPoints
          the number of connections   
            
         
        """
        pass
    
    ## Getter for property: (int) NumberOfFlanges
    ##   the number of flanges.  
    ##    When changing the number of flanges this is not applied till an update is performed by calling @link Update::DoUpdate Update::DoUpdate@endlink    
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return int
    @property
    def NumberOfFlanges(self) -> int:
        """
        Getter for property: (int) NumberOfFlanges
          the number of flanges.  
           When changing the number of flanges this is not applied till an update is performed by calling @link Update::DoUpdate Update::DoUpdate@endlink    
         
        """
        pass
    
    ## Setter for property: (int) NumberOfFlanges

    ##   the number of flanges.  
    ##    When changing the number of flanges this is not applied till an update is performed by calling @link Update::DoUpdate Update::DoUpdate@endlink    
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @NumberOfFlanges.setter
    def NumberOfFlanges(self, numberOfFlanges: int):
        """
        Setter for property: (int) NumberOfFlanges
          the number of flanges.  
           When changing the number of flanges this is not applied till an update is performed by calling @link Update::DoUpdate Update::DoUpdate@endlink    
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ProjectTolerance
    ##   the projection tolerance   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def ProjectTolerance(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ProjectTolerance
          the projection tolerance   
            
         
        """
        pass
    
    ## Getter for property: (bool) UseMaxLengthStep
    ##   the usage of max length step   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return bool
    @property
    def UseMaxLengthStep(self) -> bool:
        """
        Getter for property: (bool) UseMaxLengthStep
          the usage of max length step   
            
         
        """
        pass
    
    ## Setter for property: (bool) UseMaxLengthStep

    ##   the usage of max length step   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @UseMaxLengthStep.setter
    def UseMaxLengthStep(self, use: bool):
        """
        Setter for property: (bool) UseMaxLengthStep
          the usage of max length step   
            
         
        """
        pass
    
    ## Getter for property: (bool) UseOriginalNodesOfConnection
    ##   the usage of original nodes of connection   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return bool
    @property
    def UseOriginalNodesOfConnection(self) -> bool:
        """
        Getter for property: (bool) UseOriginalNodesOfConnection
          the usage of original nodes of connection   
            
         
        """
        pass
    
    ## Setter for property: (bool) UseOriginalNodesOfConnection

    ##   the usage of original nodes of connection   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @UseOriginalNodesOfConnection.setter
    def UseOriginalNodesOfConnection(self, use: bool):
        """
        Setter for property: (bool) UseOriginalNodesOfConnection
          the usage of original nodes of connection   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Width
    ##   the width value   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Width(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Width
          the width value   
            
         
        """
        pass
    
##  Csys types 
##  Existing CSYS 
class CsysType(Enum):
    """
    Members Include: <Existing> <Predefined> <Absolute> <LocalCartesian> <LocalCylindrical> <LocalSpherical>
    """
    Existing: int
    Predefined: int
    Absolute: int
    LocalCartesian: int
    LocalCylindrical: int
    LocalSpherical: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> CsysType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


import NXOpen
##   @brief  Location interface. This defines connection locations with common properties like coordinates.  
## 
##    <br> To obtain an instance of this object use the AddLocation creators on the Connections  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class CurveLocation(Location): 
    """ <summary> Location interface. This defines connection locations with common properties like coordinates. </summary> """


    ## Getter for property: (@link NXOpen.IBaseCurve NXOpen.IBaseCurve@endlink) Curve
    ##   the CURVE used for creating the location.  
    ##   
    ##                 If the location type is not curve, this method will raise an error.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.IBaseCurve
    @property
    def Curve(self) -> NXOpen.IBaseCurve:
        """
        Getter for property: (@link NXOpen.IBaseCurve NXOpen.IBaseCurve@endlink) Curve
          the CURVE used for creating the location.  
          
                        If the location type is not curve, this method will raise an error.   
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.IBaseCurve NXOpen.IBaseCurve@endlink) Curve

    ##   the CURVE used for creating the location.  
    ##   
    ##                 If the location type is not curve, this method will raise an error.   
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @Curve.setter
    def Curve(self, curve: NXOpen.IBaseCurve):
        """
        Setter for property: (@link NXOpen.IBaseCurve NXOpen.IBaseCurve@endlink) Curve
          the CURVE used for creating the location.  
          
                        If the location type is not curve, this method will raise an error.   
         
        """
        pass
    
import NXOpen
##  Damper connection. Use this interface to set/get properties and parameters of the Damper connection.  
## 
##   <br>  Created in NX12.0.0  <br> 

class Damper(IConnection): 
    """ Damper connection. Use this interface to set/get properties and parameters of the Damper connection.  """


    ## Getter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) Csys
    ##   the csys   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.CoordinateSystem
    @property
    def Csys(self) -> NXOpen.CoordinateSystem:
        """
        Getter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) Csys
          the csys   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) Csys

    ##   the csys   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @Csys.setter
    def Csys(self, csys: NXOpen.CoordinateSystem):
        """
        Setter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) Csys
          the csys   
            
         
        """
        pass
    
    ## Getter for property: (@link CsysType NXOpen.CAE.Connections.CsysType@endlink) CsysType
    ##   the csys type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return CsysType
    @property
    def CsysType(self) -> CsysType:
        """
        Getter for property: (@link CsysType NXOpen.CAE.Connections.CsysType@endlink) CsysType
          the csys type   
            
         
        """
        pass
    
    ## Setter for property: (@link CsysType NXOpen.CAE.Connections.CsysType@endlink) CsysType

    ##   the csys type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @CsysType.setter
    def CsysType(self, csysType: CsysType):
        """
        Setter for property: (@link CsysType NXOpen.CAE.Connections.CsysType@endlink) CsysType
          the csys type   
            
         
        """
        pass
    
    ## Getter for property: (@link NodalPairingMethod NXOpen.CAE.Connections.NodalPairingMethod@endlink) PairingMethod
    ##   the pairing method of targets   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NodalPairingMethod
    @property
    def PairingMethod(self) -> NodalPairingMethod:
        """
        Getter for property: (@link NodalPairingMethod NXOpen.CAE.Connections.NodalPairingMethod@endlink) PairingMethod
          the pairing method of targets   
            
         
        """
        pass
    
    ## Setter for property: (@link NodalPairingMethod NXOpen.CAE.Connections.NodalPairingMethod@endlink) PairingMethod

    ##   the pairing method of targets   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @PairingMethod.setter
    def PairingMethod(self, method: NodalPairingMethod):
        """
        Setter for property: (@link NodalPairingMethod NXOpen.CAE.Connections.NodalPairingMethod@endlink) PairingMethod
          the pairing method of targets   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RxViscousDampingConstant
    ##   the RX viscous damping constant   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def RxViscousDampingConstant(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RxViscousDampingConstant
          the RX viscous damping constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RyViscousDampingConstant
    ##   the RY viscous damping constant   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def RyViscousDampingConstant(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RyViscousDampingConstant
          the RY viscous damping constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RzViscousDampingConstant
    ##   the RZ viscous damping constant   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def RzViscousDampingConstant(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RzViscousDampingConstant
          the RZ viscous damping constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) SearchConeAngle
    ##   the search cone angle   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def SearchConeAngle(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) SearchConeAngle
          the search cone angle   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) SearchOrientation
    ##   the pairing search orientation   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Direction
    @property
    def SearchOrientation(self) -> NXOpen.Direction:
        """
        Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) SearchOrientation
          the pairing search orientation   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) SearchOrientation

    ##   the pairing search orientation   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @SearchOrientation.setter
    def SearchOrientation(self, orientation: NXOpen.Direction):
        """
        Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) SearchOrientation
          the pairing search orientation   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) SearchRange
    ##   the search range   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def SearchRange(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) SearchRange
          the search range   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) XViscousDampingConstant
    ##   the X viscous damping constant   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def XViscousDampingConstant(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) XViscousDampingConstant
          the X viscous damping constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) YViscousDampingConstant
    ##   the Y viscous damping constant   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def YViscousDampingConstant(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) YViscousDampingConstant
          the Y viscous damping constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ZViscousDampingConstant
    ##   the Z viscous damping constant   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def ZViscousDampingConstant(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ZViscousDampingConstant
          the Z viscous damping constant   
            
         
        """
        pass
    
##  Diameter definition types 
##  Undefined diameter type 
class DiameterType(Enum):
    """
    Members Include: <Undefined> <User> <Formula> <TableFile> <FlangeHoleDetection>
    """
    Undefined: int
    User: int
    Formula: int
    TableFile: int
    FlangeHoleDetection: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> DiameterType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


##  line locations discretization method 
##  Discretize the line using step length 
class DiscretizationMethod(Enum):
    """
    Members Include: <StepLength> <NumberOfPoints>
    """
    StepLength: int
    NumberOfPoints: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> DiscretizationMethod:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


##  Degrees Of Freedom Combination types 
##  User defined combination for all DOFs 
class DofCombination(Enum):
    """
    Members Include: <UserDefined> <Fixed> <Spherical> <Inplane> <Slider> <Revolute> <Cylindrical> <Universal> <SliderUniversal> <Inline>
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
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> DofCombination:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


##  Degrees Of Freedom types 
##  The DOF is not constrained 
class DofType(Enum):
    """
    Members Include: <Free> <Fixed>
    """
    Free: int
    Fixed: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> DofType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


##  Degrees of freedom definition 
##  X Translation degree of freedom 
class Dof(Enum):
    """
    Members Include: <X> <Y> <Z> <Rx> <Ry> <Rz>
    """
    X: int
    Y: int
    Z: int
    Rx: int
    Ry: int
    Rz: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> Dof:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


import NXOpen
##   @brief  Element collection provides methods to manage @link CAE::Connections::Element CAE::Connections::Element@endlink  objects  
## 
##    <br> To obtain an instance of this class, refer to @link NXOpen::CAE::BaseFEModel  NXOpen::CAE::BaseFEModel @endlink  <br> 
## 
##   <br>  Created in NX11.0.0  <br> 

class ElementCollection(NXOpen.TaggedObjectCollection): 
    """ <summary> Element collection provides methods to manage <ja_class>CAE.Connections.Element</ja_class> objects </summary> """


    ##  Creates a @link NXOpen::CAE::Connections::Element NXOpen::CAE::Connections::Element@endlink 
    ##  @return element (@link Element NXOpen.CAE.Connections.Element@endlink): .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## <param name="fem"> (@link ElementCollection NXOpen.CAE.Connections.ElementCollection@endlink) </param>
    ## <param name="elementType"> (@link ElementType NXOpen.CAE.Connections.ElementType@endlink) </param>
    ## <param name="name"> (str) </param>
    ## <param name="connections"> (@link IConnection List[NXOpen.CAE.Connections.IConnection]@endlink) </param>
    @overload
    def Create(self, fem: ElementCollection, elementType: ElementType, name: str, connections: List[IConnection]) -> Element:
        """
         Creates a @link NXOpen::CAE::Connections::Element NXOpen::CAE::Connections::Element@endlink 
         @return element (@link Element NXOpen.CAE.Connections.Element@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::CAE::Connections::Element NXOpen::CAE::Connections::Element@endlink 
    ##  @return element (@link Element NXOpen.CAE.Connections.Element@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## <param name="fem"> (@link ElementCollection NXOpen.CAE.Connections.ElementCollection@endlink) </param>
    ## <param name="elementType"> (@link ElementType NXOpen.CAE.Connections.ElementType@endlink) </param>
    ## <param name="connectionType"> (@link ConnectionType NXOpen.CAE.Connections.ConnectionType@endlink) </param>
    ## <param name="name"> (str) </param>
    @overload
    def Create(self, fem: ElementCollection, elementType: ElementType, connectionType: ConnectionType, name: str) -> Element:
        """
         Creates a @link NXOpen::CAE::Connections::Element NXOpen::CAE::Connections::Element@endlink 
         @return element (@link Element NXOpen.CAE.Connections.Element@endlink): .
        """
        pass
    
##  Element status 
##  Invalid 
class ElementStatusType(Enum):
    """
    Members Include: <Invalid> <NotUpdated> <Updated>
    """
    Invalid: int
    NotUpdated: int
    Updated: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> ElementStatusType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


##  Element type 
##  None 
class ElementType(Enum):
    """
    Members Include: <NotSet> <EHex8> <EHex8Spider> <E1d> <E1DSpider> <ESpider> <EBushing> <ESpring> <EDamper> <ERigid> <EKinematic> <ERigidConnector> <ERigidRigidConnector> <EInterpolationSpider> <EMassRigidSpider> <EMassInterpolationSpider> <EScalarSpringRigidSpider> <EScalarSpringRigidInterpolationSpider> <EJoint> <EJointInterpolation> <EBeamRigidSpider> <EBar> <EBarInterpolationSpider> <ECbear2Fou3InterpolationSpider> <ECbear2RigidSpider> <ECbush2RigidSpider> <EBeamSpider> <ECbush2Fou3InterpolationSpider> <EConstrainedJointMPCSpider> <EMassFou3InterpolationSpider> <EFou3InterpolationSpider> <EBeam> <ECWeld> <EClinkCbear2RigidSpider> <EClinkCbush2RigidSpider> <EClinkBarRigidSpider> <EClinkBeamRigidSpider> <EClinkFou3> <EQuad4InterpolationSpider>
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
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> ElementType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


import NXOpen
import NXOpen.CAE
##   @brief  This is the class to access a connection element  
## 
##    <br> To obtain an instance of this object use the Create creator in @link CAE::Connections::ElementCollection CAE::Connections::ElementCollection@endlink .  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class Element(NXOpen.NXObject): 
    """ <summary> This is the class to access a connection element </summary> """


    ## Getter for property: (bool) IsCompatibleType
    ##   the compatibility of the element
    ##                 (whether it accepts compatible or incompatible meshes)
    ##               
    ##     
    ##  
    ## Getter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return bool
    @property
    def IsCompatibleType(self) -> bool:
        """
        Getter for property: (bool) IsCompatibleType
          the compatibility of the element
                        (whether it accepts compatible or incompatible meshes)
                      
            
         
        """
        pass
    
    ## Getter for property: (bool) Manual
    ##   the flag telling if the connection element is set up manually.  
    ##   
    ##               
    ##  
    ## Getter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return bool
    @property
    def Manual(self) -> bool:
        """
        Getter for property: (bool) Manual
          the flag telling if the connection element is set up manually.  
          
                      
         
        """
        pass
    
    ## Setter for property: (bool) Manual

    ##   the flag telling if the connection element is set up manually.  
    ##   
    ##               
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @Manual.setter
    def Manual(self, manual: bool):
        """
        Setter for property: (bool) Manual
          the flag telling if the connection element is set up manually.  
          
                      
         
        """
        pass
    
    ## Getter for property: (@link SeamWeldNodeSelectionMethod NXOpen.CAE.Connections.SeamWeldNodeSelectionMethod@endlink) NodeSelectionMethod
    ##   the node selection method.  
    ##    To be used when connection element has been set up manually (@link NXOpen::CAE::Connections::Element::Manual NXOpen::CAE::Connections::Element::Manual@endlink  is true).
    ##               
    ##  
    ## Getter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return SeamWeldNodeSelectionMethod
    @property
    def NodeSelectionMethod(self) -> SeamWeldNodeSelectionMethod:
        """
        Getter for property: (@link SeamWeldNodeSelectionMethod NXOpen.CAE.Connections.SeamWeldNodeSelectionMethod@endlink) NodeSelectionMethod
          the node selection method.  
           To be used when connection element has been set up manually (@link NXOpen::CAE::Connections::Element::Manual NXOpen::CAE::Connections::Element::Manual@endlink  is true).
                      
         
        """
        pass
    
    ## Setter for property: (@link SeamWeldNodeSelectionMethod NXOpen.CAE.Connections.SeamWeldNodeSelectionMethod@endlink) NodeSelectionMethod

    ##   the node selection method.  
    ##    To be used when connection element has been set up manually (@link NXOpen::CAE::Connections::Element::Manual NXOpen::CAE::Connections::Element::Manual@endlink  is true).
    ##               
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @NodeSelectionMethod.setter
    def NodeSelectionMethod(self, method: SeamWeldNodeSelectionMethod):
        """
        Setter for property: (@link SeamWeldNodeSelectionMethod NXOpen.CAE.Connections.SeamWeldNodeSelectionMethod@endlink) NodeSelectionMethod
          the node selection method.  
           To be used when connection element has been set up manually (@link NXOpen::CAE::Connections::Element::Manual NXOpen::CAE::Connections::Element::Manual@endlink  is true).
                      
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.CAE.PropertyTable NXOpen.CAE.PropertyTable@endlink) PropertyTable
    ##   the property table.  
    ##      
    ##  
    ## Getter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.CAE.PropertyTable
    @property
    def PropertyTable(self) -> NXOpen.CAE.PropertyTable:
        """
        Getter for property: (@link NXOpen.CAE.PropertyTable NXOpen.CAE.PropertyTable@endlink) PropertyTable
          the property table.  
             
         
        """
        pass
    
    ## Getter for property: (@link ElementStatusType NXOpen.CAE.Connections.ElementStatusType@endlink) Status
    ##  the status of the element
    ##               
    ##     
    ##  
    ## Getter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return ElementStatusType
    @property
    def Status(self) -> ElementStatusType:
        """
        Getter for property: (@link ElementStatusType NXOpen.CAE.Connections.ElementStatusType@endlink) Status
         the status of the element
                      
            
         
        """
        pass
    
    ## Getter for property: (@link ElementType NXOpen.CAE.Connections.ElementType@endlink) Type
    ##  the type of the element
    ##               
    ##     
    ##  
    ## Getter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return ElementType
    @property
    def Type(self) -> ElementType:
        """
        Getter for property: (@link ElementType NXOpen.CAE.Connections.ElementType@endlink) Type
         the type of the element
                      
            
         
        """
        pass
    
    ## Setter for property: (@link ElementType NXOpen.CAE.Connections.ElementType@endlink) Type

    ##  the type of the element
    ##               
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @Type.setter
    def Type(self, type: ElementType):
        """
        Setter for property: (@link ElementType NXOpen.CAE.Connections.ElementType@endlink) Type
         the type of the element
                      
            
         
        """
        pass
    
    ##  Adds connections to this element
    ##             
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ## <param name="connections"> (@link IConnection List[NXOpen.CAE.Connections.IConnection]@endlink) </param>
    def AddConnections(element: Element, connections: List[IConnection]) -> None:
        """
         Adds connections to this element
                    
        """
        pass
    
    ##  Mesh the Connection Element.
    ##             
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    @staticmethod
    def GenerateElements(element: Element) -> None:
        """
         Mesh the Connection Element.
                    
        """
        pass
    
    ##  Gets connections from this element
    ##             
    ##  @return connections (@link IConnection List[NXOpen.CAE.Connections.IConnection]@endlink): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    @staticmethod
    def GetConnections(element: Element) -> List[IConnection]:
        """
         Gets connections from this element
                    
         @return connections (@link IConnection List[NXOpen.CAE.Connections.IConnection]@endlink): .
        """
        pass
    
    ##  Get the manual element groups. To be used when connection element has been set up manually (@link NXOpen::CAE::Connections::Element::Manual NXOpen::CAE::Connections::Element::Manual@endlink  is true).
    ##             
    ##  @return groups (@link NXOpen.CAE.CaeGroup List[NXOpen.CAE.CaeGroup]@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    @staticmethod
    def GetElementGroups(element: Element) -> List[NXOpen.CAE.CaeGroup]:
        """
         Get the manual element groups. To be used when connection element has been set up manually (@link NXOpen::CAE::Connections::Element::Manual NXOpen::CAE::Connections::Element::Manual@endlink  is true).
                    
         @return groups (@link NXOpen.CAE.CaeGroup List[NXOpen.CAE.CaeGroup]@endlink): .
        """
        pass
    
    ##  Get the manual elements. To be used when connection element has been set up manually (@link NXOpen::CAE::Connections::Element::Manual NXOpen::CAE::Connections::Element::Manual@endlink  is true).
    ##             
    ##  @return elems (@link NXOpen.CAE.FEElement List[NXOpen.CAE.FEElement]@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    @staticmethod
    def GetElements(element: Element) -> List[NXOpen.CAE.FEElement]:
        """
         Get the manual elements. To be used when connection element has been set up manually (@link NXOpen::CAE::Connections::Element::Manual NXOpen::CAE::Connections::Element::Manual@endlink  is true).
                    
         @return elems (@link NXOpen.CAE.FEElement List[NXOpen.CAE.FEElement]@endlink): .
        """
        pass
    
    ##  Get the elements generated for a given @link CAE::Connections::IConnection CAE::Connections::IConnection@endlink  meshed by this @link CAE::Connections::Element CAE::Connections::Element@endlink .
    ##             
    ##  @return elems (@link NXOpen.CAE.FEElement List[NXOpen.CAE.FEElement]@endlink): .
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ## <param name="connection"> (@link IConnection NXOpen.CAE.Connections.IConnection@endlink) </param>
    def GetGeneratedElementsOfConnection(element: Element, connection: IConnection) -> List[NXOpen.CAE.FEElement]:
        """
         Get the elements generated for a given @link CAE::Connections::IConnection CAE::Connections::IConnection@endlink  meshed by this @link CAE::Connections::Element CAE::Connections::Element@endlink .
                    
         @return elems (@link NXOpen.CAE.FEElement List[NXOpen.CAE.FEElement]@endlink): .
        """
        pass
    
    ##  Get the elements generated at a given location of a @link CAE::Connections::IConnection CAE::Connections::IConnection@endlink  meshed by this @link CAE::Connections::Element CAE::Connections::Element@endlink .
    ##                 Current version does not support @link CAE::Connections::Bolt CAE::Connections::Bolt@endlink  and nodal (@link CAE::Connections::Spring CAE::Connections::Spring@endlink , @link CAE::Connections::Damper CAE::Connections::Damper@endlink , 
    ##                 @link CAE::Connections::Bushing CAE::Connections::Bushing@endlink , @link CAE::Connections::Rigid CAE::Connections::Rigid@endlink , @link CAE::Connections::Kinematic CAE::Connections::Kinematic@endlink ) connections.
    ##             
    ##  @return elems (@link NXOpen.CAE.FEElement List[NXOpen.CAE.FEElement]@endlink): .
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ## <param name="connection"> (@link IConnection NXOpen.CAE.Connections.IConnection@endlink) </param>
    ## <param name="indexOfLocation"> (int) </param>
    ## <param name="indexOfDefinitionInLocation"> (int) </param>
    def GetGeneratedElementsOfConnectionAtLocation(element: Element, connection: IConnection, indexOfLocation: int, indexOfDefinitionInLocation: int) -> List[NXOpen.CAE.FEElement]:
        """
         Get the elements generated at a given location of a @link CAE::Connections::IConnection CAE::Connections::IConnection@endlink  meshed by this @link CAE::Connections::Element CAE::Connections::Element@endlink .
                        Current version does not support @link CAE::Connections::Bolt CAE::Connections::Bolt@endlink  and nodal (@link CAE::Connections::Spring CAE::Connections::Spring@endlink , @link CAE::Connections::Damper CAE::Connections::Damper@endlink , 
                        @link CAE::Connections::Bushing CAE::Connections::Bushing@endlink , @link CAE::Connections::Rigid CAE::Connections::Rigid@endlink , @link CAE::Connections::Kinematic CAE::Connections::Kinematic@endlink ) connections.
                    
         @return elems (@link NXOpen.CAE.FEElement List[NXOpen.CAE.FEElement]@endlink): .
        """
        pass
    
    ##  Get the nodes generated for a given @link CAE::Connections::IConnection CAE::Connections::IConnection@endlink  meshed by this @link CAE::Connections::Element CAE::Connections::Element@endlink .
    ##             
    ##  @return nodes (@link NXOpen.CAE.FENode List[NXOpen.CAE.FENode]@endlink): .
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ## <param name="connection"> (@link IConnection NXOpen.CAE.Connections.IConnection@endlink) </param>
    def GetGeneratedNodesOfConnection(element: Element, connection: IConnection) -> List[NXOpen.CAE.FENode]:
        """
         Get the nodes generated for a given @link CAE::Connections::IConnection CAE::Connections::IConnection@endlink  meshed by this @link CAE::Connections::Element CAE::Connections::Element@endlink .
                    
         @return nodes (@link NXOpen.CAE.FENode List[NXOpen.CAE.FENode]@endlink): .
        """
        pass
    
    ##  Get the manual node groups. To be used when connection element has been set up manually (@link NXOpen::CAE::Connections::Element::Manual NXOpen::CAE::Connections::Element::Manual@endlink  is true).
    ##             
    ##  @return groups (@link NXOpen.CAE.CaeGroup List[NXOpen.CAE.CaeGroup]@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    @staticmethod
    def GetNodeGroups(element: Element) -> List[NXOpen.CAE.CaeGroup]:
        """
         Get the manual node groups. To be used when connection element has been set up manually (@link NXOpen::CAE::Connections::Element::Manual NXOpen::CAE::Connections::Element::Manual@endlink  is true).
                    
         @return groups (@link NXOpen.CAE.CaeGroup List[NXOpen.CAE.CaeGroup]@endlink): .
        """
        pass
    
    ##  Get the manual nodes. To be used when connection element has been set up manually (@link NXOpen::CAE::Connections::Element::Manual NXOpen::CAE::Connections::Element::Manual@endlink  is true).
    ##             
    ##  @return nodes (@link NXOpen.CAE.FENode List[NXOpen.CAE.FENode]@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    @staticmethod
    def GetNodes(element: Element) -> List[NXOpen.CAE.FENode]:
        """
         Get the manual nodes. To be used when connection element has been set up manually (@link NXOpen::CAE::Connections::Element::Manual NXOpen::CAE::Connections::Element::Manual@endlink  is true).
                    
         @return nodes (@link NXOpen.CAE.FENode List[NXOpen.CAE.FENode]@endlink): .
        """
        pass
    
    ##  Mark the Connection Element as changed. To be used when the Property Table has been modified before calling @link NXOpen::CAE::Connections::Element::GenerateElements NXOpen::CAE::Connections::Element::GenerateElements@endlink .
    ##             
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    @staticmethod
    def MarkAsModifiedByPropertyTable(element: Element) -> None:
        """
         Mark the Connection Element as changed. To be used when the Property Table has been modified before calling @link NXOpen::CAE::Connections::Element::GenerateElements NXOpen::CAE::Connections::Element::GenerateElements@endlink .
                    
        """
        pass
    
    ##  Removes a connection from this element. This does not delete/destroy the connection, instead
    ##                 this element will no longer keep a reference to the connection.
    ##             
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ## <param name="connections"> (@link IConnection List[NXOpen.CAE.Connections.IConnection]@endlink) </param>
    def RemoveConnections(element: Element, connections: List[IConnection]) -> None:
        """
         Removes a connection from this element. This does not delete/destroy the connection, instead
                        this element will no longer keep a reference to the connection.
                    
        """
        pass
    
    ##  Set the manual element groups. To be used when connection element has been set up manually (@link NXOpen::CAE::Connections::Element::SetManual NXOpen::CAE::Connections::Element::SetManual@endlink  is true).
    ##             
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ## <param name="groups"> (@link NXOpen.CAE.CaeGroup List[NXOpen.CAE.CaeGroup]@endlink) </param>
    def SetElementGroups(element: Element, groups: List[NXOpen.CAE.CaeGroup]) -> None:
        """
         Set the manual element groups. To be used when connection element has been set up manually (@link NXOpen::CAE::Connections::Element::SetManual NXOpen::CAE::Connections::Element::SetManual@endlink  is true).
                    
        """
        pass
    
    ##  Set the manual elements. To be used when connection element has been set up manually (@link NXOpen::CAE::Connections::Element::SetManual NXOpen::CAE::Connections::Element::SetManual@endlink  is true).
    ##             
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ## <param name="elems"> (@link NXOpen.CAE.FEElement List[NXOpen.CAE.FEElement]@endlink) </param>
    def SetElements(element: Element, elems: List[NXOpen.CAE.FEElement]) -> None:
        """
         Set the manual elements. To be used when connection element has been set up manually (@link NXOpen::CAE::Connections::Element::SetManual NXOpen::CAE::Connections::Element::SetManual@endlink  is true).
                    
        """
        pass
    
    ##  Set the manual node groups. To be used when connection element has been set up manually (@link NXOpen::CAE::Connections::Element::SetManual NXOpen::CAE::Connections::Element::SetManual@endlink  is true).
    ##             
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ## <param name="groups"> (@link NXOpen.CAE.CaeGroup List[NXOpen.CAE.CaeGroup]@endlink) </param>
    def SetNodeGroups(element: Element, groups: List[NXOpen.CAE.CaeGroup]) -> None:
        """
         Set the manual node groups. To be used when connection element has been set up manually (@link NXOpen::CAE::Connections::Element::SetManual NXOpen::CAE::Connections::Element::SetManual@endlink  is true).
                    
        """
        pass
    
    ##  Set the manual nodes. To be used when connection element has been set up manually (@link NXOpen::CAE::Connections::Element::SetManual NXOpen::CAE::Connections::Element::SetManual@endlink  is true).
    ##             
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ## <param name="nodes"> (@link NXOpen.CAE.FENode List[NXOpen.CAE.FENode]@endlink) </param>
    def SetNodes(element: Element, nodes: List[NXOpen.CAE.FENode]) -> None:
        """
         Set the manual nodes. To be used when connection element has been set up manually (@link NXOpen::CAE::Connections::Element::SetManual NXOpen::CAE::Connections::Element::SetManual@endlink  is true).
                    
        """
        pass
    
import NXOpen.CAE
##   @brief  Location interface. This defines connection locations with common properties like coordinates.  
## 
##    <br> To obtain an instance of this object use the AddLocation creators on the Connections  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class FeEdgesLocation(Location): 
    """ <summary> Location interface. This defines connection locations with common properties like coordinates. </summary> """


    ##  Retrieve location edges. 
    ##  @return edges (@link NXOpen.CAE.FEElemEdge List[NXOpen.CAE.FEElemEdge]@endlink):  Edges used for location .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetFeEdges(location: FeEdgesLocation) -> List[NXOpen.CAE.FEElemEdge]:
        """
         Retrieve location edges. 
         @return edges (@link NXOpen.CAE.FEElemEdge List[NXOpen.CAE.FEElemEdge]@endlink):  Edges used for location .
        """
        pass
    
    ##  Add location edges. 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##  Edges used for location 
    def SetFeEdges(location: FeEdgesLocation, edges: List[NXOpen.CAE.FEElemEdge]) -> None:
        """
         Add location edges. 
        """
        pass
    
import NXOpen
import NXOpen.CAE
##   @brief  The Folder class offers a way to create a hierarchy of connections and sub-folders  
## 
##    <br> To obtain an instance of this object use the add_folder creator in a parent folder or access connection root folder from @link CAE::IFEModel CAE::IFEModel@endlink   <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class Folder(NXOpen.NXObject): 
    """ <summary> The Folder class offers a way to create a hierarchy of connections and sub-folders </summary> """


    ## Getter for property: (@link Folder NXOpen.CAE.Connections.Folder@endlink) Parent
    ##   the parent folder   
    ##     
    ##  
    ## Getter License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return Folder
    @property
    def Parent(self) -> Folder:
        """
        Getter for property: (@link Folder NXOpen.CAE.Connections.Folder@endlink) Parent
          the parent folder   
            
         
        """
        pass
    
    ##  Add a subfolder to this folder. The subfolder is moved if found in other folder. 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##  the added folder 
    def AddFolder(parent: Folder, subfolder: Folder) -> None:
        """
         Add a subfolder to this folder. The subfolder is moved if found in other folder. 
        """
        pass
    
    ##  Clone a @link CAE::Connections::IConnection CAE::Connections::IConnection@endlink  in the same folder of the specified connection 
    ##  @return newConnection (@link IConnection NXOpen.CAE.Connections.IConnection@endlink):  the created connection .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##  the original connection 
    def CloneConnection(parent: Folder, originalConnection: IConnection, newConnectionName: str) -> IConnection:
        """
         Clone a @link CAE::Connections::IConnection CAE::Connections::IConnection@endlink  in the same folder of the specified connection 
         @return newConnection (@link IConnection NXOpen.CAE.Connections.IConnection@endlink):  the created connection .
        """
        pass
    
    ##  Create a @link CAE::Connections::IConnection CAE::Connections::IConnection@endlink  in this folder of the specified type with the specified name 
    ##  @return connection (@link IConnection NXOpen.CAE.Connections.IConnection@endlink):  the created connection .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##  name of the connection 
    def CreateConnection(parent: Folder, type: ConnectionType, name: str) -> IConnection:
        """
         Create a @link CAE::Connections::IConnection CAE::Connections::IConnection@endlink  in this folder of the specified type with the specified name 
         @return connection (@link IConnection NXOpen.CAE.Connections.IConnection@endlink):  the created connection .
        """
        pass
    
    ##  Creates a @link CAE::Connections::Folder CAE::Connections::Folder@endlink  in this folder with the specified name 
    ##  @return folder (@link Folder NXOpen.CAE.Connections.Folder@endlink):  the created @link CAE::Connections::Folder CAE::Connections::Folder@endlink  .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##   Name that the created folder should have 
    def CreateFolder(parent: Folder, name: str) -> Folder:
        """
         Creates a @link CAE::Connections::Folder CAE::Connections::Folder@endlink  in this folder with the specified name 
         @return folder (@link Folder NXOpen.CAE.Connections.Folder@endlink):  the created @link CAE::Connections::Folder CAE::Connections::Folder@endlink  .
        """
        pass
    
    ##  Create @link CAE::Connections::SpotWeld CAE::Connections::SpotWeld@endlink  connections in the current @link CAE::Connections::Folder CAE::Connections::Folder@endlink 
    ##             using connection data imported from a WCD file. This method allows user to create a spotweld connection specifically for composer application 
    ##  @return connections (@link SpotWeld List[NXOpen.CAE.Connections.SpotWeld]@endlink):  the created connections .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##  name of the wcd import file 
    def CreateSpotWeldConnectionFromWcdFile(parent: Folder, file: str, matfile: str, pDbData: ConnectionDBItemData) -> List[SpotWeld]:
        """
         Create @link CAE::Connections::SpotWeld CAE::Connections::SpotWeld@endlink  connections in the current @link CAE::Connections::Folder CAE::Connections::Folder@endlink 
                    using connection data imported from a WCD file. This method allows user to create a spotweld connection specifically for composer application 
         @return connections (@link SpotWeld List[NXOpen.CAE.Connections.SpotWeld]@endlink):  the created connections .
        """
        pass
    
    ##  Delete @link CAE::Connections::IConnection CAE::Connections::IConnection@endlink  or @link CAE::Connections::Folder CAE::Connections::Folder@endlink  instances. Use this to avoid performance issue in particular cases. 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##  the objects to delete 
    def DeleteObjects(parent: Folder, objects: List[NXOpen.NXObject]) -> None:
        """
         Delete @link CAE::Connections::IConnection CAE::Connections::IConnection@endlink  or @link CAE::Connections::Folder CAE::Connections::Folder@endlink  instances. Use this to avoid performance issue in particular cases. 
        """
        pass
    
    ##  Create @link CAE::Connections::IConnection CAE::Connections::IConnection@endlink  connections in the current @link CAE::Connections::Folder CAE::Connections::Folder@endlink 
    ##             using connection auto detect.  
    ##  @return connections (@link IConnection List[NXOpen.CAE.Connections.IConnection]@endlink):  the created connections .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##  the import parameters see @link CAE::CaeSession::GetDataContainer CAE::CaeSession::GetDataContainer@endlink . 
    def DetectConnections(parent: Folder, propertyList: NXOpen.CAE.CaeDataContainer) -> List[IConnection]:
        """
         Create @link CAE::Connections::IConnection CAE::Connections::IConnection@endlink  connections in the current @link CAE::Connections::Folder CAE::Connections::Folder@endlink 
                    using connection auto detect.  
         @return connections (@link IConnection List[NXOpen.CAE.Connections.IConnection]@endlink):  the created connections .
        """
        pass
    
    ##  Export @link CAE::Connections::IConnection CAE::Connections::IConnection@endlink  connections in the current @link CAE::Connections::Folder CAE::Connections::Folder@endlink 
    ##             to a xMCF file.  
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##  the connections to export 
    def ExportConnectionsToXMcf(parent: Folder, connections: List[IConnection], propertyList: NXOpen.CAE.CaeDataContainer) -> None:
        """
         Export @link CAE::Connections::IConnection CAE::Connections::IConnection@endlink  connections in the current @link CAE::Connections::Folder CAE::Connections::Folder@endlink 
                    to a xMCF file.  
        """
        pass
    
    ##  Export @link CAE::Connections::SpotWeld CAE::Connections::SpotWeld@endlink  connections in the current @link CAE::Connections::Folder CAE::Connections::Folder@endlink 
    ##             to a WCD file.  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##  filepath of the exported file 
    def ExportSpotWeldConnectionsToWcdFile(parent: Folder, filePath: str, outputLength: NXOpen.Unit, connections: List[IConnection]) -> None:
        """
         Export @link CAE::Connections::SpotWeld CAE::Connections::SpotWeld@endlink  connections in the current @link CAE::Connections::Folder CAE::Connections::Folder@endlink 
                    to a WCD file.  
        """
        pass
    
    ##  Get all the connections under this folder and its descendant folders 
    ##  @return connections (@link IConnection List[NXOpen.CAE.Connections.IConnection]@endlink):  all connections under this folder and its descendants .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    @staticmethod
    def GetAllConnections(folder: Folder) -> List[IConnection]:
        """
         Get all the connections under this folder and its descendant folders 
         @return connections (@link IConnection List[NXOpen.CAE.Connections.IConnection]@endlink):  all connections under this folder and its descendants .
        """
        pass
    
    ##  Get the child folders 
    ##  @return children (@link Folder List[NXOpen.CAE.Connections.Folder]@endlink):  child folders.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    @staticmethod
    def GetChildFolders(folder: Folder) -> List[Folder]:
        """
         Get the child folders 
         @return children (@link Folder List[NXOpen.CAE.Connections.Folder]@endlink):  child folders.
        """
        pass
    
    ##  Get the connections 
    ##  @return connections (@link IConnection List[NXOpen.CAE.Connections.IConnection]@endlink):  connections found in folder .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    @staticmethod
    def GetConnections(folder: Folder) -> List[IConnection]:
        """
         Get the connections 
         @return connections (@link IConnection List[NXOpen.CAE.Connections.IConnection]@endlink):  connections found in folder .
        """
        pass
    
    ##  Create @link CAE::Connections::IConnection CAE::Connections::IConnection@endlink  connections in the current @link CAE::Connections::Folder CAE::Connections::Folder@endlink  
    ##             using connection data imported from a MCF file.  
    ##  @return connections (@link IConnection List[NXOpen.CAE.Connections.IConnection]@endlink):  the created connections .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##  name of the import file 
    def ImportConnectionsFromMcf(parent: Folder, file: str, inputFileUnit: NXOpen.Unit) -> List[IConnection]:
        """
         Create @link CAE::Connections::IConnection CAE::Connections::IConnection@endlink  connections in the current @link CAE::Connections::Folder CAE::Connections::Folder@endlink  
                    using connection data imported from a MCF file.  
         @return connections (@link IConnection List[NXOpen.CAE.Connections.IConnection]@endlink):  the created connections .
        """
        pass
    
    ##  Create @link CAE::Connections::IConnection CAE::Connections::IConnection@endlink  connections in the current @link CAE::Connections::Folder CAE::Connections::Folder@endlink 
    ##             using connection data imported from a xMCF file.  
    ##  @return connections (@link IConnection List[NXOpen.CAE.Connections.IConnection]@endlink):  the created connections .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##  the import parameters see @link CAE::CaeSession::GetDataContainer CAE::CaeSession::GetDataContainer@endlink . 
    def ImportConnectionsFromXMcf(parent: Folder, propertyList: NXOpen.CAE.CaeDataContainer) -> List[IConnection]:
        """
         Create @link CAE::Connections::IConnection CAE::Connections::IConnection@endlink  connections in the current @link CAE::Connections::Folder CAE::Connections::Folder@endlink 
                    using connection data imported from a xMCF file.  
         @return connections (@link IConnection List[NXOpen.CAE.Connections.IConnection]@endlink):  the created connections .
        """
        pass
    
    ##  Create @link CAE::Connections::LumpedMass CAE::Connections::LumpedMass@endlink  connection in the current @link CAE::Connections::Folder CAE::Connections::Folder@endlink 
    ##             using lumped mass intermediate representation imported from an external file.  
    ##  @return oConnections (@link LumpedMass List[NXOpen.CAE.Connections.LumpedMass]@endlink):  The intermediate connection representations .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##  The length unit 
    def ImportLumpedMassFromInterchangeData(parent: Folder, lengthUnit: NXOpen.Unit, massUnit: NXOpen.Unit, reportErrors: bool, iConnections: List[LMIEConnection]) -> List[LumpedMass]:
        """
         Create @link CAE::Connections::LumpedMass CAE::Connections::LumpedMass@endlink  connection in the current @link CAE::Connections::Folder CAE::Connections::Folder@endlink 
                    using lumped mass intermediate representation imported from an external file.  
         @return oConnections (@link LumpedMass List[NXOpen.CAE.Connections.LumpedMass]@endlink):  The intermediate connection representations .
        """
        pass
    
    ##  Create @link CAE::Connections::SpotWeld CAE::Connections::SpotWeld@endlink  connections in the current @link CAE::Connections::Folder CAE::Connections::Folder@endlink 
    ##             using connection data imported from a WCD file. This method allows user to set the height value and material for the Spot weld 
    ##  @return connections (@link SpotWeld List[NXOpen.CAE.Connections.SpotWeld]@endlink):  the created connections .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##  name of the import file 
    def ImportSpotWeldFromWcdWithHeightAndMaterial(parent: Folder, file: str, inputFileUnit: NXOpen.Unit, heightType: HeightType, heightValue: float, useInputFileMaterial: bool, userDefinedMaterialType: MaterialType, userDefinedMaterial: NXOpen.PhysicalMaterial) -> List[SpotWeld]:
        """
         Create @link CAE::Connections::SpotWeld CAE::Connections::SpotWeld@endlink  connections in the current @link CAE::Connections::Folder CAE::Connections::Folder@endlink 
                    using connection data imported from a WCD file. This method allows user to set the height value and material for the Spot weld 
         @return connections (@link SpotWeld List[NXOpen.CAE.Connections.SpotWeld]@endlink):  the created connections .
        """
        pass
    
    ##  Add an array of connections to this folder. The connections are removed from the previous parent folder. 
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##  the array of connections that are moved 
    def MoveConnectionsToThisFolder(parent: Folder, connections: List[IConnection]) -> None:
        """
         Add an array of connections to this folder. The connections are removed from the previous parent folder. 
        """
        pass
    
import NXOpen.CAE
##   @brief  This defines Group Location used by Universal Connections.  
## 
##    <br> To obtain an instance of this object use the AddLocation creators on the Connections  <br> 
## 
##   <br>  Created in NX1980.0.0  <br> 

class GroupLocation(Location): 
    """ <summary> This defines Group Location used by Universal Connections. </summary> """


    ## Getter for property: (@link NXOpen.CAE.CaeGroup NXOpen.CAE.CaeGroup@endlink) Group
    ##   the Group used for creating the location.  
    ##   
    ##                 If the location type is not a Group, this method will raise an error.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.CAE.CaeGroup
    @property
    def Group(self) -> NXOpen.CAE.CaeGroup:
        """
        Getter for property: (@link NXOpen.CAE.CaeGroup NXOpen.CAE.CaeGroup@endlink) Group
          the Group used for creating the location.  
          
                        If the location type is not a Group, this method will raise an error.   
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.CAE.CaeGroup NXOpen.CAE.CaeGroup@endlink) Group

    ##   the Group used for creating the location.  
    ##   
    ##                 If the location type is not a Group, this method will raise an error.   
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @Group.setter
    def Group(self, group: NXOpen.CAE.CaeGroup):
        """
        Setter for property: (@link NXOpen.CAE.CaeGroup NXOpen.CAE.CaeGroup@endlink) Group
          the Group used for creating the location.  
          
                        If the location type is not a Group, this method will raise an error.   
         
        """
        pass
    
##  Head diameter definition types 
##  User defined diameter 
class HeadDiameterType(Enum):
    """
    Members Include: <User> <FactorOfDiameter>
    """
    User: int
    FactorOfDiameter: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> HeadDiameterType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


##  Types of height definitions 
##  Undefined height type, used for connections that don't use this parameter 
class HeightType(Enum):
    """
    Members Include: <Undefined> <User> <MeanOfFlangesThickness> <DistanceBetweenFlanges> <DistanceBetweenFlangesMeanOfFlangesThickness> <DistanceBetweenFlangesMaxOfFlangesThickness> <DistanceBetweenFlangesAndMeanOfFlangesThickness> <SumOfFlangesThickness>
    """
    Undefined: int
    User: int
    MeanOfFlangesThickness: int
    DistanceBetweenFlanges: int
    DistanceBetweenFlangesMeanOfFlangesThickness: int
    DistanceBetweenFlangesMaxOfFlangesThickness: int
    DistanceBetweenFlangesAndMeanOfFlangesThickness: int
    SumOfFlangesThickness: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> HeightType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


import NXOpen
##   @brief  This class represents an Interface to the Bushing type.  
## 
##   
## 
##   <br>  Created in NX1953.0.0  <br> 

class IBushingType(NXOpen.INXObject): 
    """ <summary> This class represents an Interface to the Bushing type. </summary> """


    ## Getter for property: (@link BushingType NXOpen.CAE.Connections.BushingType@endlink) BushingType
    ##   the bushing type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return BushingType
    @property
    @abstractmethod
    def BushingType(self) -> BushingType:
        """
        Getter for property: (@link BushingType NXOpen.CAE.Connections.BushingType@endlink) BushingType
          the bushing type   
            
         
        """
        pass
    
    ## Setter for property: (@link BushingType NXOpen.CAE.Connections.BushingType@endlink) BushingType

    ##   the bushing type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @BushingType.setter
    def BushingType(self, bushingType: BushingType):
        """
        Setter for property: (@link BushingType NXOpen.CAE.Connections.BushingType@endlink) BushingType
          the bushing type   
            
         
        """
        pass
    
import NXOpen
##   @brief  This class represents an interface to a connection object.  
## 
##    <br> This is an abstract class, and cannot be created.  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class IConnection(NXOpen.DisplayableObject): 
    """ <summary> This class represents an interface to a connection object. </summary> """


    ## Getter for property: (bool) HasConnectionElement
    ##  the connection is part or not of a mesh object
    ##               
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return bool
    @property
    def HasConnectionElement(self) -> bool:
        """
        Getter for property: (bool) HasConnectionElement
         the connection is part or not of a mesh object
                      
            
         
        """
        pass
    
    ## Getter for property: (@link UniversalConnectionState NXOpen.CAE.Connections.UniversalConnectionState@endlink) State
    ##  the status of the connection
    ##               
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return UniversalConnectionState
    @property
    def State(self) -> UniversalConnectionState:
        """
        Getter for property: (@link UniversalConnectionState NXOpen.CAE.Connections.UniversalConnectionState@endlink) State
         the status of the connection
                      
            
         
        """
        pass
    
    ## Getter for property: (str) UserDescription
    ##   the connection user description   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return str
    @property
    def UserDescription(self) -> str:
        """
        Getter for property: (str) UserDescription
          the connection user description   
            
         
        """
        pass
    
    ## Setter for property: (str) UserDescription

    ##   the connection user description   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @UserDescription.setter
    def UserDescription(self, description: str):
        """
        Setter for property: (str) UserDescription
          the connection user description   
            
         
        """
        pass
    
import NXOpen
##   @brief  This class represents an Interface to the Connection Csys.  
## 
##   
## 
##   <br>  Created in NX12.0.0  <br> 

class ICsys(NXOpen.INXObject): 
    """ <summary> This class represents an Interface to the Connection Csys. </summary> """


    ## Getter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) Csys
    ##   the csys   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.CoordinateSystem
    @property
    @abstractmethod
    def Csys(self) -> NXOpen.CoordinateSystem:
        """
        Getter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) Csys
          the csys   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) Csys

    ##   the csys   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @Csys.setter
    def Csys(self, csys: NXOpen.CoordinateSystem):
        """
        Setter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) Csys
          the csys   
            
         
        """
        pass
    
    ## Getter for property: (@link CsysType NXOpen.CAE.Connections.CsysType@endlink) CsysType
    ##   the csys type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return CsysType
    @property
    @abstractmethod
    def CsysType(self) -> CsysType:
        """
        Getter for property: (@link CsysType NXOpen.CAE.Connections.CsysType@endlink) CsysType
          the csys type   
            
         
        """
        pass
    
    ## Setter for property: (@link CsysType NXOpen.CAE.Connections.CsysType@endlink) CsysType

    ##   the csys type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @CsysType.setter
    def CsysType(self, csysType: CsysType):
        """
        Setter for property: (@link CsysType NXOpen.CAE.Connections.CsysType@endlink) CsysType
          the csys type   
            
         
        """
        pass
    
    ##  Gets supported csys types of connection. 
    ##  @return types (@link CsysType List[NXOpen.CAE.Connections.CsysType]@endlink):  Supported CSys Types .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    @abstractmethod
    def GetSupportedCsysTypes(connectionTag: ICsys) -> List[CsysType]:
        """
         Gets supported csys types of connection. 
         @return types (@link CsysType List[NXOpen.CAE.Connections.CsysType]@endlink):  Supported CSys Types .
        """
        pass
    
import NXOpen
import NXOpen.Fields
##   @brief  This class represents an Interface to the Cylindrical Stiffness dynamic.  
## 
##   
## 
##   <br>  Created in NX1953.0.0  <br> 

class ICylindricalStiffnessDynamic(NXOpen.INXObject): 
    """ <summary> This class represents an Interface to the Cylindrical Stiffness dynamic. </summary> """


    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RCylindricalStiffnessDynamic
    ##   the R cylindrical stiffness dynamic   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Fields.ScalarFieldWrapper
    @property
    @abstractmethod
    def RCylindricalStiffnessDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RCylindricalStiffnessDynamic
          the R cylindrical stiffness dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RCylindricalStiffnessDynamic

    ##   the R cylindrical stiffness dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @RCylindricalStiffnessDynamic.setter
    def RCylindricalStiffnessDynamic(self, rDynamic: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RCylindricalStiffnessDynamic
          the R cylindrical stiffness dynamic   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RrCylindricalStiffnessDynamic
    ##   the RR cylindrical stiffness dynamic   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Fields.ScalarFieldWrapper
    @property
    @abstractmethod
    def RrCylindricalStiffnessDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RrCylindricalStiffnessDynamic
          the RR cylindrical stiffness dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RrCylindricalStiffnessDynamic

    ##   the RR cylindrical stiffness dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @RrCylindricalStiffnessDynamic.setter
    def RrCylindricalStiffnessDynamic(self, rrDynamic: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RrCylindricalStiffnessDynamic
          the RR cylindrical stiffness dynamic   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzCylindricalStiffnessDynamic
    ##   the RZ cylindrical stiffness dynamic   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Fields.ScalarFieldWrapper
    @property
    @abstractmethod
    def RzCylindricalStiffnessDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzCylindricalStiffnessDynamic
          the RZ cylindrical stiffness dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzCylindricalStiffnessDynamic

    ##   the RZ cylindrical stiffness dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @RzCylindricalStiffnessDynamic.setter
    def RzCylindricalStiffnessDynamic(self, rzDynamic: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzCylindricalStiffnessDynamic
          the RZ cylindrical stiffness dynamic   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZCylindricalStiffnessDynamic
    ##   the Z cylindrical stiffness dynamic   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Fields.ScalarFieldWrapper
    @property
    @abstractmethod
    def ZCylindricalStiffnessDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZCylindricalStiffnessDynamic
          the Z cylindrical stiffness dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZCylindricalStiffnessDynamic

    ##   the Z cylindrical stiffness dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @ZCylindricalStiffnessDynamic.setter
    def ZCylindricalStiffnessDynamic(self, zDynamic: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZCylindricalStiffnessDynamic
          the Z cylindrical stiffness dynamic   
            
         
        """
        pass
    
import NXOpen
##   @brief  This class represents an Interface to the Cylindrical stiffness.  
## 
##   
## 
##   <br>  Created in NX1953.0.0  <br> 

class ICylindricalStiffness(NXOpen.INXObject): 
    """ <summary> This class represents an Interface to the Cylindrical stiffness. </summary> """


    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RCylindricalStiffnessConstant
    ##   the R cylindrical stiffness constant   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    @abstractmethod
    def RCylindricalStiffnessConstant(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RCylindricalStiffnessConstant
          the R cylindrical stiffness constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RrCylindricalStiffnessConstant
    ##   the RR cylindrical stiffness constant   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    @abstractmethod
    def RrCylindricalStiffnessConstant(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RrCylindricalStiffnessConstant
          the RR cylindrical stiffness constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RzCylindricalStiffnessConstant
    ##   the RZ cylindrical stiffness constant   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    @abstractmethod
    def RzCylindricalStiffnessConstant(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RzCylindricalStiffnessConstant
          the RZ cylindrical stiffness constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ZCylindricalStiffnessConstant
    ##   the Z cylindrical stiffness constant   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    @abstractmethod
    def ZCylindricalStiffnessConstant(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ZCylindricalStiffnessConstant
          the Z cylindrical stiffness constant   
            
         
        """
        pass
    
import NXOpen
import NXOpen.Fields
##   @brief  This class represents an Interface to the CylindricalStructuralDamping dynamic.  
## 
##   
## 
##   <br>  Created in NX1953.0.0  <br> 

class ICylindricalStructuralDampingDynamic(NXOpen.INXObject): 
    """ <summary> This class represents an Interface to the CylindricalStructuralDamping dynamic. </summary> """


    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RCylindricalStructuralDampingDynamic
    ##   the R cylindrical structural damping dynamic   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Fields.ScalarFieldWrapper
    @property
    @abstractmethod
    def RCylindricalStructuralDampingDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RCylindricalStructuralDampingDynamic
          the R cylindrical structural damping dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RCylindricalStructuralDampingDynamic

    ##   the R cylindrical structural damping dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @RCylindricalStructuralDampingDynamic.setter
    def RCylindricalStructuralDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RCylindricalStructuralDampingDynamic
          the R cylindrical structural damping dynamic   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RrCylindricalStructuralDampingDynamic
    ##   the RR cylindrical structural damping dynamic   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Fields.ScalarFieldWrapper
    @property
    @abstractmethod
    def RrCylindricalStructuralDampingDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RrCylindricalStructuralDampingDynamic
          the RR cylindrical structural damping dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RrCylindricalStructuralDampingDynamic

    ##   the RR cylindrical structural damping dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @RrCylindricalStructuralDampingDynamic.setter
    def RrCylindricalStructuralDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RrCylindricalStructuralDampingDynamic
          the RR cylindrical structural damping dynamic   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzCylindricalStructuralDampingDynamic
    ##   the RZ cylindrical structural damping dynamic   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Fields.ScalarFieldWrapper
    @property
    @abstractmethod
    def RzCylindricalStructuralDampingDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzCylindricalStructuralDampingDynamic
          the RZ cylindrical structural damping dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzCylindricalStructuralDampingDynamic

    ##   the RZ cylindrical structural damping dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @RzCylindricalStructuralDampingDynamic.setter
    def RzCylindricalStructuralDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzCylindricalStructuralDampingDynamic
          the RZ cylindrical structural damping dynamic   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZCylindricalStructuralDampingDynamic
    ##   the Z cylindrical structural damping dynamic   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Fields.ScalarFieldWrapper
    @property
    @abstractmethod
    def ZCylindricalStructuralDampingDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZCylindricalStructuralDampingDynamic
          the Z cylindrical structural damping dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZCylindricalStructuralDampingDynamic

    ##   the Z cylindrical structural damping dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @ZCylindricalStructuralDampingDynamic.setter
    def ZCylindricalStructuralDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZCylindricalStructuralDampingDynamic
          the Z cylindrical structural damping dynamic   
            
         
        """
        pass
    
import NXOpen
##   @brief  This class represents an Interface to the CylindricalStructuralDamping constants.  
## 
##   
## 
##   <br>  Created in NX1953.0.0  <br> 

class ICylindricalStructuralDamping(NXOpen.INXObject): 
    """ <summary> This class represents an Interface to the CylindricalStructuralDamping constants. </summary> """


    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RCylindricalStructuralDampingConstant
    ##   the R cylindrical structural damping constant   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    @abstractmethod
    def RCylindricalStructuralDampingConstant(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RCylindricalStructuralDampingConstant
          the R cylindrical structural damping constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RrCylindricalStructuralDampingConstant
    ##   the RR structural damping constant   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    @abstractmethod
    def RrCylindricalStructuralDampingConstant(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RrCylindricalStructuralDampingConstant
          the RR structural damping constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RzCylindricalStructuralDampingConstant
    ##   the RZ structural damping constant   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    @abstractmethod
    def RzCylindricalStructuralDampingConstant(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RzCylindricalStructuralDampingConstant
          the RZ structural damping constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ZCylindricalStructuralDampingConstant
    ##   the Z cylindrical structural damping constant   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    @abstractmethod
    def ZCylindricalStructuralDampingConstant(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ZCylindricalStructuralDampingConstant
          the Z cylindrical structural damping constant   
            
         
        """
        pass
    
import NXOpen
import NXOpen.Fields
##   @brief  This class represents an Interface to the CylindricalViscousDamping dynamic.  
## 
##   
## 
##   <br>  Created in NX1953.0.0  <br> 

class ICylindricalViscousDampingDynamic(NXOpen.INXObject): 
    """ <summary> This class represents an Interface to the CylindricalViscousDamping dynamic. </summary> """


    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RCylindricalViscousDampingDynamic
    ##   the R cylindrical viscous damping dynamic   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Fields.ScalarFieldWrapper
    @property
    @abstractmethod
    def RCylindricalViscousDampingDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RCylindricalViscousDampingDynamic
          the R cylindrical viscous damping dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RCylindricalViscousDampingDynamic

    ##   the R cylindrical viscous damping dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @RCylindricalViscousDampingDynamic.setter
    def RCylindricalViscousDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RCylindricalViscousDampingDynamic
          the R cylindrical viscous damping dynamic   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RrCylindricalViscousDampingDynamic
    ##   the RR cylindrical viscous damping dynamic   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Fields.ScalarFieldWrapper
    @property
    @abstractmethod
    def RrCylindricalViscousDampingDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RrCylindricalViscousDampingDynamic
          the RR cylindrical viscous damping dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RrCylindricalViscousDampingDynamic

    ##   the RR cylindrical viscous damping dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @RrCylindricalViscousDampingDynamic.setter
    def RrCylindricalViscousDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RrCylindricalViscousDampingDynamic
          the RR cylindrical viscous damping dynamic   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzCylindricalViscousDampingDynamic
    ##   the RZ cylindrical viscous damping dynamic   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Fields.ScalarFieldWrapper
    @property
    @abstractmethod
    def RzCylindricalViscousDampingDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzCylindricalViscousDampingDynamic
          the RZ cylindrical viscous damping dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzCylindricalViscousDampingDynamic

    ##   the RZ cylindrical viscous damping dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @RzCylindricalViscousDampingDynamic.setter
    def RzCylindricalViscousDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzCylindricalViscousDampingDynamic
          the RZ cylindrical viscous damping dynamic   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZCylindricalViscousDampingDynamic
    ##   the Z cylindrical viscous damping dynamic   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Fields.ScalarFieldWrapper
    @property
    @abstractmethod
    def ZCylindricalViscousDampingDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZCylindricalViscousDampingDynamic
          the Z cylindrical viscous damping dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZCylindricalViscousDampingDynamic

    ##   the Z cylindrical viscous damping dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @ZCylindricalViscousDampingDynamic.setter
    def ZCylindricalViscousDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZCylindricalViscousDampingDynamic
          the Z cylindrical viscous damping dynamic   
            
         
        """
        pass
    
import NXOpen
##   @brief  This class represents an Interface to the CylindricalViscousDamping constants.  
## 
##   
## 
##   <br>  Created in NX1953.0.0  <br> 

class ICylindricalViscousDamping(NXOpen.INXObject): 
    """ <summary> This class represents an Interface to the CylindricalViscousDamping constants. </summary> """


    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RCylindricalViscousDampingConstant
    ##   the R cylindrical viscous damping constant   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    @abstractmethod
    def RCylindricalViscousDampingConstant(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RCylindricalViscousDampingConstant
          the R cylindrical viscous damping constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RrCylindricalViscousDampingConstant
    ##   the RR cylindrical viscous damping constant   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    @abstractmethod
    def RrCylindricalViscousDampingConstant(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RrCylindricalViscousDampingConstant
          the RR cylindrical viscous damping constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RzCylindricalViscousDampingConstant
    ##   the RZ cylindrical viscous damping constant   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    @abstractmethod
    def RzCylindricalViscousDampingConstant(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RzCylindricalViscousDampingConstant
          the RZ cylindrical viscous damping constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ZCylindricalViscousDampingConstant
    ##   the Z cylindrical viscous damping constant   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    @abstractmethod
    def ZCylindricalViscousDampingConstant(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ZCylindricalViscousDampingConstant
          the Z cylindrical viscous damping constant   
            
         
        """
        pass
    
import NXOpen
##   @brief  This class represents an Interface to the Diameter parameters.  
## 
##   
## 
##   <br>  Created in NX12.0.0  <br> 

class IDiameter(NXOpen.INXObject): 
    """ <summary> This class represents an Interface to the Diameter parameters. </summary> """


    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Coefficient
    ##   the coefficient for formula defined diameter   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    @abstractmethod
    def Coefficient(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Coefficient
          the coefficient for formula defined diameter   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Diameter
    ##   the connection diameter   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    @abstractmethod
    def Diameter(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Diameter
          the connection diameter   
            
         
        """
        pass
    
    ## Getter for property: (@link DiameterType NXOpen.CAE.Connections.DiameterType@endlink) DiameterType
    ##   the connection diameter type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return DiameterType
    @property
    @abstractmethod
    def DiameterType(self) -> DiameterType:
        """
        Getter for property: (@link DiameterType NXOpen.CAE.Connections.DiameterType@endlink) DiameterType
          the connection diameter type   
            
         
        """
        pass
    
    ## Setter for property: (@link DiameterType NXOpen.CAE.Connections.DiameterType@endlink) DiameterType

    ##   the connection diameter type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @DiameterType.setter
    def DiameterType(self, diameterType: DiameterType):
        """
        Setter for property: (@link DiameterType NXOpen.CAE.Connections.DiameterType@endlink) DiameterType
          the connection diameter type   
            
         
        """
        pass
    
    ## Getter for property: (str) TableFile
    ##   the table file used to compute the diameter   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return str
    @property
    @abstractmethod
    def TableFile(self) -> str:
        """
        Getter for property: (str) TableFile
          the table file used to compute the diameter   
            
         
        """
        pass
    
    ## Setter for property: (str) TableFile

    ##   the table file used to compute the diameter   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @TableFile.setter
    def TableFile(self, tableFile: str):
        """
        Setter for property: (str) TableFile
          the table file used to compute the diameter   
            
         
        """
        pass
    
    ##  Gets manual adjustent state. 
    ##  @return state (bool): .
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    @abstractmethod
    def GetManualAdjustment(connection: IDiameter) -> bool:
        """
         Gets manual adjustent state. 
         @return state (bool): .
        """
        pass
    
    ##  Gets manual adjustent factor. 
    ##  @return factor (@link NXOpen.Expression NXOpen.Expression@endlink): .
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    @abstractmethod
    def GetManualAdjustmentFactor(connection: IDiameter) -> NXOpen.Expression:
        """
         Gets manual adjustent factor. 
         @return factor (@link NXOpen.Expression NXOpen.Expression@endlink): .
        """
        pass
    
    ##  Gets supported diameter types of connection. 
    ##  @return types (@link DiameterType List[NXOpen.CAE.Connections.DiameterType]@endlink):  Supported CSys Types .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    @abstractmethod
    def GetSupportedDiameterTypes(connection: IDiameter) -> List[DiameterType]:
        """
         Gets supported diameter types of connection. 
         @return types (@link DiameterType List[NXOpen.CAE.Connections.DiameterType]@endlink):  Supported CSys Types .
        """
        pass
    
    ##  Sets manual adjustent state. 
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="state"> (bool) </param>
    @abstractmethod
    def SetManualAdjustment(connection: IDiameter, state: bool) -> None:
        """
         Sets manual adjustent state. 
        """
        pass
    
import NXOpen
##   @brief  This class represents an interface to the connection's degrees of freedom combination.  
## 
##   
## 
##   <br>  Created in NX12.0.0  <br> 

class IDofCombination(NXOpen.INXObject): 
    """ <summary> This class represents an interface to the connection's degrees of freedom combination. </summary> """


    ## Getter for property: (@link DofCombination NXOpen.CAE.Connections.DofCombination@endlink) DofCombination
    ##   the degrees of freedom combination type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return DofCombination
    @property
    @abstractmethod
    def DofCombination(self) -> DofCombination:
        """
        Getter for property: (@link DofCombination NXOpen.CAE.Connections.DofCombination@endlink) DofCombination
          the degrees of freedom combination type   
            
         
        """
        pass
    
    ## Setter for property: (@link DofCombination NXOpen.CAE.Connections.DofCombination@endlink) DofCombination

    ##   the degrees of freedom combination type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @DofCombination.setter
    def DofCombination(self, type: DofCombination):
        """
        Setter for property: (@link DofCombination NXOpen.CAE.Connections.DofCombination@endlink) DofCombination
          the degrees of freedom combination type   
            
         
        """
        pass
    
import NXOpen
##   @brief  This class represents an interface to the connection's degrees of freedom.  
## 
##   
## 
##   <br>  Created in NX12.0.0  <br> 

class IDof(NXOpen.INXObject): 
    """ <summary> This class represents an interface to the connection's degrees of freedom. </summary> """


    ##  Get the specified degrees of freedom  
    ##  @return type (@link DofType NXOpen.CAE.Connections.DofType@endlink): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="dof"> (@link Dof NXOpen.CAE.Connections.Dof@endlink) </param>
    @abstractmethod
    def GetDof(connection: IDof, dof: Dof) -> DofType:
        """
         Get the specified degrees of freedom  
         @return type (@link DofType NXOpen.CAE.Connections.DofType@endlink): .
        """
        pass
    
    ##  Set the specified degrees of freedom  
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ## <param name="dof"> (@link Dof NXOpen.CAE.Connections.Dof@endlink) </param>
    ## <param name="type"> (@link DofType NXOpen.CAE.Connections.DofType@endlink) </param>
    @abstractmethod
    def SetDof(connection: IDof, dof: Dof, type: DofType) -> None:
        """
         Set the specified degrees of freedom  
        """
        pass
    
import NXOpen
##   @brief  This interface offers access to the flanges of a connection (SpotWeld for example).
##         The flanges are used for specifying the connecting surfaces of the connection. Each flange can have one or more entities like meshes, elements etc.
##           
## 
##   
## 
##   <br>  Created in NX12.0.0  <br> 

class IFlangesContainer(NXOpen.INXObject): 
    """ <summary> This interface offers access to the flanges of a connection (SpotWeld for example).
        The flanges are used for specifying the connecting surfaces of the connection. Each flange can have one or more entities like meshes, elements etc.
         </summary> """


    ## Getter for property: (int) NumberOfFlanges
    ##   the number of flanges.  
    ##    When changing the number of flanges this is not applied till an update is performed by calling @link Update::DoUpdate Update::DoUpdate@endlink    
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return int
    @property
    @abstractmethod
    def NumberOfFlanges(self) -> int:
        """
        Getter for property: (int) NumberOfFlanges
          the number of flanges.  
           When changing the number of flanges this is not applied till an update is performed by calling @link Update::DoUpdate Update::DoUpdate@endlink    
         
        """
        pass
    
    ## Setter for property: (int) NumberOfFlanges

    ##   the number of flanges.  
    ##    When changing the number of flanges this is not applied till an update is performed by calling @link Update::DoUpdate Update::DoUpdate@endlink    
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @NumberOfFlanges.setter
    def NumberOfFlanges(self, numberOfFlanges: int):
        """
        Setter for property: (int) NumberOfFlanges
          the number of flanges.  
           When changing the number of flanges this is not applied till an update is performed by calling @link Update::DoUpdate Update::DoUpdate@endlink    
         
        """
        pass
    
    ##  Add entities to flange. Changes are not applied till an update is performed by calling @link Update::DoUpdate Update::DoUpdate@endlink  
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##  Flange entities 
    @abstractmethod
    def AddFlangeEntities(connection: IFlangesContainer, flangeIndex: int, entities: List[NXOpen.TaggedObject]) -> None:
        """
         Add entities to flange. Changes are not applied till an update is performed by calling @link Update::DoUpdate Update::DoUpdate@endlink  
        """
        pass
    
    ##  Gets entities from flange. These can be meshes, elements, groups. 
    ##  @return entities (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink):  Flange entities .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="flangeIndex"> (int) </param>
    @abstractmethod
    def GetFlangeEntities(connection: IFlangesContainer, flangeIndex: int) -> List[NXOpen.TaggedObject]:
        """
         Gets entities from flange. These can be meshes, elements, groups. 
         @return entities (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink):  Flange entities .
        """
        pass
    
    ##  Retrieve the max number of flanges supported by this connection 
    ##  @return number (int): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    @staticmethod
    @abstractmethod
    def GetMaxNumberOfFlanges(connection: IFlangesContainer) -> int:
        """
         Retrieve the max number of flanges supported by this connection 
         @return number (int): .
        """
        pass
    
    ##  Retrieve the minimum number of flanges supported by this connection 
    ##  @return number (int): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    @staticmethod
    @abstractmethod
    def GetMinNumberOfFlanges(connection: IFlangesContainer) -> int:
        """
         Retrieve the minimum number of flanges supported by this connection 
         @return number (int): .
        """
        pass
    
    ##  Remove entities from flange. Changes are not applied till an update is performed by calling @link Update::DoUpdate Update::DoUpdate@endlink  
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##  Flange entities 
    @abstractmethod
    def RemoveFlangeEntities(connection: IFlangesContainer, flangeIndex: int, entities: List[NXOpen.TaggedObject]) -> None:
        """
         Remove entities from flange. Changes are not applied till an update is performed by calling @link Update::DoUpdate Update::DoUpdate@endlink  
        """
        pass
    
import NXOpen
##   @brief  This class represents an Interface to the Friction constants.  
## 
##   
## 
##   <br>  Created in NX1847.0.0  <br> 

class IFriction(NXOpen.INXObject): 
    """ <summary> This class represents an Interface to the Friction constants. </summary> """


    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) CharacteristicLengthRadius
    ##   the radius characteristic length used by Revolute and Spherical Kinematic   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    @abstractmethod
    def CharacteristicLengthRadius(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) CharacteristicLengthRadius
          the radius characteristic length used by Revolute and Spherical Kinematic   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) FrictionCoefficient
    ##   the friction coefficient   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    @abstractmethod
    def FrictionCoefficient(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) FrictionCoefficient
          the friction coefficient   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) TighteningForce
    ##   the tightening force   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    @abstractmethod
    def TighteningForce(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) TighteningForce
          the tightening force   
            
         
        """
        pass
    
    ## Getter for property: (bool) UseFriction
    ##   the flag indicating whether to use friction parameters or not   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return bool
    @property
    @abstractmethod
    def UseFriction(self) -> bool:
        """
        Getter for property: (bool) UseFriction
          the flag indicating whether to use friction parameters or not   
            
         
        """
        pass
    
    ## Setter for property: (bool) UseFriction

    ##   the flag indicating whether to use friction parameters or not   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @UseFriction.setter
    def UseFriction(self, useFriction: bool):
        """
        Setter for property: (bool) UseFriction
          the flag indicating whether to use friction parameters or not   
            
         
        """
        pass
    
import NXOpen
##   @brief  This class represents an Interface to the Height parameters.  
## 
##   
## 
##   <br>  Created in NX12.0.0  <br> 

class IHeight(NXOpen.INXObject): 
    """ <summary> This class represents an Interface to the Height parameters. </summary> """


    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Height
    ##   the height value   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    @abstractmethod
    def Height(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Height
          the height value   
            
         
        """
        pass
    
    ## Getter for property: (@link HeightType NXOpen.CAE.Connections.HeightType@endlink) HeightType
    ##   the connection height type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return HeightType
    @property
    @abstractmethod
    def HeightType(self) -> HeightType:
        """
        Getter for property: (@link HeightType NXOpen.CAE.Connections.HeightType@endlink) HeightType
          the connection height type   
            
         
        """
        pass
    
    ## Setter for property: (@link HeightType NXOpen.CAE.Connections.HeightType@endlink) HeightType

    ##   the connection height type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @HeightType.setter
    def HeightType(self, heightType: HeightType):
        """
        Setter for property: (@link HeightType NXOpen.CAE.Connections.HeightType@endlink) HeightType
          the connection height type   
            
         
        """
        pass
    
    ##  Gets supported height types of connection. 
    ##  @return types (@link HeightType List[NXOpen.CAE.Connections.HeightType]@endlink):  Supported CSys Types .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    @abstractmethod
    def GetSupportedHeightTypes(connection: IHeight) -> List[HeightType]:
        """
         Gets supported height types of connection. 
         @return types (@link HeightType List[NXOpen.CAE.Connections.HeightType]@endlink):  Supported CSys Types .
        """
        pass
    
import NXOpen
import NXOpen.Assemblies
import NXOpen.Features
##   @brief  This class represents an Interface to the Join Data Container.  
## 
##   
## 
##   <br>  Created in NX2007.0.0  <br> 

class IJoinDataContainer(NXOpen.INXObject): 
    """ <summary> This class represents an Interface to the Join Data Container. </summary> """


    ##  Add a join data to the connection 
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##  The join feature 
    @abstractmethod
    def AddJoinData(connection: IJoinDataContainer, feature: NXOpen.Features.Feature, component: NXOpen.Assemblies.Component) -> None:
        """
         Add a join data to the connection 
        """
        pass
    
    ##  Get all join data features from the connection 
    ##  @return A tuple consisting of (features, components). 
    ##  - features is: @link NXOpen.Features.Feature List[NXOpen.Features.Feature]@endlink. The join features .
    ##  - components is: @link NXOpen.Assemblies.Component List[NXOpen.Assemblies.Component]@endlink. The CAD components of the join features .

    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    @abstractmethod
    def GetAllJoinFeatures(connection: IJoinDataContainer) -> Tuple[List[NXOpen.Features.Feature], List[NXOpen.Assemblies.Component]]:
        """
         Get all join data features from the connection 
         @return A tuple consisting of (features, components). 
         - features is: @link NXOpen.Features.Feature List[NXOpen.Features.Feature]@endlink. The join features .
         - components is: @link NXOpen.Assemblies.Component List[NXOpen.Assemblies.Component]@endlink. The CAD components of the join features .

        """
        pass
    
    ##  Get a join data feature from the connection 
    ##  @return A tuple consisting of (feature, component). 
    ##  - feature is: @link NXOpen.Features.Feature NXOpen.Features.Feature@endlink. The join feature .
    ##  - component is: @link NXOpen.Assemblies.Component NXOpen.Assemblies.Component@endlink. The CAD component of the join feature .

    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    ##  The join data index 
    @staticmethod
    @abstractmethod
    def GetJoinFeature(connection: IJoinDataContainer, index: int) -> Tuple[NXOpen.Features.Feature, NXOpen.Assemblies.Component]:
        """
         Get a join data feature from the connection 
         @return A tuple consisting of (feature, component). 
         - feature is: @link NXOpen.Features.Feature NXOpen.Features.Feature@endlink. The join feature .
         - component is: @link NXOpen.Assemblies.Component NXOpen.Assemblies.Component@endlink. The CAD component of the join feature .

        """
        pass
    
    ##  Get the number of join data from the connection 
    ##  @return numberOfJoinData (int):  The number of join data .
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    @abstractmethod
    def GetNumberOfJoinData(connection: IJoinDataContainer) -> int:
        """
         Get the number of join data from the connection 
         @return numberOfJoinData (int):  The number of join data .
        """
        pass
    
    ##  Remove all join data from the connection 
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    @staticmethod
    @abstractmethod
    def RemoveAllJoinData(connection: IJoinDataContainer) -> None:
        """
         Remove all join data from the connection 
        """
        pass
    
    ##  Add a join data to the connection 
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##  The join feature 
    @abstractmethod
    def RemoveJoinData(connection: IJoinDataContainer, feature: NXOpen.Features.Feature, component: NXOpen.Assemblies.Component) -> None:
        """
         Add a join data to the connection 
        """
        pass
    
    ##  Remove a join data from the connection 
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##  The join data index 
    @abstractmethod
    def RemoveJoinDataByIndex(connection: IJoinDataContainer, index: int) -> None:
        """
         Remove a join data from the connection 
        """
        pass
    
    ##  Set the join data of the connection 
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##  The join features 
    @abstractmethod
    def SetJoinData(connection: IJoinDataContainer, features: List[NXOpen.Features.Feature], components: List[NXOpen.Assemblies.Component]) -> None:
        """
         Set the join data of the connection 
        """
        pass
    
    ##  Unlink all join data from the connection 
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    @staticmethod
    @abstractmethod
    def UnlinkJoinData(connection: IJoinDataContainer) -> None:
        """
         Unlink all join data from the connection 
        """
        pass
    
import NXOpen
##   @brief  This class represents an Interface to the Diameter parameters.  
## 
##   
## 
##   <br>  Created in NX12.0.0  <br> 

class ILineDiscretization(NXOpen.INXObject): 
    """ <summary> This class represents an Interface to the Diameter parameters. </summary> """


    ## Getter for property: (@link DiscretizationMethod NXOpen.CAE.Connections.DiscretizationMethod@endlink) DiscretizationMethod
    ##   the discretization method   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return DiscretizationMethod
    @property
    @abstractmethod
    def DiscretizationMethod(self) -> DiscretizationMethod:
        """
        Getter for property: (@link DiscretizationMethod NXOpen.CAE.Connections.DiscretizationMethod@endlink) DiscretizationMethod
          the discretization method   
            
         
        """
        pass
    
    ## Setter for property: (@link DiscretizationMethod NXOpen.CAE.Connections.DiscretizationMethod@endlink) DiscretizationMethod

    ##   the discretization method   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @DiscretizationMethod.setter
    def DiscretizationMethod(self, method: DiscretizationMethod):
        """
        Setter for property: (@link DiscretizationMethod NXOpen.CAE.Connections.DiscretizationMethod@endlink) DiscretizationMethod
          the discretization method   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) DistanceFromStart
    ##   the line Discretization distance from start   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    @abstractmethod
    def DistanceFromStart(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) DistanceFromStart
          the line Discretization distance from start   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) DistanceToEnd
    ##   the line Discretization distance to end   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    @abstractmethod
    def DistanceToEnd(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) DistanceToEnd
          the line Discretization distance to end   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) LengthStep
    ##   the line Discretization length step   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    @abstractmethod
    def LengthStep(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) LengthStep
          the line Discretization length step   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxLengthStep
    ##   the line Discretization max length step   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    @abstractmethod
    def MaxLengthStep(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxLengthStep
          the line Discretization max length step   
            
         
        """
        pass
    
    ## Getter for property: (int) NumberOfDiscretizationPoints
    ##   the number of connections   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return int
    @property
    @abstractmethod
    def NumberOfDiscretizationPoints(self) -> int:
        """
        Getter for property: (int) NumberOfDiscretizationPoints
          the number of connections   
            
         
        """
        pass
    
    ## Setter for property: (int) NumberOfDiscretizationPoints

    ##   the number of connections   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @NumberOfDiscretizationPoints.setter
    def NumberOfDiscretizationPoints(self, num: int):
        """
        Setter for property: (int) NumberOfDiscretizationPoints
          the number of connections   
            
         
        """
        pass
    
    ## Getter for property: (bool) UseMaxLengthStep
    ##   the usage of max length step   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return bool
    @property
    @abstractmethod
    def UseMaxLengthStep(self) -> bool:
        """
        Getter for property: (bool) UseMaxLengthStep
          the usage of max length step   
            
         
        """
        pass
    
    ## Setter for property: (bool) UseMaxLengthStep

    ##   the usage of max length step   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @UseMaxLengthStep.setter
    def UseMaxLengthStep(self, use: bool):
        """
        Setter for property: (bool) UseMaxLengthStep
          the usage of max length step   
            
         
        """
        pass
    
    ## Getter for property: (bool) UseOriginalNodesOfConnection
    ##   the usage of original nodes of connection   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return bool
    @property
    @abstractmethod
    def UseOriginalNodesOfConnection(self) -> bool:
        """
        Getter for property: (bool) UseOriginalNodesOfConnection
          the usage of original nodes of connection   
            
         
        """
        pass
    
    ## Setter for property: (bool) UseOriginalNodesOfConnection

    ##   the usage of original nodes of connection   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @UseOriginalNodesOfConnection.setter
    def UseOriginalNodesOfConnection(self, use: bool):
        """
        Setter for property: (bool) UseOriginalNodesOfConnection
          the usage of original nodes of connection   
            
         
        """
        pass
    
import NXOpen
##   @brief  This class represents an Interface to the Diameter parameters.  
## 
##   
## 
##   <br>  Created in NX12.0.0  <br> 

class ILineOffset(NXOpen.INXObject): 
    """ <summary> This class represents an Interface to the Diameter parameters. </summary> """


    ##  Gets the line offset distance 
    ##  @return distance (@link NXOpen.Expression NXOpen.Expression@endlink): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="lindeDefinitionIndex"> (int) </param>
    @abstractmethod
    def GetOffsetDistance(connectionTag: ILineOffset, lindeDefinitionIndex: int) -> NXOpen.Expression:
        """
         Gets the line offset distance 
         @return distance (@link NXOpen.Expression NXOpen.Expression@endlink): .
        """
        pass
    
    ##  Gets the line offset vector 
    ##  @return offsetvector (@link NXOpen.Direction NXOpen.Direction@endlink): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="lindeDefinitionIndex"> (int) </param>
    @abstractmethod
    def GetOffsetVector(connectionTag: ILineOffset, lindeDefinitionIndex: int) -> NXOpen.Direction:
        """
         Gets the line offset vector 
         @return offsetvector (@link NXOpen.Direction NXOpen.Direction@endlink): .
        """
        pass
    
    ##  Sets the line offset vector 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ## <param name="lindeDefinitionIndex"> (int) </param>
    ## <param name="offsetvector"> (@link NXOpen.Direction NXOpen.Direction@endlink) </param>
    @abstractmethod
    def SetOffsetVector(connectionTag: ILineOffset, lindeDefinitionIndex: int, offsetvector: NXOpen.Direction) -> None:
        """
         Sets the line offset vector 
        """
        pass
    
import NXOpen
##   @brief  This class represents an Interface to the Locations parameters.  
## 
##   
## 
##   <br>  Created in NX12.0.0  <br> 

class ILocationsContainer(NXOpen.INXObject): 
    """ <summary> This class represents an Interface to the Locations parameters. </summary> """


    ##  Convert a location to coordinates. The location is given by its index 
    ##  @return location (@link Location NXOpen.CAE.Connections.Location@endlink):  The created coordinates type location .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##  The index of definition  
    @abstractmethod
    def ConvertLocationToCoordinatesType(connection: ILocationsContainer, indexOfDefinition: int, index: int) -> Location:
        """
         Convert a location to coordinates. The location is given by its index 
         @return location (@link Location NXOpen.CAE.Connections.Location@endlink):  The created coordinates type location .
        """
        pass
    
    ##  Get a node location to connection location list 
    ##  @return location (@link Location NXOpen.CAE.Connections.Location@endlink):  The location .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ##  The index of definition  
    @abstractmethod
    def GetLocation(connection: ILocationsContainer, indexOfDefinition: int, indexOfLocation: int) -> Location:
        """
         Get a node location to connection location list 
         @return location (@link Location NXOpen.CAE.Connections.Location@endlink):  The location .
        """
        pass
    
    ##  Gets the number of line offset definitions 
    ##  @return numberOfDefinitions (int):  The number of definitions .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    @abstractmethod
    def GetNumberOfDefinitions(connectionTag: ILocationsContainer) -> int:
        """
         Gets the number of line offset definitions 
         @return numberOfDefinitions (int):  The number of definitions .
        """
        pass
    
    ##  Get a node location to connection location list 
    ##  @return number_of_locations (int):  The number of locations .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ##  The index of definition  
    @abstractmethod
    def GetNumberOfLocations(connection: ILocationsContainer, indexOfDefinition: int) -> int:
        """
         Get a node location to connection location list 
         @return number_of_locations (int):  The number of locations .
        """
        pass
    
    ##  Move the location by number of positions 
    ##  @return success (bool):  The operation result .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ##  The index of definition  
    @abstractmethod
    def MoveLocation(connection: ILocationsContainer, indexOfDefinition: int, indexOfLocation: int, numberOfPositions: int) -> bool:
        """
         Move the location by number of positions 
         @return success (bool):  The operation result .
        """
        pass
    
    ##  Remove a location from connection location list 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##  The index of definition  
    @abstractmethod
    def RemoveLocation(connection: ILocationsContainer, indexOfDefinition: int, indexOfLocation: int) -> None:
        """
         Remove a location from connection location list 
        """
        pass
    
import NXOpen
import NXOpen.CAE
##   @brief  This class represents an Interface to the Multi Point Locations container.  
## 
##   
## 
##   <br>  Created in NX12.0.0  <br> 

class ILocationsMultiPointContainer(NXOpen.INXObject): 
    """ <summary> This class represents an Interface to the Multi Point Locations container. </summary> """


    ##  Adds a Selection Recipe to connection location list 
    ##  @return location (@link SelectionRecipeLocation NXOpen.CAE.Connections.SelectionRecipeLocation@endlink):  The created selection recipe type location .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##  The index of definition  
    @abstractmethod
    def AddLocationSelectionRecipe(connection: ILocationsMultiPointContainer, indexOfDefinition: int, selectionRecipe: NXOpen.CAE.SelectionRecipe) -> SelectionRecipeLocation:
        """
         Adds a Selection Recipe to connection location list 
         @return location (@link SelectionRecipeLocation NXOpen.CAE.Connections.SelectionRecipeLocation@endlink):  The created selection recipe type location .
        """
        pass
    
import NXOpen
import NXOpen.CAE
##   @brief  This class represents an Interface to the Locations parameters.  
## 
##   
## 
##   <br>  Created in NX12.0.0  <br> 

class ILocationsSinglePointContainer(NXOpen.INXObject): 
    """ <summary> This class represents an Interface to the Locations parameters. </summary> """


    ##  Adds a coordinates location to connection location list 
    ##  @return location (@link CoordinatesLocation NXOpen.CAE.Connections.CoordinatesLocation@endlink):  The created coordinates type location .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##  The index of definition  
    @abstractmethod
    def AddLocationCoordinates(connection: ILocationsSinglePointContainer, indexOfDefinition: int, coordinates: NXOpen.Point3d) -> CoordinatesLocation:
        """
         Adds a coordinates location to connection location list 
         @return location (@link CoordinatesLocation NXOpen.CAE.Connections.CoordinatesLocation@endlink):  The created coordinates type location .
        """
        pass
    
    ##  Adds a node location to connection location list 
    ##  @return location (@link NodeLocation NXOpen.CAE.Connections.NodeLocation@endlink):  The node type location .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##  The index of definition  
    @abstractmethod
    def AddLocationNode(connection: ILocationsSinglePointContainer, indexOfDefinition: int, node: NXOpen.CAE.FENode) -> NodeLocation:
        """
         Adds a node location to connection location list 
         @return location (@link NodeLocation NXOpen.CAE.Connections.NodeLocation@endlink):  The node type location .
        """
        pass
    
    ##  Adds a point location to connection location list 
    ##  @return location (@link PointLocation NXOpen.CAE.Connections.PointLocation@endlink):  The created point type location .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##  The index of definition  
    @abstractmethod
    def AddLocationPoint(connection: ILocationsSinglePointContainer, indexOfDefinition: int, point: NXOpen.Point) -> PointLocation:
        """
         Adds a point location to connection location list 
         @return location (@link PointLocation NXOpen.CAE.Connections.PointLocation@endlink):  The created point type location .
        """
        pass
    
import NXOpen
import NXOpen.CAE
##   @brief  This class represents an Interface to the Locations parameters.  
## 
##   
## 
##   <br>  Created in NX12.0.0  <br> 

class ILocationsWithDirContainer(NXOpen.INXObject): 
    """ <summary> This class represents an Interface to the Locations parameters. </summary> """


    ##  Adds a coordinates location with direction definited by coordinates to connection location list 
    ##  @return location (@link LocationWithDir NXOpen.CAE.Connections.LocationWithDir@endlink):  The created coordinates with direction type location .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##  The index of definition  
    @abstractmethod
    def AddLocationCoordinatesWithDirectionCoordinates(connection: ILocationsWithDirContainer, indexOfDefinition: int, point: NXOpen.Point, direction: NXOpen.Point) -> LocationWithDir:
        """
         Adds a coordinates location with direction definited by coordinates to connection location list 
         @return location (@link LocationWithDir NXOpen.CAE.Connections.LocationWithDir@endlink):  The created coordinates with direction type location .
        """
        pass
    
    ##  Adds a coordinates location with direction definited by vector to connection location list 
    ##  @return location (@link LocationWithDir NXOpen.CAE.Connections.LocationWithDir@endlink):  The created point with direction type location .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##  The index of definition  
    @abstractmethod
    def AddLocationCoordinatesWithDirectionSelectionRecipes(connection: ILocationsWithDirContainer, indexOfDefinition: int, startSelectionRecipe: NXOpen.CAE.SelectionRecipe, endSelectionRecipe: NXOpen.CAE.SelectionRecipe) -> LocationWithDir:
        """
         Adds a coordinates location with direction definited by vector to connection location list 
         @return location (@link LocationWithDir NXOpen.CAE.Connections.LocationWithDir@endlink):  The created point with direction type location .
        """
        pass
    
    ##  Adds a coordinates location with direction definited by vector to connection location list 
    ##  @return location (@link LocationWithDir NXOpen.CAE.Connections.LocationWithDir@endlink):  The created point with direction type location .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##  The index of definition  
    @abstractmethod
    def AddLocationCoordinatesWithDirectionVector(connection: ILocationsWithDirContainer, indexOfDefinition: int, masterPoint: NXOpen.Point, direction: NXOpen.Direction) -> LocationWithDir:
        """
         Adds a coordinates location with direction definited by vector to connection location list 
         @return location (@link LocationWithDir NXOpen.CAE.Connections.LocationWithDir@endlink):  The created point with direction type location .
        """
        pass
    
import NXOpen
import NXOpen.CAE
##   @brief  This class represents an Interface to the Locations With Discretization container.  
## 
##   
## 
##   <br>  Created in NX12.0.0  <br> 

class ILocationsWithDiscretizationContainer(NXOpen.INXObject): 
    """ <summary> This class represents an Interface to the Locations With Discretization container. </summary> """


    ##  Adds a curve location to connection location list 
    ##  @return location (@link CurveLocation NXOpen.CAE.Connections.CurveLocation@endlink):  The created curve type location .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##  Curve used for location creation 
    @abstractmethod
    def AddLocationCurve(connection: ILocationsWithDiscretizationContainer, indexOfDefinition: int, curve: NXOpen.IBaseCurve) -> CurveLocation:
        """
         Adds a curve location to connection location list 
         @return location (@link CurveLocation NXOpen.CAE.Connections.CurveLocation@endlink):  The created curve type location .
        """
        pass
    
    ##  Adds Fe Edges to connection location list 
    ##  @return location (@link FeEdgesLocation NXOpen.CAE.Connections.FeEdgesLocation@endlink):  The created edge group type location .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##  Edges used for location 
    @abstractmethod
    def AddLocationFeEdges(connection: ILocationsWithDiscretizationContainer, indexOfDefinition: int, edges: List[NXOpen.CAE.FEElemEdge]) -> FeEdgesLocation:
        """
         Adds Fe Edges to connection location list 
         @return location (@link FeEdgesLocation NXOpen.CAE.Connections.FeEdgesLocation@endlink):  The created edge group type location .
        """
        pass
    
    ##  Adds a group location to connection location list 
    ##  @return location (@link GroupLocation NXOpen.CAE.Connections.GroupLocation@endlink):  The created group type location .
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##  Group used for location creation 
    @abstractmethod
    def AddLocationGroup(connection: ILocationsWithDiscretizationContainer, indexOfDefinition: int, group: NXOpen.CAE.CaeGroup) -> GroupLocation:
        """
         Adds a group location to connection location list 
         @return location (@link GroupLocation NXOpen.CAE.Connections.GroupLocation@endlink):  The created group type location .
        """
        pass
    
    ##  Adds a series of coordinates location to connection location list 
    ##  @return location (@link CoordinatesSeriesLocation NXOpen.CAE.Connections.CoordinatesSeriesLocation@endlink):  The coordinates series type location .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##  The location coordinates 
    @abstractmethod
    def AddLocationSeriesOfCoordinates(connection: ILocationsWithDiscretizationContainer, indexOfDefinition: int, coordinates: List[NXOpen.Point3d]) -> CoordinatesSeriesLocation:
        """
         Adds a series of coordinates location to connection location list 
         @return location (@link CoordinatesSeriesLocation NXOpen.CAE.Connections.CoordinatesSeriesLocation@endlink):  The coordinates series type location .
        """
        pass
    
    ##  Adds a series of nodes location to connection location list 
    ##  @return location (@link NodeSeriesLocation NXOpen.CAE.Connections.NodeSeriesLocation@endlink):  The node series type location .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##  The index of definition  
    @abstractmethod
    def AddLocationSeriesOfNodes(connection: ILocationsWithDiscretizationContainer, indexOfDefinition: int, nodes: List[NXOpen.CAE.FENode]) -> NodeSeriesLocation:
        """
         Adds a series of nodes location to connection location list 
         @return location (@link NodeSeriesLocation NXOpen.CAE.Connections.NodeSeriesLocation@endlink):  The node series type location .
        """
        pass
    
    ##  Adds a series of points location to connection location list 
    ##  @return location (@link PointSeriesLocation NXOpen.CAE.Connections.PointSeriesLocation@endlink):  The point series type location .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##  The index of definition  
    @abstractmethod
    def AddLocationSeriesOfPoints(connection: ILocationsWithDiscretizationContainer, indexOfDefinition: int, points: List[NXOpen.Point]) -> PointSeriesLocation:
        """
         Adds a series of points location to connection location list 
         @return location (@link PointSeriesLocation NXOpen.CAE.Connections.PointSeriesLocation@endlink):  The point series type location .
        """
        pass
    
import NXOpen
##   @brief  This class represents an Interface to the Mass Both Target.  
## 
##   
## 
##   <br>  Created in NX1980.0.0  <br> 

class IMassBothTargets(NXOpen.INXObject): 
    """ <summary> This class represents an Interface to the Mass Both Target. </summary> """


    ## Getter for property: (bool) IsMassOnBothTargets
    ##   the isMassOnBothTargets   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return bool
    @property
    @abstractmethod
    def IsMassOnBothTargets(self) -> bool:
        """
        Getter for property: (bool) IsMassOnBothTargets
          the isMassOnBothTargets   
            
         
        """
        pass
    
    ## Setter for property: (bool) IsMassOnBothTargets

    ##   the isMassOnBothTargets   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @IsMassOnBothTargets.setter
    def IsMassOnBothTargets(self, isMassOnBothTargets: bool):
        """
        Setter for property: (bool) IsMassOnBothTargets
          the isMassOnBothTargets   
            
         
        """
        pass
    
import NXOpen
##   @brief  This class represents an Interface to the Lumped Mass panel connection parameters.  
## 
##   
## 
##   <br>  Created in NX1847.0.0  <br> 

class IMassConnectivity(NXOpen.INXObject): 
    """ <summary> This class represents an Interface to the Lumped Mass panel connection parameters. </summary> """


    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ExpansionRadiusFactorTolerance
    ##   the expansion radius factor   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    @abstractmethod
    def ExpansionRadiusFactorTolerance(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ExpansionRadiusFactorTolerance
          the expansion radius factor   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ExpansionRadiusTolerance
    ##   the expansion radius   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    @abstractmethod
    def ExpansionRadiusTolerance(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ExpansionRadiusTolerance
          the expansion radius   
            
         
        """
        pass
    
    ## Getter for property: (@link MassConnectivityType NXOpen.CAE.Connections.MassConnectivityType@endlink) MassConnectivityType
    ##   the mass connection type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return MassConnectivityType
    @property
    @abstractmethod
    def MassConnectivityType(self) -> MassConnectivityType:
        """
        Getter for property: (@link MassConnectivityType NXOpen.CAE.Connections.MassConnectivityType@endlink) MassConnectivityType
          the mass connection type   
            
         
        """
        pass
    
    ## Setter for property: (@link MassConnectivityType NXOpen.CAE.Connections.MassConnectivityType@endlink) MassConnectivityType

    ##   the mass connection type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @MassConnectivityType.setter
    def MassConnectivityType(self, type: MassConnectivityType):
        """
        Setter for property: (@link MassConnectivityType NXOpen.CAE.Connections.MassConnectivityType@endlink) MassConnectivityType
          the mass connection type   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxDistanceTolerance
    ##   the maximum distance from definition point to center of support element   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    @abstractmethod
    def MaxDistanceTolerance(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxDistanceTolerance
          the maximum distance from definition point to center of support element   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) PanelSearchDistance
    ##   the panel search distance   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    @abstractmethod
    def PanelSearchDistance(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) PanelSearchDistance
          the panel search distance   
            
         
        """
        pass
    
    ## Getter for property: (@link PanelSearchType NXOpen.CAE.Connections.PanelSearchType@endlink) PanelSearchType
    ##   the panel search type  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return PanelSearchType
    @property
    @abstractmethod
    def PanelSearchType(self) -> PanelSearchType:
        """
        Getter for property: (@link PanelSearchType NXOpen.CAE.Connections.PanelSearchType@endlink) PanelSearchType
          the panel search type  
            
         
        """
        pass
    
    ## Setter for property: (@link PanelSearchType NXOpen.CAE.Connections.PanelSearchType@endlink) PanelSearchType

    ##   the panel search type  
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @PanelSearchType.setter
    def PanelSearchType(self, type: PanelSearchType):
        """
        Setter for property: (@link PanelSearchType NXOpen.CAE.Connections.PanelSearchType@endlink) PanelSearchType
          the panel search type  
            
         
        """
        pass
    
    ## Getter for property: (@link RingSearchType NXOpen.CAE.Connections.RingSearchType@endlink) RingSearchType
    ##   the search tolerance type  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return RingSearchType
    @property
    @abstractmethod
    def RingSearchType(self) -> RingSearchType:
        """
        Getter for property: (@link RingSearchType NXOpen.CAE.Connections.RingSearchType@endlink) RingSearchType
          the search tolerance type  
            
         
        """
        pass
    
    ## Setter for property: (@link RingSearchType NXOpen.CAE.Connections.RingSearchType@endlink) RingSearchType

    ##   the search tolerance type  
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @RingSearchType.setter
    def RingSearchType(self, type: RingSearchType):
        """
        Setter for property: (@link RingSearchType NXOpen.CAE.Connections.RingSearchType@endlink) RingSearchType
          the search tolerance type  
            
         
        """
        pass
    
    ##  Add panels 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##  Panels entities 
    @abstractmethod
    def AddPanels(mass: IMassConnectivity, entities: List[NXOpen.TaggedObject]) -> None:
        """
         Add panels 
        """
        pass
    
    ##  Gets panels 
    ##  @return entities (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink):  Panels entities .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    @abstractmethod
    def GetPanels(mass: IMassConnectivity) -> List[NXOpen.TaggedObject]:
        """
         Gets panels 
         @return entities (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink):  Panels entities .
        """
        pass
    
    ##  Remove panels 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##  Panels entities 
    @abstractmethod
    def RemovePanels(mass: IMassConnectivity, entities: List[NXOpen.TaggedObject]) -> None:
        """
         Remove panels 
        """
        pass
    
import NXOpen
##   @brief  This class represents an Interface to the Mass Inertia.  
## 
##   
## 
##   <br>  Created in NX1847.0.0  <br> 

class IMassInertia(NXOpen.INXObject): 
    """ <summary> This class represents an Interface to the Mass Inertia. </summary> """


    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) InertiaXX
    ##   the inertia XX.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    @abstractmethod
    def InertiaXX(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) InertiaXX
          the inertia XX.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) InertiaYX
    ##   the inertia XY.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    @abstractmethod
    def InertiaYX(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) InertiaYX
          the inertia XY.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) InertiaYY
    ##   the inertia YY.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    @abstractmethod
    def InertiaYY(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) InertiaYY
          the inertia YY.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) InertiaZX
    ##   the inertia XZ.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    @abstractmethod
    def InertiaZX(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) InertiaZX
          the inertia XZ.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) InertiaZY
    ##   the inertia YZ.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    @abstractmethod
    def InertiaZY(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) InertiaZY
          the inertia YZ.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) InertiaZZ
    ##   the inertia ZZ.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    @abstractmethod
    def InertiaZZ(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) InertiaZZ
          the inertia ZZ.  
             
         
        """
        pass
    
import NXOpen
##   @brief  This class represents an Interface to the Mass Physical Params.  
## 
##   
## 
##   <br>  Created in NX1847.0.0  <br> 

class IMassPhysicalParams(NXOpen.INXObject): 
    """ <summary> This class represents an Interface to the Mass Physical Params. </summary> """


    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Mass
    ##   the mass value   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    @abstractmethod
    def Mass(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Mass
          the mass value   
            
         
        """
        pass
    
import NXOpen
##   @brief  This class represents an Interface to the Lumped Mass target.  
## 
##   
## 
##   <br>  Created in NX1847.0.0  <br> 

class IMassTarget(NXOpen.INXObject): 
    """ <summary> This class represents an Interface to the Lumped Mass target. </summary> """


    ## Getter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) Center
    ##   the target center   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.TaggedObject
    @property
    @abstractmethod
    def Center(self) -> NXOpen.TaggedObject:
        """
        Getter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) Center
          the target center   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) Center

    ##   the target center   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @Center.setter
    def Center(self, center: NXOpen.TaggedObject):
        """
        Setter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) Center
          the target center   
            
         
        """
        pass
    
    ## Getter for property: (@link LocalSpiderCenterType NXOpen.CAE.Connections.LocalSpiderCenterType@endlink) LocalSpiderCenterType
    ##   the local spider center type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return LocalSpiderCenterType
    @property
    @abstractmethod
    def LocalSpiderCenterType(self) -> LocalSpiderCenterType:
        """
        Getter for property: (@link LocalSpiderCenterType NXOpen.CAE.Connections.LocalSpiderCenterType@endlink) LocalSpiderCenterType
          the local spider center type   
            
         
        """
        pass
    
    ## Setter for property: (@link LocalSpiderCenterType NXOpen.CAE.Connections.LocalSpiderCenterType@endlink) LocalSpiderCenterType

    ##   the local spider center type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @LocalSpiderCenterType.setter
    def LocalSpiderCenterType(self, localSpiderCenterType: LocalSpiderCenterType):
        """
        Setter for property: (@link LocalSpiderCenterType NXOpen.CAE.Connections.LocalSpiderCenterType@endlink) LocalSpiderCenterType
          the local spider center type   
            
         
        """
        pass
    
    ## Getter for property: (@link MassCenterType NXOpen.CAE.Connections.MassCenterType@endlink) MassCenterType
    ##   the mass center type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return MassCenterType
    @property
    @abstractmethod
    def MassCenterType(self) -> MassCenterType:
        """
        Getter for property: (@link MassCenterType NXOpen.CAE.Connections.MassCenterType@endlink) MassCenterType
          the mass center type   
            
         
        """
        pass
    
    ## Setter for property: (@link MassCenterType NXOpen.CAE.Connections.MassCenterType@endlink) MassCenterType

    ##   the mass center type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @MassCenterType.setter
    def MassCenterType(self, massCenterType: MassCenterType):
        """
        Setter for property: (@link MassCenterType NXOpen.CAE.Connections.MassCenterType@endlink) MassCenterType
          the mass center type   
            
         
        """
        pass
    
    ## Getter for property: (@link MassDistributionType NXOpen.CAE.Connections.MassDistributionType@endlink) MassDistributionType
    ##   the mass distribution type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return MassDistributionType
    @property
    @abstractmethod
    def MassDistributionType(self) -> MassDistributionType:
        """
        Getter for property: (@link MassDistributionType NXOpen.CAE.Connections.MassDistributionType@endlink) MassDistributionType
          the mass distribution type   
            
         
        """
        pass
    
    ## Setter for property: (@link MassDistributionType NXOpen.CAE.Connections.MassDistributionType@endlink) MassDistributionType

    ##   the mass distribution type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @MassDistributionType.setter
    def MassDistributionType(self, type: MassDistributionType):
        """
        Setter for property: (@link MassDistributionType NXOpen.CAE.Connections.MassDistributionType@endlink) MassDistributionType
          the mass distribution type   
            
         
        """
        pass
    
    ##  Add entities to mass spider legs. 
    ##             Changes are not applied till an update is performed by calling @link Update::DoUpdate Update::DoUpdate@endlink  
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##  Mass support entities 
    @abstractmethod
    def AddSupportEntities(mass: IMassTarget, entities: List[NXOpen.TaggedObject]) -> None:
        """
         Add entities to mass spider legs. 
                    Changes are not applied till an update is performed by calling @link Update::DoUpdate Update::DoUpdate@endlink  
        """
        pass
    
    ##  Gets entities from mass spider legs. 
    ##             These can be any combination of CAD (point, edge, face, body) or FE (node, edge, face, element and mesh) 
    ##             objects able to return nodes. 
    ##  @return entities (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink):  Mass support entities .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    @abstractmethod
    def GetSupportEntities(mass: IMassTarget) -> List[NXOpen.TaggedObject]:
        """
         Gets entities from mass spider legs. 
                    These can be any combination of CAD (point, edge, face, body) or FE (node, edge, face, element and mesh) 
                    objects able to return nodes. 
         @return entities (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink):  Mass support entities .
        """
        pass
    
    ##  Remove entities from mass spider legs. 
    ##             Changes are not applied till an update is performed by calling @link Update::DoUpdate Update::DoUpdate@endlink  
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##  Mass support entities 
    @abstractmethod
    def RemoveSupportEntities(mass: IMassTarget, entities: List[NXOpen.TaggedObject]) -> None:
        """
         Remove entities from mass spider legs. 
                    Changes are not applied till an update is performed by calling @link Update::DoUpdate Update::DoUpdate@endlink  
        """
        pass
    
    ##  Add entities to mass spider legs. 
    ##             Changes are not applied till an update is performed by calling @link Update::DoUpdate Update::DoUpdate@endlink  
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##  Mass support entities 
    @abstractmethod
    def SetSupportEntities(mass: IMassTarget, entities: List[NXOpen.TaggedObject]) -> None:
        """
         Add entities to mass spider legs. 
                    Changes are not applied till an update is performed by calling @link Update::DoUpdate Update::DoUpdate@endlink  
        """
        pass
    
import NXOpen
##   @brief  This class represents an Interface to the Mass Type.  
## 
##   
## 
##   <br>  Created in NX1980.0.0  <br> 

class IMassType(NXOpen.INXObject): 
    """ <summary> This class represents an Interface to the Mass Type. </summary> """


    ## Getter for property: (@link MassType NXOpen.CAE.Connections.MassType@endlink) MassTypeValue
    ##   the mass type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return MassType
    @property
    @abstractmethod
    def MassTypeValue(self) -> MassType:
        """
        Getter for property: (@link MassType NXOpen.CAE.Connections.MassType@endlink) MassTypeValue
          the mass type   
            
         
        """
        pass
    
    ## Setter for property: (@link MassType NXOpen.CAE.Connections.MassType@endlink) MassTypeValue

    ##   the mass type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @MassTypeValue.setter
    def MassTypeValue(self, type: MassType):
        """
        Setter for property: (@link MassType NXOpen.CAE.Connections.MassType@endlink) MassTypeValue
          the mass type   
            
         
        """
        pass
    
import NXOpen
##   @brief  This class represents an Interface to the Material entity.  
## 
##   
## 
##   <br>  Created in NX12.0.0  <br> 

class IMaterial(NXOpen.INXObject): 
    """ <summary> This class represents an Interface to the Material entity. </summary> """


    ## Getter for property: (@link NXOpen.PhysicalMaterial NXOpen.PhysicalMaterial@endlink) Material
    ##   the connection material   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.PhysicalMaterial
    @property
    @abstractmethod
    def Material(self) -> NXOpen.PhysicalMaterial:
        """
        Getter for property: (@link NXOpen.PhysicalMaterial NXOpen.PhysicalMaterial@endlink) Material
          the connection material   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.PhysicalMaterial NXOpen.PhysicalMaterial@endlink) Material

    ##   the connection material   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @Material.setter
    def Material(self, material: NXOpen.PhysicalMaterial):
        """
        Setter for property: (@link NXOpen.PhysicalMaterial NXOpen.PhysicalMaterial@endlink) Material
          the connection material   
            
         
        """
        pass
    
    ##  Use this function to check if the connection supports having no material 
    ##  @return value (bool): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    @abstractmethod
    def CanHaveNoMaterial(connection: IMaterial) -> bool:
        """
         Use this function to check if the connection supports having no material 
         @return value (bool): .
        """
        pass
    
    ##  Use this function to check if the connection supports inherited material 
    ##  @return value (bool): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    @abstractmethod
    def CanInheritMaterial(connection: IMaterial) -> bool:
        """
         Use this function to check if the connection supports inherited material 
         @return value (bool): .
        """
        pass
    
    ##  Use this function to check if the connection inherits material from flanges 
    ##  @return value (bool): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    @abstractmethod
    def IsInheritedMaterial(connection: IMaterial) -> bool:
        """
         Use this function to check if the connection inherits material from flanges 
         @return value (bool): .
        """
        pass
    
    ##  Use this function to set inherited material to connection 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    @staticmethod
    @abstractmethod
    def SetInheritedMaterial(connection: IMaterial) -> None:
        """
         Use this function to set inherited material to connection 
        """
        pass
    
import NXOpen
##   @brief  This class represents an Interface to the Nodal Target Center Option.  
## 
##   
## 
##   <br>  Created in NX1847.0.0  <br> 

class INodalTargetCenterOption(NXOpen.INXObject): 
    """ <summary> This class represents an Interface to the Nodal Target Center Option. </summary> """


    ## Getter for property: (@link NodalTargetCenterType NXOpen.CAE.Connections.NodalTargetCenterType@endlink) CenterType
    ##   the target center type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return NodalTargetCenterType
    @property
    @abstractmethod
    def CenterType(self) -> NodalTargetCenterType:
        """
        Getter for property: (@link NodalTargetCenterType NXOpen.CAE.Connections.NodalTargetCenterType@endlink) CenterType
          the target center type   
            
         
        """
        pass
    
    ## Setter for property: (@link NodalTargetCenterType NXOpen.CAE.Connections.NodalTargetCenterType@endlink) CenterType

    ##   the target center type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @CenterType.setter
    def CenterType(self, centerType: NodalTargetCenterType):
        """
        Setter for property: (@link NodalTargetCenterType NXOpen.CAE.Connections.NodalTargetCenterType@endlink) CenterType
          the target center type   
            
         
        """
        pass
    
    ##  Get available center types
    ##  @return types (@link NodalTargetCenterType List[NXOpen.CAE.Connections.NodalTargetCenterType]@endlink): .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    @abstractmethod
    def GetAvailableTargetCenterTypes(target: INodalTargetCenterOption) -> List[NodalTargetCenterType]:
        """
         Get available center types
         @return types (@link NodalTargetCenterType List[NXOpen.CAE.Connections.NodalTargetCenterType]@endlink): .
        """
        pass
    
    ##  Check if center type is allowed 
    ##  @return allowed (bool): .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    @abstractmethod
    def IsCoincidentCenterTypeAllowed(target: INodalTargetCenterOption) -> bool:
        """
         Check if center type is allowed 
         @return allowed (bool): .
        """
        pass
    
import NXOpen
##   @brief  This class represents an Interface to the Connection Target.  
## 
##   
## 
##   <br>  Created in NX12.0.0  <br> 

class INodalTargetCenter(NXOpen.INXObject): 
    """ <summary> This class represents an Interface to the Connection Target. </summary> """


    ## Getter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) TargetCenter
    ##   the target center   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.TaggedObject
    @property
    @abstractmethod
    def TargetCenter(self) -> NXOpen.TaggedObject:
        """
        Getter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) TargetCenter
          the target center   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) TargetCenter

    ##   the target center   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @TargetCenter.setter
    def TargetCenter(self, center: NXOpen.TaggedObject):
        """
        Setter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) TargetCenter
          the target center   
            
         
        """
        pass
    
import NXOpen
##   @brief  This class represents an Interface to the Connection Target.  
## 
##   
## 
##   <br>  Created in NX12.0.0  <br> 

class INodalTargetLegs(NXOpen.INXObject): 
    """ <summary> This class represents an Interface to the Connection Target. </summary> """


    ##  Add entities to target's group of points. 
    ##             Changes are not applied till an update is performed by calling @link Update::DoUpdate Update::DoUpdate@endlink  
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##  Legs entities 
    @abstractmethod
    def AddLegsEntities(target: INodalTargetLegs, entities: List[NXOpen.TaggedObject]) -> None:
        """
         Add entities to target's group of points. 
                    Changes are not applied till an update is performed by calling @link Update::DoUpdate Update::DoUpdate@endlink  
        """
        pass
    
    ##  Gets entities from target's group of points. 
    ##             These can be any combination of CAD (point, edge, face, body) or FE (node, edge, face, element and mesh) 
    ##             objects able to return nodes. 
    ##  @return entities (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink):  Legs entities .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    @abstractmethod
    def GetLegsEntities(target: INodalTargetLegs) -> List[NXOpen.TaggedObject]:
        """
         Gets entities from target's group of points. 
                    These can be any combination of CAD (point, edge, face, body) or FE (node, edge, face, element and mesh) 
                    objects able to return nodes. 
         @return entities (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink):  Legs entities .
        """
        pass
    
    ##  Remove entities from target's group of points. 
    ##             Changes are not applied till an update is performed by calling @link Update::DoUpdate Update::DoUpdate@endlink  
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##  Legs entities 
    @abstractmethod
    def RemoveLegsEntities(target: INodalTargetLegs, entities: List[NXOpen.TaggedObject]) -> None:
        """
         Remove entities from target's group of points. 
                    Changes are not applied till an update is performed by calling @link Update::DoUpdate Update::DoUpdate@endlink  
        """
        pass
    
import NXOpen
import NXOpen.CAE
##   @brief  This class represents an Interface to the Nodal Target Local Spider Definition.  
## 
##   
## 
##   <br>  Created in NX1847.0.0  <br> 

class INodalTargetLocalSpiderDefinition(NXOpen.INXObject): 
    """ <summary> This class represents an Interface to the Nodal Target Local Spider Definition. </summary> """


    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ExpansionRadius
    ##   the Expansion Radius   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    @abstractmethod
    def ExpansionRadius(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ExpansionRadius
          the Expansion Radius   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ExpansionRadiusFactor
    ##   the Expansion Radius Factor   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    @abstractmethod
    def ExpansionRadiusFactor(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ExpansionRadiusFactor
          the Expansion Radius Factor   
            
         
        """
        pass
    
    ## Getter for property: (@link LocalSpiderCenterType NXOpen.CAE.Connections.LocalSpiderCenterType@endlink) LocalSpiderCenterType
    ##   the Local Spider Center type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return LocalSpiderCenterType
    @property
    @abstractmethod
    def LocalSpiderCenterType(self) -> LocalSpiderCenterType:
        """
        Getter for property: (@link LocalSpiderCenterType NXOpen.CAE.Connections.LocalSpiderCenterType@endlink) LocalSpiderCenterType
          the Local Spider Center type   
            
         
        """
        pass
    
    ## Setter for property: (@link LocalSpiderCenterType NXOpen.CAE.Connections.LocalSpiderCenterType@endlink) LocalSpiderCenterType

    ##   the Local Spider Center type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @LocalSpiderCenterType.setter
    def LocalSpiderCenterType(self, localSpiderCenterType: LocalSpiderCenterType):
        """
        Setter for property: (@link LocalSpiderCenterType NXOpen.CAE.Connections.LocalSpiderCenterType@endlink) LocalSpiderCenterType
          the Local Spider Center type   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxDistance
    ##   the Maximum Distance   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    @abstractmethod
    def MaxDistance(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxDistance
          the Maximum Distance   
            
         
        """
        pass
    
    ## Getter for property: (@link PanelSearchType NXOpen.CAE.Connections.PanelSearchType@endlink) PanelSearchType
    ##   the Panel Search type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return PanelSearchType
    @property
    @abstractmethod
    def PanelSearchType(self) -> PanelSearchType:
        """
        Getter for property: (@link PanelSearchType NXOpen.CAE.Connections.PanelSearchType@endlink) PanelSearchType
          the Panel Search type   
            
         
        """
        pass
    
    ## Setter for property: (@link PanelSearchType NXOpen.CAE.Connections.PanelSearchType@endlink) PanelSearchType

    ##   the Panel Search type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @PanelSearchType.setter
    def PanelSearchType(self, panelSearchType: PanelSearchType):
        """
        Setter for property: (@link PanelSearchType NXOpen.CAE.Connections.PanelSearchType@endlink) PanelSearchType
          the Panel Search type   
            
         
        """
        pass
    
    ## Getter for property: (@link RingSearchType NXOpen.CAE.Connections.RingSearchType@endlink) RingSearchType
    ##   the Ring Search type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return RingSearchType
    @property
    @abstractmethod
    def RingSearchType(self) -> RingSearchType:
        """
        Getter for property: (@link RingSearchType NXOpen.CAE.Connections.RingSearchType@endlink) RingSearchType
          the Ring Search type   
            
         
        """
        pass
    
    ## Setter for property: (@link RingSearchType NXOpen.CAE.Connections.RingSearchType@endlink) RingSearchType

    ##   the Ring Search type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @RingSearchType.setter
    def RingSearchType(self, ringSearchType: RingSearchType):
        """
        Setter for property: (@link RingSearchType NXOpen.CAE.Connections.RingSearchType@endlink) RingSearchType
          the Ring Search type   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) SearchTolerance
    ##   the Search Tolerance   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    @abstractmethod
    def SearchTolerance(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) SearchTolerance
          the Search Tolerance   
            
         
        """
        pass
    
    ##  Adds a mesh point location to the target locations list 
    ##  @return location (@link MeshPointLocation NXOpen.CAE.Connections.MeshPointLocation@endlink):  The created mesh point type location .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##  Mesh Point used for location creation 
    @abstractmethod
    def AddLocationMeshPoint(target: INodalTargetLocalSpiderDefinition, meshPoint: NXOpen.CAE.MeshPoint) -> MeshPointLocation:
        """
         Adds a mesh point location to the target locations list 
         @return location (@link MeshPointLocation NXOpen.CAE.Connections.MeshPointLocation@endlink):  The created mesh point type location .
        """
        pass
    
    ##  Adds a node location to the target locations list 
    ##  @return location (@link NodeLocation NXOpen.CAE.Connections.NodeLocation@endlink):  The node type location .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##  Node used for location 
    @abstractmethod
    def AddLocationNode(target: INodalTargetLocalSpiderDefinition, node: NXOpen.CAE.FENode) -> NodeLocation:
        """
         Adds a node location to the target locations list 
         @return location (@link NodeLocation NXOpen.CAE.Connections.NodeLocation@endlink):  The node type location .
        """
        pass
    
    ##  Adds a point location to the target locations list 
    ##  @return location (@link PointLocation NXOpen.CAE.Connections.PointLocation@endlink):  The created point type location .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##  Point used for location creation 
    @abstractmethod
    def AddLocationPoint(target: INodalTargetLocalSpiderDefinition, point: NXOpen.Point) -> PointLocation:
        """
         Adds a point location to the target locations list 
         @return location (@link PointLocation NXOpen.CAE.Connections.PointLocation@endlink):  The created point type location .
        """
        pass
    
    ##  Adds a Selection Recipe to the target locations list 
    ##  @return location (@link SelectionRecipeLocation NXOpen.CAE.Connections.SelectionRecipeLocation@endlink):  The created selection recipe type location .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##  Selection Recipe used for location creation 
    @abstractmethod
    def AddLocationSelectionRecipe(target: INodalTargetLocalSpiderDefinition, selectionRecipe: NXOpen.CAE.SelectionRecipe) -> SelectionRecipeLocation:
        """
         Adds a Selection Recipe to the target locations list 
         @return location (@link SelectionRecipeLocation NXOpen.CAE.Connections.SelectionRecipeLocation@endlink):  The created selection recipe type location .
        """
        pass
    
    ##  Add regions entities to the target. 
    ##             Changes are not applied till an update is performed by calling @link Update::DoUpdate Update::DoUpdate@endlink  
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##  Regions entities 
    @abstractmethod
    def AddRegionsEntities(target: INodalTargetLocalSpiderDefinition, entities: List[NXOpen.TaggedObject]) -> None:
        """
         Add regions entities to the target. 
                    Changes are not applied till an update is performed by calling @link Update::DoUpdate Update::DoUpdate@endlink  
        """
        pass
    
    ##  Get a location from the target locations list 
    ##  @return location (@link Location NXOpen.CAE.Connections.Location@endlink):  The location .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ##  The location index 
    @abstractmethod
    def GetLocation(target: INodalTargetLocalSpiderDefinition, indexOfLocation: int) -> Location:
        """
         Get a location from the target locations list 
         @return location (@link Location NXOpen.CAE.Connections.Location@endlink):  The location .
        """
        pass
    
    ##  Get the number of locations in the target 
    ##  @return number_of_locations (int):  The number of locations .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    @abstractmethod
    def GetNumberOfLocations(target: INodalTargetLocalSpiderDefinition) -> int:
        """
         Get the number of locations in the target 
         @return number_of_locations (int):  The number of locations .
        """
        pass
    
    ##  Gets regions entities in the target. 
    ##             These can be any combination of CAD (point, edge, face, body) or FE (node, edge, face, element and mesh) 
    ##             objects able to return nodes. 
    ##  @return entities (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink):  Legs entities .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    @abstractmethod
    def GetRegionsEntities(target: INodalTargetLocalSpiderDefinition) -> List[NXOpen.TaggedObject]:
        """
         Gets regions entities in the target. 
                    These can be any combination of CAD (point, edge, face, body) or FE (node, edge, face, element and mesh) 
                    objects able to return nodes. 
         @return entities (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink):  Legs entities .
        """
        pass
    
    ##  Remove a location from the target locations list 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##  The location index 
    @abstractmethod
    def RemoveLocation(target: INodalTargetLocalSpiderDefinition, indexOfLocation: int) -> None:
        """
         Remove a location from the target locations list 
        """
        pass
    
    ##  Remove regions entities from the target. 
    ##             Changes are not applied till an update is performed by calling @link Update::DoUpdate Update::DoUpdate@endlink  
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##  Regions entities 
    @abstractmethod
    def RemoveRegionsEntities(target: INodalTargetLocalSpiderDefinition, entities: List[NXOpen.TaggedObject]) -> None:
        """
         Remove regions entities from the target. 
                    Changes are not applied till an update is performed by calling @link Update::DoUpdate Update::DoUpdate@endlink  
        """
        pass
    
import NXOpen
##   @brief  This class represents an Interface to the Connection Target Container.  
## 
##   
## 
##   <br>  Created in NX12.0.0  <br> 

class INodalTargetsContainer(NXOpen.INXObject): 
    """ <summary> This class represents an Interface to the Connection Target Container. </summary> """


    ##  Get target 
    ##  @return target (@link NodalTarget NXOpen.CAE.Connections.NodalTarget@endlink): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="index"> (int) </param>
    @abstractmethod
    def GetTarget(connection: INodalTargetsContainer, index: int) -> NodalTarget:
        """
         Get target 
         @return target (@link NodalTarget NXOpen.CAE.Connections.NodalTarget@endlink): .
        """
        pass
    
    ##  Set the target type 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ## <param name="index"> (int) </param>
    ## <param name="type"> (@link NodalTargetType NXOpen.CAE.Connections.NodalTargetType@endlink) </param>
    @abstractmethod
    def SetTargetType(connection: INodalTargetsContainer, index: int, type: NodalTargetType) -> None:
        """
         Set the target type 
        """
        pass
    
    ##  Swap targets 
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    @staticmethod
    @abstractmethod
    def SwapTargets(connection: INodalTargetsContainer) -> None:
        """
         Swap targets 
        """
        pass
    
import NXOpen
##   @brief  This class represents an Interface to the nodal connections pairing algorithm parameters.  
## 
##   
## 
##   <br>  Created in NX12.0.0  <br> 

class INodalTargetsPairing(NXOpen.INXObject): 
    """ <summary> This class represents an Interface to the nodal connections pairing algorithm parameters. </summary> """


    ## Getter for property: (@link NodalPairingMethod NXOpen.CAE.Connections.NodalPairingMethod@endlink) PairingMethod
    ##   the pairing method of targets   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NodalPairingMethod
    @property
    @abstractmethod
    def PairingMethod(self) -> NodalPairingMethod:
        """
        Getter for property: (@link NodalPairingMethod NXOpen.CAE.Connections.NodalPairingMethod@endlink) PairingMethod
          the pairing method of targets   
            
         
        """
        pass
    
    ## Setter for property: (@link NodalPairingMethod NXOpen.CAE.Connections.NodalPairingMethod@endlink) PairingMethod

    ##   the pairing method of targets   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @PairingMethod.setter
    def PairingMethod(self, method: NodalPairingMethod):
        """
        Setter for property: (@link NodalPairingMethod NXOpen.CAE.Connections.NodalPairingMethod@endlink) PairingMethod
          the pairing method of targets   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) SearchConeAngle
    ##   the search cone angle   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    @abstractmethod
    def SearchConeAngle(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) SearchConeAngle
          the search cone angle   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) SearchOrientation
    ##   the pairing search orientation   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Direction
    @property
    @abstractmethod
    def SearchOrientation(self) -> NXOpen.Direction:
        """
        Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) SearchOrientation
          the pairing search orientation   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) SearchOrientation

    ##   the pairing search orientation   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @SearchOrientation.setter
    def SearchOrientation(self, orientation: NXOpen.Direction):
        """
        Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) SearchOrientation
          the pairing search orientation   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) SearchRange
    ##   the search range   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    @abstractmethod
    def SearchRange(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) SearchRange
          the search range   
            
         
        """
        pass
    
import NXOpen
import NXOpen.Fields
##   @brief  This class represents an Interface to the Nonlinear Cylindrical Damping.  
## 
##   
## 
##   <br>  Created in NX1980.0.0  <br> 

class INonlinearCylindricalDamping(NXOpen.INXObject): 
    """ <summary> This class represents an Interface to the Nonlinear Cylindrical Damping. </summary> """


    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RNonlinearCylindricalDamping
    ##   the R nonlinear cylindrical damping   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.Fields.ScalarFieldWrapper
    @property
    @abstractmethod
    def RNonlinearCylindricalDamping(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RNonlinearCylindricalDamping
          the R nonlinear cylindrical damping   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RNonlinearCylindricalDamping

    ##   the R nonlinear cylindrical damping   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @RNonlinearCylindricalDamping.setter
    def RNonlinearCylindricalDamping(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RNonlinearCylindricalDamping
          the R nonlinear cylindrical damping   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RrNonlinearCylindricalDamping
    ##   the RR nonlinear cylindrical damping   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.Fields.ScalarFieldWrapper
    @property
    @abstractmethod
    def RrNonlinearCylindricalDamping(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RrNonlinearCylindricalDamping
          the RR nonlinear cylindrical damping   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RrNonlinearCylindricalDamping

    ##   the RR nonlinear cylindrical damping   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @RrNonlinearCylindricalDamping.setter
    def RrNonlinearCylindricalDamping(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RrNonlinearCylindricalDamping
          the RR nonlinear cylindrical damping   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzNonlinearCylindricalDamping
    ##   the RZ nonlinear cylindrical damping   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.Fields.ScalarFieldWrapper
    @property
    @abstractmethod
    def RzNonlinearCylindricalDamping(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzNonlinearCylindricalDamping
          the RZ nonlinear cylindrical damping   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzNonlinearCylindricalDamping

    ##   the RZ nonlinear cylindrical damping   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @RzNonlinearCylindricalDamping.setter
    def RzNonlinearCylindricalDamping(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzNonlinearCylindricalDamping
          the RZ nonlinear cylindrical damping   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZNonlinearCylindricalDamping
    ##   the Z nonlinear cylindrical damping   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.Fields.ScalarFieldWrapper
    @property
    @abstractmethod
    def ZNonlinearCylindricalDamping(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZNonlinearCylindricalDamping
          the Z nonlinear cylindrical damping   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZNonlinearCylindricalDamping

    ##   the Z nonlinear cylindrical damping   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @ZNonlinearCylindricalDamping.setter
    def ZNonlinearCylindricalDamping(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZNonlinearCylindricalDamping
          the Z nonlinear cylindrical damping   
            
         
        """
        pass
    
import NXOpen
import NXOpen.Fields
##   @brief  This class represents an Interface to the Nonlinear Cylindrical Stiffness.  
## 
##   
## 
##   <br>  Created in NX1980.0.0  <br> 

class INonlinearCylindricalStiffness(NXOpen.INXObject): 
    """ <summary> This class represents an Interface to the Nonlinear Cylindrical Stiffness. </summary> """


    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RNonlinearCylindricalStiffness
    ##   the R nonlinear cylindrical stiffness   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.Fields.ScalarFieldWrapper
    @property
    @abstractmethod
    def RNonlinearCylindricalStiffness(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RNonlinearCylindricalStiffness
          the R nonlinear cylindrical stiffness   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RNonlinearCylindricalStiffness

    ##   the R nonlinear cylindrical stiffness   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @RNonlinearCylindricalStiffness.setter
    def RNonlinearCylindricalStiffness(self, rDynamic: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RNonlinearCylindricalStiffness
          the R nonlinear cylindrical stiffness   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RrNonlinearCylindricalStiffness
    ##   the RR nonlinear cylindrical stiffness   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.Fields.ScalarFieldWrapper
    @property
    @abstractmethod
    def RrNonlinearCylindricalStiffness(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RrNonlinearCylindricalStiffness
          the RR nonlinear cylindrical stiffness   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RrNonlinearCylindricalStiffness

    ##   the RR nonlinear cylindrical stiffness   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @RrNonlinearCylindricalStiffness.setter
    def RrNonlinearCylindricalStiffness(self, rrDynamic: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RrNonlinearCylindricalStiffness
          the RR nonlinear cylindrical stiffness   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzNonlinearCylindricalStiffness
    ##   the RZ nonlinear cylindrical stiffness   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.Fields.ScalarFieldWrapper
    @property
    @abstractmethod
    def RzNonlinearCylindricalStiffness(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzNonlinearCylindricalStiffness
          the RZ nonlinear cylindrical stiffness   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzNonlinearCylindricalStiffness

    ##   the RZ nonlinear cylindrical stiffness   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @RzNonlinearCylindricalStiffness.setter
    def RzNonlinearCylindricalStiffness(self, rzDynamic: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzNonlinearCylindricalStiffness
          the RZ nonlinear cylindrical stiffness   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZNonlinearCylindricalStiffness
    ##   the Z nonlinear cylindrical stiffness   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.Fields.ScalarFieldWrapper
    @property
    @abstractmethod
    def ZNonlinearCylindricalStiffness(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZNonlinearCylindricalStiffness
          the Z nonlinear cylindrical stiffness   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZNonlinearCylindricalStiffness

    ##   the Z nonlinear cylindrical stiffness   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @ZNonlinearCylindricalStiffness.setter
    def ZNonlinearCylindricalStiffness(self, zDynamic: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZNonlinearCylindricalStiffness
          the Z nonlinear cylindrical stiffness   
            
         
        """
        pass
    
import NXOpen
import NXOpen.Fields
##   @brief  This class represents an Interface to the nonlinear damping.  
## 
##   
## 
##   <br>  Created in NX1980.0.0  <br> 

class INonlinearDamping(NXOpen.INXObject): 
    """ <summary> This class represents an Interface to the nonlinear damping. </summary> """


    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RxNonlinearDamping
    ##   the RX nonlinear damping   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.Fields.ScalarFieldWrapper
    @property
    @abstractmethod
    def RxNonlinearDamping(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RxNonlinearDamping
          the RX nonlinear damping   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RxNonlinearDamping

    ##   the RX nonlinear damping   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @RxNonlinearDamping.setter
    def RxNonlinearDamping(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RxNonlinearDamping
          the RX nonlinear damping   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RyNonlinearDamping
    ##   the RY nonlinear damping   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.Fields.ScalarFieldWrapper
    @property
    @abstractmethod
    def RyNonlinearDamping(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RyNonlinearDamping
          the RY nonlinear damping   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RyNonlinearDamping

    ##   the RY nonlinear damping   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @RyNonlinearDamping.setter
    def RyNonlinearDamping(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RyNonlinearDamping
          the RY nonlinear damping   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzNonlinearDamping
    ##   the RZ nonlinear damping   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.Fields.ScalarFieldWrapper
    @property
    @abstractmethod
    def RzNonlinearDamping(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzNonlinearDamping
          the RZ nonlinear damping   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzNonlinearDamping

    ##   the RZ nonlinear damping   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @RzNonlinearDamping.setter
    def RzNonlinearDamping(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzNonlinearDamping
          the RZ nonlinear damping   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) XNonlinearDamping
    ##   the X nonlinear damping   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.Fields.ScalarFieldWrapper
    @property
    @abstractmethod
    def XNonlinearDamping(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) XNonlinearDamping
          the X nonlinear damping   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) XNonlinearDamping

    ##   the X nonlinear damping   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @XNonlinearDamping.setter
    def XNonlinearDamping(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) XNonlinearDamping
          the X nonlinear damping   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) YNonlinearDamping
    ##   the Y nonlinear damping   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.Fields.ScalarFieldWrapper
    @property
    @abstractmethod
    def YNonlinearDamping(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) YNonlinearDamping
          the Y nonlinear damping   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) YNonlinearDamping

    ##   the Y nonlinear damping   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @YNonlinearDamping.setter
    def YNonlinearDamping(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) YNonlinearDamping
          the Y nonlinear damping   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZNonlinearDamping
    ##   the Z nonlinear damping   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.Fields.ScalarFieldWrapper
    @property
    @abstractmethod
    def ZNonlinearDamping(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZNonlinearDamping
          the Z nonlinear damping   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZNonlinearDamping

    ##   the Z nonlinear damping   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @ZNonlinearDamping.setter
    def ZNonlinearDamping(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZNonlinearDamping
          the Z nonlinear damping   
            
         
        """
        pass
    
import NXOpen
import NXOpen.Fields
##   @brief  This class represents an Interface to the nonlinear stiffness.  
## 
##   
## 
##   <br>  Created in NX1980.0.0  <br> 

class INonlinearStiffness(NXOpen.INXObject): 
    """ <summary> This class represents an Interface to the nonlinear stiffness. </summary> """


    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RxNonlinearStiffness
    ##   the RX nonlinear stiffness   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.Fields.ScalarFieldWrapper
    @property
    @abstractmethod
    def RxNonlinearStiffness(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RxNonlinearStiffness
          the RX nonlinear stiffness   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RxNonlinearStiffness

    ##   the RX nonlinear stiffness   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @RxNonlinearStiffness.setter
    def RxNonlinearStiffness(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RxNonlinearStiffness
          the RX nonlinear stiffness   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RyNonlinearStiffness
    ##   the RY nonlinear stiffness   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.Fields.ScalarFieldWrapper
    @property
    @abstractmethod
    def RyNonlinearStiffness(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RyNonlinearStiffness
          the RY nonlinear stiffness   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RyNonlinearStiffness

    ##   the RY nonlinear stiffness   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @RyNonlinearStiffness.setter
    def RyNonlinearStiffness(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RyNonlinearStiffness
          the RY nonlinear stiffness   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzNonlinearStiffness
    ##   the RZ nonlinear stiffness   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.Fields.ScalarFieldWrapper
    @property
    @abstractmethod
    def RzNonlinearStiffness(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzNonlinearStiffness
          the RZ nonlinear stiffness   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzNonlinearStiffness

    ##   the RZ nonlinear stiffness   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @RzNonlinearStiffness.setter
    def RzNonlinearStiffness(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzNonlinearStiffness
          the RZ nonlinear stiffness   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) XNonlinearStiffness
    ##   the X nonlinear stiffness   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.Fields.ScalarFieldWrapper
    @property
    @abstractmethod
    def XNonlinearStiffness(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) XNonlinearStiffness
          the X nonlinear stiffness   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) XNonlinearStiffness

    ##   the X nonlinear stiffness   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @XNonlinearStiffness.setter
    def XNonlinearStiffness(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) XNonlinearStiffness
          the X nonlinear stiffness   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) YNonlinearStiffness
    ##   the Y nonlinear stiffness   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.Fields.ScalarFieldWrapper
    @property
    @abstractmethod
    def YNonlinearStiffness(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) YNonlinearStiffness
          the Y nonlinear stiffness   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) YNonlinearStiffness

    ##   the Y nonlinear stiffness   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @YNonlinearStiffness.setter
    def YNonlinearStiffness(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) YNonlinearStiffness
          the Y nonlinear stiffness   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZNonlinearStiffness
    ##   the Z nonlinear stiffness   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.Fields.ScalarFieldWrapper
    @property
    @abstractmethod
    def ZNonlinearStiffness(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZNonlinearStiffness
          the Z nonlinear stiffness   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZNonlinearStiffness

    ##   the Z nonlinear stiffness   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @ZNonlinearStiffness.setter
    def ZNonlinearStiffness(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZNonlinearStiffness
          the Z nonlinear stiffness   
            
         
        """
        pass
    
import NXOpen
##   @brief  This interface offers access to the flanges of a Seam Weld connection.
##           
## 
##   
## 
##   <br>  Created in NX1847.0.0  <br> 

class ISeamWeldFlangesContainer(IFlangesContainer): 
    """ <summary> This interface offers access to the flanges of a Seam Weld connection.
         </summary> """


    ##  Get the flange angle.
    ##  @return angle (@link NXOpen.Expression NXOpen.Expression@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="flangeIndex"> (int) </param>
    @abstractmethod
    def GetFlangeAngle(connection: ISeamWeldFlangesContainer, flangeIndex: int) -> NXOpen.Expression:
        """
         Get the flange angle.
         @return angle (@link NXOpen.Expression NXOpen.Expression@endlink): .
        """
        pass
    
    ##  Get the flange gap.
    ##  @return gap (@link NXOpen.Expression NXOpen.Expression@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="flangeIndex"> (int) </param>
    @abstractmethod
    def GetFlangeGap(connection: ISeamWeldFlangesContainer, flangeIndex: int) -> NXOpen.Expression:
        """
         Get the flange gap.
         @return gap (@link NXOpen.Expression NXOpen.Expression@endlink): .
        """
        pass
    
    ##  Get the flange thickness.
    ##  @return thickness (@link NXOpen.Expression NXOpen.Expression@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="flangeIndex"> (int) </param>
    @abstractmethod
    def GetFlangeThickness(connection: ISeamWeldFlangesContainer, flangeIndex: int) -> NXOpen.Expression:
        """
         Get the flange thickness.
         @return thickness (@link NXOpen.Expression NXOpen.Expression@endlink): .
        """
        pass
    
    ##  Get the flange thickness inherited flag.
    ##  @return thicknessInherited (bool): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="flangeIndex"> (int) </param>
    @abstractmethod
    def GetFlangeThicknessInherited(connection: ISeamWeldFlangesContainer, flangeIndex: int) -> bool:
        """
         Get the flange thickness inherited flag.
         @return thicknessInherited (bool): .
        """
        pass
    
    ##  Set the flange thickness inherited flag.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ## <param name="flangeIndex"> (int) </param>
    ## <param name="thicknessInherited"> (bool) </param>
    @abstractmethod
    def SetFlangeThicknessInherited(connection: ISeamWeldFlangesContainer, flangeIndex: int, thicknessInherited: bool) -> None:
        """
         Set the flange thickness inherited flag.
        """
        pass
    
import NXOpen
import NXOpen.Fields
##   @brief  This class represents an Interface to the Stiffness dynamic.  
## 
##   
## 
##   <br>  Created in NX12.0.0  <br> 

class IStiffnessDynamic(NXOpen.INXObject): 
    """ <summary> This class represents an Interface to the Stiffness dynamic. </summary> """


    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RxStiffnessDynamic
    ##   the RX stiffness dynamic   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Fields.ScalarFieldWrapper
    @property
    @abstractmethod
    def RxStiffnessDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RxStiffnessDynamic
          the RX stiffness dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RxStiffnessDynamic

    ##   the RX stiffness dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @RxStiffnessDynamic.setter
    def RxStiffnessDynamic(self, rxDynamic: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RxStiffnessDynamic
          the RX stiffness dynamic   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RyStiffnessDynamic
    ##   the RY stiffness dynamic   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Fields.ScalarFieldWrapper
    @property
    @abstractmethod
    def RyStiffnessDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RyStiffnessDynamic
          the RY stiffness dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RyStiffnessDynamic

    ##   the RY stiffness dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @RyStiffnessDynamic.setter
    def RyStiffnessDynamic(self, ryDynamic: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RyStiffnessDynamic
          the RY stiffness dynamic   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzStiffnessDynamic
    ##   the RZ stiffness dynamic   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Fields.ScalarFieldWrapper
    @property
    @abstractmethod
    def RzStiffnessDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzStiffnessDynamic
          the RZ stiffness dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzStiffnessDynamic

    ##   the RZ stiffness dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @RzStiffnessDynamic.setter
    def RzStiffnessDynamic(self, rzDynamic: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzStiffnessDynamic
          the RZ stiffness dynamic   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) XStiffnessDynamic
    ##   the X stiffness dynamic   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Fields.ScalarFieldWrapper
    @property
    @abstractmethod
    def XStiffnessDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) XStiffnessDynamic
          the X stiffness dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) XStiffnessDynamic

    ##   the X stiffness dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @XStiffnessDynamic.setter
    def XStiffnessDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) XStiffnessDynamic
          the X stiffness dynamic   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) YStiffnessDynamic
    ##   the Y stiffness dynamic   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Fields.ScalarFieldWrapper
    @property
    @abstractmethod
    def YStiffnessDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) YStiffnessDynamic
          the Y stiffness dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) YStiffnessDynamic

    ##   the Y stiffness dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @YStiffnessDynamic.setter
    def YStiffnessDynamic(self, yDynamic: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) YStiffnessDynamic
          the Y stiffness dynamic   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZStiffnessDynamic
    ##   the Z stiffness dynamic   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Fields.ScalarFieldWrapper
    @property
    @abstractmethod
    def ZStiffnessDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZStiffnessDynamic
          the Z stiffness dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZStiffnessDynamic

    ##   the Z stiffness dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @ZStiffnessDynamic.setter
    def ZStiffnessDynamic(self, zDynamic: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZStiffnessDynamic
          the Z stiffness dynamic   
            
         
        """
        pass
    
import NXOpen
##   @brief  This class represents an Interface to the Stiffness constants.  
## 
##   
## 
##   <br>  Created in NX12.0.0  <br> 

class IStiffness(NXOpen.INXObject): 
    """ <summary> This class represents an Interface to the Stiffness constants. </summary> """


    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RxStiffnessConstant
    ##   the RX stiffness constant   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    @abstractmethod
    def RxStiffnessConstant(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RxStiffnessConstant
          the RX stiffness constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RyStiffnessConstant
    ##   the RY stiffness constant   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    @abstractmethod
    def RyStiffnessConstant(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RyStiffnessConstant
          the RY stiffness constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RzStiffnessConstant
    ##   the RZ stiffness constant   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    @abstractmethod
    def RzStiffnessConstant(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RzStiffnessConstant
          the RZ stiffness constant   
            
         
        """
        pass
    
    ## Getter for property: (@link StiffnessType NXOpen.CAE.Connections.StiffnessType@endlink) StiffnessType
    ##   the stiffness type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return StiffnessType
    @property
    @abstractmethod
    def StiffnessType(self) -> StiffnessType:
        """
        Getter for property: (@link StiffnessType NXOpen.CAE.Connections.StiffnessType@endlink) StiffnessType
          the stiffness type   
            
         
        """
        pass
    
    ## Setter for property: (@link StiffnessType NXOpen.CAE.Connections.StiffnessType@endlink) StiffnessType

    ##   the stiffness type   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @StiffnessType.setter
    def StiffnessType(self, oStiffnessType: StiffnessType):
        """
        Setter for property: (@link StiffnessType NXOpen.CAE.Connections.StiffnessType@endlink) StiffnessType
          the stiffness type   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) XStiffnessConstant
    ##   the X stiffness constant   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    @abstractmethod
    def XStiffnessConstant(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) XStiffnessConstant
          the X stiffness constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) YStiffnessConstant
    ##   the Y stiffness constant   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    @abstractmethod
    def YStiffnessConstant(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) YStiffnessConstant
          the Y stiffness constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ZStiffnessConstant
    ##   the Z stiffness constant   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    @abstractmethod
    def ZStiffnessConstant(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ZStiffnessConstant
          the Z stiffness constant   
            
         
        """
        pass
    
    ##  Gets supported stiffness types of connection. 
    ##  @return types (@link StiffnessType List[NXOpen.CAE.Connections.StiffnessType]@endlink):  Supported Stiffness Types .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    @abstractmethod
    def GetSupportedStiffnessTypes(connectionTag: IStiffness) -> List[StiffnessType]:
        """
         Gets supported stiffness types of connection. 
         @return types (@link StiffnessType List[NXOpen.CAE.Connections.StiffnessType]@endlink):  Supported Stiffness Types .
        """
        pass
    
import NXOpen
import NXOpen.Fields
##   @brief  This class represents an Interface to the StructuralDamping dynamic.  
## 
##   
## 
##   <br>  Created in NX12.0.0  <br> 

class IStructuralDampingDynamic(NXOpen.INXObject): 
    """ <summary> This class represents an Interface to the StructuralDamping dynamic. </summary> """


    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RxStructuralDampingDynamic
    ##   the RX structural damping dynamic   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Fields.ScalarFieldWrapper
    @property
    @abstractmethod
    def RxStructuralDampingDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RxStructuralDampingDynamic
          the RX structural damping dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RxStructuralDampingDynamic

    ##   the RX structural damping dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @RxStructuralDampingDynamic.setter
    def RxStructuralDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RxStructuralDampingDynamic
          the RX structural damping dynamic   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RyStructuralDampingDynamic
    ##   the RY structural damping dynamic   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Fields.ScalarFieldWrapper
    @property
    @abstractmethod
    def RyStructuralDampingDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RyStructuralDampingDynamic
          the RY structural damping dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RyStructuralDampingDynamic

    ##   the RY structural damping dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @RyStructuralDampingDynamic.setter
    def RyStructuralDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RyStructuralDampingDynamic
          the RY structural damping dynamic   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzStructuralDampingDynamic
    ##   the RZ structural damping dynamic   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Fields.ScalarFieldWrapper
    @property
    @abstractmethod
    def RzStructuralDampingDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzStructuralDampingDynamic
          the RZ structural damping dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzStructuralDampingDynamic

    ##   the RZ structural damping dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @RzStructuralDampingDynamic.setter
    def RzStructuralDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzStructuralDampingDynamic
          the RZ structural damping dynamic   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) XStructuralDampingDynamic
    ##   the X structural damping dynamic   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Fields.ScalarFieldWrapper
    @property
    @abstractmethod
    def XStructuralDampingDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) XStructuralDampingDynamic
          the X structural damping dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) XStructuralDampingDynamic

    ##   the X structural damping dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @XStructuralDampingDynamic.setter
    def XStructuralDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) XStructuralDampingDynamic
          the X structural damping dynamic   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) YStructuralDampingDynamic
    ##   the Y structural damping dynamic   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Fields.ScalarFieldWrapper
    @property
    @abstractmethod
    def YStructuralDampingDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) YStructuralDampingDynamic
          the Y structural damping dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) YStructuralDampingDynamic

    ##   the Y structural damping dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @YStructuralDampingDynamic.setter
    def YStructuralDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) YStructuralDampingDynamic
          the Y structural damping dynamic   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZStructuralDampingDynamic
    ##   the Z structural damping dynamic   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Fields.ScalarFieldWrapper
    @property
    @abstractmethod
    def ZStructuralDampingDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZStructuralDampingDynamic
          the Z structural damping dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZStructuralDampingDynamic

    ##   the Z structural damping dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @ZStructuralDampingDynamic.setter
    def ZStructuralDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZStructuralDampingDynamic
          the Z structural damping dynamic   
            
         
        """
        pass
    
import NXOpen
##   @brief  This class represents an Interface to the StructuralDamping constants.  
## 
##   
## 
##   <br>  Created in NX12.0.0  <br> 

class IStructuralDamping(NXOpen.INXObject): 
    """ <summary> This class represents an Interface to the StructuralDamping constants. </summary> """


    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RxStructuralDampingConstant
    ##   the RX structural damping constant   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    @abstractmethod
    def RxStructuralDampingConstant(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RxStructuralDampingConstant
          the RX structural damping constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RyStructuralDampingConstant
    ##   the RY structural damping constant   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    @abstractmethod
    def RyStructuralDampingConstant(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RyStructuralDampingConstant
          the RY structural damping constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RzStructuralDampingConstant
    ##   the RZ structural damping constant   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    @abstractmethod
    def RzStructuralDampingConstant(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RzStructuralDampingConstant
          the RZ structural damping constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) XStructuralDampingConstant
    ##   the X structural damping constant   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    @abstractmethod
    def XStructuralDampingConstant(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) XStructuralDampingConstant
          the X structural damping constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) YStructuralDampingConstant
    ##   the Y structural damping constant   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    @abstractmethod
    def YStructuralDampingConstant(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) YStructuralDampingConstant
          the Y structural damping constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ZStructuralDampingConstant
    ##   the Z structural damping constant   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    @abstractmethod
    def ZStructuralDampingConstant(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ZStructuralDampingConstant
          the Z structural damping constant   
            
         
        """
        pass
    
import NXOpen
##   @brief  This class represents an Interface to the Tolerance parameters.  
## 
##   
## 
##   <br>  Created in NX11.0.0  <br> 

class ITolerance(NXOpen.INXObject): 
    """ <summary> This class represents an Interface to the Tolerance parameters. </summary> """


    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxAngleBetweenNormals
    ##   the maximum angle of normals with the projection surface   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    @abstractmethod
    def MaxAngleBetweenNormals(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxAngleBetweenNormals
          the maximum angle of normals with the projection surface   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxDistCGToElemCG
    ##   the maximum distance from definition point to center of support element   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    @abstractmethod
    def MaxDistCGToElemCG(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxDistCGToElemCG
          the maximum distance from definition point to center of support element   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxNormalDistCGToFlanges
    ##   the maximum normal distance from definition point to center of element   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    @abstractmethod
    def MaxNormalDistCGToFlanges(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxNormalDistCGToFlanges
          the maximum normal distance from definition point to center of element   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ProjectTolerance
    ##   the projection tolerance   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    @abstractmethod
    def ProjectTolerance(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ProjectTolerance
          the projection tolerance   
            
         
        """
        pass
    
import NXOpen
import NXOpen.Fields
##   @brief  This class represents an Interface to the ViscousDamping dynamic.  
## 
##   
## 
##   <br>  Created in NX12.0.0  <br> 

class IViscousDampingDynamic(NXOpen.INXObject): 
    """ <summary> This class represents an Interface to the ViscousDamping dynamic. </summary> """


    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RxViscousDampingDynamic
    ##   the RX viscous damping dynamic   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Fields.ScalarFieldWrapper
    @property
    @abstractmethod
    def RxViscousDampingDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RxViscousDampingDynamic
          the RX viscous damping dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RxViscousDampingDynamic

    ##   the RX viscous damping dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @RxViscousDampingDynamic.setter
    def RxViscousDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RxViscousDampingDynamic
          the RX viscous damping dynamic   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RyViscousDampingDynamic
    ##   the RY viscous damping dynamic   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Fields.ScalarFieldWrapper
    @property
    @abstractmethod
    def RyViscousDampingDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RyViscousDampingDynamic
          the RY viscous damping dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RyViscousDampingDynamic

    ##   the RY viscous damping dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @RyViscousDampingDynamic.setter
    def RyViscousDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RyViscousDampingDynamic
          the RY viscous damping dynamic   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzViscousDampingDynamic
    ##   the RZ viscous damping dynamic   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Fields.ScalarFieldWrapper
    @property
    @abstractmethod
    def RzViscousDampingDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzViscousDampingDynamic
          the RZ viscous damping dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzViscousDampingDynamic

    ##   the RZ viscous damping dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @RzViscousDampingDynamic.setter
    def RzViscousDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzViscousDampingDynamic
          the RZ viscous damping dynamic   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) XViscousDampingDynamic
    ##   the X viscous damping dynamic   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Fields.ScalarFieldWrapper
    @property
    @abstractmethod
    def XViscousDampingDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) XViscousDampingDynamic
          the X viscous damping dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) XViscousDampingDynamic

    ##   the X viscous damping dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @XViscousDampingDynamic.setter
    def XViscousDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) XViscousDampingDynamic
          the X viscous damping dynamic   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) YViscousDampingDynamic
    ##   the Y viscous damping dynamic   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Fields.ScalarFieldWrapper
    @property
    @abstractmethod
    def YViscousDampingDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) YViscousDampingDynamic
          the Y viscous damping dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) YViscousDampingDynamic

    ##   the Y viscous damping dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @YViscousDampingDynamic.setter
    def YViscousDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) YViscousDampingDynamic
          the Y viscous damping dynamic   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZViscousDampingDynamic
    ##   the Z viscous damping dynamic   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Fields.ScalarFieldWrapper
    @property
    @abstractmethod
    def ZViscousDampingDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZViscousDampingDynamic
          the Z viscous damping dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZViscousDampingDynamic

    ##   the Z viscous damping dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @ZViscousDampingDynamic.setter
    def ZViscousDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZViscousDampingDynamic
          the Z viscous damping dynamic   
            
         
        """
        pass
    
import NXOpen
##   @brief  This class represents an Interface to the ViscousDamping constants.  
## 
##   
## 
##   <br>  Created in NX12.0.0  <br> 

class IViscousDamping(NXOpen.INXObject): 
    """ <summary> This class represents an Interface to the ViscousDamping constants. </summary> """


    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RxViscousDampingConstant
    ##   the RX viscous damping constant   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    @abstractmethod
    def RxViscousDampingConstant(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RxViscousDampingConstant
          the RX viscous damping constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RyViscousDampingConstant
    ##   the RY viscous damping constant   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    @abstractmethod
    def RyViscousDampingConstant(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RyViscousDampingConstant
          the RY viscous damping constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RzViscousDampingConstant
    ##   the RZ viscous damping constant   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    @abstractmethod
    def RzViscousDampingConstant(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RzViscousDampingConstant
          the RZ viscous damping constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) XViscousDampingConstant
    ##   the X viscous damping constant   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    @abstractmethod
    def XViscousDampingConstant(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) XViscousDampingConstant
          the X viscous damping constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) YViscousDampingConstant
    ##   the Y viscous damping constant   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    @abstractmethod
    def YViscousDampingConstant(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) YViscousDampingConstant
          the Y viscous damping constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ZViscousDampingConstant
    ##   the Z viscous damping constant   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    @abstractmethod
    def ZViscousDampingConstant(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ZViscousDampingConstant
          the Z viscous damping constant   
            
         
        """
        pass
    
import NXOpen
##   @brief  This class represents an Interface to the Width parameters.  
## 
##   
## 
##   <br>  Created in NX12.0.0  <br> 

class IWidth(NXOpen.INXObject): 
    """ <summary> This class represents an Interface to the Width parameters. </summary> """


    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Width
    ##   the width value   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    @abstractmethod
    def Width(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Width
          the width value   
            
         
        """
        pass
    
import NXOpen
import NXOpen.Assemblies
import NXOpen.CAE
import NXOpen.Features
##  @brief  This class contains join data utility methods  
## 
##     <br> To obtain an instance of this class, refer to @link NXOpen::CAE::CaeSession  NXOpen::CAE::CaeSession @endlink  <br> 
## 
##   <br>  Created in NX2206.0.0  <br> 

class JoinDataUtils(NXOpen.Object): 
    """<summary> This class contains join data utility methods </summary>  """


    ##  Function that creates connections based on the feature records
    ##  @return connections (@link IConnection List[NXOpen.CAE.Connections.IConnection]@endlink): The created connections based on the join features.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##  The join features 
    def CreateConnectionsFromJoinFeatures(features: List[NXOpen.Features.Feature], components: List[NXOpen.Assemblies.Component]) -> List[IConnection]:
        """
         Function that creates connections based on the feature records
         @return connections (@link IConnection List[NXOpen.CAE.Connections.IConnection]@endlink): The created connections based on the join features.
        """
        pass
    
    ##  Function that loads the required CAD components 
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##  The FE Model 
    def LoadCadComponents(feModel: NXOpen.CAE.IFEModel, cadComponentsLoadType: CadComponentsLoadType) -> None:
        """
         Function that loads the required CAD components 
        """
        pass
    
import NXOpen
##  Kinematic connection. Use this interface to set/get properties and parameters of the Kinematic connection.  
## 
##   <br>  Created in NX12.0.0  <br> 

class Kinematic(IConnection): 
    """ Kinematic connection. Use this interface to set/get properties and parameters of the Kinematic connection.  """


    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) CharacteristicLengthRadius
    ##   the radius characteristic length used by Revolute and Spherical Kinematic   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def CharacteristicLengthRadius(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) CharacteristicLengthRadius
          the radius characteristic length used by Revolute and Spherical Kinematic   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) Csys
    ##   the csys   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.CoordinateSystem
    @property
    def Csys(self) -> NXOpen.CoordinateSystem:
        """
        Getter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) Csys
          the csys   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) Csys

    ##   the csys   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @Csys.setter
    def Csys(self, csys: NXOpen.CoordinateSystem):
        """
        Setter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) Csys
          the csys   
            
         
        """
        pass
    
    ## Getter for property: (@link CsysType NXOpen.CAE.Connections.CsysType@endlink) CsysType
    ##   the csys type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return CsysType
    @property
    def CsysType(self) -> CsysType:
        """
        Getter for property: (@link CsysType NXOpen.CAE.Connections.CsysType@endlink) CsysType
          the csys type   
            
         
        """
        pass
    
    ## Setter for property: (@link CsysType NXOpen.CAE.Connections.CsysType@endlink) CsysType

    ##   the csys type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @CsysType.setter
    def CsysType(self, csysType: CsysType):
        """
        Setter for property: (@link CsysType NXOpen.CAE.Connections.CsysType@endlink) CsysType
          the csys type   
            
         
        """
        pass
    
    ## Getter for property: (@link DofCombination NXOpen.CAE.Connections.DofCombination@endlink) DofCombination
    ##   the degrees of freedom combination type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return DofCombination
    @property
    def DofCombination(self) -> DofCombination:
        """
        Getter for property: (@link DofCombination NXOpen.CAE.Connections.DofCombination@endlink) DofCombination
          the degrees of freedom combination type   
            
         
        """
        pass
    
    ## Setter for property: (@link DofCombination NXOpen.CAE.Connections.DofCombination@endlink) DofCombination

    ##   the degrees of freedom combination type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @DofCombination.setter
    def DofCombination(self, type: DofCombination):
        """
        Setter for property: (@link DofCombination NXOpen.CAE.Connections.DofCombination@endlink) DofCombination
          the degrees of freedom combination type   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) FrictionCoefficient
    ##   the friction coefficient   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def FrictionCoefficient(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) FrictionCoefficient
          the friction coefficient   
            
         
        """
        pass
    
    ## Getter for property: (@link NodalPairingMethod NXOpen.CAE.Connections.NodalPairingMethod@endlink) PairingMethod
    ##   the pairing method of targets   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NodalPairingMethod
    @property
    def PairingMethod(self) -> NodalPairingMethod:
        """
        Getter for property: (@link NodalPairingMethod NXOpen.CAE.Connections.NodalPairingMethod@endlink) PairingMethod
          the pairing method of targets   
            
         
        """
        pass
    
    ## Setter for property: (@link NodalPairingMethod NXOpen.CAE.Connections.NodalPairingMethod@endlink) PairingMethod

    ##   the pairing method of targets   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @PairingMethod.setter
    def PairingMethod(self, method: NodalPairingMethod):
        """
        Setter for property: (@link NodalPairingMethod NXOpen.CAE.Connections.NodalPairingMethod@endlink) PairingMethod
          the pairing method of targets   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) SearchConeAngle
    ##   the search cone angle   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def SearchConeAngle(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) SearchConeAngle
          the search cone angle   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) SearchOrientation
    ##   the pairing search orientation   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Direction
    @property
    def SearchOrientation(self) -> NXOpen.Direction:
        """
        Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) SearchOrientation
          the pairing search orientation   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) SearchOrientation

    ##   the pairing search orientation   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @SearchOrientation.setter
    def SearchOrientation(self, orientation: NXOpen.Direction):
        """
        Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) SearchOrientation
          the pairing search orientation   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) SearchRange
    ##   the search range   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def SearchRange(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) SearchRange
          the search range   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) TighteningForce
    ##   the tightening force   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def TighteningForce(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) TighteningForce
          the tightening force   
            
         
        """
        pass
    
    ## Getter for property: (bool) UseFriction
    ##   the flag indicating whether to use friction parameters or not   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return bool
    @property
    def UseFriction(self) -> bool:
        """
        Getter for property: (bool) UseFriction
          the flag indicating whether to use friction parameters or not   
            
         
        """
        pass
    
    ## Setter for property: (bool) UseFriction

    ##   the flag indicating whether to use friction parameters or not   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @UseFriction.setter
    def UseFriction(self, useFriction: bool):
        """
        Setter for property: (bool) UseFriction
          the flag indicating whether to use friction parameters or not   
            
         
        """
        pass
    
import NXOpen
##   LMIEBody   <br> No creator  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class LMIEBody(NXOpen.TaggedObject): 
    """  LMIEBody  """
    pass


##   Lumped Mass Center Definition. Use this interface to set/get properties and parameters of the Lumped Mass Center Definition.   <br> No creator  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class LMIECenterDefinition(LMIEError): 
    """  Lumped Mass Center Definition. Use this interface to set/get properties and parameters of the Lumped Mass Center Definition.  """


    ## Getter for property: (@link MassCenterType NXOpen.CAE.Connections.MassCenterType@endlink) MassCenterType
    ##   the mass center type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return MassCenterType
    @property
    def MassCenterType(self) -> MassCenterType:
        """
        Getter for property: (@link MassCenterType NXOpen.CAE.Connections.MassCenterType@endlink) MassCenterType
          the mass center type   
            
         
        """
        pass
    
    ## Setter for property: (@link MassCenterType NXOpen.CAE.Connections.MassCenterType@endlink) MassCenterType

    ##   the mass center type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @MassCenterType.setter
    def MassCenterType(self, massCenterType: MassCenterType):
        """
        Setter for property: (@link MassCenterType NXOpen.CAE.Connections.MassCenterType@endlink) MassCenterType
          the mass center type   
            
         
        """
        pass
    
    ## Getter for property: (@link LMIENode NXOpen.CAE.Connections.LMIENode@endlink) Node
    ##   the node   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return LMIENode
    @property
    def Node(self) -> LMIENode:
        """
        Getter for property: (@link LMIENode NXOpen.CAE.Connections.LMIENode@endlink) Node
          the node   
            
         
        """
        pass
    
    ## Setter for property: (@link LMIENode NXOpen.CAE.Connections.LMIENode@endlink) Node

    ##   the node   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @Node.setter
    def Node(self, node: LMIENode):
        """
        Setter for property: (@link LMIENode NXOpen.CAE.Connections.LMIENode@endlink) Node
          the node   
            
         
        """
        pass
    
    ## Getter for property: (@link LMIEPoint NXOpen.CAE.Connections.LMIEPoint@endlink) Point
    ##   the point   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return LMIEPoint
    @property
    def Point(self) -> LMIEPoint:
        """
        Getter for property: (@link LMIEPoint NXOpen.CAE.Connections.LMIEPoint@endlink) Point
          the point   
            
         
        """
        pass
    
    ## Setter for property: (@link LMIEPoint NXOpen.CAE.Connections.LMIEPoint@endlink) Point

    ##   the point   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @Point.setter
    def Point(self, point: LMIEPoint):
        """
        Setter for property: (@link LMIEPoint NXOpen.CAE.Connections.LMIEPoint@endlink) Point
          the point   
            
         
        """
        pass
    
    ## Getter for property: (@link LMIESelectionRecipe NXOpen.CAE.Connections.LMIESelectionRecipe@endlink) SelectionRecipe
    ##   the selection recipe   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return LMIESelectionRecipe
    @property
    def SelectionRecipe(self) -> LMIESelectionRecipe:
        """
        Getter for property: (@link LMIESelectionRecipe NXOpen.CAE.Connections.LMIESelectionRecipe@endlink) SelectionRecipe
          the selection recipe   
            
         
        """
        pass
    
    ## Setter for property: (@link LMIESelectionRecipe NXOpen.CAE.Connections.LMIESelectionRecipe@endlink) SelectionRecipe

    ##   the selection recipe   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @SelectionRecipe.setter
    def SelectionRecipe(self, recipe: LMIESelectionRecipe):
        """
        Setter for property: (@link LMIESelectionRecipe NXOpen.CAE.Connections.LMIESelectionRecipe@endlink) SelectionRecipe
          the selection recipe   
            
         
        """
        pass
    
    ##  Create a standalone node 
    ##  @return node (@link LMIENode NXOpen.CAE.Connections.LMIENode@endlink):  Center Node .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    def CreateNode(obj: LMIECenterDefinition) -> LMIENode:
        """
         Create a standalone node 
         @return node (@link LMIENode NXOpen.CAE.Connections.LMIENode@endlink):  Center Node .
        """
        pass
    
    ##  Create a standalone point 
    ##  @return point (@link LMIEPoint NXOpen.CAE.Connections.LMIEPoint@endlink):  Center Point .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    def CreatePoint(obj: LMIECenterDefinition) -> LMIEPoint:
        """
         Create a standalone point 
         @return point (@link LMIEPoint NXOpen.CAE.Connections.LMIEPoint@endlink):  Center Point .
        """
        pass
    
    ##  Create a standalone selection recipe 
    ##  @return recipe (@link LMIESelectionRecipe NXOpen.CAE.Connections.LMIESelectionRecipe@endlink):  Center Selection Recipe .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    def CreateSelectionRecipe(obj: LMIECenterDefinition) -> LMIESelectionRecipe:
        """
         Create a standalone selection recipe 
         @return recipe (@link LMIESelectionRecipe NXOpen.CAE.Connections.LMIESelectionRecipe@endlink):  Center Selection Recipe .
        """
        pass
    
##   LMIEConnection   <br> No creator  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class LMIEConnection(LMIEError): 
    """  LMIEConnection  """


    ## Getter for property: (@link LMIECenterDefinition NXOpen.CAE.Connections.LMIECenterDefinition@endlink) CenterDefinition
    ##   the center definition   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return LMIECenterDefinition
    @property
    def CenterDefinition(self) -> LMIECenterDefinition:
        """
        Getter for property: (@link LMIECenterDefinition NXOpen.CAE.Connections.LMIECenterDefinition@endlink) CenterDefinition
          the center definition   
            
         
        """
        pass
    
    ## Setter for property: (@link LMIECenterDefinition NXOpen.CAE.Connections.LMIECenterDefinition@endlink) CenterDefinition

    ##   the center definition   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @CenterDefinition.setter
    def CenterDefinition(self, opt: LMIECenterDefinition):
        """
        Setter for property: (@link LMIECenterDefinition NXOpen.CAE.Connections.LMIECenterDefinition@endlink) CenterDefinition
          the center definition   
            
         
        """
        pass
    
    ## Getter for property: (@link ElementType NXOpen.CAE.Connections.ElementType@endlink) ConnectionElementType
    ##   the connection element type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return ElementType
    @property
    def ConnectionElementType(self) -> ElementType:
        """
        Getter for property: (@link ElementType NXOpen.CAE.Connections.ElementType@endlink) ConnectionElementType
          the connection element type   
            
         
        """
        pass
    
    ## Setter for property: (@link ElementType NXOpen.CAE.Connections.ElementType@endlink) ConnectionElementType

    ##   the connection element type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @ConnectionElementType.setter
    def ConnectionElementType(self, connElementType: ElementType):
        """
        Setter for property: (@link ElementType NXOpen.CAE.Connections.ElementType@endlink) ConnectionElementType
          the connection element type   
            
         
        """
        pass
    
    ## Getter for property: (str) Description
    ##   the mass description   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return str
    @property
    def Description(self) -> str:
        """
        Getter for property: (str) Description
          the mass description   
            
         
        """
        pass
    
    ## Setter for property: (str) Description

    ##   the mass description   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @Description.setter
    def Description(self, desc: str):
        """
        Setter for property: (str) Description
          the mass description   
            
         
        """
        pass
    
    ## Getter for property: (str) FolderName
    ##   the folder name   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return str
    @property
    def FolderName(self) -> str:
        """
        Getter for property: (str) FolderName
          the folder name   
            
         
        """
        pass
    
    ## Setter for property: (str) FolderName

    ##   the folder name   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @FolderName.setter
    def FolderName(self, folderName: str):
        """
        Setter for property: (str) FolderName
          the folder name   
            
         
        """
        pass
    
    ## Getter for property: (int) Id
    ##   the ID   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return int
    @property
    def Id(self) -> int:
        """
        Getter for property: (int) Id
          the ID   
            
         
        """
        pass
    
    ## Setter for property: (int) Id

    ##   the ID   
    ##     
    ##  
    ## Setter License requirements: sc_gso_10 (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @Id.setter
    def Id(self, pId: int):
        """
        Setter for property: (int) Id
          the ID   
            
         
        """
        pass
    
    ## Getter for property: (@link LMIEInertia NXOpen.CAE.Connections.LMIEInertia@endlink) Inertia
    ##   the inertia   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return LMIEInertia
    @property
    def Inertia(self) -> LMIEInertia:
        """
        Getter for property: (@link LMIEInertia NXOpen.CAE.Connections.LMIEInertia@endlink) Inertia
          the inertia   
            
         
        """
        pass
    
    ## Setter for property: (@link LMIEInertia NXOpen.CAE.Connections.LMIEInertia@endlink) Inertia

    ##   the inertia   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @Inertia.setter
    def Inertia(self, opt: LMIEInertia):
        """
        Setter for property: (@link LMIEInertia NXOpen.CAE.Connections.LMIEInertia@endlink) Inertia
          the inertia   
            
         
        """
        pass
    
    ## Getter for property: (@link LMIELegConnection NXOpen.CAE.Connections.LMIELegConnection@endlink) LegConnection
    ##   the leg connection   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return LMIELegConnection
    @property
    def LegConnection(self) -> LMIELegConnection:
        """
        Getter for property: (@link LMIELegConnection NXOpen.CAE.Connections.LMIELegConnection@endlink) LegConnection
          the leg connection   
            
         
        """
        pass
    
    ## Setter for property: (@link LMIELegConnection NXOpen.CAE.Connections.LMIELegConnection@endlink) LegConnection

    ##   the leg connection   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @LegConnection.setter
    def LegConnection(self, opt: LMIELegConnection):
        """
        Setter for property: (@link LMIELegConnection NXOpen.CAE.Connections.LMIELegConnection@endlink) LegConnection
          the leg connection   
            
         
        """
        pass
    
    ## Getter for property: (@link LMIEMass NXOpen.CAE.Connections.LMIEMass@endlink) Mass
    ##   the mass   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return LMIEMass
    @property
    def Mass(self) -> LMIEMass:
        """
        Getter for property: (@link LMIEMass NXOpen.CAE.Connections.LMIEMass@endlink) Mass
          the mass   
            
         
        """
        pass
    
    ## Setter for property: (@link LMIEMass NXOpen.CAE.Connections.LMIEMass@endlink) Mass

    ##   the mass   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @Mass.setter
    def Mass(self, opt: LMIEMass):
        """
        Setter for property: (@link LMIEMass NXOpen.CAE.Connections.LMIEMass@endlink) Mass
          the mass   
            
         
        """
        pass
    
    ## Getter for property: (str) Plvc
    ##   the plvc   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return str
    @property
    def Plvc(self) -> str:
        """
        Getter for property: (str) Plvc
          the plvc   
            
         
        """
        pass
    
    ## Setter for property: (str) Plvc

    ##   the plvc   
    ##     
    ##  
    ## Setter License requirements: sc_gso_10 (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @Plvc.setter
    def Plvc(self, pPlvc: str):
        """
        Setter for property: (str) Plvc
          the plvc   
            
         
        """
        pass
    
    ## Getter for property: (@link LMIEUnitSystem NXOpen.CAE.Connections.LMIEUnitSystem@endlink) UnitSystem
    ##   the unit system    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return LMIEUnitSystem
    @property
    def UnitSystem(self) -> LMIEUnitSystem:
        """
        Getter for property: (@link LMIEUnitSystem NXOpen.CAE.Connections.LMIEUnitSystem@endlink) UnitSystem
          the unit system    
            
         
        """
        pass
    
    ## Setter for property: (@link LMIEUnitSystem NXOpen.CAE.Connections.LMIEUnitSystem@endlink) UnitSystem

    ##   the unit system    
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @UnitSystem.setter
    def UnitSystem(self, opt: LMIEUnitSystem):
        """
        Setter for property: (@link LMIEUnitSystem NXOpen.CAE.Connections.LMIEUnitSystem@endlink) UnitSystem
          the unit system    
            
         
        """
        pass
    
    ##  Create a standalone center definition 
    ##  @return opt (@link LMIECenterDefinition NXOpen.CAE.Connections.LMIECenterDefinition@endlink):  The center definition .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    def CreateCenterDefinition(obj: LMIEConnection) -> LMIECenterDefinition:
        """
         Create a standalone center definition 
         @return opt (@link LMIECenterDefinition NXOpen.CAE.Connections.LMIECenterDefinition@endlink):  The center definition .
        """
        pass
    
    ##  Create a standalone inertia 
    ##  @return opt (@link LMIEInertia NXOpen.CAE.Connections.LMIEInertia@endlink):  The inertia .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    def CreateInertia(obj: LMIEConnection) -> LMIEInertia:
        """
         Create a standalone inertia 
         @return opt (@link LMIEInertia NXOpen.CAE.Connections.LMIEInertia@endlink):  The inertia .
        """
        pass
    
    ##  Create a standalone leg connection 
    ##  @return opt (@link LMIELegConnection NXOpen.CAE.Connections.LMIELegConnection@endlink):  The leg connection .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    def CreateLegConnection(obj: LMIEConnection) -> LMIELegConnection:
        """
         Create a standalone leg connection 
         @return opt (@link LMIELegConnection NXOpen.CAE.Connections.LMIELegConnection@endlink):  The leg connection .
        """
        pass
    
    ##  Create a standalone leg definition 
    ##  @return opt (@link LMIELegDefinition NXOpen.CAE.Connections.LMIELegDefinition@endlink):  The leg definition .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    def CreateLegDefinition(obj: LMIEConnection) -> LMIELegDefinition:
        """
         Create a standalone leg definition 
         @return opt (@link LMIELegDefinition NXOpen.CAE.Connections.LMIELegDefinition@endlink):  The leg definition .
        """
        pass
    
    ##  Create a standalone mass 
    ##  @return opt (@link LMIEMass NXOpen.CAE.Connections.LMIEMass@endlink):  Mass Options .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    def CreateMass(obj: LMIEConnection) -> LMIEMass:
        """
         Create a standalone mass 
         @return opt (@link LMIEMass NXOpen.CAE.Connections.LMIEMass@endlink):  Mass Options .
        """
        pass
    
    ##  Create a standalone unit system  
    ##  @return opt (@link LMIEUnitSystem NXOpen.CAE.Connections.LMIEUnitSystem@endlink):  Unit System .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    def CreateUnitSystem(obj: LMIEConnection) -> LMIEUnitSystem:
        """
         Create a standalone unit system  
         @return opt (@link LMIEUnitSystem NXOpen.CAE.Connections.LMIEUnitSystem@endlink):  Unit System .
        """
        pass
    
    ##  Get the leg definitions 
    ##  @return opt (@link LMIELegDefinition List[NXOpen.CAE.Connections.LMIELegDefinition]@endlink):  The leg definitions .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetLegDefinitions(obj: LMIEConnection) -> List[LMIELegDefinition]:
        """
         Get the leg definitions 
         @return opt (@link LMIELegDefinition List[NXOpen.CAE.Connections.LMIELegDefinition]@endlink):  The leg definitions .
        """
        pass
    
    ##  Set the leg definitions 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ##  The leg definitions 
    def SetLegDefinitions(obj: LMIEConnection, opt: List[LMIELegDefinition]) -> None:
        """
         Set the leg definitions 
        """
        pass
    
import NXOpen
##   LMIEElementEdge object   <br> No creator  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class LMIEElementEdge(NXOpen.TaggedObject): 
    """  LMIEElementEdge object  """


    ## Getter for property: (int) EdgeNumber
    ##   the edge number   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return int
    @property
    def EdgeNumber(self) -> int:
        """
        Getter for property: (int) EdgeNumber
          the edge number   
            
         
        """
        pass
    
    ## Setter for property: (int) EdgeNumber

    ##   the edge number   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @EdgeNumber.setter
    def EdgeNumber(self, edgeNumber: int):
        """
        Setter for property: (int) EdgeNumber
          the edge number   
            
         
        """
        pass
    
    ## Getter for property: (str) Id
    ##   the element id   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return str
    @property
    def Id(self) -> str:
        """
        Getter for property: (str) Id
          the element id   
            
         
        """
        pass
    
    ## Setter for property: (str) Id

    ##   the element id   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @Id.setter
    def Id(self, elementId: str):
        """
        Setter for property: (str) Id
          the element id   
            
         
        """
        pass
    
import NXOpen
##   LMIEElementFace object   <br> No creator  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class LMIEElementFace(NXOpen.TaggedObject): 
    """  LMIEElementFace object  """


    ## Getter for property: (int) FaceNumber
    ##   the face number   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return int
    @property
    def FaceNumber(self) -> int:
        """
        Getter for property: (int) FaceNumber
          the face number   
            
         
        """
        pass
    
    ## Setter for property: (int) FaceNumber

    ##   the face number   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @FaceNumber.setter
    def FaceNumber(self, faceNumber: int):
        """
        Setter for property: (int) FaceNumber
          the face number   
            
         
        """
        pass
    
    ## Getter for property: (str) Id
    ##   the element id   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return str
    @property
    def Id(self) -> str:
        """
        Getter for property: (str) Id
          the element id   
            
         
        """
        pass
    
    ## Setter for property: (str) Id

    ##   the element id   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @Id.setter
    def Id(self, elementId: str):
        """
        Setter for property: (str) Id
          the element id   
            
         
        """
        pass
    
import NXOpen
##   LMIEElement object   <br> No creator  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class LMIEElement(NXOpen.TaggedObject): 
    """  LMIEElement object  """


    ## Getter for property: (str) Id
    ##   the element id   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return str
    @property
    def Id(self) -> str:
        """
        Getter for property: (str) Id
          the element id   
            
         
        """
        pass
    
    ## Setter for property: (str) Id

    ##   the element id   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @Id.setter
    def Id(self, unit: str):
        """
        Setter for property: (str) Id
          the element id   
            
         
        """
        pass
    
import NXOpen
##   LMIEError   <br> No creator  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class LMIEError(NXOpen.NXObject): 
    """  LMIEError  """


    ##  The error codes 
    ##  @return errorCodes (List[str]):  The error codes .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetErrorCodes(obj: LMIEError) -> List[str]:
        """
         The error codes 
         @return errorCodes (List[str]):  The error codes .
        """
        pass
    
    ##  The error messages 
    ##  @return errorMsgs (List[str]):  The error messages .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetErrorMessages(obj: LMIEError) -> List[str]:
        """
         The error messages 
         @return errorMsgs (List[str]):  The error messages .
        """
        pass
    
    ##  The error values for an error 
    ##  @return errorValues (List[str]):  The error values for an error .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="errorIndex"> (int) </param>
    def GetErrorValues(obj: LMIEError, errorIndex: int) -> List[str]:
        """
         The error values for an error 
         @return errorValues (List[str]):  The error values for an error .
        """
        pass
    
    ##  The warning codes 
    ##  @return warningCodes (List[str]):  The warning codes .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetWarningCodes(obj: LMIEError) -> List[str]:
        """
         The warning codes 
         @return warningCodes (List[str]):  The warning codes .
        """
        pass
    
    ##  Has errors 
    ##  @return hasErrors (bool): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def HasErrors(obj: LMIEError) -> bool:
        """
         Has errors 
         @return hasErrors (bool): .
        """
        pass
    
##   Lumped mass import export inertia object.   <br> No creator  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class LMIEInertia(LMIEError): 
    """  Lumped mass import export inertia object.  """


    ## Getter for property: (float) Ixx
    ##   the Ixx value   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return float
    @property
    def Ixx(self) -> float:
        """
        Getter for property: (float) Ixx
          the Ixx value   
            
         
        """
        pass
    
    ## Setter for property: (float) Ixx

    ##   the Ixx value   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @Ixx.setter
    def Ixx(self, outputValue: float):
        """
        Setter for property: (float) Ixx
          the Ixx value   
            
         
        """
        pass
    
    ## Getter for property: (float) Iyx
    ##   the Iyx value   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return float
    @property
    def Iyx(self) -> float:
        """
        Getter for property: (float) Iyx
          the Iyx value   
            
         
        """
        pass
    
    ## Setter for property: (float) Iyx

    ##   the Iyx value   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @Iyx.setter
    def Iyx(self, outputValue: float):
        """
        Setter for property: (float) Iyx
          the Iyx value   
            
         
        """
        pass
    
    ## Getter for property: (float) Iyy
    ##   the Iyy value   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return float
    @property
    def Iyy(self) -> float:
        """
        Getter for property: (float) Iyy
          the Iyy value   
            
         
        """
        pass
    
    ## Setter for property: (float) Iyy

    ##   the Iyy value   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @Iyy.setter
    def Iyy(self, outputValue: float):
        """
        Setter for property: (float) Iyy
          the Iyy value   
            
         
        """
        pass
    
    ## Getter for property: (float) Izx
    ##   the Izx value   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return float
    @property
    def Izx(self) -> float:
        """
        Getter for property: (float) Izx
          the Izx value   
            
         
        """
        pass
    
    ## Setter for property: (float) Izx

    ##   the Izx value   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @Izx.setter
    def Izx(self, outputValue: float):
        """
        Setter for property: (float) Izx
          the Izx value   
            
         
        """
        pass
    
    ## Getter for property: (float) Izy
    ##   the Izy value   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return float
    @property
    def Izy(self) -> float:
        """
        Getter for property: (float) Izy
          the Izy value   
            
         
        """
        pass
    
    ## Setter for property: (float) Izy

    ##   the Izy value   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @Izy.setter
    def Izy(self, outputValue: float):
        """
        Setter for property: (float) Izy
          the Izy value   
            
         
        """
        pass
    
    ## Getter for property: (float) Izz
    ##   the Izz value   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return float
    @property
    def Izz(self) -> float:
        """
        Getter for property: (float) Izz
          the Izz value   
            
         
        """
        pass
    
    ## Setter for property: (float) Izz

    ##   the Izz value   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @Izz.setter
    def Izz(self, outputValue: float):
        """
        Setter for property: (float) Izz
          the Izz value   
            
         
        """
        pass
    
##   Mass definition.   <br> No creator  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class LMIELegConnection(LMIEError): 
    """  Mass definition.  """


    ## Getter for property: (@link MassConnectivityType NXOpen.CAE.Connections.MassConnectivityType@endlink) LegConnectionType
    ##   the leg connection type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return MassConnectivityType
    @property
    def LegConnectionType(self) -> MassConnectivityType:
        """
        Getter for property: (@link MassConnectivityType NXOpen.CAE.Connections.MassConnectivityType@endlink) LegConnectionType
          the leg connection type   
            
         
        """
        pass
    
    ## Setter for property: (@link MassConnectivityType NXOpen.CAE.Connections.MassConnectivityType@endlink) LegConnectionType

    ##   the leg connection type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @LegConnectionType.setter
    def LegConnectionType(self, type: MassConnectivityType):
        """
        Setter for property: (@link MassConnectivityType NXOpen.CAE.Connections.MassConnectivityType@endlink) LegConnectionType
          the leg connection type   
            
         
        """
        pass
    
    ## Getter for property: (@link LMIELocalSpiders NXOpen.CAE.Connections.LMIELocalSpiders@endlink) LocalSpiders
    ##   the local spiders   
    ##     
    ##  
    ## Getter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return LMIELocalSpiders
    @property
    def LocalSpiders(self) -> LMIELocalSpiders:
        """
        Getter for property: (@link LMIELocalSpiders NXOpen.CAE.Connections.LMIELocalSpiders@endlink) LocalSpiders
          the local spiders   
            
         
        """
        pass
    
    ## Setter for property: (@link LMIELocalSpiders NXOpen.CAE.Connections.LMIELocalSpiders@endlink) LocalSpiders

    ##   the local spiders   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @LocalSpiders.setter
    def LocalSpiders(self, opt: LMIELocalSpiders):
        """
        Setter for property: (@link LMIELocalSpiders NXOpen.CAE.Connections.LMIELocalSpiders@endlink) LocalSpiders
          the local spiders   
            
         
        """
        pass
    
    ## Getter for property: (@link LMIENearestNodes NXOpen.CAE.Connections.LMIENearestNodes@endlink) NearestNodes
    ##   the nearest nodes   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return LMIENearestNodes
    @property
    def NearestNodes(self) -> LMIENearestNodes:
        """
        Getter for property: (@link LMIENearestNodes NXOpen.CAE.Connections.LMIENearestNodes@endlink) NearestNodes
          the nearest nodes   
            
         
        """
        pass
    
    ## Setter for property: (@link LMIENearestNodes NXOpen.CAE.Connections.LMIENearestNodes@endlink) NearestNodes

    ##   the nearest nodes   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @NearestNodes.setter
    def NearestNodes(self, opt: LMIENearestNodes):
        """
        Setter for property: (@link LMIENearestNodes NXOpen.CAE.Connections.LMIENearestNodes@endlink) NearestNodes
          the nearest nodes   
            
         
        """
        pass
    
    ##  Create a standalone local spiders 
    ##  @return opt (@link LMIELocalSpiders NXOpen.CAE.Connections.LMIELocalSpiders@endlink):  Local spiders .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    def CreateLocalSpiders(obj: LMIELegConnection) -> LMIELocalSpiders:
        """
         Create a standalone local spiders 
         @return opt (@link LMIELocalSpiders NXOpen.CAE.Connections.LMIELocalSpiders@endlink):  Local spiders .
        """
        pass
    
    ##  Create a standalone nearest nodes 
    ##  @return opt (@link LMIENearestNodes NXOpen.CAE.Connections.LMIENearestNodes@endlink):  Nearest nodes .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    def CreateNearestNodes(obj: LMIELegConnection) -> LMIENearestNodes:
        """
         Create a standalone nearest nodes 
         @return opt (@link LMIENearestNodes NXOpen.CAE.Connections.LMIENearestNodes@endlink):  Nearest nodes .
        """
        pass
    
##   Mass definition.   <br> No creator  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class LMIELegDefinition(LMIEError): 
    """  Mass definition.  """


    ## Getter for property: (@link LMIENode NXOpen.CAE.Connections.LMIENode@endlink) Node
    ##   the node   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return LMIENode
    @property
    def Node(self) -> LMIENode:
        """
        Getter for property: (@link LMIENode NXOpen.CAE.Connections.LMIENode@endlink) Node
          the node   
            
         
        """
        pass
    
    ## Setter for property: (@link LMIENode NXOpen.CAE.Connections.LMIENode@endlink) Node

    ##   the node   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @Node.setter
    def Node(self, node: LMIENode):
        """
        Setter for property: (@link LMIENode NXOpen.CAE.Connections.LMIENode@endlink) Node
          the node   
            
         
        """
        pass
    
    ## Getter for property: (@link LMIEPoint NXOpen.CAE.Connections.LMIEPoint@endlink) Point
    ##   the point   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return LMIEPoint
    @property
    def Point(self) -> LMIEPoint:
        """
        Getter for property: (@link LMIEPoint NXOpen.CAE.Connections.LMIEPoint@endlink) Point
          the point   
            
         
        """
        pass
    
    ## Setter for property: (@link LMIEPoint NXOpen.CAE.Connections.LMIEPoint@endlink) Point

    ##   the point   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @Point.setter
    def Point(self, point: LMIEPoint):
        """
        Setter for property: (@link LMIEPoint NXOpen.CAE.Connections.LMIEPoint@endlink) Point
          the point   
            
         
        """
        pass
    
    ## Getter for property: (@link LMIESelectionRecipe NXOpen.CAE.Connections.LMIESelectionRecipe@endlink) SelectionRecipe
    ##   the selection recipe   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return LMIESelectionRecipe
    @property
    def SelectionRecipe(self) -> LMIESelectionRecipe:
        """
        Getter for property: (@link LMIESelectionRecipe NXOpen.CAE.Connections.LMIESelectionRecipe@endlink) SelectionRecipe
          the selection recipe   
            
         
        """
        pass
    
    ## Setter for property: (@link LMIESelectionRecipe NXOpen.CAE.Connections.LMIESelectionRecipe@endlink) SelectionRecipe

    ##   the selection recipe   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @SelectionRecipe.setter
    def SelectionRecipe(self, recipe: LMIESelectionRecipe):
        """
        Setter for property: (@link LMIESelectionRecipe NXOpen.CAE.Connections.LMIESelectionRecipe@endlink) SelectionRecipe
          the selection recipe   
            
         
        """
        pass
    
    ##  Create a standalone node 
    ##  @return node (@link LMIENode NXOpen.CAE.Connections.LMIENode@endlink):  Leg Node .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    def CreateNode(obj: LMIELegDefinition) -> LMIENode:
        """
         Create a standalone node 
         @return node (@link LMIENode NXOpen.CAE.Connections.LMIENode@endlink):  Leg Node .
        """
        pass
    
    ##  Create a standalone point 
    ##  @return point (@link LMIEPoint NXOpen.CAE.Connections.LMIEPoint@endlink):  Leg Point .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    def CreatePoint(obj: LMIELegDefinition) -> LMIEPoint:
        """
         Create a standalone point 
         @return point (@link LMIEPoint NXOpen.CAE.Connections.LMIEPoint@endlink):  Leg Point .
        """
        pass
    
    ##  Create a standalone selection recipe 
    ##  @return recipe (@link LMIESelectionRecipe NXOpen.CAE.Connections.LMIESelectionRecipe@endlink):  Leg Selection Recipe .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    def CreateSelectionRecipe(obj: LMIELegDefinition) -> LMIESelectionRecipe:
        """
         Create a standalone selection recipe 
         @return recipe (@link LMIESelectionRecipe NXOpen.CAE.Connections.LMIESelectionRecipe@endlink):  Leg Selection Recipe .
        """
        pass
    
##   Local Spider Center Options definition.   <br> No creator  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class LMIELocalSpiderCenterOptions(LMIEError): 
    """  Local Spider Center Options definition.  """


    ## Getter for property: (@link LocalSpiderCenterType NXOpen.CAE.Connections.LocalSpiderCenterType@endlink) LocalSpiderCenterType
    ##   the Local Spider Center type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return LocalSpiderCenterType
    @property
    def LocalSpiderCenterType(self) -> LocalSpiderCenterType:
        """
        Getter for property: (@link LocalSpiderCenterType NXOpen.CAE.Connections.LocalSpiderCenterType@endlink) LocalSpiderCenterType
          the Local Spider Center type   
            
         
        """
        pass
    
    ## Setter for property: (@link LocalSpiderCenterType NXOpen.CAE.Connections.LocalSpiderCenterType@endlink) LocalSpiderCenterType

    ##   the Local Spider Center type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @LocalSpiderCenterType.setter
    def LocalSpiderCenterType(self, type: LocalSpiderCenterType):
        """
        Setter for property: (@link LocalSpiderCenterType NXOpen.CAE.Connections.LocalSpiderCenterType@endlink) LocalSpiderCenterType
          the Local Spider Center type   
            
         
        """
        pass
    
##   Mass Local Spiders definition.   <br> No creator  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class LMIELocalSpiders(LMIEError): 
    """  Mass Local Spiders definition.  """


    ## Getter for property: (@link LMIELocalSpiderCenterOptions NXOpen.CAE.Connections.LMIELocalSpiderCenterOptions@endlink) LocalSpiderCenterOptions
    ##   the local spider center options   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return LMIELocalSpiderCenterOptions
    @property
    def LocalSpiderCenterOptions(self) -> LMIELocalSpiderCenterOptions:
        """
        Getter for property: (@link LMIELocalSpiderCenterOptions NXOpen.CAE.Connections.LMIELocalSpiderCenterOptions@endlink) LocalSpiderCenterOptions
          the local spider center options   
            
         
        """
        pass
    
    ## Setter for property: (@link LMIELocalSpiderCenterOptions NXOpen.CAE.Connections.LMIELocalSpiderCenterOptions@endlink) LocalSpiderCenterOptions

    ##   the local spider center options   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @LocalSpiderCenterOptions.setter
    def LocalSpiderCenterOptions(self, opt: LMIELocalSpiderCenterOptions):
        """
        Setter for property: (@link LMIELocalSpiderCenterOptions NXOpen.CAE.Connections.LMIELocalSpiderCenterOptions@endlink) LocalSpiderCenterOptions
          the local spider center options   
            
         
        """
        pass
    
    ## Getter for property: (float) MaxSearchDistance
    ##   the mass distribution type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return float
    @property
    def MaxSearchDistance(self) -> float:
        """
        Getter for property: (float) MaxSearchDistance
          the mass distribution type   
            
         
        """
        pass
    
    ## Setter for property: (float) MaxSearchDistance

    ##   the mass distribution type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @MaxSearchDistance.setter
    def MaxSearchDistance(self, val: float):
        """
        Setter for property: (float) MaxSearchDistance
          the mass distribution type   
            
         
        """
        pass
    
    ## Getter for property: (@link LMIEPanelOptions NXOpen.CAE.Connections.LMIEPanelOptions@endlink) PanelOptions
    ##   the panel options   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return LMIEPanelOptions
    @property
    def PanelOptions(self) -> LMIEPanelOptions:
        """
        Getter for property: (@link LMIEPanelOptions NXOpen.CAE.Connections.LMIEPanelOptions@endlink) PanelOptions
          the panel options   
            
         
        """
        pass
    
    ## Setter for property: (@link LMIEPanelOptions NXOpen.CAE.Connections.LMIEPanelOptions@endlink) PanelOptions

    ##   the panel options   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @PanelOptions.setter
    def PanelOptions(self, opt: LMIEPanelOptions):
        """
        Setter for property: (@link LMIEPanelOptions NXOpen.CAE.Connections.LMIEPanelOptions@endlink) PanelOptions
          the panel options   
            
         
        """
        pass
    
    ## Getter for property: (@link LMIERegionSelection NXOpen.CAE.Connections.LMIERegionSelection@endlink) RegionSelection
    ##   the region selection   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return LMIERegionSelection
    @property
    def RegionSelection(self) -> LMIERegionSelection:
        """
        Getter for property: (@link LMIERegionSelection NXOpen.CAE.Connections.LMIERegionSelection@endlink) RegionSelection
          the region selection   
            
         
        """
        pass
    
    ## Setter for property: (@link LMIERegionSelection NXOpen.CAE.Connections.LMIERegionSelection@endlink) RegionSelection

    ##   the region selection   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @RegionSelection.setter
    def RegionSelection(self, opt: LMIERegionSelection):
        """
        Setter for property: (@link LMIERegionSelection NXOpen.CAE.Connections.LMIERegionSelection@endlink) RegionSelection
          the region selection   
            
         
        """
        pass
    
    ## Getter for property: (@link LMIERingOptions NXOpen.CAE.Connections.LMIERingOptions@endlink) RingOptions
    ##   the ring options   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return LMIERingOptions
    @property
    def RingOptions(self) -> LMIERingOptions:
        """
        Getter for property: (@link LMIERingOptions NXOpen.CAE.Connections.LMIERingOptions@endlink) RingOptions
          the ring options   
            
         
        """
        pass
    
    ## Setter for property: (@link LMIERingOptions NXOpen.CAE.Connections.LMIERingOptions@endlink) RingOptions

    ##   the ring options   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @RingOptions.setter
    def RingOptions(self, opt: LMIERingOptions):
        """
        Setter for property: (@link LMIERingOptions NXOpen.CAE.Connections.LMIERingOptions@endlink) RingOptions
          the ring options   
            
         
        """
        pass
    
    ##  Create a standalone local spider center options 
    ##  @return opt (@link LMIELocalSpiderCenterOptions NXOpen.CAE.Connections.LMIELocalSpiderCenterOptions@endlink):  Local Spider Center options .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    def CreateLocalSpiderCenterOptions(obj: LMIELocalSpiders) -> LMIELocalSpiderCenterOptions:
        """
         Create a standalone local spider center options 
         @return opt (@link LMIELocalSpiderCenterOptions NXOpen.CAE.Connections.LMIELocalSpiderCenterOptions@endlink):  Local Spider Center options .
        """
        pass
    
    ##  Create a standalone panel options 
    ##  @return opt (@link LMIEPanelOptions NXOpen.CAE.Connections.LMIEPanelOptions@endlink):  Panel options .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    def CreatePanelOptions(obj: LMIELocalSpiders) -> LMIEPanelOptions:
        """
         Create a standalone panel options 
         @return opt (@link LMIEPanelOptions NXOpen.CAE.Connections.LMIEPanelOptions@endlink):  Panel options .
        """
        pass
    
    ##  Create a standalone region selection 
    ##  @return opt (@link LMIERegionSelection NXOpen.CAE.Connections.LMIERegionSelection@endlink):  Region selection .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    def CreateRegionSelection(obj: LMIELocalSpiders) -> LMIERegionSelection:
        """
         Create a standalone region selection 
         @return opt (@link LMIERegionSelection NXOpen.CAE.Connections.LMIERegionSelection@endlink):  Region selection .
        """
        pass
    
    ##  Create a standalone ring options 
    ##  @return opt (@link LMIERingOptions NXOpen.CAE.Connections.LMIERingOptions@endlink):  Ring options .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    def CreateRingOptions(obj: LMIELocalSpiders) -> LMIERingOptions:
        """
         Create a standalone ring options 
         @return opt (@link LMIERingOptions NXOpen.CAE.Connections.LMIERingOptions@endlink):  Ring options .
        """
        pass
    
##   Mass definition.   <br> No creator  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class LMIEMass(LMIEError): 
    """  Mass definition.  """


    ## Getter for property: (@link MassDistributionType NXOpen.CAE.Connections.MassDistributionType@endlink) MassDistributionType
    ##   the mass distribution type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return MassDistributionType
    @property
    def MassDistributionType(self) -> MassDistributionType:
        """
        Getter for property: (@link MassDistributionType NXOpen.CAE.Connections.MassDistributionType@endlink) MassDistributionType
          the mass distribution type   
            
         
        """
        pass
    
    ## Setter for property: (@link MassDistributionType NXOpen.CAE.Connections.MassDistributionType@endlink) MassDistributionType

    ##   the mass distribution type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @MassDistributionType.setter
    def MassDistributionType(self, type: MassDistributionType):
        """
        Setter for property: (@link MassDistributionType NXOpen.CAE.Connections.MassDistributionType@endlink) MassDistributionType
          the mass distribution type   
            
         
        """
        pass
    
    ## Getter for property: (@link MassType NXOpen.CAE.Connections.MassType@endlink) MassType
    ##   the mass type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return MassType
    @property
    def MassType(self) -> MassType:
        """
        Getter for property: (@link MassType NXOpen.CAE.Connections.MassType@endlink) MassType
          the mass type   
            
         
        """
        pass
    
    ## Setter for property: (@link MassType NXOpen.CAE.Connections.MassType@endlink) MassType

    ##   the mass type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @MassType.setter
    def MassType(self, type: MassType):
        """
        Setter for property: (@link MassType NXOpen.CAE.Connections.MassType@endlink) MassType
          the mass type   
            
         
        """
        pass
    
    ## Getter for property: (float) MassValue
    ##   the mass distribution type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return float
    @property
    def MassValue(self) -> float:
        """
        Getter for property: (float) MassValue
          the mass distribution type   
            
         
        """
        pass
    
    ## Setter for property: (float) MassValue

    ##   the mass distribution type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @MassValue.setter
    def MassValue(self, val: float):
        """
        Setter for property: (float) MassValue
          the mass distribution type   
            
         
        """
        pass
    
import NXOpen
##   LMIEMesh object   <br> No creator  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class LMIEMesh(NXOpen.TaggedObject): 
    """  LMIEMesh object  """
    pass


##   Mass definition.   <br> No creator  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class LMIENearestNodes(LMIEError): 
    """  Mass definition.  """


    ## Getter for property: (float) MaxSearchDistance
    ##   the mass distribution type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return float
    @property
    def MaxSearchDistance(self) -> float:
        """
        Getter for property: (float) MaxSearchDistance
          the mass distribution type   
            
         
        """
        pass
    
    ## Setter for property: (float) MaxSearchDistance

    ##   the mass distribution type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @MaxSearchDistance.setter
    def MaxSearchDistance(self, val: float):
        """
        Setter for property: (float) MaxSearchDistance
          the mass distribution type   
            
         
        """
        pass
    
    ## Getter for property: (@link LMIERegionSelection NXOpen.CAE.Connections.LMIERegionSelection@endlink) RegionSelection
    ##   the region selection   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return LMIERegionSelection
    @property
    def RegionSelection(self) -> LMIERegionSelection:
        """
        Getter for property: (@link LMIERegionSelection NXOpen.CAE.Connections.LMIERegionSelection@endlink) RegionSelection
          the region selection   
            
         
        """
        pass
    
    ## Setter for property: (@link LMIERegionSelection NXOpen.CAE.Connections.LMIERegionSelection@endlink) RegionSelection

    ##   the region selection   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @RegionSelection.setter
    def RegionSelection(self, opt: LMIERegionSelection):
        """
        Setter for property: (@link LMIERegionSelection NXOpen.CAE.Connections.LMIERegionSelection@endlink) RegionSelection
          the region selection   
            
         
        """
        pass
    
    ##  Create a standalone region selection 
    ##  @return opt (@link LMIERegionSelection NXOpen.CAE.Connections.LMIERegionSelection@endlink):  Region selection .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    def CreateRegionSelection(obj: LMIENearestNodes) -> LMIERegionSelection:
        """
         Create a standalone region selection 
         @return opt (@link LMIERegionSelection NXOpen.CAE.Connections.LMIERegionSelection@endlink):  Region selection .
        """
        pass
    
##   Lumped Mass center definition node.   <br> No creator  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class LMIENode(LMIEError): 
    """  Lumped Mass center definition node.  """


    ## Getter for property: (str) Id
    ##   the node id   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return str
    @property
    def Id(self) -> str:
        """
        Getter for property: (str) Id
          the node id   
            
         
        """
        pass
    
    ## Setter for property: (str) Id

    ##   the node id   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @Id.setter
    def Id(self, id: str):
        """
        Setter for property: (str) Id
          the node id   
            
         
        """
        pass
    
##   Mass definition.   <br> No creator  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class LMIEPanelOptions(LMIEError): 
    """  Mass definition.  """


    ## Getter for property: (float) Distance
    ##   the mass distribution type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return float
    @property
    def Distance(self) -> float:
        """
        Getter for property: (float) Distance
          the mass distribution type   
            
         
        """
        pass
    
    ## Setter for property: (float) Distance

    ##   the mass distribution type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @Distance.setter
    def Distance(self, val: float):
        """
        Setter for property: (float) Distance
          the mass distribution type   
            
         
        """
        pass
    
    ## Getter for property: (@link PanelSearchType NXOpen.CAE.Connections.PanelSearchType@endlink) SearchPanelsType
    ##   the Ring Search type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return PanelSearchType
    @property
    def SearchPanelsType(self) -> PanelSearchType:
        """
        Getter for property: (@link PanelSearchType NXOpen.CAE.Connections.PanelSearchType@endlink) SearchPanelsType
          the Ring Search type   
            
         
        """
        pass
    
    ## Setter for property: (@link PanelSearchType NXOpen.CAE.Connections.PanelSearchType@endlink) SearchPanelsType

    ##   the Ring Search type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @SearchPanelsType.setter
    def SearchPanelsType(self, type: PanelSearchType):
        """
        Setter for property: (@link PanelSearchType NXOpen.CAE.Connections.PanelSearchType@endlink) SearchPanelsType
          the Ring Search type   
            
         
        """
        pass
    
##   Lumped Mass PID.   <br> No creator  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class LMIEPid(LMIEError): 
    """  Lumped Mass PID.  """


    ## Getter for property: (int) Label
    ##   the PID label   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return int
    @property
    def Label(self) -> int:
        """
        Getter for property: (int) Label
          the PID label   
            
         
        """
        pass
    
    ## Setter for property: (int) Label

    ##   the PID label   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @Label.setter
    def Label(self, label: int):
        """
        Setter for property: (int) Label
          the PID label   
            
         
        """
        pass
    
import NXOpen
##   Lumped Mass center definition point.   <br> No creator  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class LMIEPoint(LMIEError): 
    """  Lumped Mass center definition point.  """


    ## Getter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) Coordinates
    ##   the point coordinates   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.Point3d
    @property
    def Coordinates(self) -> NXOpen.Point3d:
        """
        Getter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) Coordinates
          the point coordinates   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) Coordinates

    ##   the point coordinates   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @Coordinates.setter
    def Coordinates(self, point: NXOpen.Point3d):
        """
        Setter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) Coordinates
          the point coordinates   
            
         
        """
        pass
    
##   Region selection.   <br> No creator  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class LMIERegionSelection(LMIEError): 
    """  Region selection.  """


    ##  Create a standalone PID 
    ##  @return opt (@link LMIEPid NXOpen.CAE.Connections.LMIEPid@endlink):  The PID .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    def CreatePid(obj: LMIERegionSelection) -> LMIEPid:
        """
         Create a standalone PID 
         @return opt (@link LMIEPid NXOpen.CAE.Connections.LMIEPid@endlink):  The PID .
        """
        pass
    
    ##  Create a standalone Selection Recipe 
    ##  @return opt (@link LMIESelectionRecipe NXOpen.CAE.Connections.LMIESelectionRecipe@endlink):  The PID .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    def CreateSelectionRecipe(obj: LMIERegionSelection) -> LMIESelectionRecipe:
        """
         Create a standalone Selection Recipe 
         @return opt (@link LMIESelectionRecipe NXOpen.CAE.Connections.LMIESelectionRecipe@endlink):  The PID .
        """
        pass
    
    ##  Get the PIDs 
    ##  @return opt (@link LMIEPid List[NXOpen.CAE.Connections.LMIEPid]@endlink):  The PIDs .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetPids(obj: LMIERegionSelection) -> List[LMIEPid]:
        """
         Get the PIDs 
         @return opt (@link LMIEPid List[NXOpen.CAE.Connections.LMIEPid]@endlink):  The PIDs .
        """
        pass
    
    ##  Get the selection recipes 
    ##  @return opt (@link LMIESelectionRecipe List[NXOpen.CAE.Connections.LMIESelectionRecipe]@endlink):  The selection recipes .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetSelectionRecipes(obj: LMIERegionSelection) -> List[LMIESelectionRecipe]:
        """
         Get the selection recipes 
         @return opt (@link LMIESelectionRecipe List[NXOpen.CAE.Connections.LMIESelectionRecipe]@endlink):  The selection recipes .
        """
        pass
    
    ##  Set the PIDs 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ##  The PIDs 
    def SetPids(obj: LMIERegionSelection, opt: List[LMIEPid]) -> None:
        """
         Set the PIDs 
        """
        pass
    
    ##  Set the selection recipes 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ##  The selection recipes 
    def SetSelectionRecipes(obj: LMIERegionSelection, opt: List[LMIESelectionRecipe]) -> None:
        """
         Set the selection recipes 
        """
        pass
    
##   Mass definition.   <br> No creator  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class LMIERingOptions(LMIEError): 
    """  Mass definition.  """


    ## Getter for property: (float) ExpansionRadius
    ##   the mass distribution type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return float
    @property
    def ExpansionRadius(self) -> float:
        """
        Getter for property: (float) ExpansionRadius
          the mass distribution type   
            
         
        """
        pass
    
    ## Setter for property: (float) ExpansionRadius

    ##   the mass distribution type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @ExpansionRadius.setter
    def ExpansionRadius(self, val: float):
        """
        Setter for property: (float) ExpansionRadius
          the mass distribution type   
            
         
        """
        pass
    
    ## Getter for property: (float) ExpansionRadiusFactor
    ##   the mass distribution type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return float
    @property
    def ExpansionRadiusFactor(self) -> float:
        """
        Getter for property: (float) ExpansionRadiusFactor
          the mass distribution type   
            
         
        """
        pass
    
    ## Setter for property: (float) ExpansionRadiusFactor

    ##   the mass distribution type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @ExpansionRadiusFactor.setter
    def ExpansionRadiusFactor(self, val: float):
        """
        Setter for property: (float) ExpansionRadiusFactor
          the mass distribution type   
            
         
        """
        pass
    
    ## Getter for property: (@link RingSearchType NXOpen.CAE.Connections.RingSearchType@endlink) RingType
    ##   the Ring Search type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return RingSearchType
    @property
    def RingType(self) -> RingSearchType:
        """
        Getter for property: (@link RingSearchType NXOpen.CAE.Connections.RingSearchType@endlink) RingType
          the Ring Search type   
            
         
        """
        pass
    
    ## Setter for property: (@link RingSearchType NXOpen.CAE.Connections.RingSearchType@endlink) RingType

    ##   the Ring Search type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @RingType.setter
    def RingType(self, type: RingSearchType):
        """
        Setter for property: (@link RingSearchType NXOpen.CAE.Connections.RingSearchType@endlink) RingType
          the Ring Search type   
            
         
        """
        pass
    
##   Lumped Mass center definition selection recipe.   <br> No creator  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class LMIESelectionRecipe(LMIEError): 
    """  Lumped Mass center definition selection recipe.  """


    ## Getter for property: (str) RecipeName
    ##   the selection recipe   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return str
    @property
    def RecipeName(self) -> str:
        """
        Getter for property: (str) RecipeName
          the selection recipe   
            
         
        """
        pass
    
    ## Setter for property: (str) RecipeName

    ##   the selection recipe   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @RecipeName.setter
    def RecipeName(self, name: str):
        """
        Setter for property: (str) RecipeName
          the selection recipe   
            
         
        """
        pass
    
##   Seam Weld connection. Use this interface to set/get properties and parameters of the spot weld connection.   <br> No creator  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class LMIEUnitSystem(LMIEError): 
    """  Seam Weld connection. Use this interface to set/get properties and parameters of the spot weld connection.  """


    ## Getter for property: (str) LengthUnit
    ##   the length unit   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return str
    @property
    def LengthUnit(self) -> str:
        """
        Getter for property: (str) LengthUnit
          the length unit   
            
         
        """
        pass
    
    ## Setter for property: (str) LengthUnit

    ##   the length unit   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @LengthUnit.setter
    def LengthUnit(self, unit: str):
        """
        Setter for property: (str) LengthUnit
          the length unit   
            
         
        """
        pass
    
    ## Getter for property: (str) MassUnit
    ##   the mass unit   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return str
    @property
    def MassUnit(self) -> str:
        """
        Getter for property: (str) MassUnit
          the mass unit   
            
         
        """
        pass
    
    ## Setter for property: (str) MassUnit

    ##   the mass unit   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @MassUnit.setter
    def MassUnit(self, unit: str):
        """
        Setter for property: (str) MassUnit
          the mass unit   
            
         
        """
        pass
    
##  Local Spider Center Types 
##  Local spider center is computed as the mean of its legs 
class LocalSpiderCenterType(Enum):
    """
    Members Include: <MeanOfSpiderLegs> <InputLegDefinition>
    """
    MeanOfSpiderLegs: int
    InputLegDefinition: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> LocalSpiderCenterType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


##  Location and Direction type 
##  Two Points/Nodes 
class LocationDirectionType(Enum):
    """
    Members Include: <Point> <Vector> <Curve> <SelectionRecipes>
    """
    Point: int
    Vector: int
    Curve: int
    SelectionRecipes: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> LocationDirectionType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


##  Location type 
##  Coordinates 
class LocationType(Enum):
    """
    Members Include: <Coordinates> <Point> <Node> <SeriesOfNodes> <SeriesOfCoordinates> <Curve> <FeEdgeGroup> <SeriesOfPoints> <LocationWithDirection> <SelectionRecipe> <MeshPoint> <Group>
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
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> LocationType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


import NXOpen
import NXOpen.CAE
##   @brief  Location With Direction interface. This defines connection locations with direction.  
## 
##    <br> To obtain an instance of this object use the AddLocationWithDirection creators on the Connections  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class LocationWithDir(Location): 
    """ <summary> Location With Direction interface. This defines connection locations with direction. </summary> """


    ## Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) DirectionPoint
    ##   the point of the direction definition end point.  
    ##     
    ##  
    ## Getter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Point
    @property
    def DirectionPoint(self) -> NXOpen.Point:
        """
        Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) DirectionPoint
          the point of the direction definition end point.  
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) DirectionPoint

    ##   the point of the direction definition end point.  
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @DirectionPoint.setter
    def DirectionPoint(self, direction: NXOpen.Point):
        """
        Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) DirectionPoint
          the point of the direction definition end point.  
            
         
        """
        pass
    
    ## Getter for property: (@link LocationDirectionType NXOpen.CAE.Connections.LocationDirectionType@endlink) DirectionType
    ##   the direction type   
    ##     
    ##  
    ## Getter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return LocationDirectionType
    @property
    def DirectionType(self) -> LocationDirectionType:
        """
        Getter for property: (@link LocationDirectionType NXOpen.CAE.Connections.LocationDirectionType@endlink) DirectionType
          the direction type   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Vector3d NXOpen.Vector3d@endlink) DirectionValue
    ##   the direction value  
    ##     
    ##  
    ## Getter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Vector3d
    @property
    def DirectionValue(self) -> NXOpen.Vector3d:
        """
        Getter for property: (@link NXOpen.Vector3d NXOpen.Vector3d@endlink) DirectionValue
          the direction value  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) DirectionVector
    ##   the direction definition vector   
    ##     
    ##  
    ## Getter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Direction
    @property
    def DirectionVector(self) -> NXOpen.Direction:
        """
        Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) DirectionVector
          the direction definition vector   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) DirectionVector

    ##   the direction definition vector   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @DirectionVector.setter
    def DirectionVector(self, direction: NXOpen.Direction):
        """
        Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) DirectionVector
          the direction definition vector   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.CAE.SelectionRecipe NXOpen.CAE.SelectionRecipe@endlink) EndSelectionRecipe
    ##   the end selection recipe  
    ##     
    ##  
    ## Getter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.CAE.SelectionRecipe
    @property
    def EndSelectionRecipe(self) -> NXOpen.CAE.SelectionRecipe:
        """
        Getter for property: (@link NXOpen.CAE.SelectionRecipe NXOpen.CAE.SelectionRecipe@endlink) EndSelectionRecipe
          the end selection recipe  
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.CAE.SelectionRecipe NXOpen.CAE.SelectionRecipe@endlink) EndSelectionRecipe

    ##   the end selection recipe  
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @EndSelectionRecipe.setter
    def EndSelectionRecipe(self, selectionRecipe: NXOpen.CAE.SelectionRecipe):
        """
        Setter for property: (@link NXOpen.CAE.SelectionRecipe NXOpen.CAE.SelectionRecipe@endlink) EndSelectionRecipe
          the end selection recipe  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) Point
    ##   the point of the direction definition start point.  
    ##     
    ##  
    ## Getter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Point
    @property
    def Point(self) -> NXOpen.Point:
        """
        Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) Point
          the point of the direction definition start point.  
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) Point

    ##   the point of the direction definition start point.  
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @Point.setter
    def Point(self, point: NXOpen.Point):
        """
        Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) Point
          the point of the direction definition start point.  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.CAE.SelectionRecipe NXOpen.CAE.SelectionRecipe@endlink) StartSelectionRecipe
    ##   the start selection recipe  
    ##     
    ##  
    ## Getter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.CAE.SelectionRecipe
    @property
    def StartSelectionRecipe(self) -> NXOpen.CAE.SelectionRecipe:
        """
        Getter for property: (@link NXOpen.CAE.SelectionRecipe NXOpen.CAE.SelectionRecipe@endlink) StartSelectionRecipe
          the start selection recipe  
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.CAE.SelectionRecipe NXOpen.CAE.SelectionRecipe@endlink) StartSelectionRecipe

    ##   the start selection recipe  
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @StartSelectionRecipe.setter
    def StartSelectionRecipe(self, selectionRecipe: NXOpen.CAE.SelectionRecipe):
        """
        Setter for property: (@link NXOpen.CAE.SelectionRecipe NXOpen.CAE.SelectionRecipe@endlink) StartSelectionRecipe
          the start selection recipe  
            
         
        """
        pass
    
import NXOpen
##   @brief  Location base class. This defines connection locations with common properties like coordinates.  
## 
##    <br> This is an abstract class and cannot be instantiated  <br> 
## 
##   <br>  Created in NX11.0.0  <br> 

class Location(NXOpen.TaggedObject): 
    """ <summary> Location base class. This defines connection locations with common properties like coordinates. </summary> """


    ##  Gets location details. 
    ##  @return details (str):  Location details .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetDetails(location: Location) -> str:
        """
         Gets location details. 
         @return details (str):  Location details .
        """
        pass
    
    ##  Gets location info. 
    ##  @return info (str):  Location details .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetInfo(location: Location) -> str:
        """
         Gets location info. 
         @return info (str):  Location details .
        """
        pass
    
    ##  Gets the coordinates from the specified location.
    ##                 The location can be any type: coordinates, node or point.
    ##                 Its coordinates will be returned. 
    ##  @return coordinates (@link NXOpen.Point3d List[NXOpen.Point3d]@endlink):  Location coordinates .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetXyzCoordinates(location: Location) -> List[NXOpen.Point3d]:
        """
         Gets the coordinates from the specified location.
                        The location can be any type: coordinates, node or point.
                        Its coordinates will be returned. 
         @return coordinates (@link NXOpen.Point3d List[NXOpen.Point3d]@endlink):  Location coordinates .
        """
        pass
    
import NXOpen
##  Lumped Mass. Use this interface to set/get properties and parameters of the lumped mass.  
## 
##   <br>  Created in NX1847.0.0  <br> 

class LumpedMass(IConnection): 
    """ Lumped Mass. Use this interface to set/get properties and parameters of the lumped mass.  """


    ## Getter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) Center
    ##   the target center   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.TaggedObject
    @property
    def Center(self) -> NXOpen.TaggedObject:
        """
        Getter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) Center
          the target center   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) Center

    ##   the target center   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @Center.setter
    def Center(self, center: NXOpen.TaggedObject):
        """
        Setter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) Center
          the target center   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) Csys
    ##   the csys   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.CoordinateSystem
    @property
    def Csys(self) -> NXOpen.CoordinateSystem:
        """
        Getter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) Csys
          the csys   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) Csys

    ##   the csys   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @Csys.setter
    def Csys(self, csys: NXOpen.CoordinateSystem):
        """
        Setter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) Csys
          the csys   
            
         
        """
        pass
    
    ## Getter for property: (@link CsysType NXOpen.CAE.Connections.CsysType@endlink) CsysType
    ##   the csys type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return CsysType
    @property
    def CsysType(self) -> CsysType:
        """
        Getter for property: (@link CsysType NXOpen.CAE.Connections.CsysType@endlink) CsysType
          the csys type   
            
         
        """
        pass
    
    ## Setter for property: (@link CsysType NXOpen.CAE.Connections.CsysType@endlink) CsysType

    ##   the csys type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @CsysType.setter
    def CsysType(self, csysType: CsysType):
        """
        Setter for property: (@link CsysType NXOpen.CAE.Connections.CsysType@endlink) CsysType
          the csys type   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ExpansionRadiusFactorTolerance
    ##   the expansion radius factor   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def ExpansionRadiusFactorTolerance(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ExpansionRadiusFactorTolerance
          the expansion radius factor   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ExpansionRadiusTolerance
    ##   the expansion radius   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def ExpansionRadiusTolerance(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ExpansionRadiusTolerance
          the expansion radius   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) InertiaXX
    ##   the inertia XX.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def InertiaXX(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) InertiaXX
          the inertia XX.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) InertiaYX
    ##   the inertia XY.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def InertiaYX(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) InertiaYX
          the inertia XY.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) InertiaYY
    ##   the inertia YY.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def InertiaYY(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) InertiaYY
          the inertia YY.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) InertiaZX
    ##   the inertia XZ.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def InertiaZX(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) InertiaZX
          the inertia XZ.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) InertiaZY
    ##   the inertia YZ.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def InertiaZY(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) InertiaZY
          the inertia YZ.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) InertiaZZ
    ##   the inertia ZZ.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def InertiaZZ(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) InertiaZZ
          the inertia ZZ.  
             
         
        """
        pass
    
    ## Getter for property: (@link LocalSpiderCenterType NXOpen.CAE.Connections.LocalSpiderCenterType@endlink) LocalSpiderCenterType
    ##   the local spider center type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return LocalSpiderCenterType
    @property
    def LocalSpiderCenterType(self) -> LocalSpiderCenterType:
        """
        Getter for property: (@link LocalSpiderCenterType NXOpen.CAE.Connections.LocalSpiderCenterType@endlink) LocalSpiderCenterType
          the local spider center type   
            
         
        """
        pass
    
    ## Setter for property: (@link LocalSpiderCenterType NXOpen.CAE.Connections.LocalSpiderCenterType@endlink) LocalSpiderCenterType

    ##   the local spider center type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @LocalSpiderCenterType.setter
    def LocalSpiderCenterType(self, localSpiderCenterType: LocalSpiderCenterType):
        """
        Setter for property: (@link LocalSpiderCenterType NXOpen.CAE.Connections.LocalSpiderCenterType@endlink) LocalSpiderCenterType
          the local spider center type   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Mass
    ##   the mass value   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Mass(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Mass
          the mass value   
            
         
        """
        pass
    
    ## Getter for property: (@link MassCenterType NXOpen.CAE.Connections.MassCenterType@endlink) MassCenterType
    ##   the mass center type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return MassCenterType
    @property
    def MassCenterType(self) -> MassCenterType:
        """
        Getter for property: (@link MassCenterType NXOpen.CAE.Connections.MassCenterType@endlink) MassCenterType
          the mass center type   
            
         
        """
        pass
    
    ## Setter for property: (@link MassCenterType NXOpen.CAE.Connections.MassCenterType@endlink) MassCenterType

    ##   the mass center type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @MassCenterType.setter
    def MassCenterType(self, massCenterType: MassCenterType):
        """
        Setter for property: (@link MassCenterType NXOpen.CAE.Connections.MassCenterType@endlink) MassCenterType
          the mass center type   
            
         
        """
        pass
    
    ## Getter for property: (@link MassConnectivityType NXOpen.CAE.Connections.MassConnectivityType@endlink) MassConnectivityType
    ##   the mass connection type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return MassConnectivityType
    @property
    def MassConnectivityType(self) -> MassConnectivityType:
        """
        Getter for property: (@link MassConnectivityType NXOpen.CAE.Connections.MassConnectivityType@endlink) MassConnectivityType
          the mass connection type   
            
         
        """
        pass
    
    ## Setter for property: (@link MassConnectivityType NXOpen.CAE.Connections.MassConnectivityType@endlink) MassConnectivityType

    ##   the mass connection type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @MassConnectivityType.setter
    def MassConnectivityType(self, type: MassConnectivityType):
        """
        Setter for property: (@link MassConnectivityType NXOpen.CAE.Connections.MassConnectivityType@endlink) MassConnectivityType
          the mass connection type   
            
         
        """
        pass
    
    ## Getter for property: (@link MassDistributionType NXOpen.CAE.Connections.MassDistributionType@endlink) MassDistributionType
    ##   the mass distribution type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return MassDistributionType
    @property
    def MassDistributionType(self) -> MassDistributionType:
        """
        Getter for property: (@link MassDistributionType NXOpen.CAE.Connections.MassDistributionType@endlink) MassDistributionType
          the mass distribution type   
            
         
        """
        pass
    
    ## Setter for property: (@link MassDistributionType NXOpen.CAE.Connections.MassDistributionType@endlink) MassDistributionType

    ##   the mass distribution type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @MassDistributionType.setter
    def MassDistributionType(self, type: MassDistributionType):
        """
        Setter for property: (@link MassDistributionType NXOpen.CAE.Connections.MassDistributionType@endlink) MassDistributionType
          the mass distribution type   
            
         
        """
        pass
    
    ## Getter for property: (@link MassType NXOpen.CAE.Connections.MassType@endlink) MassTypeValue
    ##   the mass type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return MassType
    @property
    def MassTypeValue(self) -> MassType:
        """
        Getter for property: (@link MassType NXOpen.CAE.Connections.MassType@endlink) MassTypeValue
          the mass type   
            
         
        """
        pass
    
    ## Setter for property: (@link MassType NXOpen.CAE.Connections.MassType@endlink) MassTypeValue

    ##   the mass type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @MassTypeValue.setter
    def MassTypeValue(self, type: MassType):
        """
        Setter for property: (@link MassType NXOpen.CAE.Connections.MassType@endlink) MassTypeValue
          the mass type   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxDistanceTolerance
    ##   the maximum distance from definition point to center of support element   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def MaxDistanceTolerance(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxDistanceTolerance
          the maximum distance from definition point to center of support element   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) PanelSearchDistance
    ##   the panel search distance   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def PanelSearchDistance(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) PanelSearchDistance
          the panel search distance   
            
         
        """
        pass
    
    ## Getter for property: (@link PanelSearchType NXOpen.CAE.Connections.PanelSearchType@endlink) PanelSearchType
    ##   the panel search type  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return PanelSearchType
    @property
    def PanelSearchType(self) -> PanelSearchType:
        """
        Getter for property: (@link PanelSearchType NXOpen.CAE.Connections.PanelSearchType@endlink) PanelSearchType
          the panel search type  
            
         
        """
        pass
    
    ## Setter for property: (@link PanelSearchType NXOpen.CAE.Connections.PanelSearchType@endlink) PanelSearchType

    ##   the panel search type  
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @PanelSearchType.setter
    def PanelSearchType(self, type: PanelSearchType):
        """
        Setter for property: (@link PanelSearchType NXOpen.CAE.Connections.PanelSearchType@endlink) PanelSearchType
          the panel search type  
            
         
        """
        pass
    
    ## Getter for property: (@link RingSearchType NXOpen.CAE.Connections.RingSearchType@endlink) RingSearchType
    ##   the search tolerance type  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return RingSearchType
    @property
    def RingSearchType(self) -> RingSearchType:
        """
        Getter for property: (@link RingSearchType NXOpen.CAE.Connections.RingSearchType@endlink) RingSearchType
          the search tolerance type  
            
         
        """
        pass
    
    ## Setter for property: (@link RingSearchType NXOpen.CAE.Connections.RingSearchType@endlink) RingSearchType

    ##   the search tolerance type  
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @RingSearchType.setter
    def RingSearchType(self, type: RingSearchType):
        """
        Setter for property: (@link RingSearchType NXOpen.CAE.Connections.RingSearchType@endlink) RingSearchType
          the search tolerance type  
            
         
        """
        pass
    
##  Lumped Mass Center Types 
##  CoG is picked by selection 
class MassCenterType(Enum):
    """
    Members Include: <Manual> <FromDefinedSpiderLegs> <FromComputedSpiderLegs>
    """
    Manual: int
    FromDefinedSpiderLegs: int
    FromComputedSpiderLegs: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> MassCenterType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


##  Lumped Mass connectivity type 
##  nearest nodes on defined panels 
class MassConnectivityType(Enum):
    """
    Members Include: <NearestNodes> <LocalSpiders>
    """
    NearestNodes: int
    LocalSpiders: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> MassConnectivityType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


##  Lumped Mass distribution type 
##  Mass is distributed on selected nodes 
class MassDistributionType(Enum):
    """
    Members Include: <Distributed> <Repeated>
    """
    Distributed: int
    Repeated: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> MassDistributionType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


##  Lumped Mass type 
##  Mass applied on selected nodes 
class MassType(Enum):
    """
    Members Include: <OnNodes> <WithSpiders>
    """
    OnNodes: int
    WithSpiders: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> MassType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


##  Material definition types 
##  User defined material 
class MaterialType(Enum):
    """
    Members Include: <User> <FromSupport> <NotSet>
    """
    User: int
    FromSupport: int
    NotSet: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> MaterialType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


import NXOpen.CAE
##   @brief  This defines Mesh Point Location used by Universal Connections.  
## 
##    <br> To obtain an instance of this object use the AddLocation creators  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class MeshPointLocation(Location): 
    """ <summary> This defines Mesh Point Location used by Universal Connections. </summary> """


    ## Getter for property: (@link NXOpen.CAE.MeshPoint NXOpen.CAE.MeshPoint@endlink) MeshPoint
    ##   the Mesh Point used for creating the location.  
    ##   
    ##                 If the location type is not mesh point, this method will raise an error.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.CAE.MeshPoint
    @property
    def MeshPoint(self) -> NXOpen.CAE.MeshPoint:
        """
        Getter for property: (@link NXOpen.CAE.MeshPoint NXOpen.CAE.MeshPoint@endlink) MeshPoint
          the Mesh Point used for creating the location.  
          
                        If the location type is not mesh point, this method will raise an error.   
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.CAE.MeshPoint NXOpen.CAE.MeshPoint@endlink) MeshPoint

    ##   the Mesh Point used for creating the location.  
    ##   
    ##                 If the location type is not mesh point, this method will raise an error.   
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @MeshPoint.setter
    def MeshPoint(self, point: NXOpen.CAE.MeshPoint):
        """
        Setter for property: (@link NXOpen.CAE.MeshPoint NXOpen.CAE.MeshPoint@endlink) MeshPoint
          the Mesh Point used for creating the location.  
          
                        If the location type is not mesh point, this method will raise an error.   
         
        """
        pass
    
##  Modelization PPTRefTargetType 
##  None 
class ModelizationPPTRefTargetType(Enum):
    """
    Members Include: <NotSet> <Ec> <Ecc> <Ead>
    """
    NotSet: int
    Ec: int
    Ecc: int
    Ead: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> ModelizationPPTRefTargetType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


##  Modelization result type 
##  None 
class ModelizationResultType(Enum):
    """
    Members Include: <NotSet> <Material> <Weights> <Section> <Csys> <Stiffness> <ViscousDamping> <StructuralDamping> <Dofs> <DynamicStiffness> <DynamicViscousDamping> <DynamicStructuralDamping> <Friction> <Contact> <Mass> <NonlinearStiffness> <NonlinearDamping> <Thickness>
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
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> ModelizationResultType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


##  Nodal pairing method 
##  Proximity 
class NodalPairingMethod(Enum):
    """
    Members Include: <Proximity> <OrientatedSearch> <SelectionOrder>
    """
    Proximity: int
    OrientatedSearch: int
    SelectionOrder: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> NodalPairingMethod:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


##  Nodal Target Center Types 
##  CoG is picked by selection 
class NodalTargetCenterType(Enum):
    """
    Members Include: <Manual> <FromComputedSpiderLegs> <Coincident> <FromDefinedSpiderLegs>
    """
    Manual: int
    FromComputedSpiderLegs: int
    Coincident: int
    FromDefinedSpiderLegs: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> NodalTargetCenterType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


import NXOpen
##   @brief  This is the Local Spider Nodal Target.  
## 
##   
## 
##   <br>  Created in NX1847.0.0  <br> 

class NodalTargetLocalSpider(NodalTarget): 
    """ <summary> This is the Local Spider Nodal Target. </summary> """


    ## Getter for property: (@link NodalTargetCenterType NXOpen.CAE.Connections.NodalTargetCenterType@endlink) CenterType
    ##   the target center type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return NodalTargetCenterType
    @property
    def CenterType(self) -> NodalTargetCenterType:
        """
        Getter for property: (@link NodalTargetCenterType NXOpen.CAE.Connections.NodalTargetCenterType@endlink) CenterType
          the target center type   
            
         
        """
        pass
    
    ## Setter for property: (@link NodalTargetCenterType NXOpen.CAE.Connections.NodalTargetCenterType@endlink) CenterType

    ##   the target center type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @CenterType.setter
    def CenterType(self, centerType: NodalTargetCenterType):
        """
        Setter for property: (@link NodalTargetCenterType NXOpen.CAE.Connections.NodalTargetCenterType@endlink) CenterType
          the target center type   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ExpansionRadius
    ##   the Expansion Radius   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def ExpansionRadius(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ExpansionRadius
          the Expansion Radius   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ExpansionRadiusFactor
    ##   the Expansion Radius Factor   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def ExpansionRadiusFactor(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ExpansionRadiusFactor
          the Expansion Radius Factor   
            
         
        """
        pass
    
    ## Getter for property: (@link LocalSpiderCenterType NXOpen.CAE.Connections.LocalSpiderCenterType@endlink) LocalSpiderCenterType
    ##   the Local Spider Center type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return LocalSpiderCenterType
    @property
    def LocalSpiderCenterType(self) -> LocalSpiderCenterType:
        """
        Getter for property: (@link LocalSpiderCenterType NXOpen.CAE.Connections.LocalSpiderCenterType@endlink) LocalSpiderCenterType
          the Local Spider Center type   
            
         
        """
        pass
    
    ## Setter for property: (@link LocalSpiderCenterType NXOpen.CAE.Connections.LocalSpiderCenterType@endlink) LocalSpiderCenterType

    ##   the Local Spider Center type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @LocalSpiderCenterType.setter
    def LocalSpiderCenterType(self, localSpiderCenterType: LocalSpiderCenterType):
        """
        Setter for property: (@link LocalSpiderCenterType NXOpen.CAE.Connections.LocalSpiderCenterType@endlink) LocalSpiderCenterType
          the Local Spider Center type   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxDistance
    ##   the Maximum Distance   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def MaxDistance(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxDistance
          the Maximum Distance   
            
         
        """
        pass
    
    ## Getter for property: (@link PanelSearchType NXOpen.CAE.Connections.PanelSearchType@endlink) PanelSearchType
    ##   the Panel Search type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return PanelSearchType
    @property
    def PanelSearchType(self) -> PanelSearchType:
        """
        Getter for property: (@link PanelSearchType NXOpen.CAE.Connections.PanelSearchType@endlink) PanelSearchType
          the Panel Search type   
            
         
        """
        pass
    
    ## Setter for property: (@link PanelSearchType NXOpen.CAE.Connections.PanelSearchType@endlink) PanelSearchType

    ##   the Panel Search type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @PanelSearchType.setter
    def PanelSearchType(self, panelSearchType: PanelSearchType):
        """
        Setter for property: (@link PanelSearchType NXOpen.CAE.Connections.PanelSearchType@endlink) PanelSearchType
          the Panel Search type   
            
         
        """
        pass
    
    ## Getter for property: (@link RingSearchType NXOpen.CAE.Connections.RingSearchType@endlink) RingSearchType
    ##   the Ring Search type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return RingSearchType
    @property
    def RingSearchType(self) -> RingSearchType:
        """
        Getter for property: (@link RingSearchType NXOpen.CAE.Connections.RingSearchType@endlink) RingSearchType
          the Ring Search type   
            
         
        """
        pass
    
    ## Setter for property: (@link RingSearchType NXOpen.CAE.Connections.RingSearchType@endlink) RingSearchType

    ##   the Ring Search type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @RingSearchType.setter
    def RingSearchType(self, ringSearchType: RingSearchType):
        """
        Setter for property: (@link RingSearchType NXOpen.CAE.Connections.RingSearchType@endlink) RingSearchType
          the Ring Search type   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) SearchTolerance
    ##   the Search Tolerance   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def SearchTolerance(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) SearchTolerance
          the Search Tolerance   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) TargetCenter
    ##   the target center   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.TaggedObject
    @property
    def TargetCenter(self) -> NXOpen.TaggedObject:
        """
        Getter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) TargetCenter
          the target center   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) TargetCenter

    ##   the target center   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @TargetCenter.setter
    def TargetCenter(self, center: NXOpen.TaggedObject):
        """
        Setter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) TargetCenter
          the target center   
            
         
        """
        pass
    
##   @brief  Set of Points Target. Use this interface to set/get parameters of the Set of Points Target type.  
## 
##   
## 
##   <br>  Created in NX12.0.0  <br> 

class NodalTargetSetOfPoints(NodalTarget): 
    """ <summary> Set of Points Target. Use this interface to set/get parameters of the Set of Points Target type. </summary> """
    pass


import NXOpen
##   @brief  Group of Points Target. Use this interface to set/get parameters of the Group of Points Target type.  
## 
##   
## 
##   <br>  Created in NX12.0.0  <br> 

class NodalTargetSinglePoint(NodalTarget): 
    """ <summary> Group of Points Target. Use this interface to set/get parameters of the Group of Points Target type. </summary> """


    ## Getter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) TargetCenter
    ##   the target center   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.TaggedObject
    @property
    def TargetCenter(self) -> NXOpen.TaggedObject:
        """
        Getter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) TargetCenter
          the target center   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) TargetCenter

    ##   the target center   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @TargetCenter.setter
    def TargetCenter(self, center: NXOpen.TaggedObject):
        """
        Setter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) TargetCenter
          the target center   
            
         
        """
        pass
    
import NXOpen
##   @brief  Group of Points Target. Use this interface to set/get parameters of the Group of Points Target type.  
## 
##   
## 
##   <br>  Created in NX12.0.0  <br> 

class NodalTargetSpider(NodalTarget): 
    """ <summary> Group of Points Target. Use this interface to set/get parameters of the Group of Points Target type. </summary> """


    ## Getter for property: (@link NodalTargetCenterType NXOpen.CAE.Connections.NodalTargetCenterType@endlink) CenterType
    ##   the target center type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return NodalTargetCenterType
    @property
    def CenterType(self) -> NodalTargetCenterType:
        """
        Getter for property: (@link NodalTargetCenterType NXOpen.CAE.Connections.NodalTargetCenterType@endlink) CenterType
          the target center type   
            
         
        """
        pass
    
    ## Setter for property: (@link NodalTargetCenterType NXOpen.CAE.Connections.NodalTargetCenterType@endlink) CenterType

    ##   the target center type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @CenterType.setter
    def CenterType(self, centerType: NodalTargetCenterType):
        """
        Setter for property: (@link NodalTargetCenterType NXOpen.CAE.Connections.NodalTargetCenterType@endlink) CenterType
          the target center type   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) TargetCenter
    ##   the target center   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.TaggedObject
    @property
    def TargetCenter(self) -> NXOpen.TaggedObject:
        """
        Getter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) TargetCenter
          the target center   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) TargetCenter

    ##   the target center   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @TargetCenter.setter
    def TargetCenter(self, center: NXOpen.TaggedObject):
        """
        Setter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) TargetCenter
          the target center   
            
         
        """
        pass
    
##  Nodal Target types 
##  Single Point 
class NodalTargetType(Enum):
    """
    Members Include: <SinglePoint> <SetOfPoints> <Spider> <NotSet> <LocalSpider>
    """
    SinglePoint: int
    SetOfPoints: int
    Spider: int
    NotSet: int
    LocalSpider: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> NodalTargetType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


import NXOpen
##   @brief  This class represents an Interface to the Connection Target.  
## 
##    <br> This is an abstract class, and cannot be created.  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class NodalTarget(NXOpen.NXObject): 
    """ <summary> This class represents an Interface to the Connection Target. </summary> """


    ## Getter for property: (@link NodalTargetType NXOpen.CAE.Connections.NodalTargetType@endlink) TargetType
    ##   the target type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NodalTargetType
    @property
    def TargetType(self) -> NodalTargetType:
        """
        Getter for property: (@link NodalTargetType NXOpen.CAE.Connections.NodalTargetType@endlink) TargetType
          the target type   
            
         
        """
        pass
    
import NXOpen.CAE
##   @brief  Location interface. This defines connection locations with common properties like coordinates.  
## 
##    <br> To obtain an instance of this object use the AddLocation creators on the Connections  <br> 
## 
##   <br>  Created in NX11.0.0  <br> 

class NodeLocation(Location): 
    """ <summary> Location interface. This defines connection locations with common properties like coordinates. </summary> """


    ## Getter for property: (@link NXOpen.CAE.FENode NXOpen.CAE.FENode@endlink) Node
    ##   the FEM node used for creating the location.  
    ##   
    ##                 If the location type is not node, this method will raise an error.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return NXOpen.CAE.FENode
    @property
    def Node(self) -> NXOpen.CAE.FENode:
        """
        Getter for property: (@link NXOpen.CAE.FENode NXOpen.CAE.FENode@endlink) Node
          the FEM node used for creating the location.  
          
                        If the location type is not node, this method will raise an error.   
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.CAE.FENode NXOpen.CAE.FENode@endlink) Node

    ##   the FEM node used for creating the location.  
    ##   
    ##                 If the location type is not node, this method will raise an error.   
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @Node.setter
    def Node(self, node: NXOpen.CAE.FENode):
        """
        Setter for property: (@link NXOpen.CAE.FENode NXOpen.CAE.FENode@endlink) Node
          the FEM node used for creating the location.  
          
                        If the location type is not node, this method will raise an error.   
         
        """
        pass
    
import NXOpen.CAE
##   @brief  Location interface. This defines connection locations with common properties like coordinates.  
## 
##    <br> To obtain an instance of this object use the AddLocation creators on the Connections  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class NodeSeriesLocation(Location): 
    """ <summary> Location interface. This defines connection locations with common properties like coordinates. </summary> """


    ##  Add location nodes. 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##  Node used for location 
    def AddNodes(location: NodeSeriesLocation, nodes: List[NXOpen.CAE.FENode]) -> None:
        """
         Add location nodes. 
        """
        pass
    
    ##  Retrieve location nodes. 
    ##  @return nodes (@link NXOpen.CAE.FENode List[NXOpen.CAE.FENode]@endlink):  Node used for location .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetNodes(location: NodeSeriesLocation) -> List[NXOpen.CAE.FENode]:
        """
         Retrieve location nodes. 
         @return nodes (@link NXOpen.CAE.FENode List[NXOpen.CAE.FENode]@endlink):  Node used for location .
        """
        pass
    
    ##  Set location nodes. 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##  Node used for location 
    def SetNodes(location: NodeSeriesLocation, nodes: List[NXOpen.CAE.FENode]) -> None:
        """
         Set location nodes. 
        """
        pass
    
##  Nut diameter definition types 
##  User defined diameter 
class NutDiameterType(Enum):
    """
    Members Include: <User> <FactorOfDiameter>
    """
    User: int
    FactorOfDiameter: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> NutDiameterType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


##  panels search type 
##  Apply on the closest panel 
class PanelSearchType(Enum):
    """
    Members Include: <NearestSelectedPanel> <AllSelectedPanels>
    """
    NearestSelectedPanel: int
    AllSelectedPanels: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> PanelSearchType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


import NXOpen
##   @brief  Location interface. This defines connection locations with common properties like coordinates.  
## 
##    <br> To obtain an instance of this object use the AddLocation creators on the Connections  <br> 
## 
##   <br>  Created in NX11.0.0  <br> 

class PointLocation(Location): 
    """ <summary> Location interface. This defines connection locations with common properties like coordinates. </summary> """


    ## Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) Point
    ##   the POINT used for creating the location.  
    ##   
    ##                 If the location type is not point, this method will raise an error.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return NXOpen.Point
    @property
    def Point(self) -> NXOpen.Point:
        """
        Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) Point
          the POINT used for creating the location.  
          
                        If the location type is not point, this method will raise an error.   
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) Point

    ##   the POINT used for creating the location.  
    ##   
    ##                 If the location type is not point, this method will raise an error.   
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @Point.setter
    def Point(self, point: NXOpen.Point):
        """
        Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) Point
          the POINT used for creating the location.  
          
                        If the location type is not point, this method will raise an error.   
         
        """
        pass
    
import NXOpen
##   @brief  Location interface. This defines connection locations with common properties like coordinates.  
## 
##    <br> To obtain an instance of this object use the AddLocation creators on the Connections  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class PointSeriesLocation(Location): 
    """ <summary> Location interface. This defines connection locations with common properties like coordinates. </summary> """


    ##  Add location nodes. 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##  Points used for location 
    def AddPoints(location: PointSeriesLocation, points: List[NXOpen.Point]) -> None:
        """
         Add location nodes. 
        """
        pass
    
    ##  Retrieve location points. 
    ##  @return points (@link NXOpen.Point List[NXOpen.Point]@endlink):  Points used for location .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetPoints(location: PointSeriesLocation) -> List[NXOpen.Point]:
        """
         Retrieve location points. 
         @return points (@link NXOpen.Point List[NXOpen.Point]@endlink):  Points used for location .
        """
        pass
    
    ##  Set location points. 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##  Points used for location 
    def SetPoints(location: PointSeriesLocation, points: List[NXOpen.Point]) -> None:
        """
         Set location points. 
        """
        pass
    
import NXOpen
##  Rigid connection. Use this interface to set/get properties and parameters of the Rigid connection.  
## 
##   <br>  Created in NX12.0.0  <br> 

class Rigid(IConnection): 
    """ Rigid connection. Use this interface to set/get properties and parameters of the Rigid connection.  """


    ## Getter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) Csys
    ##   the csys   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.CoordinateSystem
    @property
    def Csys(self) -> NXOpen.CoordinateSystem:
        """
        Getter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) Csys
          the csys   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) Csys

    ##   the csys   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @Csys.setter
    def Csys(self, csys: NXOpen.CoordinateSystem):
        """
        Setter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) Csys
          the csys   
            
         
        """
        pass
    
    ## Getter for property: (@link CsysType NXOpen.CAE.Connections.CsysType@endlink) CsysType
    ##   the csys type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return CsysType
    @property
    def CsysType(self) -> CsysType:
        """
        Getter for property: (@link CsysType NXOpen.CAE.Connections.CsysType@endlink) CsysType
          the csys type   
            
         
        """
        pass
    
    ## Setter for property: (@link CsysType NXOpen.CAE.Connections.CsysType@endlink) CsysType

    ##   the csys type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @CsysType.setter
    def CsysType(self, csysType: CsysType):
        """
        Setter for property: (@link CsysType NXOpen.CAE.Connections.CsysType@endlink) CsysType
          the csys type   
            
         
        """
        pass
    
    ## Getter for property: (@link NodalPairingMethod NXOpen.CAE.Connections.NodalPairingMethod@endlink) PairingMethod
    ##   the pairing method of targets   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NodalPairingMethod
    @property
    def PairingMethod(self) -> NodalPairingMethod:
        """
        Getter for property: (@link NodalPairingMethod NXOpen.CAE.Connections.NodalPairingMethod@endlink) PairingMethod
          the pairing method of targets   
            
         
        """
        pass
    
    ## Setter for property: (@link NodalPairingMethod NXOpen.CAE.Connections.NodalPairingMethod@endlink) PairingMethod

    ##   the pairing method of targets   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @PairingMethod.setter
    def PairingMethod(self, method: NodalPairingMethod):
        """
        Setter for property: (@link NodalPairingMethod NXOpen.CAE.Connections.NodalPairingMethod@endlink) PairingMethod
          the pairing method of targets   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) SearchConeAngle
    ##   the search cone angle   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def SearchConeAngle(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) SearchConeAngle
          the search cone angle   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) SearchOrientation
    ##   the pairing search orientation   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Direction
    @property
    def SearchOrientation(self) -> NXOpen.Direction:
        """
        Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) SearchOrientation
          the pairing search orientation   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) SearchOrientation

    ##   the pairing search orientation   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @SearchOrientation.setter
    def SearchOrientation(self, orientation: NXOpen.Direction):
        """
        Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) SearchOrientation
          the pairing search orientation   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) SearchRange
    ##   the search range   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def SearchRange(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) SearchRange
          the search range   
            
         
        """
        pass
    
##  nodal ring search type 
##  One Ring 
class RingSearchType(Enum):
    """
    Members Include: <OneRing> <TwoRings> <ExpansionRadius> <ExpansionRadiusFactor>
    """
    OneRing: int
    TwoRings: int
    ExpansionRadius: int
    ExpansionRadiusFactor: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> RingSearchType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


import NXOpen
##  Rivet connection. Use this interface to set/get properties and parameters of the rivet connection.  
## 
##   <br>  Created in NX1847.0.0  <br> 

class Rivet(IConnection): 
    """ Rivet connection. Use this interface to set/get properties and parameters of the rivet connection.  """


    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Coefficient
    ##   the coefficient for formula defined diameter   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Coefficient(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Coefficient
          the coefficient for formula defined diameter   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Diameter
    ##   the connection diameter   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Diameter(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Diameter
          the connection diameter   
            
         
        """
        pass
    
    ## Getter for property: (@link DiameterType NXOpen.CAE.Connections.DiameterType@endlink) DiameterType
    ##   the connection diameter type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return DiameterType
    @property
    def DiameterType(self) -> DiameterType:
        """
        Getter for property: (@link DiameterType NXOpen.CAE.Connections.DiameterType@endlink) DiameterType
          the connection diameter type   
            
         
        """
        pass
    
    ## Setter for property: (@link DiameterType NXOpen.CAE.Connections.DiameterType@endlink) DiameterType

    ##   the connection diameter type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @DiameterType.setter
    def DiameterType(self, diameterType: DiameterType):
        """
        Setter for property: (@link DiameterType NXOpen.CAE.Connections.DiameterType@endlink) DiameterType
          the connection diameter type   
            
         
        """
        pass
    
    ## Getter for property: (@link DiscretizationMethod NXOpen.CAE.Connections.DiscretizationMethod@endlink) DiscretizationMethod
    ##   the discretization method   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return DiscretizationMethod
    @property
    def DiscretizationMethod(self) -> DiscretizationMethod:
        """
        Getter for property: (@link DiscretizationMethod NXOpen.CAE.Connections.DiscretizationMethod@endlink) DiscretizationMethod
          the discretization method   
            
         
        """
        pass
    
    ## Setter for property: (@link DiscretizationMethod NXOpen.CAE.Connections.DiscretizationMethod@endlink) DiscretizationMethod

    ##   the discretization method   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @DiscretizationMethod.setter
    def DiscretizationMethod(self, method: DiscretizationMethod):
        """
        Setter for property: (@link DiscretizationMethod NXOpen.CAE.Connections.DiscretizationMethod@endlink) DiscretizationMethod
          the discretization method   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) DistanceFromStart
    ##   the line Discretization distance from start   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def DistanceFromStart(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) DistanceFromStart
          the line Discretization distance from start   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) DistanceToEnd
    ##   the line Discretization distance to end   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def DistanceToEnd(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) DistanceToEnd
          the line Discretization distance to end   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Height
    ##   the height value   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Height(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Height
          the height value   
            
         
        """
        pass
    
    ## Getter for property: (@link HeightType NXOpen.CAE.Connections.HeightType@endlink) HeightType
    ##   the connection height type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return HeightType
    @property
    def HeightType(self) -> HeightType:
        """
        Getter for property: (@link HeightType NXOpen.CAE.Connections.HeightType@endlink) HeightType
          the connection height type   
            
         
        """
        pass
    
    ## Setter for property: (@link HeightType NXOpen.CAE.Connections.HeightType@endlink) HeightType

    ##   the connection height type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @HeightType.setter
    def HeightType(self, heightType: HeightType):
        """
        Setter for property: (@link HeightType NXOpen.CAE.Connections.HeightType@endlink) HeightType
          the connection height type   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) LengthStep
    ##   the line Discretization length step   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def LengthStep(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) LengthStep
          the line Discretization length step   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.PhysicalMaterial NXOpen.PhysicalMaterial@endlink) Material
    ##   the connection material   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.PhysicalMaterial
    @property
    def Material(self) -> NXOpen.PhysicalMaterial:
        """
        Getter for property: (@link NXOpen.PhysicalMaterial NXOpen.PhysicalMaterial@endlink) Material
          the connection material   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.PhysicalMaterial NXOpen.PhysicalMaterial@endlink) Material

    ##   the connection material   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @Material.setter
    def Material(self, material: NXOpen.PhysicalMaterial):
        """
        Setter for property: (@link NXOpen.PhysicalMaterial NXOpen.PhysicalMaterial@endlink) Material
          the connection material   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxAngleBetweenNormals
    ##   the maximum angle of normals with the projection surface   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def MaxAngleBetweenNormals(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxAngleBetweenNormals
          the maximum angle of normals with the projection surface   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxDistCGToElemCG
    ##   the maximum distance from definition point to center of support element   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def MaxDistCGToElemCG(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxDistCGToElemCG
          the maximum distance from definition point to center of support element   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxLengthStep
    ##   the line Discretization max length step   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def MaxLengthStep(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxLengthStep
          the line Discretization max length step   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxNormalDistCGToFlanges
    ##   the maximum normal distance from definition point to center of element   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def MaxNormalDistCGToFlanges(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxNormalDistCGToFlanges
          the maximum normal distance from definition point to center of element   
            
         
        """
        pass
    
    ## Getter for property: (int) NumberOfDiscretizationPoints
    ##   the number of connections   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return int
    @property
    def NumberOfDiscretizationPoints(self) -> int:
        """
        Getter for property: (int) NumberOfDiscretizationPoints
          the number of connections   
            
         
        """
        pass
    
    ## Setter for property: (int) NumberOfDiscretizationPoints

    ##   the number of connections   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @NumberOfDiscretizationPoints.setter
    def NumberOfDiscretizationPoints(self, num: int):
        """
        Setter for property: (int) NumberOfDiscretizationPoints
          the number of connections   
            
         
        """
        pass
    
    ## Getter for property: (int) NumberOfFlanges
    ##   the number of flanges.  
    ##    When changing the number of flanges this is not applied till an update is performed by calling @link Update::DoUpdate Update::DoUpdate@endlink    
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return int
    @property
    def NumberOfFlanges(self) -> int:
        """
        Getter for property: (int) NumberOfFlanges
          the number of flanges.  
           When changing the number of flanges this is not applied till an update is performed by calling @link Update::DoUpdate Update::DoUpdate@endlink    
         
        """
        pass
    
    ## Setter for property: (int) NumberOfFlanges

    ##   the number of flanges.  
    ##    When changing the number of flanges this is not applied till an update is performed by calling @link Update::DoUpdate Update::DoUpdate@endlink    
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @NumberOfFlanges.setter
    def NumberOfFlanges(self, numberOfFlanges: int):
        """
        Setter for property: (int) NumberOfFlanges
          the number of flanges.  
           When changing the number of flanges this is not applied till an update is performed by calling @link Update::DoUpdate Update::DoUpdate@endlink    
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ProjectTolerance
    ##   the projection tolerance   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def ProjectTolerance(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ProjectTolerance
          the projection tolerance   
            
         
        """
        pass
    
    ## Getter for property: (str) TableFile
    ##   the table file used to compute the diameter   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return str
    @property
    def TableFile(self) -> str:
        """
        Getter for property: (str) TableFile
          the table file used to compute the diameter   
            
         
        """
        pass
    
    ## Setter for property: (str) TableFile

    ##   the table file used to compute the diameter   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @TableFile.setter
    def TableFile(self, tableFile: str):
        """
        Setter for property: (str) TableFile
          the table file used to compute the diameter   
            
         
        """
        pass
    
    ## Getter for property: (bool) UseMaxLengthStep
    ##   the usage of max length step   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return bool
    @property
    def UseMaxLengthStep(self) -> bool:
        """
        Getter for property: (bool) UseMaxLengthStep
          the usage of max length step   
            
         
        """
        pass
    
    ## Setter for property: (bool) UseMaxLengthStep

    ##   the usage of max length step   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @UseMaxLengthStep.setter
    def UseMaxLengthStep(self, use: bool):
        """
        Setter for property: (bool) UseMaxLengthStep
          the usage of max length step   
            
         
        """
        pass
    
    ## Getter for property: (bool) UseOriginalNodesOfConnection
    ##   the usage of original nodes of connection   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return bool
    @property
    def UseOriginalNodesOfConnection(self) -> bool:
        """
        Getter for property: (bool) UseOriginalNodesOfConnection
          the usage of original nodes of connection   
            
         
        """
        pass
    
    ## Setter for property: (bool) UseOriginalNodesOfConnection

    ##   the usage of original nodes of connection   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @UseOriginalNodesOfConnection.setter
    def UseOriginalNodesOfConnection(self, use: bool):
        """
        Setter for property: (bool) UseOriginalNodesOfConnection
          the usage of original nodes of connection   
            
         
        """
        pass
    
import NXOpen
##   Sealing connection. Use this interface to set/get properties and parameters of the spot weld connection.   <br> To obtain an instance of this object use the connection creators on the @link CAE::Connections::Folder CAE::Connections::Folder@endlink   <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class Sealing(IConnection): 
    """  Sealing connection. Use this interface to set/get properties and parameters of the spot weld connection.  """


    ## Getter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) Csys
    ##   the csys   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.CoordinateSystem
    @property
    def Csys(self) -> NXOpen.CoordinateSystem:
        """
        Getter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) Csys
          the csys   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) Csys

    ##   the csys   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @Csys.setter
    def Csys(self, csys: NXOpen.CoordinateSystem):
        """
        Setter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) Csys
          the csys   
            
         
        """
        pass
    
    ## Getter for property: (@link CsysType NXOpen.CAE.Connections.CsysType@endlink) CsysType
    ##   the csys type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return CsysType
    @property
    def CsysType(self) -> CsysType:
        """
        Getter for property: (@link CsysType NXOpen.CAE.Connections.CsysType@endlink) CsysType
          the csys type   
            
         
        """
        pass
    
    ## Setter for property: (@link CsysType NXOpen.CAE.Connections.CsysType@endlink) CsysType

    ##   the csys type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @CsysType.setter
    def CsysType(self, csysType: CsysType):
        """
        Setter for property: (@link CsysType NXOpen.CAE.Connections.CsysType@endlink) CsysType
          the csys type   
            
         
        """
        pass
    
    ## Getter for property: (@link DiscretizationMethod NXOpen.CAE.Connections.DiscretizationMethod@endlink) DiscretizationMethod
    ##   the discretization method   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return DiscretizationMethod
    @property
    def DiscretizationMethod(self) -> DiscretizationMethod:
        """
        Getter for property: (@link DiscretizationMethod NXOpen.CAE.Connections.DiscretizationMethod@endlink) DiscretizationMethod
          the discretization method   
            
         
        """
        pass
    
    ## Setter for property: (@link DiscretizationMethod NXOpen.CAE.Connections.DiscretizationMethod@endlink) DiscretizationMethod

    ##   the discretization method   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @DiscretizationMethod.setter
    def DiscretizationMethod(self, method: DiscretizationMethod):
        """
        Setter for property: (@link DiscretizationMethod NXOpen.CAE.Connections.DiscretizationMethod@endlink) DiscretizationMethod
          the discretization method   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) DistanceFromStart
    ##   the line Discretization distance from start   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def DistanceFromStart(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) DistanceFromStart
          the line Discretization distance from start   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) DistanceToEnd
    ##   the line Discretization distance to end   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def DistanceToEnd(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) DistanceToEnd
          the line Discretization distance to end   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) LengthStep
    ##   the line Discretization length step   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def LengthStep(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) LengthStep
          the line Discretization length step   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Mass
    ##   the mass value   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Mass(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Mass
          the mass value   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxAngleBetweenNormals
    ##   the maximum angle of normals with the projection surface   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def MaxAngleBetweenNormals(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxAngleBetweenNormals
          the maximum angle of normals with the projection surface   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxDistCGToElemCG
    ##   the maximum distance from definition point to center of support element   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def MaxDistCGToElemCG(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxDistCGToElemCG
          the maximum distance from definition point to center of support element   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxLengthStep
    ##   the line Discretization max length step   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def MaxLengthStep(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxLengthStep
          the line Discretization max length step   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxNormalDistCGToFlanges
    ##   the maximum normal distance from definition point to center of element   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def MaxNormalDistCGToFlanges(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxNormalDistCGToFlanges
          the maximum normal distance from definition point to center of element   
            
         
        """
        pass
    
    ## Getter for property: (int) NumberOfDiscretizationPoints
    ##   the number of connections   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return int
    @property
    def NumberOfDiscretizationPoints(self) -> int:
        """
        Getter for property: (int) NumberOfDiscretizationPoints
          the number of connections   
            
         
        """
        pass
    
    ## Setter for property: (int) NumberOfDiscretizationPoints

    ##   the number of connections   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @NumberOfDiscretizationPoints.setter
    def NumberOfDiscretizationPoints(self, num: int):
        """
        Setter for property: (int) NumberOfDiscretizationPoints
          the number of connections   
            
         
        """
        pass
    
    ## Getter for property: (int) NumberOfFlanges
    ##   the number of flanges.  
    ##    When changing the number of flanges this is not applied till an update is performed by calling @link Update::DoUpdate Update::DoUpdate@endlink    
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return int
    @property
    def NumberOfFlanges(self) -> int:
        """
        Getter for property: (int) NumberOfFlanges
          the number of flanges.  
           When changing the number of flanges this is not applied till an update is performed by calling @link Update::DoUpdate Update::DoUpdate@endlink    
         
        """
        pass
    
    ## Setter for property: (int) NumberOfFlanges

    ##   the number of flanges.  
    ##    When changing the number of flanges this is not applied till an update is performed by calling @link Update::DoUpdate Update::DoUpdate@endlink    
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @NumberOfFlanges.setter
    def NumberOfFlanges(self, numberOfFlanges: int):
        """
        Setter for property: (int) NumberOfFlanges
          the number of flanges.  
           When changing the number of flanges this is not applied till an update is performed by calling @link Update::DoUpdate Update::DoUpdate@endlink    
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ProjectTolerance
    ##   the projection tolerance   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def ProjectTolerance(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ProjectTolerance
          the projection tolerance   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RxStiffnessConstant
    ##   the RX stiffness constant   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def RxStiffnessConstant(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RxStiffnessConstant
          the RX stiffness constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RyStiffnessConstant
    ##   the RY stiffness constant   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def RyStiffnessConstant(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RyStiffnessConstant
          the RY stiffness constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RzStiffnessConstant
    ##   the RZ stiffness constant   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def RzStiffnessConstant(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RzStiffnessConstant
          the RZ stiffness constant   
            
         
        """
        pass
    
    ## Getter for property: (@link StiffnessType NXOpen.CAE.Connections.StiffnessType@endlink) StiffnessType
    ##   the stiffness type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return StiffnessType
    @property
    def StiffnessType(self) -> StiffnessType:
        """
        Getter for property: (@link StiffnessType NXOpen.CAE.Connections.StiffnessType@endlink) StiffnessType
          the stiffness type   
            
         
        """
        pass
    
    ## Setter for property: (@link StiffnessType NXOpen.CAE.Connections.StiffnessType@endlink) StiffnessType

    ##   the stiffness type   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @StiffnessType.setter
    def StiffnessType(self, oStiffnessType: StiffnessType):
        """
        Setter for property: (@link StiffnessType NXOpen.CAE.Connections.StiffnessType@endlink) StiffnessType
          the stiffness type   
            
         
        """
        pass
    
    ## Getter for property: (bool) UseMaxLengthStep
    ##   the usage of max length step   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return bool
    @property
    def UseMaxLengthStep(self) -> bool:
        """
        Getter for property: (bool) UseMaxLengthStep
          the usage of max length step   
            
         
        """
        pass
    
    ## Setter for property: (bool) UseMaxLengthStep

    ##   the usage of max length step   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @UseMaxLengthStep.setter
    def UseMaxLengthStep(self, use: bool):
        """
        Setter for property: (bool) UseMaxLengthStep
          the usage of max length step   
            
         
        """
        pass
    
    ## Getter for property: (bool) UseOriginalNodesOfConnection
    ##   the usage of original nodes of connection   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return bool
    @property
    def UseOriginalNodesOfConnection(self) -> bool:
        """
        Getter for property: (bool) UseOriginalNodesOfConnection
          the usage of original nodes of connection   
            
         
        """
        pass
    
    ## Setter for property: (bool) UseOriginalNodesOfConnection

    ##   the usage of original nodes of connection   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @UseOriginalNodesOfConnection.setter
    def UseOriginalNodesOfConnection(self, use: bool):
        """
        Setter for property: (bool) UseOriginalNodesOfConnection
          the usage of original nodes of connection   
            
         
        """
        pass
    
    ## Getter for property: (bool) WithOrientation
    ##   the target type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return bool
    @property
    def WithOrientation(self) -> bool:
        """
        Getter for property: (bool) WithOrientation
          the target type   
            
         
        """
        pass
    
    ## Setter for property: (bool) WithOrientation

    ##   the target type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @WithOrientation.setter
    def WithOrientation(self, orientation: bool):
        """
        Setter for property: (bool) WithOrientation
          the target type   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) XStiffnessConstant
    ##   the X stiffness constant   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def XStiffnessConstant(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) XStiffnessConstant
          the X stiffness constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) YStiffnessConstant
    ##   the Y stiffness constant   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def YStiffnessConstant(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) YStiffnessConstant
          the Y stiffness constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ZStiffnessConstant
    ##   the Z stiffness constant   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def ZStiffnessConstant(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ZStiffnessConstant
          the Z stiffness constant   
            
         
        """
        pass
    
##  Seam Weld Location type 
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## Vector</term><description> 
## </description> </item><item><term> 
## Flange1Side1</term><description> 
## </description> </item><item><term> 
## Flange1Side2</term><description> 
## </description> </item><item><term> 
## Flange2Side1</term><description> 
## </description> </item><item><term> 
## Flange2Side2</term><description> 
## </description> </item></list>
class SeamWeldLocationType(Enum):
    """
    Members Include: <Vector> <Flange1Side1> <Flange1Side2> <Flange2Side1> <Flange2Side2>
    """
    Vector: int
    Flange1Side1: int
    Flange1Side2: int
    Flange2Side1: int
    Flange2Side2: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> SeamWeldLocationType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


##  Seam Weld Material type 
##  Seam weld angle material type 
class SeamWeldMaterialType(Enum):
    """
    Members Include: <Angle> <Overlap> <Double>
    """
    Angle: int
    Overlap: int
    Double: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> SeamWeldMaterialType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


##  Seam Weld xMCF Type (describes the weld topology) 
##  Unspecified 
class SeamWeldMcfType(Enum):
    """
    Members Include: <Other> <YJoint> <OverlapWeld> <CornerWeld> <ButtJoint> <EdgeWeld> <DoubleCornerWeld> <CruciformJoint> <KJoint> <IWeld> <SplitIWeld>
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
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> SeamWeldMcfType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


##  Seam Weld Node Selection Method 
##  Use the node locations in the USWC(s) 
class SeamWeldNodeSelectionMethod(Enum):
    """
    Members Include: <ConnectionNodes> <Specify>
    """
    ConnectionNodes: int
    Specify: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> SeamWeldNodeSelectionMethod:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


##  Seam Weld Section type 
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## Undefined</term><description> 
## </description> </item><item><term> 
## I</term><description> 
## </description> </item><item><term> 
## V</term><description> 
## </description> </item><item><term> 
## U</term><description> 
## </description> </item><item><term> 
## X</term><description> 
## </description> </item><item><term> 
## Y</term><description> 
## </description> </item><item><term> 
## Hv</term><description> 
## </description> </item><item><term> 
## Hy</term><description> 
## </description> </item><item><term> 
## Fillet</term><description> 
## </description> </item><item><term> 
## Radius</term><description> 
## </description> </item></list>
class SeamWeldSectionType(Enum):
    """
    Members Include: <Undefined> <I> <V> <U> <X> <Y> <Hv> <Hy> <Fillet> <Radius>
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
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> SeamWeldSectionType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


##  Seam Weld Shape type 
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## Undefined</term><description> 
## </description> </item><item><term> 
## Straight</term><description> 
## </description> </item><item><term> 
## Convex</term><description> 
## </description> </item><item><term> 
## Concave</term><description> 
## </description> </item></list>
class SeamWeldShapeType(Enum):
    """
    Members Include: <Undefined> <Straight> <Convex> <Concave>
    """
    Undefined: int
    Straight: int
    Convex: int
    Concave: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> SeamWeldShapeType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


##  Seam Weld Side 
##  Weld on Side of the Larger Sheet Angle 
class SeamWeldSide(Enum):
    """
    Members Include: <OnLargerSheetAngle> <OnSmallerSheetAngle> <OnBothSheetSides>
    """
    OnLargerSheetAngle: int
    OnSmallerSheetAngle: int
    OnBothSheetSides: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> SeamWeldSide:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


##  Seam Weld Type 
##  Seam weld done with material 
class SeamWeldType(Enum):
    """
    Members Include: <WithMaterial> <WithLaser> <Resistance> <Friction> <Brazing>
    """
    WithMaterial: int
    WithLaser: int
    Resistance: int
    Friction: int
    Brazing: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> SeamWeldType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


import NXOpen
##   Seam Weld connection. Use this interface to set/get properties and parameters of the seam weld connection.   <br> To obtain an instance of this object use the connection creators on the @link CAE::Connections::Folder CAE::Connections::Folder@endlink   <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class SeamWeld(IConnection): 
    """  Seam Weld connection. Use this interface to set/get properties and parameters of the seam weld connection.  """


    ## Getter for property: (@link DiscretizationMethod NXOpen.CAE.Connections.DiscretizationMethod@endlink) DiscretizationMethod
    ##   the discretization method   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return DiscretizationMethod
    @property
    def DiscretizationMethod(self) -> DiscretizationMethod:
        """
        Getter for property: (@link DiscretizationMethod NXOpen.CAE.Connections.DiscretizationMethod@endlink) DiscretizationMethod
          the discretization method   
            
         
        """
        pass
    
    ## Setter for property: (@link DiscretizationMethod NXOpen.CAE.Connections.DiscretizationMethod@endlink) DiscretizationMethod

    ##   the discretization method   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @DiscretizationMethod.setter
    def DiscretizationMethod(self, method: DiscretizationMethod):
        """
        Setter for property: (@link DiscretizationMethod NXOpen.CAE.Connections.DiscretizationMethod@endlink) DiscretizationMethod
          the discretization method   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) DistanceFromStart
    ##   the line Discretization distance from start   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def DistanceFromStart(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) DistanceFromStart
          the line Discretization distance from start   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) DistanceToEnd
    ##   the line Discretization distance to end   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def DistanceToEnd(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) DistanceToEnd
          the line Discretization distance to end   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Height
    ##   the height value   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Height(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Height
          the height value   
            
         
        """
        pass
    
    ## Getter for property: (@link HeightType NXOpen.CAE.Connections.HeightType@endlink) HeightType
    ##   the connection height type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return HeightType
    @property
    def HeightType(self) -> HeightType:
        """
        Getter for property: (@link HeightType NXOpen.CAE.Connections.HeightType@endlink) HeightType
          the connection height type   
            
         
        """
        pass
    
    ## Setter for property: (@link HeightType NXOpen.CAE.Connections.HeightType@endlink) HeightType

    ##   the connection height type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @HeightType.setter
    def HeightType(self, heightType: HeightType):
        """
        Setter for property: (@link HeightType NXOpen.CAE.Connections.HeightType@endlink) HeightType
          the connection height type   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) LengthStep
    ##   the line Discretization length step   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def LengthStep(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) LengthStep
          the line Discretization length step   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.PhysicalMaterial NXOpen.PhysicalMaterial@endlink) Material
    ##   the connection material   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.PhysicalMaterial
    @property
    def Material(self) -> NXOpen.PhysicalMaterial:
        """
        Getter for property: (@link NXOpen.PhysicalMaterial NXOpen.PhysicalMaterial@endlink) Material
          the connection material   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.PhysicalMaterial NXOpen.PhysicalMaterial@endlink) Material

    ##   the connection material   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @Material.setter
    def Material(self, material: NXOpen.PhysicalMaterial):
        """
        Setter for property: (@link NXOpen.PhysicalMaterial NXOpen.PhysicalMaterial@endlink) Material
          the connection material   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxAngleBetweenNormals
    ##   the maximum angle of normals with the projection surface   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def MaxAngleBetweenNormals(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxAngleBetweenNormals
          the maximum angle of normals with the projection surface   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxDistCGToElemCG
    ##   the maximum distance from definition point to center of support element   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def MaxDistCGToElemCG(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxDistCGToElemCG
          the maximum distance from definition point to center of support element   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxLengthStep
    ##   the line Discretization max length step   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def MaxLengthStep(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxLengthStep
          the line Discretization max length step   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxNormalDistCGToFlanges
    ##   the maximum normal distance from definition point to center of element   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def MaxNormalDistCGToFlanges(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxNormalDistCGToFlanges
          the maximum normal distance from definition point to center of element   
            
         
        """
        pass
    
    ## Getter for property: (int) NumberOfDiscretizationPoints
    ##   the number of connections   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return int
    @property
    def NumberOfDiscretizationPoints(self) -> int:
        """
        Getter for property: (int) NumberOfDiscretizationPoints
          the number of connections   
            
         
        """
        pass
    
    ## Setter for property: (int) NumberOfDiscretizationPoints

    ##   the number of connections   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @NumberOfDiscretizationPoints.setter
    def NumberOfDiscretizationPoints(self, num: int):
        """
        Setter for property: (int) NumberOfDiscretizationPoints
          the number of connections   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ProjectTolerance
    ##   the projection tolerance   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def ProjectTolerance(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ProjectTolerance
          the projection tolerance   
            
         
        """
        pass
    
    ## Getter for property: (@link SeamWeldMcfType NXOpen.CAE.Connections.SeamWeldMcfType@endlink) SeamWeldMcfType
    ##   the seam weld MCF type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return SeamWeldMcfType
    @property
    def SeamWeldMcfType(self) -> SeamWeldMcfType:
        """
        Getter for property: (@link SeamWeldMcfType NXOpen.CAE.Connections.SeamWeldMcfType@endlink) SeamWeldMcfType
          the seam weld MCF type   
            
         
        """
        pass
    
    ## Setter for property: (@link SeamWeldMcfType NXOpen.CAE.Connections.SeamWeldMcfType@endlink) SeamWeldMcfType

    ##   the seam weld MCF type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @SeamWeldMcfType.setter
    def SeamWeldMcfType(self, seamWeldMcfType: SeamWeldMcfType):
        """
        Setter for property: (@link SeamWeldMcfType NXOpen.CAE.Connections.SeamWeldMcfType@endlink) SeamWeldMcfType
          the seam weld MCF type   
            
         
        """
        pass
    
    ## Getter for property: (@link SeamWeldType NXOpen.CAE.Connections.SeamWeldType@endlink) SeamWeldType
    ##   the seam weld type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return SeamWeldType
    @property
    def SeamWeldType(self) -> SeamWeldType:
        """
        Getter for property: (@link SeamWeldType NXOpen.CAE.Connections.SeamWeldType@endlink) SeamWeldType
          the seam weld type   
            
         
        """
        pass
    
    ## Setter for property: (@link SeamWeldType NXOpen.CAE.Connections.SeamWeldType@endlink) SeamWeldType

    ##   the seam weld type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @SeamWeldType.setter
    def SeamWeldType(self, seamWeldType: SeamWeldType):
        """
        Setter for property: (@link SeamWeldType NXOpen.CAE.Connections.SeamWeldType@endlink) SeamWeldType
          the seam weld type   
            
         
        """
        pass
    
    ## Getter for property: (bool) UseMaxLengthStep
    ##   the usage of max length step   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return bool
    @property
    def UseMaxLengthStep(self) -> bool:
        """
        Getter for property: (bool) UseMaxLengthStep
          the usage of max length step   
            
         
        """
        pass
    
    ## Setter for property: (bool) UseMaxLengthStep

    ##   the usage of max length step   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @UseMaxLengthStep.setter
    def UseMaxLengthStep(self, use: bool):
        """
        Setter for property: (bool) UseMaxLengthStep
          the usage of max length step   
            
         
        """
        pass
    
    ## Getter for property: (bool) UseOriginalNodesOfConnection
    ##   the usage of original nodes of connection   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return bool
    @property
    def UseOriginalNodesOfConnection(self) -> bool:
        """
        Getter for property: (bool) UseOriginalNodesOfConnection
          the usage of original nodes of connection   
            
         
        """
        pass
    
    ## Setter for property: (bool) UseOriginalNodesOfConnection

    ##   the usage of original nodes of connection   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @UseOriginalNodesOfConnection.setter
    def UseOriginalNodesOfConnection(self, use: bool):
        """
        Setter for property: (bool) UseOriginalNodesOfConnection
          the usage of original nodes of connection   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Width
    ##   the width value   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Width(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Width
          the width value   
            
         
        """
        pass
    
    ##  Convert to Flange-Side location type.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ## <param name="weldIndex"> (int) </param>
    def ConvertToFlangeSideLocationType(connection: SeamWeld, weldIndex: int) -> None:
        """
         Convert to Flange-Side location type.
        """
        pass
    
    ##  Convert to Vector location type.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ## <param name="weldIndex"> (int) </param>
    def ConvertToVectorLocationType(connection: SeamWeld, weldIndex: int) -> None:
        """
         Convert to Vector location type.
        """
        pass
    
    ##  Get default weld angle.
    ##  @return defaultAngle (@link NXOpen.Expression NXOpen.Expression@endlink): .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetDefaultWeldAngle(connection: SeamWeld) -> NXOpen.Expression:
        """
         Get default weld angle.
         @return defaultAngle (@link NXOpen.Expression NXOpen.Expression@endlink): .
        """
        pass
    
    ##  Get default weld penetration.
    ##  @return defaultPenetration (@link NXOpen.Expression NXOpen.Expression@endlink): .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetDefaultWeldPenetration(connection: SeamWeld) -> NXOpen.Expression:
        """
         Get default weld penetration.
         @return defaultPenetration (@link NXOpen.Expression NXOpen.Expression@endlink): .
        """
        pass
    
    ##  Get default weld thickness.
    ##  @return defaultThickness (@link NXOpen.Expression NXOpen.Expression@endlink): .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetDefaultWeldThickness(connection: SeamWeld) -> NXOpen.Expression:
        """
         Get default weld thickness.
         @return defaultThickness (@link NXOpen.Expression NXOpen.Expression@endlink): .
        """
        pass
    
    ##  Get default weld width.
    ##  @return defaultWidth (@link NXOpen.Expression NXOpen.Expression@endlink): .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetDefaultWeldWidth(connection: SeamWeld) -> NXOpen.Expression:
        """
         Get default weld width.
         @return defaultWidth (@link NXOpen.Expression NXOpen.Expression@endlink): .
        """
        pass
    
    ##  Get minimum and maximum number of welds in a Seam Weld connection 
    ##  @return A tuple consisting of (minNumWelds, maxNumWelds). 
    ##  - minNumWelds is: int.
    ##  - maxNumWelds is: int.

    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetMinMaxNumberOfWelds(connection: SeamWeld) -> Tuple[int, int]:
        """
         Get minimum and maximum number of welds in a Seam Weld connection 
         @return A tuple consisting of (minNumWelds, maxNumWelds). 
         - minNumWelds is: int.
         - maxNumWelds is: int.

        """
        pass
    
    ##  Get the number of welds in a Seam Weld connection 
    ##  @return numWelds (int): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetNumberOfWelds(connection: SeamWeld) -> int:
        """
         Get the number of welds in a Seam Weld connection 
         @return numWelds (int): .
        """
        pass
    
    ##  Get the seam weld Location parameter 
    ##  @return locationParameter (float): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="weldIndex"> (int) </param>
    def GetSeamWeldLocationParameter(connection: SeamWeld, weldIndex: int) -> float:
        """
         Get the seam weld Location parameter 
         @return locationParameter (float): .
        """
        pass
    
    ##  Get the seam weld Location type 
    ##  @return seamWeldLocationType (@link SeamWeldLocationType NXOpen.CAE.Connections.SeamWeldLocationType@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="weldIndex"> (int) </param>
    def GetSeamWeldLocationType(connection: SeamWeld, weldIndex: int) -> SeamWeldLocationType:
        """
         Get the seam weld Location type 
         @return seamWeldLocationType (@link SeamWeldLocationType NXOpen.CAE.Connections.SeamWeldLocationType@endlink): .
        """
        pass
    
    ##  Get the seam weld Location vector 
    ##  @return locationVector (@link NXOpen.Direction NXOpen.Direction@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="weldIndex"> (int) </param>
    def GetSeamWeldLocationVector(connection: SeamWeld, weldIndex: int) -> NXOpen.Direction:
        """
         Get the seam weld Location vector 
         @return locationVector (@link NXOpen.Direction NXOpen.Direction@endlink): .
        """
        pass
    
    ##  Get the seam weld Material 
    ##  @return material (@link NXOpen.PhysicalMaterial NXOpen.PhysicalMaterial@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="weldIndex"> (int) </param>
    def GetSeamWeldMaterial(connection: SeamWeld, weldIndex: int) -> NXOpen.PhysicalMaterial:
        """
         Get the seam weld Material 
         @return material (@link NXOpen.PhysicalMaterial NXOpen.PhysicalMaterial@endlink): .
        """
        pass
    
    ##  Get the seam weld Section type 
    ##  @return seamWeldSectionType (@link SeamWeldSectionType NXOpen.CAE.Connections.SeamWeldSectionType@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="weldIndex"> (int) </param>
    def GetSeamWeldSectionType(connection: SeamWeld, weldIndex: int) -> SeamWeldSectionType:
        """
         Get the seam weld Section type 
         @return seamWeldSectionType (@link SeamWeldSectionType NXOpen.CAE.Connections.SeamWeldSectionType@endlink): .
        """
        pass
    
    ##  Get the seam weld Shape type 
    ##  @return seamWeldShapeType (@link SeamWeldShapeType NXOpen.CAE.Connections.SeamWeldShapeType@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="weldIndex"> (int) </param>
    def GetSeamWeldShapeType(connection: SeamWeld, weldIndex: int) -> SeamWeldShapeType:
        """
         Get the seam weld Shape type 
         @return seamWeldShapeType (@link SeamWeldShapeType NXOpen.CAE.Connections.SeamWeldShapeType@endlink): .
        """
        pass
    
    ##  Get the weld angle.
    ##  @return angle (@link NXOpen.Expression NXOpen.Expression@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="weldIndex"> (int) </param>
    def GetWeldAngle(connection: SeamWeld, weldIndex: int) -> NXOpen.Expression:
        """
         Get the weld angle.
         @return angle (@link NXOpen.Expression NXOpen.Expression@endlink): .
        """
        pass
    
    ##  Get the weld penetration.
    ##  @return penetration (@link NXOpen.Expression NXOpen.Expression@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="weldIndex"> (int) </param>
    def GetWeldPenetration(connection: SeamWeld, weldIndex: int) -> NXOpen.Expression:
        """
         Get the weld penetration.
         @return penetration (@link NXOpen.Expression NXOpen.Expression@endlink): .
        """
        pass
    
    ##  Get the weld thickness.
    ##  @return thickness (@link NXOpen.Expression NXOpen.Expression@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="weldIndex"> (int) </param>
    def GetWeldThickness(connection: SeamWeld, weldIndex: int) -> NXOpen.Expression:
        """
         Get the weld thickness.
         @return thickness (@link NXOpen.Expression NXOpen.Expression@endlink): .
        """
        pass
    
    ##  Get the weld width.
    ##  @return width (@link NXOpen.Expression NXOpen.Expression@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="weldIndex"> (int) </param>
    def GetWeldWidth(connection: SeamWeld, weldIndex: int) -> NXOpen.Expression:
        """
         Get the weld width.
         @return width (@link NXOpen.Expression NXOpen.Expression@endlink): .
        """
        pass
    
    ##  Set the number of welds in a Seam Weld connection 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="numWelds"> (int) </param>
    def SetNumberOfWelds(connection: SeamWeld, numWelds: int) -> None:
        """
         Set the number of welds in a Seam Weld connection 
        """
        pass
    
    ##  Set the seam weld Location parameter 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ## <param name="weldIndex"> (int) </param>
    ## <param name="locationParameter"> (float) </param>
    def SetSeamWeldLocationParameter(connection: SeamWeld, weldIndex: int, locationParameter: float) -> None:
        """
         Set the seam weld Location parameter 
        """
        pass
    
    ##  Set the seam weld Location type 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ## <param name="weldIndex"> (int) </param>
    ## <param name="seamWeldLocationType"> (@link SeamWeldLocationType NXOpen.CAE.Connections.SeamWeldLocationType@endlink) </param>
    def SetSeamWeldLocationType(connection: SeamWeld, weldIndex: int, seamWeldLocationType: SeamWeldLocationType) -> None:
        """
         Set the seam weld Location type 
        """
        pass
    
    ##  Set the seam weld Location vector 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ## <param name="weldIndex"> (int) </param>
    ## <param name="locationVector"> (@link NXOpen.Direction NXOpen.Direction@endlink) </param>
    def SetSeamWeldLocationVector(connection: SeamWeld, weldIndex: int, locationVector: NXOpen.Direction) -> None:
        """
         Set the seam weld Location vector 
        """
        pass
    
    ##  Set the seam weld Material 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ## <param name="weldIndex"> (int) </param>
    ## <param name="material"> (@link NXOpen.PhysicalMaterial NXOpen.PhysicalMaterial@endlink) </param>
    def SetSeamWeldMaterial(connection: SeamWeld, weldIndex: int, material: NXOpen.PhysicalMaterial) -> None:
        """
         Set the seam weld Material 
        """
        pass
    
    ##  Set the seam weld Section type 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ## <param name="weldIndex"> (int) </param>
    ## <param name="seamWeldSectionType"> (@link SeamWeldSectionType NXOpen.CAE.Connections.SeamWeldSectionType@endlink) </param>
    def SetSeamWeldSectionType(connection: SeamWeld, weldIndex: int, seamWeldSectionType: SeamWeldSectionType) -> None:
        """
         Set the seam weld Section type 
        """
        pass
    
    ##  Set the seam weld Shape type 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ## <param name="weldIndex"> (int) </param>
    ## <param name="seamWeldShapeType"> (@link SeamWeldShapeType NXOpen.CAE.Connections.SeamWeldShapeType@endlink) </param>
    def SetSeamWeldShapeType(connection: SeamWeld, weldIndex: int, seamWeldShapeType: SeamWeldShapeType) -> None:
        """
         Set the seam weld Shape type 
        """
        pass
    
import NXOpen.CAE
##   @brief  Location interface. This defines connection locations with common properties like coordinates.  
## 
##    <br> To obtain an instance of this object use the AddLocation creators on the Connections  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class SelectionRecipeLocation(Location): 
    """ <summary> Location interface. This defines connection locations with common properties like coordinates. </summary> """


    ## Getter for property: (@link NXOpen.CAE.SelectionRecipe NXOpen.CAE.SelectionRecipe@endlink) SelectionRecipe
    ##   the Selection Recipe used for creating the location.  
    ##   
    ##                 If the location type is not a Selection Recipe, this method will raise an error.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.CAE.SelectionRecipe
    @property
    def SelectionRecipe(self) -> NXOpen.CAE.SelectionRecipe:
        """
        Getter for property: (@link NXOpen.CAE.SelectionRecipe NXOpen.CAE.SelectionRecipe@endlink) SelectionRecipe
          the Selection Recipe used for creating the location.  
          
                        If the location type is not a Selection Recipe, this method will raise an error.   
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.CAE.SelectionRecipe NXOpen.CAE.SelectionRecipe@endlink) SelectionRecipe

    ##   the Selection Recipe used for creating the location.  
    ##   
    ##                 If the location type is not a Selection Recipe, this method will raise an error.   
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @SelectionRecipe.setter
    def SelectionRecipe(self, selectionRecipe: NXOpen.CAE.SelectionRecipe):
        """
        Setter for property: (@link NXOpen.CAE.SelectionRecipe NXOpen.CAE.SelectionRecipe@endlink) SelectionRecipe
          the Selection Recipe used for creating the location.  
          
                        If the location type is not a Selection Recipe, this method will raise an error.   
         
        """
        pass
    
##  Shank length discretization definition types 
##  No shank discretization for shank length 
class ShankLengthDiscretizationType(Enum):
    """
    Members Include: <NotSet> <UserDefined> <PercentLength> <PercentCurve>
    """
    NotSet: int
    UserDefined: int
    PercentLength: int
    PercentCurve: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> ShankLengthDiscretizationType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


##  Shank segment discretization definition types 
##  No shank discretization for shank segments 
class ShankSegmentDiscretizationType(Enum):
    """
    Members Include: <NotSet> <SegmentLength> <NumSegments>
    """
    NotSet: int
    SegmentLength: int
    NumSegments: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> ShankSegmentDiscretizationType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


import NXOpen
##  Contains smart template application utility methods  <br> To obtain an instance of this class, refer to @link NXOpen::Session  NXOpen::Session @endlink  <br> 
## 
##   <br>  Created in NX1872.0.0  <br> 

class SmartTemplateBuilder(NXOpen.Object): 
    """ Contains smart template application utility methods """


    ##  Create Smart template tools  
    ##  @return smartTemplateTool (@link SmartTemplateTool NXOpen.CAE.Connections.SmartTemplateTool@endlink): .
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: sc_gso_smart (" Simcenter Smart Template Pre/Post Applications") OR sc_gso_comp (" Simcenter NVH Composer")
    @staticmethod
    def GetSmartTemplateTool() -> SmartTemplateTool:
        """
         Create Smart template tools  
         @return smartTemplateTool (@link SmartTemplateTool NXOpen.CAE.Connections.SmartTemplateTool@endlink): .
        """
        pass
    
import NXOpen
import NXOpen.CAE
##  Contains smart template application utility methods 
## 
##   <br>  Created in NX1872.0.0  <br> 

class SmartTemplateTool(NXOpen.TaggedObject): 
    """ Contains smart template application utility methods """


    ##  Destroy the smart template tool object 
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: sc_gso_smart (" Simcenter Smart Template Pre/Post Applications") OR sc_gso_comp (" Simcenter NVH Composer")
    @staticmethod
    def Destroy(smartTemplateTool: SmartTemplateTool) -> None:
        """
         Destroy the smart template tool object 
        """
        pass
    
    ##  Export PIDs to Groups
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: sc_gso_comp (" Simcenter NVH Composer")
    ##  The context Cae part
    def ExportPIDs(smartTemplateTool: SmartTemplateTool, caePart: NXOpen.CAE.CaePart, iAbsoluteExportPath: str) -> None:
        """
         Export PIDs to Groups
        """
        pass
    
    ##  Export the requested result data to an Excel file 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: sc_gso_smart (" Simcenter Smart Template Pre/Post Applications")
    ##  The solution. 
    def ExportResultDataToExcel(smartTemplateTool: SmartTemplateTool, pSimSolution: NXOpen.CAE.SimSolution, iAbsoluteExportPath: str, resultName: str, drivingPoints: bool, indexFile: str) -> None:
        """
         Export the requested result data to an Excel file 
        """
        pass
    
    ##  Export SOL200 Design sensitivity analysis solution report
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: sc_gso_smart (" Simcenter Smart Template Pre/Post Applications")
    ##  The SOL200 Design sensitivity analysis solution
    def ExportResults(smartTemplateTool: SmartTemplateTool, pSimSolution: NXOpen.CAE.SimSolution, iAbsoluteExportPath: str) -> None:
        """
         Export SOL200 Design sensitivity analysis solution report
        """
        pass
    
    ##  Get Physical property tables associated to group
    ##  @return physicalPropertyTableTags (@link NXOpen.CAE.PhysicalPropertyTable List[NXOpen.CAE.PhysicalPropertyTable]@endlink):  Group elements associated physical property tables. .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: sc_gso_smart (" Simcenter Smart Template Pre/Post Applications")
    ##  Element or mesh entity type group 
    def GetGroupPhysicalPropertyTables(smartTemplateTool: SmartTemplateTool, caeGroup: NXOpen.CAE.CaeGroup) -> List[NXOpen.CAE.PhysicalPropertyTable]:
        """
         Get Physical property tables associated to group
         @return physicalPropertyTableTags (@link NXOpen.CAE.PhysicalPropertyTable List[NXOpen.CAE.PhysicalPropertyTable]@endlink):  Group elements associated physical property tables. .
        """
        pass
    
    ##  Get hard point name and associated type from the input file 
    ##  @return A tuple consisting of (listOfHardPointTypes, listOfHardPointNames). 
    ##  - listOfHardPointTypes is: @link NXOpen.CAE.SelRecipeBaseStrategy.Type List[NXOpen.CAE.SelRecipeBaseStrategy.Type]@endlink.
    ##  - listOfHardPointNames is: List[str].

    ## 
    ##   <br>  Created in NX1984.0.0  <br> 

    ## License requirements: sc_gso_smart (" Simcenter Smart Template Pre/Post Applications")
    ##  The path for the hard point file. 
    @staticmethod
    def GetHardPointNameAndType(smartTemplateTool: SmartTemplateTool, iAbsoluteFilePath: str) -> Tuple[List[NXOpen.CAE.SelRecipeBaseStrategy.Type], List[str]]:
        """
         Get hard point name and associated type from the input file 
         @return A tuple consisting of (listOfHardPointTypes, listOfHardPointNames). 
         - listOfHardPointTypes is: @link NXOpen.CAE.SelRecipeBaseStrategy.Type List[NXOpen.CAE.SelRecipeBaseStrategy.Type]@endlink.
         - listOfHardPointNames is: List[str].

        """
        pass
    
    ##  Import PIDs to xml file
    ##  @return caeGroups (@link NXOpen.CAE.CaeGroup List[NXOpen.CAE.CaeGroup]@endlink): .
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: sc_gso_smart (" Simcenter Smart Template Pre/Post Applications")
    ##  The context Cae part
    @overload
    def ImportGroups(self, smartTemplateTool: SmartTemplateTool, caePart: NXOpen.CAE.CaePart, iAbsoluteImportPath: str) -> List[NXOpen.CAE.CaeGroup]:
        """
         Import PIDs to xml file
         @return caeGroups (@link NXOpen.CAE.CaeGroup List[NXOpen.CAE.CaeGroup]@endlink): .
        """
        pass
    
    ##  Import PIDs to xml file
    ##  @return caeGroups (@link NXOpen.CAE.CaeGroup List[NXOpen.CAE.CaeGroup]@endlink): .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: sc_gso_smart (" Simcenter Smart Template Pre/Post Applications")
    ##  The context Cae part
    @overload
    def ImportGroups(self, smartTemplateTool: SmartTemplateTool, caePart: NXOpen.CAE.CaePart, iAbsoluteImportPath: str, selectedGroups: List[str]) -> List[NXOpen.CAE.CaeGroup]:
        """
         Import PIDs to xml file
         @return caeGroups (@link NXOpen.CAE.CaeGroup List[NXOpen.CAE.CaeGroup]@endlink): .
        """
        pass
    
import NXOpen
##  Spot Weld connection. Use this interface to set/get properties and parameters of the spot weld connection.  
## 
##   <br>  Created in NX12.0.0  <br> 

class SpotWeld(IConnection): 
    """ Spot Weld connection. Use this interface to set/get properties and parameters of the spot weld connection.  """


    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Coefficient
    ##   the coefficient for formula defined diameter   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Coefficient(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Coefficient
          the coefficient for formula defined diameter   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Diameter
    ##   the connection diameter   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Diameter(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Diameter
          the connection diameter   
            
         
        """
        pass
    
    ## Getter for property: (@link DiameterType NXOpen.CAE.Connections.DiameterType@endlink) DiameterType
    ##   the connection diameter type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return DiameterType
    @property
    def DiameterType(self) -> DiameterType:
        """
        Getter for property: (@link DiameterType NXOpen.CAE.Connections.DiameterType@endlink) DiameterType
          the connection diameter type   
            
         
        """
        pass
    
    ## Setter for property: (@link DiameterType NXOpen.CAE.Connections.DiameterType@endlink) DiameterType

    ##   the connection diameter type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @DiameterType.setter
    def DiameterType(self, diameterType: DiameterType):
        """
        Setter for property: (@link DiameterType NXOpen.CAE.Connections.DiameterType@endlink) DiameterType
          the connection diameter type   
            
         
        """
        pass
    
    ## Getter for property: (@link DiscretizationMethod NXOpen.CAE.Connections.DiscretizationMethod@endlink) DiscretizationMethod
    ##   the discretization method   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return DiscretizationMethod
    @property
    def DiscretizationMethod(self) -> DiscretizationMethod:
        """
        Getter for property: (@link DiscretizationMethod NXOpen.CAE.Connections.DiscretizationMethod@endlink) DiscretizationMethod
          the discretization method   
            
         
        """
        pass
    
    ## Setter for property: (@link DiscretizationMethod NXOpen.CAE.Connections.DiscretizationMethod@endlink) DiscretizationMethod

    ##   the discretization method   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @DiscretizationMethod.setter
    def DiscretizationMethod(self, method: DiscretizationMethod):
        """
        Setter for property: (@link DiscretizationMethod NXOpen.CAE.Connections.DiscretizationMethod@endlink) DiscretizationMethod
          the discretization method   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) DistanceFromStart
    ##   the line Discretization distance from start   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def DistanceFromStart(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) DistanceFromStart
          the line Discretization distance from start   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) DistanceToEnd
    ##   the line Discretization distance to end   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def DistanceToEnd(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) DistanceToEnd
          the line Discretization distance to end   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Height
    ##   the height value   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Height(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Height
          the height value   
            
         
        """
        pass
    
    ## Getter for property: (@link HeightType NXOpen.CAE.Connections.HeightType@endlink) HeightType
    ##   the connection height type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return HeightType
    @property
    def HeightType(self) -> HeightType:
        """
        Getter for property: (@link HeightType NXOpen.CAE.Connections.HeightType@endlink) HeightType
          the connection height type   
            
         
        """
        pass
    
    ## Setter for property: (@link HeightType NXOpen.CAE.Connections.HeightType@endlink) HeightType

    ##   the connection height type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @HeightType.setter
    def HeightType(self, heightType: HeightType):
        """
        Setter for property: (@link HeightType NXOpen.CAE.Connections.HeightType@endlink) HeightType
          the connection height type   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) LengthStep
    ##   the line Discretization length step   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def LengthStep(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) LengthStep
          the line Discretization length step   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.PhysicalMaterial NXOpen.PhysicalMaterial@endlink) Material
    ##   the connection material   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.PhysicalMaterial
    @property
    def Material(self) -> NXOpen.PhysicalMaterial:
        """
        Getter for property: (@link NXOpen.PhysicalMaterial NXOpen.PhysicalMaterial@endlink) Material
          the connection material   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.PhysicalMaterial NXOpen.PhysicalMaterial@endlink) Material

    ##   the connection material   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @Material.setter
    def Material(self, material: NXOpen.PhysicalMaterial):
        """
        Setter for property: (@link NXOpen.PhysicalMaterial NXOpen.PhysicalMaterial@endlink) Material
          the connection material   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxAngleBetweenNormals
    ##   the maximum angle of normals with the projection surface   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def MaxAngleBetweenNormals(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxAngleBetweenNormals
          the maximum angle of normals with the projection surface   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxDistCGToElemCG
    ##   the maximum distance from definition point to center of support element   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def MaxDistCGToElemCG(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxDistCGToElemCG
          the maximum distance from definition point to center of support element   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxLengthStep
    ##   the line Discretization max length step   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def MaxLengthStep(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxLengthStep
          the line Discretization max length step   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxNormalDistCGToFlanges
    ##   the maximum normal distance from definition point to center of element   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def MaxNormalDistCGToFlanges(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxNormalDistCGToFlanges
          the maximum normal distance from definition point to center of element   
            
         
        """
        pass
    
    ## Getter for property: (int) NumberOfDiscretizationPoints
    ##   the number of connections   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return int
    @property
    def NumberOfDiscretizationPoints(self) -> int:
        """
        Getter for property: (int) NumberOfDiscretizationPoints
          the number of connections   
            
         
        """
        pass
    
    ## Setter for property: (int) NumberOfDiscretizationPoints

    ##   the number of connections   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @NumberOfDiscretizationPoints.setter
    def NumberOfDiscretizationPoints(self, num: int):
        """
        Setter for property: (int) NumberOfDiscretizationPoints
          the number of connections   
            
         
        """
        pass
    
    ## Getter for property: (int) NumberOfFlanges
    ##   the number of flanges.  
    ##    When changing the number of flanges this is not applied till an update is performed by calling @link Update::DoUpdate Update::DoUpdate@endlink    
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return int
    @property
    def NumberOfFlanges(self) -> int:
        """
        Getter for property: (int) NumberOfFlanges
          the number of flanges.  
           When changing the number of flanges this is not applied till an update is performed by calling @link Update::DoUpdate Update::DoUpdate@endlink    
         
        """
        pass
    
    ## Setter for property: (int) NumberOfFlanges

    ##   the number of flanges.  
    ##    When changing the number of flanges this is not applied till an update is performed by calling @link Update::DoUpdate Update::DoUpdate@endlink    
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @NumberOfFlanges.setter
    def NumberOfFlanges(self, numberOfFlanges: int):
        """
        Setter for property: (int) NumberOfFlanges
          the number of flanges.  
           When changing the number of flanges this is not applied till an update is performed by calling @link Update::DoUpdate Update::DoUpdate@endlink    
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ProjectTolerance
    ##   the projection tolerance   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def ProjectTolerance(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ProjectTolerance
          the projection tolerance   
            
         
        """
        pass
    
    ## Getter for property: (str) TableFile
    ##   the table file used to compute the diameter   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return str
    @property
    def TableFile(self) -> str:
        """
        Getter for property: (str) TableFile
          the table file used to compute the diameter   
            
         
        """
        pass
    
    ## Setter for property: (str) TableFile

    ##   the table file used to compute the diameter   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @TableFile.setter
    def TableFile(self, tableFile: str):
        """
        Setter for property: (str) TableFile
          the table file used to compute the diameter   
            
         
        """
        pass
    
    ## Getter for property: (bool) UseMaxLengthStep
    ##   the usage of max length step   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return bool
    @property
    def UseMaxLengthStep(self) -> bool:
        """
        Getter for property: (bool) UseMaxLengthStep
          the usage of max length step   
            
         
        """
        pass
    
    ## Setter for property: (bool) UseMaxLengthStep

    ##   the usage of max length step   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @UseMaxLengthStep.setter
    def UseMaxLengthStep(self, use: bool):
        """
        Setter for property: (bool) UseMaxLengthStep
          the usage of max length step   
            
         
        """
        pass
    
    ## Getter for property: (bool) UseOriginalNodesOfConnection
    ##   the usage of original nodes of connection   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return bool
    @property
    def UseOriginalNodesOfConnection(self) -> bool:
        """
        Getter for property: (bool) UseOriginalNodesOfConnection
          the usage of original nodes of connection   
            
         
        """
        pass
    
    ## Setter for property: (bool) UseOriginalNodesOfConnection

    ##   the usage of original nodes of connection   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @UseOriginalNodesOfConnection.setter
    def UseOriginalNodesOfConnection(self, use: bool):
        """
        Setter for property: (bool) UseOriginalNodesOfConnection
          the usage of original nodes of connection   
            
         
        """
        pass
    
import NXOpen
##  Spring connection. Use this interface to set/get properties and parameters of the Spring connection.  
## 
##   <br>  Created in NX12.0.0  <br> 

class Spring(IConnection): 
    """ Spring connection. Use this interface to set/get properties and parameters of the Spring connection.  """


    ## Getter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) Csys
    ##   the csys   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.CoordinateSystem
    @property
    def Csys(self) -> NXOpen.CoordinateSystem:
        """
        Getter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) Csys
          the csys   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) Csys

    ##   the csys   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @Csys.setter
    def Csys(self, csys: NXOpen.CoordinateSystem):
        """
        Setter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) Csys
          the csys   
            
         
        """
        pass
    
    ## Getter for property: (@link CsysType NXOpen.CAE.Connections.CsysType@endlink) CsysType
    ##   the csys type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return CsysType
    @property
    def CsysType(self) -> CsysType:
        """
        Getter for property: (@link CsysType NXOpen.CAE.Connections.CsysType@endlink) CsysType
          the csys type   
            
         
        """
        pass
    
    ## Setter for property: (@link CsysType NXOpen.CAE.Connections.CsysType@endlink) CsysType

    ##   the csys type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @CsysType.setter
    def CsysType(self, csysType: CsysType):
        """
        Setter for property: (@link CsysType NXOpen.CAE.Connections.CsysType@endlink) CsysType
          the csys type   
            
         
        """
        pass
    
    ## Getter for property: (bool) IsMassOnBothTargets
    ##   the isMassOnBothTargets   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return bool
    @property
    def IsMassOnBothTargets(self) -> bool:
        """
        Getter for property: (bool) IsMassOnBothTargets
          the isMassOnBothTargets   
            
         
        """
        pass
    
    ## Setter for property: (bool) IsMassOnBothTargets

    ##   the isMassOnBothTargets   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @IsMassOnBothTargets.setter
    def IsMassOnBothTargets(self, isMassOnBothTargets: bool):
        """
        Setter for property: (bool) IsMassOnBothTargets
          the isMassOnBothTargets   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Mass
    ##   the mass value   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Mass(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Mass
          the mass value   
            
         
        """
        pass
    
    ## Getter for property: (@link NodalPairingMethod NXOpen.CAE.Connections.NodalPairingMethod@endlink) PairingMethod
    ##   the pairing method of targets   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NodalPairingMethod
    @property
    def PairingMethod(self) -> NodalPairingMethod:
        """
        Getter for property: (@link NodalPairingMethod NXOpen.CAE.Connections.NodalPairingMethod@endlink) PairingMethod
          the pairing method of targets   
            
         
        """
        pass
    
    ## Setter for property: (@link NodalPairingMethod NXOpen.CAE.Connections.NodalPairingMethod@endlink) PairingMethod

    ##   the pairing method of targets   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @PairingMethod.setter
    def PairingMethod(self, method: NodalPairingMethod):
        """
        Setter for property: (@link NodalPairingMethod NXOpen.CAE.Connections.NodalPairingMethod@endlink) PairingMethod
          the pairing method of targets   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RxStiffnessConstant
    ##   the RX stiffness constant   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def RxStiffnessConstant(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RxStiffnessConstant
          the RX stiffness constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RyStiffnessConstant
    ##   the RY stiffness constant   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def RyStiffnessConstant(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RyStiffnessConstant
          the RY stiffness constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RzStiffnessConstant
    ##   the RZ stiffness constant   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def RzStiffnessConstant(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RzStiffnessConstant
          the RZ stiffness constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) SearchConeAngle
    ##   the search cone angle   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def SearchConeAngle(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) SearchConeAngle
          the search cone angle   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) SearchOrientation
    ##   the pairing search orientation   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Direction
    @property
    def SearchOrientation(self) -> NXOpen.Direction:
        """
        Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) SearchOrientation
          the pairing search orientation   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) SearchOrientation

    ##   the pairing search orientation   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @SearchOrientation.setter
    def SearchOrientation(self, orientation: NXOpen.Direction):
        """
        Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) SearchOrientation
          the pairing search orientation   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) SearchRange
    ##   the search range   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def SearchRange(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) SearchRange
          the search range   
            
         
        """
        pass
    
    ## Getter for property: (@link StiffnessType NXOpen.CAE.Connections.StiffnessType@endlink) StiffnessType
    ##   the stiffness type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return StiffnessType
    @property
    def StiffnessType(self) -> StiffnessType:
        """
        Getter for property: (@link StiffnessType NXOpen.CAE.Connections.StiffnessType@endlink) StiffnessType
          the stiffness type   
            
         
        """
        pass
    
    ## Setter for property: (@link StiffnessType NXOpen.CAE.Connections.StiffnessType@endlink) StiffnessType

    ##   the stiffness type   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @StiffnessType.setter
    def StiffnessType(self, oStiffnessType: StiffnessType):
        """
        Setter for property: (@link StiffnessType NXOpen.CAE.Connections.StiffnessType@endlink) StiffnessType
          the stiffness type   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) XStiffnessConstant
    ##   the X stiffness constant   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def XStiffnessConstant(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) XStiffnessConstant
          the X stiffness constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) YStiffnessConstant
    ##   the Y stiffness constant   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def YStiffnessConstant(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) YStiffnessConstant
          the Y stiffness constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ZStiffnessConstant
    ##   the Z stiffness constant   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def ZStiffnessConstant(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ZStiffnessConstant
          the Z stiffness constant   
            
         
        """
        pass
    
##  Stiffness type 
##  Stiffness value will be specified per element 
class StiffnessType(Enum):
    """
    Members Include: <PerElement> <PerUnitLength>
    """
    PerElement: int
    PerUnitLength: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> StiffnessType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


##  Nodal target dependency type 
##  No dependency 
class TargetDependencyType(Enum):
    """
    Members Include: <NotSet> <Dependent> <Independent>
    """
    NotSet: int
    Dependent: int
    Independent: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> TargetDependencyType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


##  Universal Connection Status 
##  Connection state cannot be determined 
class UniversalConnectionState(Enum):
    """
    Members Include: <Unknown> <Meshed> <NotMeshed> <Invalid>
    """
    Unknown: int
    Meshed: int
    NotMeshed: int
    Invalid: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> UniversalConnectionState:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


import NXOpen
import NXOpen.CAE
import NXOpen.Features
##  Contains universal connections utility methods  <br> To obtain an instance of this class, refer to @link NXOpen::CAE::CaeSession  NXOpen::CAE::CaeSession @endlink  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class Utils(NXOpen.Object): 
    """ Contains universal connections utility methods """


    ##  Create standalone LMIEConnection 
    ##  @return opt (@link LMIEConnection NXOpen.CAE.Connections.LMIEConnection@endlink):  The created standalone LMIEConnection .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## <param name="contextPart"> (@link NXOpen.INXObject NXOpen.INXObject@endlink) </param>
    def CreateLmieconnection(contextPart: NXOpen.INXObject) -> LMIEConnection:
        """
         Create standalone LMIEConnection 
         @return opt (@link LMIEConnection NXOpen.CAE.Connections.LMIEConnection@endlink):  The created standalone LMIEConnection .
        """
        pass
    
    ##  Exports the intermediate connection representations of lumped mass connections to external file. File type is determined by the extension. 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ##  The array of input lumped mass intermediate representations 
    def ExportLumpedMassInterchangeData(iConnections: List[LMIEConnection], iAbsoluteExportPath: str, iConvertConnectionDataFromPartUnits: bool) -> None:
        """
         Exports the intermediate connection representations of lumped mass connections to external file. File type is determined by the extension. 
        """
        pass
    
    ##  Filters a list of connections by type 
    ##  @return oConnections (@link IConnection List[NXOpen.CAE.Connections.IConnection]@endlink):  all connections matching the specified connection type .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ##  The array of input connections 
    def FilterConnectionsByType(iConnections: List[IConnection], type: ConnectionType) -> List[IConnection]:
        """
         Filters a list of connections by type 
         @return oConnections (@link IConnection List[NXOpen.CAE.Connections.IConnection]@endlink):  all connections matching the specified connection type .
        """
        pass
    
    ##  Get Bodies from Given Imported Feature 
    ##  @return body (@link NXOpen.Body List[NXOpen.Body]@endlink):  list of bodies of given imported feature .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: sc_gso_creation (" Simcenter GSO BIW Creation environment")
    ##  The context Feature 
    @staticmethod
    def GetBodyFromFeature(feature: NXOpen.Features.Feature) -> List[NXOpen.Body]:
        """
         Get Bodies from Given Imported Feature 
         @return body (@link NXOpen.Body List[NXOpen.Body]@endlink):  list of bodies of given imported feature .
        """
        pass
    
    ##  Retrieve object at projection of a Bolt Universal Connection  
    ##  @return boltSupportObject (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink):  The Support Object .
    ## 
    ##   <br>  Created in NX1934.0.0  <br> 

    ## License requirements: None.
    ##  The Bolt Universal Connection 
    def GetBoltSupportOfLocation(iBoltConnection: IConnection, locationIndex: int, coordinateIndex: int, boltSupportIndex: int) -> NXOpen.TaggedObject:
        """
         Retrieve object at projection of a Bolt Universal Connection  
         @return boltSupportObject (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink):  The Support Object .
        """
        pass
    
    ##  Get XYZ Coordinates from Constraint File 
    ##  @return coordinates (@link NXOpen.Point3d List[NXOpen.Point3d]@endlink):  The array of the coordinates read from constraint file .
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: sc_gso_abmesh (" Simcenter GSO Ansa Batch Mesh environment")
    ##  The absolute path of the constraint file to be parsed 
    @staticmethod
    def GetCoordinatesFromConstraintFile(constraintFilePath: str) -> List[NXOpen.Point3d]:
        """
         Get XYZ Coordinates from Constraint File 
         @return coordinates (@link NXOpen.Point3d List[NXOpen.Point3d]@endlink):  The array of the coordinates read from constraint file .
        """
        pass
    
    ##  Retrieve element labels from FeModel  
    ##  @return labels (List[int]):  The element labels .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    ##  The FeModel 
    def GetElemLabels(feModel: NXOpen.CAE.IFEModel, fromChildren: bool) -> List[int]:
        """
         Retrieve element labels from FeModel  
         @return labels (List[int]):  The element labels .
        """
        pass
    
    ##  Get Feature from Given Imported Body 
    ##  @return feature (@link NXOpen.Features.Feature NXOpen.Features.Feature@endlink):  Feature of given imported Body .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: sc_gso_creation (" Simcenter GSO BIW Creation environment")
    ##  The context Body 
    @staticmethod
    def GetFeatureFromBody(body: NXOpen.Body) -> NXOpen.Features.Feature:
        """
         Get Feature from Given Imported Body 
         @return feature (@link NXOpen.Features.Feature NXOpen.Features.Feature@endlink):  Feature of given imported Body .
        """
        pass
    
    ##  Retrieve free edges from element collectors  
    ##  @return freeEdges (@link NXOpen.CAE.FEElement List[NXOpen.CAE.FEElement]@endlink):  The Free Edges .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ##  The FeModel 
    def GetFreeEdgesFromElementCollectors(feModel: NXOpen.CAE.IFEModel, iElementCollectors: List[NXOpen.CAE.Mesh]) -> List[NXOpen.CAE.FEElement]:
        """
         Retrieve free edges from element collectors  
         @return freeEdges (@link NXOpen.CAE.FEElement List[NXOpen.CAE.FEElement]@endlink):  The Free Edges .
        """
        pass
    
    ##  Returns the intermediate connection representations of lumped mass connections 
    ##  @return oConnections (@link LMIEConnection List[NXOpen.CAE.Connections.LMIEConnection]@endlink):  The intermediate connection representations .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ##  The length unit 
    def GetInterchangeDataFromLumpedMass(conversionLengthUnit: NXOpen.Unit, conversionMassUnit: NXOpen.Unit, iConnections: List[LumpedMass], iAbsoluteExportPath: str) -> List[LMIEConnection]:
        """
         Returns the intermediate connection representations of lumped mass connections 
         @return oConnections (@link LMIEConnection List[NXOpen.CAE.Connections.LMIEConnection]@endlink):  The intermediate connection representations .
        """
        pass
    
    ##  Retrieve node labels from FeModel  
    ##  @return labels (List[int]):  The node labels .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    ##  The FeModel 
    def GetNodeLabels(feModel: NXOpen.CAE.IFEModel, fromChildren: bool) -> List[int]:
        """
         Retrieve node labels from FeModel  
         @return labels (List[int]):  The node labels .
        """
        pass
    
    ##  Retrieve object at projection of a Universal Connection other than Bolt  
    ##  @return objectAtProjection (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink):  The Object at projection .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ##  The Universal Connection 
    def GetObjectAtProjectionOfLocation(iConnection: IConnection, locationIndex: int, coordinateIndex: int, flangeIndex: int) -> NXOpen.TaggedObject:
        """
         Retrieve object at projection of a Universal Connection other than Bolt  
         @return objectAtProjection (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink):  The Object at projection .
        """
        pass
    
    ##  Returns the projection points of the connections per geometry flanges
    ##  @return A tuple consisting of (oFlanges, oProjectionPoints, oFlangeObjectIndexList). 
    ##  - oFlanges is: @link NXOpen.INXObject List[NXOpen.INXObject]@endlink. The array of the geometry flange objects .
    ##  - oProjectionPoints is: @link NXOpen.Point3d List[NXOpen.Point3d]@endlink. The array of the projection points .
    ##  - oFlangeObjectIndexList is: List[int]. The array of projection point index ranges per flanges. The size of the array is number of flanges + 1. For the flange i the index range is [oFlangeObjectIndexList[i], ..., oFlangeObjectIndexList[i + 1] - 1]. .

    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ##  The array of input connections 
    @staticmethod
    def GetProjectionPoints(iConnections: List[IConnection]) -> Tuple[List[NXOpen.INXObject], List[NXOpen.Point3d], List[int]]:
        """
         Returns the projection points of the connections per geometry flanges
         @return A tuple consisting of (oFlanges, oProjectionPoints, oFlangeObjectIndexList). 
         - oFlanges is: @link NXOpen.INXObject List[NXOpen.INXObject]@endlink. The array of the geometry flange objects .
         - oProjectionPoints is: @link NXOpen.Point3d List[NXOpen.Point3d]@endlink. The array of the projection points .
         - oFlangeObjectIndexList is: List[int]. The array of projection point index ranges per flanges. The size of the array is number of flanges + 1. For the flange i the index range is [oFlangeObjectIndexList[i], ..., oFlangeObjectIndexList[i + 1] - 1]. .

        """
        pass
    
    ##  Imports the intermediate connection representations of lumped mass connections from external file. File type is determined by the extension. 
    ##  @return oConnections (@link LMIEConnection List[NXOpen.CAE.Connections.LMIEConnection]@endlink):  The intermediate connection representations .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ##  The absolute path where the connections are to be imported from 
    def ImportLumpedMassInterchangeData(contextPart: NXOpen.INXObject, iAbsoluteImportPath: str) -> List[LMIEConnection]:
        """
         Imports the intermediate connection representations of lumped mass connections from external file. File type is determined by the extension. 
         @return oConnections (@link LMIEConnection List[NXOpen.CAE.Connections.LMIEConnection]@endlink):  The intermediate connection representations .
        """
        pass
    
    ##  Map CAD Prt geometry in FemPart 
    ##  @return caeFeature (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink):  Mapped cad feature in FemPart .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##  The context fem part
    def MapObject(femPart: NXOpen.CAE.FemPart, cadFeature: NXOpen.TaggedObject, syncGeomData: bool) -> NXOpen.TaggedObject:
        """
         Map CAD Prt geometry in FemPart 
         @return caeFeature (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink):  Mapped cad feature in FemPart .
        """
        pass
    
    ##  Print the connection element's information file 
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## <param name="connectionElement"> (@link Element NXOpen.CAE.Connections.Element@endlink) </param>
    @staticmethod
    def PrintConnectionElementInformationFile(connectionElement: Element) -> None:
        """
         Print the connection element's information file 
        """
        pass
    
    ##  Print the connection's information file 
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## <param name="connection"> (@link IConnection NXOpen.CAE.Connections.IConnection@endlink) </param>
    @staticmethod
    def PrintConnectionInformationFile(connection: IConnection) -> None:
        """
         Print the connection's information file 
        """
        pass
    
    ##  Reimport mesh created by external mesher. The work part should be a FEM meshed with an external mesher. 
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: sc_gso_abmesh (" Simcenter GSO Ansa Batch Mesh environment")
    @staticmethod
    def ReimportMesh() -> None:
        """
         Reimport mesh created by external mesher. The work part should be a FEM meshed with an external mesher. 
        """
        pass
    
    ##  Redo labeling of current work AFEM physical properties. The work part should be a AFEM.  
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: sc_gso_creation (" Simcenter GSO BIW Creation environment")
    ##  The context Assembly FEM Part
    @staticmethod
    def RelabelAFEMPhysicalProperty(assyFemPart: NXOpen.CAE.AssyFemPart) -> None:
        """
         Redo labeling of current work AFEM physical properties. The work part should be a AFEM.  
        """
        pass
    
    ##  Redo labeling of current work AFEM. The work part should be a AFEM.  
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: sc_gso_creation (" Simcenter GSO BIW Creation environment")
    @staticmethod
    def RelabelAfem() -> None:
        """
         Redo labeling of current work AFEM. The work part should be a AFEM.  
        """
        pass
    
    ##  Relabel assembly FEM with offset start ID 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: sc_gso_creation (" Simcenter GSO BIW Creation environment") OR sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ##  The context Assembly FEM Part
    def RelabelAfmOffsets(assyFemPart: NXOpen.CAE.AssyFemPart, node_offset: int, elem_offset: int, csys_offset: int, phys_offset: int) -> None:
        """
         Relabel assembly FEM with offset start ID 
        """
        pass
    
    ##  Remesh Seam Weld Connection Compatible Components 
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: sc_gso_abmesh (" Simcenter GSO Ansa Batch Mesh environment")
    ##  The array of input connections 
    @staticmethod
    def RemeshCompatibleConnectionComponents(connections: List[IConnection]) -> None:
        """
         Remesh Seam Weld Connection Compatible Components 
        """
        pass
    
    ##  Returns the nearest polygon geometry per connections when project failed 
    ##  @return A tuple consisting of (oNearestFlanges, oFlangeObjectIndices). 
    ##  - oNearestFlanges is: @link NXOpen.INXObject List[NXOpen.INXObject]@endlink. The array of the geometry flange objects .
    ##  - oFlangeObjectIndices is: List[int]. The array of nearest flange ranges per flanges. The size of the array is number of flanges + 1. For the flange i the index range is [oFlangeObjectIndexList[i], ..., oFlangeObjectIndexList[i + 1] - 1]. .

    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: sc_gso_creation (" Simcenter GSO BIW Creation environment")
    ##  The array of input connections 
    @staticmethod
    def SearchNearestFlanges(iConnections: List[IConnection]) -> Tuple[List[NXOpen.INXObject], List[int]]:
        """
         Returns the nearest polygon geometry per connections when project failed 
         @return A tuple consisting of (oNearestFlanges, oFlangeObjectIndices). 
         - oNearestFlanges is: @link NXOpen.INXObject List[NXOpen.INXObject]@endlink. The array of the geometry flange objects .
         - oFlangeObjectIndices is: List[int]. The array of nearest flange ranges per flanges. The size of the array is number of flanges + 1. For the flange i the index range is [oFlangeObjectIndexList[i], ..., oFlangeObjectIndexList[i + 1] - 1]. .

        """
        pass
    
    ##  Splits the warped quads by invoking an external mesher. The work part should be a FEM meshed with an external mesher. 
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: sc_gso_abmesh (" Simcenter GSO Ansa Batch Mesh environment")
    @staticmethod
    def SplitWarpedQuads() -> None:
        """
         Splits the warped quads by invoking an external mesher. The work part should be a FEM meshed with an external mesher. 
        """
        pass
    
    ##  Write XYZ Coordinates to Constraint File 
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: sc_gso_abmesh (" Simcenter GSO Ansa Batch Mesh environment")
    ##  The absolute path of the constraint file to be parsed 
    def WriteCoordinatesToConstraintFile(constraintFilePath: str, connectionName: str, coordinates: List[NXOpen.Point3d]) -> None:
        """
         Write XYZ Coordinates to Constraint File 
        """
        pass
    
## @package NXOpen.CAE.Connections
## Classes, Enums and Structs under NXOpen.CAE.Connections namespace

