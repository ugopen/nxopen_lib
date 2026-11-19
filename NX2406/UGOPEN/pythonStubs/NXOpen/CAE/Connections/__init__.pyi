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
    ##  Returns the discretization method   
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
         Returns the discretization method   
            
         
        """
        pass
    
    ## Setter for property: (@link DiscretizationMethod NXOpen.CAE.Connections.DiscretizationMethod@endlink) DiscretizationMethod

    ##  Returns the discretization method   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @DiscretizationMethod.setter
    def DiscretizationMethod(self, method: DiscretizationMethod):
        """
        Setter for property: (@link DiscretizationMethod NXOpen.CAE.Connections.DiscretizationMethod@endlink) DiscretizationMethod
         Returns the discretization method   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) DistanceFromStart
    ##  Returns the line Discretization distance from start   
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
         Returns the line Discretization distance from start   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) DistanceToEnd
    ##  Returns the line Discretization distance to end   
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
         Returns the line Discretization distance to end   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Height
    ##  Returns the height value   
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
         Returns the height value   
            
         
        """
        pass
    
    ## Getter for property: (@link HeightType NXOpen.CAE.Connections.HeightType@endlink) HeightType
    ##  Returns the connection height type   
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
         Returns the connection height type   
            
         
        """
        pass
    
    ## Setter for property: (@link HeightType NXOpen.CAE.Connections.HeightType@endlink) HeightType

    ##  Returns the connection height type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @HeightType.setter
    def HeightType(self, heightType: HeightType):
        """
        Setter for property: (@link HeightType NXOpen.CAE.Connections.HeightType@endlink) HeightType
         Returns the connection height type   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) LengthStep
    ##  Returns the line Discretization length step   
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
         Returns the line Discretization length step   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.PhysicalMaterial NXOpen.PhysicalMaterial@endlink) Material
    ##  Returns the connection material   
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
         Returns the connection material   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.PhysicalMaterial NXOpen.PhysicalMaterial@endlink) Material

    ##  Returns the connection material   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @Material.setter
    def Material(self, material: NXOpen.PhysicalMaterial):
        """
        Setter for property: (@link NXOpen.PhysicalMaterial NXOpen.PhysicalMaterial@endlink) Material
         Returns the connection material   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxAngleBetweenNormals
    ##  Returns the maximum angle of normals with the projection surface   
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
         Returns the maximum angle of normals with the projection surface   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxDistCGToElemCG
    ##  Returns the maximum distance from definition point to center of support element   
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
         Returns the maximum distance from definition point to center of support element   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxLengthStep
    ##  Returns the line Discretization max length step   
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
         Returns the line Discretization max length step   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxNormalDistCGToFlanges
    ##  Returns the maximum normal distance from definition point to center of element   
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
         Returns the maximum normal distance from definition point to center of element   
            
         
        """
        pass
    
    ## Getter for property: (int) NumberOfDiscretizationPoints
    ##  Returns the number of connections   
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
         Returns the number of connections   
            
         
        """
        pass
    
    ## Setter for property: (int) NumberOfDiscretizationPoints

    ##  Returns the number of connections   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @NumberOfDiscretizationPoints.setter
    def NumberOfDiscretizationPoints(self, num: int):
        """
        Setter for property: (int) NumberOfDiscretizationPoints
         Returns the number of connections   
            
         
        """
        pass
    
    ## Getter for property: (int) NumberOfFlanges
    ##  Returns the number of flanges.  
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
         Returns the number of flanges.  
           When changing the number of flanges this is not applied till an update is performed by calling @link Update::DoUpdate Update::DoUpdate@endlink    
         
        """
        pass
    
    ## Setter for property: (int) NumberOfFlanges

    ##  Returns the number of flanges.  
    ##    When changing the number of flanges this is not applied till an update is performed by calling @link Update::DoUpdate Update::DoUpdate@endlink    
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @NumberOfFlanges.setter
    def NumberOfFlanges(self, numberOfFlanges: int):
        """
        Setter for property: (int) NumberOfFlanges
         Returns the number of flanges.  
           When changing the number of flanges this is not applied till an update is performed by calling @link Update::DoUpdate Update::DoUpdate@endlink    
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ProjectTolerance
    ##  Returns the projection tolerance   
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
         Returns the projection tolerance   
            
         
        """
        pass
    
    ## Getter for property: (bool) UseMaxLengthStep
    ##  Returns the usage of max length step   
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
         Returns the usage of max length step   
            
         
        """
        pass
    
    ## Setter for property: (bool) UseMaxLengthStep

    ##  Returns the usage of max length step   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @UseMaxLengthStep.setter
    def UseMaxLengthStep(self, use: bool):
        """
        Setter for property: (bool) UseMaxLengthStep
         Returns the usage of max length step   
            
         
        """
        pass
    
    ## Getter for property: (bool) UseOriginalNodesOfConnection
    ##  Returns the usage of original nodes of connection   
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
         Returns the usage of original nodes of connection   
            
         
        """
        pass
    
    ## Setter for property: (bool) UseOriginalNodesOfConnection

    ##  Returns the usage of original nodes of connection   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @UseOriginalNodesOfConnection.setter
    def UseOriginalNodesOfConnection(self, use: bool):
        """
        Setter for property: (bool) UseOriginalNodesOfConnection
         Returns the usage of original nodes of connection   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Width
    ##  Returns the width value   
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
         Returns the width value   
            
         
        """
        pass
    
import NXOpen
##  Bar connection. Use this interface to set/get properties and parameters of the Bar connection.  
## 
##   <br>  Created in NX1926.0.0  <br> 

class Bar(IConnection): 
    """ Bar connection. Use this interface to set/get properties and parameters of the Bar connection.  """


    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Coefficient
    ##  Returns the coefficient for formula defined diameter   
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
         Returns the coefficient for formula defined diameter   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Diameter
    ##  Returns the connection diameter   
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
         Returns the connection diameter   
            
         
        """
        pass
    
    ## Getter for property: (@link DiameterType NXOpen.CAE.Connections.DiameterType@endlink) DiameterType
    ##  Returns the connection diameter type   
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
         Returns the connection diameter type   
            
         
        """
        pass
    
    ## Setter for property: (@link DiameterType NXOpen.CAE.Connections.DiameterType@endlink) DiameterType

    ##  Returns the connection diameter type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @DiameterType.setter
    def DiameterType(self, diameterType: DiameterType):
        """
        Setter for property: (@link DiameterType NXOpen.CAE.Connections.DiameterType@endlink) DiameterType
         Returns the connection diameter type   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.PhysicalMaterial NXOpen.PhysicalMaterial@endlink) Material
    ##  Returns the connection material   
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
         Returns the connection material   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.PhysicalMaterial NXOpen.PhysicalMaterial@endlink) Material

    ##  Returns the connection material   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @Material.setter
    def Material(self, material: NXOpen.PhysicalMaterial):
        """
        Setter for property: (@link NXOpen.PhysicalMaterial NXOpen.PhysicalMaterial@endlink) Material
         Returns the connection material   
            
         
        """
        pass
    
    ## Getter for property: (@link NodalPairingMethod NXOpen.CAE.Connections.NodalPairingMethod@endlink) PairingMethod
    ##  Returns the pairing method of targets   
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
         Returns the pairing method of targets   
            
         
        """
        pass
    
    ## Setter for property: (@link NodalPairingMethod NXOpen.CAE.Connections.NodalPairingMethod@endlink) PairingMethod

    ##  Returns the pairing method of targets   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @PairingMethod.setter
    def PairingMethod(self, method: NodalPairingMethod):
        """
        Setter for property: (@link NodalPairingMethod NXOpen.CAE.Connections.NodalPairingMethod@endlink) PairingMethod
         Returns the pairing method of targets   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) SearchConeAngle
    ##  Returns the search cone angle   
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
         Returns the search cone angle   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) SearchOrientation
    ##  Returns the pairing search orientation   
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
         Returns the pairing search orientation   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) SearchOrientation

    ##  Returns the pairing search orientation   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @SearchOrientation.setter
    def SearchOrientation(self, orientation: NXOpen.Direction):
        """
        Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) SearchOrientation
         Returns the pairing search orientation   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) SearchRange
    ##  Returns the search range   
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
         Returns the search range   
            
         
        """
        pass
    
    ## Getter for property: (str) TableFile
    ##  Returns the table file used to compute the diameter   
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
         Returns the table file used to compute the diameter   
            
         
        """
        pass
    
    ## Setter for property: (str) TableFile

    ##  Returns the table file used to compute the diameter   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @TableFile.setter
    def TableFile(self, tableFile: str):
        """
        Setter for property: (str) TableFile
         Returns the table file used to compute the diameter   
            
         
        """
        pass
    
import NXOpen
##  Bearing connection. Use this interface to set/get properties and parameters of the Bearing connection.  
## 
##   <br>  Created in NX1953.0.0  <br> 

class Bearing(IConnection): 
    """ Bearing connection. Use this interface to set/get properties and parameters of the Bearing connection.  """


    ## Getter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) Csys
    ##  Returns the csys   
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
         Returns the csys   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) Csys

    ##  Returns the csys   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @Csys.setter
    def Csys(self, csys: NXOpen.CoordinateSystem):
        """
        Setter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) Csys
         Returns the csys   
            
         
        """
        pass
    
    ## Getter for property: (@link CsysType NXOpen.CAE.Connections.CsysType@endlink) CsysType
    ##  Returns the csys type   
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
         Returns the csys type   
            
         
        """
        pass
    
    ## Setter for property: (@link CsysType NXOpen.CAE.Connections.CsysType@endlink) CsysType

    ##  Returns the csys type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @CsysType.setter
    def CsysType(self, csysType: CsysType):
        """
        Setter for property: (@link CsysType NXOpen.CAE.Connections.CsysType@endlink) CsysType
         Returns the csys type   
            
         
        """
        pass
    
    ## Getter for property: (@link NodalPairingMethod NXOpen.CAE.Connections.NodalPairingMethod@endlink) PairingMethod
    ##  Returns the pairing method of targets   
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
         Returns the pairing method of targets   
            
         
        """
        pass
    
    ## Setter for property: (@link NodalPairingMethod NXOpen.CAE.Connections.NodalPairingMethod@endlink) PairingMethod

    ##  Returns the pairing method of targets   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @PairingMethod.setter
    def PairingMethod(self, method: NodalPairingMethod):
        """
        Setter for property: (@link NodalPairingMethod NXOpen.CAE.Connections.NodalPairingMethod@endlink) PairingMethod
         Returns the pairing method of targets   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) SearchConeAngle
    ##  Returns the search cone angle   
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
         Returns the search cone angle   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) SearchOrientation
    ##  Returns the pairing search orientation   
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
         Returns the pairing search orientation   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) SearchOrientation

    ##  Returns the pairing search orientation   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @SearchOrientation.setter
    def SearchOrientation(self, orientation: NXOpen.Direction):
        """
        Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) SearchOrientation
         Returns the pairing search orientation   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) SearchRange
    ##  Returns the search range   
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
         Returns the search range   
            
         
        """
        pass
    
import NXOpen
##  Bolt connection. Use this interface to set/get properties and parameters of the spot weld connection.   <br> To obtain an instance of this object use the connection creators on the @link CAE::Connections::Folder CAE::Connections::Folder@endlink   <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class Bolt(IConnection): 
    """ Bolt connection. Use this interface to set/get properties and parameters of the spot weld connection.  """


    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Coefficient
    ##  Returns the coefficient for formula defined diameter   
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
         Returns the coefficient for formula defined diameter   
            
         
        """
        pass
    
    ## Getter for property: (bool) DefineNutDiameter
    ##  Returns the define nut diameter   
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
         Returns the define nut diameter   
            
         
        """
        pass
    
    ## Setter for property: (bool) DefineNutDiameter

    ##  Returns the define nut diameter   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @DefineNutDiameter.setter
    def DefineNutDiameter(self, param: bool):
        """
        Setter for property: (bool) DefineNutDiameter
         Returns the define nut diameter   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Diameter
    ##  Returns the connection diameter   
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
         Returns the connection diameter   
            
         
        """
        pass
    
    ## Getter for property: (@link DiameterType NXOpen.CAE.Connections.DiameterType@endlink) DiameterType
    ##  Returns the connection diameter type   
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
         Returns the connection diameter type   
            
         
        """
        pass
    
    ## Setter for property: (@link DiameterType NXOpen.CAE.Connections.DiameterType@endlink) DiameterType

    ##  Returns the connection diameter type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @DiameterType.setter
    def DiameterType(self, diameterType: DiameterType):
        """
        Setter for property: (@link DiameterType NXOpen.CAE.Connections.DiameterType@endlink) DiameterType
         Returns the connection diameter type   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) HeadDiameter
    ##  Returns the head diameter    
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
         Returns the head diameter    
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) HeadDiameterCoefficient
    ##  Returns the head diameter coefficient   
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
         Returns the head diameter coefficient   
            
         
        """
        pass
    
    ## Getter for property: (@link HeadDiameterType NXOpen.CAE.Connections.HeadDiameterType@endlink) HeadDiameterType
    ##  Returns the head diameter type   
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
         Returns the head diameter type   
            
         
        """
        pass
    
    ## Setter for property: (@link HeadDiameterType NXOpen.CAE.Connections.HeadDiameterType@endlink) HeadDiameterType

    ##  Returns the head diameter type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @HeadDiameterType.setter
    def HeadDiameterType(self, param: HeadDiameterType):
        """
        Setter for property: (@link HeadDiameterType NXOpen.CAE.Connections.HeadDiameterType@endlink) HeadDiameterType
         Returns the head diameter type   
            
         
        """
        pass
    
    ## Getter for property: (bool) LimitLocationEndpointsLength
    ##  Returns the flag indicating to limit the bolt's length to the length between the location endpoints    
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
         Returns the flag indicating to limit the bolt's length to the length between the location endpoints    
            
         
        """
        pass
    
    ## Setter for property: (bool) LimitLocationEndpointsLength

    ##  Returns the flag indicating to limit the bolt's length to the length between the location endpoints    
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @LimitLocationEndpointsLength.setter
    def LimitLocationEndpointsLength(self, param: bool):
        """
        Setter for property: (bool) LimitLocationEndpointsLength
         Returns the flag indicating to limit the bolt's length to the length between the location endpoints    
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.PhysicalMaterial NXOpen.PhysicalMaterial@endlink) Material
    ##  Returns the connection material   
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
         Returns the connection material   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.PhysicalMaterial NXOpen.PhysicalMaterial@endlink) Material

    ##  Returns the connection material   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @Material.setter
    def Material(self, material: NXOpen.PhysicalMaterial):
        """
        Setter for property: (@link NXOpen.PhysicalMaterial NXOpen.PhysicalMaterial@endlink) Material
         Returns the connection material   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxBoltLength
    ##  Returns the maximum bolt length   
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
         Returns the maximum bolt length   
            
         
        """
        pass
    
    ## Getter for property: (int) NumberOfFlanges
    ##  Returns the number of flanges.  
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
         Returns the number of flanges.  
           When changing the number of flanges this is not applied till an update is performed by calling @link Update::DoUpdate Update::DoUpdate@endlink    
         
        """
        pass
    
    ## Setter for property: (int) NumberOfFlanges

    ##  Returns the number of flanges.  
    ##    When changing the number of flanges this is not applied till an update is performed by calling @link Update::DoUpdate Update::DoUpdate@endlink    
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @NumberOfFlanges.setter
    def NumberOfFlanges(self, numberOfFlanges: int):
        """
        Setter for property: (int) NumberOfFlanges
         Returns the number of flanges.  
           When changing the number of flanges this is not applied till an update is performed by calling @link Update::DoUpdate Update::DoUpdate@endlink    
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) NutDiameter
    ##  Returns the nut diameter    
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
         Returns the nut diameter    
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) NutDiameterCoefficient
    ##  Returns the nut diameter coefficient   
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
         Returns the nut diameter coefficient   
            
         
        """
        pass
    
    ## Getter for property: (@link NutDiameterType NXOpen.CAE.Connections.NutDiameterType@endlink) NutDiameterType
    ##  Returns the nut diameter type   
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
         Returns the nut diameter type   
            
         
        """
        pass
    
    ## Setter for property: (@link NutDiameterType NXOpen.CAE.Connections.NutDiameterType@endlink) NutDiameterType

    ##  Returns the nut diameter type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @NutDiameterType.setter
    def NutDiameterType(self, param: NutDiameterType):
        """
        Setter for property: (@link NutDiameterType NXOpen.CAE.Connections.NutDiameterType@endlink) NutDiameterType
         Returns the nut diameter type   
            
         
        """
        pass
    
    ## Getter for property: (@link ShankLengthDiscretizationType NXOpen.CAE.Connections.ShankLengthDiscretizationType@endlink) ShankLengthDiscretizationType
    ##  Returns the shank length discretization type   
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
         Returns the shank length discretization type   
            
         
        """
        pass
    
    ## Setter for property: (@link ShankLengthDiscretizationType NXOpen.CAE.Connections.ShankLengthDiscretizationType@endlink) ShankLengthDiscretizationType

    ##  Returns the shank length discretization type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    @ShankLengthDiscretizationType.setter
    def ShankLengthDiscretizationType(self, param: ShankLengthDiscretizationType):
        """
        Setter for property: (@link ShankLengthDiscretizationType NXOpen.CAE.Connections.ShankLengthDiscretizationType@endlink) ShankLengthDiscretizationType
         Returns the shank length discretization type   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ShankLengthPercentage
    ##  Returns the shank length percentage   
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
         Returns the shank length percentage   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ShankLengthUser
    ##  Returns the user specified shank length   
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
         Returns the user specified shank length   
            
         
        """
        pass
    
    ## Getter for property: (str) TableFile
    ##  Returns the table file used to compute the diameter   
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
         Returns the table file used to compute the diameter   
            
         
        """
        pass
    
    ## Setter for property: (str) TableFile

    ##  Returns the table file used to compute the diameter   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @TableFile.setter
    def TableFile(self, tableFile: str):
        """
        Setter for property: (str) TableFile
         Returns the table file used to compute the diameter   
            
         
        """
        pass
    
    ## Getter for property: (bool) UseMasterPointAsCenter
    ##  Returns the flag to use the master point as center   
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
         Returns the flag to use the master point as center   
            
         
        """
        pass
    
    ## Setter for property: (bool) UseMasterPointAsCenter

    ##  Returns the flag to use the master point as center   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    @UseMasterPointAsCenter.setter
    def UseMasterPointAsCenter(self, param: bool):
        """
        Setter for property: (bool) UseMasterPointAsCenter
         Returns the flag to use the master point as center   
            
         
        """
        pass
    
##  Bushing type 
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## Rectangular</term><description> 
##  Rectangular bushing type </description> </item><item><term> 
## Cylindrical</term><description> 
##  Cylindrical bushing type </description> </item></list>
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
    ##  Returns the bushing type   
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
         Returns the bushing type   
            
         
        """
        pass
    
    ## Setter for property: (@link BushingType NXOpen.CAE.Connections.BushingType@endlink) BushingType

    ##  Returns the bushing type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @BushingType.setter
    def BushingType(self, bushingType: BushingType):
        """
        Setter for property: (@link BushingType NXOpen.CAE.Connections.BushingType@endlink) BushingType
         Returns the bushing type   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) Csys
    ##  Returns the csys   
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
         Returns the csys   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) Csys

    ##  Returns the csys   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @Csys.setter
    def Csys(self, csys: NXOpen.CoordinateSystem):
        """
        Setter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) Csys
         Returns the csys   
            
         
        """
        pass
    
    ## Getter for property: (@link CsysType NXOpen.CAE.Connections.CsysType@endlink) CsysType
    ##  Returns the csys type   
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
         Returns the csys type   
            
         
        """
        pass
    
    ## Setter for property: (@link CsysType NXOpen.CAE.Connections.CsysType@endlink) CsysType

    ##  Returns the csys type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @CsysType.setter
    def CsysType(self, csysType: CsysType):
        """
        Setter for property: (@link CsysType NXOpen.CAE.Connections.CsysType@endlink) CsysType
         Returns the csys type   
            
         
        """
        pass
    
    ## Getter for property: (bool) IsMassOnBothTargets
    ##  Returns the isMassOnBothTargets   
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
         Returns the isMassOnBothTargets   
            
         
        """
        pass
    
    ## Setter for property: (bool) IsMassOnBothTargets

    ##  Returns the isMassOnBothTargets   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @IsMassOnBothTargets.setter
    def IsMassOnBothTargets(self, isMassOnBothTargets: bool):
        """
        Setter for property: (bool) IsMassOnBothTargets
         Returns the isMassOnBothTargets   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Mass
    ##  Returns the mass value   
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
         Returns the mass value   
            
         
        """
        pass
    
    ## Getter for property: (@link NodalPairingMethod NXOpen.CAE.Connections.NodalPairingMethod@endlink) PairingMethod
    ##  Returns the pairing method of targets   
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
         Returns the pairing method of targets   
            
         
        """
        pass
    
    ## Setter for property: (@link NodalPairingMethod NXOpen.CAE.Connections.NodalPairingMethod@endlink) PairingMethod

    ##  Returns the pairing method of targets   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @PairingMethod.setter
    def PairingMethod(self, method: NodalPairingMethod):
        """
        Setter for property: (@link NodalPairingMethod NXOpen.CAE.Connections.NodalPairingMethod@endlink) PairingMethod
         Returns the pairing method of targets   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RCylindricalStiffnessConstant
    ##  Returns the R cylindrical stiffness constant   
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
         Returns the R cylindrical stiffness constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RCylindricalStiffnessDynamic
    ##  Returns the R cylindrical stiffness dynamic   
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
         Returns the R cylindrical stiffness dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RCylindricalStiffnessDynamic

    ##  Returns the R cylindrical stiffness dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @RCylindricalStiffnessDynamic.setter
    def RCylindricalStiffnessDynamic(self, rDynamic: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RCylindricalStiffnessDynamic
         Returns the R cylindrical stiffness dynamic   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RCylindricalStructuralDampingConstant
    ##  Returns the R cylindrical structural damping constant   
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
         Returns the R cylindrical structural damping constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RCylindricalStructuralDampingDynamic
    ##  Returns the R cylindrical structural damping dynamic   
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
         Returns the R cylindrical structural damping dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RCylindricalStructuralDampingDynamic

    ##  Returns the R cylindrical structural damping dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @RCylindricalStructuralDampingDynamic.setter
    def RCylindricalStructuralDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RCylindricalStructuralDampingDynamic
         Returns the R cylindrical structural damping dynamic   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RCylindricalViscousDampingConstant
    ##  Returns the R cylindrical viscous damping constant   
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
         Returns the R cylindrical viscous damping constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RCylindricalViscousDampingDynamic
    ##  Returns the R cylindrical viscous damping dynamic   
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
         Returns the R cylindrical viscous damping dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RCylindricalViscousDampingDynamic

    ##  Returns the R cylindrical viscous damping dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @RCylindricalViscousDampingDynamic.setter
    def RCylindricalViscousDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RCylindricalViscousDampingDynamic
         Returns the R cylindrical viscous damping dynamic   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RNonlinearCylindricalDamping
    ##  Returns the R nonlinear cylindrical damping   
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
         Returns the R nonlinear cylindrical damping   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RNonlinearCylindricalDamping

    ##  Returns the R nonlinear cylindrical damping   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @RNonlinearCylindricalDamping.setter
    def RNonlinearCylindricalDamping(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RNonlinearCylindricalDamping
         Returns the R nonlinear cylindrical damping   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RNonlinearCylindricalStiffness
    ##  Returns the R nonlinear cylindrical stiffness   
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
         Returns the R nonlinear cylindrical stiffness   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RNonlinearCylindricalStiffness

    ##  Returns the R nonlinear cylindrical stiffness   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @RNonlinearCylindricalStiffness.setter
    def RNonlinearCylindricalStiffness(self, rDynamic: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RNonlinearCylindricalStiffness
         Returns the R nonlinear cylindrical stiffness   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RrCylindricalStiffnessConstant
    ##  Returns the RR cylindrical stiffness constant   
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
         Returns the RR cylindrical stiffness constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RrCylindricalStiffnessDynamic
    ##  Returns the RR cylindrical stiffness dynamic   
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
         Returns the RR cylindrical stiffness dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RrCylindricalStiffnessDynamic

    ##  Returns the RR cylindrical stiffness dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @RrCylindricalStiffnessDynamic.setter
    def RrCylindricalStiffnessDynamic(self, rrDynamic: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RrCylindricalStiffnessDynamic
         Returns the RR cylindrical stiffness dynamic   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RrCylindricalStructuralDampingConstant
    ##  Returns the RR structural damping constant   
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
         Returns the RR structural damping constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RrCylindricalStructuralDampingDynamic
    ##  Returns the RR cylindrical structural damping dynamic   
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
         Returns the RR cylindrical structural damping dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RrCylindricalStructuralDampingDynamic

    ##  Returns the RR cylindrical structural damping dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @RrCylindricalStructuralDampingDynamic.setter
    def RrCylindricalStructuralDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RrCylindricalStructuralDampingDynamic
         Returns the RR cylindrical structural damping dynamic   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RrCylindricalViscousDampingConstant
    ##  Returns the RR cylindrical viscous damping constant   
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
         Returns the RR cylindrical viscous damping constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RrCylindricalViscousDampingDynamic
    ##  Returns the RR cylindrical viscous damping dynamic   
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
         Returns the RR cylindrical viscous damping dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RrCylindricalViscousDampingDynamic

    ##  Returns the RR cylindrical viscous damping dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @RrCylindricalViscousDampingDynamic.setter
    def RrCylindricalViscousDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RrCylindricalViscousDampingDynamic
         Returns the RR cylindrical viscous damping dynamic   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RrNonlinearCylindricalDamping
    ##  Returns the RR nonlinear cylindrical damping   
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
         Returns the RR nonlinear cylindrical damping   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RrNonlinearCylindricalDamping

    ##  Returns the RR nonlinear cylindrical damping   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @RrNonlinearCylindricalDamping.setter
    def RrNonlinearCylindricalDamping(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RrNonlinearCylindricalDamping
         Returns the RR nonlinear cylindrical damping   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RrNonlinearCylindricalStiffness
    ##  Returns the RR nonlinear cylindrical stiffness   
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
         Returns the RR nonlinear cylindrical stiffness   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RrNonlinearCylindricalStiffness

    ##  Returns the RR nonlinear cylindrical stiffness   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @RrNonlinearCylindricalStiffness.setter
    def RrNonlinearCylindricalStiffness(self, rrDynamic: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RrNonlinearCylindricalStiffness
         Returns the RR nonlinear cylindrical stiffness   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RxNonlinearDamping
    ##  Returns the RX nonlinear damping   
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
         Returns the RX nonlinear damping   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RxNonlinearDamping

    ##  Returns the RX nonlinear damping   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @RxNonlinearDamping.setter
    def RxNonlinearDamping(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RxNonlinearDamping
         Returns the RX nonlinear damping   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RxNonlinearStiffness
    ##  Returns the RX nonlinear stiffness   
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
         Returns the RX nonlinear stiffness   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RxNonlinearStiffness

    ##  Returns the RX nonlinear stiffness   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @RxNonlinearStiffness.setter
    def RxNonlinearStiffness(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RxNonlinearStiffness
         Returns the RX nonlinear stiffness   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RxStiffnessConstant
    ##  Returns the RX stiffness constant   
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
         Returns the RX stiffness constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RxStiffnessDynamic
    ##  Returns the RX stiffness dynamic   
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
         Returns the RX stiffness dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RxStiffnessDynamic

    ##  Returns the RX stiffness dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @RxStiffnessDynamic.setter
    def RxStiffnessDynamic(self, rxDynamic: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RxStiffnessDynamic
         Returns the RX stiffness dynamic   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RxStructuralDampingConstant
    ##  Returns the RX structural damping constant   
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
         Returns the RX structural damping constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RxStructuralDampingDynamic
    ##  Returns the RX structural damping dynamic   
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
         Returns the RX structural damping dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RxStructuralDampingDynamic

    ##  Returns the RX structural damping dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @RxStructuralDampingDynamic.setter
    def RxStructuralDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RxStructuralDampingDynamic
         Returns the RX structural damping dynamic   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RxViscousDampingConstant
    ##  Returns the RX viscous damping constant   
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
         Returns the RX viscous damping constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RxViscousDampingDynamic
    ##  Returns the RX viscous damping dynamic   
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
         Returns the RX viscous damping dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RxViscousDampingDynamic

    ##  Returns the RX viscous damping dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @RxViscousDampingDynamic.setter
    def RxViscousDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RxViscousDampingDynamic
         Returns the RX viscous damping dynamic   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RyNonlinearDamping
    ##  Returns the RY nonlinear damping   
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
         Returns the RY nonlinear damping   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RyNonlinearDamping

    ##  Returns the RY nonlinear damping   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @RyNonlinearDamping.setter
    def RyNonlinearDamping(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RyNonlinearDamping
         Returns the RY nonlinear damping   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RyNonlinearStiffness
    ##  Returns the RY nonlinear stiffness   
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
         Returns the RY nonlinear stiffness   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RyNonlinearStiffness

    ##  Returns the RY nonlinear stiffness   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @RyNonlinearStiffness.setter
    def RyNonlinearStiffness(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RyNonlinearStiffness
         Returns the RY nonlinear stiffness   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RyStiffnessConstant
    ##  Returns the RY stiffness constant   
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
         Returns the RY stiffness constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RyStiffnessDynamic
    ##  Returns the RY stiffness dynamic   
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
         Returns the RY stiffness dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RyStiffnessDynamic

    ##  Returns the RY stiffness dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @RyStiffnessDynamic.setter
    def RyStiffnessDynamic(self, ryDynamic: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RyStiffnessDynamic
         Returns the RY stiffness dynamic   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RyStructuralDampingConstant
    ##  Returns the RY structural damping constant   
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
         Returns the RY structural damping constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RyStructuralDampingDynamic
    ##  Returns the RY structural damping dynamic   
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
         Returns the RY structural damping dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RyStructuralDampingDynamic

    ##  Returns the RY structural damping dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @RyStructuralDampingDynamic.setter
    def RyStructuralDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RyStructuralDampingDynamic
         Returns the RY structural damping dynamic   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RyViscousDampingConstant
    ##  Returns the RY viscous damping constant   
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
         Returns the RY viscous damping constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RyViscousDampingDynamic
    ##  Returns the RY viscous damping dynamic   
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
         Returns the RY viscous damping dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RyViscousDampingDynamic

    ##  Returns the RY viscous damping dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @RyViscousDampingDynamic.setter
    def RyViscousDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RyViscousDampingDynamic
         Returns the RY viscous damping dynamic   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RzCylindricalStiffnessConstant
    ##  Returns the RZ cylindrical stiffness constant   
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
         Returns the RZ cylindrical stiffness constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzCylindricalStiffnessDynamic
    ##  Returns the RZ cylindrical stiffness dynamic   
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
         Returns the RZ cylindrical stiffness dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzCylindricalStiffnessDynamic

    ##  Returns the RZ cylindrical stiffness dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @RzCylindricalStiffnessDynamic.setter
    def RzCylindricalStiffnessDynamic(self, rzDynamic: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzCylindricalStiffnessDynamic
         Returns the RZ cylindrical stiffness dynamic   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RzCylindricalStructuralDampingConstant
    ##  Returns the RZ structural damping constant   
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
         Returns the RZ structural damping constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzCylindricalStructuralDampingDynamic
    ##  Returns the RZ cylindrical structural damping dynamic   
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
         Returns the RZ cylindrical structural damping dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzCylindricalStructuralDampingDynamic

    ##  Returns the RZ cylindrical structural damping dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @RzCylindricalStructuralDampingDynamic.setter
    def RzCylindricalStructuralDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzCylindricalStructuralDampingDynamic
         Returns the RZ cylindrical structural damping dynamic   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RzCylindricalViscousDampingConstant
    ##  Returns the RZ cylindrical viscous damping constant   
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
         Returns the RZ cylindrical viscous damping constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzCylindricalViscousDampingDynamic
    ##  Returns the RZ cylindrical viscous damping dynamic   
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
         Returns the RZ cylindrical viscous damping dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzCylindricalViscousDampingDynamic

    ##  Returns the RZ cylindrical viscous damping dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @RzCylindricalViscousDampingDynamic.setter
    def RzCylindricalViscousDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzCylindricalViscousDampingDynamic
         Returns the RZ cylindrical viscous damping dynamic   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzNonlinearCylindricalDamping
    ##  Returns the RZ nonlinear cylindrical damping   
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
         Returns the RZ nonlinear cylindrical damping   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzNonlinearCylindricalDamping

    ##  Returns the RZ nonlinear cylindrical damping   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @RzNonlinearCylindricalDamping.setter
    def RzNonlinearCylindricalDamping(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzNonlinearCylindricalDamping
         Returns the RZ nonlinear cylindrical damping   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzNonlinearCylindricalStiffness
    ##  Returns the RZ nonlinear cylindrical stiffness   
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
         Returns the RZ nonlinear cylindrical stiffness   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzNonlinearCylindricalStiffness

    ##  Returns the RZ nonlinear cylindrical stiffness   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @RzNonlinearCylindricalStiffness.setter
    def RzNonlinearCylindricalStiffness(self, rzDynamic: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzNonlinearCylindricalStiffness
         Returns the RZ nonlinear cylindrical stiffness   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzNonlinearDamping
    ##  Returns the RZ nonlinear damping   
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
         Returns the RZ nonlinear damping   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzNonlinearDamping

    ##  Returns the RZ nonlinear damping   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @RzNonlinearDamping.setter
    def RzNonlinearDamping(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzNonlinearDamping
         Returns the RZ nonlinear damping   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzNonlinearStiffness
    ##  Returns the RZ nonlinear stiffness   
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
         Returns the RZ nonlinear stiffness   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzNonlinearStiffness

    ##  Returns the RZ nonlinear stiffness   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @RzNonlinearStiffness.setter
    def RzNonlinearStiffness(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzNonlinearStiffness
         Returns the RZ nonlinear stiffness   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RzStiffnessConstant
    ##  Returns the RZ stiffness constant   
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
         Returns the RZ stiffness constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzStiffnessDynamic
    ##  Returns the RZ stiffness dynamic   
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
         Returns the RZ stiffness dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzStiffnessDynamic

    ##  Returns the RZ stiffness dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @RzStiffnessDynamic.setter
    def RzStiffnessDynamic(self, rzDynamic: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzStiffnessDynamic
         Returns the RZ stiffness dynamic   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RzStructuralDampingConstant
    ##  Returns the RZ structural damping constant   
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
         Returns the RZ structural damping constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzStructuralDampingDynamic
    ##  Returns the RZ structural damping dynamic   
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
         Returns the RZ structural damping dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzStructuralDampingDynamic

    ##  Returns the RZ structural damping dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @RzStructuralDampingDynamic.setter
    def RzStructuralDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzStructuralDampingDynamic
         Returns the RZ structural damping dynamic   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RzViscousDampingConstant
    ##  Returns the RZ viscous damping constant   
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
         Returns the RZ viscous damping constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzViscousDampingDynamic
    ##  Returns the RZ viscous damping dynamic   
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
         Returns the RZ viscous damping dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzViscousDampingDynamic

    ##  Returns the RZ viscous damping dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @RzViscousDampingDynamic.setter
    def RzViscousDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzViscousDampingDynamic
         Returns the RZ viscous damping dynamic   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) SearchConeAngle
    ##  Returns the search cone angle   
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
         Returns the search cone angle   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) SearchOrientation
    ##  Returns the pairing search orientation   
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
         Returns the pairing search orientation   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) SearchOrientation

    ##  Returns the pairing search orientation   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @SearchOrientation.setter
    def SearchOrientation(self, orientation: NXOpen.Direction):
        """
        Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) SearchOrientation
         Returns the pairing search orientation   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) SearchRange
    ##  Returns the search range   
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
         Returns the search range   
            
         
        """
        pass
    
    ## Getter for property: (@link StiffnessType NXOpen.CAE.Connections.StiffnessType@endlink) StiffnessType
    ##  Returns the stiffness type   
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
         Returns the stiffness type   
            
         
        """
        pass
    
    ## Setter for property: (@link StiffnessType NXOpen.CAE.Connections.StiffnessType@endlink) StiffnessType

    ##  Returns the stiffness type   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @StiffnessType.setter
    def StiffnessType(self, oStiffnessType: StiffnessType):
        """
        Setter for property: (@link StiffnessType NXOpen.CAE.Connections.StiffnessType@endlink) StiffnessType
         Returns the stiffness type   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) XNonlinearDamping
    ##  Returns the X nonlinear damping   
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
         Returns the X nonlinear damping   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) XNonlinearDamping

    ##  Returns the X nonlinear damping   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @XNonlinearDamping.setter
    def XNonlinearDamping(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) XNonlinearDamping
         Returns the X nonlinear damping   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) XNonlinearStiffness
    ##  Returns the X nonlinear stiffness   
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
         Returns the X nonlinear stiffness   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) XNonlinearStiffness

    ##  Returns the X nonlinear stiffness   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @XNonlinearStiffness.setter
    def XNonlinearStiffness(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) XNonlinearStiffness
         Returns the X nonlinear stiffness   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) XStiffnessConstant
    ##  Returns the X stiffness constant   
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
         Returns the X stiffness constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) XStiffnessDynamic
    ##  Returns the X stiffness dynamic   
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
         Returns the X stiffness dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) XStiffnessDynamic

    ##  Returns the X stiffness dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @XStiffnessDynamic.setter
    def XStiffnessDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) XStiffnessDynamic
         Returns the X stiffness dynamic   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) XStructuralDampingConstant
    ##  Returns the X structural damping constant   
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
         Returns the X structural damping constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) XStructuralDampingDynamic
    ##  Returns the X structural damping dynamic   
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
         Returns the X structural damping dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) XStructuralDampingDynamic

    ##  Returns the X structural damping dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @XStructuralDampingDynamic.setter
    def XStructuralDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) XStructuralDampingDynamic
         Returns the X structural damping dynamic   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) XViscousDampingConstant
    ##  Returns the X viscous damping constant   
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
         Returns the X viscous damping constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) XViscousDampingDynamic
    ##  Returns the X viscous damping dynamic   
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
         Returns the X viscous damping dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) XViscousDampingDynamic

    ##  Returns the X viscous damping dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @XViscousDampingDynamic.setter
    def XViscousDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) XViscousDampingDynamic
         Returns the X viscous damping dynamic   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) YNonlinearDamping
    ##  Returns the Y nonlinear damping   
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
         Returns the Y nonlinear damping   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) YNonlinearDamping

    ##  Returns the Y nonlinear damping   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @YNonlinearDamping.setter
    def YNonlinearDamping(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) YNonlinearDamping
         Returns the Y nonlinear damping   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) YNonlinearStiffness
    ##  Returns the Y nonlinear stiffness   
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
         Returns the Y nonlinear stiffness   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) YNonlinearStiffness

    ##  Returns the Y nonlinear stiffness   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @YNonlinearStiffness.setter
    def YNonlinearStiffness(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) YNonlinearStiffness
         Returns the Y nonlinear stiffness   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) YStiffnessConstant
    ##  Returns the Y stiffness constant   
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
         Returns the Y stiffness constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) YStiffnessDynamic
    ##  Returns the Y stiffness dynamic   
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
         Returns the Y stiffness dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) YStiffnessDynamic

    ##  Returns the Y stiffness dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @YStiffnessDynamic.setter
    def YStiffnessDynamic(self, yDynamic: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) YStiffnessDynamic
         Returns the Y stiffness dynamic   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) YStructuralDampingConstant
    ##  Returns the Y structural damping constant   
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
         Returns the Y structural damping constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) YStructuralDampingDynamic
    ##  Returns the Y structural damping dynamic   
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
         Returns the Y structural damping dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) YStructuralDampingDynamic

    ##  Returns the Y structural damping dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @YStructuralDampingDynamic.setter
    def YStructuralDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) YStructuralDampingDynamic
         Returns the Y structural damping dynamic   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) YViscousDampingConstant
    ##  Returns the Y viscous damping constant   
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
         Returns the Y viscous damping constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) YViscousDampingDynamic
    ##  Returns the Y viscous damping dynamic   
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
         Returns the Y viscous damping dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) YViscousDampingDynamic

    ##  Returns the Y viscous damping dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @YViscousDampingDynamic.setter
    def YViscousDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) YViscousDampingDynamic
         Returns the Y viscous damping dynamic   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ZCylindricalStiffnessConstant
    ##  Returns the Z cylindrical stiffness constant   
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
         Returns the Z cylindrical stiffness constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZCylindricalStiffnessDynamic
    ##  Returns the Z cylindrical stiffness dynamic   
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
         Returns the Z cylindrical stiffness dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZCylindricalStiffnessDynamic

    ##  Returns the Z cylindrical stiffness dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @ZCylindricalStiffnessDynamic.setter
    def ZCylindricalStiffnessDynamic(self, zDynamic: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZCylindricalStiffnessDynamic
         Returns the Z cylindrical stiffness dynamic   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ZCylindricalStructuralDampingConstant
    ##  Returns the Z cylindrical structural damping constant   
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
         Returns the Z cylindrical structural damping constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZCylindricalStructuralDampingDynamic
    ##  Returns the Z cylindrical structural damping dynamic   
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
         Returns the Z cylindrical structural damping dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZCylindricalStructuralDampingDynamic

    ##  Returns the Z cylindrical structural damping dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @ZCylindricalStructuralDampingDynamic.setter
    def ZCylindricalStructuralDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZCylindricalStructuralDampingDynamic
         Returns the Z cylindrical structural damping dynamic   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ZCylindricalViscousDampingConstant
    ##  Returns the Z cylindrical viscous damping constant   
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
         Returns the Z cylindrical viscous damping constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZCylindricalViscousDampingDynamic
    ##  Returns the Z cylindrical viscous damping dynamic   
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
         Returns the Z cylindrical viscous damping dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZCylindricalViscousDampingDynamic

    ##  Returns the Z cylindrical viscous damping dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @ZCylindricalViscousDampingDynamic.setter
    def ZCylindricalViscousDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZCylindricalViscousDampingDynamic
         Returns the Z cylindrical viscous damping dynamic   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZNonlinearCylindricalDamping
    ##  Returns the Z nonlinear cylindrical damping   
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
         Returns the Z nonlinear cylindrical damping   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZNonlinearCylindricalDamping

    ##  Returns the Z nonlinear cylindrical damping   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @ZNonlinearCylindricalDamping.setter
    def ZNonlinearCylindricalDamping(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZNonlinearCylindricalDamping
         Returns the Z nonlinear cylindrical damping   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZNonlinearCylindricalStiffness
    ##  Returns the Z nonlinear cylindrical stiffness   
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
         Returns the Z nonlinear cylindrical stiffness   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZNonlinearCylindricalStiffness

    ##  Returns the Z nonlinear cylindrical stiffness   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @ZNonlinearCylindricalStiffness.setter
    def ZNonlinearCylindricalStiffness(self, zDynamic: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZNonlinearCylindricalStiffness
         Returns the Z nonlinear cylindrical stiffness   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZNonlinearDamping
    ##  Returns the Z nonlinear damping   
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
         Returns the Z nonlinear damping   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZNonlinearDamping

    ##  Returns the Z nonlinear damping   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @ZNonlinearDamping.setter
    def ZNonlinearDamping(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZNonlinearDamping
         Returns the Z nonlinear damping   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZNonlinearStiffness
    ##  Returns the Z nonlinear stiffness   
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
         Returns the Z nonlinear stiffness   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZNonlinearStiffness

    ##  Returns the Z nonlinear stiffness   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @ZNonlinearStiffness.setter
    def ZNonlinearStiffness(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZNonlinearStiffness
         Returns the Z nonlinear stiffness   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ZStiffnessConstant
    ##  Returns the Z stiffness constant   
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
         Returns the Z stiffness constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZStiffnessDynamic
    ##  Returns the Z stiffness dynamic   
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
         Returns the Z stiffness dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZStiffnessDynamic

    ##  Returns the Z stiffness dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @ZStiffnessDynamic.setter
    def ZStiffnessDynamic(self, zDynamic: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZStiffnessDynamic
         Returns the Z stiffness dynamic   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ZStructuralDampingConstant
    ##  Returns the Z structural damping constant   
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
         Returns the Z structural damping constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZStructuralDampingDynamic
    ##  Returns the Z structural damping dynamic   
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
         Returns the Z structural damping dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZStructuralDampingDynamic

    ##  Returns the Z structural damping dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @ZStructuralDampingDynamic.setter
    def ZStructuralDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZStructuralDampingDynamic
         Returns the Z structural damping dynamic   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ZViscousDampingConstant
    ##  Returns the Z viscous damping constant   
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
         Returns the Z viscous damping constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZViscousDampingDynamic
    ##  Returns the Z viscous damping dynamic   
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
         Returns the Z viscous damping dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZViscousDampingDynamic

    ##  Returns the Z viscous damping dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @ZViscousDampingDynamic.setter
    def ZViscousDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZViscousDampingDynamic
         Returns the Z viscous damping dynamic   
            
         
        """
        pass
    
##  CAD Components Load Type 
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## AllParts</term><description> 
##  Full loading of all CAD components </description> </item><item><term> 
## MainAssociatedPartsOnly</term><description> 
##  Full loading of the main associated CAD components </description> </item></list>
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
    ##  Returns the coefficient for formula defined diameter   
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
         Returns the coefficient for formula defined diameter   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Diameter
    ##  Returns the connection diameter   
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
         Returns the connection diameter   
            
         
        """
        pass
    
    ## Getter for property: (@link DiameterType NXOpen.CAE.Connections.DiameterType@endlink) DiameterType
    ##  Returns the connection diameter type   
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
         Returns the connection diameter type   
            
         
        """
        pass
    
    ## Setter for property: (@link DiameterType NXOpen.CAE.Connections.DiameterType@endlink) DiameterType

    ##  Returns the connection diameter type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @DiameterType.setter
    def DiameterType(self, diameterType: DiameterType):
        """
        Setter for property: (@link DiameterType NXOpen.CAE.Connections.DiameterType@endlink) DiameterType
         Returns the connection diameter type   
            
         
        """
        pass
    
    ## Getter for property: (@link DiscretizationMethod NXOpen.CAE.Connections.DiscretizationMethod@endlink) DiscretizationMethod
    ##  Returns the discretization method   
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
         Returns the discretization method   
            
         
        """
        pass
    
    ## Setter for property: (@link DiscretizationMethod NXOpen.CAE.Connections.DiscretizationMethod@endlink) DiscretizationMethod

    ##  Returns the discretization method   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @DiscretizationMethod.setter
    def DiscretizationMethod(self, method: DiscretizationMethod):
        """
        Setter for property: (@link DiscretizationMethod NXOpen.CAE.Connections.DiscretizationMethod@endlink) DiscretizationMethod
         Returns the discretization method   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) DistanceFromStart
    ##  Returns the line Discretization distance from start   
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
         Returns the line Discretization distance from start   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) DistanceToEnd
    ##  Returns the line Discretization distance to end   
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
         Returns the line Discretization distance to end   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Height
    ##  Returns the height value   
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
         Returns the height value   
            
         
        """
        pass
    
    ## Getter for property: (@link HeightType NXOpen.CAE.Connections.HeightType@endlink) HeightType
    ##  Returns the connection height type   
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
         Returns the connection height type   
            
         
        """
        pass
    
    ## Setter for property: (@link HeightType NXOpen.CAE.Connections.HeightType@endlink) HeightType

    ##  Returns the connection height type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @HeightType.setter
    def HeightType(self, heightType: HeightType):
        """
        Setter for property: (@link HeightType NXOpen.CAE.Connections.HeightType@endlink) HeightType
         Returns the connection height type   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) LengthStep
    ##  Returns the line Discretization length step   
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
         Returns the line Discretization length step   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.PhysicalMaterial NXOpen.PhysicalMaterial@endlink) Material
    ##  Returns the connection material   
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
         Returns the connection material   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.PhysicalMaterial NXOpen.PhysicalMaterial@endlink) Material

    ##  Returns the connection material   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @Material.setter
    def Material(self, material: NXOpen.PhysicalMaterial):
        """
        Setter for property: (@link NXOpen.PhysicalMaterial NXOpen.PhysicalMaterial@endlink) Material
         Returns the connection material   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxAngleBetweenNormals
    ##  Returns the maximum angle of normals with the projection surface   
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
         Returns the maximum angle of normals with the projection surface   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxDistCGToElemCG
    ##  Returns the maximum distance from definition point to center of support element   
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
         Returns the maximum distance from definition point to center of support element   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxLengthStep
    ##  Returns the line Discretization max length step   
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
         Returns the line Discretization max length step   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxNormalDistCGToFlanges
    ##  Returns the maximum normal distance from definition point to center of element   
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
         Returns the maximum normal distance from definition point to center of element   
            
         
        """
        pass
    
    ## Getter for property: (int) NumberOfDiscretizationPoints
    ##  Returns the number of connections   
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
         Returns the number of connections   
            
         
        """
        pass
    
    ## Setter for property: (int) NumberOfDiscretizationPoints

    ##  Returns the number of connections   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @NumberOfDiscretizationPoints.setter
    def NumberOfDiscretizationPoints(self, num: int):
        """
        Setter for property: (int) NumberOfDiscretizationPoints
         Returns the number of connections   
            
         
        """
        pass
    
    ## Getter for property: (int) NumberOfFlanges
    ##  Returns the number of flanges.  
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
         Returns the number of flanges.  
           When changing the number of flanges this is not applied till an update is performed by calling @link Update::DoUpdate Update::DoUpdate@endlink    
         
        """
        pass
    
    ## Setter for property: (int) NumberOfFlanges

    ##  Returns the number of flanges.  
    ##    When changing the number of flanges this is not applied till an update is performed by calling @link Update::DoUpdate Update::DoUpdate@endlink    
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @NumberOfFlanges.setter
    def NumberOfFlanges(self, numberOfFlanges: int):
        """
        Setter for property: (int) NumberOfFlanges
         Returns the number of flanges.  
           When changing the number of flanges this is not applied till an update is performed by calling @link Update::DoUpdate Update::DoUpdate@endlink    
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ProjectTolerance
    ##  Returns the projection tolerance   
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
         Returns the projection tolerance   
            
         
        """
        pass
    
    ## Getter for property: (str) TableFile
    ##  Returns the table file used to compute the diameter   
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
         Returns the table file used to compute the diameter   
            
         
        """
        pass
    
    ## Setter for property: (str) TableFile

    ##  Returns the table file used to compute the diameter   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @TableFile.setter
    def TableFile(self, tableFile: str):
        """
        Setter for property: (str) TableFile
         Returns the table file used to compute the diameter   
            
         
        """
        pass
    
    ## Getter for property: (bool) UseMaxLengthStep
    ##  Returns the usage of max length step   
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
         Returns the usage of max length step   
            
         
        """
        pass
    
    ## Setter for property: (bool) UseMaxLengthStep

    ##  Returns the usage of max length step   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @UseMaxLengthStep.setter
    def UseMaxLengthStep(self, use: bool):
        """
        Setter for property: (bool) UseMaxLengthStep
         Returns the usage of max length step   
            
         
        """
        pass
    
    ## Getter for property: (bool) UseOriginalNodesOfConnection
    ##  Returns the usage of original nodes of connection   
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
         Returns the usage of original nodes of connection   
            
         
        """
        pass
    
    ## Setter for property: (bool) UseOriginalNodesOfConnection

    ##  Returns the usage of original nodes of connection   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @UseOriginalNodesOfConnection.setter
    def UseOriginalNodesOfConnection(self, use: bool):
        """
        Setter for property: (bool) UseOriginalNodesOfConnection
         Returns the usage of original nodes of connection   
            
         
        """
        pass
    
import NXOpen
##  Composer connection. Use this interface to set/get properties and parameters of the spot weld connection.  
## 
##   <br>  Created in NX12.0.0  <br> 

class ComponentData(NXOpen.TaggedObject): 
    """ Composer connection. Use this interface to set/get properties and parameters of the spot weld connection.  """


    ## Getter for property: (str) ComponentName
    ##  Returns the component name    
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
         Returns the component name    
            
         
        """
        pass
    
    ## Setter for property: (str) ComponentName

    ##  Returns the component name    
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @ComponentName.setter
    def ComponentName(self, name: str):
        """
        Setter for property: (str) ComponentName
         Returns the component name    
            
         
        """
        pass
    
    ## Getter for property: (str) ConnectionPointsPath
    ##  Returns the connection points path    
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
         Returns the connection points path    
            
         
        """
        pass
    
    ## Setter for property: (str) ConnectionPointsPath

    ##  Returns the connection points path    
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @ConnectionPointsPath.setter
    def ConnectionPointsPath(self, connectionPointsPath: str):
        """
        Setter for property: (str) ConnectionPointsPath
         Returns the connection points path    
            
         
        """
        pass
    
    ## Getter for property: (str) FilePath
    ##  Returns the file path    
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
         Returns the file path    
            
         
        """
        pass
    
    ## Setter for property: (str) FilePath

    ##  Returns the file path    
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @FilePath.setter
    def FilePath(self, path: str):
        """
        Setter for property: (str) FilePath
         Returns the file path    
            
         
        """
        pass
    
    ## Getter for property: (str) ImportedConnectionPointsPath
    ##  Returns the imported connection points path    
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
         Returns the imported connection points path    
            
         
        """
        pass
    
    ## Setter for property: (str) ImportedConnectionPointsPath

    ##  Returns the imported connection points path    
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @ImportedConnectionPointsPath.setter
    def ImportedConnectionPointsPath(self, importedConnPointsPath: str):
        """
        Setter for property: (str) ImportedConnectionPointsPath
         Returns the imported connection points path    
            
         
        """
        pass
    
    ## Getter for property: (str) MeshPath
    ##  Returns the mesh path    
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
         Returns the mesh path    
            
         
        """
        pass
    
    ## Setter for property: (str) MeshPath

    ##  Returns the mesh path    
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @MeshPath.setter
    def MeshPath(self, meshPath: str):
        """
        Setter for property: (str) MeshPath
         Returns the mesh path    
            
         
        """
        pass
    
    ## Getter for property: (str) RepresentationFilePath
    ##  Returns the component representation path    
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
         Returns the component representation path    
            
         
        """
        pass
    
    ## Setter for property: (str) RepresentationFilePath

    ##  Returns the component representation path    
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @RepresentationFilePath.setter
    def RepresentationFilePath(self, representationTypeFilePath: str):
        """
        Setter for property: (str) RepresentationFilePath
         Returns the component representation path    
            
         
        """
        pass
    
    ## Getter for property: (str) RepresentationType
    ##  Returns the component Representation Type    
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
         Returns the component Representation Type    
            
         
        """
        pass
    
    ## Setter for property: (str) RepresentationType

    ##  Returns the component Representation Type    
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @RepresentationType.setter
    def RepresentationType(self, representationType: str):
        """
        Setter for property: (str) RepresentationType
         Returns the component Representation Type    
            
         
        """
        pass
    
    ## Getter for property: (str) SolverType
    ##  Returns the component Solver Type    
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
         Returns the component Solver Type    
            
         
        """
        pass
    
    ## Setter for property: (str) SolverType

    ##  Returns the component Solver Type    
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @SolverType.setter
    def SolverType(self, solverType: str):
        """
        Setter for property: (str) SolverType
         Returns the component Solver Type    
            
         
        """
        pass
    
##  composer Connection type 
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## NotSet</term><description> 
##  None </description> </item><item><term> 
## Bolt</term><description> 
##  Bolt </description> </item><item><term> 
## Spring</term><description> 
##  Spring </description> </item><item><term> 
## Latch</term><description> 
##  Latch </description> </item><item><term> 
## Bushing</term><description> 
##  Bushing </description> </item><item><term> 
## BumpStop</term><description> 
##  BumpStop </description> </item><item><term> 
## Kinematic</term><description> 
##  Kinematic </description> </item><item><term> 
## WeatherStrip</term><description> 
##  WeatherStrip </description> </item><item><term> 
## SeamWeld</term><description> 
##  SeamWeld </description> </item><item><term> 
## Adhesive</term><description> 
##  Adhesive </description> </item><item><term> 
## SpotWeld</term><description> 
##  SpotWeld </description> </item><item><term> 
## Bar</term><description> 
##  Bar </description> </item></list>
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
    ##  Returns the assembly name    
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
         Returns the assembly name    
            
         
        """
        pass
    
    ## Setter for property: (str) AssemblyName

    ##  Returns the assembly name    
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @AssemblyName.setter
    def AssemblyName(self, assemblyName: str):
        """
        Setter for property: (str) AssemblyName
         Returns the assembly name    
            
         
        """
        pass
    
    ## Getter for property: (str) ComponentUnitSystem
    ##  Returns the component unit system    
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
         Returns the component unit system    
            
         
        """
        pass
    
    ## Setter for property: (str) ComponentUnitSystem

    ##  Returns the component unit system    
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @ComponentUnitSystem.setter
    def ComponentUnitSystem(self, componentUnitSystem: str):
        """
        Setter for property: (str) ComponentUnitSystem
         Returns the component unit system    
            
         
        """
        pass
    
    ## Getter for property: (str) InputFileDir
    ##  Returns the input file direction    
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
         Returns the input file direction    
            
         
        """
        pass
    
    ## Setter for property: (str) InputFileDir

    ##  Returns the input file direction    
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @InputFileDir.setter
    def InputFileDir(self, inputFileDir: str):
        """
        Setter for property: (str) InputFileDir
         Returns the input file direction    
            
         
        """
        pass
    
    ## Getter for property: (str) MaterialDBDir
    ##  Returns the material file direction    
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
         Returns the material file direction    
            
         
        """
        pass
    
    ## Setter for property: (str) MaterialDBDir

    ##  Returns the material file direction    
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @MaterialDBDir.setter
    def MaterialDBDir(self, materialDBDir: str):
        """
        Setter for property: (str) MaterialDBDir
         Returns the material file direction    
            
         
        """
        pass
    
    ## Getter for property: (str) OutputFileDir
    ##  Returns the output file direction    
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
         Returns the output file direction    
            
         
        """
        pass
    
    ## Setter for property: (str) OutputFileDir

    ##  Returns the output file direction    
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @OutputFileDir.setter
    def OutputFileDir(self, outputFileDir: str):
        """
        Setter for property: (str) OutputFileDir
         Returns the output file direction    
            
         
        """
        pass
    
    ## Getter for property: (int) StartNumAxisSystems
    ##  Returns the start axis number    
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
         Returns the start axis number    
            
         
        """
        pass
    
    ## Setter for property: (int) StartNumAxisSystems

    ##  Returns the start axis number    
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @StartNumAxisSystems.setter
    def StartNumAxisSystems(self, startNumAxisSystems: int):
        """
        Setter for property: (int) StartNumAxisSystems
         Returns the start axis number    
            
         
        """
        pass
    
    ## Getter for property: (int) StartNumNodeAndElement
    ##  Returns the start node and element number    
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
         Returns the start node and element number    
            
         
        """
        pass
    
    ## Setter for property: (int) StartNumNodeAndElement

    ##  Returns the start node and element number    
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @StartNumNodeAndElement.setter
    def StartNumNodeAndElement(self, startNumNodeAndElement: int):
        """
        Setter for property: (int) StartNumNodeAndElement
         Returns the start node and element number    
            
         
        """
        pass
    
    ## Getter for property: (int) StartNumProperties
    ##  Returns the start properties number    
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
         Returns the start properties number    
            
         
        """
        pass
    
    ## Setter for property: (int) StartNumProperties

    ##  Returns the start properties number    
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @StartNumProperties.setter
    def StartNumProperties(self, startNumProperties: int):
        """
        Setter for property: (int) StartNumProperties
         Returns the start properties number    
            
         
        """
        pass
    
    ##  Create component. 
    ##  @return component (@link ComponentData NXOpen.CAE.Connections.ComponentData@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    def CreateComponent(self) -> ComponentData:
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
    def CreateConnection(self) -> ConnectionData:
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
    def GetComponents(self) -> List[ComponentData]:
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
    def GetConnections(self) -> List[ConnectionData]:
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
    def SetComponents(self, components: List[ComponentData]) -> None:
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
    def SetConnections(self, connections: List[ConnectionData]) -> None:
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
    ##  Returns the composer data    
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
         Returns the composer data    
            
         
        """
        pass
    
    ## Setter for property: (@link ComposerData NXOpen.CAE.Connections.ComposerData@endlink) ComposerData

    ##  Returns the composer data    
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @ComposerData.setter
    def ComposerData(self, composerData: ComposerData):
        """
        Setter for property: (@link ComposerData NXOpen.CAE.Connections.ComposerData@endlink) ComposerData
         Returns the composer data    
            
         
        """
        pass
    
    ## Getter for property: (@link ConnectionDBData NXOpen.CAE.Connections.ConnectionDBData@endlink) ConnectionDBData
    ##  Returns the connection db data    
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
         Returns the connection db data    
            
         
        """
        pass
    
    ## Setter for property: (@link ConnectionDBData NXOpen.CAE.Connections.ConnectionDBData@endlink) ConnectionDBData

    ##  Returns the connection db data    
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @ConnectionDBData.setter
    def ConnectionDBData(self, connectionDBData: ConnectionDBData):
        """
        Setter for property: (@link ConnectionDBData NXOpen.CAE.Connections.ConnectionDBData@endlink) ConnectionDBData
         Returns the connection db data    
            
         
        """
        pass
    
    ##  CheckAssemblyConnections  
    ##  @return results (List[str]): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    def CheckAssemblyConnections(self) -> List[str]:
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
    def CheckAssemblyDocumentConnections(self, documentName: str) -> List[str]:
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
    def CreateComposerData(self) -> ComposerData:
        """
         Create composer data. 
         @return composerData (@link ComposerData NXOpen.CAE.Connections.ComposerData@endlink): .
        """
        pass
    
    ##  Destroy the composer object 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer") OR sc_gso_creation (" Simcenter GSO BIW Creation environment") OR nx_masterfem ("Finite Element Modeling")
    def Destroy(self) -> None:
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
    def ExportHardPointToXml(self, tWorkPart: NXOpen.CAE.CaePart, tUnit: NXOpen.Unit, file: str) -> None:
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
    def GetAxisFromAlias(self, axisAlias: str) -> List[NXOpen.CoordinateSystem]:
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
    def GetLumpedMassData(self) -> List[LMIEConnection]:
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
    def GetMaterialsData(self, inputBdfFilePath: str) -> List[str]:
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
    def GetMeshPartFromPID(self, pid: int) -> List[NXOpen.TaggedObject]:
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
    def GetMeshPartInContextFromPID(self, tWorkPart: NXOpen.CAE.CaePart, pid: int) -> List[NXOpen.TaggedObject]:
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
    def ImportAndModifyHardPointLabel(self, tWorkPart: NXOpen.CAE.CaePart, file: str) -> List[NXOpen.CAE.SelectionRecipe]:
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
    ## 
    ## <param name="tWorkPart"> (@link NXOpen.CAE.CaePart NXOpen.CAE.CaePart@endlink)  I - The work part tag </param>
    ## <param name="file"> (str)  The XML file name </param>
    ## <param name="isUpdate"> (bool)  Flag to specify the status of update </param>
    def ImportAndUpdateHardPointFromXml(self, tWorkPart: NXOpen.CAE.CaePart, file: str, isUpdate: bool) -> Tuple[List[NXOpen.CAE.SelectionRecipe], List[NXOpen.CAE.SelectionRecipe]]:
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
    def MigrateToHardPointFile(self, file: str) -> None:
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
    def ReadAssemblyDefinition(self, filePath: str) -> None:
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
    def ReadConnectionsDB(self, filePath: str) -> None:
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
    def SearchBoltComponentAndPIDs(self, documentName: str) -> List[str]:
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
    def SearchPIDs(self, documentName: str) -> Tuple[bool, List[str], List[str]]:
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
    ## 
    ## <param name="iConnections"> (@link LMIEConnection List[NXOpen.CAE.Connections.LMIEConnection]@endlink)  The intermediate connection representations </param>
    def SetLumpedMassData(self, iConnections: List[LMIEConnection]) -> None:
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
    def WriteAssemblyDefinition(self, filePath: str) -> None:
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
    ##  Returns the comp1    
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
         Returns the comp1    
            
         
        """
        pass
    
    ## Setter for property: (@link ComponentData NXOpen.CAE.Connections.ComponentData@endlink) Comp1

    ##  Returns the comp1    
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @Comp1.setter
    def Comp1(self, comp1: ComponentData):
        """
        Setter for property: (@link ComponentData NXOpen.CAE.Connections.ComponentData@endlink) Comp1
         Returns the comp1    
            
         
        """
        pass
    
    ## Getter for property: (@link ComponentData NXOpen.CAE.Connections.ComponentData@endlink) Comp2
    ##  Returns the comp2    
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
         Returns the comp2    
            
         
        """
        pass
    
    ## Setter for property: (@link ComponentData NXOpen.CAE.Connections.ComponentData@endlink) Comp2

    ##  Returns the comp2    
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @Comp2.setter
    def Comp2(self, comp2: ComponentData):
        """
        Setter for property: (@link ComponentData NXOpen.CAE.Connections.ComponentData@endlink) Comp2
         Returns the comp2    
            
         
        """
        pass
    
    ## Getter for property: (@link ComponentData NXOpen.CAE.Connections.ComponentData@endlink) Comp3
    ##  Returns the comp3    
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
         Returns the comp3    
            
         
        """
        pass
    
    ## Setter for property: (@link ComponentData NXOpen.CAE.Connections.ComponentData@endlink) Comp3

    ##  Returns the comp3    
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @Comp3.setter
    def Comp3(self, comp3: ComponentData):
        """
        Setter for property: (@link ComponentData NXOpen.CAE.Connections.ComponentData@endlink) Comp3
         Returns the comp3    
            
         
        """
        pass
    
    ## Getter for property: (@link ComposerConnectionType NXOpen.CAE.Connections.ComposerConnectionType@endlink) ConnectionType
    ##  Returns the connection type    
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
         Returns the connection type    
            
         
        """
        pass
    
    ## Setter for property: (@link ComposerConnectionType NXOpen.CAE.Connections.ComposerConnectionType@endlink) ConnectionType

    ##  Returns the connection type    
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @ConnectionType.setter
    def ConnectionType(self, type: ComposerConnectionType):
        """
        Setter for property: (@link ComposerConnectionType NXOpen.CAE.Connections.ComposerConnectionType@endlink) ConnectionType
         Returns the connection type    
            
         
        """
        pass
    
    ## Getter for property: (str) DBItem
    ##  Returns the db item    
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
         Returns the db item    
            
         
        """
        pass
    
    ## Setter for property: (str) DBItem

    ##  Returns the db item    
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @DBItem.setter
    def DBItem(self, name: str):
        """
        Setter for property: (str) DBItem
         Returns the db item    
            
         
        """
        pass
    
    ## Getter for property: (bool) Dof1
    ##  Returns the dof1   
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
         Returns the dof1   
            
         
        """
        pass
    
    ## Setter for property: (bool) Dof1

    ##  Returns the dof1   
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @Dof1.setter
    def Dof1(self, name: bool):
        """
        Setter for property: (bool) Dof1
         Returns the dof1   
            
         
        """
        pass
    
    ## Getter for property: (bool) Dof2
    ##  Returns the dof2   
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
         Returns the dof2   
            
         
        """
        pass
    
    ## Setter for property: (bool) Dof2

    ##  Returns the dof2   
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @Dof2.setter
    def Dof2(self, name: bool):
        """
        Setter for property: (bool) Dof2
         Returns the dof2   
            
         
        """
        pass
    
    ## Getter for property: (bool) Dof3
    ##  Returns the dof3   
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
         Returns the dof3   
            
         
        """
        pass
    
    ## Setter for property: (bool) Dof3

    ##  Returns the dof3   
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @Dof3.setter
    def Dof3(self, name: bool):
        """
        Setter for property: (bool) Dof3
         Returns the dof3   
            
         
        """
        pass
    
    ## Getter for property: (bool) Dof4
    ##  Returns the dof4   
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
         Returns the dof4   
            
         
        """
        pass
    
    ## Setter for property: (bool) Dof4

    ##  Returns the dof4   
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @Dof4.setter
    def Dof4(self, name: bool):
        """
        Setter for property: (bool) Dof4
         Returns the dof4   
            
         
        """
        pass
    
    ## Getter for property: (bool) Dof5
    ##  Returns the dof5   
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
         Returns the dof5   
            
         
        """
        pass
    
    ## Setter for property: (bool) Dof5

    ##  Returns the dof5   
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @Dof5.setter
    def Dof5(self, name: bool):
        """
        Setter for property: (bool) Dof5
         Returns the dof5   
            
         
        """
        pass
    
    ## Getter for property: (bool) Dof6
    ##  Returns the dof6   
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
         Returns the dof6   
            
         
        """
        pass
    
    ## Setter for property: (bool) Dof6

    ##  Returns the dof6   
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @Dof6.setter
    def Dof6(self, name: bool):
        """
        Setter for property: (bool) Dof6
         Returns the dof6   
            
         
        """
        pass
    
    ## Getter for property: (float) ExpansionRadius1
    ##  Returns the expansion radius1   
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
         Returns the expansion radius1   
            
         
        """
        pass
    
    ## Setter for property: (float) ExpansionRadius1

    ##  Returns the expansion radius1   
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @ExpansionRadius1.setter
    def ExpansionRadius1(self, expansionRadius1: float):
        """
        Setter for property: (float) ExpansionRadius1
         Returns the expansion radius1   
            
         
        """
        pass
    
    ## Getter for property: (float) ExpansionRadius2
    ##  Returns the expansion radius2   
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
         Returns the expansion radius2   
            
         
        """
        pass
    
    ## Setter for property: (float) ExpansionRadius2

    ##  Returns the expansion radius2   
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @ExpansionRadius2.setter
    def ExpansionRadius2(self, expansionRadius2: float):
        """
        Setter for property: (float) ExpansionRadius2
         Returns the expansion radius2   
            
         
        """
        pass
    
    ## Getter for property: (float) ExpansionRadiusFactor1
    ##  Returns the expansion radius factor1   
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
         Returns the expansion radius factor1   
            
         
        """
        pass
    
    ## Setter for property: (float) ExpansionRadiusFactor1

    ##  Returns the expansion radius factor1   
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @ExpansionRadiusFactor1.setter
    def ExpansionRadiusFactor1(self, expansionRadiusFactor1: float):
        """
        Setter for property: (float) ExpansionRadiusFactor1
         Returns the expansion radius factor1   
            
         
        """
        pass
    
    ## Getter for property: (float) ExpansionRadiusFactor2
    ##  Returns the expansion radius factor2   
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
         Returns the expansion radius factor2   
            
         
        """
        pass
    
    ## Setter for property: (float) ExpansionRadiusFactor2

    ##  Returns the expansion radius factor2   
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @ExpansionRadiusFactor2.setter
    def ExpansionRadiusFactor2(self, expansionRadiusFactor2: float):
        """
        Setter for property: (float) ExpansionRadiusFactor2
         Returns the expansion radius factor2   
            
         
        """
        pass
    
    ## Getter for property: (float) FlangeSearchTolerance1
    ##  Returns the expansion radius factor1   
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
         Returns the expansion radius factor1   
            
         
        """
        pass
    
    ## Setter for property: (float) FlangeSearchTolerance1

    ##  Returns the expansion radius factor1   
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @FlangeSearchTolerance1.setter
    def FlangeSearchTolerance1(self, flangeSearchTolerance1: float):
        """
        Setter for property: (float) FlangeSearchTolerance1
         Returns the expansion radius factor1   
            
         
        """
        pass
    
    ## Getter for property: (float) FlangeSearchTolerance2
    ##  Returns the expansion radius factor2   
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
         Returns the expansion radius factor2   
            
         
        """
        pass
    
    ## Setter for property: (float) FlangeSearchTolerance2

    ##  Returns the expansion radius factor2   
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @FlangeSearchTolerance2.setter
    def FlangeSearchTolerance2(self, flangeSearchTolerance2: float):
        """
        Setter for property: (float) FlangeSearchTolerance2
         Returns the expansion radius factor2   
            
         
        """
        pass
    
    ## Getter for property: (str) FlangeType1
    ##  Returns the flange type1    
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
         Returns the flange type1    
            
         
        """
        pass
    
    ## Setter for property: (str) FlangeType1

    ##  Returns the flange type1    
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @FlangeType1.setter
    def FlangeType1(self, flangeType1: str):
        """
        Setter for property: (str) FlangeType1
         Returns the flange type1    
            
         
        """
        pass
    
    ## Getter for property: (str) FlangeType2
    ##  Returns the flange type2    
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
         Returns the flange type2    
            
         
        """
        pass
    
    ## Setter for property: (str) FlangeType2

    ##  Returns the flange type2    
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @FlangeType2.setter
    def FlangeType2(self, flangeType2: str):
        """
        Setter for property: (str) FlangeType2
         Returns the flange type2    
            
         
        """
        pass
    
    ## Getter for property: (float) HeadDiameter
    ##  Returns the head diameter    
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
         Returns the head diameter    
            
         
        """
        pass
    
    ## Setter for property: (float) HeadDiameter

    ##  Returns the head diameter    
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @HeadDiameter.setter
    def HeadDiameter(self, headDiameter: float):
        """
        Setter for property: (float) HeadDiameter
         Returns the head diameter    
            
         
        """
        pass
    
    ## Getter for property: (float) LengthStep
    ##  Returns the expansion radius factor2   
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
         Returns the expansion radius factor2   
            
         
        """
        pass
    
    ## Setter for property: (float) LengthStep

    ##  Returns the expansion radius factor2   
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @LengthStep.setter
    def LengthStep(self, lengthStep: float):
        """
        Setter for property: (float) LengthStep
         Returns the expansion radius factor2   
            
         
        """
        pass
    
    ## Getter for property: (str) LinePart1
    ##  Returns the line part1    
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
         Returns the line part1    
            
         
        """
        pass
    
    ## Setter for property: (str) LinePart1

    ##  Returns the line part1    
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @LinePart1.setter
    def LinePart1(self, linePart: str):
        """
        Setter for property: (str) LinePart1
         Returns the line part1    
            
         
        """
        pass
    
    ## Getter for property: (str) LinePart2
    ##  Returns the line part2    
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
         Returns the line part2    
            
         
        """
        pass
    
    ## Setter for property: (str) LinePart2

    ##  Returns the line part2    
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @LinePart2.setter
    def LinePart2(self, linePart: str):
        """
        Setter for property: (str) LinePart2
         Returns the line part2    
            
         
        """
        pass
    
    ## Getter for property: (float) MaximumDistanceTolerance1
    ##  Returns the maximum distance tolerance1    
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
         Returns the maximum distance tolerance1    
            
         
        """
        pass
    
    ## Setter for property: (float) MaximumDistanceTolerance1

    ##  Returns the maximum distance tolerance1    
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @MaximumDistanceTolerance1.setter
    def MaximumDistanceTolerance1(self, maximumDistanceTolerance1: float):
        """
        Setter for property: (float) MaximumDistanceTolerance1
         Returns the maximum distance tolerance1    
            
         
        """
        pass
    
    ## Getter for property: (float) MaximumDistanceTolerance2
    ##  Returns the maximum distance tolerance2    
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
         Returns the maximum distance tolerance2    
            
         
        """
        pass
    
    ## Setter for property: (float) MaximumDistanceTolerance2

    ##  Returns the maximum distance tolerance2    
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @MaximumDistanceTolerance2.setter
    def MaximumDistanceTolerance2(self, maximumDistanceTolerance2: float):
        """
        Setter for property: (float) MaximumDistanceTolerance2
         Returns the maximum distance tolerance2    
            
         
        """
        pass
    
    ## Getter for property: (str) Name
    ##  Returns the assembly name    
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
         Returns the assembly name    
            
         
        """
        pass
    
    ## Setter for property: (str) Name

    ##  Returns the assembly name    
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns the assembly name    
            
         
        """
        pass
    
    ## Getter for property: (str) SearchType1
    ##  Returns the search type1    
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
         Returns the search type1    
            
         
        """
        pass
    
    ## Setter for property: (str) SearchType1

    ##  Returns the search type1    
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @SearchType1.setter
    def SearchType1(self, searchType1: str):
        """
        Setter for property: (str) SearchType1
         Returns the search type1    
            
         
        """
        pass
    
    ## Getter for property: (str) SearchType2
    ##  Returns the search type2    
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
         Returns the search type2    
            
         
        """
        pass
    
    ## Setter for property: (str) SearchType2

    ##  Returns the search type2    
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @SearchType2.setter
    def SearchType2(self, searchType2: str):
        """
        Setter for property: (str) SearchType2
         Returns the search type2    
            
         
        """
        pass
    
    ## Getter for property: (float) ShankDiameter
    ##  Returns the shank diameter    
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
         Returns the shank diameter    
            
         
        """
        pass
    
    ## Setter for property: (float) ShankDiameter

    ##  Returns the shank diameter    
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @ShankDiameter.setter
    def ShankDiameter(self, shankDiameter: float):
        """
        Setter for property: (float) ShankDiameter
         Returns the shank diameter    
            
         
        """
        pass
    
    ## Getter for property: (str) WCDFile
    ##  Returns the WCD File    
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
         Returns the WCD File    
            
         
        """
        pass
    
    ## Setter for property: (str) WCDFile

    ##  Returns the WCD File    
    ##     
    ##  
    ## Setter License requirements: sc_gso_10 (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @WCDFile.setter
    def WCDFile(self, wcdFile: str):
        """
        Setter for property: (str) WCDFile
         Returns the WCD File    
            
         
        """
        pass
    
    ##  Gets axis. 
    ##  @return axis (str): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    def GetAxis(self) -> str:
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
    def GetComponents1(self) -> List[ComponentData]:
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
    def GetComponents2(self) -> List[ComponentData]:
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
    def GetInvalidDOF(self) -> List[int]:
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
    def GetLineFEEdgeRecipe1(self) -> List[str]:
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
    def GetLineFEEdgeRecipe2(self) -> List[str]:
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
    def GetPID1s(self) -> List[int]:
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
    def GetPID2s(self) -> List[int]:
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
    def GetPID3s(self) -> List[int]:
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
    def GetPointNameCoord1(self) -> List[str]:
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
    def GetPointNameCoord2(self) -> List[str]:
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
    def GetPointNameCoord3(self) -> List[str]:
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
    def SetAxis(self, axis: str) -> None:
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
    def SetComponents1(self, comps: List[ComponentData]) -> None:
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
    def SetComponents2(self, comps: List[ComponentData]) -> None:
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
    def SetLineFEEdgeRecipe1(self, lineFEEdgeRecipe1s: List[str]) -> None:
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
    def SetLineFEEdgeRecipe2(self, lineFEEdgeRecipe2s: List[str]) -> None:
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
    def SetPID1s(self, pID1s: List[int]) -> None:
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
    def SetPID2s(self, pID2s: List[int]) -> None:
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
    def SetPID3s(self, pID3s: List[int]) -> None:
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
    def SetPointNameCoord1(self, pointNameCoord1s: List[str]) -> None:
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
    def SetPointNameCoord2(self, pointNameCoord2s: List[str]) -> None:
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
    def SetPointNameCoord3(self, pointNameCoord3s: List[str]) -> None:
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
    def GetConnectionDBItemDatas(self) -> List[ConnectionDBItemData]:
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
    def SetConnectionDBItemDatas(self, components: List[ConnectionDBItemData]) -> None:
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
    ##  Returns the adhesive width    
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
         Returns the adhesive width    
            
         
        """
        pass
    
    ## Getter for property: (float) Height
    ##  Returns the height    
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
         Returns the height    
            
         
        """
        pass
    
    ## Getter for property: (@link HeightType NXOpen.CAE.Connections.HeightType@endlink) HeightType
    ##  Returns the height type    
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
         Returns the height type    
            
         
        """
        pass
    
    ## Getter for property: (float) Mass
    ##  Returns the mass    
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
         Returns the mass    
            
         
        """
        pass
    
    ## Setter for property: (float) Mass

    ##  Returns the mass    
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @Mass.setter
    def Mass(self, mass: float):
        """
        Setter for property: (float) Mass
         Returns the mass    
            
         
        """
        pass
    
    ## Getter for property: (int) MaterialID
    ##  Returns the material ID    
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
         Returns the material ID    
            
         
        """
        pass
    
    ## Setter for property: (int) MaterialID

    ##  Returns the material ID    
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @MaterialID.setter
    def MaterialID(self, materialID: int):
        """
        Setter for property: (int) MaterialID
         Returns the material ID    
            
         
        """
        pass
    
    ## Getter for property: (str) Name
    ##  Returns the name    
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
         Returns the name    
            
         
        """
        pass
    
    ## Setter for property: (str) Name

    ##  Returns the name    
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns the name    
            
         
        """
        pass
    
    ## Getter for property: (float) ScrewDiameter
    ##  Returns the screw diameter    
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
         Returns the screw diameter    
            
         
        """
        pass
    
    ## Setter for property: (float) ScrewDiameter

    ##  Returns the screw diameter    
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @ScrewDiameter.setter
    def ScrewDiameter(self, screwDiameter: float):
        """
        Setter for property: (float) ScrewDiameter
         Returns the screw diameter    
            
         
        """
        pass
    
    ## Getter for property: (float) StiffnessR
    ##  Returns the stiffness R    
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
         Returns the stiffness R    
            
         
        """
        pass
    
    ## Setter for property: (float) StiffnessR

    ##  Returns the stiffness R    
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @StiffnessR.setter
    def StiffnessR(self, stiffnessR: float):
        """
        Setter for property: (float) StiffnessR
         Returns the stiffness R    
            
         
        """
        pass
    
    ## Getter for property: (float) StiffnessRR
    ##  Returns the stiffness RR    
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
         Returns the stiffness RR    
            
         
        """
        pass
    
    ## Setter for property: (float) StiffnessRR

    ##  Returns the stiffness RR    
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @StiffnessRR.setter
    def StiffnessRR(self, stiffnessRR: float):
        """
        Setter for property: (float) StiffnessRR
         Returns the stiffness RR    
            
         
        """
        pass
    
    ## Getter for property: (float) StiffnessRS
    ##  Returns the stiffness RS    
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
         Returns the stiffness RS    
            
         
        """
        pass
    
    ## Setter for property: (float) StiffnessRS

    ##  Returns the stiffness RS    
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @StiffnessRS.setter
    def StiffnessRS(self, stiffnessRS: float):
        """
        Setter for property: (float) StiffnessRS
         Returns the stiffness RS    
            
         
        """
        pass
    
    ## Getter for property: (float) StiffnessRX
    ##  Returns the stiffness RX    
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
         Returns the stiffness RX    
            
         
        """
        pass
    
    ## Setter for property: (float) StiffnessRX

    ##  Returns the stiffness RX    
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @StiffnessRX.setter
    def StiffnessRX(self, stiffnessRX: float):
        """
        Setter for property: (float) StiffnessRX
         Returns the stiffness RX    
            
         
        """
        pass
    
    ## Getter for property: (float) StiffnessRY
    ##  Returns the stiffness RY    
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
         Returns the stiffness RY    
            
         
        """
        pass
    
    ## Setter for property: (float) StiffnessRY

    ##  Returns the stiffness RY    
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @StiffnessRY.setter
    def StiffnessRY(self, stiffnessRY: float):
        """
        Setter for property: (float) StiffnessRY
         Returns the stiffness RY    
            
         
        """
        pass
    
    ## Getter for property: (float) StiffnessRZ
    ##  Returns the stiffness RZ    
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
         Returns the stiffness RZ    
            
         
        """
        pass
    
    ## Setter for property: (float) StiffnessRZ

    ##  Returns the stiffness RZ    
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @StiffnessRZ.setter
    def StiffnessRZ(self, stiffnessRZ: float):
        """
        Setter for property: (float) StiffnessRZ
         Returns the stiffness RZ    
            
         
        """
        pass
    
    ## Getter for property: (float) StiffnessS
    ##  Returns the stiffness RS    
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
         Returns the stiffness RS    
            
         
        """
        pass
    
    ## Setter for property: (float) StiffnessS

    ##  Returns the stiffness RS    
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @StiffnessS.setter
    def StiffnessS(self, stiffnessS: float):
        """
        Setter for property: (float) StiffnessS
         Returns the stiffness RS    
            
         
        """
        pass
    
    ## Getter for property: (@link ConnectionDBItemStiffnessType NXOpen.CAE.Connections.ConnectionDBItemStiffnessType@endlink) StiffnessType
    ##  Returns the mass    
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
         Returns the mass    
            
         
        """
        pass
    
    ## Setter for property: (@link ConnectionDBItemStiffnessType NXOpen.CAE.Connections.ConnectionDBItemStiffnessType@endlink) StiffnessType

    ##  Returns the mass    
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @StiffnessType.setter
    def StiffnessType(self, stiffnessType: ConnectionDBItemStiffnessType):
        """
        Setter for property: (@link ConnectionDBItemStiffnessType NXOpen.CAE.Connections.ConnectionDBItemStiffnessType@endlink) StiffnessType
         Returns the mass    
            
         
        """
        pass
    
    ## Getter for property: (float) StiffnessX
    ##  Returns the stiffness X    
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
         Returns the stiffness X    
            
         
        """
        pass
    
    ## Setter for property: (float) StiffnessX

    ##  Returns the stiffness X    
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @StiffnessX.setter
    def StiffnessX(self, stiffnessX: float):
        """
        Setter for property: (float) StiffnessX
         Returns the stiffness X    
            
         
        """
        pass
    
    ## Getter for property: (float) StiffnessY
    ##  Returns the stiffness Y    
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
         Returns the stiffness Y    
            
         
        """
        pass
    
    ## Setter for property: (float) StiffnessY

    ##  Returns the stiffness Y    
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @StiffnessY.setter
    def StiffnessY(self, stiffnessY: float):
        """
        Setter for property: (float) StiffnessY
         Returns the stiffness Y    
            
         
        """
        pass
    
    ## Getter for property: (float) StiffnessZ
    ##  Returns the stiffness Z    
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
         Returns the stiffness Z    
            
         
        """
        pass
    
    ## Setter for property: (float) StiffnessZ

    ##  Returns the stiffness Z    
    ##     
    ##  
    ## Setter License requirements: sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @StiffnessZ.setter
    def StiffnessZ(self, stiffnessZ: float):
        """
        Setter for property: (float) StiffnessZ
         Returns the stiffness Z    
            
         
        """
        pass
    
    ##  The Dofs  
    ##  @return listOfDofs (List[int]): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    def GetDofs(self) -> List[int]:
        """
         The Dofs  
         @return listOfDofs (List[int]): .
        """
        pass
    
##  connection DB item stiffness type 
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## NotSet</term><description> 
##  None </description> </item><item><term> 
## Rectangular</term><description> 
##  Rectangular </description> </item><item><term> 
## Spherical</term><description> 
##  Spherical </description> </item><item><term> 
## Cylindrical</term><description> 
##  Cylindrical </description> </item></list>
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
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## NotSet</term><description> 
##  None </description> </item><item><term> 
## SpotWeld</term><description> 
##  SpotWeld </description> </item><item><term> 
## Adhesive</term><description> 
##  Adhesive </description> </item><item><term> 
## Bolt</term><description> 
##  Bolt </description> </item><item><term> 
## Spring</term><description> 
##  Spring </description> </item><item><term> 
## Rigid</term><description> 
##  Rigid </description> </item><item><term> 
## Bushing</term><description> 
##  Bushing </description> </item><item><term> 
## Damper</term><description> 
##  Damper </description> </item><item><term> 
## Kinematic</term><description> 
##  Kinematic </description> </item><item><term> 
## SeamWeld</term><description> 
##  Seam Weld </description> </item><item><term> 
## Sealing</term><description> 
##  Sealing </description> </item><item><term> 
## Rivet</term><description> 
##  Rivet </description> </item><item><term> 
## LumpedMass</term><description> 
##  Lumped Mass </description> </item><item><term> 
## Clinch</term><description> 
##  Clinch </description> </item><item><term> 
## Crimp</term><description> 
##  Crimp </description> </item><item><term> 
## Bar</term><description> 
##  Bar </description> </item><item><term> 
## Bearing</term><description> 
##  Bearing </description> </item></list>
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
    def GetCoordinates(self) -> NXOpen.Point3d:
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
    ## 
    ## <param name="coordinates"> (@link NXOpen.Point3d NXOpen.Point3d@endlink)  The location coordinates </param>
    def SetCoordinates(self, coordinates: NXOpen.Point3d) -> None:
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
    def GetCoordinates(self) -> List[NXOpen.Point3d]:
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
    ## 
    ## <param name="coordinates"> (@link NXOpen.Point3d List[NXOpen.Point3d]@endlink)  The location coordinates </param>
    def SetCoordinates(self, coordinates: List[NXOpen.Point3d]) -> None:
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
    ##  Returns the discretization method   
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
         Returns the discretization method   
            
         
        """
        pass
    
    ## Setter for property: (@link DiscretizationMethod NXOpen.CAE.Connections.DiscretizationMethod@endlink) DiscretizationMethod

    ##  Returns the discretization method   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @DiscretizationMethod.setter
    def DiscretizationMethod(self, method: DiscretizationMethod):
        """
        Setter for property: (@link DiscretizationMethod NXOpen.CAE.Connections.DiscretizationMethod@endlink) DiscretizationMethod
         Returns the discretization method   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) DistanceFromStart
    ##  Returns the line Discretization distance from start   
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
         Returns the line Discretization distance from start   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) DistanceToEnd
    ##  Returns the line Discretization distance to end   
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
         Returns the line Discretization distance to end   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Height
    ##  Returns the height value   
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
         Returns the height value   
            
         
        """
        pass
    
    ## Getter for property: (@link HeightType NXOpen.CAE.Connections.HeightType@endlink) HeightType
    ##  Returns the connection height type   
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
         Returns the connection height type   
            
         
        """
        pass
    
    ## Setter for property: (@link HeightType NXOpen.CAE.Connections.HeightType@endlink) HeightType

    ##  Returns the connection height type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @HeightType.setter
    def HeightType(self, heightType: HeightType):
        """
        Setter for property: (@link HeightType NXOpen.CAE.Connections.HeightType@endlink) HeightType
         Returns the connection height type   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) LengthStep
    ##  Returns the line Discretization length step   
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
         Returns the line Discretization length step   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.PhysicalMaterial NXOpen.PhysicalMaterial@endlink) Material
    ##  Returns the connection material   
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
         Returns the connection material   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.PhysicalMaterial NXOpen.PhysicalMaterial@endlink) Material

    ##  Returns the connection material   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @Material.setter
    def Material(self, material: NXOpen.PhysicalMaterial):
        """
        Setter for property: (@link NXOpen.PhysicalMaterial NXOpen.PhysicalMaterial@endlink) Material
         Returns the connection material   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxAngleBetweenNormals
    ##  Returns the maximum angle of normals with the projection surface   
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
         Returns the maximum angle of normals with the projection surface   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxDistCGToElemCG
    ##  Returns the maximum distance from definition point to center of support element   
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
         Returns the maximum distance from definition point to center of support element   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxLengthStep
    ##  Returns the line Discretization max length step   
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
         Returns the line Discretization max length step   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxNormalDistCGToFlanges
    ##  Returns the maximum normal distance from definition point to center of element   
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
         Returns the maximum normal distance from definition point to center of element   
            
         
        """
        pass
    
    ## Getter for property: (int) NumberOfDiscretizationPoints
    ##  Returns the number of connections   
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
         Returns the number of connections   
            
         
        """
        pass
    
    ## Setter for property: (int) NumberOfDiscretizationPoints

    ##  Returns the number of connections   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @NumberOfDiscretizationPoints.setter
    def NumberOfDiscretizationPoints(self, num: int):
        """
        Setter for property: (int) NumberOfDiscretizationPoints
         Returns the number of connections   
            
         
        """
        pass
    
    ## Getter for property: (int) NumberOfFlanges
    ##  Returns the number of flanges.  
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
         Returns the number of flanges.  
           When changing the number of flanges this is not applied till an update is performed by calling @link Update::DoUpdate Update::DoUpdate@endlink    
         
        """
        pass
    
    ## Setter for property: (int) NumberOfFlanges

    ##  Returns the number of flanges.  
    ##    When changing the number of flanges this is not applied till an update is performed by calling @link Update::DoUpdate Update::DoUpdate@endlink    
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @NumberOfFlanges.setter
    def NumberOfFlanges(self, numberOfFlanges: int):
        """
        Setter for property: (int) NumberOfFlanges
         Returns the number of flanges.  
           When changing the number of flanges this is not applied till an update is performed by calling @link Update::DoUpdate Update::DoUpdate@endlink    
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ProjectTolerance
    ##  Returns the projection tolerance   
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
         Returns the projection tolerance   
            
         
        """
        pass
    
    ## Getter for property: (bool) UseMaxLengthStep
    ##  Returns the usage of max length step   
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
         Returns the usage of max length step   
            
         
        """
        pass
    
    ## Setter for property: (bool) UseMaxLengthStep

    ##  Returns the usage of max length step   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @UseMaxLengthStep.setter
    def UseMaxLengthStep(self, use: bool):
        """
        Setter for property: (bool) UseMaxLengthStep
         Returns the usage of max length step   
            
         
        """
        pass
    
    ## Getter for property: (bool) UseOriginalNodesOfConnection
    ##  Returns the usage of original nodes of connection   
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
         Returns the usage of original nodes of connection   
            
         
        """
        pass
    
    ## Setter for property: (bool) UseOriginalNodesOfConnection

    ##  Returns the usage of original nodes of connection   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @UseOriginalNodesOfConnection.setter
    def UseOriginalNodesOfConnection(self, use: bool):
        """
        Setter for property: (bool) UseOriginalNodesOfConnection
         Returns the usage of original nodes of connection   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Width
    ##  Returns the width value   
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
         Returns the width value   
            
         
        """
        pass
    
##  Csys types 
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## Existing</term><description> 
##  Existing CSYS </description> </item><item><term> 
## Predefined</term><description> 
##  Predefined CSYS </description> </item><item><term> 
## Absolute</term><description> 
##  Absolute CSYS </description> </item><item><term> 
## LocalCartesian</term><description> 
##  Local Cartesian CSYS </description> </item><item><term> 
## LocalCylindrical</term><description> 
##  Local Cylindrical CSYS </description> </item><item><term> 
## LocalSpherical</term><description> 
##  Local Spherical CSYS </description> </item></list>
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
    ##  Returns the CURVE used for creating the location.  
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
         Returns the CURVE used for creating the location.  
          
                        If the location type is not curve, this method will raise an error.   
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.IBaseCurve NXOpen.IBaseCurve@endlink) Curve

    ##  Returns the CURVE used for creating the location.  
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
         Returns the CURVE used for creating the location.  
          
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
    ##  Returns the csys   
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
         Returns the csys   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) Csys

    ##  Returns the csys   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @Csys.setter
    def Csys(self, csys: NXOpen.CoordinateSystem):
        """
        Setter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) Csys
         Returns the csys   
            
         
        """
        pass
    
    ## Getter for property: (@link CsysType NXOpen.CAE.Connections.CsysType@endlink) CsysType
    ##  Returns the csys type   
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
         Returns the csys type   
            
         
        """
        pass
    
    ## Setter for property: (@link CsysType NXOpen.CAE.Connections.CsysType@endlink) CsysType

    ##  Returns the csys type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @CsysType.setter
    def CsysType(self, csysType: CsysType):
        """
        Setter for property: (@link CsysType NXOpen.CAE.Connections.CsysType@endlink) CsysType
         Returns the csys type   
            
         
        """
        pass
    
    ## Getter for property: (@link NodalPairingMethod NXOpen.CAE.Connections.NodalPairingMethod@endlink) PairingMethod
    ##  Returns the pairing method of targets   
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
         Returns the pairing method of targets   
            
         
        """
        pass
    
    ## Setter for property: (@link NodalPairingMethod NXOpen.CAE.Connections.NodalPairingMethod@endlink) PairingMethod

    ##  Returns the pairing method of targets   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @PairingMethod.setter
    def PairingMethod(self, method: NodalPairingMethod):
        """
        Setter for property: (@link NodalPairingMethod NXOpen.CAE.Connections.NodalPairingMethod@endlink) PairingMethod
         Returns the pairing method of targets   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RxViscousDampingConstant
    ##  Returns the RX viscous damping constant   
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
         Returns the RX viscous damping constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RyViscousDampingConstant
    ##  Returns the RY viscous damping constant   
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
         Returns the RY viscous damping constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RzViscousDampingConstant
    ##  Returns the RZ viscous damping constant   
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
         Returns the RZ viscous damping constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) SearchConeAngle
    ##  Returns the search cone angle   
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
         Returns the search cone angle   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) SearchOrientation
    ##  Returns the pairing search orientation   
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
         Returns the pairing search orientation   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) SearchOrientation

    ##  Returns the pairing search orientation   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @SearchOrientation.setter
    def SearchOrientation(self, orientation: NXOpen.Direction):
        """
        Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) SearchOrientation
         Returns the pairing search orientation   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) SearchRange
    ##  Returns the search range   
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
         Returns the search range   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) XViscousDampingConstant
    ##  Returns the X viscous damping constant   
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
         Returns the X viscous damping constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) YViscousDampingConstant
    ##  Returns the Y viscous damping constant   
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
         Returns the Y viscous damping constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ZViscousDampingConstant
    ##  Returns the Z viscous damping constant   
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
         Returns the Z viscous damping constant   
            
         
        """
        pass
    
##  Diameter definition types 
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## Undefined</term><description> 
##  Undefined diameter type </description> </item><item><term> 
## User</term><description> 
##  User defined diameter </description> </item><item><term> 
## Formula</term><description> 
##  Formula defined diameter </description> </item><item><term> 
## TableFile</term><description> 
##  Table defined diameter </description> </item><item><term> 
## FlangeHoleDetection</term><description> 
##  Flange hole defined diameter </description> </item></list>
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
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## StepLength</term><description> 
##  Discretize the line using step length </description> </item><item><term> 
## NumberOfPoints</term><description> 
##  Discretize the line using the total number of points </description> </item></list>
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
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## UserDefined</term><description> 
##  User defined combination for all DOFs </description> </item><item><term> 
## Fixed</term><description> 
##  DOF1 fixed, DOF2 fixed, DOF3 fixed, DOF4 fixed, DOF5 fixed, DOF6 fixed </description> </item><item><term> 
## Spherical</term><description> 
##  DOF1 fixed, DOF2 fixed, DOF3 fixed, DOF4 free,  DOF5 free,  DOF6 free </description> </item><item><term> 
## Inplane</term><description> 
##  DOF1 fixed, DOF2 free,  DOF3 free,  DOF4 free,  DOF5 free,  DOF6 free </description> </item><item><term> 
## Slider</term><description> 
##  DOF1 free,  DOF2 fixed, DOF3 fixed, DOF4 fixed, DOF5 fixed, DOF6 fixed </description> </item><item><term> 
## Revolute</term><description> 
##  DOF1 fixed, DOF2 fixed, DOF3 fixed, DOF4 free,  DOF5 fixed, DOF6 fixed </description> </item><item><term> 
## Cylindrical</term><description> 
##  DOF1 free,  DOF2 fixed, DOF3 fixed, DOF4 free,  DOF5 fixed, DOF6 fixed </description> </item><item><term> 
## Universal</term><description> 
##  DOF1 fixed, DOF2 fixed, DOF3 fixed, DOF4 free,  DOF5 fixed, DOF6 free </description> </item><item><term> 
## SliderUniversal</term><description> 
##  DOF1 free,  DOF2 fixed, DOF3 fixed, DOF4 free,  DOF5 fixed, DOF6 free </description> </item><item><term> 
## Inline</term><description> 
##  DOF1 free,  DOF2 fixed, DOF3 fixed, DOF4 free,  DOF5 free, DOF6 free </description> </item></list>
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
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## Free</term><description> 
##  The DOF is not constrained </description> </item><item><term> 
## Fixed</term><description> 
##  The DOF is fixed </description> </item></list>
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
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## X</term><description> 
##  X Translation degree of freedom </description> </item><item><term> 
## Y</term><description> 
##  Y Translation degree of freedom </description> </item><item><term> 
## Z</term><description> 
##  Z Translation degree of freedom </description> </item><item><term> 
## Rx</term><description> 
##  X Rotation degree of freedom </description> </item><item><term> 
## Ry</term><description> 
##  Y Rotation degree of freedom </description> </item><item><term> 
## Rz</term><description> 
##  Z Rotation degree of freedom </description> </item></list>
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
    def Create(self, elementType: ElementType, name: str, connections: List[IConnection]) -> Element:
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
    def Create(self, elementType: ElementType, connectionType: ConnectionType, name: str) -> Element:
        """
         Creates a @link NXOpen::CAE::Connections::Element NXOpen::CAE::Connections::Element@endlink 
         @return element (@link Element NXOpen.CAE.Connections.Element@endlink): .
        """
        pass
    
##  Element status 
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## Invalid</term><description> 
##  Invalid </description> </item><item><term> 
## NotUpdated</term><description> 
##  Not updated </description> </item><item><term> 
## Updated</term><description> 
##  Updated </description> </item></list>
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
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## NotSet</term><description> 
##  None </description> </item><item><term> 
## EHex8</term><description> 
##  Hex8 </description> </item><item><term> 
## EHex8Spider</term><description> 
##  Hex8 + Spider </description> </item><item><term> 
## E1d</term><description> 
##  1D </description> </item><item><term> 
## E1DSpider</term><description> 
##  1D + Spider </description> </item><item><term> 
## ESpider</term><description> 
##  Spider </description> </item><item><term> 
## EBushing</term><description> 
##  Bushing Elm </description> </item><item><term> 
## ESpring</term><description> 
##  Spring Elm </description> </item><item><term> 
## EDamper</term><description> 
##  Damper Elm </description> </item><item><term> 
## ERigid</term><description> 
##  Rigid Elm </description> </item><item><term> 
## EKinematic</term><description> 
##  Kinematic Elm </description> </item><item><term> 
## ERigidConnector</term><description> 
##  Rigid Connector </description> </item><item><term> 
## ERigidRigidConnector</term><description> 
##  Rigid Connector - Rigid Connector </description> </item><item><term> 
## EInterpolationSpider</term><description> 
##  Interpolation + Spider </description> </item><item><term> 
## EMassRigidSpider</term><description> 
##  Concentrated Mass + Rigid Spider </description> </item><item><term> 
## EMassInterpolationSpider</term><description> 
##  Concentrated Mass + Interpolation Spider </description> </item><item><term> 
## EScalarSpringRigidSpider</term><description> 
##  Scalar Spring + Rigid Spider </description> </item><item><term> 
## EScalarSpringRigidInterpolationSpider</term><description> 
##  Scalar Spring + Rigid Spider + Interpolation Spider </description> </item><item><term> 
## EJoint</term><description> 
##  Joint Elm </description> </item><item><term> 
## EJointInterpolation</term><description> 
##  Joint Interpolation </description> </item><item><term> 
## EBeamRigidSpider</term><description> 
##  Beam + Rigid Spider </description> </item><item><term> 
## EBar</term><description> 
##  Bar + Rigid Spider </description> </item><item><term> 
## EBarInterpolationSpider</term><description> 
##  Bar + Interpolation Spider </description> </item><item><term> 
## ECbear2Fou3InterpolationSpider</term><description> 
##  CBEAR2 + FOU3 + Interpolation Spider </description> </item><item><term> 
## ECbear2RigidSpider</term><description> 
##  CBear2 + Rbe2 </description> </item><item><term> 
## ECbush2RigidSpider</term><description> 
##  CBush2 + Rbe2 </description> </item><item><term> 
## EBeamSpider</term><description> 
##  Beam Spider </description> </item><item><term> 
## ECbush2Fou3InterpolationSpider</term><description> 
##  CBUSH2 + FOU3 + Interpolation Spider </description> </item><item><term> 
## EConstrainedJointMPCSpider</term><description> 
##  Constrained Joint + MPC Spider </description> </item><item><term> 
## EMassFou3InterpolationSpider</term><description> 
##  Concentrated Mass + FOU3 + Interpolation Spider </description> </item><item><term> 
## EFou3InterpolationSpider</term><description> 
##  FOU3 + Interpolation Spider </description> </item><item><term> 
## EBeam</term><description> 
##  Beam </description> </item><item><term> 
## ECWeld</term><description> 
##  CWeld </description> </item><item><term> 
## EClinkCbear2RigidSpider</term><description> 
##  CLINK + CBEAR2 + RBE2 </description> </item><item><term> 
## EClinkCbush2RigidSpider</term><description> 
##  Clink + CBUSH2 +RBE2 </description> </item><item><term> 
## EClinkBarRigidSpider</term><description> 
##  Clink + CBAR + RBE2 </description> </item><item><term> 
## EClinkBeamRigidSpider</term><description> 
##  Clink + CBEAM + RBE2 </description> </item><item><term> 
## EClinkFou3</term><description> 
##  Clink + FOU3 </description> </item><item><term> 
## EQuad4InterpolationSpider</term><description> 
##  Quad4 + Interpolation Spider </description> </item></list>
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
    ##  Returns the compatibility of the element
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
         Returns the compatibility of the element
                        (whether it accepts compatible or incompatible meshes)
                      
            
         
        """
        pass
    
    ## Getter for property: (bool) Manual
    ##  Returns the flag telling if the connection element is set up manually.  
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
         Returns the flag telling if the connection element is set up manually.  
          
                      
         
        """
        pass
    
    ## Setter for property: (bool) Manual

    ##  Returns the flag telling if the connection element is set up manually.  
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
         Returns the flag telling if the connection element is set up manually.  
          
                      
         
        """
        pass
    
    ## Getter for property: (@link SeamWeldNodeSelectionMethod NXOpen.CAE.Connections.SeamWeldNodeSelectionMethod@endlink) NodeSelectionMethod
    ##  Returns the node selection method.  
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
         Returns the node selection method.  
           To be used when connection element has been set up manually (@link NXOpen::CAE::Connections::Element::Manual NXOpen::CAE::Connections::Element::Manual@endlink  is true).
                      
         
        """
        pass
    
    ## Setter for property: (@link SeamWeldNodeSelectionMethod NXOpen.CAE.Connections.SeamWeldNodeSelectionMethod@endlink) NodeSelectionMethod

    ##  Returns the node selection method.  
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
         Returns the node selection method.  
           To be used when connection element has been set up manually (@link NXOpen::CAE::Connections::Element::Manual NXOpen::CAE::Connections::Element::Manual@endlink  is true).
                      
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.CAE.PropertyTable NXOpen.CAE.PropertyTable@endlink) PropertyTable
    ##  Returns the property table.  
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
         Returns the property table.  
             
         
        """
        pass
    
    ## Getter for property: (@link ElementStatusType NXOpen.CAE.Connections.ElementStatusType@endlink) Status
    ##  Returnsthe status of the element
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
         Returnsthe status of the element
                      
            
         
        """
        pass
    
    ## Getter for property: (@link ElementType NXOpen.CAE.Connections.ElementType@endlink) Type
    ##  Returnsthe type of the element
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
         Returnsthe type of the element
                      
            
         
        """
        pass
    
    ## Setter for property: (@link ElementType NXOpen.CAE.Connections.ElementType@endlink) Type

    ##  Returnsthe type of the element
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
         Returnsthe type of the element
                      
            
         
        """
        pass
    
    ##  Adds connections to this element
    ##             
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ## <param name="connections"> (@link IConnection List[NXOpen.CAE.Connections.IConnection]@endlink) </param>
    def AddConnections(self, connections: List[IConnection]) -> None:
        """
         Adds connections to this element
                    
        """
        pass
    
    ##  Mesh the Connection Element.
    ##             
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    def GenerateElements(self) -> None:
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
    def GetConnections(self) -> List[IConnection]:
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
    def GetElementGroups(self) -> List[NXOpen.CAE.CaeGroup]:
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
    def GetElements(self) -> List[NXOpen.CAE.FEElement]:
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
    def GetGeneratedElementsOfConnection(self, connection: IConnection) -> List[NXOpen.CAE.FEElement]:
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
    def GetGeneratedElementsOfConnectionAtLocation(self, connection: IConnection, indexOfLocation: int, indexOfDefinitionInLocation: int) -> List[NXOpen.CAE.FEElement]:
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
    def GetGeneratedNodesOfConnection(self, connection: IConnection) -> List[NXOpen.CAE.FENode]:
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
    def GetNodeGroups(self) -> List[NXOpen.CAE.CaeGroup]:
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
    def GetNodes(self) -> List[NXOpen.CAE.FENode]:
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
    def MarkAsModifiedByPropertyTable(self) -> None:
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
    def RemoveConnections(self, connections: List[IConnection]) -> None:
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
    def SetElementGroups(self, groups: List[NXOpen.CAE.CaeGroup]) -> None:
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
    def SetElements(self, elems: List[NXOpen.CAE.FEElement]) -> None:
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
    def SetNodeGroups(self, groups: List[NXOpen.CAE.CaeGroup]) -> None:
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
    def SetNodes(self, nodes: List[NXOpen.CAE.FENode]) -> None:
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
    def GetFeEdges(self) -> List[NXOpen.CAE.FEElemEdge]:
        """
         Retrieve location edges. 
         @return edges (@link NXOpen.CAE.FEElemEdge List[NXOpen.CAE.FEElemEdge]@endlink):  Edges used for location .
        """
        pass
    
    ##  Add location edges. 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ## <param name="edges"> (@link NXOpen.CAE.FEElemEdge List[NXOpen.CAE.FEElemEdge]@endlink)  Edges used for location </param>
    def SetFeEdges(self, edges: List[NXOpen.CAE.FEElemEdge]) -> None:
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
    ##  Returns the parent folder   
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
         Returns the parent folder   
            
         
        """
        pass
    
    ##  Add a subfolder to this folder. The subfolder is moved if found in other folder. 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ## <param name="subfolder"> (@link Folder NXOpen.CAE.Connections.Folder@endlink)  the added folder </param>
    def AddFolder(self, subfolder: Folder) -> None:
        """
         Add a subfolder to this folder. The subfolder is moved if found in other folder. 
        """
        pass
    
    ##  Clone a @link CAE::Connections::IConnection CAE::Connections::IConnection@endlink  in the same folder of the specified connection 
    ##  @return newConnection (@link IConnection NXOpen.CAE.Connections.IConnection@endlink):  the created connection .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ## <param name="originalConnection"> (@link IConnection NXOpen.CAE.Connections.IConnection@endlink)  the original connection </param>
    ## <param name="newConnectionName"> (str)  name of new connection </param>
    def CloneConnection(self, originalConnection: IConnection, newConnectionName: str) -> IConnection:
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
    ## 
    ## <param name="type"> (@link ConnectionType NXOpen.CAE.Connections.ConnectionType@endlink) </param>
    ## <param name="name"> (str)  name of the connection </param>
    def CreateConnection(self, type: ConnectionType, name: str) -> IConnection:
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
    ## 
    ## <param name="name"> (str)   Name that the created folder should have </param>
    def CreateFolder(self, name: str) -> Folder:
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
    ## 
    ## <param name="file"> (str)  name of the wcd import file </param>
    ## <param name="matfile"> (str)  name of the material    file </param>
    ## <param name="pDbData"> (@link ConnectionDBItemData NXOpen.CAE.Connections.ConnectionDBItemData@endlink)  connection db data pointer </param>
    def CreateSpotWeldConnectionFromWcdFile(self, file: str, matfile: str, pDbData: ConnectionDBItemData) -> List[SpotWeld]:
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
    ## 
    ## <param name="objects"> (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink)  the objects to delete </param>
    def DeleteObjects(self, objects: List[NXOpen.NXObject]) -> None:
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
    ## 
    ## <param name="propertyList"> (@link NXOpen.CAE.CaeDataContainer NXOpen.CAE.CaeDataContainer@endlink)  the import parameters see @link CAE::CaeSession::GetDataContainer CAE::CaeSession::GetDataContainer@endlink . </param>
    def DetectConnections(self, propertyList: NXOpen.CAE.CaeDataContainer) -> List[IConnection]:
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
    ## 
    ## <param name="connections"> (@link IConnection List[NXOpen.CAE.Connections.IConnection]@endlink)  the connections to export </param>
    ## <param name="propertyList"> (@link NXOpen.CAE.CaeDataContainer NXOpen.CAE.CaeDataContainer@endlink)  the import parameters see @link CAE::CaeSession::GetDataContainer CAE::CaeSession::GetDataContainer@endlink . </param>
    def ExportConnectionsToXMcf(self, connections: List[IConnection], propertyList: NXOpen.CAE.CaeDataContainer) -> None:
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
    ## 
    ## <param name="filePath"> (str)  filepath of the exported file </param>
    ## <param name="outputLength"> (@link NXOpen.Unit NXOpen.Unit@endlink)  the length unit to be used in the output file </param>
    ## <param name="connections"> (@link IConnection List[NXOpen.CAE.Connections.IConnection]@endlink)  connections to export </param>
    def ExportSpotWeldConnectionsToWcdFile(self, filePath: str, outputLength: NXOpen.Unit, connections: List[IConnection]) -> None:
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
    def GetAllConnections(self) -> List[IConnection]:
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
    def GetChildFolders(self) -> List[Folder]:
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
    def GetConnections(self) -> List[IConnection]:
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
    ## 
    ## <param name="file"> (str)  name of the import file </param>
    ## <param name="inputFileUnit"> (@link NXOpen.Unit NXOpen.Unit@endlink)  the length unit used in the input file </param>
    def ImportConnectionsFromMcf(self, file: str, inputFileUnit: NXOpen.Unit) -> List[IConnection]:
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
    ## 
    ## <param name="propertyList"> (@link NXOpen.CAE.CaeDataContainer NXOpen.CAE.CaeDataContainer@endlink)  the import parameters see @link CAE::CaeSession::GetDataContainer CAE::CaeSession::GetDataContainer@endlink . </param>
    def ImportConnectionsFromXMcf(self, propertyList: NXOpen.CAE.CaeDataContainer) -> List[IConnection]:
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
    ## 
    ## <param name="lengthUnit"> (@link NXOpen.Unit NXOpen.Unit@endlink)  The length unit </param>
    ## <param name="massUnit"> (@link NXOpen.Unit NXOpen.Unit@endlink)  The mass unit </param>
    ## <param name="reportErrors"> (bool) </param>
    ## <param name="iConnections"> (@link LMIEConnection List[NXOpen.CAE.Connections.LMIEConnection]@endlink)  The array of input lumped mass connections in intermediate representation </param>
    def ImportLumpedMassFromInterchangeData(self, lengthUnit: NXOpen.Unit, massUnit: NXOpen.Unit, reportErrors: bool, iConnections: List[LMIEConnection]) -> List[LumpedMass]:
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
    ## 
    ## <param name="file"> (str)  name of the import file </param>
    ## <param name="inputFileUnit"> (@link NXOpen.Unit NXOpen.Unit@endlink)  the length unit used in the input file </param>
    ## <param name="heightType"> (@link HeightType NXOpen.CAE.Connections.HeightType@endlink)  Height type </param>
    ## <param name="heightValue"> (float)  Height value. To be considered only when Height type is JA_CAE_CONNECTIONS_TYPES_HeightType_User </param>
    ## <param name="useInputFileMaterial"> (bool)  flag to indicate whether to use the material(s) defined in the imported input file or not </param>
    ## <param name="userDefinedMaterialType"> (@link MaterialType NXOpen.CAE.Connections.MaterialType@endlink)  the user defined material type </param>
    ## <param name="userDefinedMaterial"> (@link NXOpen.PhysicalMaterial NXOpen.PhysicalMaterial@endlink)  the user defined material, only use when the user defined material type is JA_CAE_CONNECTIONS_TYPES_MaterialType_User </param>
    def ImportSpotWeldFromWcdWithHeightAndMaterial(self, file: str, inputFileUnit: NXOpen.Unit, heightType: HeightType, heightValue: float, useInputFileMaterial: bool, userDefinedMaterialType: MaterialType, userDefinedMaterial: NXOpen.PhysicalMaterial) -> List[SpotWeld]:
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
    ## 
    ## <param name="connections"> (@link IConnection List[NXOpen.CAE.Connections.IConnection]@endlink)  the array of connections that are moved </param>
    def MoveConnectionsToThisFolder(self, connections: List[IConnection]) -> None:
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
    ##  Returns the Group used for creating the location.  
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
         Returns the Group used for creating the location.  
          
                        If the location type is not a Group, this method will raise an error.   
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.CAE.CaeGroup NXOpen.CAE.CaeGroup@endlink) Group

    ##  Returns the Group used for creating the location.  
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
         Returns the Group used for creating the location.  
          
                        If the location type is not a Group, this method will raise an error.   
         
        """
        pass
    
##  Head diameter definition types 
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## User</term><description> 
##  User defined diameter </description> </item><item><term> 
## FactorOfDiameter</term><description> 
##  User defined relationship with bolt diameter </description> </item></list>
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
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## Undefined</term><description> 
##  Undefined height type, used for connections that don't use this parameter </description> </item><item><term> 
## User</term><description> 
##  User defined thickness </description> </item><item><term> 
## MeanOfFlangesThickness</term><description> 
##  Mean of flanges thickness </description> </item><item><term> 
## DistanceBetweenFlanges</term><description> 
##  Distance between flanges </description> </item><item><term> 
## DistanceBetweenFlangesMeanOfFlangesThickness</term><description> 
##  Distance between flanges - Mean of flanges thickness </description> </item><item><term> 
## DistanceBetweenFlangesMaxOfFlangesThickness</term><description> 
##  Distance between flanges - Max of flanges thickness </description> </item><item><term> 
## DistanceBetweenFlangesAndMeanOfFlangesThickness</term><description> 
##  Distance between flanges + Mean of the Flange Thickness </description> </item><item><term> 
## SumOfFlangesThickness</term><description> 
##  Sum of the Flange Thickness </description> </item></list>
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
    ##  Returns the bushing type   
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
         Returns the bushing type   
            
         
        """
        pass
    
    ## Setter for property: (@link BushingType NXOpen.CAE.Connections.BushingType@endlink) BushingType

    ##  Returns the bushing type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @BushingType.setter
    def BushingType(self, bushingType: BushingType):
        """
        Setter for property: (@link BushingType NXOpen.CAE.Connections.BushingType@endlink) BushingType
         Returns the bushing type   
            
         
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
    ##  Returnsthe connection is part or not of a mesh object
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
         Returnsthe connection is part or not of a mesh object
                      
            
         
        """
        pass
    
    ## Getter for property: (@link UniversalConnectionState NXOpen.CAE.Connections.UniversalConnectionState@endlink) State
    ##  Returnsthe status of the connection
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
         Returnsthe status of the connection
                      
            
         
        """
        pass
    
    ## Getter for property: (str) UserDescription
    ##  Returns the connection user description   
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
         Returns the connection user description   
            
         
        """
        pass
    
    ## Setter for property: (str) UserDescription

    ##  Returns the connection user description   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @UserDescription.setter
    def UserDescription(self, description: str):
        """
        Setter for property: (str) UserDescription
         Returns the connection user description   
            
         
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
    ##  Returns the csys   
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
         Returns the csys   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) Csys

    ##  Returns the csys   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @Csys.setter
    def Csys(self, csys: NXOpen.CoordinateSystem):
        """
        Setter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) Csys
         Returns the csys   
            
         
        """
        pass
    
    ## Getter for property: (@link CsysType NXOpen.CAE.Connections.CsysType@endlink) CsysType
    ##  Returns the csys type   
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
         Returns the csys type   
            
         
        """
        pass
    
    ## Setter for property: (@link CsysType NXOpen.CAE.Connections.CsysType@endlink) CsysType

    ##  Returns the csys type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @CsysType.setter
    def CsysType(self, csysType: CsysType):
        """
        Setter for property: (@link CsysType NXOpen.CAE.Connections.CsysType@endlink) CsysType
         Returns the csys type   
            
         
        """
        pass
    
    ##  Gets supported csys types of connection. 
    ##  @return types (@link CsysType List[NXOpen.CAE.Connections.CsysType]@endlink):  Supported CSys Types .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    @abstractmethod
    def GetSupportedCsysTypes(self) -> List[CsysType]:
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
    ##  Returns the R cylindrical stiffness dynamic   
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
         Returns the R cylindrical stiffness dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RCylindricalStiffnessDynamic

    ##  Returns the R cylindrical stiffness dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @RCylindricalStiffnessDynamic.setter
    def RCylindricalStiffnessDynamic(self, rDynamic: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RCylindricalStiffnessDynamic
         Returns the R cylindrical stiffness dynamic   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RrCylindricalStiffnessDynamic
    ##  Returns the RR cylindrical stiffness dynamic   
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
         Returns the RR cylindrical stiffness dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RrCylindricalStiffnessDynamic

    ##  Returns the RR cylindrical stiffness dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @RrCylindricalStiffnessDynamic.setter
    def RrCylindricalStiffnessDynamic(self, rrDynamic: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RrCylindricalStiffnessDynamic
         Returns the RR cylindrical stiffness dynamic   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzCylindricalStiffnessDynamic
    ##  Returns the RZ cylindrical stiffness dynamic   
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
         Returns the RZ cylindrical stiffness dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzCylindricalStiffnessDynamic

    ##  Returns the RZ cylindrical stiffness dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @RzCylindricalStiffnessDynamic.setter
    def RzCylindricalStiffnessDynamic(self, rzDynamic: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzCylindricalStiffnessDynamic
         Returns the RZ cylindrical stiffness dynamic   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZCylindricalStiffnessDynamic
    ##  Returns the Z cylindrical stiffness dynamic   
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
         Returns the Z cylindrical stiffness dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZCylindricalStiffnessDynamic

    ##  Returns the Z cylindrical stiffness dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @ZCylindricalStiffnessDynamic.setter
    def ZCylindricalStiffnessDynamic(self, zDynamic: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZCylindricalStiffnessDynamic
         Returns the Z cylindrical stiffness dynamic   
            
         
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
    ##  Returns the R cylindrical stiffness constant   
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
         Returns the R cylindrical stiffness constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RrCylindricalStiffnessConstant
    ##  Returns the RR cylindrical stiffness constant   
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
         Returns the RR cylindrical stiffness constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RzCylindricalStiffnessConstant
    ##  Returns the RZ cylindrical stiffness constant   
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
         Returns the RZ cylindrical stiffness constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ZCylindricalStiffnessConstant
    ##  Returns the Z cylindrical stiffness constant   
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
         Returns the Z cylindrical stiffness constant   
            
         
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
    ##  Returns the R cylindrical structural damping dynamic   
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
         Returns the R cylindrical structural damping dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RCylindricalStructuralDampingDynamic

    ##  Returns the R cylindrical structural damping dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @RCylindricalStructuralDampingDynamic.setter
    def RCylindricalStructuralDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RCylindricalStructuralDampingDynamic
         Returns the R cylindrical structural damping dynamic   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RrCylindricalStructuralDampingDynamic
    ##  Returns the RR cylindrical structural damping dynamic   
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
         Returns the RR cylindrical structural damping dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RrCylindricalStructuralDampingDynamic

    ##  Returns the RR cylindrical structural damping dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @RrCylindricalStructuralDampingDynamic.setter
    def RrCylindricalStructuralDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RrCylindricalStructuralDampingDynamic
         Returns the RR cylindrical structural damping dynamic   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzCylindricalStructuralDampingDynamic
    ##  Returns the RZ cylindrical structural damping dynamic   
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
         Returns the RZ cylindrical structural damping dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzCylindricalStructuralDampingDynamic

    ##  Returns the RZ cylindrical structural damping dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @RzCylindricalStructuralDampingDynamic.setter
    def RzCylindricalStructuralDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzCylindricalStructuralDampingDynamic
         Returns the RZ cylindrical structural damping dynamic   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZCylindricalStructuralDampingDynamic
    ##  Returns the Z cylindrical structural damping dynamic   
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
         Returns the Z cylindrical structural damping dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZCylindricalStructuralDampingDynamic

    ##  Returns the Z cylindrical structural damping dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @ZCylindricalStructuralDampingDynamic.setter
    def ZCylindricalStructuralDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZCylindricalStructuralDampingDynamic
         Returns the Z cylindrical structural damping dynamic   
            
         
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
    ##  Returns the R cylindrical structural damping constant   
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
         Returns the R cylindrical structural damping constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RrCylindricalStructuralDampingConstant
    ##  Returns the RR structural damping constant   
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
         Returns the RR structural damping constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RzCylindricalStructuralDampingConstant
    ##  Returns the RZ structural damping constant   
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
         Returns the RZ structural damping constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ZCylindricalStructuralDampingConstant
    ##  Returns the Z cylindrical structural damping constant   
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
         Returns the Z cylindrical structural damping constant   
            
         
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
    ##  Returns the R cylindrical viscous damping dynamic   
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
         Returns the R cylindrical viscous damping dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RCylindricalViscousDampingDynamic

    ##  Returns the R cylindrical viscous damping dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @RCylindricalViscousDampingDynamic.setter
    def RCylindricalViscousDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RCylindricalViscousDampingDynamic
         Returns the R cylindrical viscous damping dynamic   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RrCylindricalViscousDampingDynamic
    ##  Returns the RR cylindrical viscous damping dynamic   
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
         Returns the RR cylindrical viscous damping dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RrCylindricalViscousDampingDynamic

    ##  Returns the RR cylindrical viscous damping dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @RrCylindricalViscousDampingDynamic.setter
    def RrCylindricalViscousDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RrCylindricalViscousDampingDynamic
         Returns the RR cylindrical viscous damping dynamic   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzCylindricalViscousDampingDynamic
    ##  Returns the RZ cylindrical viscous damping dynamic   
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
         Returns the RZ cylindrical viscous damping dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzCylindricalViscousDampingDynamic

    ##  Returns the RZ cylindrical viscous damping dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @RzCylindricalViscousDampingDynamic.setter
    def RzCylindricalViscousDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzCylindricalViscousDampingDynamic
         Returns the RZ cylindrical viscous damping dynamic   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZCylindricalViscousDampingDynamic
    ##  Returns the Z cylindrical viscous damping dynamic   
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
         Returns the Z cylindrical viscous damping dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZCylindricalViscousDampingDynamic

    ##  Returns the Z cylindrical viscous damping dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @ZCylindricalViscousDampingDynamic.setter
    def ZCylindricalViscousDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZCylindricalViscousDampingDynamic
         Returns the Z cylindrical viscous damping dynamic   
            
         
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
    ##  Returns the R cylindrical viscous damping constant   
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
         Returns the R cylindrical viscous damping constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RrCylindricalViscousDampingConstant
    ##  Returns the RR cylindrical viscous damping constant   
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
         Returns the RR cylindrical viscous damping constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RzCylindricalViscousDampingConstant
    ##  Returns the RZ cylindrical viscous damping constant   
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
         Returns the RZ cylindrical viscous damping constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ZCylindricalViscousDampingConstant
    ##  Returns the Z cylindrical viscous damping constant   
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
         Returns the Z cylindrical viscous damping constant   
            
         
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
    ##  Returns the coefficient for formula defined diameter   
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
         Returns the coefficient for formula defined diameter   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Diameter
    ##  Returns the connection diameter   
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
         Returns the connection diameter   
            
         
        """
        pass
    
    ## Getter for property: (@link DiameterType NXOpen.CAE.Connections.DiameterType@endlink) DiameterType
    ##  Returns the connection diameter type   
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
         Returns the connection diameter type   
            
         
        """
        pass
    
    ## Setter for property: (@link DiameterType NXOpen.CAE.Connections.DiameterType@endlink) DiameterType

    ##  Returns the connection diameter type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @DiameterType.setter
    def DiameterType(self, diameterType: DiameterType):
        """
        Setter for property: (@link DiameterType NXOpen.CAE.Connections.DiameterType@endlink) DiameterType
         Returns the connection diameter type   
            
         
        """
        pass
    
    ## Getter for property: (str) TableFile
    ##  Returns the table file used to compute the diameter   
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
         Returns the table file used to compute the diameter   
            
         
        """
        pass
    
    ## Setter for property: (str) TableFile

    ##  Returns the table file used to compute the diameter   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @TableFile.setter
    def TableFile(self, tableFile: str):
        """
        Setter for property: (str) TableFile
         Returns the table file used to compute the diameter   
            
         
        """
        pass
    
    ##  Gets manual adjustent state. 
    ##  @return state (bool): .
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: None.
    @abstractmethod
    def GetManualAdjustment(self) -> bool:
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
    @abstractmethod
    def GetManualAdjustmentFactor(self) -> NXOpen.Expression:
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
    @abstractmethod
    def GetSupportedDiameterTypes(self) -> List[DiameterType]:
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
    def SetManualAdjustment(self, state: bool) -> None:
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
    ##  Returns the degrees of freedom combination type   
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
         Returns the degrees of freedom combination type   
            
         
        """
        pass
    
    ## Setter for property: (@link DofCombination NXOpen.CAE.Connections.DofCombination@endlink) DofCombination

    ##  Returns the degrees of freedom combination type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @DofCombination.setter
    def DofCombination(self, type: DofCombination):
        """
        Setter for property: (@link DofCombination NXOpen.CAE.Connections.DofCombination@endlink) DofCombination
         Returns the degrees of freedom combination type   
            
         
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
    def GetDof(self, dof: Dof) -> DofType:
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
    def SetDof(self, dof: Dof, type: DofType) -> None:
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
    ##  Returns the number of flanges.  
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
         Returns the number of flanges.  
           When changing the number of flanges this is not applied till an update is performed by calling @link Update::DoUpdate Update::DoUpdate@endlink    
         
        """
        pass
    
    ## Setter for property: (int) NumberOfFlanges

    ##  Returns the number of flanges.  
    ##    When changing the number of flanges this is not applied till an update is performed by calling @link Update::DoUpdate Update::DoUpdate@endlink    
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @NumberOfFlanges.setter
    def NumberOfFlanges(self, numberOfFlanges: int):
        """
        Setter for property: (int) NumberOfFlanges
         Returns the number of flanges.  
           When changing the number of flanges this is not applied till an update is performed by calling @link Update::DoUpdate Update::DoUpdate@endlink    
         
        """
        pass
    
    ##  Add entities to flange. Changes are not applied till an update is performed by calling @link Update::DoUpdate Update::DoUpdate@endlink  
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ## <param name="flangeIndex"> (int) </param>
    ## <param name="entities"> (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink)  Flange entities </param>
    @abstractmethod
    def AddFlangeEntities(self, flangeIndex: int, entities: List[NXOpen.TaggedObject]) -> None:
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
    def GetFlangeEntities(self, flangeIndex: int) -> List[NXOpen.TaggedObject]:
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
    @abstractmethod
    def GetMaxNumberOfFlanges(self) -> int:
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
    @abstractmethod
    def GetMinNumberOfFlanges(self) -> int:
        """
         Retrieve the minimum number of flanges supported by this connection 
         @return number (int): .
        """
        pass
    
    ##  Remove entities from flange. Changes are not applied till an update is performed by calling @link Update::DoUpdate Update::DoUpdate@endlink  
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ## <param name="flangeIndex"> (int) </param>
    ## <param name="entities"> (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink)  Flange entities </param>
    @abstractmethod
    def RemoveFlangeEntities(self, flangeIndex: int, entities: List[NXOpen.TaggedObject]) -> None:
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
    ##  Returns the radius characteristic length used by Revolute and Spherical Kinematic   
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
         Returns the radius characteristic length used by Revolute and Spherical Kinematic   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) FrictionCoefficient
    ##  Returns the friction coefficient   
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
         Returns the friction coefficient   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) TighteningForce
    ##  Returns the tightening force   
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
         Returns the tightening force   
            
         
        """
        pass
    
    ## Getter for property: (bool) UseFriction
    ##  Returns the flag indicating whether to use friction parameters or not   
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
         Returns the flag indicating whether to use friction parameters or not   
            
         
        """
        pass
    
    ## Setter for property: (bool) UseFriction

    ##  Returns the flag indicating whether to use friction parameters or not   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @UseFriction.setter
    def UseFriction(self, useFriction: bool):
        """
        Setter for property: (bool) UseFriction
         Returns the flag indicating whether to use friction parameters or not   
            
         
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
    ##  Returns the height value   
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
         Returns the height value   
            
         
        """
        pass
    
    ## Getter for property: (@link HeightType NXOpen.CAE.Connections.HeightType@endlink) HeightType
    ##  Returns the connection height type   
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
         Returns the connection height type   
            
         
        """
        pass
    
    ## Setter for property: (@link HeightType NXOpen.CAE.Connections.HeightType@endlink) HeightType

    ##  Returns the connection height type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @HeightType.setter
    def HeightType(self, heightType: HeightType):
        """
        Setter for property: (@link HeightType NXOpen.CAE.Connections.HeightType@endlink) HeightType
         Returns the connection height type   
            
         
        """
        pass
    
    ##  Gets supported height types of connection. 
    ##  @return types (@link HeightType List[NXOpen.CAE.Connections.HeightType]@endlink):  Supported CSys Types .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    @abstractmethod
    def GetSupportedHeightTypes(self) -> List[HeightType]:
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
    ## 
    ## <param name="feature"> (@link NXOpen.Features.Feature NXOpen.Features.Feature@endlink)  The join feature </param>
    ## <param name="component"> (@link NXOpen.Assemblies.Component NXOpen.Assemblies.Component@endlink)  The CAD component of the join feature </param>
    @abstractmethod
    def AddJoinData(self, feature: NXOpen.Features.Feature, component: NXOpen.Assemblies.Component) -> None:
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
    @abstractmethod
    def GetAllJoinFeatures(self) -> Tuple[List[NXOpen.Features.Feature], List[NXOpen.Assemblies.Component]]:
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
    ## 
    ## <param name="index"> (int)  The join data index </param>
    @abstractmethod
    def GetJoinFeature(self, index: int) -> Tuple[NXOpen.Features.Feature, NXOpen.Assemblies.Component]:
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
    @abstractmethod
    def GetNumberOfJoinData(self) -> int:
        """
         Get the number of join data from the connection 
         @return numberOfJoinData (int):  The number of join data .
        """
        pass
    
    ##  Remove all join data from the connection 
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    @abstractmethod
    def RemoveAllJoinData(self) -> None:
        """
         Remove all join data from the connection 
        """
        pass
    
    ##  Add a join data to the connection 
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ## <param name="feature"> (@link NXOpen.Features.Feature NXOpen.Features.Feature@endlink)  The join feature </param>
    ## <param name="component"> (@link NXOpen.Assemblies.Component NXOpen.Assemblies.Component@endlink)  The CAD component of the join feature </param>
    @abstractmethod
    def RemoveJoinData(self, feature: NXOpen.Features.Feature, component: NXOpen.Assemblies.Component) -> None:
        """
         Add a join data to the connection 
        """
        pass
    
    ##  Remove a join data from the connection 
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ## <param name="index"> (int)  The join data index </param>
    @abstractmethod
    def RemoveJoinDataByIndex(self, index: int) -> None:
        """
         Remove a join data from the connection 
        """
        pass
    
    ##  Set the join data of the connection 
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ## <param name="features"> (@link NXOpen.Features.Feature List[NXOpen.Features.Feature]@endlink)  The join features </param>
    ## <param name="components"> (@link NXOpen.Assemblies.Component List[NXOpen.Assemblies.Component]@endlink)  The CAD components of the join features </param>
    @abstractmethod
    def SetJoinData(self, features: List[NXOpen.Features.Feature], components: List[NXOpen.Assemblies.Component]) -> None:
        """
         Set the join data of the connection 
        """
        pass
    
    ##  Unlink all join data from the connection 
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    @abstractmethod
    def UnlinkJoinData(self) -> None:
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
    ##  Returns the discretization method   
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
         Returns the discretization method   
            
         
        """
        pass
    
    ## Setter for property: (@link DiscretizationMethod NXOpen.CAE.Connections.DiscretizationMethod@endlink) DiscretizationMethod

    ##  Returns the discretization method   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @DiscretizationMethod.setter
    def DiscretizationMethod(self, method: DiscretizationMethod):
        """
        Setter for property: (@link DiscretizationMethod NXOpen.CAE.Connections.DiscretizationMethod@endlink) DiscretizationMethod
         Returns the discretization method   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) DistanceFromStart
    ##  Returns the line Discretization distance from start   
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
         Returns the line Discretization distance from start   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) DistanceToEnd
    ##  Returns the line Discretization distance to end   
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
         Returns the line Discretization distance to end   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) LengthStep
    ##  Returns the line Discretization length step   
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
         Returns the line Discretization length step   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxLengthStep
    ##  Returns the line Discretization max length step   
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
         Returns the line Discretization max length step   
            
         
        """
        pass
    
    ## Getter for property: (int) NumberOfDiscretizationPoints
    ##  Returns the number of connections   
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
         Returns the number of connections   
            
         
        """
        pass
    
    ## Setter for property: (int) NumberOfDiscretizationPoints

    ##  Returns the number of connections   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @NumberOfDiscretizationPoints.setter
    def NumberOfDiscretizationPoints(self, num: int):
        """
        Setter for property: (int) NumberOfDiscretizationPoints
         Returns the number of connections   
            
         
        """
        pass
    
    ## Getter for property: (bool) UseMaxLengthStep
    ##  Returns the usage of max length step   
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
         Returns the usage of max length step   
            
         
        """
        pass
    
    ## Setter for property: (bool) UseMaxLengthStep

    ##  Returns the usage of max length step   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @UseMaxLengthStep.setter
    def UseMaxLengthStep(self, use: bool):
        """
        Setter for property: (bool) UseMaxLengthStep
         Returns the usage of max length step   
            
         
        """
        pass
    
    ## Getter for property: (bool) UseOriginalNodesOfConnection
    ##  Returns the usage of original nodes of connection   
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
         Returns the usage of original nodes of connection   
            
         
        """
        pass
    
    ## Setter for property: (bool) UseOriginalNodesOfConnection

    ##  Returns the usage of original nodes of connection   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @UseOriginalNodesOfConnection.setter
    def UseOriginalNodesOfConnection(self, use: bool):
        """
        Setter for property: (bool) UseOriginalNodesOfConnection
         Returns the usage of original nodes of connection   
            
         
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
    def GetOffsetDistance(self, lindeDefinitionIndex: int) -> NXOpen.Expression:
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
    def GetOffsetVector(self, lindeDefinitionIndex: int) -> NXOpen.Direction:
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
    def SetOffsetVector(self, lindeDefinitionIndex: int, offsetvector: NXOpen.Direction) -> None:
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
    ## 
    ## <param name="indexOfDefinition"> (int)  The index of definition  </param>
    ## <param name="index"> (int)  The location index </param>
    @abstractmethod
    def ConvertLocationToCoordinatesType(self, indexOfDefinition: int, index: int) -> Location:
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
    ## 
    ## <param name="indexOfDefinition"> (int)  The index of definition  </param>
    ## <param name="indexOfLocation"> (int)  The location index </param>
    @abstractmethod
    def GetLocation(self, indexOfDefinition: int, indexOfLocation: int) -> Location:
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
    @abstractmethod
    def GetNumberOfDefinitions(self) -> int:
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
    ## 
    ## <param name="indexOfDefinition"> (int)  The index of definition  </param>
    @abstractmethod
    def GetNumberOfLocations(self, indexOfDefinition: int) -> int:
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
    ## 
    ## <param name="indexOfDefinition"> (int)  The index of definition  </param>
    ## <param name="indexOfLocation"> (int)  The index of location </param>
    ## <param name="numberOfPositions"> (int)  The number of positions to move the location </param>
    @abstractmethod
    def MoveLocation(self, indexOfDefinition: int, indexOfLocation: int, numberOfPositions: int) -> bool:
        """
         Move the location by number of positions 
         @return success (bool):  The operation result .
        """
        pass
    
    ##  Remove a location from connection location list 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ## <param name="indexOfDefinition"> (int)  The index of definition  </param>
    ## <param name="indexOfLocation"> (int)  The location index </param>
    @abstractmethod
    def RemoveLocation(self, indexOfDefinition: int, indexOfLocation: int) -> None:
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
    ## 
    ## <param name="indexOfDefinition"> (int)  The index of definition  </param>
    ## <param name="selectionRecipe"> (@link NXOpen.CAE.SelectionRecipe NXOpen.CAE.SelectionRecipe@endlink)  Selection Recipe used for location creation </param>
    @abstractmethod
    def AddLocationSelectionRecipe(self, indexOfDefinition: int, selectionRecipe: NXOpen.CAE.SelectionRecipe) -> SelectionRecipeLocation:
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
    ## 
    ## <param name="indexOfDefinition"> (int)  The index of definition  </param>
    ## <param name="coordinates"> (@link NXOpen.Point3d NXOpen.Point3d@endlink)  Coordinates </param>
    @abstractmethod
    def AddLocationCoordinates(self, indexOfDefinition: int, coordinates: NXOpen.Point3d) -> CoordinatesLocation:
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
    ## 
    ## <param name="indexOfDefinition"> (int)  The index of definition  </param>
    ## <param name="node"> (@link NXOpen.CAE.FENode NXOpen.CAE.FENode@endlink)  Node used for location </param>
    @abstractmethod
    def AddLocationNode(self, indexOfDefinition: int, node: NXOpen.CAE.FENode) -> NodeLocation:
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
    ## 
    ## <param name="indexOfDefinition"> (int)  The index of definition  </param>
    ## <param name="point"> (@link NXOpen.Point NXOpen.Point@endlink)  Point used for location creation </param>
    @abstractmethod
    def AddLocationPoint(self, indexOfDefinition: int, point: NXOpen.Point) -> PointLocation:
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
    ## 
    ## <param name="indexOfDefinition"> (int)  The index of definition  </param>
    ## <param name="point"> (@link NXOpen.Point NXOpen.Point@endlink)  Location Coordinates </param>
    ## <param name="direction"> (@link NXOpen.Point NXOpen.Point@endlink)  Direction Point </param>
    @abstractmethod
    def AddLocationCoordinatesWithDirectionCoordinates(self, indexOfDefinition: int, point: NXOpen.Point, direction: NXOpen.Point) -> LocationWithDir:
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
    ## 
    ## <param name="indexOfDefinition"> (int)  The index of definition  </param>
    ## <param name="startSelectionRecipe"> (@link NXOpen.CAE.SelectionRecipe NXOpen.CAE.SelectionRecipe@endlink)  The start Selection Recipe </param>
    ## <param name="endSelectionRecipe"> (@link NXOpen.CAE.SelectionRecipe NXOpen.CAE.SelectionRecipe@endlink)  The end Selection Recipe </param>
    @abstractmethod
    def AddLocationCoordinatesWithDirectionSelectionRecipes(self, indexOfDefinition: int, startSelectionRecipe: NXOpen.CAE.SelectionRecipe, endSelectionRecipe: NXOpen.CAE.SelectionRecipe) -> LocationWithDir:
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
    ## 
    ## <param name="indexOfDefinition"> (int)  The index of definition  </param>
    ## <param name="masterPoint"> (@link NXOpen.Point NXOpen.Point@endlink)  Location Coordinates </param>
    ## <param name="direction"> (@link NXOpen.Direction NXOpen.Direction@endlink)  Direction direction </param>
    @abstractmethod
    def AddLocationCoordinatesWithDirectionVector(self, indexOfDefinition: int, masterPoint: NXOpen.Point, direction: NXOpen.Direction) -> LocationWithDir:
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
    ## 
    ## <param name="indexOfDefinition"> (int) </param>
    ## <param name="curve"> (@link NXOpen.IBaseCurve NXOpen.IBaseCurve@endlink)  Curve used for location creation </param>
    @abstractmethod
    def AddLocationCurve(self, indexOfDefinition: int, curve: NXOpen.IBaseCurve) -> CurveLocation:
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
    ## 
    ## <param name="indexOfDefinition"> (int) </param>
    ## <param name="edges"> (@link NXOpen.CAE.FEElemEdge List[NXOpen.CAE.FEElemEdge]@endlink)  Edges used for location </param>
    @abstractmethod
    def AddLocationFeEdges(self, indexOfDefinition: int, edges: List[NXOpen.CAE.FEElemEdge]) -> FeEdgesLocation:
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
    ## 
    ## <param name="indexOfDefinition"> (int) </param>
    ## <param name="group"> (@link NXOpen.CAE.CaeGroup NXOpen.CAE.CaeGroup@endlink)  Group used for location creation </param>
    @abstractmethod
    def AddLocationGroup(self, indexOfDefinition: int, group: NXOpen.CAE.CaeGroup) -> GroupLocation:
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
    ## 
    ## <param name="indexOfDefinition"> (int) </param>
    ## <param name="coordinates"> (@link NXOpen.Point3d List[NXOpen.Point3d]@endlink)  The location coordinates </param>
    @abstractmethod
    def AddLocationSeriesOfCoordinates(self, indexOfDefinition: int, coordinates: List[NXOpen.Point3d]) -> CoordinatesSeriesLocation:
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
    ## 
    ## <param name="indexOfDefinition"> (int)  The index of definition  </param>
    ## <param name="nodes"> (@link NXOpen.CAE.FENode List[NXOpen.CAE.FENode]@endlink)  Nodes used for location </param>
    @abstractmethod
    def AddLocationSeriesOfNodes(self, indexOfDefinition: int, nodes: List[NXOpen.CAE.FENode]) -> NodeSeriesLocation:
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
    ## 
    ## <param name="indexOfDefinition"> (int)  The index of definition  </param>
    ## <param name="points"> (@link NXOpen.Point List[NXOpen.Point]@endlink)  Points used for location </param>
    @abstractmethod
    def AddLocationSeriesOfPoints(self, indexOfDefinition: int, points: List[NXOpen.Point]) -> PointSeriesLocation:
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
    ##  Returns the isMassOnBothTargets   
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
         Returns the isMassOnBothTargets   
            
         
        """
        pass
    
    ## Setter for property: (bool) IsMassOnBothTargets

    ##  Returns the isMassOnBothTargets   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @IsMassOnBothTargets.setter
    def IsMassOnBothTargets(self, isMassOnBothTargets: bool):
        """
        Setter for property: (bool) IsMassOnBothTargets
         Returns the isMassOnBothTargets   
            
         
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
    ##  Returns the expansion radius factor   
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
         Returns the expansion radius factor   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ExpansionRadiusTolerance
    ##  Returns the expansion radius   
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
         Returns the expansion radius   
            
         
        """
        pass
    
    ## Getter for property: (@link MassConnectivityType NXOpen.CAE.Connections.MassConnectivityType@endlink) MassConnectivityType
    ##  Returns the mass connection type   
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
         Returns the mass connection type   
            
         
        """
        pass
    
    ## Setter for property: (@link MassConnectivityType NXOpen.CAE.Connections.MassConnectivityType@endlink) MassConnectivityType

    ##  Returns the mass connection type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @MassConnectivityType.setter
    def MassConnectivityType(self, type: MassConnectivityType):
        """
        Setter for property: (@link MassConnectivityType NXOpen.CAE.Connections.MassConnectivityType@endlink) MassConnectivityType
         Returns the mass connection type   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxDistanceTolerance
    ##  Returns the maximum distance from definition point to center of support element   
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
         Returns the maximum distance from definition point to center of support element   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) PanelSearchDistance
    ##  Returns the panel search distance   
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
         Returns the panel search distance   
            
         
        """
        pass
    
    ## Getter for property: (@link PanelSearchType NXOpen.CAE.Connections.PanelSearchType@endlink) PanelSearchType
    ##  Returns the panel search type  
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
         Returns the panel search type  
            
         
        """
        pass
    
    ## Setter for property: (@link PanelSearchType NXOpen.CAE.Connections.PanelSearchType@endlink) PanelSearchType

    ##  Returns the panel search type  
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @PanelSearchType.setter
    def PanelSearchType(self, type: PanelSearchType):
        """
        Setter for property: (@link PanelSearchType NXOpen.CAE.Connections.PanelSearchType@endlink) PanelSearchType
         Returns the panel search type  
            
         
        """
        pass
    
    ## Getter for property: (@link RingSearchType NXOpen.CAE.Connections.RingSearchType@endlink) RingSearchType
    ##  Returns the search tolerance type  
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
         Returns the search tolerance type  
            
         
        """
        pass
    
    ## Setter for property: (@link RingSearchType NXOpen.CAE.Connections.RingSearchType@endlink) RingSearchType

    ##  Returns the search tolerance type  
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @RingSearchType.setter
    def RingSearchType(self, type: RingSearchType):
        """
        Setter for property: (@link RingSearchType NXOpen.CAE.Connections.RingSearchType@endlink) RingSearchType
         Returns the search tolerance type  
            
         
        """
        pass
    
    ##  Add panels 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ## <param name="entities"> (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink)  Panels entities </param>
    @abstractmethod
    def AddPanels(self, entities: List[NXOpen.TaggedObject]) -> None:
        """
         Add panels 
        """
        pass
    
    ##  Gets panels 
    ##  @return entities (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink):  Panels entities .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    @abstractmethod
    def GetPanels(self) -> List[NXOpen.TaggedObject]:
        """
         Gets panels 
         @return entities (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink):  Panels entities .
        """
        pass
    
    ##  Remove panels 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ## <param name="entities"> (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink)  Panels entities </param>
    @abstractmethod
    def RemovePanels(self, entities: List[NXOpen.TaggedObject]) -> None:
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
    ##  Returns the inertia XX.  
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
         Returns the inertia XX.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) InertiaYX
    ##  Returns the inertia XY.  
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
         Returns the inertia XY.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) InertiaYY
    ##  Returns the inertia YY.  
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
         Returns the inertia YY.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) InertiaZX
    ##  Returns the inertia XZ.  
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
         Returns the inertia XZ.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) InertiaZY
    ##  Returns the inertia YZ.  
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
         Returns the inertia YZ.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) InertiaZZ
    ##  Returns the inertia ZZ.  
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
         Returns the inertia ZZ.  
             
         
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
    ##  Returns the mass value   
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
         Returns the mass value   
            
         
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
    ##  Returns the target center   
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
         Returns the target center   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) Center

    ##  Returns the target center   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @Center.setter
    def Center(self, center: NXOpen.TaggedObject):
        """
        Setter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) Center
         Returns the target center   
            
         
        """
        pass
    
    ## Getter for property: (@link LocalSpiderCenterType NXOpen.CAE.Connections.LocalSpiderCenterType@endlink) LocalSpiderCenterType
    ##  Returns the local spider center type   
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
         Returns the local spider center type   
            
         
        """
        pass
    
    ## Setter for property: (@link LocalSpiderCenterType NXOpen.CAE.Connections.LocalSpiderCenterType@endlink) LocalSpiderCenterType

    ##  Returns the local spider center type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @LocalSpiderCenterType.setter
    def LocalSpiderCenterType(self, localSpiderCenterType: LocalSpiderCenterType):
        """
        Setter for property: (@link LocalSpiderCenterType NXOpen.CAE.Connections.LocalSpiderCenterType@endlink) LocalSpiderCenterType
         Returns the local spider center type   
            
         
        """
        pass
    
    ## Getter for property: (@link MassCenterType NXOpen.CAE.Connections.MassCenterType@endlink) MassCenterType
    ##  Returns the mass center type   
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
         Returns the mass center type   
            
         
        """
        pass
    
    ## Setter for property: (@link MassCenterType NXOpen.CAE.Connections.MassCenterType@endlink) MassCenterType

    ##  Returns the mass center type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @MassCenterType.setter
    def MassCenterType(self, massCenterType: MassCenterType):
        """
        Setter for property: (@link MassCenterType NXOpen.CAE.Connections.MassCenterType@endlink) MassCenterType
         Returns the mass center type   
            
         
        """
        pass
    
    ## Getter for property: (@link MassDistributionType NXOpen.CAE.Connections.MassDistributionType@endlink) MassDistributionType
    ##  Returns the mass distribution type   
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
         Returns the mass distribution type   
            
         
        """
        pass
    
    ## Setter for property: (@link MassDistributionType NXOpen.CAE.Connections.MassDistributionType@endlink) MassDistributionType

    ##  Returns the mass distribution type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @MassDistributionType.setter
    def MassDistributionType(self, type: MassDistributionType):
        """
        Setter for property: (@link MassDistributionType NXOpen.CAE.Connections.MassDistributionType@endlink) MassDistributionType
         Returns the mass distribution type   
            
         
        """
        pass
    
    ##  Add entities to mass spider legs. 
    ##             Changes are not applied till an update is performed by calling @link Update::DoUpdate Update::DoUpdate@endlink  
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ## <param name="entities"> (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink)  Mass support entities </param>
    @abstractmethod
    def AddSupportEntities(self, entities: List[NXOpen.TaggedObject]) -> None:
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
    @abstractmethod
    def GetSupportEntities(self) -> List[NXOpen.TaggedObject]:
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
    ## 
    ## <param name="entities"> (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink)  Mass support entities </param>
    @abstractmethod
    def RemoveSupportEntities(self, entities: List[NXOpen.TaggedObject]) -> None:
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
    ## 
    ## <param name="entities"> (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink)  Mass support entities </param>
    @abstractmethod
    def SetSupportEntities(self, entities: List[NXOpen.TaggedObject]) -> None:
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
    ##  Returns the mass type   
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
         Returns the mass type   
            
         
        """
        pass
    
    ## Setter for property: (@link MassType NXOpen.CAE.Connections.MassType@endlink) MassTypeValue

    ##  Returns the mass type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @MassTypeValue.setter
    def MassTypeValue(self, type: MassType):
        """
        Setter for property: (@link MassType NXOpen.CAE.Connections.MassType@endlink) MassTypeValue
         Returns the mass type   
            
         
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
    ##  Returns the connection material   
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
         Returns the connection material   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.PhysicalMaterial NXOpen.PhysicalMaterial@endlink) Material

    ##  Returns the connection material   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @Material.setter
    def Material(self, material: NXOpen.PhysicalMaterial):
        """
        Setter for property: (@link NXOpen.PhysicalMaterial NXOpen.PhysicalMaterial@endlink) Material
         Returns the connection material   
            
         
        """
        pass
    
    ##  Use this function to check if the connection supports having no material 
    ##  @return value (bool): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    @abstractmethod
    def CanHaveNoMaterial(self) -> bool:
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
    @abstractmethod
    def CanInheritMaterial(self) -> bool:
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
    @abstractmethod
    def IsInheritedMaterial(self) -> bool:
        """
         Use this function to check if the connection inherits material from flanges 
         @return value (bool): .
        """
        pass
    
    ##  Use this function to set inherited material to connection 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    @abstractmethod
    def SetInheritedMaterial(self) -> None:
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
    ##  Returns the target center type   
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
         Returns the target center type   
            
         
        """
        pass
    
    ## Setter for property: (@link NodalTargetCenterType NXOpen.CAE.Connections.NodalTargetCenterType@endlink) CenterType

    ##  Returns the target center type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @CenterType.setter
    def CenterType(self, centerType: NodalTargetCenterType):
        """
        Setter for property: (@link NodalTargetCenterType NXOpen.CAE.Connections.NodalTargetCenterType@endlink) CenterType
         Returns the target center type   
            
         
        """
        pass
    
    ##  Get available center types
    ##  @return types (@link NodalTargetCenterType List[NXOpen.CAE.Connections.NodalTargetCenterType]@endlink): .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    @abstractmethod
    def GetAvailableTargetCenterTypes(self) -> List[NodalTargetCenterType]:
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
    @abstractmethod
    def IsCoincidentCenterTypeAllowed(self) -> bool:
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
    ##  Returns the target center   
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
         Returns the target center   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) TargetCenter

    ##  Returns the target center   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @TargetCenter.setter
    def TargetCenter(self, center: NXOpen.TaggedObject):
        """
        Setter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) TargetCenter
         Returns the target center   
            
         
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
    ## 
    ## <param name="entities"> (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink)  Legs entities </param>
    @abstractmethod
    def AddLegsEntities(self, entities: List[NXOpen.TaggedObject]) -> None:
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
    @abstractmethod
    def GetLegsEntities(self) -> List[NXOpen.TaggedObject]:
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
    ## 
    ## <param name="entities"> (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink)  Legs entities </param>
    @abstractmethod
    def RemoveLegsEntities(self, entities: List[NXOpen.TaggedObject]) -> None:
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
    ##  Returns the Expansion Radius   
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
         Returns the Expansion Radius   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ExpansionRadiusFactor
    ##  Returns the Expansion Radius Factor   
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
         Returns the Expansion Radius Factor   
            
         
        """
        pass
    
    ## Getter for property: (@link LocalSpiderCenterType NXOpen.CAE.Connections.LocalSpiderCenterType@endlink) LocalSpiderCenterType
    ##  Returns the Local Spider Center type   
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
         Returns the Local Spider Center type   
            
         
        """
        pass
    
    ## Setter for property: (@link LocalSpiderCenterType NXOpen.CAE.Connections.LocalSpiderCenterType@endlink) LocalSpiderCenterType

    ##  Returns the Local Spider Center type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @LocalSpiderCenterType.setter
    def LocalSpiderCenterType(self, localSpiderCenterType: LocalSpiderCenterType):
        """
        Setter for property: (@link LocalSpiderCenterType NXOpen.CAE.Connections.LocalSpiderCenterType@endlink) LocalSpiderCenterType
         Returns the Local Spider Center type   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxDistance
    ##  Returns the Maximum Distance   
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
         Returns the Maximum Distance   
            
         
        """
        pass
    
    ## Getter for property: (@link PanelSearchType NXOpen.CAE.Connections.PanelSearchType@endlink) PanelSearchType
    ##  Returns the Panel Search type   
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
         Returns the Panel Search type   
            
         
        """
        pass
    
    ## Setter for property: (@link PanelSearchType NXOpen.CAE.Connections.PanelSearchType@endlink) PanelSearchType

    ##  Returns the Panel Search type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @PanelSearchType.setter
    def PanelSearchType(self, panelSearchType: PanelSearchType):
        """
        Setter for property: (@link PanelSearchType NXOpen.CAE.Connections.PanelSearchType@endlink) PanelSearchType
         Returns the Panel Search type   
            
         
        """
        pass
    
    ## Getter for property: (@link RingSearchType NXOpen.CAE.Connections.RingSearchType@endlink) RingSearchType
    ##  Returns the Ring Search type   
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
         Returns the Ring Search type   
            
         
        """
        pass
    
    ## Setter for property: (@link RingSearchType NXOpen.CAE.Connections.RingSearchType@endlink) RingSearchType

    ##  Returns the Ring Search type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @RingSearchType.setter
    def RingSearchType(self, ringSearchType: RingSearchType):
        """
        Setter for property: (@link RingSearchType NXOpen.CAE.Connections.RingSearchType@endlink) RingSearchType
         Returns the Ring Search type   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) SearchTolerance
    ##  Returns the Search Tolerance   
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
         Returns the Search Tolerance   
            
         
        """
        pass
    
    ##  Adds a mesh point location to the target locations list 
    ##  @return location (@link MeshPointLocation NXOpen.CAE.Connections.MeshPointLocation@endlink):  The created mesh point type location .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ## <param name="meshPoint"> (@link NXOpen.CAE.MeshPoint NXOpen.CAE.MeshPoint@endlink)  Mesh Point used for location creation </param>
    @abstractmethod
    def AddLocationMeshPoint(self, meshPoint: NXOpen.CAE.MeshPoint) -> MeshPointLocation:
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
    ## 
    ## <param name="node"> (@link NXOpen.CAE.FENode NXOpen.CAE.FENode@endlink)  Node used for location </param>
    @abstractmethod
    def AddLocationNode(self, node: NXOpen.CAE.FENode) -> NodeLocation:
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
    ## 
    ## <param name="point"> (@link NXOpen.Point NXOpen.Point@endlink)  Point used for location creation </param>
    @abstractmethod
    def AddLocationPoint(self, point: NXOpen.Point) -> PointLocation:
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
    ## 
    ## <param name="selectionRecipe"> (@link NXOpen.CAE.SelectionRecipe NXOpen.CAE.SelectionRecipe@endlink)  Selection Recipe used for location creation </param>
    @abstractmethod
    def AddLocationSelectionRecipe(self, selectionRecipe: NXOpen.CAE.SelectionRecipe) -> SelectionRecipeLocation:
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
    ## 
    ## <param name="entities"> (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink)  Regions entities </param>
    @abstractmethod
    def AddRegionsEntities(self, entities: List[NXOpen.TaggedObject]) -> None:
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
    ## 
    ## <param name="indexOfLocation"> (int)  The location index </param>
    @abstractmethod
    def GetLocation(self, indexOfLocation: int) -> Location:
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
    @abstractmethod
    def GetNumberOfLocations(self) -> int:
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
    @abstractmethod
    def GetRegionsEntities(self) -> List[NXOpen.TaggedObject]:
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
    ## 
    ## <param name="indexOfLocation"> (int)  The location index </param>
    @abstractmethod
    def RemoveLocation(self, indexOfLocation: int) -> None:
        """
         Remove a location from the target locations list 
        """
        pass
    
    ##  Remove regions entities from the target. 
    ##             Changes are not applied till an update is performed by calling @link Update::DoUpdate Update::DoUpdate@endlink  
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ## <param name="entities"> (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink)  Regions entities </param>
    @abstractmethod
    def RemoveRegionsEntities(self, entities: List[NXOpen.TaggedObject]) -> None:
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
    def GetTarget(self, index: int) -> NodalTarget:
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
    def SetTargetType(self, index: int, type: NodalTargetType) -> None:
        """
         Set the target type 
        """
        pass
    
    ##  Swap targets 
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    @abstractmethod
    def SwapTargets(self) -> None:
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
    ##  Returns the pairing method of targets   
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
         Returns the pairing method of targets   
            
         
        """
        pass
    
    ## Setter for property: (@link NodalPairingMethod NXOpen.CAE.Connections.NodalPairingMethod@endlink) PairingMethod

    ##  Returns the pairing method of targets   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @PairingMethod.setter
    def PairingMethod(self, method: NodalPairingMethod):
        """
        Setter for property: (@link NodalPairingMethod NXOpen.CAE.Connections.NodalPairingMethod@endlink) PairingMethod
         Returns the pairing method of targets   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) SearchConeAngle
    ##  Returns the search cone angle   
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
         Returns the search cone angle   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) SearchOrientation
    ##  Returns the pairing search orientation   
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
         Returns the pairing search orientation   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) SearchOrientation

    ##  Returns the pairing search orientation   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @SearchOrientation.setter
    def SearchOrientation(self, orientation: NXOpen.Direction):
        """
        Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) SearchOrientation
         Returns the pairing search orientation   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) SearchRange
    ##  Returns the search range   
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
         Returns the search range   
            
         
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
    ##  Returns the R nonlinear cylindrical damping   
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
         Returns the R nonlinear cylindrical damping   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RNonlinearCylindricalDamping

    ##  Returns the R nonlinear cylindrical damping   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @RNonlinearCylindricalDamping.setter
    def RNonlinearCylindricalDamping(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RNonlinearCylindricalDamping
         Returns the R nonlinear cylindrical damping   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RrNonlinearCylindricalDamping
    ##  Returns the RR nonlinear cylindrical damping   
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
         Returns the RR nonlinear cylindrical damping   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RrNonlinearCylindricalDamping

    ##  Returns the RR nonlinear cylindrical damping   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @RrNonlinearCylindricalDamping.setter
    def RrNonlinearCylindricalDamping(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RrNonlinearCylindricalDamping
         Returns the RR nonlinear cylindrical damping   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzNonlinearCylindricalDamping
    ##  Returns the RZ nonlinear cylindrical damping   
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
         Returns the RZ nonlinear cylindrical damping   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzNonlinearCylindricalDamping

    ##  Returns the RZ nonlinear cylindrical damping   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @RzNonlinearCylindricalDamping.setter
    def RzNonlinearCylindricalDamping(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzNonlinearCylindricalDamping
         Returns the RZ nonlinear cylindrical damping   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZNonlinearCylindricalDamping
    ##  Returns the Z nonlinear cylindrical damping   
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
         Returns the Z nonlinear cylindrical damping   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZNonlinearCylindricalDamping

    ##  Returns the Z nonlinear cylindrical damping   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @ZNonlinearCylindricalDamping.setter
    def ZNonlinearCylindricalDamping(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZNonlinearCylindricalDamping
         Returns the Z nonlinear cylindrical damping   
            
         
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
    ##  Returns the R nonlinear cylindrical stiffness   
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
         Returns the R nonlinear cylindrical stiffness   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RNonlinearCylindricalStiffness

    ##  Returns the R nonlinear cylindrical stiffness   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @RNonlinearCylindricalStiffness.setter
    def RNonlinearCylindricalStiffness(self, rDynamic: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RNonlinearCylindricalStiffness
         Returns the R nonlinear cylindrical stiffness   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RrNonlinearCylindricalStiffness
    ##  Returns the RR nonlinear cylindrical stiffness   
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
         Returns the RR nonlinear cylindrical stiffness   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RrNonlinearCylindricalStiffness

    ##  Returns the RR nonlinear cylindrical stiffness   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @RrNonlinearCylindricalStiffness.setter
    def RrNonlinearCylindricalStiffness(self, rrDynamic: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RrNonlinearCylindricalStiffness
         Returns the RR nonlinear cylindrical stiffness   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzNonlinearCylindricalStiffness
    ##  Returns the RZ nonlinear cylindrical stiffness   
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
         Returns the RZ nonlinear cylindrical stiffness   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzNonlinearCylindricalStiffness

    ##  Returns the RZ nonlinear cylindrical stiffness   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @RzNonlinearCylindricalStiffness.setter
    def RzNonlinearCylindricalStiffness(self, rzDynamic: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzNonlinearCylindricalStiffness
         Returns the RZ nonlinear cylindrical stiffness   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZNonlinearCylindricalStiffness
    ##  Returns the Z nonlinear cylindrical stiffness   
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
         Returns the Z nonlinear cylindrical stiffness   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZNonlinearCylindricalStiffness

    ##  Returns the Z nonlinear cylindrical stiffness   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @ZNonlinearCylindricalStiffness.setter
    def ZNonlinearCylindricalStiffness(self, zDynamic: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZNonlinearCylindricalStiffness
         Returns the Z nonlinear cylindrical stiffness   
            
         
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
    ##  Returns the RX nonlinear damping   
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
         Returns the RX nonlinear damping   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RxNonlinearDamping

    ##  Returns the RX nonlinear damping   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @RxNonlinearDamping.setter
    def RxNonlinearDamping(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RxNonlinearDamping
         Returns the RX nonlinear damping   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RyNonlinearDamping
    ##  Returns the RY nonlinear damping   
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
         Returns the RY nonlinear damping   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RyNonlinearDamping

    ##  Returns the RY nonlinear damping   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @RyNonlinearDamping.setter
    def RyNonlinearDamping(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RyNonlinearDamping
         Returns the RY nonlinear damping   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzNonlinearDamping
    ##  Returns the RZ nonlinear damping   
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
         Returns the RZ nonlinear damping   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzNonlinearDamping

    ##  Returns the RZ nonlinear damping   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @RzNonlinearDamping.setter
    def RzNonlinearDamping(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzNonlinearDamping
         Returns the RZ nonlinear damping   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) XNonlinearDamping
    ##  Returns the X nonlinear damping   
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
         Returns the X nonlinear damping   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) XNonlinearDamping

    ##  Returns the X nonlinear damping   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @XNonlinearDamping.setter
    def XNonlinearDamping(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) XNonlinearDamping
         Returns the X nonlinear damping   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) YNonlinearDamping
    ##  Returns the Y nonlinear damping   
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
         Returns the Y nonlinear damping   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) YNonlinearDamping

    ##  Returns the Y nonlinear damping   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @YNonlinearDamping.setter
    def YNonlinearDamping(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) YNonlinearDamping
         Returns the Y nonlinear damping   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZNonlinearDamping
    ##  Returns the Z nonlinear damping   
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
         Returns the Z nonlinear damping   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZNonlinearDamping

    ##  Returns the Z nonlinear damping   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @ZNonlinearDamping.setter
    def ZNonlinearDamping(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZNonlinearDamping
         Returns the Z nonlinear damping   
            
         
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
    ##  Returns the RX nonlinear stiffness   
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
         Returns the RX nonlinear stiffness   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RxNonlinearStiffness

    ##  Returns the RX nonlinear stiffness   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @RxNonlinearStiffness.setter
    def RxNonlinearStiffness(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RxNonlinearStiffness
         Returns the RX nonlinear stiffness   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RyNonlinearStiffness
    ##  Returns the RY nonlinear stiffness   
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
         Returns the RY nonlinear stiffness   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RyNonlinearStiffness

    ##  Returns the RY nonlinear stiffness   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @RyNonlinearStiffness.setter
    def RyNonlinearStiffness(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RyNonlinearStiffness
         Returns the RY nonlinear stiffness   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzNonlinearStiffness
    ##  Returns the RZ nonlinear stiffness   
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
         Returns the RZ nonlinear stiffness   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzNonlinearStiffness

    ##  Returns the RZ nonlinear stiffness   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @RzNonlinearStiffness.setter
    def RzNonlinearStiffness(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzNonlinearStiffness
         Returns the RZ nonlinear stiffness   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) XNonlinearStiffness
    ##  Returns the X nonlinear stiffness   
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
         Returns the X nonlinear stiffness   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) XNonlinearStiffness

    ##  Returns the X nonlinear stiffness   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @XNonlinearStiffness.setter
    def XNonlinearStiffness(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) XNonlinearStiffness
         Returns the X nonlinear stiffness   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) YNonlinearStiffness
    ##  Returns the Y nonlinear stiffness   
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
         Returns the Y nonlinear stiffness   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) YNonlinearStiffness

    ##  Returns the Y nonlinear stiffness   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @YNonlinearStiffness.setter
    def YNonlinearStiffness(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) YNonlinearStiffness
         Returns the Y nonlinear stiffness   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZNonlinearStiffness
    ##  Returns the Z nonlinear stiffness   
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
         Returns the Z nonlinear stiffness   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZNonlinearStiffness

    ##  Returns the Z nonlinear stiffness   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @ZNonlinearStiffness.setter
    def ZNonlinearStiffness(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZNonlinearStiffness
         Returns the Z nonlinear stiffness   
            
         
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
    def GetFlangeAngle(self, flangeIndex: int) -> NXOpen.Expression:
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
    def GetFlangeGap(self, flangeIndex: int) -> NXOpen.Expression:
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
    def GetFlangeThickness(self, flangeIndex: int) -> NXOpen.Expression:
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
    def GetFlangeThicknessInherited(self, flangeIndex: int) -> bool:
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
    def SetFlangeThicknessInherited(self, flangeIndex: int, thicknessInherited: bool) -> None:
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
    ##  Returns the RX stiffness dynamic   
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
         Returns the RX stiffness dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RxStiffnessDynamic

    ##  Returns the RX stiffness dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @RxStiffnessDynamic.setter
    def RxStiffnessDynamic(self, rxDynamic: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RxStiffnessDynamic
         Returns the RX stiffness dynamic   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RyStiffnessDynamic
    ##  Returns the RY stiffness dynamic   
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
         Returns the RY stiffness dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RyStiffnessDynamic

    ##  Returns the RY stiffness dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @RyStiffnessDynamic.setter
    def RyStiffnessDynamic(self, ryDynamic: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RyStiffnessDynamic
         Returns the RY stiffness dynamic   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzStiffnessDynamic
    ##  Returns the RZ stiffness dynamic   
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
         Returns the RZ stiffness dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzStiffnessDynamic

    ##  Returns the RZ stiffness dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @RzStiffnessDynamic.setter
    def RzStiffnessDynamic(self, rzDynamic: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzStiffnessDynamic
         Returns the RZ stiffness dynamic   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) XStiffnessDynamic
    ##  Returns the X stiffness dynamic   
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
         Returns the X stiffness dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) XStiffnessDynamic

    ##  Returns the X stiffness dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @XStiffnessDynamic.setter
    def XStiffnessDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) XStiffnessDynamic
         Returns the X stiffness dynamic   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) YStiffnessDynamic
    ##  Returns the Y stiffness dynamic   
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
         Returns the Y stiffness dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) YStiffnessDynamic

    ##  Returns the Y stiffness dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @YStiffnessDynamic.setter
    def YStiffnessDynamic(self, yDynamic: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) YStiffnessDynamic
         Returns the Y stiffness dynamic   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZStiffnessDynamic
    ##  Returns the Z stiffness dynamic   
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
         Returns the Z stiffness dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZStiffnessDynamic

    ##  Returns the Z stiffness dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @ZStiffnessDynamic.setter
    def ZStiffnessDynamic(self, zDynamic: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZStiffnessDynamic
         Returns the Z stiffness dynamic   
            
         
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
    ##  Returns the RX stiffness constant   
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
         Returns the RX stiffness constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RyStiffnessConstant
    ##  Returns the RY stiffness constant   
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
         Returns the RY stiffness constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RzStiffnessConstant
    ##  Returns the RZ stiffness constant   
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
         Returns the RZ stiffness constant   
            
         
        """
        pass
    
    ## Getter for property: (@link StiffnessType NXOpen.CAE.Connections.StiffnessType@endlink) StiffnessType
    ##  Returns the stiffness type   
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
         Returns the stiffness type   
            
         
        """
        pass
    
    ## Setter for property: (@link StiffnessType NXOpen.CAE.Connections.StiffnessType@endlink) StiffnessType

    ##  Returns the stiffness type   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @StiffnessType.setter
    def StiffnessType(self, oStiffnessType: StiffnessType):
        """
        Setter for property: (@link StiffnessType NXOpen.CAE.Connections.StiffnessType@endlink) StiffnessType
         Returns the stiffness type   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) XStiffnessConstant
    ##  Returns the X stiffness constant   
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
         Returns the X stiffness constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) YStiffnessConstant
    ##  Returns the Y stiffness constant   
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
         Returns the Y stiffness constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ZStiffnessConstant
    ##  Returns the Z stiffness constant   
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
         Returns the Z stiffness constant   
            
         
        """
        pass
    
    ##  Gets supported stiffness types of connection. 
    ##  @return types (@link StiffnessType List[NXOpen.CAE.Connections.StiffnessType]@endlink):  Supported Stiffness Types .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    @abstractmethod
    def GetSupportedStiffnessTypes(self) -> List[StiffnessType]:
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
    ##  Returns the RX structural damping dynamic   
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
         Returns the RX structural damping dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RxStructuralDampingDynamic

    ##  Returns the RX structural damping dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @RxStructuralDampingDynamic.setter
    def RxStructuralDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RxStructuralDampingDynamic
         Returns the RX structural damping dynamic   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RyStructuralDampingDynamic
    ##  Returns the RY structural damping dynamic   
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
         Returns the RY structural damping dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RyStructuralDampingDynamic

    ##  Returns the RY structural damping dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @RyStructuralDampingDynamic.setter
    def RyStructuralDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RyStructuralDampingDynamic
         Returns the RY structural damping dynamic   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzStructuralDampingDynamic
    ##  Returns the RZ structural damping dynamic   
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
         Returns the RZ structural damping dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzStructuralDampingDynamic

    ##  Returns the RZ structural damping dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @RzStructuralDampingDynamic.setter
    def RzStructuralDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzStructuralDampingDynamic
         Returns the RZ structural damping dynamic   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) XStructuralDampingDynamic
    ##  Returns the X structural damping dynamic   
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
         Returns the X structural damping dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) XStructuralDampingDynamic

    ##  Returns the X structural damping dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @XStructuralDampingDynamic.setter
    def XStructuralDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) XStructuralDampingDynamic
         Returns the X structural damping dynamic   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) YStructuralDampingDynamic
    ##  Returns the Y structural damping dynamic   
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
         Returns the Y structural damping dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) YStructuralDampingDynamic

    ##  Returns the Y structural damping dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @YStructuralDampingDynamic.setter
    def YStructuralDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) YStructuralDampingDynamic
         Returns the Y structural damping dynamic   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZStructuralDampingDynamic
    ##  Returns the Z structural damping dynamic   
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
         Returns the Z structural damping dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZStructuralDampingDynamic

    ##  Returns the Z structural damping dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @ZStructuralDampingDynamic.setter
    def ZStructuralDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZStructuralDampingDynamic
         Returns the Z structural damping dynamic   
            
         
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
    ##  Returns the RX structural damping constant   
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
         Returns the RX structural damping constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RyStructuralDampingConstant
    ##  Returns the RY structural damping constant   
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
         Returns the RY structural damping constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RzStructuralDampingConstant
    ##  Returns the RZ structural damping constant   
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
         Returns the RZ structural damping constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) XStructuralDampingConstant
    ##  Returns the X structural damping constant   
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
         Returns the X structural damping constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) YStructuralDampingConstant
    ##  Returns the Y structural damping constant   
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
         Returns the Y structural damping constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ZStructuralDampingConstant
    ##  Returns the Z structural damping constant   
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
         Returns the Z structural damping constant   
            
         
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
    ##  Returns the maximum angle of normals with the projection surface   
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
         Returns the maximum angle of normals with the projection surface   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxDistCGToElemCG
    ##  Returns the maximum distance from definition point to center of support element   
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
         Returns the maximum distance from definition point to center of support element   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxNormalDistCGToFlanges
    ##  Returns the maximum normal distance from definition point to center of element   
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
         Returns the maximum normal distance from definition point to center of element   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ProjectTolerance
    ##  Returns the projection tolerance   
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
         Returns the projection tolerance   
            
         
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
    ##  Returns the RX viscous damping dynamic   
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
         Returns the RX viscous damping dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RxViscousDampingDynamic

    ##  Returns the RX viscous damping dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @RxViscousDampingDynamic.setter
    def RxViscousDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RxViscousDampingDynamic
         Returns the RX viscous damping dynamic   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RyViscousDampingDynamic
    ##  Returns the RY viscous damping dynamic   
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
         Returns the RY viscous damping dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RyViscousDampingDynamic

    ##  Returns the RY viscous damping dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @RyViscousDampingDynamic.setter
    def RyViscousDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RyViscousDampingDynamic
         Returns the RY viscous damping dynamic   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzViscousDampingDynamic
    ##  Returns the RZ viscous damping dynamic   
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
         Returns the RZ viscous damping dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzViscousDampingDynamic

    ##  Returns the RZ viscous damping dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @RzViscousDampingDynamic.setter
    def RzViscousDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) RzViscousDampingDynamic
         Returns the RZ viscous damping dynamic   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) XViscousDampingDynamic
    ##  Returns the X viscous damping dynamic   
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
         Returns the X viscous damping dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) XViscousDampingDynamic

    ##  Returns the X viscous damping dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @XViscousDampingDynamic.setter
    def XViscousDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) XViscousDampingDynamic
         Returns the X viscous damping dynamic   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) YViscousDampingDynamic
    ##  Returns the Y viscous damping dynamic   
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
         Returns the Y viscous damping dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) YViscousDampingDynamic

    ##  Returns the Y viscous damping dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @YViscousDampingDynamic.setter
    def YViscousDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) YViscousDampingDynamic
         Returns the Y viscous damping dynamic   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZViscousDampingDynamic
    ##  Returns the Z viscous damping dynamic   
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
         Returns the Z viscous damping dynamic   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZViscousDampingDynamic

    ##  Returns the Z viscous damping dynamic   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @ZViscousDampingDynamic.setter
    def ZViscousDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: (@link NXOpen.Fields.ScalarFieldWrapper NXOpen.Fields.ScalarFieldWrapper@endlink) ZViscousDampingDynamic
         Returns the Z viscous damping dynamic   
            
         
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
    ##  Returns the RX viscous damping constant   
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
         Returns the RX viscous damping constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RyViscousDampingConstant
    ##  Returns the RY viscous damping constant   
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
         Returns the RY viscous damping constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RzViscousDampingConstant
    ##  Returns the RZ viscous damping constant   
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
         Returns the RZ viscous damping constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) XViscousDampingConstant
    ##  Returns the X viscous damping constant   
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
         Returns the X viscous damping constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) YViscousDampingConstant
    ##  Returns the Y viscous damping constant   
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
         Returns the Y viscous damping constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ZViscousDampingConstant
    ##  Returns the Z viscous damping constant   
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
         Returns the Z viscous damping constant   
            
         
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
    ##  Returns the width value   
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
         Returns the width value   
            
         
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
    ## <param name="features"> (@link NXOpen.Features.Feature List[NXOpen.Features.Feature]@endlink)  The join features </param>
    ## <param name="components"> (@link NXOpen.Assemblies.Component List[NXOpen.Assemblies.Component]@endlink)  The CAD components of the join features </param>
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
    ## <param name="feModel"> (@link NXOpen.CAE.IFEModel NXOpen.CAE.IFEModel@endlink)  The FE Model </param>
    ## <param name="cadComponentsLoadType"> (@link CadComponentsLoadType NXOpen.CAE.Connections.CadComponentsLoadType@endlink) </param>
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
    ##  Returns the radius characteristic length used by Revolute and Spherical Kinematic   
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
         Returns the radius characteristic length used by Revolute and Spherical Kinematic   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) Csys
    ##  Returns the csys   
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
         Returns the csys   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) Csys

    ##  Returns the csys   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @Csys.setter
    def Csys(self, csys: NXOpen.CoordinateSystem):
        """
        Setter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) Csys
         Returns the csys   
            
         
        """
        pass
    
    ## Getter for property: (@link CsysType NXOpen.CAE.Connections.CsysType@endlink) CsysType
    ##  Returns the csys type   
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
         Returns the csys type   
            
         
        """
        pass
    
    ## Setter for property: (@link CsysType NXOpen.CAE.Connections.CsysType@endlink) CsysType

    ##  Returns the csys type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @CsysType.setter
    def CsysType(self, csysType: CsysType):
        """
        Setter for property: (@link CsysType NXOpen.CAE.Connections.CsysType@endlink) CsysType
         Returns the csys type   
            
         
        """
        pass
    
    ## Getter for property: (@link DofCombination NXOpen.CAE.Connections.DofCombination@endlink) DofCombination
    ##  Returns the degrees of freedom combination type   
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
         Returns the degrees of freedom combination type   
            
         
        """
        pass
    
    ## Setter for property: (@link DofCombination NXOpen.CAE.Connections.DofCombination@endlink) DofCombination

    ##  Returns the degrees of freedom combination type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @DofCombination.setter
    def DofCombination(self, type: DofCombination):
        """
        Setter for property: (@link DofCombination NXOpen.CAE.Connections.DofCombination@endlink) DofCombination
         Returns the degrees of freedom combination type   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) FrictionCoefficient
    ##  Returns the friction coefficient   
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
         Returns the friction coefficient   
            
         
        """
        pass
    
    ## Getter for property: (@link NodalPairingMethod NXOpen.CAE.Connections.NodalPairingMethod@endlink) PairingMethod
    ##  Returns the pairing method of targets   
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
         Returns the pairing method of targets   
            
         
        """
        pass
    
    ## Setter for property: (@link NodalPairingMethod NXOpen.CAE.Connections.NodalPairingMethod@endlink) PairingMethod

    ##  Returns the pairing method of targets   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @PairingMethod.setter
    def PairingMethod(self, method: NodalPairingMethod):
        """
        Setter for property: (@link NodalPairingMethod NXOpen.CAE.Connections.NodalPairingMethod@endlink) PairingMethod
         Returns the pairing method of targets   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) SearchConeAngle
    ##  Returns the search cone angle   
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
         Returns the search cone angle   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) SearchOrientation
    ##  Returns the pairing search orientation   
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
         Returns the pairing search orientation   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) SearchOrientation

    ##  Returns the pairing search orientation   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @SearchOrientation.setter
    def SearchOrientation(self, orientation: NXOpen.Direction):
        """
        Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) SearchOrientation
         Returns the pairing search orientation   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) SearchRange
    ##  Returns the search range   
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
         Returns the search range   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) TighteningForce
    ##  Returns the tightening force   
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
         Returns the tightening force   
            
         
        """
        pass
    
    ## Getter for property: (bool) UseFriction
    ##  Returns the flag indicating whether to use friction parameters or not   
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
         Returns the flag indicating whether to use friction parameters or not   
            
         
        """
        pass
    
    ## Setter for property: (bool) UseFriction

    ##  Returns the flag indicating whether to use friction parameters or not   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @UseFriction.setter
    def UseFriction(self, useFriction: bool):
        """
        Setter for property: (bool) UseFriction
         Returns the flag indicating whether to use friction parameters or not   
            
         
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
    ##  Returns the mass center type   
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
         Returns the mass center type   
            
         
        """
        pass
    
    ## Setter for property: (@link MassCenterType NXOpen.CAE.Connections.MassCenterType@endlink) MassCenterType

    ##  Returns the mass center type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @MassCenterType.setter
    def MassCenterType(self, massCenterType: MassCenterType):
        """
        Setter for property: (@link MassCenterType NXOpen.CAE.Connections.MassCenterType@endlink) MassCenterType
         Returns the mass center type   
            
         
        """
        pass
    
    ## Getter for property: (@link LMIENode NXOpen.CAE.Connections.LMIENode@endlink) Node
    ##  Returns the node   
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
         Returns the node   
            
         
        """
        pass
    
    ## Setter for property: (@link LMIENode NXOpen.CAE.Connections.LMIENode@endlink) Node

    ##  Returns the node   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @Node.setter
    def Node(self, node: LMIENode):
        """
        Setter for property: (@link LMIENode NXOpen.CAE.Connections.LMIENode@endlink) Node
         Returns the node   
            
         
        """
        pass
    
    ## Getter for property: (@link LMIEPoint NXOpen.CAE.Connections.LMIEPoint@endlink) Point
    ##  Returns the point   
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
         Returns the point   
            
         
        """
        pass
    
    ## Setter for property: (@link LMIEPoint NXOpen.CAE.Connections.LMIEPoint@endlink) Point

    ##  Returns the point   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @Point.setter
    def Point(self, point: LMIEPoint):
        """
        Setter for property: (@link LMIEPoint NXOpen.CAE.Connections.LMIEPoint@endlink) Point
         Returns the point   
            
         
        """
        pass
    
    ## Getter for property: (@link LMIESelectionRecipe NXOpen.CAE.Connections.LMIESelectionRecipe@endlink) SelectionRecipe
    ##  Returns the selection recipe   
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
         Returns the selection recipe   
            
         
        """
        pass
    
    ## Setter for property: (@link LMIESelectionRecipe NXOpen.CAE.Connections.LMIESelectionRecipe@endlink) SelectionRecipe

    ##  Returns the selection recipe   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @SelectionRecipe.setter
    def SelectionRecipe(self, recipe: LMIESelectionRecipe):
        """
        Setter for property: (@link LMIESelectionRecipe NXOpen.CAE.Connections.LMIESelectionRecipe@endlink) SelectionRecipe
         Returns the selection recipe   
            
         
        """
        pass
    
    ##  Create a standalone node 
    ##  @return node (@link LMIENode NXOpen.CAE.Connections.LMIENode@endlink):  Center Node .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    def CreateNode(self) -> LMIENode:
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
    def CreatePoint(self) -> LMIEPoint:
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
    def CreateSelectionRecipe(self) -> LMIESelectionRecipe:
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
    ##  Returns the center definition   
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
         Returns the center definition   
            
         
        """
        pass
    
    ## Setter for property: (@link LMIECenterDefinition NXOpen.CAE.Connections.LMIECenterDefinition@endlink) CenterDefinition

    ##  Returns the center definition   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @CenterDefinition.setter
    def CenterDefinition(self, opt: LMIECenterDefinition):
        """
        Setter for property: (@link LMIECenterDefinition NXOpen.CAE.Connections.LMIECenterDefinition@endlink) CenterDefinition
         Returns the center definition   
            
         
        """
        pass
    
    ## Getter for property: (@link ElementType NXOpen.CAE.Connections.ElementType@endlink) ConnectionElementType
    ##  Returns the connection element type   
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
         Returns the connection element type   
            
         
        """
        pass
    
    ## Setter for property: (@link ElementType NXOpen.CAE.Connections.ElementType@endlink) ConnectionElementType

    ##  Returns the connection element type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @ConnectionElementType.setter
    def ConnectionElementType(self, connElementType: ElementType):
        """
        Setter for property: (@link ElementType NXOpen.CAE.Connections.ElementType@endlink) ConnectionElementType
         Returns the connection element type   
            
         
        """
        pass
    
    ## Getter for property: (str) Description
    ##  Returns the mass description   
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
         Returns the mass description   
            
         
        """
        pass
    
    ## Setter for property: (str) Description

    ##  Returns the mass description   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @Description.setter
    def Description(self, desc: str):
        """
        Setter for property: (str) Description
         Returns the mass description   
            
         
        """
        pass
    
    ## Getter for property: (str) FolderName
    ##  Returns the folder name   
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
         Returns the folder name   
            
         
        """
        pass
    
    ## Setter for property: (str) FolderName

    ##  Returns the folder name   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @FolderName.setter
    def FolderName(self, folderName: str):
        """
        Setter for property: (str) FolderName
         Returns the folder name   
            
         
        """
        pass
    
    ## Getter for property: (int) Id
    ##  Returns the ID   
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
         Returns the ID   
            
         
        """
        pass
    
    ## Setter for property: (int) Id

    ##  Returns the ID   
    ##     
    ##  
    ## Setter License requirements: sc_gso_10 (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @Id.setter
    def Id(self, pId: int):
        """
        Setter for property: (int) Id
         Returns the ID   
            
         
        """
        pass
    
    ## Getter for property: (@link LMIEInertia NXOpen.CAE.Connections.LMIEInertia@endlink) Inertia
    ##  Returns the inertia   
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
         Returns the inertia   
            
         
        """
        pass
    
    ## Setter for property: (@link LMIEInertia NXOpen.CAE.Connections.LMIEInertia@endlink) Inertia

    ##  Returns the inertia   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @Inertia.setter
    def Inertia(self, opt: LMIEInertia):
        """
        Setter for property: (@link LMIEInertia NXOpen.CAE.Connections.LMIEInertia@endlink) Inertia
         Returns the inertia   
            
         
        """
        pass
    
    ## Getter for property: (@link LMIELegConnection NXOpen.CAE.Connections.LMIELegConnection@endlink) LegConnection
    ##  Returns the leg connection   
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
         Returns the leg connection   
            
         
        """
        pass
    
    ## Setter for property: (@link LMIELegConnection NXOpen.CAE.Connections.LMIELegConnection@endlink) LegConnection

    ##  Returns the leg connection   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @LegConnection.setter
    def LegConnection(self, opt: LMIELegConnection):
        """
        Setter for property: (@link LMIELegConnection NXOpen.CAE.Connections.LMIELegConnection@endlink) LegConnection
         Returns the leg connection   
            
         
        """
        pass
    
    ## Getter for property: (@link LMIEMass NXOpen.CAE.Connections.LMIEMass@endlink) Mass
    ##  Returns the mass   
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
         Returns the mass   
            
         
        """
        pass
    
    ## Setter for property: (@link LMIEMass NXOpen.CAE.Connections.LMIEMass@endlink) Mass

    ##  Returns the mass   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @Mass.setter
    def Mass(self, opt: LMIEMass):
        """
        Setter for property: (@link LMIEMass NXOpen.CAE.Connections.LMIEMass@endlink) Mass
         Returns the mass   
            
         
        """
        pass
    
    ## Getter for property: (str) Plvc
    ##  Returns the plvc   
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
         Returns the plvc   
            
         
        """
        pass
    
    ## Setter for property: (str) Plvc

    ##  Returns the plvc   
    ##     
    ##  
    ## Setter License requirements: sc_gso_10 (" Simcenter NVH Composer")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @Plvc.setter
    def Plvc(self, pPlvc: str):
        """
        Setter for property: (str) Plvc
         Returns the plvc   
            
         
        """
        pass
    
    ## Getter for property: (@link LMIEUnitSystem NXOpen.CAE.Connections.LMIEUnitSystem@endlink) UnitSystem
    ##  Returns the unit system    
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
         Returns the unit system    
            
         
        """
        pass
    
    ## Setter for property: (@link LMIEUnitSystem NXOpen.CAE.Connections.LMIEUnitSystem@endlink) UnitSystem

    ##  Returns the unit system    
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @UnitSystem.setter
    def UnitSystem(self, opt: LMIEUnitSystem):
        """
        Setter for property: (@link LMIEUnitSystem NXOpen.CAE.Connections.LMIEUnitSystem@endlink) UnitSystem
         Returns the unit system    
            
         
        """
        pass
    
    ##  Create a standalone center definition 
    ##  @return opt (@link LMIECenterDefinition NXOpen.CAE.Connections.LMIECenterDefinition@endlink):  The center definition .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    def CreateCenterDefinition(self) -> LMIECenterDefinition:
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
    def CreateInertia(self) -> LMIEInertia:
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
    def CreateLegConnection(self) -> LMIELegConnection:
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
    def CreateLegDefinition(self) -> LMIELegDefinition:
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
    def CreateMass(self) -> LMIEMass:
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
    def CreateUnitSystem(self) -> LMIEUnitSystem:
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
    def GetLegDefinitions(self) -> List[LMIELegDefinition]:
        """
         Get the leg definitions 
         @return opt (@link LMIELegDefinition List[NXOpen.CAE.Connections.LMIELegDefinition]@endlink):  The leg definitions .
        """
        pass
    
    ##  Set the leg definitions 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="opt"> (@link LMIELegDefinition List[NXOpen.CAE.Connections.LMIELegDefinition]@endlink)  The leg definitions </param>
    def SetLegDefinitions(self, opt: List[LMIELegDefinition]) -> None:
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
    ##  Returns the edge number   
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
         Returns the edge number   
            
         
        """
        pass
    
    ## Setter for property: (int) EdgeNumber

    ##  Returns the edge number   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @EdgeNumber.setter
    def EdgeNumber(self, edgeNumber: int):
        """
        Setter for property: (int) EdgeNumber
         Returns the edge number   
            
         
        """
        pass
    
    ## Getter for property: (str) Id
    ##  Returns the element id   
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
         Returns the element id   
            
         
        """
        pass
    
    ## Setter for property: (str) Id

    ##  Returns the element id   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @Id.setter
    def Id(self, elementId: str):
        """
        Setter for property: (str) Id
         Returns the element id   
            
         
        """
        pass
    
import NXOpen
##   LMIEElementFace object   <br> No creator  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class LMIEElementFace(NXOpen.TaggedObject): 
    """  LMIEElementFace object  """


    ## Getter for property: (int) FaceNumber
    ##  Returns the face number   
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
         Returns the face number   
            
         
        """
        pass
    
    ## Setter for property: (int) FaceNumber

    ##  Returns the face number   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @FaceNumber.setter
    def FaceNumber(self, faceNumber: int):
        """
        Setter for property: (int) FaceNumber
         Returns the face number   
            
         
        """
        pass
    
    ## Getter for property: (str) Id
    ##  Returns the element id   
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
         Returns the element id   
            
         
        """
        pass
    
    ## Setter for property: (str) Id

    ##  Returns the element id   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @Id.setter
    def Id(self, elementId: str):
        """
        Setter for property: (str) Id
         Returns the element id   
            
         
        """
        pass
    
import NXOpen
##   LMIEElement object   <br> No creator  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class LMIEElement(NXOpen.TaggedObject): 
    """  LMIEElement object  """


    ## Getter for property: (str) Id
    ##  Returns the element id   
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
         Returns the element id   
            
         
        """
        pass
    
    ## Setter for property: (str) Id

    ##  Returns the element id   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @Id.setter
    def Id(self, unit: str):
        """
        Setter for property: (str) Id
         Returns the element id   
            
         
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
    def GetErrorCodes(self) -> List[str]:
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
    def GetErrorMessages(self) -> List[str]:
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
    def GetErrorValues(self, errorIndex: int) -> List[str]:
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
    def GetWarningCodes(self) -> List[str]:
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
    def HasErrors(self) -> bool:
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
    ##  Returns the Ixx value   
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
         Returns the Ixx value   
            
         
        """
        pass
    
    ## Setter for property: (float) Ixx

    ##  Returns the Ixx value   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @Ixx.setter
    def Ixx(self, outputValue: float):
        """
        Setter for property: (float) Ixx
         Returns the Ixx value   
            
         
        """
        pass
    
    ## Getter for property: (float) Iyx
    ##  Returns the Iyx value   
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
         Returns the Iyx value   
            
         
        """
        pass
    
    ## Setter for property: (float) Iyx

    ##  Returns the Iyx value   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @Iyx.setter
    def Iyx(self, outputValue: float):
        """
        Setter for property: (float) Iyx
         Returns the Iyx value   
            
         
        """
        pass
    
    ## Getter for property: (float) Iyy
    ##  Returns the Iyy value   
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
         Returns the Iyy value   
            
         
        """
        pass
    
    ## Setter for property: (float) Iyy

    ##  Returns the Iyy value   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @Iyy.setter
    def Iyy(self, outputValue: float):
        """
        Setter for property: (float) Iyy
         Returns the Iyy value   
            
         
        """
        pass
    
    ## Getter for property: (float) Izx
    ##  Returns the Izx value   
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
         Returns the Izx value   
            
         
        """
        pass
    
    ## Setter for property: (float) Izx

    ##  Returns the Izx value   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @Izx.setter
    def Izx(self, outputValue: float):
        """
        Setter for property: (float) Izx
         Returns the Izx value   
            
         
        """
        pass
    
    ## Getter for property: (float) Izy
    ##  Returns the Izy value   
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
         Returns the Izy value   
            
         
        """
        pass
    
    ## Setter for property: (float) Izy

    ##  Returns the Izy value   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @Izy.setter
    def Izy(self, outputValue: float):
        """
        Setter for property: (float) Izy
         Returns the Izy value   
            
         
        """
        pass
    
    ## Getter for property: (float) Izz
    ##  Returns the Izz value   
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
         Returns the Izz value   
            
         
        """
        pass
    
    ## Setter for property: (float) Izz

    ##  Returns the Izz value   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @Izz.setter
    def Izz(self, outputValue: float):
        """
        Setter for property: (float) Izz
         Returns the Izz value   
            
         
        """
        pass
    
##   Mass definition.   <br> No creator  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class LMIELegConnection(LMIEError): 
    """  Mass definition.  """


    ## Getter for property: (@link MassConnectivityType NXOpen.CAE.Connections.MassConnectivityType@endlink) LegConnectionType
    ##  Returns the leg connection type   
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
         Returns the leg connection type   
            
         
        """
        pass
    
    ## Setter for property: (@link MassConnectivityType NXOpen.CAE.Connections.MassConnectivityType@endlink) LegConnectionType

    ##  Returns the leg connection type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @LegConnectionType.setter
    def LegConnectionType(self, type: MassConnectivityType):
        """
        Setter for property: (@link MassConnectivityType NXOpen.CAE.Connections.MassConnectivityType@endlink) LegConnectionType
         Returns the leg connection type   
            
         
        """
        pass
    
    ## Getter for property: (@link LMIELocalSpiders NXOpen.CAE.Connections.LMIELocalSpiders@endlink) LocalSpiders
    ##  Returns the local spiders   
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
         Returns the local spiders   
            
         
        """
        pass
    
    ## Setter for property: (@link LMIELocalSpiders NXOpen.CAE.Connections.LMIELocalSpiders@endlink) LocalSpiders

    ##  Returns the local spiders   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @LocalSpiders.setter
    def LocalSpiders(self, opt: LMIELocalSpiders):
        """
        Setter for property: (@link LMIELocalSpiders NXOpen.CAE.Connections.LMIELocalSpiders@endlink) LocalSpiders
         Returns the local spiders   
            
         
        """
        pass
    
    ## Getter for property: (@link LMIENearestNodes NXOpen.CAE.Connections.LMIENearestNodes@endlink) NearestNodes
    ##  Returns the nearest nodes   
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
         Returns the nearest nodes   
            
         
        """
        pass
    
    ## Setter for property: (@link LMIENearestNodes NXOpen.CAE.Connections.LMIENearestNodes@endlink) NearestNodes

    ##  Returns the nearest nodes   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @NearestNodes.setter
    def NearestNodes(self, opt: LMIENearestNodes):
        """
        Setter for property: (@link LMIENearestNodes NXOpen.CAE.Connections.LMIENearestNodes@endlink) NearestNodes
         Returns the nearest nodes   
            
         
        """
        pass
    
    ##  Create a standalone local spiders 
    ##  @return opt (@link LMIELocalSpiders NXOpen.CAE.Connections.LMIELocalSpiders@endlink):  Local spiders .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    def CreateLocalSpiders(self) -> LMIELocalSpiders:
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
    def CreateNearestNodes(self) -> LMIENearestNodes:
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
    ##  Returns the node   
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
         Returns the node   
            
         
        """
        pass
    
    ## Setter for property: (@link LMIENode NXOpen.CAE.Connections.LMIENode@endlink) Node

    ##  Returns the node   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @Node.setter
    def Node(self, node: LMIENode):
        """
        Setter for property: (@link LMIENode NXOpen.CAE.Connections.LMIENode@endlink) Node
         Returns the node   
            
         
        """
        pass
    
    ## Getter for property: (@link LMIEPoint NXOpen.CAE.Connections.LMIEPoint@endlink) Point
    ##  Returns the point   
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
         Returns the point   
            
         
        """
        pass
    
    ## Setter for property: (@link LMIEPoint NXOpen.CAE.Connections.LMIEPoint@endlink) Point

    ##  Returns the point   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @Point.setter
    def Point(self, point: LMIEPoint):
        """
        Setter for property: (@link LMIEPoint NXOpen.CAE.Connections.LMIEPoint@endlink) Point
         Returns the point   
            
         
        """
        pass
    
    ## Getter for property: (@link LMIESelectionRecipe NXOpen.CAE.Connections.LMIESelectionRecipe@endlink) SelectionRecipe
    ##  Returns the selection recipe   
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
         Returns the selection recipe   
            
         
        """
        pass
    
    ## Setter for property: (@link LMIESelectionRecipe NXOpen.CAE.Connections.LMIESelectionRecipe@endlink) SelectionRecipe

    ##  Returns the selection recipe   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @SelectionRecipe.setter
    def SelectionRecipe(self, recipe: LMIESelectionRecipe):
        """
        Setter for property: (@link LMIESelectionRecipe NXOpen.CAE.Connections.LMIESelectionRecipe@endlink) SelectionRecipe
         Returns the selection recipe   
            
         
        """
        pass
    
    ##  Create a standalone node 
    ##  @return node (@link LMIENode NXOpen.CAE.Connections.LMIENode@endlink):  Leg Node .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    def CreateNode(self) -> LMIENode:
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
    def CreatePoint(self) -> LMIEPoint:
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
    def CreateSelectionRecipe(self) -> LMIESelectionRecipe:
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
    ##  Returns the Local Spider Center type   
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
         Returns the Local Spider Center type   
            
         
        """
        pass
    
    ## Setter for property: (@link LocalSpiderCenterType NXOpen.CAE.Connections.LocalSpiderCenterType@endlink) LocalSpiderCenterType

    ##  Returns the Local Spider Center type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @LocalSpiderCenterType.setter
    def LocalSpiderCenterType(self, type: LocalSpiderCenterType):
        """
        Setter for property: (@link LocalSpiderCenterType NXOpen.CAE.Connections.LocalSpiderCenterType@endlink) LocalSpiderCenterType
         Returns the Local Spider Center type   
            
         
        """
        pass
    
##   Mass Local Spiders definition.   <br> No creator  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class LMIELocalSpiders(LMIEError): 
    """  Mass Local Spiders definition.  """


    ## Getter for property: (@link LMIELocalSpiderCenterOptions NXOpen.CAE.Connections.LMIELocalSpiderCenterOptions@endlink) LocalSpiderCenterOptions
    ##  Returns the local spider center options   
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
         Returns the local spider center options   
            
         
        """
        pass
    
    ## Setter for property: (@link LMIELocalSpiderCenterOptions NXOpen.CAE.Connections.LMIELocalSpiderCenterOptions@endlink) LocalSpiderCenterOptions

    ##  Returns the local spider center options   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @LocalSpiderCenterOptions.setter
    def LocalSpiderCenterOptions(self, opt: LMIELocalSpiderCenterOptions):
        """
        Setter for property: (@link LMIELocalSpiderCenterOptions NXOpen.CAE.Connections.LMIELocalSpiderCenterOptions@endlink) LocalSpiderCenterOptions
         Returns the local spider center options   
            
         
        """
        pass
    
    ## Getter for property: (float) MaxSearchDistance
    ##  Returns the mass distribution type   
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
         Returns the mass distribution type   
            
         
        """
        pass
    
    ## Setter for property: (float) MaxSearchDistance

    ##  Returns the mass distribution type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @MaxSearchDistance.setter
    def MaxSearchDistance(self, val: float):
        """
        Setter for property: (float) MaxSearchDistance
         Returns the mass distribution type   
            
         
        """
        pass
    
    ## Getter for property: (@link LMIEPanelOptions NXOpen.CAE.Connections.LMIEPanelOptions@endlink) PanelOptions
    ##  Returns the panel options   
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
         Returns the panel options   
            
         
        """
        pass
    
    ## Setter for property: (@link LMIEPanelOptions NXOpen.CAE.Connections.LMIEPanelOptions@endlink) PanelOptions

    ##  Returns the panel options   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @PanelOptions.setter
    def PanelOptions(self, opt: LMIEPanelOptions):
        """
        Setter for property: (@link LMIEPanelOptions NXOpen.CAE.Connections.LMIEPanelOptions@endlink) PanelOptions
         Returns the panel options   
            
         
        """
        pass
    
    ## Getter for property: (@link LMIERegionSelection NXOpen.CAE.Connections.LMIERegionSelection@endlink) RegionSelection
    ##  Returns the region selection   
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
         Returns the region selection   
            
         
        """
        pass
    
    ## Setter for property: (@link LMIERegionSelection NXOpen.CAE.Connections.LMIERegionSelection@endlink) RegionSelection

    ##  Returns the region selection   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @RegionSelection.setter
    def RegionSelection(self, opt: LMIERegionSelection):
        """
        Setter for property: (@link LMIERegionSelection NXOpen.CAE.Connections.LMIERegionSelection@endlink) RegionSelection
         Returns the region selection   
            
         
        """
        pass
    
    ## Getter for property: (@link LMIERingOptions NXOpen.CAE.Connections.LMIERingOptions@endlink) RingOptions
    ##  Returns the ring options   
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
         Returns the ring options   
            
         
        """
        pass
    
    ## Setter for property: (@link LMIERingOptions NXOpen.CAE.Connections.LMIERingOptions@endlink) RingOptions

    ##  Returns the ring options   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @RingOptions.setter
    def RingOptions(self, opt: LMIERingOptions):
        """
        Setter for property: (@link LMIERingOptions NXOpen.CAE.Connections.LMIERingOptions@endlink) RingOptions
         Returns the ring options   
            
         
        """
        pass
    
    ##  Create a standalone local spider center options 
    ##  @return opt (@link LMIELocalSpiderCenterOptions NXOpen.CAE.Connections.LMIELocalSpiderCenterOptions@endlink):  Local Spider Center options .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    def CreateLocalSpiderCenterOptions(self) -> LMIELocalSpiderCenterOptions:
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
    def CreatePanelOptions(self) -> LMIEPanelOptions:
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
    def CreateRegionSelection(self) -> LMIERegionSelection:
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
    def CreateRingOptions(self) -> LMIERingOptions:
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
    ##  Returns the mass distribution type   
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
         Returns the mass distribution type   
            
         
        """
        pass
    
    ## Setter for property: (@link MassDistributionType NXOpen.CAE.Connections.MassDistributionType@endlink) MassDistributionType

    ##  Returns the mass distribution type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @MassDistributionType.setter
    def MassDistributionType(self, type: MassDistributionType):
        """
        Setter for property: (@link MassDistributionType NXOpen.CAE.Connections.MassDistributionType@endlink) MassDistributionType
         Returns the mass distribution type   
            
         
        """
        pass
    
    ## Getter for property: (@link MassType NXOpen.CAE.Connections.MassType@endlink) MassType
    ##  Returns the mass type   
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
         Returns the mass type   
            
         
        """
        pass
    
    ## Setter for property: (@link MassType NXOpen.CAE.Connections.MassType@endlink) MassType

    ##  Returns the mass type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @MassType.setter
    def MassType(self, type: MassType):
        """
        Setter for property: (@link MassType NXOpen.CAE.Connections.MassType@endlink) MassType
         Returns the mass type   
            
         
        """
        pass
    
    ## Getter for property: (float) MassValue
    ##  Returns the mass distribution type   
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
         Returns the mass distribution type   
            
         
        """
        pass
    
    ## Setter for property: (float) MassValue

    ##  Returns the mass distribution type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @MassValue.setter
    def MassValue(self, val: float):
        """
        Setter for property: (float) MassValue
         Returns the mass distribution type   
            
         
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
    ##  Returns the mass distribution type   
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
         Returns the mass distribution type   
            
         
        """
        pass
    
    ## Setter for property: (float) MaxSearchDistance

    ##  Returns the mass distribution type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @MaxSearchDistance.setter
    def MaxSearchDistance(self, val: float):
        """
        Setter for property: (float) MaxSearchDistance
         Returns the mass distribution type   
            
         
        """
        pass
    
    ## Getter for property: (@link LMIERegionSelection NXOpen.CAE.Connections.LMIERegionSelection@endlink) RegionSelection
    ##  Returns the region selection   
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
         Returns the region selection   
            
         
        """
        pass
    
    ## Setter for property: (@link LMIERegionSelection NXOpen.CAE.Connections.LMIERegionSelection@endlink) RegionSelection

    ##  Returns the region selection   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @RegionSelection.setter
    def RegionSelection(self, opt: LMIERegionSelection):
        """
        Setter for property: (@link LMIERegionSelection NXOpen.CAE.Connections.LMIERegionSelection@endlink) RegionSelection
         Returns the region selection   
            
         
        """
        pass
    
    ##  Create a standalone region selection 
    ##  @return opt (@link LMIERegionSelection NXOpen.CAE.Connections.LMIERegionSelection@endlink):  Region selection .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    def CreateRegionSelection(self) -> LMIERegionSelection:
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
    ##  Returns the node id   
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
         Returns the node id   
            
         
        """
        pass
    
    ## Setter for property: (str) Id

    ##  Returns the node id   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @Id.setter
    def Id(self, id: str):
        """
        Setter for property: (str) Id
         Returns the node id   
            
         
        """
        pass
    
##   Mass definition.   <br> No creator  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class LMIEPanelOptions(LMIEError): 
    """  Mass definition.  """


    ## Getter for property: (float) Distance
    ##  Returns the mass distribution type   
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
         Returns the mass distribution type   
            
         
        """
        pass
    
    ## Setter for property: (float) Distance

    ##  Returns the mass distribution type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @Distance.setter
    def Distance(self, val: float):
        """
        Setter for property: (float) Distance
         Returns the mass distribution type   
            
         
        """
        pass
    
    ## Getter for property: (@link PanelSearchType NXOpen.CAE.Connections.PanelSearchType@endlink) SearchPanelsType
    ##  Returns the Ring Search type   
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
         Returns the Ring Search type   
            
         
        """
        pass
    
    ## Setter for property: (@link PanelSearchType NXOpen.CAE.Connections.PanelSearchType@endlink) SearchPanelsType

    ##  Returns the Ring Search type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @SearchPanelsType.setter
    def SearchPanelsType(self, type: PanelSearchType):
        """
        Setter for property: (@link PanelSearchType NXOpen.CAE.Connections.PanelSearchType@endlink) SearchPanelsType
         Returns the Ring Search type   
            
         
        """
        pass
    
##   Lumped Mass PID.   <br> No creator  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class LMIEPid(LMIEError): 
    """  Lumped Mass PID.  """


    ## Getter for property: (int) Label
    ##  Returns the PID label   
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
         Returns the PID label   
            
         
        """
        pass
    
    ## Setter for property: (int) Label

    ##  Returns the PID label   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @Label.setter
    def Label(self, label: int):
        """
        Setter for property: (int) Label
         Returns the PID label   
            
         
        """
        pass
    
import NXOpen
##   Lumped Mass center definition point.   <br> No creator  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class LMIEPoint(LMIEError): 
    """  Lumped Mass center definition point.  """


    ## Getter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) Coordinates
    ##  Returns the point coordinates   
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
         Returns the point coordinates   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) Coordinates

    ##  Returns the point coordinates   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @Coordinates.setter
    def Coordinates(self, point: NXOpen.Point3d):
        """
        Setter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) Coordinates
         Returns the point coordinates   
            
         
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
    def CreatePid(self) -> LMIEPid:
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
    def CreateSelectionRecipe(self) -> LMIESelectionRecipe:
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
    def GetPids(self) -> List[LMIEPid]:
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
    def GetSelectionRecipes(self) -> List[LMIESelectionRecipe]:
        """
         Get the selection recipes 
         @return opt (@link LMIESelectionRecipe List[NXOpen.CAE.Connections.LMIESelectionRecipe]@endlink):  The selection recipes .
        """
        pass
    
    ##  Set the PIDs 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="opt"> (@link LMIEPid List[NXOpen.CAE.Connections.LMIEPid]@endlink)  The PIDs </param>
    def SetPids(self, opt: List[LMIEPid]) -> None:
        """
         Set the PIDs 
        """
        pass
    
    ##  Set the selection recipes 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="opt"> (@link LMIESelectionRecipe List[NXOpen.CAE.Connections.LMIESelectionRecipe]@endlink)  The selection recipes </param>
    def SetSelectionRecipes(self, opt: List[LMIESelectionRecipe]) -> None:
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
    ##  Returns the mass distribution type   
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
         Returns the mass distribution type   
            
         
        """
        pass
    
    ## Setter for property: (float) ExpansionRadius

    ##  Returns the mass distribution type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @ExpansionRadius.setter
    def ExpansionRadius(self, val: float):
        """
        Setter for property: (float) ExpansionRadius
         Returns the mass distribution type   
            
         
        """
        pass
    
    ## Getter for property: (float) ExpansionRadiusFactor
    ##  Returns the mass distribution type   
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
         Returns the mass distribution type   
            
         
        """
        pass
    
    ## Setter for property: (float) ExpansionRadiusFactor

    ##  Returns the mass distribution type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @ExpansionRadiusFactor.setter
    def ExpansionRadiusFactor(self, val: float):
        """
        Setter for property: (float) ExpansionRadiusFactor
         Returns the mass distribution type   
            
         
        """
        pass
    
    ## Getter for property: (@link RingSearchType NXOpen.CAE.Connections.RingSearchType@endlink) RingType
    ##  Returns the Ring Search type   
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
         Returns the Ring Search type   
            
         
        """
        pass
    
    ## Setter for property: (@link RingSearchType NXOpen.CAE.Connections.RingSearchType@endlink) RingType

    ##  Returns the Ring Search type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @RingType.setter
    def RingType(self, type: RingSearchType):
        """
        Setter for property: (@link RingSearchType NXOpen.CAE.Connections.RingSearchType@endlink) RingType
         Returns the Ring Search type   
            
         
        """
        pass
    
##   Lumped Mass center definition selection recipe.   <br> No creator  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class LMIESelectionRecipe(LMIEError): 
    """  Lumped Mass center definition selection recipe.  """


    ## Getter for property: (str) RecipeName
    ##  Returns the selection recipe   
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
         Returns the selection recipe   
            
         
        """
        pass
    
    ## Setter for property: (str) RecipeName

    ##  Returns the selection recipe   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @RecipeName.setter
    def RecipeName(self, name: str):
        """
        Setter for property: (str) RecipeName
         Returns the selection recipe   
            
         
        """
        pass
    
##   Seam Weld connection. Use this interface to set/get properties and parameters of the spot weld connection.   <br> No creator  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class LMIEUnitSystem(LMIEError): 
    """  Seam Weld connection. Use this interface to set/get properties and parameters of the spot weld connection.  """


    ## Getter for property: (str) LengthUnit
    ##  Returns the length unit   
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
         Returns the length unit   
            
         
        """
        pass
    
    ## Setter for property: (str) LengthUnit

    ##  Returns the length unit   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @LengthUnit.setter
    def LengthUnit(self, unit: str):
        """
        Setter for property: (str) LengthUnit
         Returns the length unit   
            
         
        """
        pass
    
    ## Getter for property: (str) MassUnit
    ##  Returns the mass unit   
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
         Returns the mass unit   
            
         
        """
        pass
    
    ## Setter for property: (str) MassUnit

    ##  Returns the mass unit   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @MassUnit.setter
    def MassUnit(self, unit: str):
        """
        Setter for property: (str) MassUnit
         Returns the mass unit   
            
         
        """
        pass
    
##  Local Spider Center Types 
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## MeanOfSpiderLegs</term><description> 
##  Local spider center is computed as the mean of its legs </description> </item><item><term> 
## InputLegDefinition</term><description> 
##  Use the input leg definition coordinates as local spider center </description> </item></list>
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
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## Point</term><description> 
##  Two Points/Nodes </description> </item><item><term> 
## Vector</term><description> 
##  Points/Node and Vector </description> </item><item><term> 
## Curve</term><description> 
##  Curves </description> </item><item><term> 
## SelectionRecipes</term><description> 
##  Selection Recipes </description> </item></list>
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
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## Coordinates</term><description> 
##  Coordinates </description> </item><item><term> 
## Point</term><description> 
##  Point </description> </item><item><term> 
## Node</term><description> 
##  Node </description> </item><item><term> 
## SeriesOfNodes</term><description> 
##  Series Of Nodes </description> </item><item><term> 
## SeriesOfCoordinates</term><description> 
##  Series Of Coordinates</description> </item><item><term> 
## Curve</term><description> 
##  Curve </description> </item><item><term> 
## FeEdgeGroup</term><description> 
##  Group Of Element Edges </description> </item><item><term> 
## SeriesOfPoints</term><description> 
##  Series Of Points </description> </item><item><term> 
## LocationWithDirection</term><description> 
##  Location with direction </description> </item><item><term> 
## SelectionRecipe</term><description> 
##  Selection Recipe </description> </item><item><term> 
## MeshPoint</term><description> 
##  Mesh Point </description> </item><item><term> 
## Group</term><description> 
##  Group </description> </item></list>
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
    ##  Returns the point of the direction definition end point.  
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
         Returns the point of the direction definition end point.  
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) DirectionPoint

    ##  Returns the point of the direction definition end point.  
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @DirectionPoint.setter
    def DirectionPoint(self, direction: NXOpen.Point):
        """
        Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) DirectionPoint
         Returns the point of the direction definition end point.  
            
         
        """
        pass
    
    ## Getter for property: (@link LocationDirectionType NXOpen.CAE.Connections.LocationDirectionType@endlink) DirectionType
    ##  Returns the direction type   
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
         Returns the direction type   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Vector3d NXOpen.Vector3d@endlink) DirectionValue
    ##  Returns the direction value  
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
         Returns the direction value  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) DirectionVector
    ##  Returns the direction definition vector   
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
         Returns the direction definition vector   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) DirectionVector

    ##  Returns the direction definition vector   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @DirectionVector.setter
    def DirectionVector(self, direction: NXOpen.Direction):
        """
        Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) DirectionVector
         Returns the direction definition vector   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.CAE.SelectionRecipe NXOpen.CAE.SelectionRecipe@endlink) EndSelectionRecipe
    ##  Returns the end selection recipe  
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
         Returns the end selection recipe  
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.CAE.SelectionRecipe NXOpen.CAE.SelectionRecipe@endlink) EndSelectionRecipe

    ##  Returns the end selection recipe  
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @EndSelectionRecipe.setter
    def EndSelectionRecipe(self, selectionRecipe: NXOpen.CAE.SelectionRecipe):
        """
        Setter for property: (@link NXOpen.CAE.SelectionRecipe NXOpen.CAE.SelectionRecipe@endlink) EndSelectionRecipe
         Returns the end selection recipe  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) Point
    ##  Returns the point of the direction definition start point.  
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
         Returns the point of the direction definition start point.  
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) Point

    ##  Returns the point of the direction definition start point.  
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @Point.setter
    def Point(self, point: NXOpen.Point):
        """
        Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) Point
         Returns the point of the direction definition start point.  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.CAE.SelectionRecipe NXOpen.CAE.SelectionRecipe@endlink) StartSelectionRecipe
    ##  Returns the start selection recipe  
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
         Returns the start selection recipe  
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.CAE.SelectionRecipe NXOpen.CAE.SelectionRecipe@endlink) StartSelectionRecipe

    ##  Returns the start selection recipe  
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @StartSelectionRecipe.setter
    def StartSelectionRecipe(self, selectionRecipe: NXOpen.CAE.SelectionRecipe):
        """
        Setter for property: (@link NXOpen.CAE.SelectionRecipe NXOpen.CAE.SelectionRecipe@endlink) StartSelectionRecipe
         Returns the start selection recipe  
            
         
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
    def GetDetails(self) -> str:
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
    def GetInfo(self) -> str:
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
    def GetXyzCoordinates(self) -> List[NXOpen.Point3d]:
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
    ##  Returns the target center   
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
         Returns the target center   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) Center

    ##  Returns the target center   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @Center.setter
    def Center(self, center: NXOpen.TaggedObject):
        """
        Setter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) Center
         Returns the target center   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) Csys
    ##  Returns the csys   
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
         Returns the csys   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) Csys

    ##  Returns the csys   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @Csys.setter
    def Csys(self, csys: NXOpen.CoordinateSystem):
        """
        Setter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) Csys
         Returns the csys   
            
         
        """
        pass
    
    ## Getter for property: (@link CsysType NXOpen.CAE.Connections.CsysType@endlink) CsysType
    ##  Returns the csys type   
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
         Returns the csys type   
            
         
        """
        pass
    
    ## Setter for property: (@link CsysType NXOpen.CAE.Connections.CsysType@endlink) CsysType

    ##  Returns the csys type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @CsysType.setter
    def CsysType(self, csysType: CsysType):
        """
        Setter for property: (@link CsysType NXOpen.CAE.Connections.CsysType@endlink) CsysType
         Returns the csys type   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ExpansionRadiusFactorTolerance
    ##  Returns the expansion radius factor   
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
         Returns the expansion radius factor   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ExpansionRadiusTolerance
    ##  Returns the expansion radius   
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
         Returns the expansion radius   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) InertiaXX
    ##  Returns the inertia XX.  
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
         Returns the inertia XX.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) InertiaYX
    ##  Returns the inertia XY.  
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
         Returns the inertia XY.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) InertiaYY
    ##  Returns the inertia YY.  
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
         Returns the inertia YY.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) InertiaZX
    ##  Returns the inertia XZ.  
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
         Returns the inertia XZ.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) InertiaZY
    ##  Returns the inertia YZ.  
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
         Returns the inertia YZ.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) InertiaZZ
    ##  Returns the inertia ZZ.  
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
         Returns the inertia ZZ.  
             
         
        """
        pass
    
    ## Getter for property: (@link LocalSpiderCenterType NXOpen.CAE.Connections.LocalSpiderCenterType@endlink) LocalSpiderCenterType
    ##  Returns the local spider center type   
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
         Returns the local spider center type   
            
         
        """
        pass
    
    ## Setter for property: (@link LocalSpiderCenterType NXOpen.CAE.Connections.LocalSpiderCenterType@endlink) LocalSpiderCenterType

    ##  Returns the local spider center type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @LocalSpiderCenterType.setter
    def LocalSpiderCenterType(self, localSpiderCenterType: LocalSpiderCenterType):
        """
        Setter for property: (@link LocalSpiderCenterType NXOpen.CAE.Connections.LocalSpiderCenterType@endlink) LocalSpiderCenterType
         Returns the local spider center type   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Mass
    ##  Returns the mass value   
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
         Returns the mass value   
            
         
        """
        pass
    
    ## Getter for property: (@link MassCenterType NXOpen.CAE.Connections.MassCenterType@endlink) MassCenterType
    ##  Returns the mass center type   
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
         Returns the mass center type   
            
         
        """
        pass
    
    ## Setter for property: (@link MassCenterType NXOpen.CAE.Connections.MassCenterType@endlink) MassCenterType

    ##  Returns the mass center type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @MassCenterType.setter
    def MassCenterType(self, massCenterType: MassCenterType):
        """
        Setter for property: (@link MassCenterType NXOpen.CAE.Connections.MassCenterType@endlink) MassCenterType
         Returns the mass center type   
            
         
        """
        pass
    
    ## Getter for property: (@link MassConnectivityType NXOpen.CAE.Connections.MassConnectivityType@endlink) MassConnectivityType
    ##  Returns the mass connection type   
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
         Returns the mass connection type   
            
         
        """
        pass
    
    ## Setter for property: (@link MassConnectivityType NXOpen.CAE.Connections.MassConnectivityType@endlink) MassConnectivityType

    ##  Returns the mass connection type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @MassConnectivityType.setter
    def MassConnectivityType(self, type: MassConnectivityType):
        """
        Setter for property: (@link MassConnectivityType NXOpen.CAE.Connections.MassConnectivityType@endlink) MassConnectivityType
         Returns the mass connection type   
            
         
        """
        pass
    
    ## Getter for property: (@link MassDistributionType NXOpen.CAE.Connections.MassDistributionType@endlink) MassDistributionType
    ##  Returns the mass distribution type   
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
         Returns the mass distribution type   
            
         
        """
        pass
    
    ## Setter for property: (@link MassDistributionType NXOpen.CAE.Connections.MassDistributionType@endlink) MassDistributionType

    ##  Returns the mass distribution type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @MassDistributionType.setter
    def MassDistributionType(self, type: MassDistributionType):
        """
        Setter for property: (@link MassDistributionType NXOpen.CAE.Connections.MassDistributionType@endlink) MassDistributionType
         Returns the mass distribution type   
            
         
        """
        pass
    
    ## Getter for property: (@link MassType NXOpen.CAE.Connections.MassType@endlink) MassTypeValue
    ##  Returns the mass type   
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
         Returns the mass type   
            
         
        """
        pass
    
    ## Setter for property: (@link MassType NXOpen.CAE.Connections.MassType@endlink) MassTypeValue

    ##  Returns the mass type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @MassTypeValue.setter
    def MassTypeValue(self, type: MassType):
        """
        Setter for property: (@link MassType NXOpen.CAE.Connections.MassType@endlink) MassTypeValue
         Returns the mass type   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxDistanceTolerance
    ##  Returns the maximum distance from definition point to center of support element   
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
         Returns the maximum distance from definition point to center of support element   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) PanelSearchDistance
    ##  Returns the panel search distance   
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
         Returns the panel search distance   
            
         
        """
        pass
    
    ## Getter for property: (@link PanelSearchType NXOpen.CAE.Connections.PanelSearchType@endlink) PanelSearchType
    ##  Returns the panel search type  
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
         Returns the panel search type  
            
         
        """
        pass
    
    ## Setter for property: (@link PanelSearchType NXOpen.CAE.Connections.PanelSearchType@endlink) PanelSearchType

    ##  Returns the panel search type  
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @PanelSearchType.setter
    def PanelSearchType(self, type: PanelSearchType):
        """
        Setter for property: (@link PanelSearchType NXOpen.CAE.Connections.PanelSearchType@endlink) PanelSearchType
         Returns the panel search type  
            
         
        """
        pass
    
    ## Getter for property: (@link RingSearchType NXOpen.CAE.Connections.RingSearchType@endlink) RingSearchType
    ##  Returns the search tolerance type  
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
         Returns the search tolerance type  
            
         
        """
        pass
    
    ## Setter for property: (@link RingSearchType NXOpen.CAE.Connections.RingSearchType@endlink) RingSearchType

    ##  Returns the search tolerance type  
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @RingSearchType.setter
    def RingSearchType(self, type: RingSearchType):
        """
        Setter for property: (@link RingSearchType NXOpen.CAE.Connections.RingSearchType@endlink) RingSearchType
         Returns the search tolerance type  
            
         
        """
        pass
    
##  Lumped Mass Center Types 
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## Manual</term><description> 
##  CoG is picked by selection </description> </item><item><term> 
## FromDefinedSpiderLegs</term><description> 
##  Use the CoG from the definition legs </description> </item><item><term> 
## FromComputedSpiderLegs</term><description> 
##  Use the CoG from the computed legs </description> </item></list>
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
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## NearestNodes</term><description> 
##  nearest nodes on defined panels </description> </item><item><term> 
## LocalSpiders</term><description> 
##  locally created spiders </description> </item></list>
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
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## Distributed</term><description> 
##  Mass is distributed on selected nodes </description> </item><item><term> 
## Repeated</term><description> 
##  Mass is applied at the defined value on each node  </description> </item></list>
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
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## OnNodes</term><description> 
##  Mass applied on selected nodes </description> </item><item><term> 
## WithSpiders</term><description> 
##  Mass with defined spider </description> </item></list>
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
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## User</term><description> 
##  User defined material </description> </item><item><term> 
## FromSupport</term><description> 
##  Material defined from support </description> </item><item><term> 
## NotSet</term><description> 
##  No material required </description> </item></list>
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
    ##  Returns the Mesh Point used for creating the location.  
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
         Returns the Mesh Point used for creating the location.  
          
                        If the location type is not mesh point, this method will raise an error.   
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.CAE.MeshPoint NXOpen.CAE.MeshPoint@endlink) MeshPoint

    ##  Returns the Mesh Point used for creating the location.  
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
         Returns the Mesh Point used for creating the location.  
          
                        If the location type is not mesh point, this method will raise an error.   
         
        """
        pass
    
##  Modelization PPTRefTargetType 
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## NotSet</term><description> 
##  None </description> </item><item><term> 
## Ec</term><description> 
##  Element collector </description> </item><item><term> 
## Ecc</term><description> 
##  Element collector container </description> </item><item><term> 
## Ead</term><description> 
##  Element Associated Data </description> </item></list>
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
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## NotSet</term><description> 
##  None </description> </item><item><term> 
## Material</term><description> 
##  Material </description> </item><item><term> 
## Weights</term><description> 
##  Interpolation element weights </description> </item><item><term> 
## Section</term><description> 
##  Section </description> </item><item><term> 
## Csys</term><description> 
##  Csys </description> </item><item><term> 
## Stiffness</term><description> 
##  Stiffness </description> </item><item><term> 
## ViscousDamping</term><description> 
##  ViscousDamping </description> </item><item><term> 
## StructuralDamping</term><description> 
##  StructuralDamping </description> </item><item><term> 
## Dofs</term><description> 
##  Dofs </description> </item><item><term> 
## DynamicStiffness</term><description> 
##  Dynamic Stiffness </description> </item><item><term> 
## DynamicViscousDamping</term><description> 
##  Dynamic ViscousDamping </description> </item><item><term> 
## DynamicStructuralDamping</term><description> 
##  Dynamic StructuralDamping </description> </item><item><term> 
## Friction</term><description> 
##  Friction </description> </item><item><term> 
## Contact</term><description> 
##  Contact </description> </item><item><term> 
## Mass</term><description> 
##  Mass </description> </item><item><term> 
## NonlinearStiffness</term><description> 
##  Nonlinear Stiffness </description> </item><item><term> 
## NonlinearDamping</term><description> 
##  Nonlinear Damping </description> </item><item><term> 
## Thickness</term><description> 
##  Thickness </description> </item></list>
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
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## Proximity</term><description> 
##  Proximity </description> </item><item><term> 
## OrientatedSearch</term><description> 
##  Oriented Search </description> </item><item><term> 
## SelectionOrder</term><description> 
##  Selection Order </description> </item></list>
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
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## Manual</term><description> 
##  CoG is picked by selection </description> </item><item><term> 
## FromComputedSpiderLegs</term><description> 
##  Use the CoG from the computed legs </description> </item><item><term> 
## Coincident</term><description> 
##  The CoG is coincident with the other target CoG </description> </item><item><term> 
## FromDefinedSpiderLegs</term><description> 
##  Use the CoG from the definition legs </description> </item></list>
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
    ##  Returns the target center type   
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
         Returns the target center type   
            
         
        """
        pass
    
    ## Setter for property: (@link NodalTargetCenterType NXOpen.CAE.Connections.NodalTargetCenterType@endlink) CenterType

    ##  Returns the target center type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @CenterType.setter
    def CenterType(self, centerType: NodalTargetCenterType):
        """
        Setter for property: (@link NodalTargetCenterType NXOpen.CAE.Connections.NodalTargetCenterType@endlink) CenterType
         Returns the target center type   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ExpansionRadius
    ##  Returns the Expansion Radius   
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
         Returns the Expansion Radius   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ExpansionRadiusFactor
    ##  Returns the Expansion Radius Factor   
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
         Returns the Expansion Radius Factor   
            
         
        """
        pass
    
    ## Getter for property: (@link LocalSpiderCenterType NXOpen.CAE.Connections.LocalSpiderCenterType@endlink) LocalSpiderCenterType
    ##  Returns the Local Spider Center type   
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
         Returns the Local Spider Center type   
            
         
        """
        pass
    
    ## Setter for property: (@link LocalSpiderCenterType NXOpen.CAE.Connections.LocalSpiderCenterType@endlink) LocalSpiderCenterType

    ##  Returns the Local Spider Center type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @LocalSpiderCenterType.setter
    def LocalSpiderCenterType(self, localSpiderCenterType: LocalSpiderCenterType):
        """
        Setter for property: (@link LocalSpiderCenterType NXOpen.CAE.Connections.LocalSpiderCenterType@endlink) LocalSpiderCenterType
         Returns the Local Spider Center type   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxDistance
    ##  Returns the Maximum Distance   
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
         Returns the Maximum Distance   
            
         
        """
        pass
    
    ## Getter for property: (@link PanelSearchType NXOpen.CAE.Connections.PanelSearchType@endlink) PanelSearchType
    ##  Returns the Panel Search type   
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
         Returns the Panel Search type   
            
         
        """
        pass
    
    ## Setter for property: (@link PanelSearchType NXOpen.CAE.Connections.PanelSearchType@endlink) PanelSearchType

    ##  Returns the Panel Search type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @PanelSearchType.setter
    def PanelSearchType(self, panelSearchType: PanelSearchType):
        """
        Setter for property: (@link PanelSearchType NXOpen.CAE.Connections.PanelSearchType@endlink) PanelSearchType
         Returns the Panel Search type   
            
         
        """
        pass
    
    ## Getter for property: (@link RingSearchType NXOpen.CAE.Connections.RingSearchType@endlink) RingSearchType
    ##  Returns the Ring Search type   
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
         Returns the Ring Search type   
            
         
        """
        pass
    
    ## Setter for property: (@link RingSearchType NXOpen.CAE.Connections.RingSearchType@endlink) RingSearchType

    ##  Returns the Ring Search type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @RingSearchType.setter
    def RingSearchType(self, ringSearchType: RingSearchType):
        """
        Setter for property: (@link RingSearchType NXOpen.CAE.Connections.RingSearchType@endlink) RingSearchType
         Returns the Ring Search type   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) SearchTolerance
    ##  Returns the Search Tolerance   
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
         Returns the Search Tolerance   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) TargetCenter
    ##  Returns the target center   
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
         Returns the target center   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) TargetCenter

    ##  Returns the target center   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @TargetCenter.setter
    def TargetCenter(self, center: NXOpen.TaggedObject):
        """
        Setter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) TargetCenter
         Returns the target center   
            
         
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
    ##  Returns the target center   
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
         Returns the target center   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) TargetCenter

    ##  Returns the target center   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @TargetCenter.setter
    def TargetCenter(self, center: NXOpen.TaggedObject):
        """
        Setter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) TargetCenter
         Returns the target center   
            
         
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
    ##  Returns the target center type   
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
         Returns the target center type   
            
         
        """
        pass
    
    ## Setter for property: (@link NodalTargetCenterType NXOpen.CAE.Connections.NodalTargetCenterType@endlink) CenterType

    ##  Returns the target center type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @CenterType.setter
    def CenterType(self, centerType: NodalTargetCenterType):
        """
        Setter for property: (@link NodalTargetCenterType NXOpen.CAE.Connections.NodalTargetCenterType@endlink) CenterType
         Returns the target center type   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) TargetCenter
    ##  Returns the target center   
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
         Returns the target center   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) TargetCenter

    ##  Returns the target center   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @TargetCenter.setter
    def TargetCenter(self, center: NXOpen.TaggedObject):
        """
        Setter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) TargetCenter
         Returns the target center   
            
         
        """
        pass
    
##  Nodal Target types 
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## SinglePoint</term><description> 
##  Single Point </description> </item><item><term> 
## SetOfPoints</term><description> 
##  Set of Points </description> </item><item><term> 
## Spider</term><description> 
##  Spider </description> </item><item><term> 
## NotSet</term><description> 
##  None </description> </item><item><term> 
## LocalSpider</term><description> 
##  Local Spider </description> </item></list>
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
    ##  Returns the target type   
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
         Returns the target type   
            
         
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
    ##  Returns the FEM node used for creating the location.  
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
         Returns the FEM node used for creating the location.  
          
                        If the location type is not node, this method will raise an error.   
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.CAE.FENode NXOpen.CAE.FENode@endlink) Node

    ##  Returns the FEM node used for creating the location.  
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
         Returns the FEM node used for creating the location.  
          
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
    ## 
    ## <param name="nodes"> (@link NXOpen.CAE.FENode List[NXOpen.CAE.FENode]@endlink)  Node used for location </param>
    def AddNodes(self, nodes: List[NXOpen.CAE.FENode]) -> None:
        """
         Add location nodes. 
        """
        pass
    
    ##  Retrieve location nodes. 
    ##  @return nodes (@link NXOpen.CAE.FENode List[NXOpen.CAE.FENode]@endlink):  Node used for location .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    def GetNodes(self) -> List[NXOpen.CAE.FENode]:
        """
         Retrieve location nodes. 
         @return nodes (@link NXOpen.CAE.FENode List[NXOpen.CAE.FENode]@endlink):  Node used for location .
        """
        pass
    
    ##  Set location nodes. 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ## <param name="nodes"> (@link NXOpen.CAE.FENode List[NXOpen.CAE.FENode]@endlink)  Node used for location </param>
    def SetNodes(self, nodes: List[NXOpen.CAE.FENode]) -> None:
        """
         Set location nodes. 
        """
        pass
    
##  Nut diameter definition types 
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## User</term><description> 
##  User defined diameter </description> </item><item><term> 
## FactorOfDiameter</term><description> 
##  User defined relationship with bolt head diameter </description> </item></list>
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
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## NearestSelectedPanel</term><description> 
##  Apply on the closest panel </description> </item><item><term> 
## AllSelectedPanels</term><description> 
##  Apply on all selected panels </description> </item></list>
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
    ##  Returns the POINT used for creating the location.  
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
         Returns the POINT used for creating the location.  
          
                        If the location type is not point, this method will raise an error.   
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) Point

    ##  Returns the POINT used for creating the location.  
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
         Returns the POINT used for creating the location.  
          
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
    ## 
    ## <param name="points"> (@link NXOpen.Point List[NXOpen.Point]@endlink)  Points used for location </param>
    def AddPoints(self, points: List[NXOpen.Point]) -> None:
        """
         Add location nodes. 
        """
        pass
    
    ##  Retrieve location points. 
    ##  @return points (@link NXOpen.Point List[NXOpen.Point]@endlink):  Points used for location .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    def GetPoints(self) -> List[NXOpen.Point]:
        """
         Retrieve location points. 
         @return points (@link NXOpen.Point List[NXOpen.Point]@endlink):  Points used for location .
        """
        pass
    
    ##  Set location points. 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ## <param name="points"> (@link NXOpen.Point List[NXOpen.Point]@endlink)  Points used for location </param>
    def SetPoints(self, points: List[NXOpen.Point]) -> None:
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
    ##  Returns the csys   
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
         Returns the csys   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) Csys

    ##  Returns the csys   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @Csys.setter
    def Csys(self, csys: NXOpen.CoordinateSystem):
        """
        Setter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) Csys
         Returns the csys   
            
         
        """
        pass
    
    ## Getter for property: (@link CsysType NXOpen.CAE.Connections.CsysType@endlink) CsysType
    ##  Returns the csys type   
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
         Returns the csys type   
            
         
        """
        pass
    
    ## Setter for property: (@link CsysType NXOpen.CAE.Connections.CsysType@endlink) CsysType

    ##  Returns the csys type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @CsysType.setter
    def CsysType(self, csysType: CsysType):
        """
        Setter for property: (@link CsysType NXOpen.CAE.Connections.CsysType@endlink) CsysType
         Returns the csys type   
            
         
        """
        pass
    
    ## Getter for property: (@link NodalPairingMethod NXOpen.CAE.Connections.NodalPairingMethod@endlink) PairingMethod
    ##  Returns the pairing method of targets   
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
         Returns the pairing method of targets   
            
         
        """
        pass
    
    ## Setter for property: (@link NodalPairingMethod NXOpen.CAE.Connections.NodalPairingMethod@endlink) PairingMethod

    ##  Returns the pairing method of targets   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @PairingMethod.setter
    def PairingMethod(self, method: NodalPairingMethod):
        """
        Setter for property: (@link NodalPairingMethod NXOpen.CAE.Connections.NodalPairingMethod@endlink) PairingMethod
         Returns the pairing method of targets   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) SearchConeAngle
    ##  Returns the search cone angle   
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
         Returns the search cone angle   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) SearchOrientation
    ##  Returns the pairing search orientation   
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
         Returns the pairing search orientation   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) SearchOrientation

    ##  Returns the pairing search orientation   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @SearchOrientation.setter
    def SearchOrientation(self, orientation: NXOpen.Direction):
        """
        Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) SearchOrientation
         Returns the pairing search orientation   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) SearchRange
    ##  Returns the search range   
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
         Returns the search range   
            
         
        """
        pass
    
##  nodal ring search type 
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## OneRing</term><description> 
##  One Ring </description> </item><item><term> 
## TwoRings</term><description> 
##  Two Rings </description> </item><item><term> 
## ExpansionRadius</term><description> 
##  Search by exansion radius </description> </item><item><term> 
## ExpansionRadiusFactor</term><description> 
##  Search by exansion radius factor </description> </item></list>
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
    ##  Returns the coefficient for formula defined diameter   
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
         Returns the coefficient for formula defined diameter   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Diameter
    ##  Returns the connection diameter   
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
         Returns the connection diameter   
            
         
        """
        pass
    
    ## Getter for property: (@link DiameterType NXOpen.CAE.Connections.DiameterType@endlink) DiameterType
    ##  Returns the connection diameter type   
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
         Returns the connection diameter type   
            
         
        """
        pass
    
    ## Setter for property: (@link DiameterType NXOpen.CAE.Connections.DiameterType@endlink) DiameterType

    ##  Returns the connection diameter type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @DiameterType.setter
    def DiameterType(self, diameterType: DiameterType):
        """
        Setter for property: (@link DiameterType NXOpen.CAE.Connections.DiameterType@endlink) DiameterType
         Returns the connection diameter type   
            
         
        """
        pass
    
    ## Getter for property: (@link DiscretizationMethod NXOpen.CAE.Connections.DiscretizationMethod@endlink) DiscretizationMethod
    ##  Returns the discretization method   
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
         Returns the discretization method   
            
         
        """
        pass
    
    ## Setter for property: (@link DiscretizationMethod NXOpen.CAE.Connections.DiscretizationMethod@endlink) DiscretizationMethod

    ##  Returns the discretization method   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @DiscretizationMethod.setter
    def DiscretizationMethod(self, method: DiscretizationMethod):
        """
        Setter for property: (@link DiscretizationMethod NXOpen.CAE.Connections.DiscretizationMethod@endlink) DiscretizationMethod
         Returns the discretization method   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) DistanceFromStart
    ##  Returns the line Discretization distance from start   
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
         Returns the line Discretization distance from start   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) DistanceToEnd
    ##  Returns the line Discretization distance to end   
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
         Returns the line Discretization distance to end   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Height
    ##  Returns the height value   
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
         Returns the height value   
            
         
        """
        pass
    
    ## Getter for property: (@link HeightType NXOpen.CAE.Connections.HeightType@endlink) HeightType
    ##  Returns the connection height type   
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
         Returns the connection height type   
            
         
        """
        pass
    
    ## Setter for property: (@link HeightType NXOpen.CAE.Connections.HeightType@endlink) HeightType

    ##  Returns the connection height type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @HeightType.setter
    def HeightType(self, heightType: HeightType):
        """
        Setter for property: (@link HeightType NXOpen.CAE.Connections.HeightType@endlink) HeightType
         Returns the connection height type   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) LengthStep
    ##  Returns the line Discretization length step   
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
         Returns the line Discretization length step   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.PhysicalMaterial NXOpen.PhysicalMaterial@endlink) Material
    ##  Returns the connection material   
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
         Returns the connection material   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.PhysicalMaterial NXOpen.PhysicalMaterial@endlink) Material

    ##  Returns the connection material   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @Material.setter
    def Material(self, material: NXOpen.PhysicalMaterial):
        """
        Setter for property: (@link NXOpen.PhysicalMaterial NXOpen.PhysicalMaterial@endlink) Material
         Returns the connection material   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxAngleBetweenNormals
    ##  Returns the maximum angle of normals with the projection surface   
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
         Returns the maximum angle of normals with the projection surface   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxDistCGToElemCG
    ##  Returns the maximum distance from definition point to center of support element   
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
         Returns the maximum distance from definition point to center of support element   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxLengthStep
    ##  Returns the line Discretization max length step   
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
         Returns the line Discretization max length step   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxNormalDistCGToFlanges
    ##  Returns the maximum normal distance from definition point to center of element   
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
         Returns the maximum normal distance from definition point to center of element   
            
         
        """
        pass
    
    ## Getter for property: (int) NumberOfDiscretizationPoints
    ##  Returns the number of connections   
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
         Returns the number of connections   
            
         
        """
        pass
    
    ## Setter for property: (int) NumberOfDiscretizationPoints

    ##  Returns the number of connections   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @NumberOfDiscretizationPoints.setter
    def NumberOfDiscretizationPoints(self, num: int):
        """
        Setter for property: (int) NumberOfDiscretizationPoints
         Returns the number of connections   
            
         
        """
        pass
    
    ## Getter for property: (int) NumberOfFlanges
    ##  Returns the number of flanges.  
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
         Returns the number of flanges.  
           When changing the number of flanges this is not applied till an update is performed by calling @link Update::DoUpdate Update::DoUpdate@endlink    
         
        """
        pass
    
    ## Setter for property: (int) NumberOfFlanges

    ##  Returns the number of flanges.  
    ##    When changing the number of flanges this is not applied till an update is performed by calling @link Update::DoUpdate Update::DoUpdate@endlink    
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @NumberOfFlanges.setter
    def NumberOfFlanges(self, numberOfFlanges: int):
        """
        Setter for property: (int) NumberOfFlanges
         Returns the number of flanges.  
           When changing the number of flanges this is not applied till an update is performed by calling @link Update::DoUpdate Update::DoUpdate@endlink    
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ProjectTolerance
    ##  Returns the projection tolerance   
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
         Returns the projection tolerance   
            
         
        """
        pass
    
    ## Getter for property: (str) TableFile
    ##  Returns the table file used to compute the diameter   
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
         Returns the table file used to compute the diameter   
            
         
        """
        pass
    
    ## Setter for property: (str) TableFile

    ##  Returns the table file used to compute the diameter   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @TableFile.setter
    def TableFile(self, tableFile: str):
        """
        Setter for property: (str) TableFile
         Returns the table file used to compute the diameter   
            
         
        """
        pass
    
    ## Getter for property: (bool) UseMaxLengthStep
    ##  Returns the usage of max length step   
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
         Returns the usage of max length step   
            
         
        """
        pass
    
    ## Setter for property: (bool) UseMaxLengthStep

    ##  Returns the usage of max length step   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @UseMaxLengthStep.setter
    def UseMaxLengthStep(self, use: bool):
        """
        Setter for property: (bool) UseMaxLengthStep
         Returns the usage of max length step   
            
         
        """
        pass
    
    ## Getter for property: (bool) UseOriginalNodesOfConnection
    ##  Returns the usage of original nodes of connection   
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
         Returns the usage of original nodes of connection   
            
         
        """
        pass
    
    ## Setter for property: (bool) UseOriginalNodesOfConnection

    ##  Returns the usage of original nodes of connection   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @UseOriginalNodesOfConnection.setter
    def UseOriginalNodesOfConnection(self, use: bool):
        """
        Setter for property: (bool) UseOriginalNodesOfConnection
         Returns the usage of original nodes of connection   
            
         
        """
        pass
    
import NXOpen
##   Sealing connection. Use this interface to set/get properties and parameters of the spot weld connection.   <br> To obtain an instance of this object use the connection creators on the @link CAE::Connections::Folder CAE::Connections::Folder@endlink   <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class Sealing(IConnection): 
    """  Sealing connection. Use this interface to set/get properties and parameters of the spot weld connection.  """


    ## Getter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) Csys
    ##  Returns the csys   
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
         Returns the csys   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) Csys

    ##  Returns the csys   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @Csys.setter
    def Csys(self, csys: NXOpen.CoordinateSystem):
        """
        Setter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) Csys
         Returns the csys   
            
         
        """
        pass
    
    ## Getter for property: (@link CsysType NXOpen.CAE.Connections.CsysType@endlink) CsysType
    ##  Returns the csys type   
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
         Returns the csys type   
            
         
        """
        pass
    
    ## Setter for property: (@link CsysType NXOpen.CAE.Connections.CsysType@endlink) CsysType

    ##  Returns the csys type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @CsysType.setter
    def CsysType(self, csysType: CsysType):
        """
        Setter for property: (@link CsysType NXOpen.CAE.Connections.CsysType@endlink) CsysType
         Returns the csys type   
            
         
        """
        pass
    
    ## Getter for property: (@link DiscretizationMethod NXOpen.CAE.Connections.DiscretizationMethod@endlink) DiscretizationMethod
    ##  Returns the discretization method   
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
         Returns the discretization method   
            
         
        """
        pass
    
    ## Setter for property: (@link DiscretizationMethod NXOpen.CAE.Connections.DiscretizationMethod@endlink) DiscretizationMethod

    ##  Returns the discretization method   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @DiscretizationMethod.setter
    def DiscretizationMethod(self, method: DiscretizationMethod):
        """
        Setter for property: (@link DiscretizationMethod NXOpen.CAE.Connections.DiscretizationMethod@endlink) DiscretizationMethod
         Returns the discretization method   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) DistanceFromStart
    ##  Returns the line Discretization distance from start   
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
         Returns the line Discretization distance from start   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) DistanceToEnd
    ##  Returns the line Discretization distance to end   
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
         Returns the line Discretization distance to end   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) LengthStep
    ##  Returns the line Discretization length step   
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
         Returns the line Discretization length step   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Mass
    ##  Returns the mass value   
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
         Returns the mass value   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxAngleBetweenNormals
    ##  Returns the maximum angle of normals with the projection surface   
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
         Returns the maximum angle of normals with the projection surface   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxDistCGToElemCG
    ##  Returns the maximum distance from definition point to center of support element   
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
         Returns the maximum distance from definition point to center of support element   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxLengthStep
    ##  Returns the line Discretization max length step   
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
         Returns the line Discretization max length step   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxNormalDistCGToFlanges
    ##  Returns the maximum normal distance from definition point to center of element   
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
         Returns the maximum normal distance from definition point to center of element   
            
         
        """
        pass
    
    ## Getter for property: (int) NumberOfDiscretizationPoints
    ##  Returns the number of connections   
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
         Returns the number of connections   
            
         
        """
        pass
    
    ## Setter for property: (int) NumberOfDiscretizationPoints

    ##  Returns the number of connections   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @NumberOfDiscretizationPoints.setter
    def NumberOfDiscretizationPoints(self, num: int):
        """
        Setter for property: (int) NumberOfDiscretizationPoints
         Returns the number of connections   
            
         
        """
        pass
    
    ## Getter for property: (int) NumberOfFlanges
    ##  Returns the number of flanges.  
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
         Returns the number of flanges.  
           When changing the number of flanges this is not applied till an update is performed by calling @link Update::DoUpdate Update::DoUpdate@endlink    
         
        """
        pass
    
    ## Setter for property: (int) NumberOfFlanges

    ##  Returns the number of flanges.  
    ##    When changing the number of flanges this is not applied till an update is performed by calling @link Update::DoUpdate Update::DoUpdate@endlink    
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @NumberOfFlanges.setter
    def NumberOfFlanges(self, numberOfFlanges: int):
        """
        Setter for property: (int) NumberOfFlanges
         Returns the number of flanges.  
           When changing the number of flanges this is not applied till an update is performed by calling @link Update::DoUpdate Update::DoUpdate@endlink    
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ProjectTolerance
    ##  Returns the projection tolerance   
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
         Returns the projection tolerance   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RxStiffnessConstant
    ##  Returns the RX stiffness constant   
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
         Returns the RX stiffness constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RyStiffnessConstant
    ##  Returns the RY stiffness constant   
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
         Returns the RY stiffness constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RzStiffnessConstant
    ##  Returns the RZ stiffness constant   
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
         Returns the RZ stiffness constant   
            
         
        """
        pass
    
    ## Getter for property: (@link StiffnessType NXOpen.CAE.Connections.StiffnessType@endlink) StiffnessType
    ##  Returns the stiffness type   
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
         Returns the stiffness type   
            
         
        """
        pass
    
    ## Setter for property: (@link StiffnessType NXOpen.CAE.Connections.StiffnessType@endlink) StiffnessType

    ##  Returns the stiffness type   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @StiffnessType.setter
    def StiffnessType(self, oStiffnessType: StiffnessType):
        """
        Setter for property: (@link StiffnessType NXOpen.CAE.Connections.StiffnessType@endlink) StiffnessType
         Returns the stiffness type   
            
         
        """
        pass
    
    ## Getter for property: (bool) UseMaxLengthStep
    ##  Returns the usage of max length step   
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
         Returns the usage of max length step   
            
         
        """
        pass
    
    ## Setter for property: (bool) UseMaxLengthStep

    ##  Returns the usage of max length step   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @UseMaxLengthStep.setter
    def UseMaxLengthStep(self, use: bool):
        """
        Setter for property: (bool) UseMaxLengthStep
         Returns the usage of max length step   
            
         
        """
        pass
    
    ## Getter for property: (bool) UseOriginalNodesOfConnection
    ##  Returns the usage of original nodes of connection   
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
         Returns the usage of original nodes of connection   
            
         
        """
        pass
    
    ## Setter for property: (bool) UseOriginalNodesOfConnection

    ##  Returns the usage of original nodes of connection   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @UseOriginalNodesOfConnection.setter
    def UseOriginalNodesOfConnection(self, use: bool):
        """
        Setter for property: (bool) UseOriginalNodesOfConnection
         Returns the usage of original nodes of connection   
            
         
        """
        pass
    
    ## Getter for property: (bool) WithOrientation
    ##  Returns the target type   
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
         Returns the target type   
            
         
        """
        pass
    
    ## Setter for property: (bool) WithOrientation

    ##  Returns the target type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @WithOrientation.setter
    def WithOrientation(self, orientation: bool):
        """
        Setter for property: (bool) WithOrientation
         Returns the target type   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) XStiffnessConstant
    ##  Returns the X stiffness constant   
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
         Returns the X stiffness constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) YStiffnessConstant
    ##  Returns the Y stiffness constant   
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
         Returns the Y stiffness constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ZStiffnessConstant
    ##  Returns the Z stiffness constant   
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
         Returns the Z stiffness constant   
            
         
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
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## Angle</term><description> 
##  Seam weld angle material type </description> </item><item><term> 
## Overlap</term><description> 
##  Seam weld overlap material type </description> </item><item><term> 
## Double</term><description> 
##  Seam weld double material type </description> </item></list>
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
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## Other</term><description> 
##  Unspecified </description> </item><item><term> 
## YJoint</term><description> 
##  Y-Joint </description> </item><item><term> 
## OverlapWeld</term><description> 
##  Overlap Weld </description> </item><item><term> 
## CornerWeld</term><description> 
##  Corner Weld </description> </item><item><term> 
## ButtJoint</term><description> 
##  Butt Joint </description> </item><item><term> 
## EdgeWeld</term><description> 
##  Edge Weld </description> </item><item><term> 
## DoubleCornerWeld</term><description> 
##  Corner Weld (Double) </description> </item><item><term> 
## CruciformJoint</term><description> 
##  Cruciform Joint </description> </item><item><term> 
## KJoint</term><description> 
##  K-Joint </description> </item><item><term> 
## IWeld</term><description> 
##  I-Weld </description> </item><item><term> 
## SplitIWeld</term><description> 
##  Split I-Weld </description> </item></list>
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
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## ConnectionNodes</term><description> 
##  Use the node locations in the USWC(s) </description> </item><item><term> 
## Specify</term><description> 
##  Explicitly specify nodes or a node group </description> </item></list>
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
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## OnLargerSheetAngle</term><description> 
##  Weld on Side of the Larger Sheet Angle </description> </item><item><term> 
## OnSmallerSheetAngle</term><description> 
##  Weld on Side of the Smaller Sheet Angle </description> </item><item><term> 
## OnBothSheetSides</term><description> 
##  Weld on Both Sides </description> </item></list>
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
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## WithMaterial</term><description> 
##  Seam weld done with material </description> </item><item><term> 
## WithLaser</term><description> 
##  Seam weld done by laser </description> </item><item><term> 
## Resistance</term><description> 
##  Seam weld done by resistance welding </description> </item><item><term> 
## Friction</term><description> 
##  Seam weld done by friction welding </description> </item><item><term> 
## Brazing</term><description> 
##  Seam weld done by braze welding </description> </item></list>
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
    ##  Returns the discretization method   
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
         Returns the discretization method   
            
         
        """
        pass
    
    ## Setter for property: (@link DiscretizationMethod NXOpen.CAE.Connections.DiscretizationMethod@endlink) DiscretizationMethod

    ##  Returns the discretization method   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @DiscretizationMethod.setter
    def DiscretizationMethod(self, method: DiscretizationMethod):
        """
        Setter for property: (@link DiscretizationMethod NXOpen.CAE.Connections.DiscretizationMethod@endlink) DiscretizationMethod
         Returns the discretization method   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) DistanceFromStart
    ##  Returns the line Discretization distance from start   
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
         Returns the line Discretization distance from start   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) DistanceToEnd
    ##  Returns the line Discretization distance to end   
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
         Returns the line Discretization distance to end   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Height
    ##  Returns the height value   
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
         Returns the height value   
            
         
        """
        pass
    
    ## Getter for property: (@link HeightType NXOpen.CAE.Connections.HeightType@endlink) HeightType
    ##  Returns the connection height type   
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
         Returns the connection height type   
            
         
        """
        pass
    
    ## Setter for property: (@link HeightType NXOpen.CAE.Connections.HeightType@endlink) HeightType

    ##  Returns the connection height type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @HeightType.setter
    def HeightType(self, heightType: HeightType):
        """
        Setter for property: (@link HeightType NXOpen.CAE.Connections.HeightType@endlink) HeightType
         Returns the connection height type   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) LengthStep
    ##  Returns the line Discretization length step   
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
         Returns the line Discretization length step   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.PhysicalMaterial NXOpen.PhysicalMaterial@endlink) Material
    ##  Returns the connection material   
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
         Returns the connection material   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.PhysicalMaterial NXOpen.PhysicalMaterial@endlink) Material

    ##  Returns the connection material   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @Material.setter
    def Material(self, material: NXOpen.PhysicalMaterial):
        """
        Setter for property: (@link NXOpen.PhysicalMaterial NXOpen.PhysicalMaterial@endlink) Material
         Returns the connection material   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxAngleBetweenNormals
    ##  Returns the maximum angle of normals with the projection surface   
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
         Returns the maximum angle of normals with the projection surface   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxDistCGToElemCG
    ##  Returns the maximum distance from definition point to center of support element   
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
         Returns the maximum distance from definition point to center of support element   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxLengthStep
    ##  Returns the line Discretization max length step   
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
         Returns the line Discretization max length step   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxNormalDistCGToFlanges
    ##  Returns the maximum normal distance from definition point to center of element   
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
         Returns the maximum normal distance from definition point to center of element   
            
         
        """
        pass
    
    ## Getter for property: (int) NumberOfDiscretizationPoints
    ##  Returns the number of connections   
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
         Returns the number of connections   
            
         
        """
        pass
    
    ## Setter for property: (int) NumberOfDiscretizationPoints

    ##  Returns the number of connections   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @NumberOfDiscretizationPoints.setter
    def NumberOfDiscretizationPoints(self, num: int):
        """
        Setter for property: (int) NumberOfDiscretizationPoints
         Returns the number of connections   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ProjectTolerance
    ##  Returns the projection tolerance   
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
         Returns the projection tolerance   
            
         
        """
        pass
    
    ## Getter for property: (@link SeamWeldMcfType NXOpen.CAE.Connections.SeamWeldMcfType@endlink) SeamWeldMcfType
    ##  Returns the seam weld MCF type   
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
         Returns the seam weld MCF type   
            
         
        """
        pass
    
    ## Setter for property: (@link SeamWeldMcfType NXOpen.CAE.Connections.SeamWeldMcfType@endlink) SeamWeldMcfType

    ##  Returns the seam weld MCF type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @SeamWeldMcfType.setter
    def SeamWeldMcfType(self, seamWeldMcfType: SeamWeldMcfType):
        """
        Setter for property: (@link SeamWeldMcfType NXOpen.CAE.Connections.SeamWeldMcfType@endlink) SeamWeldMcfType
         Returns the seam weld MCF type   
            
         
        """
        pass
    
    ## Getter for property: (@link SeamWeldType NXOpen.CAE.Connections.SeamWeldType@endlink) SeamWeldType
    ##  Returns the seam weld type   
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
         Returns the seam weld type   
            
         
        """
        pass
    
    ## Setter for property: (@link SeamWeldType NXOpen.CAE.Connections.SeamWeldType@endlink) SeamWeldType

    ##  Returns the seam weld type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @SeamWeldType.setter
    def SeamWeldType(self, seamWeldType: SeamWeldType):
        """
        Setter for property: (@link SeamWeldType NXOpen.CAE.Connections.SeamWeldType@endlink) SeamWeldType
         Returns the seam weld type   
            
         
        """
        pass
    
    ## Getter for property: (bool) UseMaxLengthStep
    ##  Returns the usage of max length step   
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
         Returns the usage of max length step   
            
         
        """
        pass
    
    ## Setter for property: (bool) UseMaxLengthStep

    ##  Returns the usage of max length step   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @UseMaxLengthStep.setter
    def UseMaxLengthStep(self, use: bool):
        """
        Setter for property: (bool) UseMaxLengthStep
         Returns the usage of max length step   
            
         
        """
        pass
    
    ## Getter for property: (bool) UseOriginalNodesOfConnection
    ##  Returns the usage of original nodes of connection   
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
         Returns the usage of original nodes of connection   
            
         
        """
        pass
    
    ## Setter for property: (bool) UseOriginalNodesOfConnection

    ##  Returns the usage of original nodes of connection   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @UseOriginalNodesOfConnection.setter
    def UseOriginalNodesOfConnection(self, use: bool):
        """
        Setter for property: (bool) UseOriginalNodesOfConnection
         Returns the usage of original nodes of connection   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Width
    ##  Returns the width value   
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
         Returns the width value   
            
         
        """
        pass
    
    ##  Convert to Flange-Side location type.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ## <param name="weldIndex"> (int) </param>
    def ConvertToFlangeSideLocationType(self, weldIndex: int) -> None:
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
    def ConvertToVectorLocationType(self, weldIndex: int) -> None:
        """
         Convert to Vector location type.
        """
        pass
    
    ##  Get default weld angle.
    ##  @return defaultAngle (@link NXOpen.Expression NXOpen.Expression@endlink): .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    def GetDefaultWeldAngle(self) -> NXOpen.Expression:
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
    def GetDefaultWeldPenetration(self) -> NXOpen.Expression:
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
    def GetDefaultWeldThickness(self) -> NXOpen.Expression:
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
    def GetDefaultWeldWidth(self) -> NXOpen.Expression:
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
    def GetMinMaxNumberOfWelds(self) -> Tuple[int, int]:
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
    def GetNumberOfWelds(self) -> int:
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
    def GetSeamWeldLocationParameter(self, weldIndex: int) -> float:
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
    def GetSeamWeldLocationType(self, weldIndex: int) -> SeamWeldLocationType:
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
    def GetSeamWeldLocationVector(self, weldIndex: int) -> NXOpen.Direction:
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
    def GetSeamWeldMaterial(self, weldIndex: int) -> NXOpen.PhysicalMaterial:
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
    def GetSeamWeldSectionType(self, weldIndex: int) -> SeamWeldSectionType:
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
    def GetSeamWeldShapeType(self, weldIndex: int) -> SeamWeldShapeType:
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
    def GetWeldAngle(self, weldIndex: int) -> NXOpen.Expression:
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
    def GetWeldPenetration(self, weldIndex: int) -> NXOpen.Expression:
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
    def GetWeldThickness(self, weldIndex: int) -> NXOpen.Expression:
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
    def GetWeldWidth(self, weldIndex: int) -> NXOpen.Expression:
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
    def SetNumberOfWelds(self, numWelds: int) -> None:
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
    def SetSeamWeldLocationParameter(self, weldIndex: int, locationParameter: float) -> None:
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
    def SetSeamWeldLocationType(self, weldIndex: int, seamWeldLocationType: SeamWeldLocationType) -> None:
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
    def SetSeamWeldLocationVector(self, weldIndex: int, locationVector: NXOpen.Direction) -> None:
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
    def SetSeamWeldMaterial(self, weldIndex: int, material: NXOpen.PhysicalMaterial) -> None:
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
    def SetSeamWeldSectionType(self, weldIndex: int, seamWeldSectionType: SeamWeldSectionType) -> None:
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
    def SetSeamWeldShapeType(self, weldIndex: int, seamWeldShapeType: SeamWeldShapeType) -> None:
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
    ##  Returns the Selection Recipe used for creating the location.  
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
         Returns the Selection Recipe used for creating the location.  
          
                        If the location type is not a Selection Recipe, this method will raise an error.   
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.CAE.SelectionRecipe NXOpen.CAE.SelectionRecipe@endlink) SelectionRecipe

    ##  Returns the Selection Recipe used for creating the location.  
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
         Returns the Selection Recipe used for creating the location.  
          
                        If the location type is not a Selection Recipe, this method will raise an error.   
         
        """
        pass
    
##  Shank length discretization definition types 
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## NotSet</term><description> 
##  No shank discretization for shank length </description> </item><item><term> 
## UserDefined</term><description> 
##  User defined length for shank discretization </description> </item><item><term> 
## PercentLength</term><description> 
##  Percentage of length for shank discretization </description> </item><item><term> 
## PercentCurve</term><description> 
##  Percentage of curve length for shank discretization </description> </item></list>
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
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## NotSet</term><description> 
##  No shank discretization for shank segments </description> </item><item><term> 
## SegmentLength</term><description> 
##  Segment length for shank segment discretization </description> </item><item><term> 
## NumSegments</term><description> 
##  Number of segments for shank segment discretization </description> </item></list>
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
    def Destroy(self) -> None:
        """
         Destroy the smart template tool object 
        """
        pass
    
    ##  Export PIDs to Groups
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: sc_gso_comp (" Simcenter NVH Composer")
    ## 
    ## <param name="caePart"> (@link NXOpen.CAE.CaePart NXOpen.CAE.CaePart@endlink)  The context Cae part</param>
    ## <param name="iAbsoluteExportPath"> (str) </param>
    def ExportPIDs(self, caePart: NXOpen.CAE.CaePart, iAbsoluteExportPath: str) -> None:
        """
         Export PIDs to Groups
        """
        pass
    
    ##  Export the requested result data to an Excel file 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: sc_gso_smart (" Simcenter Smart Template Pre/Post Applications")
    ## 
    ## <param name="pSimSolution"> (@link NXOpen.CAE.SimSolution NXOpen.CAE.SimSolution@endlink)  The solution. </param>
    ## <param name="iAbsoluteExportPath"> (str)  The path for the Excel file. </param>
    ## <param name="resultName"> (str)  The result name. </param>
    ## <param name="drivingPoints"> (bool)  The driving points. </param>
    ## <param name="indexFile"> (str)  The driving points. </param>
    def ExportResultDataToExcel(self, pSimSolution: NXOpen.CAE.SimSolution, iAbsoluteExportPath: str, resultName: str, drivingPoints: bool, indexFile: str) -> None:
        """
         Export the requested result data to an Excel file 
        """
        pass
    
    ##  Export SOL200 Design sensitivity analysis solution report
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: sc_gso_smart (" Simcenter Smart Template Pre/Post Applications")
    ## 
    ## <param name="pSimSolution"> (@link NXOpen.CAE.SimSolution NXOpen.CAE.SimSolution@endlink)  The SOL200 Design sensitivity analysis solution</param>
    ## <param name="iAbsoluteExportPath"> (str) </param>
    def ExportResults(self, pSimSolution: NXOpen.CAE.SimSolution, iAbsoluteExportPath: str) -> None:
        """
         Export SOL200 Design sensitivity analysis solution report
        """
        pass
    
    ##  Get Physical property tables associated to group
    ##  @return physicalPropertyTableTags (@link NXOpen.CAE.PhysicalPropertyTable List[NXOpen.CAE.PhysicalPropertyTable]@endlink):  Group elements associated physical property tables. .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: sc_gso_smart (" Simcenter Smart Template Pre/Post Applications")
    ## 
    ## <param name="caeGroup"> (@link NXOpen.CAE.CaeGroup NXOpen.CAE.CaeGroup@endlink)  Element or mesh entity type group </param>
    def GetGroupPhysicalPropertyTables(self, caeGroup: NXOpen.CAE.CaeGroup) -> List[NXOpen.CAE.PhysicalPropertyTable]:
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
    ## 
    ## <param name="iAbsoluteFilePath"> (str)  The path for the hard point file. </param>
    def GetHardPointNameAndType(self, iAbsoluteFilePath: str) -> Tuple[List[NXOpen.CAE.SelRecipeBaseStrategy.Type], List[str]]:
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
    ## <param name="smartTemplateTool"> (@link SmartTemplateTool NXOpen.CAE.Connections.SmartTemplateTool@endlink) </param>
    ## <param name="caePart"> (@link NXOpen.CAE.CaePart NXOpen.CAE.CaePart@endlink)  The context Cae part</param>
    ## <param name="iAbsoluteImportPath"> (str)  XML file</param>
    @overload
    def ImportGroups(self, caePart: NXOpen.CAE.CaePart, iAbsoluteImportPath: str) -> List[NXOpen.CAE.CaeGroup]:
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
    ## <param name="smartTemplateTool"> (@link SmartTemplateTool NXOpen.CAE.Connections.SmartTemplateTool@endlink) </param>
    ## <param name="caePart"> (@link NXOpen.CAE.CaePart NXOpen.CAE.CaePart@endlink)  The context Cae part</param>
    ## <param name="iAbsoluteImportPath"> (str)  XML file</param>
    ## <param name="selectedGroups"> (List[str]) </param>
    @overload
    def ImportGroups(self, caePart: NXOpen.CAE.CaePart, iAbsoluteImportPath: str, selectedGroups: List[str]) -> List[NXOpen.CAE.CaeGroup]:
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
    ##  Returns the coefficient for formula defined diameter   
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
         Returns the coefficient for formula defined diameter   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Diameter
    ##  Returns the connection diameter   
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
         Returns the connection diameter   
            
         
        """
        pass
    
    ## Getter for property: (@link DiameterType NXOpen.CAE.Connections.DiameterType@endlink) DiameterType
    ##  Returns the connection diameter type   
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
         Returns the connection diameter type   
            
         
        """
        pass
    
    ## Setter for property: (@link DiameterType NXOpen.CAE.Connections.DiameterType@endlink) DiameterType

    ##  Returns the connection diameter type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @DiameterType.setter
    def DiameterType(self, diameterType: DiameterType):
        """
        Setter for property: (@link DiameterType NXOpen.CAE.Connections.DiameterType@endlink) DiameterType
         Returns the connection diameter type   
            
         
        """
        pass
    
    ## Getter for property: (@link DiscretizationMethod NXOpen.CAE.Connections.DiscretizationMethod@endlink) DiscretizationMethod
    ##  Returns the discretization method   
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
         Returns the discretization method   
            
         
        """
        pass
    
    ## Setter for property: (@link DiscretizationMethod NXOpen.CAE.Connections.DiscretizationMethod@endlink) DiscretizationMethod

    ##  Returns the discretization method   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @DiscretizationMethod.setter
    def DiscretizationMethod(self, method: DiscretizationMethod):
        """
        Setter for property: (@link DiscretizationMethod NXOpen.CAE.Connections.DiscretizationMethod@endlink) DiscretizationMethod
         Returns the discretization method   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) DistanceFromStart
    ##  Returns the line Discretization distance from start   
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
         Returns the line Discretization distance from start   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) DistanceToEnd
    ##  Returns the line Discretization distance to end   
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
         Returns the line Discretization distance to end   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Height
    ##  Returns the height value   
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
         Returns the height value   
            
         
        """
        pass
    
    ## Getter for property: (@link HeightType NXOpen.CAE.Connections.HeightType@endlink) HeightType
    ##  Returns the connection height type   
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
         Returns the connection height type   
            
         
        """
        pass
    
    ## Setter for property: (@link HeightType NXOpen.CAE.Connections.HeightType@endlink) HeightType

    ##  Returns the connection height type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @HeightType.setter
    def HeightType(self, heightType: HeightType):
        """
        Setter for property: (@link HeightType NXOpen.CAE.Connections.HeightType@endlink) HeightType
         Returns the connection height type   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) LengthStep
    ##  Returns the line Discretization length step   
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
         Returns the line Discretization length step   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.PhysicalMaterial NXOpen.PhysicalMaterial@endlink) Material
    ##  Returns the connection material   
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
         Returns the connection material   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.PhysicalMaterial NXOpen.PhysicalMaterial@endlink) Material

    ##  Returns the connection material   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @Material.setter
    def Material(self, material: NXOpen.PhysicalMaterial):
        """
        Setter for property: (@link NXOpen.PhysicalMaterial NXOpen.PhysicalMaterial@endlink) Material
         Returns the connection material   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxAngleBetweenNormals
    ##  Returns the maximum angle of normals with the projection surface   
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
         Returns the maximum angle of normals with the projection surface   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxDistCGToElemCG
    ##  Returns the maximum distance from definition point to center of support element   
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
         Returns the maximum distance from definition point to center of support element   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxLengthStep
    ##  Returns the line Discretization max length step   
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
         Returns the line Discretization max length step   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxNormalDistCGToFlanges
    ##  Returns the maximum normal distance from definition point to center of element   
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
         Returns the maximum normal distance from definition point to center of element   
            
         
        """
        pass
    
    ## Getter for property: (int) NumberOfDiscretizationPoints
    ##  Returns the number of connections   
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
         Returns the number of connections   
            
         
        """
        pass
    
    ## Setter for property: (int) NumberOfDiscretizationPoints

    ##  Returns the number of connections   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @NumberOfDiscretizationPoints.setter
    def NumberOfDiscretizationPoints(self, num: int):
        """
        Setter for property: (int) NumberOfDiscretizationPoints
         Returns the number of connections   
            
         
        """
        pass
    
    ## Getter for property: (int) NumberOfFlanges
    ##  Returns the number of flanges.  
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
         Returns the number of flanges.  
           When changing the number of flanges this is not applied till an update is performed by calling @link Update::DoUpdate Update::DoUpdate@endlink    
         
        """
        pass
    
    ## Setter for property: (int) NumberOfFlanges

    ##  Returns the number of flanges.  
    ##    When changing the number of flanges this is not applied till an update is performed by calling @link Update::DoUpdate Update::DoUpdate@endlink    
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @NumberOfFlanges.setter
    def NumberOfFlanges(self, numberOfFlanges: int):
        """
        Setter for property: (int) NumberOfFlanges
         Returns the number of flanges.  
           When changing the number of flanges this is not applied till an update is performed by calling @link Update::DoUpdate Update::DoUpdate@endlink    
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ProjectTolerance
    ##  Returns the projection tolerance   
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
         Returns the projection tolerance   
            
         
        """
        pass
    
    ## Getter for property: (str) TableFile
    ##  Returns the table file used to compute the diameter   
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
         Returns the table file used to compute the diameter   
            
         
        """
        pass
    
    ## Setter for property: (str) TableFile

    ##  Returns the table file used to compute the diameter   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @TableFile.setter
    def TableFile(self, tableFile: str):
        """
        Setter for property: (str) TableFile
         Returns the table file used to compute the diameter   
            
         
        """
        pass
    
    ## Getter for property: (bool) UseMaxLengthStep
    ##  Returns the usage of max length step   
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
         Returns the usage of max length step   
            
         
        """
        pass
    
    ## Setter for property: (bool) UseMaxLengthStep

    ##  Returns the usage of max length step   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @UseMaxLengthStep.setter
    def UseMaxLengthStep(self, use: bool):
        """
        Setter for property: (bool) UseMaxLengthStep
         Returns the usage of max length step   
            
         
        """
        pass
    
    ## Getter for property: (bool) UseOriginalNodesOfConnection
    ##  Returns the usage of original nodes of connection   
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
         Returns the usage of original nodes of connection   
            
         
        """
        pass
    
    ## Setter for property: (bool) UseOriginalNodesOfConnection

    ##  Returns the usage of original nodes of connection   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @UseOriginalNodesOfConnection.setter
    def UseOriginalNodesOfConnection(self, use: bool):
        """
        Setter for property: (bool) UseOriginalNodesOfConnection
         Returns the usage of original nodes of connection   
            
         
        """
        pass
    
import NXOpen
##  Spring connection. Use this interface to set/get properties and parameters of the Spring connection.  
## 
##   <br>  Created in NX12.0.0  <br> 

class Spring(IConnection): 
    """ Spring connection. Use this interface to set/get properties and parameters of the Spring connection.  """


    ## Getter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) Csys
    ##  Returns the csys   
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
         Returns the csys   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) Csys

    ##  Returns the csys   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @Csys.setter
    def Csys(self, csys: NXOpen.CoordinateSystem):
        """
        Setter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) Csys
         Returns the csys   
            
         
        """
        pass
    
    ## Getter for property: (@link CsysType NXOpen.CAE.Connections.CsysType@endlink) CsysType
    ##  Returns the csys type   
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
         Returns the csys type   
            
         
        """
        pass
    
    ## Setter for property: (@link CsysType NXOpen.CAE.Connections.CsysType@endlink) CsysType

    ##  Returns the csys type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @CsysType.setter
    def CsysType(self, csysType: CsysType):
        """
        Setter for property: (@link CsysType NXOpen.CAE.Connections.CsysType@endlink) CsysType
         Returns the csys type   
            
         
        """
        pass
    
    ## Getter for property: (bool) IsMassOnBothTargets
    ##  Returns the isMassOnBothTargets   
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
         Returns the isMassOnBothTargets   
            
         
        """
        pass
    
    ## Setter for property: (bool) IsMassOnBothTargets

    ##  Returns the isMassOnBothTargets   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @IsMassOnBothTargets.setter
    def IsMassOnBothTargets(self, isMassOnBothTargets: bool):
        """
        Setter for property: (bool) IsMassOnBothTargets
         Returns the isMassOnBothTargets   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Mass
    ##  Returns the mass value   
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
         Returns the mass value   
            
         
        """
        pass
    
    ## Getter for property: (@link NodalPairingMethod NXOpen.CAE.Connections.NodalPairingMethod@endlink) PairingMethod
    ##  Returns the pairing method of targets   
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
         Returns the pairing method of targets   
            
         
        """
        pass
    
    ## Setter for property: (@link NodalPairingMethod NXOpen.CAE.Connections.NodalPairingMethod@endlink) PairingMethod

    ##  Returns the pairing method of targets   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @PairingMethod.setter
    def PairingMethod(self, method: NodalPairingMethod):
        """
        Setter for property: (@link NodalPairingMethod NXOpen.CAE.Connections.NodalPairingMethod@endlink) PairingMethod
         Returns the pairing method of targets   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RxStiffnessConstant
    ##  Returns the RX stiffness constant   
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
         Returns the RX stiffness constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RyStiffnessConstant
    ##  Returns the RY stiffness constant   
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
         Returns the RY stiffness constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RzStiffnessConstant
    ##  Returns the RZ stiffness constant   
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
         Returns the RZ stiffness constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) SearchConeAngle
    ##  Returns the search cone angle   
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
         Returns the search cone angle   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) SearchOrientation
    ##  Returns the pairing search orientation   
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
         Returns the pairing search orientation   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) SearchOrientation

    ##  Returns the pairing search orientation   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @SearchOrientation.setter
    def SearchOrientation(self, orientation: NXOpen.Direction):
        """
        Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) SearchOrientation
         Returns the pairing search orientation   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) SearchRange
    ##  Returns the search range   
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
         Returns the search range   
            
         
        """
        pass
    
    ## Getter for property: (@link StiffnessType NXOpen.CAE.Connections.StiffnessType@endlink) StiffnessType
    ##  Returns the stiffness type   
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
         Returns the stiffness type   
            
         
        """
        pass
    
    ## Setter for property: (@link StiffnessType NXOpen.CAE.Connections.StiffnessType@endlink) StiffnessType

    ##  Returns the stiffness type   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @StiffnessType.setter
    def StiffnessType(self, oStiffnessType: StiffnessType):
        """
        Setter for property: (@link StiffnessType NXOpen.CAE.Connections.StiffnessType@endlink) StiffnessType
         Returns the stiffness type   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) XStiffnessConstant
    ##  Returns the X stiffness constant   
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
         Returns the X stiffness constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) YStiffnessConstant
    ##  Returns the Y stiffness constant   
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
         Returns the Y stiffness constant   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ZStiffnessConstant
    ##  Returns the Z stiffness constant   
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
         Returns the Z stiffness constant   
            
         
        """
        pass
    
##  Stiffness type 
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## PerElement</term><description> 
##  Stiffness value will be specified per element </description> </item><item><term> 
## PerUnitLength</term><description> 
##  Stiffness value will be specified per unit length </description> </item></list>
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
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## NotSet</term><description> 
##  No dependency </description> </item><item><term> 
## Dependent</term><description> 
##  Dependent target </description> </item><item><term> 
## Independent</term><description> 
##  Independent target </description> </item></list>
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
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## Unknown</term><description> 
##  Connection state cannot be determined </description> </item><item><term> 
## Meshed</term><description> 
##  The Connection is meshed </description> </item><item><term> 
## NotMeshed</term><description> 
##  The Connection is not meshed </description> </item><item><term> 
## Invalid</term><description> 
##  The Connection is not valid </description> </item></list>
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
    ## <param name="iConnections"> (@link LMIEConnection List[NXOpen.CAE.Connections.LMIEConnection]@endlink)  The array of input lumped mass intermediate representations </param>
    ## <param name="iAbsoluteExportPath"> (str)  The absolute path where the connections are to be exported </param>
    ## <param name="iConvertConnectionDataFromPartUnits"> (bool)  If the interchange data unit system is different from the part unit system, we want to convert the data before exporting </param>
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
    ## <param name="iConnections"> (@link IConnection List[NXOpen.CAE.Connections.IConnection]@endlink)  The array of input connections </param>
    ## <param name="type"> (@link ConnectionType NXOpen.CAE.Connections.ConnectionType@endlink)  The connection type to filter by </param>
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
    ## <param name="feature"> (@link NXOpen.Features.Feature NXOpen.Features.Feature@endlink)  The context Feature </param>
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
    ## <param name="iBoltConnection"> (@link IConnection NXOpen.CAE.Connections.IConnection@endlink)  The Bolt Universal Connection </param>
    ## <param name="locationIndex"> (int) </param>
    ## <param name="coordinateIndex"> (int) </param>
    ## <param name="boltSupportIndex"> (int) </param>
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
    ## <param name="constraintFilePath"> (str)  The absolute path of the constraint file to be parsed </param>
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
    ## <param name="feModel"> (@link NXOpen.CAE.IFEModel NXOpen.CAE.IFEModel@endlink)  The FeModel </param>
    ## <param name="fromChildren"> (bool)  For AFEM retrieve labels also from children </param>
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
    ## <param name="body"> (@link NXOpen.Body NXOpen.Body@endlink)  The context Body </param>
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
    ## <param name="feModel"> (@link NXOpen.CAE.IFEModel NXOpen.CAE.IFEModel@endlink)  The FeModel </param>
    ## <param name="iElementCollectors"> (@link NXOpen.CAE.Mesh List[NXOpen.CAE.Mesh]@endlink)  The Meshes </param>
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
    ## <param name="conversionLengthUnit"> (@link NXOpen.Unit NXOpen.Unit@endlink)  The length unit </param>
    ## <param name="conversionMassUnit"> (@link NXOpen.Unit NXOpen.Unit@endlink)  The mass unit </param>
    ## <param name="iConnections"> (@link LumpedMass List[NXOpen.CAE.Connections.LumpedMass]@endlink)  The array of input lumped mass connections </param>
    ## <param name="iAbsoluteExportPath"> (str)  The absolute path where the connections are to be exported </param>
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
    ## <param name="feModel"> (@link NXOpen.CAE.IFEModel NXOpen.CAE.IFEModel@endlink)  The FeModel </param>
    ## <param name="fromChildren"> (bool)  For AFEM retrieve labels also from children </param>
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
    ## <param name="iConnection"> (@link IConnection NXOpen.CAE.Connections.IConnection@endlink)  The Universal Connection </param>
    ## <param name="locationIndex"> (int) </param>
    ## <param name="coordinateIndex"> (int) </param>
    ## <param name="flangeIndex"> (int) </param>
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
    ## <param name="iConnections"> (@link IConnection List[NXOpen.CAE.Connections.IConnection]@endlink)  The array of input connections </param>
    def GetProjectionPoints(iConnections: List[IConnection]) -> Tuple[List[NXOpen.INXObject], List[NXOpen.Point3d], List[int]]:
        """
         Returns the projection points of the connections per geometry flanges
         @return A tuple consisting of (oFlanges, oProjectionPoints, oFlangeObjectIndexList). 
         - oFlanges is: @link NXOpen.INXObject List[NXOpen.INXObject]@endlink. The array of the geometry flange objects .
         - oProjectionPoints is: @link NXOpen.Point3d List[NXOpen.Point3d]@endlink. The array of the projection points .
         - oFlangeObjectIndexList is: List[int]. The array of projection point index ranges per flanges. The size of the array is number of flanges + 1. For the flange i the index range is [oFlangeObjectIndexList[i], ..., oFlangeObjectIndexList[i + 1] - 1]. .

        """
        pass
    
    ##  Returns the projection points of the connections per geometry faces
    ##  @return A tuple consisting of (oFaces, oProjectionPoints, oFaceObjectIndexList). 
    ##  - oFaces is: @link NXOpen.CAE.CAEFace List[NXOpen.CAE.CAEFace]@endlink. The array of the geometry face objects .
    ##  - oProjectionPoints is: @link NXOpen.Point3d List[NXOpen.Point3d]@endlink. The array of the projection points .
    ##  - oFaceObjectIndexList is: List[int]. The array of projection point index ranges per faces. The size of the array is number of faces + 1. For the face i the index range is [oFaceObjectIndexList[i], ..., oFaceObjectIndexList[i + 1] - 1]. .

    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: None.
    ## <param name="iConnections"> (@link IConnection List[NXOpen.CAE.Connections.IConnection]@endlink)  The array of input connections </param>
    def GetProjectionPointsOnFaces(iConnections: List[IConnection]) -> Tuple[List[NXOpen.CAE.CAEFace], List[NXOpen.Point3d], List[int]]:
        """
         Returns the projection points of the connections per geometry faces
         @return A tuple consisting of (oFaces, oProjectionPoints, oFaceObjectIndexList). 
         - oFaces is: @link NXOpen.CAE.CAEFace List[NXOpen.CAE.CAEFace]@endlink. The array of the geometry face objects .
         - oProjectionPoints is: @link NXOpen.Point3d List[NXOpen.Point3d]@endlink. The array of the projection points .
         - oFaceObjectIndexList is: List[int]. The array of projection point index ranges per faces. The size of the array is number of faces + 1. For the face i the index range is [oFaceObjectIndexList[i], ..., oFaceObjectIndexList[i + 1] - 1]. .

        """
        pass
    
    ##  Imports the intermediate connection representations of lumped mass connections from external file. File type is determined by the extension. 
    ##  @return oConnections (@link LMIEConnection List[NXOpen.CAE.Connections.LMIEConnection]@endlink):  The intermediate connection representations .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## <param name="contextPart"> (@link NXOpen.INXObject NXOpen.INXObject@endlink) </param>
    ## <param name="iAbsoluteImportPath"> (str)  The absolute path where the connections are to be imported from </param>
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
    ## <param name="femPart"> (@link NXOpen.CAE.FemPart NXOpen.CAE.FemPart@endlink)  The context fem part</param>
    ## <param name="cadFeature"> (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink)  The cad entity </param>
    ## <param name="syncGeomData"> (bool)  Synchronize CAD Geometry option if new entitiy is created </param>
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
    def PrintConnectionInformationFile(connection: IConnection) -> None:
        """
         Print the connection's information file 
        """
        pass
    
    ##  Reimport mesh created by external mesher. The work part should be a FEM meshed with an external mesher. 
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: sc_gso_abmesh (" Simcenter GSO Ansa Batch Mesh environment")
    def ReimportMesh() -> None:
        """
         Reimport mesh created by external mesher. The work part should be a FEM meshed with an external mesher. 
        """
        pass
    
    ##  Redo labeling of current work AFEM physical properties. The work part should be a AFEM.  
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: sc_gso_creation (" Simcenter GSO BIW Creation environment")
    ## <param name="assyFemPart"> (@link NXOpen.CAE.AssyFemPart NXOpen.CAE.AssyFemPart@endlink)  The context Assembly FEM Part</param>
    def RelabelAFEMPhysicalProperty(assyFemPart: NXOpen.CAE.AssyFemPart) -> None:
        """
         Redo labeling of current work AFEM physical properties. The work part should be a AFEM.  
        """
        pass
    
    ##  Redo labeling of current work AFEM. The work part should be a AFEM.  
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: sc_gso_creation (" Simcenter GSO BIW Creation environment")
    def RelabelAfem() -> None:
        """
         Redo labeling of current work AFEM. The work part should be a AFEM.  
        """
        pass
    
    ##  Relabel assembly FEM with offset start ID 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: sc_gso_creation (" Simcenter GSO BIW Creation environment") OR sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer")
    ## <param name="assyFemPart"> (@link NXOpen.CAE.AssyFemPart NXOpen.CAE.AssyFemPart@endlink)  The context Assembly FEM Part</param>
    ## <param name="node_offset"> (int) </param>
    ## <param name="elem_offset"> (int) </param>
    ## <param name="csys_offset"> (int) </param>
    ## <param name="phys_offset"> (int) </param>
    def RelabelAfmOffsets(assyFemPart: NXOpen.CAE.AssyFemPart, node_offset: int, elem_offset: int, csys_offset: int, phys_offset: int) -> None:
        """
         Relabel assembly FEM with offset start ID 
        """
        pass
    
    ##  Remesh Seam Weld Connection Compatible Components 
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: sc_gso_abmesh (" Simcenter GSO Ansa Batch Mesh environment")
    ## <param name="connections"> (@link IConnection List[NXOpen.CAE.Connections.IConnection]@endlink)  The array of input connections </param>
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
    ## <param name="iConnections"> (@link IConnection List[NXOpen.CAE.Connections.IConnection]@endlink)  The array of input connections </param>
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
    def SplitWarpedQuads() -> None:
        """
         Splits the warped quads by invoking an external mesher. The work part should be a FEM meshed with an external mesher. 
        """
        pass
    
    ##  Write XYZ Coordinates to Constraint File 
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: sc_gso_abmesh (" Simcenter GSO Ansa Batch Mesh environment")
    ## <param name="constraintFilePath"> (str)  The absolute path of the constraint file to be parsed </param>
    ## <param name="connectionName"> (str) </param>
    ## <param name="coordinates"> (@link NXOpen.Point3d List[NXOpen.Point3d]@endlink)  The array of the coordinates to be exported </param>
    def WriteCoordinatesToConstraintFile(constraintFilePath: str, connectionName: str, coordinates: List[NXOpen.Point3d]) -> None:
        """
         Write XYZ Coordinates to Constraint File 
        """
        pass
    
## @package NXOpen.CAE.Connections
## Classes, Enums and Structs under NXOpen.CAE.Connections namespace

