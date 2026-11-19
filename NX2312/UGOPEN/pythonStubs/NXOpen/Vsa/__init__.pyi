from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
## 
##     
##      <br> To create a new instance of this class, use @link NXOpen::Vsa::VsaManager::CreateAssemblyOperationBuilder  NXOpen::Vsa::VsaManager::CreateAssemblyOperationBuilder @endlink  <br> 
## 
##  <br>  Usable only on Windows <br>  
## 
##   <br>  Created in NX1899.0.0  <br> 

class AssemblyOperationBuilder(NXOpen.Builder): 
    """
    
    """


    ## 
    ##         
    ##         
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Normal</term><description> 
    ## </description> </item><item><term> 
    ## Uniform</term><description> 
    ## </description> </item><item><term> 
    ## Extreme</term><description> 
    ## </description> </item><item><term> 
    ## DirectionalBias</term><description> 
    ## </description> </item><item><term> 
    ## RotationalBias</term><description> 
    ## </description> </item></list>
    class APIEnumDistributionFloatType(Enum):
        """
        Members Include: <Normal> <Uniform> <Extreme> <DirectionalBias> <RotationalBias>
        """
        Normal: int
        Uniform: int
        Extreme: int
        DirectionalBias: int
        RotationalBias: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> AssemblyOperationBuilder.APIEnumDistributionFloatType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (float) DirectionDistributionI
    ##   the Normal distribution   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return float
    @property
    def DirectionDistributionI(self) -> float:
        """
        Getter for property: (float) DirectionDistributionI
          the Normal distribution   
            
         
        """
        pass
    
    ## Setter for property: (float) DirectionDistributionI

    ##   the Normal distribution   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @DirectionDistributionI.setter
    def DirectionDistributionI(self, directionDistributionI: float):
        """
        Setter for property: (float) DirectionDistributionI
          the Normal distribution   
            
         
        """
        pass
    
    ## Getter for property: (float) DirectionDistributionJ
    ##   the  Normal distribution   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return float
    @property
    def DirectionDistributionJ(self) -> float:
        """
        Getter for property: (float) DirectionDistributionJ
          the  Normal distribution   
            
         
        """
        pass
    
    ## Setter for property: (float) DirectionDistributionJ

    ##   the  Normal distribution   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @DirectionDistributionJ.setter
    def DirectionDistributionJ(self, directionDistributionJ: float):
        """
        Setter for property: (float) DirectionDistributionJ
          the  Normal distribution   
            
         
        """
        pass
    
    ## Getter for property: (float) DirectionDistributionK
    ##   the  Normal distribution   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return float
    @property
    def DirectionDistributionK(self) -> float:
        """
        Getter for property: (float) DirectionDistributionK
          the  Normal distribution   
            
         
        """
        pass
    
    ## Setter for property: (float) DirectionDistributionK

    ##   the  Normal distribution   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @DirectionDistributionK.setter
    def DirectionDistributionK(self, directionDistributionK: float):
        """
        Setter for property: (float) DirectionDistributionK
          the  Normal distribution   
            
         
        """
        pass
    
    ## Getter for property: (@link AssemblyOperationBuilder.APIEnumDistributionFloatType NXOpen.Vsa.AssemblyOperationBuilder.APIEnumDistributionFloatType@endlink) DistributionFloatType
    ##   the enum  Float Type.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return AssemblyOperationBuilder.APIEnumDistributionFloatType
    @property
    def DistributionFloatType(self) -> AssemblyOperationBuilder.APIEnumDistributionFloatType:
        """
        Getter for property: (@link AssemblyOperationBuilder.APIEnumDistributionFloatType NXOpen.Vsa.AssemblyOperationBuilder.APIEnumDistributionFloatType@endlink) DistributionFloatType
          the enum  Float Type.  
             
         
        """
        pass
    
    ## Setter for property: (@link AssemblyOperationBuilder.APIEnumDistributionFloatType NXOpen.Vsa.AssemblyOperationBuilder.APIEnumDistributionFloatType@endlink) DistributionFloatType

    ##   the enum  Float Type.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @DistributionFloatType.setter
    def DistributionFloatType(self, distributionFloatType: AssemblyOperationBuilder.APIEnumDistributionFloatType):
        """
        Setter for property: (@link AssemblyOperationBuilder.APIEnumDistributionFloatType NXOpen.Vsa.AssemblyOperationBuilder.APIEnumDistributionFloatType@endlink) DistributionFloatType
          the enum  Float Type.  
             
         
        """
        pass
    
    ## Getter for property: (bool) OverrideDefaultFloatDist
    ##   the property represents  override defualt distribution float flag.  
    ##      
    ##  
    ## Getter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return bool
    @property
    def OverrideDefaultFloatDist(self) -> bool:
        """
        Getter for property: (bool) OverrideDefaultFloatDist
          the property represents  override defualt distribution float flag.  
             
         
        """
        pass
    
    ## Setter for property: (bool) OverrideDefaultFloatDist

    ##   the property represents  override defualt distribution float flag.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @OverrideDefaultFloatDist.setter
    def OverrideDefaultFloatDist(self, overrideDefaultFloatDist: bool):
        """
        Setter for property: (bool) OverrideDefaultFloatDist
          the property represents  override defualt distribution float flag.  
             
         
        """
        pass
    
    ## Getter for property: (str) StrDescription
    ##   the str description   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return str
    @property
    def StrDescription(self) -> str:
        """
        Getter for property: (str) StrDescription
          the str description   
            
         
        """
        pass
    
    ## Setter for property: (str) StrDescription

    ##   the str description   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @StrDescription.setter
    def StrDescription(self, strDescription: str):
        """
        Setter for property: (str) StrDescription
          the str description   
            
         
        """
        pass
    
    ## Getter for property: (str) StrName
    ##   the str name   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return str
    @property
    def StrName(self) -> str:
        """
        Getter for property: (str) StrName
          the str name   
            
         
        """
        pass
    
    ## Setter for property: (str) StrName

    ##   the str name   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @StrName.setter
    def StrName(self, strName: str):
        """
        Setter for property: (str) StrName
          the str name   
            
         
        """
        pass
    
    ##  It's a function to add constraints to the assembly operation  
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def ButtonAdd(builder: AssemblyOperationBuilder) -> None:
        """
         It's a function to add constraints to the assembly operation  
        """
        pass
    
    ##  Function to auto order the existing constraints 
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def ButtonAutoOrder(builder: AssemblyOperationBuilder) -> None:
        """
         Function to auto order the existing constraints 
        """
        pass
    
    ##  It's a function to clears constraints from the dialog box 
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def ButtonClear(builder: AssemblyOperationBuilder) -> None:
        """
         It's a function to clears constraints from the dialog box 
        """
        pass
    
    ##  Function to hide the shown normal 
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def ButtonHideNormal(builder: AssemblyOperationBuilder) -> None:
        """
         Function to hide the shown normal 
        """
        pass
    
    ##  It's a function to modify the existing constraints
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def ButtonModify(builder: AssemblyOperationBuilder) -> None:
        """
         It's a function to modify the existing constraints
        """
        pass
    
    ##  Function to move the existing constraint down 
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def ButtonMoveDown(builder: AssemblyOperationBuilder) -> None:
        """
         Function to move the existing constraint down 
        """
        pass
    
    ##  Function to move the existing constraint up
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def ButtonMoveUp(builder: AssemblyOperationBuilder) -> None:
        """
         Function to move the existing constraint up
        """
        pass
    
    ##  Function to remove the existing constraint 
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def ButtonObjectRemove(builder: AssemblyOperationBuilder) -> None:
        """
         Function to remove the existing constraint 
        """
        pass
    
    ##  It's a function to modify the existing constraints
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def ButtonRemove(builder: AssemblyOperationBuilder) -> None:
        """
         It's a function to modify the existing constraints
        """
        pass
    
    ##  Function to show normal of the selected constraint 
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def ButtonShowNormal(builder: AssemblyOperationBuilder) -> None:
        """
         Function to show normal of the selected constraint 
        """
        pass
    
    ##  Function to modify the existing constraints
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def ButtonValidate(builder: AssemblyOperationBuilder) -> None:
        """
         Function to modify the existing constraints
        """
        pass
    
    ##  The Constaint Object 
    ##  @return feature (@link NXOpen.NXObject NXOpen.NXObject@endlink): .
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="index"> (int) </param>
    def GetConstraintObjetItem(builder: AssemblyOperationBuilder, index: int) -> NXOpen.NXObject:
        """
         The Constaint Object 
         @return feature (@link NXOpen.NXObject NXOpen.NXObject@endlink): .
        """
        pass
    
    ##  The Constaint Target 
    ##  @return feature (@link NXOpen.NXObject NXOpen.NXObject@endlink): .
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="index"> (int) </param>
    def GetConstraintTargetItem(builder: AssemblyOperationBuilder, index: int) -> NXOpen.NXObject:
        """
         The Constaint Target 
         @return feature (@link NXOpen.NXObject NXOpen.NXObject@endlink): .
        """
        pass
    
    ##  The Fastener Size 
    ##  @return fastenerSize (float): .
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="index"> (int) </param>
    def GetFastenerSizeItem(builder: AssemblyOperationBuilder, index: int) -> float:
        """
         The Fastener Size 
         @return fastenerSize (float): .
        """
        pass
    
    ##  The Fastner Type 
    ##  @return fastnerType (bool): .
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="index"> (int) </param>
    def GetFastenerTypeItem(builder: AssemblyOperationBuilder, index: int) -> bool:
        """
         The Fastner Type 
         @return fastnerType (bool): .
        """
        pass
    
    ##  The Float Type 
    ##  @return floatType (bool): .
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="index"> (int) </param>
    def GetFloatTypeItem(builder: AssemblyOperationBuilder, index: int) -> bool:
        """
         The Float Type 
         @return floatType (bool): .
        """
        pass
    
    ##  Gets One Object Being Moved 
    ##  @return part (@link NXOpen.NXObject NXOpen.NXObject@endlink): .
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="index"> (int) </param>
    def GetObjectBeingMovedItem(builder: AssemblyOperationBuilder, index: int) -> NXOpen.NXObject:
        """
         Gets One Object Being Moved 
         @return part (@link NXOpen.NXObject NXOpen.NXObject@endlink): .
        """
        pass
    
    ##  The Remove Constraint 
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="index"> (int) </param>
    def RemoveConstraint(builder: AssemblyOperationBuilder, index: int) -> None:
        """
         The Remove Constraint 
        """
        pass
    
    ##  The Constaint Object 
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ## <param name="index"> (int) </param>
    ## <param name="feature"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    def SetConstraintObjetItem(builder: AssemblyOperationBuilder, index: int, feature: NXOpen.NXObject) -> None:
        """
         The Constaint Object 
        """
        pass
    
    ##  The Constaint Target 
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ## <param name="index"> (int) </param>
    ## <param name="feature"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    def SetConstraintTargetItem(builder: AssemblyOperationBuilder, index: int, feature: NXOpen.NXObject) -> None:
        """
         The Constaint Target 
        """
        pass
    
    ##  The Fastener Size 
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ## <param name="index"> (int) </param>
    ## <param name="fastenerSize"> (float) </param>
    def SetFastenerSizeItem(builder: AssemblyOperationBuilder, index: int, fastenerSize: float) -> None:
        """
         The Fastener Size 
        """
        pass
    
    ##  The Float Type 
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ## <param name="index"> (int) </param>
    ## <param name="fastnerType"> (bool) </param>
    def SetFastenerTypeItem(builder: AssemblyOperationBuilder, index: int, fastnerType: bool) -> None:
        """
         The Float Type 
        """
        pass
    
    ##  The Float Type 
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ## <param name="index"> (int) </param>
    ## <param name="floatType"> (bool) </param>
    def SetFloatTypeItem(builder: AssemblyOperationBuilder, index: int, floatType: bool) -> None:
        """
         The Float Type 
        """
        pass
    
    ##  Sets One Object Being Moved 
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ## <param name="index"> (int) </param>
    ## <param name="part"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    def SetObjectBeingMovedItem(builder: AssemblyOperationBuilder, index: int, part: NXOpen.NXObject) -> None:
        """
         Sets One Object Being Moved 
        """
        pass
    
    ##  The swap the existing  Constraint 
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="nIndex1"> (int) </param>
    ## <param name="nIndex2"> (int) </param>
    def SwapConstraint(builder: AssemblyOperationBuilder, nIndex1: int, nIndex2: int) -> None:
        """
         The swap the existing  Constraint 
        """
        pass
    
import NXOpen
##  Represents a class that is used for NX testing.  This class should not
## be made available to customers  <br> Use the static method in this class to obtain an instance.  <br> 
## 
##  <br>  Usable only on Windows <br>  
## 
##   <br>  Created in NX1953.0.0  <br> 

class AutotestValidation(NXOpen.Object): 
    """ Represents a class that is used for NX testing.  This class should not
be made available to customers """


    ##  Print all Measurement operation simulation result 
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def ValidateSimulationResultAll() -> None:
        """
         Print all Measurement operation simulation result 
        """
        pass
    
import NXOpen
## 
##     
##      <br> To create a new instance of this class, use @link NXOpen::Vsa::VsaManager::CreateBallFeatureBuilder  NXOpen::Vsa::VsaManager::CreateBallFeatureBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## DoubleAnchorX </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleAnchorY </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleAnchorZ </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleDiameter </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleKurtosisForm </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleKurtosisLoc </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleKurtosisSize </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleSkewnessForm </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleSkewnessLoc </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleSkewnessSize </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## EnumForm </term> <description> 
##  
## Normal </description> </item> 
## 
## <item><term> 
##  
## EnumLoc </term> <description> 
##  
## Normal </description> </item> 
## 
## </list> 

## 
##  <br>  Usable only on Windows <br>  
## 
##   <br>  Created in NX2306.0.0  <br> 

class BallFeatureBuilder(NXOpen.Builder): 
    """
    
    """


    ## 
    ##         
    ##         
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Normal</term><description> 
    ## </description> </item><item><term> 
    ## Uniform</term><description> 
    ## </description> </item><item><term> 
    ## Extreme</term><description> 
    ## </description> </item><item><term> 
    ## Pearson</term><description> 
    ## </description> </item><item><term> 
    ## Trapeziodal</term><description> 
    ## </description> </item></list>
    class APIEnumForm(Enum):
        """
        Members Include: <Normal> <Uniform> <Extreme> <Pearson> <Trapeziodal>
        """
        Normal: int
        Uniform: int
        Extreme: int
        Pearson: int
        Trapeziodal: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> BallFeatureBuilder.APIEnumForm:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## 
    ##         
    ##         
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Normal</term><description> 
    ## </description> </item><item><term> 
    ## Uniform</term><description> 
    ## </description> </item><item><term> 
    ## Extreme</term><description> 
    ## </description> </item><item><term> 
    ## Pearson</term><description> 
    ## </description> </item><item><term> 
    ## Trapeziodal</term><description> 
    ## </description> </item></list>
    class APIEnumLoc(Enum):
        """
        Members Include: <Normal> <Uniform> <Extreme> <Pearson> <Trapeziodal>
        """
        Normal: int
        Uniform: int
        Extreme: int
        Pearson: int
        Trapeziodal: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> BallFeatureBuilder.APIEnumLoc:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## 
    ##         
    ##         
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Normal</term><description> 
    ## </description> </item><item><term> 
    ## Uniform</term><description> 
    ## </description> </item><item><term> 
    ## Extreme</term><description> 
    ## </description> </item><item><term> 
    ## Pearson</term><description> 
    ## </description> </item><item><term> 
    ## Trapeziodal</term><description> 
    ## </description> </item></list>
    class APIEnumSize(Enum):
        """
        Members Include: <Normal> <Uniform> <Extreme> <Pearson> <Trapeziodal>
        """
        Normal: int
        Uniform: int
        Extreme: int
        Pearson: int
        Trapeziodal: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> BallFeatureBuilder.APIEnumSize:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (float) DoubleAnchorX
    ##   the double anchor x   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return float
    @property
    def DoubleAnchorX(self) -> float:
        """
        Getter for property: (float) DoubleAnchorX
          the double anchor x   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleAnchorX

    ##   the double anchor x   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @DoubleAnchorX.setter
    def DoubleAnchorX(self, doubleAnchorX: float):
        """
        Setter for property: (float) DoubleAnchorX
          the double anchor x   
            
         
        """
        pass
    
    ## Getter for property: (float) DoubleAnchorY
    ##   the double anchor y   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return float
    @property
    def DoubleAnchorY(self) -> float:
        """
        Getter for property: (float) DoubleAnchorY
          the double anchor y   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleAnchorY

    ##   the double anchor y   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @DoubleAnchorY.setter
    def DoubleAnchorY(self, doubleAnchorY: float):
        """
        Setter for property: (float) DoubleAnchorY
          the double anchor y   
            
         
        """
        pass
    
    ## Getter for property: (float) DoubleAnchorZ
    ##   the double anchor z   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return float
    @property
    def DoubleAnchorZ(self) -> float:
        """
        Getter for property: (float) DoubleAnchorZ
          the double anchor z   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleAnchorZ

    ##   the double anchor z   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @DoubleAnchorZ.setter
    def DoubleAnchorZ(self, doubleAnchorZ: float):
        """
        Setter for property: (float) DoubleAnchorZ
          the double anchor z   
            
         
        """
        pass
    
    ## Getter for property: (float) DoubleDiameter
    ##   the double diameter   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return float
    @property
    def DoubleDiameter(self) -> float:
        """
        Getter for property: (float) DoubleDiameter
          the double diameter   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleDiameter

    ##   the double diameter   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @DoubleDiameter.setter
    def DoubleDiameter(self, doubleDiameter: float):
        """
        Setter for property: (float) DoubleDiameter
          the double diameter   
            
         
        """
        pass
    
    ## Getter for property: (float) DoubleKurtosisForm
    ##   the double kurtosis form   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return float
    @property
    def DoubleKurtosisForm(self) -> float:
        """
        Getter for property: (float) DoubleKurtosisForm
          the double kurtosis form   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleKurtosisForm

    ##   the double kurtosis form   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @DoubleKurtosisForm.setter
    def DoubleKurtosisForm(self, doubleKurtosisForm: float):
        """
        Setter for property: (float) DoubleKurtosisForm
          the double kurtosis form   
            
         
        """
        pass
    
    ## Getter for property: (float) DoubleKurtosisLoc
    ##   the double kurtosis loc   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return float
    @property
    def DoubleKurtosisLoc(self) -> float:
        """
        Getter for property: (float) DoubleKurtosisLoc
          the double kurtosis loc   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleKurtosisLoc

    ##   the double kurtosis loc   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @DoubleKurtosisLoc.setter
    def DoubleKurtosisLoc(self, doubleKurtosisLoc: float):
        """
        Setter for property: (float) DoubleKurtosisLoc
          the double kurtosis loc   
            
         
        """
        pass
    
    ## Getter for property: (float) DoubleKurtosisSize
    ##   the double kurtosis size   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return float
    @property
    def DoubleKurtosisSize(self) -> float:
        """
        Getter for property: (float) DoubleKurtosisSize
          the double kurtosis size   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleKurtosisSize

    ##   the double kurtosis size   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @DoubleKurtosisSize.setter
    def DoubleKurtosisSize(self, doubleKurtosisSize: float):
        """
        Setter for property: (float) DoubleKurtosisSize
          the double kurtosis size   
            
         
        """
        pass
    
    ## Getter for property: (float) DoubleSkewnessForm
    ##   the double skewness form   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return float
    @property
    def DoubleSkewnessForm(self) -> float:
        """
        Getter for property: (float) DoubleSkewnessForm
          the double skewness form   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleSkewnessForm

    ##   the double skewness form   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @DoubleSkewnessForm.setter
    def DoubleSkewnessForm(self, doubleSkewnessForm: float):
        """
        Setter for property: (float) DoubleSkewnessForm
          the double skewness form   
            
         
        """
        pass
    
    ## Getter for property: (float) DoubleSkewnessLoc
    ##   the double skewness loc   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return float
    @property
    def DoubleSkewnessLoc(self) -> float:
        """
        Getter for property: (float) DoubleSkewnessLoc
          the double skewness loc   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleSkewnessLoc

    ##   the double skewness loc   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @DoubleSkewnessLoc.setter
    def DoubleSkewnessLoc(self, doubleSkewnessLoc: float):
        """
        Setter for property: (float) DoubleSkewnessLoc
          the double skewness loc   
            
         
        """
        pass
    
    ## Getter for property: (float) DoubleSkewnessSize
    ##   the double skewness size   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return float
    @property
    def DoubleSkewnessSize(self) -> float:
        """
        Getter for property: (float) DoubleSkewnessSize
          the double skewness size   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleSkewnessSize

    ##   the double skewness size   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @DoubleSkewnessSize.setter
    def DoubleSkewnessSize(self, doubleSkewnessSize: float):
        """
        Setter for property: (float) DoubleSkewnessSize
          the double skewness size   
            
         
        """
        pass
    
    ## Getter for property: (@link BallFeatureBuilder.APIEnumForm NXOpen.Vsa.BallFeatureBuilder.APIEnumForm@endlink) EnumForm
    ##   the enum form   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return BallFeatureBuilder.APIEnumForm
    @property
    def EnumForm(self) -> BallFeatureBuilder.APIEnumForm:
        """
        Getter for property: (@link BallFeatureBuilder.APIEnumForm NXOpen.Vsa.BallFeatureBuilder.APIEnumForm@endlink) EnumForm
          the enum form   
            
         
        """
        pass
    
    ## Setter for property: (@link BallFeatureBuilder.APIEnumForm NXOpen.Vsa.BallFeatureBuilder.APIEnumForm@endlink) EnumForm

    ##   the enum form   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @EnumForm.setter
    def EnumForm(self, enumForm: BallFeatureBuilder.APIEnumForm):
        """
        Setter for property: (@link BallFeatureBuilder.APIEnumForm NXOpen.Vsa.BallFeatureBuilder.APIEnumForm@endlink) EnumForm
          the enum form   
            
         
        """
        pass
    
    ## Getter for property: (@link BallFeatureBuilder.APIEnumLoc NXOpen.Vsa.BallFeatureBuilder.APIEnumLoc@endlink) EnumLoc
    ##   the enum loc   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return BallFeatureBuilder.APIEnumLoc
    @property
    def EnumLoc(self) -> BallFeatureBuilder.APIEnumLoc:
        """
        Getter for property: (@link BallFeatureBuilder.APIEnumLoc NXOpen.Vsa.BallFeatureBuilder.APIEnumLoc@endlink) EnumLoc
          the enum loc   
            
         
        """
        pass
    
    ## Setter for property: (@link BallFeatureBuilder.APIEnumLoc NXOpen.Vsa.BallFeatureBuilder.APIEnumLoc@endlink) EnumLoc

    ##   the enum loc   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @EnumLoc.setter
    def EnumLoc(self, enumLoc: BallFeatureBuilder.APIEnumLoc):
        """
        Setter for property: (@link BallFeatureBuilder.APIEnumLoc NXOpen.Vsa.BallFeatureBuilder.APIEnumLoc@endlink) EnumLoc
          the enum loc   
            
         
        """
        pass
    
    ## Getter for property: (@link BallFeatureBuilder.APIEnumSize NXOpen.Vsa.BallFeatureBuilder.APIEnumSize@endlink) EnumSize
    ##   the enum size   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return BallFeatureBuilder.APIEnumSize
    @property
    def EnumSize(self) -> BallFeatureBuilder.APIEnumSize:
        """
        Getter for property: (@link BallFeatureBuilder.APIEnumSize NXOpen.Vsa.BallFeatureBuilder.APIEnumSize@endlink) EnumSize
          the enum size   
            
         
        """
        pass
    
    ## Setter for property: (@link BallFeatureBuilder.APIEnumSize NXOpen.Vsa.BallFeatureBuilder.APIEnumSize@endlink) EnumSize

    ##   the enum size   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @EnumSize.setter
    def EnumSize(self, enumSize: BallFeatureBuilder.APIEnumSize):
        """
        Setter for property: (@link BallFeatureBuilder.APIEnumSize NXOpen.Vsa.BallFeatureBuilder.APIEnumSize@endlink) EnumSize
          the enum size   
            
         
        """
        pass
    
    ## Getter for property: (str) StringDescription
    ##   the string description   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return str
    @property
    def StringDescription(self) -> str:
        """
        Getter for property: (str) StringDescription
          the string description   
            
         
        """
        pass
    
    ## Setter for property: (str) StringDescription

    ##   the string description   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @StringDescription.setter
    def StringDescription(self, stringDescription: str):
        """
        Setter for property: (str) StringDescription
          the string description   
            
         
        """
        pass
    
    ## Getter for property: (str) StringName
    ##   the string name   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return str
    @property
    def StringName(self) -> str:
        """
        Getter for property: (str) StringName
          the string name   
            
         
        """
        pass
    
    ## Setter for property: (str) StringName

    ##   the string name   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @StringName.setter
    def StringName(self, stringName: str):
        """
        Setter for property: (str) StringName
          the string name   
            
         
        """
        pass
    
import NXOpen
##  Represents a Ball feature  <br> To create or edit an instance of this class, use @link NXOpen::Vsa::BallFeatureBuilder  NXOpen::Vsa::BallFeatureBuilder @endlink  <br> 
## 
##  <br>  Usable only on Windows <br>  
## 
##   <br>  Created in NX2306.0.0  <br> 

class BallFeature(NXOpen.NXObject): 
    """ Represents a Ball feature """
    pass


import NXOpen
## 
##     
##      <br> To create a new instance of this class, use @link NXOpen::Vsa::VsaManager::CreateDpvinspectionRoutineBuilder  NXOpen::Vsa::VsaManager::CreateDpvinspectionRoutineBuilder @endlink  <br> 
## 
##  <br>  Usable only on Windows <br>  
## 
##   <br>  Created in NX2206.0.0  <br> 

class DPVInspectionRoutineBuilder(NXOpen.Builder): 
    """
    
    """
    pass


import NXOpen
##  Represents a @link NXOpen::Vsa::FixturePlaneFeatureBuilder NXOpen::Vsa::FixturePlaneFeatureBuilder@endlink   <br> To create a new instance of this class, use @link NXOpen::Vsa::VsaManager::CreatePlaneFeatureBuilder  NXOpen::Vsa::VsaManager::CreatePlaneFeatureBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## DoubleKurtosisForm </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleKurtosisLoc </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleKurtosisSize </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleSkewnessForm </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleSkewnessLoc </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleSkewnessSize </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## FormType </term> <description> 
##  
## Normal </description> </item> 
## 
## <item><term> 
##  
## I </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## J </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## K </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## LocType </term> <description> 
##  
## Normal </description> </item> 
## 
## <item><term> 
##  
## SizeType </term> <description> 
##  
## Normal </description> </item> 
## 
## <item><term> 
##  
## X </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## Y </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## Z </term> <description> 
##  
## 0 </description> </item> 
## 
## </list> 

## 
##  <br>  Usable only on Windows <br>  
## 
##   <br>  Created in NX2312.0.0  <br> 

class FixturePlaneFeatureBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>NXOpen.Vsa.FixturePlaneFeatureBuilder</ja_class> """


    ## 
    ##         This enum is for Form distribution type.
    ##         
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Normal</term><description> 
    ## </description> </item><item><term> 
    ## Uniform</term><description> 
    ## </description> </item><item><term> 
    ## Extreme</term><description> 
    ## </description> </item><item><term> 
    ## Pearson</term><description> 
    ## </description> </item><item><term> 
    ## Trapeziodal</term><description> 
    ## </description> </item></list>
    class APIFormType(Enum):
        """
        Members Include: <Normal> <Uniform> <Extreme> <Pearson> <Trapeziodal>
        """
        Normal: int
        Uniform: int
        Extreme: int
        Pearson: int
        Trapeziodal: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> FixturePlaneFeatureBuilder.APIFormType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## 
    ##         This enum is for Location distribution type.
    ##         
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Normal</term><description> 
    ## </description> </item><item><term> 
    ## Uniform</term><description> 
    ## </description> </item><item><term> 
    ## Extreme</term><description> 
    ## </description> </item><item><term> 
    ## Pearson</term><description> 
    ## </description> </item><item><term> 
    ## Trapeziodal</term><description> 
    ## </description> </item></list>
    class APILocType(Enum):
        """
        Members Include: <Normal> <Uniform> <Extreme> <Pearson> <Trapeziodal>
        """
        Normal: int
        Uniform: int
        Extreme: int
        Pearson: int
        Trapeziodal: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> FixturePlaneFeatureBuilder.APILocType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## 
    ##          This enum is for Size distribution type.
    ##         
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Normal</term><description> 
    ## </description> </item><item><term> 
    ## Uniform</term><description> 
    ## </description> </item><item><term> 
    ## Extreme</term><description> 
    ## </description> </item><item><term> 
    ## Pearson</term><description> 
    ## </description> </item><item><term> 
    ## Trapeziodal</term><description> 
    ## </description> </item></list>
    class APISizeType(Enum):
        """
        Members Include: <Normal> <Uniform> <Extreme> <Pearson> <Trapeziodal>
        """
        Normal: int
        Uniform: int
        Extreme: int
        Pearson: int
        Trapeziodal: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> FixturePlaneFeatureBuilder.APISizeType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (str) Description
    ##   the string description   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return str
    @property
    def Description(self) -> str:
        """
        Getter for property: (str) Description
          the string description   
            
         
        """
        pass
    
    ## Setter for property: (str) Description

    ##   the string description   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @Description.setter
    def Description(self, stringDescription: str):
        """
        Setter for property: (str) Description
          the string description   
            
         
        """
        pass
    
    ## Getter for property: (float) DoubleKurtosisForm
    ##   the double kurtosis form   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return float
    @property
    def DoubleKurtosisForm(self) -> float:
        """
        Getter for property: (float) DoubleKurtosisForm
          the double kurtosis form   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleKurtosisForm

    ##   the double kurtosis form   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @DoubleKurtosisForm.setter
    def DoubleKurtosisForm(self, doubleKurtosisForm: float):
        """
        Setter for property: (float) DoubleKurtosisForm
          the double kurtosis form   
            
         
        """
        pass
    
    ## Getter for property: (float) DoubleKurtosisLoc
    ##   the double kurtosis loc   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return float
    @property
    def DoubleKurtosisLoc(self) -> float:
        """
        Getter for property: (float) DoubleKurtosisLoc
          the double kurtosis loc   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleKurtosisLoc

    ##   the double kurtosis loc   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @DoubleKurtosisLoc.setter
    def DoubleKurtosisLoc(self, doubleKurtosisLoc: float):
        """
        Setter for property: (float) DoubleKurtosisLoc
          the double kurtosis loc   
            
         
        """
        pass
    
    ## Getter for property: (float) DoubleKurtosisSize
    ##   the double kurtosis size   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return float
    @property
    def DoubleKurtosisSize(self) -> float:
        """
        Getter for property: (float) DoubleKurtosisSize
          the double kurtosis size   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleKurtosisSize

    ##   the double kurtosis size   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @DoubleKurtosisSize.setter
    def DoubleKurtosisSize(self, doubleKurtosisSize: float):
        """
        Setter for property: (float) DoubleKurtosisSize
          the double kurtosis size   
            
         
        """
        pass
    
    ## Getter for property: (float) DoubleSkewnessForm
    ##   the double skewness form   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return float
    @property
    def DoubleSkewnessForm(self) -> float:
        """
        Getter for property: (float) DoubleSkewnessForm
          the double skewness form   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleSkewnessForm

    ##   the double skewness form   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @DoubleSkewnessForm.setter
    def DoubleSkewnessForm(self, doubleSkewnessForm: float):
        """
        Setter for property: (float) DoubleSkewnessForm
          the double skewness form   
            
         
        """
        pass
    
    ## Getter for property: (float) DoubleSkewnessLoc
    ##   the double skewness loc   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return float
    @property
    def DoubleSkewnessLoc(self) -> float:
        """
        Getter for property: (float) DoubleSkewnessLoc
          the double skewness loc   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleSkewnessLoc

    ##   the double skewness loc   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @DoubleSkewnessLoc.setter
    def DoubleSkewnessLoc(self, doubleSkewnessLoc: float):
        """
        Setter for property: (float) DoubleSkewnessLoc
          the double skewness loc   
            
         
        """
        pass
    
    ## Getter for property: (float) DoubleSkewnessSize
    ##   the double skewness size   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return float
    @property
    def DoubleSkewnessSize(self) -> float:
        """
        Getter for property: (float) DoubleSkewnessSize
          the double skewness size   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleSkewnessSize

    ##   the double skewness size   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @DoubleSkewnessSize.setter
    def DoubleSkewnessSize(self, doubleSkewnessSize: float):
        """
        Setter for property: (float) DoubleSkewnessSize
          the double skewness size   
            
         
        """
        pass
    
    ## Getter for property: (@link FixturePlaneFeatureBuilder.APIFormType NXOpen.Vsa.FixturePlaneFeatureBuilder.APIFormType@endlink) FormType
    ##   the enum form   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return FixturePlaneFeatureBuilder.APIFormType
    @property
    def FormType(self) -> FixturePlaneFeatureBuilder.APIFormType:
        """
        Getter for property: (@link FixturePlaneFeatureBuilder.APIFormType NXOpen.Vsa.FixturePlaneFeatureBuilder.APIFormType@endlink) FormType
          the enum form   
            
         
        """
        pass
    
    ## Setter for property: (@link FixturePlaneFeatureBuilder.APIFormType NXOpen.Vsa.FixturePlaneFeatureBuilder.APIFormType@endlink) FormType

    ##   the enum form   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @FormType.setter
    def FormType(self, formType: FixturePlaneFeatureBuilder.APIFormType):
        """
        Setter for property: (@link FixturePlaneFeatureBuilder.APIFormType NXOpen.Vsa.FixturePlaneFeatureBuilder.APIFormType@endlink) FormType
          the enum form   
            
         
        """
        pass
    
    ## Getter for property: (float) I
    ##   the i   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return float
    @property
    def I(self) -> float:
        """
        Getter for property: (float) I
          the i   
            
         
        """
        pass
    
    ## Setter for property: (float) I

    ##   the i   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @I.setter
    def I(self, i: float):
        """
        Setter for property: (float) I
          the i   
            
         
        """
        pass
    
    ## Getter for property: (float) ILength
    ##   the length vector I  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return float
    @property
    def ILength(self) -> float:
        """
        Getter for property: (float) ILength
          the length vector I  
            
         
        """
        pass
    
    ## Setter for property: (float) ILength

    ##   the length vector I  
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @ILength.setter
    def ILength(self, vectorI: float):
        """
        Setter for property: (float) ILength
          the length vector I  
            
         
        """
        pass
    
    ## Getter for property: (float) J
    ##   the j   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return float
    @property
    def J(self) -> float:
        """
        Getter for property: (float) J
          the j   
            
         
        """
        pass
    
    ## Setter for property: (float) J

    ##   the j   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @J.setter
    def J(self, j: float):
        """
        Setter for property: (float) J
          the j   
            
         
        """
        pass
    
    ## Getter for property: (float) JLength
    ##   the length vector J  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return float
    @property
    def JLength(self) -> float:
        """
        Getter for property: (float) JLength
          the length vector J  
            
         
        """
        pass
    
    ## Setter for property: (float) JLength

    ##   the length vector J  
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @JLength.setter
    def JLength(self, vectorJ: float):
        """
        Setter for property: (float) JLength
          the length vector J  
            
         
        """
        pass
    
    ## Getter for property: (float) K
    ##   the k   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return float
    @property
    def K(self) -> float:
        """
        Getter for property: (float) K
          the k   
            
         
        """
        pass
    
    ## Setter for property: (float) K

    ##   the k   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @K.setter
    def K(self, k: float):
        """
        Setter for property: (float) K
          the k   
            
         
        """
        pass
    
    ## Getter for property: (float) KLength
    ##   the length vector K  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return float
    @property
    def KLength(self) -> float:
        """
        Getter for property: (float) KLength
          the length vector K  
            
         
        """
        pass
    
    ## Setter for property: (float) KLength

    ##   the length vector K  
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @KLength.setter
    def KLength(self, vectorK: float):
        """
        Setter for property: (float) KLength
          the length vector K  
            
         
        """
        pass
    
    ## Getter for property: (float) Length
    ##   the length Length  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return float
    @property
    def Length(self) -> float:
        """
        Getter for property: (float) Length
          the length Length  
            
         
        """
        pass
    
    ## Setter for property: (float) Length

    ##   the length Length  
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @Length.setter
    def Length(self, length: float):
        """
        Setter for property: (float) Length
          the length Length  
            
         
        """
        pass
    
    ## Getter for property: (@link FixturePlaneFeatureBuilder.APILocType NXOpen.Vsa.FixturePlaneFeatureBuilder.APILocType@endlink) LocType
    ##   the enum loc   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return FixturePlaneFeatureBuilder.APILocType
    @property
    def LocType(self) -> FixturePlaneFeatureBuilder.APILocType:
        """
        Getter for property: (@link FixturePlaneFeatureBuilder.APILocType NXOpen.Vsa.FixturePlaneFeatureBuilder.APILocType@endlink) LocType
          the enum loc   
            
         
        """
        pass
    
    ## Setter for property: (@link FixturePlaneFeatureBuilder.APILocType NXOpen.Vsa.FixturePlaneFeatureBuilder.APILocType@endlink) LocType

    ##   the enum loc   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @LocType.setter
    def LocType(self, locType: FixturePlaneFeatureBuilder.APILocType):
        """
        Setter for property: (@link FixturePlaneFeatureBuilder.APILocType NXOpen.Vsa.FixturePlaneFeatureBuilder.APILocType@endlink) LocType
          the enum loc   
            
         
        """
        pass
    
    ## Getter for property: (str) Name
    ##   the name   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

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
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
          the name   
            
         
        """
        pass
    
    ## Getter for property: (@link FixturePlaneFeatureBuilder.APISizeType NXOpen.Vsa.FixturePlaneFeatureBuilder.APISizeType@endlink) SizeType
    ##   the enum size   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return FixturePlaneFeatureBuilder.APISizeType
    @property
    def SizeType(self) -> FixturePlaneFeatureBuilder.APISizeType:
        """
        Getter for property: (@link FixturePlaneFeatureBuilder.APISizeType NXOpen.Vsa.FixturePlaneFeatureBuilder.APISizeType@endlink) SizeType
          the enum size   
            
         
        """
        pass
    
    ## Setter for property: (@link FixturePlaneFeatureBuilder.APISizeType NXOpen.Vsa.FixturePlaneFeatureBuilder.APISizeType@endlink) SizeType

    ##   the enum size   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @SizeType.setter
    def SizeType(self, sizeType: FixturePlaneFeatureBuilder.APISizeType):
        """
        Setter for property: (@link FixturePlaneFeatureBuilder.APISizeType NXOpen.Vsa.FixturePlaneFeatureBuilder.APISizeType@endlink) SizeType
          the enum size   
            
         
        """
        pass
    
    ## Getter for property: (float) Width
    ##   the length Width  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return float
    @property
    def Width(self) -> float:
        """
        Getter for property: (float) Width
          the length Width  
            
         
        """
        pass
    
    ## Setter for property: (float) Width

    ##   the length Width  
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @Width.setter
    def Width(self, width: float):
        """
        Setter for property: (float) Width
          the length Width  
            
         
        """
        pass
    
    ## Getter for property: (float) X
    ##   the x   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return float
    @property
    def X(self) -> float:
        """
        Getter for property: (float) X
          the x   
            
         
        """
        pass
    
    ## Setter for property: (float) X

    ##   the x   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @X.setter
    def X(self, x: float):
        """
        Setter for property: (float) X
          the x   
            
         
        """
        pass
    
    ## Getter for property: (float) Y
    ##   the y   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return float
    @property
    def Y(self) -> float:
        """
        Getter for property: (float) Y
          the y   
            
         
        """
        pass
    
    ## Setter for property: (float) Y

    ##   the y   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @Y.setter
    def Y(self, y: float):
        """
        Setter for property: (float) Y
          the y   
            
         
        """
        pass
    
    ## Getter for property: (float) Z
    ##   the z   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return float
    @property
    def Z(self) -> float:
        """
        Getter for property: (float) Z
          the z   
            
         
        """
        pass
    
    ## Setter for property: (float) Z

    ##   the z   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @Z.setter
    def Z(self, z: float):
        """
        Setter for property: (float) Z
          the z   
            
         
        """
        pass
    
import NXOpen
##  Represents a Fixture Plane Feature  <br> To create or edit an instance of this class, use @link NXOpen::Vsa::FixturePlaneFeatureBuilder  NXOpen::Vsa::FixturePlaneFeatureBuilder @endlink  <br> 
## 
##   <br>  Created in NX2312.0.0  <br> 

class FixturePlaneFeature(NXOpen.Object): 
    """ Represents a Fixture Plane Feature """
    pass


import NXOpen
## 
##     
##      <br> To create a new instance of this class, use @link NXOpen::Vsa::VsaManager::CreateGdtmeasurementOperationBuilder  NXOpen::Vsa::VsaManager::CreateGdtmeasurementOperationBuilder @endlink  <br> 
## 
##  <br>  Usable only on Windows <br>  
## 
##   <br>  Created in NX1980.0.0  <br> 

class GDTMeasurementOperationBuilder(NXOpen.Builder): 
    """
    
    """


    ## 
    ##         
    ##         
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Short</term><description> 
    ## </description> </item><item><term> 
    ## Long</term><description> 
    ## </description> </item></list>
    class APIEnumNameFormat(Enum):
        """
        Members Include: <Short> <Long>
        """
        Short: int
        Long: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> GDTMeasurementOperationBuilder.APIEnumNameFormat:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## 
    ##         
    ##         
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Position</term><description> 
    ## </description> </item><item><term> 
    ## Profile</term><description> 
    ## </description> </item><item><term> 
    ## Angularity</term><description> 
    ## </description> </item><item><term> 
    ## Flatness</term><description> 
    ## </description> </item></list>
    class APIGeometricChar(Enum):
        """
        Members Include: <Position> <Profile> <Angularity> <Flatness>
        """
        Position: int
        Profile: int
        Angularity: int
        Flatness: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> GDTMeasurementOperationBuilder.APIGeometricChar:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link GDTMeasurementOperationBuilder.APIEnumNameFormat NXOpen.Vsa.GDTMeasurementOperationBuilder.APIEnumNameFormat@endlink) EnumNameFormat
    ##   the Name Format   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return GDTMeasurementOperationBuilder.APIEnumNameFormat
    @property
    def EnumNameFormat(self) -> GDTMeasurementOperationBuilder.APIEnumNameFormat:
        """
        Getter for property: (@link GDTMeasurementOperationBuilder.APIEnumNameFormat NXOpen.Vsa.GDTMeasurementOperationBuilder.APIEnumNameFormat@endlink) EnumNameFormat
          the Name Format   
            
         
        """
        pass
    
    ## Setter for property: (@link GDTMeasurementOperationBuilder.APIEnumNameFormat NXOpen.Vsa.GDTMeasurementOperationBuilder.APIEnumNameFormat@endlink) EnumNameFormat

    ##   the Name Format   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @EnumNameFormat.setter
    def EnumNameFormat(self, nameFormat: GDTMeasurementOperationBuilder.APIEnumNameFormat):
        """
        Setter for property: (@link GDTMeasurementOperationBuilder.APIEnumNameFormat NXOpen.Vsa.GDTMeasurementOperationBuilder.APIEnumNameFormat@endlink) EnumNameFormat
          the Name Format   
            
         
        """
        pass
    
    ## Getter for property: (@link GDTMeasurementOperationBuilder.APIGeometricChar NXOpen.Vsa.GDTMeasurementOperationBuilder.APIGeometricChar@endlink) GeaomCharacteristic
    ##   the geom characteristic   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return GDTMeasurementOperationBuilder.APIGeometricChar
    @property
    def GeaomCharacteristic(self) -> GDTMeasurementOperationBuilder.APIGeometricChar:
        """
        Getter for property: (@link GDTMeasurementOperationBuilder.APIGeometricChar NXOpen.Vsa.GDTMeasurementOperationBuilder.APIGeometricChar@endlink) GeaomCharacteristic
          the geom characteristic   
            
         
        """
        pass
    
    ## Setter for property: (@link GDTMeasurementOperationBuilder.APIGeometricChar NXOpen.Vsa.GDTMeasurementOperationBuilder.APIGeometricChar@endlink) GeaomCharacteristic

    ##   the geom characteristic   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @GeaomCharacteristic.setter
    def GeaomCharacteristic(self, geomChar: GDTMeasurementOperationBuilder.APIGeometricChar):
        """
        Setter for property: (@link GDTMeasurementOperationBuilder.APIGeometricChar NXOpen.Vsa.GDTMeasurementOperationBuilder.APIGeometricChar@endlink) GeaomCharacteristic
          the geom characteristic   
            
         
        """
        pass
    
    ## Getter for property: (float) MeasurementZoneLimit
    ##   the MeasurementZoneLimit   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return float
    @property
    def MeasurementZoneLimit(self) -> float:
        """
        Getter for property: (float) MeasurementZoneLimit
          the MeasurementZoneLimit   
            
         
        """
        pass
    
    ## Setter for property: (float) MeasurementZoneLimit

    ##   the MeasurementZoneLimit   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @MeasurementZoneLimit.setter
    def MeasurementZoneLimit(self, measurementZoneLimit: float):
        """
        Setter for property: (float) MeasurementZoneLimit
          the MeasurementZoneLimit   
            
         
        """
        pass
    
    ## Getter for property: (str) StrDescription
    ##   the str description   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return str
    @property
    def StrDescription(self) -> str:
        """
        Getter for property: (str) StrDescription
          the str description   
            
         
        """
        pass
    
    ## Setter for property: (str) StrDescription

    ##   the str description   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @StrDescription.setter
    def StrDescription(self, strDescription: str):
        """
        Setter for property: (str) StrDescription
          the str description   
            
         
        """
        pass
    
    ## Getter for property: (str) StrName
    ##   the str name   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return str
    @property
    def StrName(self) -> str:
        """
        Getter for property: (str) StrName
          the str name   
            
         
        """
        pass
    
    ## Setter for property: (str) StrName

    ##   the str name   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @StrName.setter
    def StrName(self, strName: str):
        """
        Setter for property: (str) StrName
          the str name   
            
         
        """
        pass
    
    ##  The measured feature 
    ##  @return feature (@link NXOpen.NXObject NXOpen.NXObject@endlink): .
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: nx_vsa_build (" Building VSA model")
    @staticmethod
    def GetMeasuredFeature(builder: GDTMeasurementOperationBuilder) -> NXOpen.NXObject:
        """
         The measured feature 
         @return feature (@link NXOpen.NXObject NXOpen.NXObject@endlink): .
        """
        pass
    
    ##  The primary datum feature 
    ##  @return feature (@link NXOpen.NXObject NXOpen.NXObject@endlink): .
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ## <param name="index"> (int) </param>
    def GetPrimaryDatumFeatureItem(builder: GDTMeasurementOperationBuilder, index: int) -> NXOpen.NXObject:
        """
         The primary datum feature 
         @return feature (@link NXOpen.NXObject NXOpen.NXObject@endlink): .
        """
        pass
    
    ##  The secondary datum feature 
    ##  @return feature (@link NXOpen.NXObject NXOpen.NXObject@endlink): .
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ## <param name="index"> (int) </param>
    def GetSecondaryDatumFeatureItem(builder: GDTMeasurementOperationBuilder, index: int) -> NXOpen.NXObject:
        """
         The secondary datum feature 
         @return feature (@link NXOpen.NXObject NXOpen.NXObject@endlink): .
        """
        pass
    
    ##  The tertiary datum feature 
    ##  @return feature (@link NXOpen.NXObject NXOpen.NXObject@endlink): .
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ## <param name="index"> (int) </param>
    def GetTertiaryDatumFeatureItem(builder: GDTMeasurementOperationBuilder, index: int) -> NXOpen.NXObject:
        """
         The tertiary datum feature 
         @return feature (@link NXOpen.NXObject NXOpen.NXObject@endlink): .
        """
        pass
    
    ##  The Remove Datum Feature 
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="ntype"> (int) </param>
    ## <param name="nIndex"> (int) </param>
    def RemoveDatumFeature(builder: GDTMeasurementOperationBuilder, ntype: int, nIndex: int) -> None:
        """
         The Remove Datum Feature 
        """
        pass
    
    ##  The measured feature 
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ## <param name="feature"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    def SetMeasuredFeature(builder: GDTMeasurementOperationBuilder, feature: NXOpen.NXObject) -> None:
        """
         The measured feature 
        """
        pass
    
    ##  The primary datum feature 
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ## <param name="index"> (int) </param>
    ## <param name="feature"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    def SetPrimaryDatumFeatureItem(builder: GDTMeasurementOperationBuilder, index: int, feature: NXOpen.NXObject) -> None:
        """
         The primary datum feature 
        """
        pass
    
    ##  The secondary datum feature 
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ## <param name="index"> (int) </param>
    ## <param name="feature"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    def SetSecondaryDatumFeatureItem(builder: GDTMeasurementOperationBuilder, index: int, feature: NXOpen.NXObject) -> None:
        """
         The secondary datum feature 
        """
        pass
    
    ##  The tertiary datum feature 
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ## <param name="index"> (int) </param>
    ## <param name="feature"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    def SetTertiaryDatumFeatureItem(builder: GDTMeasurementOperationBuilder, index: int, feature: NXOpen.NXObject) -> None:
        """
         The tertiary datum feature 
        """
        pass
    
    ##  The swap the existing  Datum Feature 
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="ntype"> (int) </param>
    ## <param name="nIndex1"> (int) </param>
    ## <param name="nIndex2"> (int) </param>
    def SwapDatumFeature(builder: GDTMeasurementOperationBuilder, ntype: int, nIndex1: int, nIndex2: int) -> None:
        """
         The swap the existing  Datum Feature 
        """
        pass
    
import NXOpen
## 
##     
##      <br> To create a new instance of this class, use @link NXOpen::Vsa::VsaManager::CreateGeneralSurfaceFeatureBuilder  NXOpen::Vsa::VsaManager::CreateGeneralSurfaceFeatureBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## DoubleKurtosisForm </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleKurtosisLoc </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleKurtosisSize </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleSkewnessForm </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleSkewnessLoc </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleSkewnessSize </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## EnumForm </term> <description> 
##  
## Normal </description> </item> 
## 
## <item><term> 
##  
## EnumLoc </term> <description> 
##  
## Normal </description> </item> 
## 
## <item><term> 
##  
## EnumSize </term> <description> 
##  
## Normal </description> </item> 
## 
## </list> 

## 
##  <br>  Usable only on Windows <br>  
## 
##   <br>  Created in NX1926.0.0  <br> 

class GeneralSurfaceFeatureBuilder(NXOpen.Builder): 
    """
    
    """


    ## 
    ##         This enum is for Form distribution type.
    ##         
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Normal</term><description> 
    ## </description> </item><item><term> 
    ## Uniform</term><description> 
    ## </description> </item><item><term> 
    ## Extreme</term><description> 
    ## </description> </item><item><term> 
    ## Pearson</term><description> 
    ## </description> </item><item><term> 
    ## Trapeziodal</term><description> 
    ## </description> </item></list>
    class APIEnumForm(Enum):
        """
        Members Include: <Normal> <Uniform> <Extreme> <Pearson> <Trapeziodal>
        """
        Normal: int
        Uniform: int
        Extreme: int
        Pearson: int
        Trapeziodal: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> GeneralSurfaceFeatureBuilder.APIEnumForm:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## 
    ##         This enum is for Location distribution type.
    ##         
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Normal</term><description> 
    ## </description> </item><item><term> 
    ## Uniform</term><description> 
    ## </description> </item><item><term> 
    ## Extreme</term><description> 
    ## </description> </item><item><term> 
    ## Pearson</term><description> 
    ## </description> </item><item><term> 
    ## Trapeziodal</term><description> 
    ## </description> </item></list>
    class APIEnumLoc(Enum):
        """
        Members Include: <Normal> <Uniform> <Extreme> <Pearson> <Trapeziodal>
        """
        Normal: int
        Uniform: int
        Extreme: int
        Pearson: int
        Trapeziodal: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> GeneralSurfaceFeatureBuilder.APIEnumLoc:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## 
    ##          This enum is for Size distribution type.
    ##         
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Normal</term><description> 
    ## </description> </item><item><term> 
    ## Uniform</term><description> 
    ## </description> </item><item><term> 
    ## Extreme</term><description> 
    ## </description> </item><item><term> 
    ## Pearson</term><description> 
    ## </description> </item><item><term> 
    ## Trapeziodal</term><description> 
    ## </description> </item></list>
    class APIEnumSize(Enum):
        """
        Members Include: <Normal> <Uniform> <Extreme> <Pearson> <Trapeziodal>
        """
        Normal: int
        Uniform: int
        Extreme: int
        Pearson: int
        Trapeziodal: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> GeneralSurfaceFeatureBuilder.APIEnumSize:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (str) Description
    ##   the string description   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return str
    @property
    def Description(self) -> str:
        """
        Getter for property: (str) Description
          the string description   
            
         
        """
        pass
    
    ## Setter for property: (str) Description

    ##   the string description   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @Description.setter
    def Description(self, stringDescription: str):
        """
        Setter for property: (str) Description
          the string description   
            
         
        """
        pass
    
    ## Getter for property: (float) DoubleKurtosisForm
    ##   the double kurtosis form   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def DoubleKurtosisForm(self) -> float:
        """
        Getter for property: (float) DoubleKurtosisForm
          the double kurtosis form   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleKurtosisForm

    ##   the double kurtosis form   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @DoubleKurtosisForm.setter
    def DoubleKurtosisForm(self, doubleKurtosisForm: float):
        """
        Setter for property: (float) DoubleKurtosisForm
          the double kurtosis form   
            
         
        """
        pass
    
    ## Getter for property: (float) DoubleKurtosisLoc
    ##   the double kurtosis loc   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def DoubleKurtosisLoc(self) -> float:
        """
        Getter for property: (float) DoubleKurtosisLoc
          the double kurtosis loc   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleKurtosisLoc

    ##   the double kurtosis loc   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @DoubleKurtosisLoc.setter
    def DoubleKurtosisLoc(self, doubleKurtosisLoc: float):
        """
        Setter for property: (float) DoubleKurtosisLoc
          the double kurtosis loc   
            
         
        """
        pass
    
    ## Getter for property: (float) DoubleKurtosisSize
    ##   the double kurtosis size   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def DoubleKurtosisSize(self) -> float:
        """
        Getter for property: (float) DoubleKurtosisSize
          the double kurtosis size   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleKurtosisSize

    ##   the double kurtosis size   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @DoubleKurtosisSize.setter
    def DoubleKurtosisSize(self, doubleKurtosisSize: float):
        """
        Setter for property: (float) DoubleKurtosisSize
          the double kurtosis size   
            
         
        """
        pass
    
    ## Getter for property: (float) DoubleSkewnessForm
    ##   the double skewness form   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def DoubleSkewnessForm(self) -> float:
        """
        Getter for property: (float) DoubleSkewnessForm
          the double skewness form   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleSkewnessForm

    ##   the double skewness form   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @DoubleSkewnessForm.setter
    def DoubleSkewnessForm(self, doubleSkewnessForm: float):
        """
        Setter for property: (float) DoubleSkewnessForm
          the double skewness form   
            
         
        """
        pass
    
    ## Getter for property: (float) DoubleSkewnessLoc
    ##   the double skewness loc   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def DoubleSkewnessLoc(self) -> float:
        """
        Getter for property: (float) DoubleSkewnessLoc
          the double skewness loc   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleSkewnessLoc

    ##   the double skewness loc   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @DoubleSkewnessLoc.setter
    def DoubleSkewnessLoc(self, doubleSkewnessLoc: float):
        """
        Setter for property: (float) DoubleSkewnessLoc
          the double skewness loc   
            
         
        """
        pass
    
    ## Getter for property: (float) DoubleSkewnessSize
    ##   the double skewness size   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def DoubleSkewnessSize(self) -> float:
        """
        Getter for property: (float) DoubleSkewnessSize
          the double skewness size   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleSkewnessSize

    ##   the double skewness size   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @DoubleSkewnessSize.setter
    def DoubleSkewnessSize(self, doubleSkewnessSize: float):
        """
        Setter for property: (float) DoubleSkewnessSize
          the double skewness size   
            
         
        """
        pass
    
    ## Getter for property: (@link GeneralSurfaceFeatureBuilder.APIEnumForm NXOpen.Vsa.GeneralSurfaceFeatureBuilder.APIEnumForm@endlink) EnumForm
    ##   the enum form   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return GeneralSurfaceFeatureBuilder.APIEnumForm
    @property
    def EnumForm(self) -> GeneralSurfaceFeatureBuilder.APIEnumForm:
        """
        Getter for property: (@link GeneralSurfaceFeatureBuilder.APIEnumForm NXOpen.Vsa.GeneralSurfaceFeatureBuilder.APIEnumForm@endlink) EnumForm
          the enum form   
            
         
        """
        pass
    
    ## Setter for property: (@link GeneralSurfaceFeatureBuilder.APIEnumForm NXOpen.Vsa.GeneralSurfaceFeatureBuilder.APIEnumForm@endlink) EnumForm

    ##   the enum form   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @EnumForm.setter
    def EnumForm(self, enumForm: GeneralSurfaceFeatureBuilder.APIEnumForm):
        """
        Setter for property: (@link GeneralSurfaceFeatureBuilder.APIEnumForm NXOpen.Vsa.GeneralSurfaceFeatureBuilder.APIEnumForm@endlink) EnumForm
          the enum form   
            
         
        """
        pass
    
    ## Getter for property: (@link GeneralSurfaceFeatureBuilder.APIEnumLoc NXOpen.Vsa.GeneralSurfaceFeatureBuilder.APIEnumLoc@endlink) EnumLoc
    ##   the enum loc   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return GeneralSurfaceFeatureBuilder.APIEnumLoc
    @property
    def EnumLoc(self) -> GeneralSurfaceFeatureBuilder.APIEnumLoc:
        """
        Getter for property: (@link GeneralSurfaceFeatureBuilder.APIEnumLoc NXOpen.Vsa.GeneralSurfaceFeatureBuilder.APIEnumLoc@endlink) EnumLoc
          the enum loc   
            
         
        """
        pass
    
    ## Setter for property: (@link GeneralSurfaceFeatureBuilder.APIEnumLoc NXOpen.Vsa.GeneralSurfaceFeatureBuilder.APIEnumLoc@endlink) EnumLoc

    ##   the enum loc   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @EnumLoc.setter
    def EnumLoc(self, enumLoc: GeneralSurfaceFeatureBuilder.APIEnumLoc):
        """
        Setter for property: (@link GeneralSurfaceFeatureBuilder.APIEnumLoc NXOpen.Vsa.GeneralSurfaceFeatureBuilder.APIEnumLoc@endlink) EnumLoc
          the enum loc   
            
         
        """
        pass
    
    ## Getter for property: (@link GeneralSurfaceFeatureBuilder.APIEnumSize NXOpen.Vsa.GeneralSurfaceFeatureBuilder.APIEnumSize@endlink) EnumSize
    ##   the enum size   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return GeneralSurfaceFeatureBuilder.APIEnumSize
    @property
    def EnumSize(self) -> GeneralSurfaceFeatureBuilder.APIEnumSize:
        """
        Getter for property: (@link GeneralSurfaceFeatureBuilder.APIEnumSize NXOpen.Vsa.GeneralSurfaceFeatureBuilder.APIEnumSize@endlink) EnumSize
          the enum size   
            
         
        """
        pass
    
    ## Setter for property: (@link GeneralSurfaceFeatureBuilder.APIEnumSize NXOpen.Vsa.GeneralSurfaceFeatureBuilder.APIEnumSize@endlink) EnumSize

    ##   the enum size   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @EnumSize.setter
    def EnumSize(self, enumSize: GeneralSurfaceFeatureBuilder.APIEnumSize):
        """
        Setter for property: (@link GeneralSurfaceFeatureBuilder.APIEnumSize NXOpen.Vsa.GeneralSurfaceFeatureBuilder.APIEnumSize@endlink) EnumSize
          the enum size   
            
         
        """
        pass
    
    ## Getter for property: (str) Name
    ##   the name   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

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
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
          the name   
            
         
        """
        pass
    
import NXOpen
## 
##     
##      <br> To create a new instance of this class, use @link NXOpen::Vsa::VsaManager::CreateHoleFeatureBuilder  NXOpen::Vsa::VsaManager::CreateHoleFeatureBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## DoubleAnchorX </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleAnchorY </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleAnchorZ </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleDiameter1 </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleDiameter2 </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleDirectionI </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleDirectionJ </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleDirectionK </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleHeight </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleKurtosisForm </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleKurtosisLoc </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleKurtosisSize </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleSkewnessForm </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleSkewnessLoc </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleSkewnessSize </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## EnumForm </term> <description> 
##  
## Normal </description> </item> 
## 
## <item><term> 
##  
## EnumLoc </term> <description> 
##  
## Normal </description> </item> 
## 
## <item><term> 
##  
## EnumSize </term> <description> 
##  
## Normal </description> </item> 
## 
## </list> 

## 
##  <br>  Usable only on Windows <br>  
## 
##   <br>  Created in NX1899.0.0  <br> 

class HoleFeatureBuilder(NXOpen.Builder): 
    """
    
    """


    ## 
    ##         
    ##         
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Normal</term><description> 
    ## </description> </item><item><term> 
    ## Uniform</term><description> 
    ## </description> </item><item><term> 
    ## Extreme</term><description> 
    ## </description> </item><item><term> 
    ## Pearson</term><description> 
    ## </description> </item><item><term> 
    ## Trapeziodal</term><description> 
    ## </description> </item></list>
    class APIEnumForm(Enum):
        """
        Members Include: <Normal> <Uniform> <Extreme> <Pearson> <Trapeziodal>
        """
        Normal: int
        Uniform: int
        Extreme: int
        Pearson: int
        Trapeziodal: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> HoleFeatureBuilder.APIEnumForm:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## 
    ##         
    ##         
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Normal</term><description> 
    ## </description> </item><item><term> 
    ## Uniform</term><description> 
    ## </description> </item><item><term> 
    ## Extreme</term><description> 
    ## </description> </item><item><term> 
    ## Pearson</term><description> 
    ## </description> </item><item><term> 
    ## Trapeziodal</term><description> 
    ## </description> </item></list>
    class APIEnumLoc(Enum):
        """
        Members Include: <Normal> <Uniform> <Extreme> <Pearson> <Trapeziodal>
        """
        Normal: int
        Uniform: int
        Extreme: int
        Pearson: int
        Trapeziodal: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> HoleFeatureBuilder.APIEnumLoc:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## 
    ##         
    ##         
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Normal</term><description> 
    ## </description> </item><item><term> 
    ## Uniform</term><description> 
    ## </description> </item><item><term> 
    ## Extreme</term><description> 
    ## </description> </item><item><term> 
    ## Pearson</term><description> 
    ## </description> </item><item><term> 
    ## Trapeziodal</term><description> 
    ## </description> </item></list>
    class APIEnumSize(Enum):
        """
        Members Include: <Normal> <Uniform> <Extreme> <Pearson> <Trapeziodal>
        """
        Normal: int
        Uniform: int
        Extreme: int
        Pearson: int
        Trapeziodal: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> HoleFeatureBuilder.APIEnumSize:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (float) DoubleAnchorX
    ##   the double anchor x   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def DoubleAnchorX(self) -> float:
        """
        Getter for property: (float) DoubleAnchorX
          the double anchor x   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleAnchorX

    ##   the double anchor x   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @DoubleAnchorX.setter
    def DoubleAnchorX(self, doubleAnchorX: float):
        """
        Setter for property: (float) DoubleAnchorX
          the double anchor x   
            
         
        """
        pass
    
    ## Getter for property: (float) DoubleAnchorY
    ##   the double anchor y   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def DoubleAnchorY(self) -> float:
        """
        Getter for property: (float) DoubleAnchorY
          the double anchor y   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleAnchorY

    ##   the double anchor y   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @DoubleAnchorY.setter
    def DoubleAnchorY(self, doubleAnchorY: float):
        """
        Setter for property: (float) DoubleAnchorY
          the double anchor y   
            
         
        """
        pass
    
    ## Getter for property: (float) DoubleAnchorZ
    ##   the double anchor z   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def DoubleAnchorZ(self) -> float:
        """
        Getter for property: (float) DoubleAnchorZ
          the double anchor z   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleAnchorZ

    ##   the double anchor z   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @DoubleAnchorZ.setter
    def DoubleAnchorZ(self, doubleAnchorZ: float):
        """
        Setter for property: (float) DoubleAnchorZ
          the double anchor z   
            
         
        """
        pass
    
    ## Getter for property: (float) DoubleDiameter1
    ##   the double diameter1   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def DoubleDiameter1(self) -> float:
        """
        Getter for property: (float) DoubleDiameter1
          the double diameter1   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleDiameter1

    ##   the double diameter1   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @DoubleDiameter1.setter
    def DoubleDiameter1(self, doubleDiameter1: float):
        """
        Setter for property: (float) DoubleDiameter1
          the double diameter1   
            
         
        """
        pass
    
    ## Getter for property: (float) DoubleDiameter2
    ##   the double diameter2   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def DoubleDiameter2(self) -> float:
        """
        Getter for property: (float) DoubleDiameter2
          the double diameter2   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleDiameter2

    ##   the double diameter2   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @DoubleDiameter2.setter
    def DoubleDiameter2(self, doubleDiameter2: float):
        """
        Setter for property: (float) DoubleDiameter2
          the double diameter2   
            
         
        """
        pass
    
    ## Getter for property: (float) DoubleDirectionI
    ##   the double direction i   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def DoubleDirectionI(self) -> float:
        """
        Getter for property: (float) DoubleDirectionI
          the double direction i   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleDirectionI

    ##   the double direction i   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @DoubleDirectionI.setter
    def DoubleDirectionI(self, doubleDirectionI: float):
        """
        Setter for property: (float) DoubleDirectionI
          the double direction i   
            
         
        """
        pass
    
    ## Getter for property: (float) DoubleDirectionJ
    ##   the double direction j   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def DoubleDirectionJ(self) -> float:
        """
        Getter for property: (float) DoubleDirectionJ
          the double direction j   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleDirectionJ

    ##   the double direction j   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @DoubleDirectionJ.setter
    def DoubleDirectionJ(self, doubleDirectionJ: float):
        """
        Setter for property: (float) DoubleDirectionJ
          the double direction j   
            
         
        """
        pass
    
    ## Getter for property: (float) DoubleDirectionK
    ##   the double direction k   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def DoubleDirectionK(self) -> float:
        """
        Getter for property: (float) DoubleDirectionK
          the double direction k   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleDirectionK

    ##   the double direction k   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @DoubleDirectionK.setter
    def DoubleDirectionK(self, doubleDirectionK: float):
        """
        Setter for property: (float) DoubleDirectionK
          the double direction k   
            
         
        """
        pass
    
    ## Getter for property: (float) DoubleHeight
    ##   the double height   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def DoubleHeight(self) -> float:
        """
        Getter for property: (float) DoubleHeight
          the double height   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleHeight

    ##   the double height   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @DoubleHeight.setter
    def DoubleHeight(self, doubleHeight: float):
        """
        Setter for property: (float) DoubleHeight
          the double height   
            
         
        """
        pass
    
    ## Getter for property: (float) DoubleKurtosisForm
    ##   the double kurtosis form   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def DoubleKurtosisForm(self) -> float:
        """
        Getter for property: (float) DoubleKurtosisForm
          the double kurtosis form   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleKurtosisForm

    ##   the double kurtosis form   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @DoubleKurtosisForm.setter
    def DoubleKurtosisForm(self, doubleKurtosisForm: float):
        """
        Setter for property: (float) DoubleKurtosisForm
          the double kurtosis form   
            
         
        """
        pass
    
    ## Getter for property: (float) DoubleKurtosisLoc
    ##   the double kurtosis loc   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def DoubleKurtosisLoc(self) -> float:
        """
        Getter for property: (float) DoubleKurtosisLoc
          the double kurtosis loc   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleKurtosisLoc

    ##   the double kurtosis loc   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @DoubleKurtosisLoc.setter
    def DoubleKurtosisLoc(self, doubleKurtosisLoc: float):
        """
        Setter for property: (float) DoubleKurtosisLoc
          the double kurtosis loc   
            
         
        """
        pass
    
    ## Getter for property: (float) DoubleKurtosisSize
    ##   the double kurtosis size   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def DoubleKurtosisSize(self) -> float:
        """
        Getter for property: (float) DoubleKurtosisSize
          the double kurtosis size   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleKurtosisSize

    ##   the double kurtosis size   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @DoubleKurtosisSize.setter
    def DoubleKurtosisSize(self, doubleKurtosisSize: float):
        """
        Setter for property: (float) DoubleKurtosisSize
          the double kurtosis size   
            
         
        """
        pass
    
    ## Getter for property: (float) DoubleSkewnessForm
    ##   the double skewness form   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def DoubleSkewnessForm(self) -> float:
        """
        Getter for property: (float) DoubleSkewnessForm
          the double skewness form   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleSkewnessForm

    ##   the double skewness form   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @DoubleSkewnessForm.setter
    def DoubleSkewnessForm(self, doubleSkewnessForm: float):
        """
        Setter for property: (float) DoubleSkewnessForm
          the double skewness form   
            
         
        """
        pass
    
    ## Getter for property: (float) DoubleSkewnessLoc
    ##   the double skewness loc   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def DoubleSkewnessLoc(self) -> float:
        """
        Getter for property: (float) DoubleSkewnessLoc
          the double skewness loc   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleSkewnessLoc

    ##   the double skewness loc   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @DoubleSkewnessLoc.setter
    def DoubleSkewnessLoc(self, doubleSkewnessLoc: float):
        """
        Setter for property: (float) DoubleSkewnessLoc
          the double skewness loc   
            
         
        """
        pass
    
    ## Getter for property: (float) DoubleSkewnessSize
    ##   the double skewness size   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def DoubleSkewnessSize(self) -> float:
        """
        Getter for property: (float) DoubleSkewnessSize
          the double skewness size   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleSkewnessSize

    ##   the double skewness size   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @DoubleSkewnessSize.setter
    def DoubleSkewnessSize(self, doubleSkewnessSize: float):
        """
        Setter for property: (float) DoubleSkewnessSize
          the double skewness size   
            
         
        """
        pass
    
    ## Getter for property: (@link HoleFeatureBuilder.APIEnumForm NXOpen.Vsa.HoleFeatureBuilder.APIEnumForm@endlink) EnumForm
    ##   the enum form   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return HoleFeatureBuilder.APIEnumForm
    @property
    def EnumForm(self) -> HoleFeatureBuilder.APIEnumForm:
        """
        Getter for property: (@link HoleFeatureBuilder.APIEnumForm NXOpen.Vsa.HoleFeatureBuilder.APIEnumForm@endlink) EnumForm
          the enum form   
            
         
        """
        pass
    
    ## Setter for property: (@link HoleFeatureBuilder.APIEnumForm NXOpen.Vsa.HoleFeatureBuilder.APIEnumForm@endlink) EnumForm

    ##   the enum form   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @EnumForm.setter
    def EnumForm(self, enumForm: HoleFeatureBuilder.APIEnumForm):
        """
        Setter for property: (@link HoleFeatureBuilder.APIEnumForm NXOpen.Vsa.HoleFeatureBuilder.APIEnumForm@endlink) EnumForm
          the enum form   
            
         
        """
        pass
    
    ## Getter for property: (@link HoleFeatureBuilder.APIEnumLoc NXOpen.Vsa.HoleFeatureBuilder.APIEnumLoc@endlink) EnumLoc
    ##   the enum loc   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return HoleFeatureBuilder.APIEnumLoc
    @property
    def EnumLoc(self) -> HoleFeatureBuilder.APIEnumLoc:
        """
        Getter for property: (@link HoleFeatureBuilder.APIEnumLoc NXOpen.Vsa.HoleFeatureBuilder.APIEnumLoc@endlink) EnumLoc
          the enum loc   
            
         
        """
        pass
    
    ## Setter for property: (@link HoleFeatureBuilder.APIEnumLoc NXOpen.Vsa.HoleFeatureBuilder.APIEnumLoc@endlink) EnumLoc

    ##   the enum loc   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @EnumLoc.setter
    def EnumLoc(self, enumLoc: HoleFeatureBuilder.APIEnumLoc):
        """
        Setter for property: (@link HoleFeatureBuilder.APIEnumLoc NXOpen.Vsa.HoleFeatureBuilder.APIEnumLoc@endlink) EnumLoc
          the enum loc   
            
         
        """
        pass
    
    ## Getter for property: (@link HoleFeatureBuilder.APIEnumSize NXOpen.Vsa.HoleFeatureBuilder.APIEnumSize@endlink) EnumSize
    ##   the enum size   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return HoleFeatureBuilder.APIEnumSize
    @property
    def EnumSize(self) -> HoleFeatureBuilder.APIEnumSize:
        """
        Getter for property: (@link HoleFeatureBuilder.APIEnumSize NXOpen.Vsa.HoleFeatureBuilder.APIEnumSize@endlink) EnumSize
          the enum size   
            
         
        """
        pass
    
    ## Setter for property: (@link HoleFeatureBuilder.APIEnumSize NXOpen.Vsa.HoleFeatureBuilder.APIEnumSize@endlink) EnumSize

    ##   the enum size   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @EnumSize.setter
    def EnumSize(self, enumSize: HoleFeatureBuilder.APIEnumSize):
        """
        Setter for property: (@link HoleFeatureBuilder.APIEnumSize NXOpen.Vsa.HoleFeatureBuilder.APIEnumSize@endlink) EnumSize
          the enum size   
            
         
        """
        pass
    
    ## Getter for property: (str) StringDescription
    ##   the string description   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return str
    @property
    def StringDescription(self) -> str:
        """
        Getter for property: (str) StringDescription
          the string description   
            
         
        """
        pass
    
    ## Setter for property: (str) StringDescription

    ##   the string description   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @StringDescription.setter
    def StringDescription(self, stringDescription: str):
        """
        Setter for property: (str) StringDescription
          the string description   
            
         
        """
        pass
    
    ## Getter for property: (str) StringName
    ##   the string name   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return str
    @property
    def StringName(self) -> str:
        """
        Getter for property: (str) StringName
          the string name   
            
         
        """
        pass
    
    ## Setter for property: (str) StringName

    ##   the string name   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @StringName.setter
    def StringName(self, stringName: str):
        """
        Setter for property: (str) StringName
          the string name   
            
         
        """
        pass
    
import NXOpen
##  Represents a Hole feature  <br> To create or edit an instance of this class, use @link NXOpen::Vsa::HoleFeatureBuilder  NXOpen::Vsa::HoleFeatureBuilder @endlink  <br> 
## 
##  <br>  Usable only on Windows <br>  
## 
##   <br>  Created in NX1899.0.0  <br> 

class HoleFeature(NXOpen.NXObject): 
    """ Represents a Hole feature """
    pass


import NXOpen
## 
##     
##      <br> To create a new instance of this class, use @link NXOpen::Vsa::VsaManager::CreateHolePatternFeatureBuilder  NXOpen::Vsa::VsaManager::CreateHolePatternFeatureBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## DoubleKurtosisForm </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleKurtosisLoc </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleKurtosisSize </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleSkewnessForm </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleSkewnessLoc </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleSkewnessSize </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## EnumForm </term> <description> 
##  
## Normal </description> </item> 
## 
## <item><term> 
##  
## EnumLoc </term> <description> 
##  
## Normal </description> </item> 
## 
## <item><term> 
##  
## EnumSize </term> <description> 
##  
## Normal </description> </item> 
## 
## </list> 

## 
##  <br>  Usable only on Windows <br>  
## 
##   <br>  Created in NX1899.0.0  <br> 

class HolePatternFeatureBuilder(NXOpen.Builder): 
    """
    
    """


    ## 
    ##         
    ##         
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Normal</term><description> 
    ## </description> </item><item><term> 
    ## Uniform</term><description> 
    ## </description> </item><item><term> 
    ## Extreme</term><description> 
    ## </description> </item><item><term> 
    ## Pearson</term><description> 
    ## </description> </item><item><term> 
    ## Trapeziodal</term><description> 
    ## </description> </item></list>
    class APIEnumForm(Enum):
        """
        Members Include: <Normal> <Uniform> <Extreme> <Pearson> <Trapeziodal>
        """
        Normal: int
        Uniform: int
        Extreme: int
        Pearson: int
        Trapeziodal: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> HolePatternFeatureBuilder.APIEnumForm:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## 
    ##         
    ##         
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Normal</term><description> 
    ## </description> </item><item><term> 
    ## Uniform</term><description> 
    ## </description> </item><item><term> 
    ## Extreme</term><description> 
    ## </description> </item><item><term> 
    ## Pearson</term><description> 
    ## </description> </item><item><term> 
    ## Trapeziodal</term><description> 
    ## </description> </item></list>
    class APIEnumLoc(Enum):
        """
        Members Include: <Normal> <Uniform> <Extreme> <Pearson> <Trapeziodal>
        """
        Normal: int
        Uniform: int
        Extreme: int
        Pearson: int
        Trapeziodal: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> HolePatternFeatureBuilder.APIEnumLoc:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## 
    ##         
    ##         
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Normal</term><description> 
    ## </description> </item><item><term> 
    ## Uniform</term><description> 
    ## </description> </item><item><term> 
    ## Extreme</term><description> 
    ## </description> </item><item><term> 
    ## Pearson</term><description> 
    ## </description> </item><item><term> 
    ## Trapeziodal</term><description> 
    ## </description> </item></list>
    class APIEnumSize(Enum):
        """
        Members Include: <Normal> <Uniform> <Extreme> <Pearson> <Trapeziodal>
        """
        Normal: int
        Uniform: int
        Extreme: int
        Pearson: int
        Trapeziodal: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> HolePatternFeatureBuilder.APIEnumSize:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (float) DoubleKurtosisForm
    ##   the double kurtosis form   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def DoubleKurtosisForm(self) -> float:
        """
        Getter for property: (float) DoubleKurtosisForm
          the double kurtosis form   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleKurtosisForm

    ##   the double kurtosis form   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @DoubleKurtosisForm.setter
    def DoubleKurtosisForm(self, doubleKurtosisForm: float):
        """
        Setter for property: (float) DoubleKurtosisForm
          the double kurtosis form   
            
         
        """
        pass
    
    ## Getter for property: (float) DoubleKurtosisLoc
    ##   the double kurtosis loc   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def DoubleKurtosisLoc(self) -> float:
        """
        Getter for property: (float) DoubleKurtosisLoc
          the double kurtosis loc   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleKurtosisLoc

    ##   the double kurtosis loc   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @DoubleKurtosisLoc.setter
    def DoubleKurtosisLoc(self, doubleKurtosisLoc: float):
        """
        Setter for property: (float) DoubleKurtosisLoc
          the double kurtosis loc   
            
         
        """
        pass
    
    ## Getter for property: (float) DoubleKurtosisSize
    ##   the double kurtosis size   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def DoubleKurtosisSize(self) -> float:
        """
        Getter for property: (float) DoubleKurtosisSize
          the double kurtosis size   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleKurtosisSize

    ##   the double kurtosis size   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @DoubleKurtosisSize.setter
    def DoubleKurtosisSize(self, doubleKurtosisSize: float):
        """
        Setter for property: (float) DoubleKurtosisSize
          the double kurtosis size   
            
         
        """
        pass
    
    ## Getter for property: (float) DoubleSkewnessForm
    ##   the double skewness form   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def DoubleSkewnessForm(self) -> float:
        """
        Getter for property: (float) DoubleSkewnessForm
          the double skewness form   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleSkewnessForm

    ##   the double skewness form   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @DoubleSkewnessForm.setter
    def DoubleSkewnessForm(self, doubleSkewnessForm: float):
        """
        Setter for property: (float) DoubleSkewnessForm
          the double skewness form   
            
         
        """
        pass
    
    ## Getter for property: (float) DoubleSkewnessLoc
    ##   the double skewness loc   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def DoubleSkewnessLoc(self) -> float:
        """
        Getter for property: (float) DoubleSkewnessLoc
          the double skewness loc   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleSkewnessLoc

    ##   the double skewness loc   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @DoubleSkewnessLoc.setter
    def DoubleSkewnessLoc(self, doubleSkewnessLoc: float):
        """
        Setter for property: (float) DoubleSkewnessLoc
          the double skewness loc   
            
         
        """
        pass
    
    ## Getter for property: (float) DoubleSkewnessSize
    ##   the double skewness size   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def DoubleSkewnessSize(self) -> float:
        """
        Getter for property: (float) DoubleSkewnessSize
          the double skewness size   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleSkewnessSize

    ##   the double skewness size   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @DoubleSkewnessSize.setter
    def DoubleSkewnessSize(self, doubleSkewnessSize: float):
        """
        Setter for property: (float) DoubleSkewnessSize
          the double skewness size   
            
         
        """
        pass
    
    ## Getter for property: (@link HolePatternFeatureBuilder.APIEnumForm NXOpen.Vsa.HolePatternFeatureBuilder.APIEnumForm@endlink) EnumForm
    ##   the enum form   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return HolePatternFeatureBuilder.APIEnumForm
    @property
    def EnumForm(self) -> HolePatternFeatureBuilder.APIEnumForm:
        """
        Getter for property: (@link HolePatternFeatureBuilder.APIEnumForm NXOpen.Vsa.HolePatternFeatureBuilder.APIEnumForm@endlink) EnumForm
          the enum form   
            
         
        """
        pass
    
    ## Setter for property: (@link HolePatternFeatureBuilder.APIEnumForm NXOpen.Vsa.HolePatternFeatureBuilder.APIEnumForm@endlink) EnumForm

    ##   the enum form   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @EnumForm.setter
    def EnumForm(self, enumForm: HolePatternFeatureBuilder.APIEnumForm):
        """
        Setter for property: (@link HolePatternFeatureBuilder.APIEnumForm NXOpen.Vsa.HolePatternFeatureBuilder.APIEnumForm@endlink) EnumForm
          the enum form   
            
         
        """
        pass
    
    ## Getter for property: (@link HolePatternFeatureBuilder.APIEnumLoc NXOpen.Vsa.HolePatternFeatureBuilder.APIEnumLoc@endlink) EnumLoc
    ##   the enum loc   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return HolePatternFeatureBuilder.APIEnumLoc
    @property
    def EnumLoc(self) -> HolePatternFeatureBuilder.APIEnumLoc:
        """
        Getter for property: (@link HolePatternFeatureBuilder.APIEnumLoc NXOpen.Vsa.HolePatternFeatureBuilder.APIEnumLoc@endlink) EnumLoc
          the enum loc   
            
         
        """
        pass
    
    ## Setter for property: (@link HolePatternFeatureBuilder.APIEnumLoc NXOpen.Vsa.HolePatternFeatureBuilder.APIEnumLoc@endlink) EnumLoc

    ##   the enum loc   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @EnumLoc.setter
    def EnumLoc(self, enumLoc: HolePatternFeatureBuilder.APIEnumLoc):
        """
        Setter for property: (@link HolePatternFeatureBuilder.APIEnumLoc NXOpen.Vsa.HolePatternFeatureBuilder.APIEnumLoc@endlink) EnumLoc
          the enum loc   
            
         
        """
        pass
    
    ## Getter for property: (@link HolePatternFeatureBuilder.APIEnumSize NXOpen.Vsa.HolePatternFeatureBuilder.APIEnumSize@endlink) EnumSize
    ##   the enum size   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return HolePatternFeatureBuilder.APIEnumSize
    @property
    def EnumSize(self) -> HolePatternFeatureBuilder.APIEnumSize:
        """
        Getter for property: (@link HolePatternFeatureBuilder.APIEnumSize NXOpen.Vsa.HolePatternFeatureBuilder.APIEnumSize@endlink) EnumSize
          the enum size   
            
         
        """
        pass
    
    ## Setter for property: (@link HolePatternFeatureBuilder.APIEnumSize NXOpen.Vsa.HolePatternFeatureBuilder.APIEnumSize@endlink) EnumSize

    ##   the enum size   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @EnumSize.setter
    def EnumSize(self, enumSize: HolePatternFeatureBuilder.APIEnumSize):
        """
        Setter for property: (@link HolePatternFeatureBuilder.APIEnumSize NXOpen.Vsa.HolePatternFeatureBuilder.APIEnumSize@endlink) EnumSize
          the enum size   
            
         
        """
        pass
    
    ## Getter for property: (int) NumInstanceCount
    ##   the enum size   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return int
    @property
    def NumInstanceCount(self) -> int:
        """
        Getter for property: (int) NumInstanceCount
          the enum size   
            
         
        """
        pass
    
    ## Setter for property: (int) NumInstanceCount

    ##   the enum size   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @NumInstanceCount.setter
    def NumInstanceCount(self, numInstanceCount: int):
        """
        Setter for property: (int) NumInstanceCount
          the enum size   
            
         
        """
        pass
    
    ## Getter for property: (str) StringDescription
    ##   the string description   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return str
    @property
    def StringDescription(self) -> str:
        """
        Getter for property: (str) StringDescription
          the string description   
            
         
        """
        pass
    
    ## Setter for property: (str) StringDescription

    ##   the string description   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @StringDescription.setter
    def StringDescription(self, stringDescription: str):
        """
        Setter for property: (str) StringDescription
          the string description   
            
         
        """
        pass
    
    ## Getter for property: (str) StringName
    ##   the string name   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return str
    @property
    def StringName(self) -> str:
        """
        Getter for property: (str) StringName
          the string name   
            
         
        """
        pass
    
    ## Setter for property: (str) StringName

    ##   the string name   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @StringName.setter
    def StringName(self, stringName: str):
        """
        Setter for property: (str) StringName
          the string name   
            
         
        """
        pass
    
import NXOpen
##  Represents a Hole pattern feature  <br> To create or edit an instance of this class, use @link NXOpen::Vsa::HolePatternFeatureBuilder  NXOpen::Vsa::HolePatternFeatureBuilder @endlink  <br> 
## 
##  <br>  Usable only on Windows <br>  
## 
##   <br>  Created in NX1899.0.0  <br> 

class HolePatternFeature(NXOpen.NXObject): 
    """ Represents a Hole pattern feature """
    pass


import NXOpen
## 
##     
##      <br> To create a new instance of this class, use @link NXOpen::Vsa::VsaManager::CreateMeasurementOperationBuilder  NXOpen::Vsa::VsaManager::CreateMeasurementOperationBuilder @endlink  <br> 
## 
##  <br>  Usable only on Windows <br>  
## 
##   <br>  Created in NX1899.0.0  <br> 

class MeasurementOperationBuilder(NXOpen.Builder): 
    """
    
    """


    ## 
    ##         
    ##         
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Relative</term><description> 
    ## </description> </item><item><term> 
    ## Absolute</term><description> 
    ## </description> </item></list>
    class APIEnumLimitType(Enum):
        """
        Members Include: <Relative> <Absolute>
        """
        Relative: int
        Absolute: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> MeasurementOperationBuilder.APIEnumLimitType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## 
    ##         
    ##         
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Angle</term><description> 
    ## </description> </item><item><term> 
    ## GapFlush</term><description> 
    ## </description> </item><item><term> 
    ## PointToPoint</term><description> 
    ## </description> </item><item><term> 
    ## PointToLine</term><description> 
    ## </description> </item></list>
    class APIEnumMeasurementType(Enum):
        """
        Members Include: <Angle> <GapFlush> <PointToPoint> <PointToLine>
        """
        Angle: int
        GapFlush: int
        PointToPoint: int
        PointToLine: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> MeasurementOperationBuilder.APIEnumMeasurementType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## 
    ##         
    ##         
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Short</term><description> 
    ## </description> </item><item><term> 
    ## Long</term><description> 
    ## </description> </item></list>
    class APIEnumNameFormat(Enum):
        """
        Members Include: <Short> <Long>
        """
        Short: int
        Long: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> MeasurementOperationBuilder.APIEnumNameFormat:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (float) DirectionI
    ##   the Nominal   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def DirectionI(self) -> float:
        """
        Getter for property: (float) DirectionI
          the Nominal   
            
         
        """
        pass
    
    ## Setter for property: (float) DirectionI

    ##   the Nominal   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @DirectionI.setter
    def DirectionI(self, directionI: float):
        """
        Setter for property: (float) DirectionI
          the Nominal   
            
         
        """
        pass
    
    ## Getter for property: (float) DirectionJ
    ##   the Nominal   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def DirectionJ(self) -> float:
        """
        Getter for property: (float) DirectionJ
          the Nominal   
            
         
        """
        pass
    
    ## Setter for property: (float) DirectionJ

    ##   the Nominal   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @DirectionJ.setter
    def DirectionJ(self, directionJ: float):
        """
        Setter for property: (float) DirectionJ
          the Nominal   
            
         
        """
        pass
    
    ## Getter for property: (float) DirectionK
    ##   the Nominal   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def DirectionK(self) -> float:
        """
        Getter for property: (float) DirectionK
          the Nominal   
            
         
        """
        pass
    
    ## Setter for property: (float) DirectionK

    ##   the Nominal   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @DirectionK.setter
    def DirectionK(self, directionK: float):
        """
        Setter for property: (float) DirectionK
          the Nominal   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.NXObject NXOpen.NXObject@endlink) FeatureFrom1
    ##   the From Feature1   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return NXOpen.NXObject
    @property
    def FeatureFrom1(self) -> NXOpen.NXObject:
        """
        Getter for property: (@link NXOpen.NXObject NXOpen.NXObject@endlink) FeatureFrom1
          the From Feature1   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXObject NXOpen.NXObject@endlink) FeatureFrom1

    ##   the From Feature1   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @FeatureFrom1.setter
    def FeatureFrom1(self, featureFrom1: NXOpen.NXObject):
        """
        Setter for property: (@link NXOpen.NXObject NXOpen.NXObject@endlink) FeatureFrom1
          the From Feature1   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.NXObject NXOpen.NXObject@endlink) FeatureFrom2
    ##   the From Feature2   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return NXOpen.NXObject
    @property
    def FeatureFrom2(self) -> NXOpen.NXObject:
        """
        Getter for property: (@link NXOpen.NXObject NXOpen.NXObject@endlink) FeatureFrom2
          the From Feature2   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXObject NXOpen.NXObject@endlink) FeatureFrom2

    ##   the From Feature2   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @FeatureFrom2.setter
    def FeatureFrom2(self, featureFrom2: NXOpen.NXObject):
        """
        Setter for property: (@link NXOpen.NXObject NXOpen.NXObject@endlink) FeatureFrom2
          the From Feature2   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.NXObject NXOpen.NXObject@endlink) FeatureFrom3
    ##   the From Feature3   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return NXOpen.NXObject
    @property
    def FeatureFrom3(self) -> NXOpen.NXObject:
        """
        Getter for property: (@link NXOpen.NXObject NXOpen.NXObject@endlink) FeatureFrom3
          the From Feature3   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXObject NXOpen.NXObject@endlink) FeatureFrom3

    ##   the From Feature3   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @FeatureFrom3.setter
    def FeatureFrom3(self, featureFrom3: NXOpen.NXObject):
        """
        Setter for property: (@link NXOpen.NXObject NXOpen.NXObject@endlink) FeatureFrom3
          the From Feature3   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.NXObject NXOpen.NXObject@endlink) FeatureTo1
    ##   the From To1   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return NXOpen.NXObject
    @property
    def FeatureTo1(self) -> NXOpen.NXObject:
        """
        Getter for property: (@link NXOpen.NXObject NXOpen.NXObject@endlink) FeatureTo1
          the From To1   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXObject NXOpen.NXObject@endlink) FeatureTo1

    ##   the From To1   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @FeatureTo1.setter
    def FeatureTo1(self, featureTo1: NXOpen.NXObject):
        """
        Setter for property: (@link NXOpen.NXObject NXOpen.NXObject@endlink) FeatureTo1
          the From To1   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.NXObject NXOpen.NXObject@endlink) FeatureTo2
    ##   the From To1   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return NXOpen.NXObject
    @property
    def FeatureTo2(self) -> NXOpen.NXObject:
        """
        Getter for property: (@link NXOpen.NXObject NXOpen.NXObject@endlink) FeatureTo2
          the From To1   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXObject NXOpen.NXObject@endlink) FeatureTo2

    ##   the From To1   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @FeatureTo2.setter
    def FeatureTo2(self, featureTo2: NXOpen.NXObject):
        """
        Setter for property: (@link NXOpen.NXObject NXOpen.NXObject@endlink) FeatureTo2
          the From To1   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.NXObject NXOpen.NXObject@endlink) FeatureTo3
    ##   the From To1   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return NXOpen.NXObject
    @property
    def FeatureTo3(self) -> NXOpen.NXObject:
        """
        Getter for property: (@link NXOpen.NXObject NXOpen.NXObject@endlink) FeatureTo3
          the From To1   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXObject NXOpen.NXObject@endlink) FeatureTo3

    ##   the From To1   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @FeatureTo3.setter
    def FeatureTo3(self, featureTo3: NXOpen.NXObject):
        """
        Setter for property: (@link NXOpen.NXObject NXOpen.NXObject@endlink) FeatureTo3
          the From To1   
            
         
        """
        pass
    
    ## Getter for property: (@link MeasurementOperationBuilder.APIEnumLimitType NXOpen.Vsa.MeasurementOperationBuilder.APIEnumLimitType@endlink) LimitType
    ##   the Limit Type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return MeasurementOperationBuilder.APIEnumLimitType
    @property
    def LimitType(self) -> MeasurementOperationBuilder.APIEnumLimitType:
        """
        Getter for property: (@link MeasurementOperationBuilder.APIEnumLimitType NXOpen.Vsa.MeasurementOperationBuilder.APIEnumLimitType@endlink) LimitType
          the Limit Type   
            
         
        """
        pass
    
    ## Setter for property: (@link MeasurementOperationBuilder.APIEnumLimitType NXOpen.Vsa.MeasurementOperationBuilder.APIEnumLimitType@endlink) LimitType

    ##   the Limit Type   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @LimitType.setter
    def LimitType(self, specifyType: MeasurementOperationBuilder.APIEnumLimitType):
        """
        Setter for property: (@link MeasurementOperationBuilder.APIEnumLimitType NXOpen.Vsa.MeasurementOperationBuilder.APIEnumLimitType@endlink) LimitType
          the Limit Type   
            
         
        """
        pass
    
    ## Getter for property: (float) Lsl
    ##   the Nominal   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def Lsl(self) -> float:
        """
        Getter for property: (float) Lsl
          the Nominal   
            
         
        """
        pass
    
    ## Setter for property: (float) Lsl

    ##   the Nominal   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @Lsl.setter
    def Lsl(self, lsl: float):
        """
        Setter for property: (float) Lsl
          the Nominal   
            
         
        """
        pass
    
    ## Getter for property: (@link MeasurementOperationBuilder.APIEnumMeasurementType NXOpen.Vsa.MeasurementOperationBuilder.APIEnumMeasurementType@endlink) MeasurementType
    ##   the enum Measurement Type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return MeasurementOperationBuilder.APIEnumMeasurementType
    @property
    def MeasurementType(self) -> MeasurementOperationBuilder.APIEnumMeasurementType:
        """
        Getter for property: (@link MeasurementOperationBuilder.APIEnumMeasurementType NXOpen.Vsa.MeasurementOperationBuilder.APIEnumMeasurementType@endlink) MeasurementType
          the enum Measurement Type   
            
         
        """
        pass
    
    ## Setter for property: (@link MeasurementOperationBuilder.APIEnumMeasurementType NXOpen.Vsa.MeasurementOperationBuilder.APIEnumMeasurementType@endlink) MeasurementType

    ##   the enum Measurement Type   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @MeasurementType.setter
    def MeasurementType(self, measurementType: MeasurementOperationBuilder.APIEnumMeasurementType):
        """
        Setter for property: (@link MeasurementOperationBuilder.APIEnumMeasurementType NXOpen.Vsa.MeasurementOperationBuilder.APIEnumMeasurementType@endlink) MeasurementType
          the enum Measurement Type   
            
         
        """
        pass
    
    ## Getter for property: (@link MeasurementOperationBuilder.APIEnumNameFormat NXOpen.Vsa.MeasurementOperationBuilder.APIEnumNameFormat@endlink) NameFormat
    ##   the Name Format   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return MeasurementOperationBuilder.APIEnumNameFormat
    @property
    def NameFormat(self) -> MeasurementOperationBuilder.APIEnumNameFormat:
        """
        Getter for property: (@link MeasurementOperationBuilder.APIEnumNameFormat NXOpen.Vsa.MeasurementOperationBuilder.APIEnumNameFormat@endlink) NameFormat
          the Name Format   
            
         
        """
        pass
    
    ## Setter for property: (@link MeasurementOperationBuilder.APIEnumNameFormat NXOpen.Vsa.MeasurementOperationBuilder.APIEnumNameFormat@endlink) NameFormat

    ##   the Name Format   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @NameFormat.setter
    def NameFormat(self, nameFormat: MeasurementOperationBuilder.APIEnumNameFormat):
        """
        Setter for property: (@link MeasurementOperationBuilder.APIEnumNameFormat NXOpen.Vsa.MeasurementOperationBuilder.APIEnumNameFormat@endlink) NameFormat
          the Name Format   
            
         
        """
        pass
    
    ## Getter for property: (float) Nominal
    ##   the Nominal   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def Nominal(self) -> float:
        """
        Getter for property: (float) Nominal
          the Nominal   
            
         
        """
        pass
    
    ## Setter for property: (float) Nominal

    ##   the Nominal   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @Nominal.setter
    def Nominal(self, nominal: float):
        """
        Setter for property: (float) Nominal
          the Nominal   
            
         
        """
        pass
    
    ## Getter for property: (str) StrDescription
    ##   the str description   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return str
    @property
    def StrDescription(self) -> str:
        """
        Getter for property: (str) StrDescription
          the str description   
            
         
        """
        pass
    
    ## Setter for property: (str) StrDescription

    ##   the str description   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @StrDescription.setter
    def StrDescription(self, strDescription: str):
        """
        Setter for property: (str) StrDescription
          the str description   
            
         
        """
        pass
    
    ## Getter for property: (str) StrName
    ##   the str name   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return str
    @property
    def StrName(self) -> str:
        """
        Getter for property: (str) StrName
          the str name   
            
         
        """
        pass
    
    ## Setter for property: (str) StrName

    ##   the str name   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @StrName.setter
    def StrName(self, strName: str):
        """
        Setter for property: (str) StrName
          the str name   
            
         
        """
        pass
    
    ## Getter for property: (bool) ToggleLimit
    ##   the toggle limit  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return bool
    @property
    def ToggleLimit(self) -> bool:
        """
        Getter for property: (bool) ToggleLimit
          the toggle limit  
            
         
        """
        pass
    
    ## Setter for property: (bool) ToggleLimit

    ##   the toggle limit  
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @ToggleLimit.setter
    def ToggleLimit(self, toggleLimit: bool):
        """
        Setter for property: (bool) ToggleLimit
          the toggle limit  
            
         
        """
        pass
    
    ## Getter for property: (float) Usl
    ##   the USL   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def Usl(self) -> float:
        """
        Getter for property: (float) Usl
          the USL   
            
         
        """
        pass
    
    ## Setter for property: (float) Usl

    ##   the USL   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @Usl.setter
    def Usl(self, usl: float):
        """
        Setter for property: (float) Usl
          the USL   
            
         
        """
        pass
    
import NXOpen
## 
##     
##      <br> To create a new instance of this class, use @link NXOpen::Vsa::VsaManager::CreatePartPropertyBuilder  NXOpen::Vsa::VsaManager::CreatePartPropertyBuilder @endlink  <br> 
## 
##  <br>  Usable only on Windows <br>  
## 
##   <br>  Created in NX2206.0.0  <br> 

class PartPropertyBuilder(NXOpen.Builder): 
    """
    
    """


    ## Getter for property: (float) ChordLength
    ##   the double Chord Length   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return float
    @property
    def ChordLength(self) -> float:
        """
        Getter for property: (float) ChordLength
          the double Chord Length   
            
         
        """
        pass
    
    ## Setter for property: (float) ChordLength

    ##   the double Chord Length   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @ChordLength.setter
    def ChordLength(self, chordLength: float):
        """
        Setter for property: (float) ChordLength
          the double Chord Length   
            
         
        """
        pass
    
    ## Getter for property: (float) MaximumSag
    ##   the double Maximum Sag   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return float
    @property
    def MaximumSag(self) -> float:
        """
        Getter for property: (float) MaximumSag
          the double Maximum Sag   
            
         
        """
        pass
    
    ## Setter for property: (float) MaximumSag

    ##   the double Maximum Sag   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @MaximumSag.setter
    def MaximumSag(self, maximumSag: float):
        """
        Setter for property: (float) MaximumSag
          the double Maximum Sag   
            
         
        """
        pass
    
    ## Getter for property: (str) PartName
    ##   the string name   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return str
    @property
    def PartName(self) -> str:
        """
        Getter for property: (str) PartName
          the string name   
            
         
        """
        pass
    
    ## Setter for property: (str) PartName

    ##   the string name   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @PartName.setter
    def PartName(self, partName: str):
        """
        Setter for property: (str) PartName
          the string name   
            
         
        """
        pass
    
import NXOpen
##  Represents a Part Property  <br> To create or edit an instance of this class, use @link NXOpen::Vsa::PartPropertyBuilder  NXOpen::Vsa::PartPropertyBuilder @endlink  <br> 
## 
##  <br>  Usable only on Windows <br>  
## 
##   <br>  Created in NX2206.0.0  <br> 

class PartProperty(NXOpen.NXObject): 
    """ Represents a Part Property """
    pass


import NXOpen
## 
##     
##      <br> To create a new instance of this class, use @link NXOpen::Vsa::VsaManager::CreatePinFeatureBuilder  NXOpen::Vsa::VsaManager::CreatePinFeatureBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## DoubleAnchorX </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleAnchorY </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleAnchorZ </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleDiameter1 </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleDiameter2 </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleDirectionI </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleDirectionJ </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleDirectionK </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleHeight </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleKurtosisForm </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleKurtosisLoc </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleKurtosisSize </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleSkewnessForm </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleSkewnessLoc </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleSkewnessSize </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## EnumForm </term> <description> 
##  
## Normal </description> </item> 
## 
## <item><term> 
##  
## EnumLoc </term> <description> 
##  
## Normal </description> </item> 
## 
## <item><term> 
##  
## EnumSize </term> <description> 
##  
## Normal </description> </item> 
## 
## </list> 

## 
##  <br>  Usable only on Windows <br>  
## 
##   <br>  Created in NX1899.0.0  <br> 

class PinFeatureBuilder(NXOpen.Builder): 
    """
    
    """


    ## 
    ##         
    ##         
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Normal</term><description> 
    ## </description> </item><item><term> 
    ## Uniform</term><description> 
    ## </description> </item><item><term> 
    ## Extreme</term><description> 
    ## </description> </item><item><term> 
    ## Pearson</term><description> 
    ## </description> </item><item><term> 
    ## Trapeziodal</term><description> 
    ## </description> </item></list>
    class APIEnumForm(Enum):
        """
        Members Include: <Normal> <Uniform> <Extreme> <Pearson> <Trapeziodal>
        """
        Normal: int
        Uniform: int
        Extreme: int
        Pearson: int
        Trapeziodal: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PinFeatureBuilder.APIEnumForm:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## 
    ##         
    ##         
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Normal</term><description> 
    ## </description> </item><item><term> 
    ## Uniform</term><description> 
    ## </description> </item><item><term> 
    ## Extreme</term><description> 
    ## </description> </item><item><term> 
    ## Pearson</term><description> 
    ## </description> </item><item><term> 
    ## Trapeziodal</term><description> 
    ## </description> </item></list>
    class APIEnumLoc(Enum):
        """
        Members Include: <Normal> <Uniform> <Extreme> <Pearson> <Trapeziodal>
        """
        Normal: int
        Uniform: int
        Extreme: int
        Pearson: int
        Trapeziodal: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PinFeatureBuilder.APIEnumLoc:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## 
    ##         
    ##         
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Normal</term><description> 
    ## </description> </item><item><term> 
    ## Uniform</term><description> 
    ## </description> </item><item><term> 
    ## Extreme</term><description> 
    ## </description> </item><item><term> 
    ## Pearson</term><description> 
    ## </description> </item><item><term> 
    ## Trapeziodal</term><description> 
    ## </description> </item></list>
    class APIEnumSize(Enum):
        """
        Members Include: <Normal> <Uniform> <Extreme> <Pearson> <Trapeziodal>
        """
        Normal: int
        Uniform: int
        Extreme: int
        Pearson: int
        Trapeziodal: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PinFeatureBuilder.APIEnumSize:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (float) DoubleAnchorX
    ##   the double anchor x   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def DoubleAnchorX(self) -> float:
        """
        Getter for property: (float) DoubleAnchorX
          the double anchor x   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleAnchorX

    ##   the double anchor x   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @DoubleAnchorX.setter
    def DoubleAnchorX(self, doubleAnchorX: float):
        """
        Setter for property: (float) DoubleAnchorX
          the double anchor x   
            
         
        """
        pass
    
    ## Getter for property: (float) DoubleAnchorY
    ##   the double anchor y   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def DoubleAnchorY(self) -> float:
        """
        Getter for property: (float) DoubleAnchorY
          the double anchor y   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleAnchorY

    ##   the double anchor y   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @DoubleAnchorY.setter
    def DoubleAnchorY(self, doubleAnchorY: float):
        """
        Setter for property: (float) DoubleAnchorY
          the double anchor y   
            
         
        """
        pass
    
    ## Getter for property: (float) DoubleAnchorZ
    ##   the double anchor z   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def DoubleAnchorZ(self) -> float:
        """
        Getter for property: (float) DoubleAnchorZ
          the double anchor z   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleAnchorZ

    ##   the double anchor z   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @DoubleAnchorZ.setter
    def DoubleAnchorZ(self, doubleAnchorZ: float):
        """
        Setter for property: (float) DoubleAnchorZ
          the double anchor z   
            
         
        """
        pass
    
    ## Getter for property: (float) DoubleDiameter1
    ##   the double diameter1   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def DoubleDiameter1(self) -> float:
        """
        Getter for property: (float) DoubleDiameter1
          the double diameter1   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleDiameter1

    ##   the double diameter1   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @DoubleDiameter1.setter
    def DoubleDiameter1(self, doubleDiameter1: float):
        """
        Setter for property: (float) DoubleDiameter1
          the double diameter1   
            
         
        """
        pass
    
    ## Getter for property: (float) DoubleDiameter2
    ##   the double diameter2   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def DoubleDiameter2(self) -> float:
        """
        Getter for property: (float) DoubleDiameter2
          the double diameter2   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleDiameter2

    ##   the double diameter2   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @DoubleDiameter2.setter
    def DoubleDiameter2(self, doubleDiameter2: float):
        """
        Setter for property: (float) DoubleDiameter2
          the double diameter2   
            
         
        """
        pass
    
    ## Getter for property: (float) DoubleDirectionI
    ##   the double direction i   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def DoubleDirectionI(self) -> float:
        """
        Getter for property: (float) DoubleDirectionI
          the double direction i   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleDirectionI

    ##   the double direction i   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @DoubleDirectionI.setter
    def DoubleDirectionI(self, doubleDirectionI: float):
        """
        Setter for property: (float) DoubleDirectionI
          the double direction i   
            
         
        """
        pass
    
    ## Getter for property: (float) DoubleDirectionJ
    ##   the double direction j   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def DoubleDirectionJ(self) -> float:
        """
        Getter for property: (float) DoubleDirectionJ
          the double direction j   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleDirectionJ

    ##   the double direction j   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @DoubleDirectionJ.setter
    def DoubleDirectionJ(self, doubleDirectionJ: float):
        """
        Setter for property: (float) DoubleDirectionJ
          the double direction j   
            
         
        """
        pass
    
    ## Getter for property: (float) DoubleDirectionK
    ##   the double direction k   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def DoubleDirectionK(self) -> float:
        """
        Getter for property: (float) DoubleDirectionK
          the double direction k   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleDirectionK

    ##   the double direction k   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @DoubleDirectionK.setter
    def DoubleDirectionK(self, doubleDirectionK: float):
        """
        Setter for property: (float) DoubleDirectionK
          the double direction k   
            
         
        """
        pass
    
    ## Getter for property: (float) DoubleHeight
    ##   the double height   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def DoubleHeight(self) -> float:
        """
        Getter for property: (float) DoubleHeight
          the double height   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleHeight

    ##   the double height   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @DoubleHeight.setter
    def DoubleHeight(self, doubleHeight: float):
        """
        Setter for property: (float) DoubleHeight
          the double height   
            
         
        """
        pass
    
    ## Getter for property: (float) DoubleKurtosisForm
    ##   the double kurtosis form   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def DoubleKurtosisForm(self) -> float:
        """
        Getter for property: (float) DoubleKurtosisForm
          the double kurtosis form   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleKurtosisForm

    ##   the double kurtosis form   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @DoubleKurtosisForm.setter
    def DoubleKurtosisForm(self, doubleKurtosisForm: float):
        """
        Setter for property: (float) DoubleKurtosisForm
          the double kurtosis form   
            
         
        """
        pass
    
    ## Getter for property: (float) DoubleKurtosisLoc
    ##   the double kurtosis loc   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def DoubleKurtosisLoc(self) -> float:
        """
        Getter for property: (float) DoubleKurtosisLoc
          the double kurtosis loc   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleKurtosisLoc

    ##   the double kurtosis loc   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @DoubleKurtosisLoc.setter
    def DoubleKurtosisLoc(self, doubleKurtosisLoc: float):
        """
        Setter for property: (float) DoubleKurtosisLoc
          the double kurtosis loc   
            
         
        """
        pass
    
    ## Getter for property: (float) DoubleKurtosisSize
    ##   the double kurtosis size   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def DoubleKurtosisSize(self) -> float:
        """
        Getter for property: (float) DoubleKurtosisSize
          the double kurtosis size   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleKurtosisSize

    ##   the double kurtosis size   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @DoubleKurtosisSize.setter
    def DoubleKurtosisSize(self, doubleKurtosisSize: float):
        """
        Setter for property: (float) DoubleKurtosisSize
          the double kurtosis size   
            
         
        """
        pass
    
    ## Getter for property: (float) DoubleSkewnessForm
    ##   the double skewness form   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def DoubleSkewnessForm(self) -> float:
        """
        Getter for property: (float) DoubleSkewnessForm
          the double skewness form   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleSkewnessForm

    ##   the double skewness form   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @DoubleSkewnessForm.setter
    def DoubleSkewnessForm(self, doubleSkewnessForm: float):
        """
        Setter for property: (float) DoubleSkewnessForm
          the double skewness form   
            
         
        """
        pass
    
    ## Getter for property: (float) DoubleSkewnessLoc
    ##   the double skewness loc   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def DoubleSkewnessLoc(self) -> float:
        """
        Getter for property: (float) DoubleSkewnessLoc
          the double skewness loc   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleSkewnessLoc

    ##   the double skewness loc   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @DoubleSkewnessLoc.setter
    def DoubleSkewnessLoc(self, doubleSkewnessLoc: float):
        """
        Setter for property: (float) DoubleSkewnessLoc
          the double skewness loc   
            
         
        """
        pass
    
    ## Getter for property: (float) DoubleSkewnessSize
    ##   the double skewness size   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def DoubleSkewnessSize(self) -> float:
        """
        Getter for property: (float) DoubleSkewnessSize
          the double skewness size   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleSkewnessSize

    ##   the double skewness size   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @DoubleSkewnessSize.setter
    def DoubleSkewnessSize(self, doubleSkewnessSize: float):
        """
        Setter for property: (float) DoubleSkewnessSize
          the double skewness size   
            
         
        """
        pass
    
    ## Getter for property: (@link PinFeatureBuilder.APIEnumForm NXOpen.Vsa.PinFeatureBuilder.APIEnumForm@endlink) EnumForm
    ##   the enum form   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return PinFeatureBuilder.APIEnumForm
    @property
    def EnumForm(self) -> PinFeatureBuilder.APIEnumForm:
        """
        Getter for property: (@link PinFeatureBuilder.APIEnumForm NXOpen.Vsa.PinFeatureBuilder.APIEnumForm@endlink) EnumForm
          the enum form   
            
         
        """
        pass
    
    ## Setter for property: (@link PinFeatureBuilder.APIEnumForm NXOpen.Vsa.PinFeatureBuilder.APIEnumForm@endlink) EnumForm

    ##   the enum form   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @EnumForm.setter
    def EnumForm(self, enumForm: PinFeatureBuilder.APIEnumForm):
        """
        Setter for property: (@link PinFeatureBuilder.APIEnumForm NXOpen.Vsa.PinFeatureBuilder.APIEnumForm@endlink) EnumForm
          the enum form   
            
         
        """
        pass
    
    ## Getter for property: (@link PinFeatureBuilder.APIEnumLoc NXOpen.Vsa.PinFeatureBuilder.APIEnumLoc@endlink) EnumLoc
    ##   the enum loc   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return PinFeatureBuilder.APIEnumLoc
    @property
    def EnumLoc(self) -> PinFeatureBuilder.APIEnumLoc:
        """
        Getter for property: (@link PinFeatureBuilder.APIEnumLoc NXOpen.Vsa.PinFeatureBuilder.APIEnumLoc@endlink) EnumLoc
          the enum loc   
            
         
        """
        pass
    
    ## Setter for property: (@link PinFeatureBuilder.APIEnumLoc NXOpen.Vsa.PinFeatureBuilder.APIEnumLoc@endlink) EnumLoc

    ##   the enum loc   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @EnumLoc.setter
    def EnumLoc(self, enumLoc: PinFeatureBuilder.APIEnumLoc):
        """
        Setter for property: (@link PinFeatureBuilder.APIEnumLoc NXOpen.Vsa.PinFeatureBuilder.APIEnumLoc@endlink) EnumLoc
          the enum loc   
            
         
        """
        pass
    
    ## Getter for property: (@link PinFeatureBuilder.APIEnumSize NXOpen.Vsa.PinFeatureBuilder.APIEnumSize@endlink) EnumSize
    ##   the enum size   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return PinFeatureBuilder.APIEnumSize
    @property
    def EnumSize(self) -> PinFeatureBuilder.APIEnumSize:
        """
        Getter for property: (@link PinFeatureBuilder.APIEnumSize NXOpen.Vsa.PinFeatureBuilder.APIEnumSize@endlink) EnumSize
          the enum size   
            
         
        """
        pass
    
    ## Setter for property: (@link PinFeatureBuilder.APIEnumSize NXOpen.Vsa.PinFeatureBuilder.APIEnumSize@endlink) EnumSize

    ##   the enum size   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @EnumSize.setter
    def EnumSize(self, enumSize: PinFeatureBuilder.APIEnumSize):
        """
        Setter for property: (@link PinFeatureBuilder.APIEnumSize NXOpen.Vsa.PinFeatureBuilder.APIEnumSize@endlink) EnumSize
          the enum size   
            
         
        """
        pass
    
    ## Getter for property: (str) StringDescription
    ##   the string description   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return str
    @property
    def StringDescription(self) -> str:
        """
        Getter for property: (str) StringDescription
          the string description   
            
         
        """
        pass
    
    ## Setter for property: (str) StringDescription

    ##   the string description   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @StringDescription.setter
    def StringDescription(self, stringDescription: str):
        """
        Setter for property: (str) StringDescription
          the string description   
            
         
        """
        pass
    
    ## Getter for property: (str) StringName
    ##   the string name   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return str
    @property
    def StringName(self) -> str:
        """
        Getter for property: (str) StringName
          the string name   
            
         
        """
        pass
    
    ## Setter for property: (str) StringName

    ##   the string name   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @StringName.setter
    def StringName(self, stringName: str):
        """
        Setter for property: (str) StringName
          the string name   
            
         
        """
        pass
    
import NXOpen
##  Represents a Pin feature  <br> To create or edit an instance of this class, use @link NXOpen::Vsa::PinFeatureBuilder  NXOpen::Vsa::PinFeatureBuilder @endlink  <br> 
## 
##  <br>  Usable only on Windows <br>  
## 
##   <br>  Created in NX1899.0.0  <br> 

class PinFeature(NXOpen.NXObject): 
    """ Represents a Pin feature """
    pass


import NXOpen
## 
##     
##      <br> To create a new instance of this class, use @link NXOpen::Vsa::VsaManager::CreatePinPatternFeatureBuilder  NXOpen::Vsa::VsaManager::CreatePinPatternFeatureBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## DoubleKurtosisForm </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleKurtosisLoc </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleKurtosisSize </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleSkewnessForm </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleSkewnessLoc </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleSkewnessSize </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## EnumForm </term> <description> 
##  
## Normal </description> </item> 
## 
## <item><term> 
##  
## EnumLoc </term> <description> 
##  
## Normal </description> </item> 
## 
## <item><term> 
##  
## EnumSize </term> <description> 
##  
## Normal </description> </item> 
## 
## </list> 

## 
##  <br>  Usable only on Windows <br>  
## 
##   <br>  Created in NX1899.0.0  <br> 

class PinPatternFeatureBuilder(NXOpen.Builder): 
    """
    
    """


    ## 
    ##         
    ##         
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Normal</term><description> 
    ## </description> </item><item><term> 
    ## Uniform</term><description> 
    ## </description> </item><item><term> 
    ## Extreme</term><description> 
    ## </description> </item><item><term> 
    ## Pearson</term><description> 
    ## </description> </item><item><term> 
    ## Trapeziodal</term><description> 
    ## </description> </item></list>
    class APIEnumForm(Enum):
        """
        Members Include: <Normal> <Uniform> <Extreme> <Pearson> <Trapeziodal>
        """
        Normal: int
        Uniform: int
        Extreme: int
        Pearson: int
        Trapeziodal: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PinPatternFeatureBuilder.APIEnumForm:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## 
    ##         
    ##         
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Normal</term><description> 
    ## </description> </item><item><term> 
    ## Uniform</term><description> 
    ## </description> </item><item><term> 
    ## Extreme</term><description> 
    ## </description> </item><item><term> 
    ## Pearson</term><description> 
    ## </description> </item><item><term> 
    ## Trapeziodal</term><description> 
    ## </description> </item></list>
    class APIEnumLoc(Enum):
        """
        Members Include: <Normal> <Uniform> <Extreme> <Pearson> <Trapeziodal>
        """
        Normal: int
        Uniform: int
        Extreme: int
        Pearson: int
        Trapeziodal: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PinPatternFeatureBuilder.APIEnumLoc:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## 
    ##         
    ##         
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Normal</term><description> 
    ## </description> </item><item><term> 
    ## Uniform</term><description> 
    ## </description> </item><item><term> 
    ## Extreme</term><description> 
    ## </description> </item><item><term> 
    ## Pearson</term><description> 
    ## </description> </item><item><term> 
    ## Trapeziodal</term><description> 
    ## </description> </item></list>
    class APIEnumSize(Enum):
        """
        Members Include: <Normal> <Uniform> <Extreme> <Pearson> <Trapeziodal>
        """
        Normal: int
        Uniform: int
        Extreme: int
        Pearson: int
        Trapeziodal: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PinPatternFeatureBuilder.APIEnumSize:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (float) DoubleKurtosisForm
    ##   the double kurtosis form   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def DoubleKurtosisForm(self) -> float:
        """
        Getter for property: (float) DoubleKurtosisForm
          the double kurtosis form   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleKurtosisForm

    ##   the double kurtosis form   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @DoubleKurtosisForm.setter
    def DoubleKurtosisForm(self, doubleKurtosisForm: float):
        """
        Setter for property: (float) DoubleKurtosisForm
          the double kurtosis form   
            
         
        """
        pass
    
    ## Getter for property: (float) DoubleKurtosisLoc
    ##   the double kurtosis loc   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def DoubleKurtosisLoc(self) -> float:
        """
        Getter for property: (float) DoubleKurtosisLoc
          the double kurtosis loc   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleKurtosisLoc

    ##   the double kurtosis loc   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @DoubleKurtosisLoc.setter
    def DoubleKurtosisLoc(self, doubleKurtosisLoc: float):
        """
        Setter for property: (float) DoubleKurtosisLoc
          the double kurtosis loc   
            
         
        """
        pass
    
    ## Getter for property: (float) DoubleKurtosisSize
    ##   the double kurtosis size   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def DoubleKurtosisSize(self) -> float:
        """
        Getter for property: (float) DoubleKurtosisSize
          the double kurtosis size   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleKurtosisSize

    ##   the double kurtosis size   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @DoubleKurtosisSize.setter
    def DoubleKurtosisSize(self, doubleKurtosisSize: float):
        """
        Setter for property: (float) DoubleKurtosisSize
          the double kurtosis size   
            
         
        """
        pass
    
    ## Getter for property: (float) DoubleSkewnessForm
    ##   the double skewness form   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def DoubleSkewnessForm(self) -> float:
        """
        Getter for property: (float) DoubleSkewnessForm
          the double skewness form   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleSkewnessForm

    ##   the double skewness form   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @DoubleSkewnessForm.setter
    def DoubleSkewnessForm(self, doubleSkewnessForm: float):
        """
        Setter for property: (float) DoubleSkewnessForm
          the double skewness form   
            
         
        """
        pass
    
    ## Getter for property: (float) DoubleSkewnessLoc
    ##   the double skewness loc   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def DoubleSkewnessLoc(self) -> float:
        """
        Getter for property: (float) DoubleSkewnessLoc
          the double skewness loc   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleSkewnessLoc

    ##   the double skewness loc   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @DoubleSkewnessLoc.setter
    def DoubleSkewnessLoc(self, doubleSkewnessLoc: float):
        """
        Setter for property: (float) DoubleSkewnessLoc
          the double skewness loc   
            
         
        """
        pass
    
    ## Getter for property: (float) DoubleSkewnessSize
    ##   the double skewness size   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def DoubleSkewnessSize(self) -> float:
        """
        Getter for property: (float) DoubleSkewnessSize
          the double skewness size   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleSkewnessSize

    ##   the double skewness size   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @DoubleSkewnessSize.setter
    def DoubleSkewnessSize(self, doubleSkewnessSize: float):
        """
        Setter for property: (float) DoubleSkewnessSize
          the double skewness size   
            
         
        """
        pass
    
    ## Getter for property: (@link PinPatternFeatureBuilder.APIEnumForm NXOpen.Vsa.PinPatternFeatureBuilder.APIEnumForm@endlink) EnumForm
    ##   the enum form   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return PinPatternFeatureBuilder.APIEnumForm
    @property
    def EnumForm(self) -> PinPatternFeatureBuilder.APIEnumForm:
        """
        Getter for property: (@link PinPatternFeatureBuilder.APIEnumForm NXOpen.Vsa.PinPatternFeatureBuilder.APIEnumForm@endlink) EnumForm
          the enum form   
            
         
        """
        pass
    
    ## Setter for property: (@link PinPatternFeatureBuilder.APIEnumForm NXOpen.Vsa.PinPatternFeatureBuilder.APIEnumForm@endlink) EnumForm

    ##   the enum form   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @EnumForm.setter
    def EnumForm(self, enumForm: PinPatternFeatureBuilder.APIEnumForm):
        """
        Setter for property: (@link PinPatternFeatureBuilder.APIEnumForm NXOpen.Vsa.PinPatternFeatureBuilder.APIEnumForm@endlink) EnumForm
          the enum form   
            
         
        """
        pass
    
    ## Getter for property: (@link PinPatternFeatureBuilder.APIEnumLoc NXOpen.Vsa.PinPatternFeatureBuilder.APIEnumLoc@endlink) EnumLoc
    ##   the enum loc   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return PinPatternFeatureBuilder.APIEnumLoc
    @property
    def EnumLoc(self) -> PinPatternFeatureBuilder.APIEnumLoc:
        """
        Getter for property: (@link PinPatternFeatureBuilder.APIEnumLoc NXOpen.Vsa.PinPatternFeatureBuilder.APIEnumLoc@endlink) EnumLoc
          the enum loc   
            
         
        """
        pass
    
    ## Setter for property: (@link PinPatternFeatureBuilder.APIEnumLoc NXOpen.Vsa.PinPatternFeatureBuilder.APIEnumLoc@endlink) EnumLoc

    ##   the enum loc   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @EnumLoc.setter
    def EnumLoc(self, enumLoc: PinPatternFeatureBuilder.APIEnumLoc):
        """
        Setter for property: (@link PinPatternFeatureBuilder.APIEnumLoc NXOpen.Vsa.PinPatternFeatureBuilder.APIEnumLoc@endlink) EnumLoc
          the enum loc   
            
         
        """
        pass
    
    ## Getter for property: (@link PinPatternFeatureBuilder.APIEnumSize NXOpen.Vsa.PinPatternFeatureBuilder.APIEnumSize@endlink) EnumSize
    ##   the enum size   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return PinPatternFeatureBuilder.APIEnumSize
    @property
    def EnumSize(self) -> PinPatternFeatureBuilder.APIEnumSize:
        """
        Getter for property: (@link PinPatternFeatureBuilder.APIEnumSize NXOpen.Vsa.PinPatternFeatureBuilder.APIEnumSize@endlink) EnumSize
          the enum size   
            
         
        """
        pass
    
    ## Setter for property: (@link PinPatternFeatureBuilder.APIEnumSize NXOpen.Vsa.PinPatternFeatureBuilder.APIEnumSize@endlink) EnumSize

    ##   the enum size   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @EnumSize.setter
    def EnumSize(self, enumSize: PinPatternFeatureBuilder.APIEnumSize):
        """
        Setter for property: (@link PinPatternFeatureBuilder.APIEnumSize NXOpen.Vsa.PinPatternFeatureBuilder.APIEnumSize@endlink) EnumSize
          the enum size   
            
         
        """
        pass
    
    ## Getter for property: (str) StringDescription
    ##   the string description   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return str
    @property
    def StringDescription(self) -> str:
        """
        Getter for property: (str) StringDescription
          the string description   
            
         
        """
        pass
    
    ## Setter for property: (str) StringDescription

    ##   the string description   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @StringDescription.setter
    def StringDescription(self, stringDescription: str):
        """
        Setter for property: (str) StringDescription
          the string description   
            
         
        """
        pass
    
    ## Getter for property: (str) StringName
    ##   the string name   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return str
    @property
    def StringName(self) -> str:
        """
        Getter for property: (str) StringName
          the string name   
            
         
        """
        pass
    
    ## Setter for property: (str) StringName

    ##   the string name   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @StringName.setter
    def StringName(self, stringName: str):
        """
        Setter for property: (str) StringName
          the string name   
            
         
        """
        pass
    
import NXOpen
##  Represents a pin pattern feature  <br> To create or edit an instance of this class, use @link NXOpen::Vsa::PinPatternFeatureBuilder  NXOpen::Vsa::PinPatternFeatureBuilder @endlink  <br> 
## 
##  <br>  Usable only on Windows <br>  
## 
##   <br>  Created in NX1899.0.0  <br> 

class PinPatternFeature(NXOpen.NXObject): 
    """ Represents a pin pattern feature """
    pass


import NXOpen
## 
##     
##      <br> To create a new instance of this class, use @link NXOpen::Vsa::VsaManager::CreatePlaneFeatureBuilder  NXOpen::Vsa::VsaManager::CreatePlaneFeatureBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## DoubleKurtosisForm </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleKurtosisLoc </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleKurtosisSize </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleSkewnessForm </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleSkewnessLoc </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleSkewnessSize </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## EnumForm </term> <description> 
##  
## Normal </description> </item> 
## 
## <item><term> 
##  
## EnumLoc </term> <description> 
##  
## Normal </description> </item> 
## 
## <item><term> 
##  
## EnumSize </term> <description> 
##  
## Normal </description> </item> 
## 
## <item><term> 
##  
## I </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## J </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## K </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## X </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## Y </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## Z </term> <description> 
##  
## 0 </description> </item> 
## 
## </list> 

## 
##  <br>  Usable only on Windows <br>  
## 
##   <br>  Created in NX1899.0.0  <br> 

class PlaneFeatureBuilder(NXOpen.Builder): 
    """
    
    """


    ## 
    ##         This enum is for Form distribution type.
    ##         
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Normal</term><description> 
    ## </description> </item><item><term> 
    ## Uniform</term><description> 
    ## </description> </item><item><term> 
    ## Extreme</term><description> 
    ## </description> </item><item><term> 
    ## Pearson</term><description> 
    ## </description> </item><item><term> 
    ## Trapeziodal</term><description> 
    ## </description> </item></list>
    class APIEnumForm(Enum):
        """
        Members Include: <Normal> <Uniform> <Extreme> <Pearson> <Trapeziodal>
        """
        Normal: int
        Uniform: int
        Extreme: int
        Pearson: int
        Trapeziodal: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PlaneFeatureBuilder.APIEnumForm:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## 
    ##         This enum is for Location distribution type.
    ##         
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Normal</term><description> 
    ## </description> </item><item><term> 
    ## Uniform</term><description> 
    ## </description> </item><item><term> 
    ## Extreme</term><description> 
    ## </description> </item><item><term> 
    ## Pearson</term><description> 
    ## </description> </item><item><term> 
    ## Trapeziodal</term><description> 
    ## </description> </item></list>
    class APIEnumLoc(Enum):
        """
        Members Include: <Normal> <Uniform> <Extreme> <Pearson> <Trapeziodal>
        """
        Normal: int
        Uniform: int
        Extreme: int
        Pearson: int
        Trapeziodal: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PlaneFeatureBuilder.APIEnumLoc:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## 
    ##          This enum is for Size distribution type.
    ##         
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Normal</term><description> 
    ## </description> </item><item><term> 
    ## Uniform</term><description> 
    ## </description> </item><item><term> 
    ## Extreme</term><description> 
    ## </description> </item><item><term> 
    ## Pearson</term><description> 
    ## </description> </item><item><term> 
    ## Trapeziodal</term><description> 
    ## </description> </item></list>
    class APIEnumSize(Enum):
        """
        Members Include: <Normal> <Uniform> <Extreme> <Pearson> <Trapeziodal>
        """
        Normal: int
        Uniform: int
        Extreme: int
        Pearson: int
        Trapeziodal: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PlaneFeatureBuilder.APIEnumSize:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (str) Description
    ##   the string description   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return str
    @property
    def Description(self) -> str:
        """
        Getter for property: (str) Description
          the string description   
            
         
        """
        pass
    
    ## Setter for property: (str) Description

    ##   the string description   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @Description.setter
    def Description(self, stringDescription: str):
        """
        Setter for property: (str) Description
          the string description   
            
         
        """
        pass
    
    ## Getter for property: (float) DoubleKurtosisForm
    ##   the double kurtosis form   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def DoubleKurtosisForm(self) -> float:
        """
        Getter for property: (float) DoubleKurtosisForm
          the double kurtosis form   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleKurtosisForm

    ##   the double kurtosis form   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @DoubleKurtosisForm.setter
    def DoubleKurtosisForm(self, doubleKurtosisForm: float):
        """
        Setter for property: (float) DoubleKurtosisForm
          the double kurtosis form   
            
         
        """
        pass
    
    ## Getter for property: (float) DoubleKurtosisLoc
    ##   the double kurtosis loc   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def DoubleKurtosisLoc(self) -> float:
        """
        Getter for property: (float) DoubleKurtosisLoc
          the double kurtosis loc   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleKurtosisLoc

    ##   the double kurtosis loc   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @DoubleKurtosisLoc.setter
    def DoubleKurtosisLoc(self, doubleKurtosisLoc: float):
        """
        Setter for property: (float) DoubleKurtosisLoc
          the double kurtosis loc   
            
         
        """
        pass
    
    ## Getter for property: (float) DoubleKurtosisSize
    ##   the double kurtosis size   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def DoubleKurtosisSize(self) -> float:
        """
        Getter for property: (float) DoubleKurtosisSize
          the double kurtosis size   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleKurtosisSize

    ##   the double kurtosis size   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @DoubleKurtosisSize.setter
    def DoubleKurtosisSize(self, doubleKurtosisSize: float):
        """
        Setter for property: (float) DoubleKurtosisSize
          the double kurtosis size   
            
         
        """
        pass
    
    ## Getter for property: (float) DoubleSkewnessForm
    ##   the double skewness form   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def DoubleSkewnessForm(self) -> float:
        """
        Getter for property: (float) DoubleSkewnessForm
          the double skewness form   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleSkewnessForm

    ##   the double skewness form   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @DoubleSkewnessForm.setter
    def DoubleSkewnessForm(self, doubleSkewnessForm: float):
        """
        Setter for property: (float) DoubleSkewnessForm
          the double skewness form   
            
         
        """
        pass
    
    ## Getter for property: (float) DoubleSkewnessLoc
    ##   the double skewness loc   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def DoubleSkewnessLoc(self) -> float:
        """
        Getter for property: (float) DoubleSkewnessLoc
          the double skewness loc   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleSkewnessLoc

    ##   the double skewness loc   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @DoubleSkewnessLoc.setter
    def DoubleSkewnessLoc(self, doubleSkewnessLoc: float):
        """
        Setter for property: (float) DoubleSkewnessLoc
          the double skewness loc   
            
         
        """
        pass
    
    ## Getter for property: (float) DoubleSkewnessSize
    ##   the double skewness size   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def DoubleSkewnessSize(self) -> float:
        """
        Getter for property: (float) DoubleSkewnessSize
          the double skewness size   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleSkewnessSize

    ##   the double skewness size   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @DoubleSkewnessSize.setter
    def DoubleSkewnessSize(self, doubleSkewnessSize: float):
        """
        Setter for property: (float) DoubleSkewnessSize
          the double skewness size   
            
         
        """
        pass
    
    ## Getter for property: (@link PlaneFeatureBuilder.APIEnumForm NXOpen.Vsa.PlaneFeatureBuilder.APIEnumForm@endlink) EnumForm
    ##   the enum form   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return PlaneFeatureBuilder.APIEnumForm
    @property
    def EnumForm(self) -> PlaneFeatureBuilder.APIEnumForm:
        """
        Getter for property: (@link PlaneFeatureBuilder.APIEnumForm NXOpen.Vsa.PlaneFeatureBuilder.APIEnumForm@endlink) EnumForm
          the enum form   
            
         
        """
        pass
    
    ## Setter for property: (@link PlaneFeatureBuilder.APIEnumForm NXOpen.Vsa.PlaneFeatureBuilder.APIEnumForm@endlink) EnumForm

    ##   the enum form   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @EnumForm.setter
    def EnumForm(self, enumForm: PlaneFeatureBuilder.APIEnumForm):
        """
        Setter for property: (@link PlaneFeatureBuilder.APIEnumForm NXOpen.Vsa.PlaneFeatureBuilder.APIEnumForm@endlink) EnumForm
          the enum form   
            
         
        """
        pass
    
    ## Getter for property: (@link PlaneFeatureBuilder.APIEnumLoc NXOpen.Vsa.PlaneFeatureBuilder.APIEnumLoc@endlink) EnumLoc
    ##   the enum loc   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return PlaneFeatureBuilder.APIEnumLoc
    @property
    def EnumLoc(self) -> PlaneFeatureBuilder.APIEnumLoc:
        """
        Getter for property: (@link PlaneFeatureBuilder.APIEnumLoc NXOpen.Vsa.PlaneFeatureBuilder.APIEnumLoc@endlink) EnumLoc
          the enum loc   
            
         
        """
        pass
    
    ## Setter for property: (@link PlaneFeatureBuilder.APIEnumLoc NXOpen.Vsa.PlaneFeatureBuilder.APIEnumLoc@endlink) EnumLoc

    ##   the enum loc   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @EnumLoc.setter
    def EnumLoc(self, enumLoc: PlaneFeatureBuilder.APIEnumLoc):
        """
        Setter for property: (@link PlaneFeatureBuilder.APIEnumLoc NXOpen.Vsa.PlaneFeatureBuilder.APIEnumLoc@endlink) EnumLoc
          the enum loc   
            
         
        """
        pass
    
    ## Getter for property: (@link PlaneFeatureBuilder.APIEnumSize NXOpen.Vsa.PlaneFeatureBuilder.APIEnumSize@endlink) EnumSize
    ##   the enum size   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return PlaneFeatureBuilder.APIEnumSize
    @property
    def EnumSize(self) -> PlaneFeatureBuilder.APIEnumSize:
        """
        Getter for property: (@link PlaneFeatureBuilder.APIEnumSize NXOpen.Vsa.PlaneFeatureBuilder.APIEnumSize@endlink) EnumSize
          the enum size   
            
         
        """
        pass
    
    ## Setter for property: (@link PlaneFeatureBuilder.APIEnumSize NXOpen.Vsa.PlaneFeatureBuilder.APIEnumSize@endlink) EnumSize

    ##   the enum size   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @EnumSize.setter
    def EnumSize(self, enumSize: PlaneFeatureBuilder.APIEnumSize):
        """
        Setter for property: (@link PlaneFeatureBuilder.APIEnumSize NXOpen.Vsa.PlaneFeatureBuilder.APIEnumSize@endlink) EnumSize
          the enum size   
            
         
        """
        pass
    
    ## Getter for property: (float) I
    ##   the i   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def I(self) -> float:
        """
        Getter for property: (float) I
          the i   
            
         
        """
        pass
    
    ## Setter for property: (float) I

    ##   the i   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @I.setter
    def I(self, i: float):
        """
        Setter for property: (float) I
          the i   
            
         
        """
        pass
    
    ## Getter for property: (float) J
    ##   the j   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def J(self) -> float:
        """
        Getter for property: (float) J
          the j   
            
         
        """
        pass
    
    ## Setter for property: (float) J

    ##   the j   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @J.setter
    def J(self, j: float):
        """
        Setter for property: (float) J
          the j   
            
         
        """
        pass
    
    ## Getter for property: (float) K
    ##   the k   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def K(self) -> float:
        """
        Getter for property: (float) K
          the k   
            
         
        """
        pass
    
    ## Setter for property: (float) K

    ##   the k   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @K.setter
    def K(self, k: float):
        """
        Setter for property: (float) K
          the k   
            
         
        """
        pass
    
    ## Getter for property: (str) Name
    ##   the name   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

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
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
          the name   
            
         
        """
        pass
    
    ## Getter for property: (float) X
    ##   the x   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def X(self) -> float:
        """
        Getter for property: (float) X
          the x   
            
         
        """
        pass
    
    ## Setter for property: (float) X

    ##   the x   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @X.setter
    def X(self, x: float):
        """
        Setter for property: (float) X
          the x   
            
         
        """
        pass
    
    ## Getter for property: (float) Y
    ##   the y   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def Y(self) -> float:
        """
        Getter for property: (float) Y
          the y   
            
         
        """
        pass
    
    ## Setter for property: (float) Y

    ##   the y   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @Y.setter
    def Y(self, y: float):
        """
        Setter for property: (float) Y
          the y   
            
         
        """
        pass
    
    ## Getter for property: (float) Z
    ##   the z   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def Z(self) -> float:
        """
        Getter for property: (float) Z
          the z   
            
         
        """
        pass
    
    ## Setter for property: (float) Z

    ##   the z   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @Z.setter
    def Z(self, z: float):
        """
        Setter for property: (float) Z
          the z   
            
         
        """
        pass
    
import NXOpen
## 
##     
##      <br> To create a new instance of this class, use @link NXOpen::Vsa::VsaManager::CreatePointFeatureBuilder  NXOpen::Vsa::VsaManager::CreatePointFeatureBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## DoubleAnchorX </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleAnchorY </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleAnchorZ </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleDirectionI </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleDirectionJ </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleDirectionK </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleKurtosisForm </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleKurtosisLoc </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleKurtosisSize </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleSkewnessForm </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleSkewnessLoc </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleSkewnessSize </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## EnumForm </term> <description> 
##  
## Normal </description> </item> 
## 
## <item><term> 
##  
## EnumLoc </term> <description> 
##  
## Normal </description> </item> 
## 
## <item><term> 
##  
## EnumSize </term> <description> 
##  
## Normal </description> </item> 
## 
## </list> 

## 
##  <br>  Usable only on Windows <br>  
## 
##   <br>  Created in NX1899.0.0  <br> 

class PointFeatureBuilder(NXOpen.Builder): 
    """
    
    """


    ## 
    ##         
    ##         
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Normal</term><description> 
    ## </description> </item><item><term> 
    ## Uniform</term><description> 
    ## </description> </item><item><term> 
    ## Extreme</term><description> 
    ## </description> </item><item><term> 
    ## Pearson</term><description> 
    ## </description> </item><item><term> 
    ## Trapeziodal</term><description> 
    ## </description> </item></list>
    class APIEnumForm(Enum):
        """
        Members Include: <Normal> <Uniform> <Extreme> <Pearson> <Trapeziodal>
        """
        Normal: int
        Uniform: int
        Extreme: int
        Pearson: int
        Trapeziodal: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PointFeatureBuilder.APIEnumForm:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## 
    ##         
    ##         
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Normal</term><description> 
    ## </description> </item><item><term> 
    ## Uniform</term><description> 
    ## </description> </item><item><term> 
    ## Extreme</term><description> 
    ## </description> </item><item><term> 
    ## Pearson</term><description> 
    ## </description> </item><item><term> 
    ## Trapeziodal</term><description> 
    ## </description> </item></list>
    class APIEnumLoc(Enum):
        """
        Members Include: <Normal> <Uniform> <Extreme> <Pearson> <Trapeziodal>
        """
        Normal: int
        Uniform: int
        Extreme: int
        Pearson: int
        Trapeziodal: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PointFeatureBuilder.APIEnumLoc:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## 
    ##         
    ##         
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Normal</term><description> 
    ## </description> </item><item><term> 
    ## Uniform</term><description> 
    ## </description> </item><item><term> 
    ## Extreme</term><description> 
    ## </description> </item><item><term> 
    ## Pearson</term><description> 
    ## </description> </item><item><term> 
    ## Trapeziodal</term><description> 
    ## </description> </item></list>
    class APIEnumSize(Enum):
        """
        Members Include: <Normal> <Uniform> <Extreme> <Pearson> <Trapeziodal>
        """
        Normal: int
        Uniform: int
        Extreme: int
        Pearson: int
        Trapeziodal: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PointFeatureBuilder.APIEnumSize:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (float) DoubleAnchorX
    ##   the property represents X value of anchore.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def DoubleAnchorX(self) -> float:
        """
        Getter for property: (float) DoubleAnchorX
          the property represents X value of anchore.  
             
         
        """
        pass
    
    ## Setter for property: (float) DoubleAnchorX

    ##   the property represents X value of anchore.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @DoubleAnchorX.setter
    def DoubleAnchorX(self, doubleAnchorX: float):
        """
        Setter for property: (float) DoubleAnchorX
          the property represents X value of anchore.  
             
         
        """
        pass
    
    ## Getter for property: (float) DoubleAnchorY
    ##   the property represents Y value of anchore.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def DoubleAnchorY(self) -> float:
        """
        Getter for property: (float) DoubleAnchorY
          the property represents Y value of anchore.  
             
         
        """
        pass
    
    ## Setter for property: (float) DoubleAnchorY

    ##   the property represents Y value of anchore.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @DoubleAnchorY.setter
    def DoubleAnchorY(self, doubleAnchorY: float):
        """
        Setter for property: (float) DoubleAnchorY
          the property represents Y value of anchore.  
             
         
        """
        pass
    
    ## Getter for property: (float) DoubleAnchorZ
    ##   the property represents Z value of anchore.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def DoubleAnchorZ(self) -> float:
        """
        Getter for property: (float) DoubleAnchorZ
          the property represents Z value of anchore.  
             
         
        """
        pass
    
    ## Setter for property: (float) DoubleAnchorZ

    ##   the property represents Z value of anchore.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @DoubleAnchorZ.setter
    def DoubleAnchorZ(self, doubleAnchorZ: float):
        """
        Setter for property: (float) DoubleAnchorZ
          the property represents Z value of anchore.  
             
         
        """
        pass
    
    ## Getter for property: (float) DoubleDirectionI
    ##   the property represents X value of normal.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def DoubleDirectionI(self) -> float:
        """
        Getter for property: (float) DoubleDirectionI
          the property represents X value of normal.  
             
         
        """
        pass
    
    ## Setter for property: (float) DoubleDirectionI

    ##   the property represents X value of normal.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @DoubleDirectionI.setter
    def DoubleDirectionI(self, doubleDirectionI: float):
        """
        Setter for property: (float) DoubleDirectionI
          the property represents X value of normal.  
             
         
        """
        pass
    
    ## Getter for property: (float) DoubleDirectionJ
    ##   the property represents Y value of normal.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def DoubleDirectionJ(self) -> float:
        """
        Getter for property: (float) DoubleDirectionJ
          the property represents Y value of normal.  
             
         
        """
        pass
    
    ## Setter for property: (float) DoubleDirectionJ

    ##   the property represents Y value of normal.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @DoubleDirectionJ.setter
    def DoubleDirectionJ(self, doubleDirectionJ: float):
        """
        Setter for property: (float) DoubleDirectionJ
          the property represents Y value of normal.  
             
         
        """
        pass
    
    ## Getter for property: (float) DoubleDirectionK
    ##   the property represents Z value of normal.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def DoubleDirectionK(self) -> float:
        """
        Getter for property: (float) DoubleDirectionK
          the property represents Z value of normal.  
             
         
        """
        pass
    
    ## Setter for property: (float) DoubleDirectionK

    ##   the property represents Z value of normal.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @DoubleDirectionK.setter
    def DoubleDirectionK(self, doubleDirectionK: float):
        """
        Setter for property: (float) DoubleDirectionK
          the property represents Z value of normal.  
             
         
        """
        pass
    
    ## Getter for property: (float) DoubleKurtosisForm
    ##   the property represents Form distribution Kurtosis.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def DoubleKurtosisForm(self) -> float:
        """
        Getter for property: (float) DoubleKurtosisForm
          the property represents Form distribution Kurtosis.  
             
         
        """
        pass
    
    ## Setter for property: (float) DoubleKurtosisForm

    ##   the property represents Form distribution Kurtosis.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @DoubleKurtosisForm.setter
    def DoubleKurtosisForm(self, doubleKurtosisForm: float):
        """
        Setter for property: (float) DoubleKurtosisForm
          the property represents Form distribution Kurtosis.  
             
         
        """
        pass
    
    ## Getter for property: (float) DoubleKurtosisLoc
    ##   the property represents Loc distribution Kurtosis.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def DoubleKurtosisLoc(self) -> float:
        """
        Getter for property: (float) DoubleKurtosisLoc
          the property represents Loc distribution Kurtosis.  
             
         
        """
        pass
    
    ## Setter for property: (float) DoubleKurtosisLoc

    ##   the property represents Loc distribution Kurtosis.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @DoubleKurtosisLoc.setter
    def DoubleKurtosisLoc(self, doubleKurtosisLoc: float):
        """
        Setter for property: (float) DoubleKurtosisLoc
          the property represents Loc distribution Kurtosis.  
             
         
        """
        pass
    
    ## Getter for property: (float) DoubleKurtosisSize
    ##   the property represents Size distribution Kurtosis.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def DoubleKurtosisSize(self) -> float:
        """
        Getter for property: (float) DoubleKurtosisSize
          the property represents Size distribution Kurtosis.  
             
         
        """
        pass
    
    ## Setter for property: (float) DoubleKurtosisSize

    ##   the property represents Size distribution Kurtosis.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @DoubleKurtosisSize.setter
    def DoubleKurtosisSize(self, doubleKurtosisSize: float):
        """
        Setter for property: (float) DoubleKurtosisSize
          the property represents Size distribution Kurtosis.  
             
         
        """
        pass
    
    ## Getter for property: (float) DoubleSkewnessForm
    ##   the property represents Form distribution Skewness.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def DoubleSkewnessForm(self) -> float:
        """
        Getter for property: (float) DoubleSkewnessForm
          the property represents Form distribution Skewness.  
             
         
        """
        pass
    
    ## Setter for property: (float) DoubleSkewnessForm

    ##   the property represents Form distribution Skewness.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @DoubleSkewnessForm.setter
    def DoubleSkewnessForm(self, doubleSkewnessForm: float):
        """
        Setter for property: (float) DoubleSkewnessForm
          the property represents Form distribution Skewness.  
             
         
        """
        pass
    
    ## Getter for property: (float) DoubleSkewnessLoc
    ##   the property represents Loc distribution Skewness.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def DoubleSkewnessLoc(self) -> float:
        """
        Getter for property: (float) DoubleSkewnessLoc
          the property represents Loc distribution Skewness.  
             
         
        """
        pass
    
    ## Setter for property: (float) DoubleSkewnessLoc

    ##   the property represents Loc distribution Skewness.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @DoubleSkewnessLoc.setter
    def DoubleSkewnessLoc(self, doubleSkewnessLoc: float):
        """
        Setter for property: (float) DoubleSkewnessLoc
          the property represents Loc distribution Skewness.  
             
         
        """
        pass
    
    ## Getter for property: (float) DoubleSkewnessSize
    ##   the property represents Size distribution Skewness.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def DoubleSkewnessSize(self) -> float:
        """
        Getter for property: (float) DoubleSkewnessSize
          the property represents Size distribution Skewness.  
             
         
        """
        pass
    
    ## Setter for property: (float) DoubleSkewnessSize

    ##   the property represents Size distribution Skewness.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @DoubleSkewnessSize.setter
    def DoubleSkewnessSize(self, doubleSkewnessSize: float):
        """
        Setter for property: (float) DoubleSkewnessSize
          the property represents Size distribution Skewness.  
             
         
        """
        pass
    
    ## Getter for property: (@link PointFeatureBuilder.APIEnumForm NXOpen.Vsa.PointFeatureBuilder.APIEnumForm@endlink) EnumForm
    ##   the property represents Form distribution type.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return PointFeatureBuilder.APIEnumForm
    @property
    def EnumForm(self) -> PointFeatureBuilder.APIEnumForm:
        """
        Getter for property: (@link PointFeatureBuilder.APIEnumForm NXOpen.Vsa.PointFeatureBuilder.APIEnumForm@endlink) EnumForm
          the property represents Form distribution type.  
             
         
        """
        pass
    
    ## Setter for property: (@link PointFeatureBuilder.APIEnumForm NXOpen.Vsa.PointFeatureBuilder.APIEnumForm@endlink) EnumForm

    ##   the property represents Form distribution type.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @EnumForm.setter
    def EnumForm(self, enumForm: PointFeatureBuilder.APIEnumForm):
        """
        Setter for property: (@link PointFeatureBuilder.APIEnumForm NXOpen.Vsa.PointFeatureBuilder.APIEnumForm@endlink) EnumForm
          the property represents Form distribution type.  
             
         
        """
        pass
    
    ## Getter for property: (@link PointFeatureBuilder.APIEnumLoc NXOpen.Vsa.PointFeatureBuilder.APIEnumLoc@endlink) EnumLoc
    ##   the property represents Loc distribution type.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return PointFeatureBuilder.APIEnumLoc
    @property
    def EnumLoc(self) -> PointFeatureBuilder.APIEnumLoc:
        """
        Getter for property: (@link PointFeatureBuilder.APIEnumLoc NXOpen.Vsa.PointFeatureBuilder.APIEnumLoc@endlink) EnumLoc
          the property represents Loc distribution type.  
             
         
        """
        pass
    
    ## Setter for property: (@link PointFeatureBuilder.APIEnumLoc NXOpen.Vsa.PointFeatureBuilder.APIEnumLoc@endlink) EnumLoc

    ##   the property represents Loc distribution type.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @EnumLoc.setter
    def EnumLoc(self, enumLoc: PointFeatureBuilder.APIEnumLoc):
        """
        Setter for property: (@link PointFeatureBuilder.APIEnumLoc NXOpen.Vsa.PointFeatureBuilder.APIEnumLoc@endlink) EnumLoc
          the property represents Loc distribution type.  
             
         
        """
        pass
    
    ## Getter for property: (@link PointFeatureBuilder.APIEnumSize NXOpen.Vsa.PointFeatureBuilder.APIEnumSize@endlink) EnumSize
    ##   the property represents Size distribution type.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return PointFeatureBuilder.APIEnumSize
    @property
    def EnumSize(self) -> PointFeatureBuilder.APIEnumSize:
        """
        Getter for property: (@link PointFeatureBuilder.APIEnumSize NXOpen.Vsa.PointFeatureBuilder.APIEnumSize@endlink) EnumSize
          the property represents Size distribution type.  
             
         
        """
        pass
    
    ## Setter for property: (@link PointFeatureBuilder.APIEnumSize NXOpen.Vsa.PointFeatureBuilder.APIEnumSize@endlink) EnumSize

    ##   the property represents Size distribution type.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @EnumSize.setter
    def EnumSize(self, enumSize: PointFeatureBuilder.APIEnumSize):
        """
        Setter for property: (@link PointFeatureBuilder.APIEnumSize NXOpen.Vsa.PointFeatureBuilder.APIEnumSize@endlink) EnumSize
          the property represents Size distribution type.  
             
         
        """
        pass
    
    ## Getter for property: (str) StringDescription
    ##   the property represents point feature discription.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return str
    @property
    def StringDescription(self) -> str:
        """
        Getter for property: (str) StringDescription
          the property represents point feature discription.  
             
         
        """
        pass
    
    ## Setter for property: (str) StringDescription

    ##   the property represents point feature discription.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @StringDescription.setter
    def StringDescription(self, stringDescription: str):
        """
        Setter for property: (str) StringDescription
          the property represents point feature discription.  
             
         
        """
        pass
    
    ## Getter for property: (str) StringName
    ##   the property represents Point feature name.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return str
    @property
    def StringName(self) -> str:
        """
        Getter for property: (str) StringName
          the property represents Point feature name.  
             
         
        """
        pass
    
    ## Setter for property: (str) StringName

    ##   the property represents Point feature name.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @StringName.setter
    def StringName(self, stringName: str):
        """
        Setter for property: (str) StringName
          the property represents Point feature name.  
             
         
        """
        pass
    
import NXOpen
##  Represents a Point feature  <br> To create or edit an instance of this class, use @link NXOpen::Vsa::PointFeatureBuilder  NXOpen::Vsa::PointFeatureBuilder @endlink  <br> 
## 
##  <br>  Usable only on Windows <br>  
## 
##   <br>  Created in NX1899.0.0  <br> 

class PointFeature(NXOpen.NXObject): 
    """ Represents a Point feature """
    pass


import NXOpen
## 
##     
##      <br> To create a new instance of this class, use @link NXOpen::Vsa::VsaManager::CreatePointSubFeatureBuilder  NXOpen::Vsa::VsaManager::CreatePointSubFeatureBuilder @endlink  <br> 
## 
##  <br>  Usable only on Windows <br>  
## 
##   <br>  Created in NX11.0.0  <br> 

class PointSubFeatureBuilder(NXOpen.Builder): 
    """
    
    """


    ## 
    ##         
    ##         
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## OnSurface</term><description> 
    ## </description> </item><item><term> 
    ## OnAnchor</term><description> 
    ## </description> </item><item><term> 
    ## OnCenter</term><description> 
    ## </description> </item><item><term> 
    ## OnTop</term><description> 
    ## </description> </item></list>
    class APIEnumPointType(Enum):
        """
        Members Include: <OnSurface> <OnAnchor> <OnCenter> <OnTop>
        """
        OnSurface: int
        OnAnchor: int
        OnCenter: int
        OnTop: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PointSubFeatureBuilder.APIEnumPointType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) AssociatedPointTag
    ##   the property represents associated point tag.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return NXOpen.Point
    @property
    def AssociatedPointTag(self) -> NXOpen.Point:
        """
        Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) AssociatedPointTag
          the property represents associated point tag.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) AssociatedPointTag

    ##   the property represents associated point tag.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @AssociatedPointTag.setter
    def AssociatedPointTag(self, associatedPointTag: NXOpen.Point):
        """
        Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) AssociatedPointTag
          the property represents associated point tag.  
             
         
        """
        pass
    
    ## Getter for property: (@link PointSubFeatureBuilder.APIEnumPointType NXOpen.Vsa.PointSubFeatureBuilder.APIEnumPointType@endlink) PointSubFeatureType
    ##   the property represents  point subfeature type.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return PointSubFeatureBuilder.APIEnumPointType
    @property
    def PointSubFeatureType(self) -> PointSubFeatureBuilder.APIEnumPointType:
        """
        Getter for property: (@link PointSubFeatureBuilder.APIEnumPointType NXOpen.Vsa.PointSubFeatureBuilder.APIEnumPointType@endlink) PointSubFeatureType
          the property represents  point subfeature type.  
             
         
        """
        pass
    
    ## Setter for property: (@link PointSubFeatureBuilder.APIEnumPointType NXOpen.Vsa.PointSubFeatureBuilder.APIEnumPointType@endlink) PointSubFeatureType

    ##   the property represents  point subfeature type.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @PointSubFeatureType.setter
    def PointSubFeatureType(self, pointSubFeatureType: PointSubFeatureBuilder.APIEnumPointType):
        """
        Setter for property: (@link PointSubFeatureBuilder.APIEnumPointType NXOpen.Vsa.PointSubFeatureBuilder.APIEnumPointType@endlink) PointSubFeatureType
          the property represents  point subfeature type.  
             
         
        """
        pass
    
    ## Getter for property: (str) StringDescription
    ##   the property represents  point subfeature discription.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return str
    @property
    def StringDescription(self) -> str:
        """
        Getter for property: (str) StringDescription
          the property represents  point subfeature discription.  
             
         
        """
        pass
    
    ## Setter for property: (str) StringDescription

    ##   the property represents  point subfeature discription.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @StringDescription.setter
    def StringDescription(self, stringDescription: str):
        """
        Setter for property: (str) StringDescription
          the property represents  point subfeature discription.  
             
         
        """
        pass
    
    ## Getter for property: (str) StringName
    ##   the property represents  point subfeature name.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return str
    @property
    def StringName(self) -> str:
        """
        Getter for property: (str) StringName
          the property represents  point subfeature name.  
             
         
        """
        pass
    
    ## Setter for property: (str) StringName

    ##   the property represents  point subfeature name.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @StringName.setter
    def StringName(self, stringName: str):
        """
        Setter for property: (str) StringName
          the property represents  point subfeature name.  
             
         
        """
        pass
    
import NXOpen
##  Represents a Point Sub feature  <br> To create or edit an instance of this class, use @link NXOpen::Vsa::PointSubFeatureBuilder  NXOpen::Vsa::PointSubFeatureBuilder @endlink  <br> 
## 
##  <br>  Usable only on Windows <br>  
## 
##   <br>  Created in NX11.0.0  <br> 

class PointSubFeature(NXOpen.NXObject): 
    """ Represents a Point Sub feature """
    pass


import NXOpen
## 
##     
##      <br> To create a new instance of this class, use @link NXOpen::Vsa::VsaManager::CreateProjectPointsBuilder  NXOpen::Vsa::VsaManager::CreateProjectPointsBuilder @endlink  <br> 
## 
##  <br>  Usable only on Windows <br>  
## 
##   <br>  Created in NX2206.0.0  <br> 

class ProjectPointsBuilder(NXOpen.Builder): 
    """
    
    """
    pass


import NXOpen
## 
##     
##      <br> To create a new instance of this class, use @link NXOpen::Vsa::VsaManager::CreateSimulationPreferencesBuilder  NXOpen::Vsa::VsaManager::CreateSimulationPreferencesBuilder @endlink  <br> 
## 
##  <br>  Usable only on Windows <br>  
## 
##   <br>  Created in NX1899.0.0  <br> 

class SimulationPreferencesBuilder(NXOpen.Builder): 
    """
    
    """


    ## 
    ##         
    ##         
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Normal</term><description> 
    ## </description> </item><item><term> 
    ## Uniform</term><description> 
    ## </description> </item><item><term> 
    ## Extreme</term><description> 
    ## </description> </item></list>
    class APIEnumDistributionFloatType(Enum):
        """
        Members Include: <Normal> <Uniform> <Extreme>
        """
        Normal: int
        Uniform: int
        Extreme: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SimulationPreferencesBuilder.APIEnumDistributionFloatType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (bool) AcceptInterferenceBuild
    ##   the property represents AcceptInterferenceBuild.  
    ##      
    ##  
    ## Getter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return bool
    @property
    def AcceptInterferenceBuild(self) -> bool:
        """
        Getter for property: (bool) AcceptInterferenceBuild
          the property represents AcceptInterferenceBuild.  
             
         
        """
        pass
    
    ## Setter for property: (bool) AcceptInterferenceBuild

    ##   the property represents AcceptInterferenceBuild.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @AcceptInterferenceBuild.setter
    def AcceptInterferenceBuild(self, acceptInterferenceBuild: bool):
        """
        Setter for property: (bool) AcceptInterferenceBuild
          the property represents AcceptInterferenceBuild.  
             
         
        """
        pass
    
    ## Getter for property: (bool) AnimateSimulation
    ##   the property represents Animate Simulation flag.  
    ##      
    ##  
    ## Getter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return bool
    @property
    def AnimateSimulation(self) -> bool:
        """
        Getter for property: (bool) AnimateSimulation
          the property represents Animate Simulation flag.  
             
         
        """
        pass
    
    ## Setter for property: (bool) AnimateSimulation

    ##   the property represents Animate Simulation flag.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @AnimateSimulation.setter
    def AnimateSimulation(self, animateSimulation: bool):
        """
        Setter for property: (bool) AnimateSimulation
          the property represents Animate Simulation flag.  
             
         
        """
        pass
    
    ## Getter for property: (int) AnimationDelay
    ##   the property represents Animation Delay.  
    ##      
    ##  
    ## Getter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return int
    @property
    def AnimationDelay(self) -> int:
        """
        Getter for property: (int) AnimationDelay
          the property represents Animation Delay.  
             
         
        """
        pass
    
    ## Setter for property: (int) AnimationDelay

    ##   the property represents Animation Delay.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @AnimationDelay.setter
    def AnimationDelay(self, animateDelay: int):
        """
        Setter for property: (int) AnimationDelay
          the property represents Animation Delay.  
             
         
        """
        pass
    
    ## Getter for property: (bool) Cp
    ##   the property represents  Cp.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return bool
    @property
    def Cp(self) -> bool:
        """
        Getter for property: (bool) Cp
          the property represents  Cp.  
             
         
        """
        pass
    
    ## Setter for property: (bool) Cp

    ##   the property represents  Cp.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @Cp.setter
    def Cp(self, cp: bool):
        """
        Setter for property: (bool) Cp
          the property represents  Cp.  
             
         
        """
        pass
    
    ## Getter for property: (bool) Cpk
    ##   the property represents  Cpk.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return bool
    @property
    def Cpk(self) -> bool:
        """
        Getter for property: (bool) Cpk
          the property represents  Cpk.  
             
         
        """
        pass
    
    ## Setter for property: (bool) Cpk

    ##   the property represents  Cpk.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @Cpk.setter
    def Cpk(self, cpk: bool):
        """
        Setter for property: (bool) Cpk
          the property represents  Cpk.  
             
         
        """
        pass
    
    ## Getter for property: (float) CutoffPercent
    ##   the property represents  CutoffPercent.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def CutoffPercent(self) -> float:
        """
        Getter for property: (float) CutoffPercent
          the property represents  CutoffPercent.  
             
         
        """
        pass
    
    ## Setter for property: (float) CutoffPercent

    ##   the property represents  CutoffPercent.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @CutoffPercent.setter
    def CutoffPercent(self, cutoffPercent: float):
        """
        Setter for property: (float) CutoffPercent
          the property represents  CutoffPercent.  
             
         
        """
        pass
    
    ## Getter for property: (int) DecimalPlaces
    ##   the property represents  DecimalPlaces.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return int
    @property
    def DecimalPlaces(self) -> int:
        """
        Getter for property: (int) DecimalPlaces
          the property represents  DecimalPlaces.  
             
         
        """
        pass
    
    ## Setter for property: (int) DecimalPlaces

    ##   the property represents  DecimalPlaces.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @DecimalPlaces.setter
    def DecimalPlaces(self, decimalPlaces: int):
        """
        Setter for property: (int) DecimalPlaces
          the property represents  DecimalPlaces.  
             
         
        """
        pass
    
    ## Getter for property: (@link SimulationPreferencesBuilder.APIEnumDistributionFloatType NXOpen.Vsa.SimulationPreferencesBuilder.APIEnumDistributionFloatType@endlink) DistributionFloatType
    ##   the enum  Float Type.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return SimulationPreferencesBuilder.APIEnumDistributionFloatType
    @property
    def DistributionFloatType(self) -> SimulationPreferencesBuilder.APIEnumDistributionFloatType:
        """
        Getter for property: (@link SimulationPreferencesBuilder.APIEnumDistributionFloatType NXOpen.Vsa.SimulationPreferencesBuilder.APIEnumDistributionFloatType@endlink) DistributionFloatType
          the enum  Float Type.  
             
         
        """
        pass
    
    ## Setter for property: (@link SimulationPreferencesBuilder.APIEnumDistributionFloatType NXOpen.Vsa.SimulationPreferencesBuilder.APIEnumDistributionFloatType@endlink) DistributionFloatType

    ##   the enum  Float Type.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @DistributionFloatType.setter
    def DistributionFloatType(self, distributionFloatType: SimulationPreferencesBuilder.APIEnumDistributionFloatType):
        """
        Setter for property: (@link SimulationPreferencesBuilder.APIEnumDistributionFloatType NXOpen.Vsa.SimulationPreferencesBuilder.APIEnumDistributionFloatType@endlink) DistributionFloatType
          the enum  Float Type.  
             
         
        """
        pass
    
    ## Getter for property: (bool) EstimatedHigh
    ##   the property represents  EstimatedHigh.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return bool
    @property
    def EstimatedHigh(self) -> bool:
        """
        Getter for property: (bool) EstimatedHigh
          the property represents  EstimatedHigh.  
             
         
        """
        pass
    
    ## Setter for property: (bool) EstimatedHigh

    ##   the property represents  EstimatedHigh.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @EstimatedHigh.setter
    def EstimatedHigh(self, estimatedHigh: bool):
        """
        Setter for property: (bool) EstimatedHigh
          the property represents  EstimatedHigh.  
             
         
        """
        pass
    
    ## Getter for property: (bool) EstimatedLow
    ##   the property represents  EstimatedLow.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return bool
    @property
    def EstimatedLow(self) -> bool:
        """
        Getter for property: (bool) EstimatedLow
          the property represents  EstimatedLow.  
             
         
        """
        pass
    
    ## Setter for property: (bool) EstimatedLow

    ##   the property represents  EstimatedLow.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @EstimatedLow.setter
    def EstimatedLow(self, estimatedLow: bool):
        """
        Setter for property: (bool) EstimatedLow
          the property represents  EstimatedLow.  
             
         
        """
        pass
    
    ## Getter for property: (bool) EstimatedPercentAboveUpperSpec
    ##   the property represents  EstimatedPercentAboveUpperSpec.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return bool
    @property
    def EstimatedPercentAboveUpperSpec(self) -> bool:
        """
        Getter for property: (bool) EstimatedPercentAboveUpperSpec
          the property represents  EstimatedPercentAboveUpperSpec.  
             
         
        """
        pass
    
    ## Setter for property: (bool) EstimatedPercentAboveUpperSpec

    ##   the property represents  EstimatedPercentAboveUpperSpec.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @EstimatedPercentAboveUpperSpec.setter
    def EstimatedPercentAboveUpperSpec(self, estimatedPercentAboveUpperSpec: bool):
        """
        Setter for property: (bool) EstimatedPercentAboveUpperSpec
          the property represents  EstimatedPercentAboveUpperSpec.  
             
         
        """
        pass
    
    ## Getter for property: (bool) EstimatedPercentBelowLowerSpec
    ##   the property represents  EstimatedPercentBelowLowerSpec.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return bool
    @property
    def EstimatedPercentBelowLowerSpec(self) -> bool:
        """
        Getter for property: (bool) EstimatedPercentBelowLowerSpec
          the property represents  EstimatedPercentBelowLowerSpec.  
             
         
        """
        pass
    
    ## Setter for property: (bool) EstimatedPercentBelowLowerSpec

    ##   the property represents  EstimatedPercentBelowLowerSpec.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @EstimatedPercentBelowLowerSpec.setter
    def EstimatedPercentBelowLowerSpec(self, estimatedPercentBelowLowerSpec: bool):
        """
        Setter for property: (bool) EstimatedPercentBelowLowerSpec
          the property represents  EstimatedPercentBelowLowerSpec.  
             
         
        """
        pass
    
    ## Getter for property: (bool) EstimatedPercentOutOfSpec
    ##   the property represents  EstimatedPercentOutOfSpec.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return bool
    @property
    def EstimatedPercentOutOfSpec(self) -> bool:
        """
        Getter for property: (bool) EstimatedPercentOutOfSpec
          the property represents  EstimatedPercentOutOfSpec.  
             
         
        """
        pass
    
    ## Setter for property: (bool) EstimatedPercentOutOfSpec

    ##   the property represents  EstimatedPercentOutOfSpec.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @EstimatedPercentOutOfSpec.setter
    def EstimatedPercentOutOfSpec(self, estimatedPercentOutOfSpec: bool):
        """
        Setter for property: (bool) EstimatedPercentOutOfSpec
          the property represents  EstimatedPercentOutOfSpec.  
             
         
        """
        pass
    
    ## Getter for property: (bool) EstimatedRange
    ##   the property represents  EstimatedRange.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return bool
    @property
    def EstimatedRange(self) -> bool:
        """
        Getter for property: (bool) EstimatedRange
          the property represents  EstimatedRange.  
             
         
        """
        pass
    
    ## Setter for property: (bool) EstimatedRange

    ##   the property represents  EstimatedRange.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @EstimatedRange.setter
    def EstimatedRange(self, estimatedRange: bool):
        """
        Setter for property: (bool) EstimatedRange
          the property represents  EstimatedRange.  
             
         
        """
        pass
    
    ## Getter for property: (bool) HLMSimulation
    ##   the property represents  HLM Simulation flag.  
    ##      
    ##  
    ## Getter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return bool
    @property
    def HLMSimulation(self) -> bool:
        """
        Getter for property: (bool) HLMSimulation
          the property represents  HLM Simulation flag.  
             
         
        """
        pass
    
    ## Setter for property: (bool) HLMSimulation

    ##   the property represents  HLM Simulation flag.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @HLMSimulation.setter
    def HLMSimulation(self, hlmSimulation: bool):
        """
        Setter for property: (bool) HLMSimulation
          the property represents  HLM Simulation flag.  
             
         
        """
        pass
    
    ## Getter for property: (int) MaxAngleTangency
    ##   the property represents  Max Angle Tangency.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return int
    @property
    def MaxAngleTangency(self) -> int:
        """
        Getter for property: (int) MaxAngleTangency
          the property represents  Max Angle Tangency.  
             
         
        """
        pass
    
    ## Setter for property: (int) MaxAngleTangency

    ##   the property represents  Max Angle Tangency.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @MaxAngleTangency.setter
    def MaxAngleTangency(self, maxAngleTangency: int):
        """
        Setter for property: (int) MaxAngleTangency
          the property represents  Max Angle Tangency.  
             
         
        """
        pass
    
    ## Getter for property: (float) MaxOffsetMating
    ##   the property represents  Max Offset for Mating.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def MaxOffsetMating(self) -> float:
        """
        Getter for property: (float) MaxOffsetMating
          the property represents  Max Offset for Mating.  
             
         
        """
        pass
    
    ## Setter for property: (float) MaxOffsetMating

    ##   the property represents  Max Offset for Mating.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @MaxOffsetMating.setter
    def MaxOffsetMating(self, maxOffsetMating: float):
        """
        Setter for property: (float) MaxOffsetMating
          the property represents  Max Offset for Mating.  
             
         
        """
        pass
    
    ## Getter for property: (bool) Mean
    ##   the property represents  Mean.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return bool
    @property
    def Mean(self) -> bool:
        """
        Getter for property: (bool) Mean
          the property represents  Mean.  
             
         
        """
        pass
    
    ## Setter for property: (bool) Mean

    ##   the property represents  Mean.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @Mean.setter
    def Mean(self, nominal: bool):
        """
        Setter for property: (bool) Mean
          the property represents  Mean.  
             
         
        """
        pass
    
    ## Getter for property: (int) NoOfMontecarlo
    ##   the property represents  No Of Montecarlo.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return int
    @property
    def NoOfMontecarlo(self) -> int:
        """
        Getter for property: (int) NoOfMontecarlo
          the property represents  No Of Montecarlo.  
             
         
        """
        pass
    
    ## Setter for property: (int) NoOfMontecarlo

    ##   the property represents  No Of Montecarlo.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @NoOfMontecarlo.setter
    def NoOfMontecarlo(self, noOfMontecarlo: int):
        """
        Setter for property: (int) NoOfMontecarlo
          the property represents  No Of Montecarlo.  
             
         
        """
        pass
    
    ## Getter for property: (bool) Nominal
    ##   the property represents  Nominal.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return bool
    @property
    def Nominal(self) -> bool:
        """
        Getter for property: (bool) Nominal
          the property represents  Nominal.  
             
         
        """
        pass
    
    ## Setter for property: (bool) Nominal

    ##   the property represents  Nominal.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @Nominal.setter
    def Nominal(self, nominal: bool):
        """
        Setter for property: (bool) Nominal
          the property represents  Nominal.  
             
         
        """
        pass
    
    ## Getter for property: (bool) SampleHigh
    ##   the property represents  SampleHigh.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return bool
    @property
    def SampleHigh(self) -> bool:
        """
        Getter for property: (bool) SampleHigh
          the property represents  SampleHigh.  
             
         
        """
        pass
    
    ## Setter for property: (bool) SampleHigh

    ##   the property represents  SampleHigh.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @SampleHigh.setter
    def SampleHigh(self, sampleHigh: bool):
        """
        Setter for property: (bool) SampleHigh
          the property represents  SampleHigh.  
             
         
        """
        pass
    
    ## Getter for property: (bool) SampleLow
    ##   the property represents  SampleLow.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return bool
    @property
    def SampleLow(self) -> bool:
        """
        Getter for property: (bool) SampleLow
          the property represents  SampleLow.  
             
         
        """
        pass
    
    ## Setter for property: (bool) SampleLow

    ##   the property represents  SampleLow.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @SampleLow.setter
    def SampleLow(self, sampleLow: bool):
        """
        Setter for property: (bool) SampleLow
          the property represents  SampleLow.  
             
         
        """
        pass
    
    ## Getter for property: (bool) SampleRange
    ##   the property represents  SampleRange.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return bool
    @property
    def SampleRange(self) -> bool:
        """
        Getter for property: (bool) SampleRange
          the property represents  SampleRange.  
             
         
        """
        pass
    
    ## Setter for property: (bool) SampleRange

    ##   the property represents  SampleRange.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @SampleRange.setter
    def SampleRange(self, sampleRange: bool):
        """
        Setter for property: (bool) SampleRange
          the property represents  SampleRange.  
             
         
        """
        pass
    
    ## Getter for property: (int) SigmaRange
    ##   the property represents  Sigma Range.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return int
    @property
    def SigmaRange(self) -> int:
        """
        Getter for property: (int) SigmaRange
          the property represents  Sigma Range.  
             
         
        """
        pass
    
    ## Setter for property: (int) SigmaRange

    ##   the property represents  Sigma Range.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @SigmaRange.setter
    def SigmaRange(self, sigmaRange: int):
        """
        Setter for property: (int) SigmaRange
          the property represents  Sigma Range.  
             
         
        """
        pass
    
    ## Getter for property: (bool) StandardDeviation
    ##   the property represents  StandardDeviation.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return bool
    @property
    def StandardDeviation(self) -> bool:
        """
        Getter for property: (bool) StandardDeviation
          the property represents  StandardDeviation.  
             
         
        """
        pass
    
    ## Setter for property: (bool) StandardDeviation

    ##   the property represents  StandardDeviation.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @StandardDeviation.setter
    def StandardDeviation(self, standardDeviation: bool):
        """
        Setter for property: (bool) StandardDeviation
          the property represents  StandardDeviation.  
             
         
        """
        pass
    
import NXOpen
## 
##     
##      <br> To create a new instance of this class, use @link NXOpen::Vsa::VsaManager::CreateSlotFeatureBuilder  NXOpen::Vsa::VsaManager::CreateSlotFeatureBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## DoubleKurtosisForm </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleKurtosisLoc </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleKurtosisSize </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleSkewnessForm </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleSkewnessLoc </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleSkewnessSize </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## EnumForm </term> <description> 
##  
## Normal </description> </item> 
## 
## <item><term> 
##  
## EnumLoc </term> <description> 
##  
## Normal </description> </item> 
## 
## <item><term> 
##  
## EnumSize </term> <description> 
##  
## Normal </description> </item> 
## 
## </list> 

## 
##  <br>  Usable only on Windows <br>  
## 
##   <br>  Created in NX1899.0.0  <br> 

class SlotFeatureBuilder(NXOpen.Builder): 
    """
    
    """


    ## 
    ##         
    ##         
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Normal</term><description> 
    ## </description> </item><item><term> 
    ## Uniform</term><description> 
    ## </description> </item><item><term> 
    ## Extreme</term><description> 
    ## </description> </item><item><term> 
    ## Pearson</term><description> 
    ## </description> </item><item><term> 
    ## Trapeziodal</term><description> 
    ## </description> </item></list>
    class APIEnumForm(Enum):
        """
        Members Include: <Normal> <Uniform> <Extreme> <Pearson> <Trapeziodal>
        """
        Normal: int
        Uniform: int
        Extreme: int
        Pearson: int
        Trapeziodal: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SlotFeatureBuilder.APIEnumForm:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## 
    ##         
    ##         
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Normal</term><description> 
    ## </description> </item><item><term> 
    ## Uniform</term><description> 
    ## </description> </item><item><term> 
    ## Extreme</term><description> 
    ## </description> </item><item><term> 
    ## Pearson</term><description> 
    ## </description> </item><item><term> 
    ## Trapeziodal</term><description> 
    ## </description> </item></list>
    class APIEnumLoc(Enum):
        """
        Members Include: <Normal> <Uniform> <Extreme> <Pearson> <Trapeziodal>
        """
        Normal: int
        Uniform: int
        Extreme: int
        Pearson: int
        Trapeziodal: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SlotFeatureBuilder.APIEnumLoc:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## 
    ##         
    ##         
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Normal</term><description> 
    ## </description> </item><item><term> 
    ## Uniform</term><description> 
    ## </description> </item><item><term> 
    ## Extreme</term><description> 
    ## </description> </item><item><term> 
    ## Pearson</term><description> 
    ## </description> </item><item><term> 
    ## Trapeziodal</term><description> 
    ## </description> </item></list>
    class APIEnumSize(Enum):
        """
        Members Include: <Normal> <Uniform> <Extreme> <Pearson> <Trapeziodal>
        """
        Normal: int
        Uniform: int
        Extreme: int
        Pearson: int
        Trapeziodal: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SlotFeatureBuilder.APIEnumSize:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (float) DoubleAnchorX
    ##   the property represents  X value of anchor.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def DoubleAnchorX(self) -> float:
        """
        Getter for property: (float) DoubleAnchorX
          the property represents  X value of anchor.  
             
         
        """
        pass
    
    ## Setter for property: (float) DoubleAnchorX

    ##   the property represents  X value of anchor.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @DoubleAnchorX.setter
    def DoubleAnchorX(self, doubleAnchorX: float):
        """
        Setter for property: (float) DoubleAnchorX
          the property represents  X value of anchor.  
             
         
        """
        pass
    
    ## Getter for property: (float) DoubleAnchorY
    ##   the property represents  Y value of anchor.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def DoubleAnchorY(self) -> float:
        """
        Getter for property: (float) DoubleAnchorY
          the property represents  Y value of anchor.  
             
         
        """
        pass
    
    ## Setter for property: (float) DoubleAnchorY

    ##   the property represents  Y value of anchor.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @DoubleAnchorY.setter
    def DoubleAnchorY(self, doubleAnchorY: float):
        """
        Setter for property: (float) DoubleAnchorY
          the property represents  Y value of anchor.  
             
         
        """
        pass
    
    ## Getter for property: (float) DoubleAnchorZ
    ##   the property represents  Z value of anchor.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def DoubleAnchorZ(self) -> float:
        """
        Getter for property: (float) DoubleAnchorZ
          the property represents  Z value of anchor.  
             
         
        """
        pass
    
    ## Setter for property: (float) DoubleAnchorZ

    ##   the property represents  Z value of anchor.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @DoubleAnchorZ.setter
    def DoubleAnchorZ(self, doubleAnchorZ: float):
        """
        Setter for property: (float) DoubleAnchorZ
          the property represents  Z value of anchor.  
             
         
        """
        pass
    
    ## Getter for property: (float) DoubleDepth
    ##   the property represents  depth of slot.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def DoubleDepth(self) -> float:
        """
        Getter for property: (float) DoubleDepth
          the property represents  depth of slot.  
             
         
        """
        pass
    
    ## Setter for property: (float) DoubleDepth

    ##   the property represents  depth of slot.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @DoubleDepth.setter
    def DoubleDepth(self, height: float):
        """
        Setter for property: (float) DoubleDepth
          the property represents  depth of slot.  
             
         
        """
        pass
    
    ## Getter for property: (float) DoubleDirectionI
    ##   the property represents  X value of normal.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def DoubleDirectionI(self) -> float:
        """
        Getter for property: (float) DoubleDirectionI
          the property represents  X value of normal.  
             
         
        """
        pass
    
    ## Setter for property: (float) DoubleDirectionI

    ##   the property represents  X value of normal.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @DoubleDirectionI.setter
    def DoubleDirectionI(self, doubleDirectionI: float):
        """
        Setter for property: (float) DoubleDirectionI
          the property represents  X value of normal.  
             
         
        """
        pass
    
    ## Getter for property: (float) DoubleDirectionJ
    ##   the property represents  Y value of normal.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def DoubleDirectionJ(self) -> float:
        """
        Getter for property: (float) DoubleDirectionJ
          the property represents  Y value of normal.  
             
         
        """
        pass
    
    ## Setter for property: (float) DoubleDirectionJ

    ##   the property represents  Y value of normal.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @DoubleDirectionJ.setter
    def DoubleDirectionJ(self, doubleDirectionJ: float):
        """
        Setter for property: (float) DoubleDirectionJ
          the property represents  Y value of normal.  
             
         
        """
        pass
    
    ## Getter for property: (float) DoubleDirectionK
    ##   the property represents  Z value of normal.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def DoubleDirectionK(self) -> float:
        """
        Getter for property: (float) DoubleDirectionK
          the property represents  Z value of normal.  
             
         
        """
        pass
    
    ## Setter for property: (float) DoubleDirectionK

    ##   the property represents  Z value of normal.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @DoubleDirectionK.setter
    def DoubleDirectionK(self, doubleDirectionK: float):
        """
        Setter for property: (float) DoubleDirectionK
          the property represents  Z value of normal.  
             
         
        """
        pass
    
    ## Getter for property: (float) DoubleKurtosisForm
    ##   the property represents  Form distribution Kurtosis.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def DoubleKurtosisForm(self) -> float:
        """
        Getter for property: (float) DoubleKurtosisForm
          the property represents  Form distribution Kurtosis.  
             
         
        """
        pass
    
    ## Setter for property: (float) DoubleKurtosisForm

    ##   the property represents  Form distribution Kurtosis.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @DoubleKurtosisForm.setter
    def DoubleKurtosisForm(self, doubleKurtosisForm: float):
        """
        Setter for property: (float) DoubleKurtosisForm
          the property represents  Form distribution Kurtosis.  
             
         
        """
        pass
    
    ## Getter for property: (float) DoubleKurtosisLoc
    ##   the property represents  Loc distribution Kurtosis.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def DoubleKurtosisLoc(self) -> float:
        """
        Getter for property: (float) DoubleKurtosisLoc
          the property represents  Loc distribution Kurtosis.  
             
         
        """
        pass
    
    ## Setter for property: (float) DoubleKurtosisLoc

    ##   the property represents  Loc distribution Kurtosis.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @DoubleKurtosisLoc.setter
    def DoubleKurtosisLoc(self, doubleKurtosisLoc: float):
        """
        Setter for property: (float) DoubleKurtosisLoc
          the property represents  Loc distribution Kurtosis.  
             
         
        """
        pass
    
    ## Getter for property: (float) DoubleKurtosisSize
    ##   the property represents  Size distribution Kurtosis.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def DoubleKurtosisSize(self) -> float:
        """
        Getter for property: (float) DoubleKurtosisSize
          the property represents  Size distribution Kurtosis.  
             
         
        """
        pass
    
    ## Setter for property: (float) DoubleKurtosisSize

    ##   the property represents  Size distribution Kurtosis.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @DoubleKurtosisSize.setter
    def DoubleKurtosisSize(self, doubleKurtosisSize: float):
        """
        Setter for property: (float) DoubleKurtosisSize
          the property represents  Size distribution Kurtosis.  
             
         
        """
        pass
    
    ## Getter for property: (float) DoubleLength
    ##   the property represents  length of slot.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def DoubleLength(self) -> float:
        """
        Getter for property: (float) DoubleLength
          the property represents  length of slot.  
             
         
        """
        pass
    
    ## Setter for property: (float) DoubleLength

    ##   the property represents  length of slot.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @DoubleLength.setter
    def DoubleLength(self, distance: float):
        """
        Setter for property: (float) DoubleLength
          the property represents  length of slot.  
             
         
        """
        pass
    
    ## Getter for property: (float) DoubleLengthVectorI
    ##   the property represents  X value of length vector.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def DoubleLengthVectorI(self) -> float:
        """
        Getter for property: (float) DoubleLengthVectorI
          the property represents  X value of length vector.  
             
         
        """
        pass
    
    ## Setter for property: (float) DoubleLengthVectorI

    ##   the property represents  X value of length vector.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @DoubleLengthVectorI.setter
    def DoubleLengthVectorI(self, doubleLengthVectorI: float):
        """
        Setter for property: (float) DoubleLengthVectorI
          the property represents  X value of length vector.  
             
         
        """
        pass
    
    ## Getter for property: (float) DoubleLengthVectorJ
    ##   the property represents  Y value of length vector.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def DoubleLengthVectorJ(self) -> float:
        """
        Getter for property: (float) DoubleLengthVectorJ
          the property represents  Y value of length vector.  
             
         
        """
        pass
    
    ## Setter for property: (float) DoubleLengthVectorJ

    ##   the property represents  Y value of length vector.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @DoubleLengthVectorJ.setter
    def DoubleLengthVectorJ(self, doubleLengthVectorJ: float):
        """
        Setter for property: (float) DoubleLengthVectorJ
          the property represents  Y value of length vector.  
             
         
        """
        pass
    
    ## Getter for property: (float) DoubleLengthVectorK
    ##   the property represents  Z value of length vector.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def DoubleLengthVectorK(self) -> float:
        """
        Getter for property: (float) DoubleLengthVectorK
          the property represents  Z value of length vector.  
             
         
        """
        pass
    
    ## Setter for property: (float) DoubleLengthVectorK

    ##   the property represents  Z value of length vector.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @DoubleLengthVectorK.setter
    def DoubleLengthVectorK(self, doubleLengthVectorK: float):
        """
        Setter for property: (float) DoubleLengthVectorK
          the property represents  Z value of length vector.  
             
         
        """
        pass
    
    ## Getter for property: (float) DoubleSkewnessForm
    ##   the property represents  Form distribution Skewness.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def DoubleSkewnessForm(self) -> float:
        """
        Getter for property: (float) DoubleSkewnessForm
          the property represents  Form distribution Skewness.  
             
         
        """
        pass
    
    ## Setter for property: (float) DoubleSkewnessForm

    ##   the property represents  Form distribution Skewness.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @DoubleSkewnessForm.setter
    def DoubleSkewnessForm(self, doubleSkewnessForm: float):
        """
        Setter for property: (float) DoubleSkewnessForm
          the property represents  Form distribution Skewness.  
             
         
        """
        pass
    
    ## Getter for property: (float) DoubleSkewnessLoc
    ##   the property represents  Loc distribution Skewness.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def DoubleSkewnessLoc(self) -> float:
        """
        Getter for property: (float) DoubleSkewnessLoc
          the property represents  Loc distribution Skewness.  
             
         
        """
        pass
    
    ## Setter for property: (float) DoubleSkewnessLoc

    ##   the property represents  Loc distribution Skewness.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @DoubleSkewnessLoc.setter
    def DoubleSkewnessLoc(self, doubleSkewnessLoc: float):
        """
        Setter for property: (float) DoubleSkewnessLoc
          the property represents  Loc distribution Skewness.  
             
         
        """
        pass
    
    ## Getter for property: (float) DoubleSkewnessSize
    ##   the property represents  Size distribution Skewness.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def DoubleSkewnessSize(self) -> float:
        """
        Getter for property: (float) DoubleSkewnessSize
          the property represents  Size distribution Skewness.  
             
         
        """
        pass
    
    ## Setter for property: (float) DoubleSkewnessSize

    ##   the property represents  Size distribution Skewness.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @DoubleSkewnessSize.setter
    def DoubleSkewnessSize(self, doubleSkewnessSize: float):
        """
        Setter for property: (float) DoubleSkewnessSize
          the property represents  Size distribution Skewness.  
             
         
        """
        pass
    
    ## Getter for property: (float) DoubleWidth
    ##   the property represents  width of slot.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def DoubleWidth(self) -> float:
        """
        Getter for property: (float) DoubleWidth
          the property represents  width of slot.  
             
         
        """
        pass
    
    ## Setter for property: (float) DoubleWidth

    ##   the property represents  width of slot.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @DoubleWidth.setter
    def DoubleWidth(self, width: float):
        """
        Setter for property: (float) DoubleWidth
          the property represents  width of slot.  
             
         
        """
        pass
    
    ## Getter for property: (@link SlotFeatureBuilder.APIEnumForm NXOpen.Vsa.SlotFeatureBuilder.APIEnumForm@endlink) EnumForm
    ##   the property represents  Form distribution type.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return SlotFeatureBuilder.APIEnumForm
    @property
    def EnumForm(self) -> SlotFeatureBuilder.APIEnumForm:
        """
        Getter for property: (@link SlotFeatureBuilder.APIEnumForm NXOpen.Vsa.SlotFeatureBuilder.APIEnumForm@endlink) EnumForm
          the property represents  Form distribution type.  
             
         
        """
        pass
    
    ## Setter for property: (@link SlotFeatureBuilder.APIEnumForm NXOpen.Vsa.SlotFeatureBuilder.APIEnumForm@endlink) EnumForm

    ##   the property represents  Form distribution type.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @EnumForm.setter
    def EnumForm(self, enumForm: SlotFeatureBuilder.APIEnumForm):
        """
        Setter for property: (@link SlotFeatureBuilder.APIEnumForm NXOpen.Vsa.SlotFeatureBuilder.APIEnumForm@endlink) EnumForm
          the property represents  Form distribution type.  
             
         
        """
        pass
    
    ## Getter for property: (@link SlotFeatureBuilder.APIEnumLoc NXOpen.Vsa.SlotFeatureBuilder.APIEnumLoc@endlink) EnumLoc
    ##   the property represents  Loc distribution type.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return SlotFeatureBuilder.APIEnumLoc
    @property
    def EnumLoc(self) -> SlotFeatureBuilder.APIEnumLoc:
        """
        Getter for property: (@link SlotFeatureBuilder.APIEnumLoc NXOpen.Vsa.SlotFeatureBuilder.APIEnumLoc@endlink) EnumLoc
          the property represents  Loc distribution type.  
             
         
        """
        pass
    
    ## Setter for property: (@link SlotFeatureBuilder.APIEnumLoc NXOpen.Vsa.SlotFeatureBuilder.APIEnumLoc@endlink) EnumLoc

    ##   the property represents  Loc distribution type.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @EnumLoc.setter
    def EnumLoc(self, enumLoc: SlotFeatureBuilder.APIEnumLoc):
        """
        Setter for property: (@link SlotFeatureBuilder.APIEnumLoc NXOpen.Vsa.SlotFeatureBuilder.APIEnumLoc@endlink) EnumLoc
          the property represents  Loc distribution type.  
             
         
        """
        pass
    
    ## Getter for property: (@link SlotFeatureBuilder.APIEnumSize NXOpen.Vsa.SlotFeatureBuilder.APIEnumSize@endlink) EnumSize
    ##   the property represents  Size distribution type.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return SlotFeatureBuilder.APIEnumSize
    @property
    def EnumSize(self) -> SlotFeatureBuilder.APIEnumSize:
        """
        Getter for property: (@link SlotFeatureBuilder.APIEnumSize NXOpen.Vsa.SlotFeatureBuilder.APIEnumSize@endlink) EnumSize
          the property represents  Size distribution type.  
             
         
        """
        pass
    
    ## Setter for property: (@link SlotFeatureBuilder.APIEnumSize NXOpen.Vsa.SlotFeatureBuilder.APIEnumSize@endlink) EnumSize

    ##   the property represents  Size distribution type.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @EnumSize.setter
    def EnumSize(self, enumSize: SlotFeatureBuilder.APIEnumSize):
        """
        Setter for property: (@link SlotFeatureBuilder.APIEnumSize NXOpen.Vsa.SlotFeatureBuilder.APIEnumSize@endlink) EnumSize
          the property represents  Size distribution type.  
             
         
        """
        pass
    
    ## Getter for property: (str) StringDescription
    ##   the property represents  slot feature discription.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return str
    @property
    def StringDescription(self) -> str:
        """
        Getter for property: (str) StringDescription
          the property represents  slot feature discription.  
             
         
        """
        pass
    
    ## Setter for property: (str) StringDescription

    ##   the property represents  slot feature discription.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @StringDescription.setter
    def StringDescription(self, stringDescription: str):
        """
        Setter for property: (str) StringDescription
          the property represents  slot feature discription.  
             
         
        """
        pass
    
    ## Getter for property: (str) StringName
    ##   the property represents  slot feature name.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return str
    @property
    def StringName(self) -> str:
        """
        Getter for property: (str) StringName
          the property represents  slot feature name.  
             
         
        """
        pass
    
    ## Setter for property: (str) StringName

    ##   the property represents  slot feature name.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @StringName.setter
    def StringName(self, stringName: str):
        """
        Setter for property: (str) StringName
          the property represents  slot feature name.  
             
         
        """
        pass
    
    ## Getter for property: (bool) ToggleSwap
    ##   the property represents  value of swap length and depth.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return bool
    @property
    def ToggleSwap(self) -> bool:
        """
        Getter for property: (bool) ToggleSwap
          the property represents  value of swap length and depth.  
             
         
        """
        pass
    
    ## Setter for property: (bool) ToggleSwap

    ##   the property represents  value of swap length and depth.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @ToggleSwap.setter
    def ToggleSwap(self, boolSwap: bool):
        """
        Setter for property: (bool) ToggleSwap
          the property represents  value of swap length and depth.  
             
         
        """
        pass
    
import NXOpen
##  Represents a Slot feature  <br> To create or edit an instance of this class, use @link NXOpen::Vsa::SlotFeatureBuilder  NXOpen::Vsa::SlotFeatureBuilder @endlink  <br> 
## 
##  <br>  Usable only on Windows <br>  
## 
##   <br>  Created in NX1899.0.0  <br> 

class SlotFeature(NXOpen.NXObject): 
    """ Represents a Slot feature """
    pass


import NXOpen
## 
##     
##      <br> To create a new instance of this class, use @link NXOpen::Vsa::VsaManager::CreateSocketFeatureBuilder  NXOpen::Vsa::VsaManager::CreateSocketFeatureBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## DoubleAnchorX </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleAnchorY </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleAnchorZ </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleDiameter </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleKurtosisForm </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleKurtosisLoc </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleKurtosisSize </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleSkewnessForm </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleSkewnessLoc </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleSkewnessSize </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## EnumForm </term> <description> 
##  
## Normal </description> </item> 
## 
## <item><term> 
##  
## EnumLoc </term> <description> 
##  
## Normal </description> </item> 
## 
## </list> 

## 
##  <br>  Usable only on Windows <br>  
## 
##   <br>  Created in NX2306.0.0  <br> 

class SocketFeatureBuilder(NXOpen.Builder): 
    """
    
    """


    ## 
    ##         
    ##         
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Normal</term><description> 
    ## </description> </item><item><term> 
    ## Uniform</term><description> 
    ## </description> </item><item><term> 
    ## Extreme</term><description> 
    ## </description> </item><item><term> 
    ## Pearson</term><description> 
    ## </description> </item><item><term> 
    ## Trapeziodal</term><description> 
    ## </description> </item></list>
    class APIEnumForm(Enum):
        """
        Members Include: <Normal> <Uniform> <Extreme> <Pearson> <Trapeziodal>
        """
        Normal: int
        Uniform: int
        Extreme: int
        Pearson: int
        Trapeziodal: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SocketFeatureBuilder.APIEnumForm:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## 
    ##         
    ##         
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Normal</term><description> 
    ## </description> </item><item><term> 
    ## Uniform</term><description> 
    ## </description> </item><item><term> 
    ## Extreme</term><description> 
    ## </description> </item><item><term> 
    ## Pearson</term><description> 
    ## </description> </item><item><term> 
    ## Trapeziodal</term><description> 
    ## </description> </item></list>
    class APIEnumLoc(Enum):
        """
        Members Include: <Normal> <Uniform> <Extreme> <Pearson> <Trapeziodal>
        """
        Normal: int
        Uniform: int
        Extreme: int
        Pearson: int
        Trapeziodal: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SocketFeatureBuilder.APIEnumLoc:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## 
    ##         
    ##         
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Normal</term><description> 
    ## </description> </item><item><term> 
    ## Uniform</term><description> 
    ## </description> </item><item><term> 
    ## Extreme</term><description> 
    ## </description> </item><item><term> 
    ## Pearson</term><description> 
    ## </description> </item><item><term> 
    ## Trapeziodal</term><description> 
    ## </description> </item></list>
    class APIEnumSize(Enum):
        """
        Members Include: <Normal> <Uniform> <Extreme> <Pearson> <Trapeziodal>
        """
        Normal: int
        Uniform: int
        Extreme: int
        Pearson: int
        Trapeziodal: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SocketFeatureBuilder.APIEnumSize:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (float) DoubleAnchorX
    ##   the double anchor x   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return float
    @property
    def DoubleAnchorX(self) -> float:
        """
        Getter for property: (float) DoubleAnchorX
          the double anchor x   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleAnchorX

    ##   the double anchor x   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @DoubleAnchorX.setter
    def DoubleAnchorX(self, doubleAnchorX: float):
        """
        Setter for property: (float) DoubleAnchorX
          the double anchor x   
            
         
        """
        pass
    
    ## Getter for property: (float) DoubleAnchorY
    ##   the double anchor y   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return float
    @property
    def DoubleAnchorY(self) -> float:
        """
        Getter for property: (float) DoubleAnchorY
          the double anchor y   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleAnchorY

    ##   the double anchor y   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @DoubleAnchorY.setter
    def DoubleAnchorY(self, doubleAnchorY: float):
        """
        Setter for property: (float) DoubleAnchorY
          the double anchor y   
            
         
        """
        pass
    
    ## Getter for property: (float) DoubleAnchorZ
    ##   the double anchor z   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return float
    @property
    def DoubleAnchorZ(self) -> float:
        """
        Getter for property: (float) DoubleAnchorZ
          the double anchor z   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleAnchorZ

    ##   the double anchor z   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @DoubleAnchorZ.setter
    def DoubleAnchorZ(self, doubleAnchorZ: float):
        """
        Setter for property: (float) DoubleAnchorZ
          the double anchor z   
            
         
        """
        pass
    
    ## Getter for property: (float) DoubleDiameter
    ##   the double diameter   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return float
    @property
    def DoubleDiameter(self) -> float:
        """
        Getter for property: (float) DoubleDiameter
          the double diameter   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleDiameter

    ##   the double diameter   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @DoubleDiameter.setter
    def DoubleDiameter(self, doubleDiameter: float):
        """
        Setter for property: (float) DoubleDiameter
          the double diameter   
            
         
        """
        pass
    
    ## Getter for property: (float) DoubleKurtosisForm
    ##   the double kurtosis form   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return float
    @property
    def DoubleKurtosisForm(self) -> float:
        """
        Getter for property: (float) DoubleKurtosisForm
          the double kurtosis form   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleKurtosisForm

    ##   the double kurtosis form   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @DoubleKurtosisForm.setter
    def DoubleKurtosisForm(self, doubleKurtosisForm: float):
        """
        Setter for property: (float) DoubleKurtosisForm
          the double kurtosis form   
            
         
        """
        pass
    
    ## Getter for property: (float) DoubleKurtosisLoc
    ##   the double kurtosis loc   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return float
    @property
    def DoubleKurtosisLoc(self) -> float:
        """
        Getter for property: (float) DoubleKurtosisLoc
          the double kurtosis loc   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleKurtosisLoc

    ##   the double kurtosis loc   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @DoubleKurtosisLoc.setter
    def DoubleKurtosisLoc(self, doubleKurtosisLoc: float):
        """
        Setter for property: (float) DoubleKurtosisLoc
          the double kurtosis loc   
            
         
        """
        pass
    
    ## Getter for property: (float) DoubleKurtosisSize
    ##   the double kurtosis size   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return float
    @property
    def DoubleKurtosisSize(self) -> float:
        """
        Getter for property: (float) DoubleKurtosisSize
          the double kurtosis size   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleKurtosisSize

    ##   the double kurtosis size   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @DoubleKurtosisSize.setter
    def DoubleKurtosisSize(self, doubleKurtosisSize: float):
        """
        Setter for property: (float) DoubleKurtosisSize
          the double kurtosis size   
            
         
        """
        pass
    
    ## Getter for property: (float) DoubleSkewnessForm
    ##   the double skewness form   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return float
    @property
    def DoubleSkewnessForm(self) -> float:
        """
        Getter for property: (float) DoubleSkewnessForm
          the double skewness form   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleSkewnessForm

    ##   the double skewness form   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @DoubleSkewnessForm.setter
    def DoubleSkewnessForm(self, doubleSkewnessForm: float):
        """
        Setter for property: (float) DoubleSkewnessForm
          the double skewness form   
            
         
        """
        pass
    
    ## Getter for property: (float) DoubleSkewnessLoc
    ##   the double skewness loc   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return float
    @property
    def DoubleSkewnessLoc(self) -> float:
        """
        Getter for property: (float) DoubleSkewnessLoc
          the double skewness loc   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleSkewnessLoc

    ##   the double skewness loc   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @DoubleSkewnessLoc.setter
    def DoubleSkewnessLoc(self, doubleSkewnessLoc: float):
        """
        Setter for property: (float) DoubleSkewnessLoc
          the double skewness loc   
            
         
        """
        pass
    
    ## Getter for property: (float) DoubleSkewnessSize
    ##   the double skewness size   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return float
    @property
    def DoubleSkewnessSize(self) -> float:
        """
        Getter for property: (float) DoubleSkewnessSize
          the double skewness size   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleSkewnessSize

    ##   the double skewness size   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @DoubleSkewnessSize.setter
    def DoubleSkewnessSize(self, doubleSkewnessSize: float):
        """
        Setter for property: (float) DoubleSkewnessSize
          the double skewness size   
            
         
        """
        pass
    
    ## Getter for property: (@link SocketFeatureBuilder.APIEnumForm NXOpen.Vsa.SocketFeatureBuilder.APIEnumForm@endlink) EnumForm
    ##   the enum form   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return SocketFeatureBuilder.APIEnumForm
    @property
    def EnumForm(self) -> SocketFeatureBuilder.APIEnumForm:
        """
        Getter for property: (@link SocketFeatureBuilder.APIEnumForm NXOpen.Vsa.SocketFeatureBuilder.APIEnumForm@endlink) EnumForm
          the enum form   
            
         
        """
        pass
    
    ## Setter for property: (@link SocketFeatureBuilder.APIEnumForm NXOpen.Vsa.SocketFeatureBuilder.APIEnumForm@endlink) EnumForm

    ##   the enum form   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @EnumForm.setter
    def EnumForm(self, enumForm: SocketFeatureBuilder.APIEnumForm):
        """
        Setter for property: (@link SocketFeatureBuilder.APIEnumForm NXOpen.Vsa.SocketFeatureBuilder.APIEnumForm@endlink) EnumForm
          the enum form   
            
         
        """
        pass
    
    ## Getter for property: (@link SocketFeatureBuilder.APIEnumLoc NXOpen.Vsa.SocketFeatureBuilder.APIEnumLoc@endlink) EnumLoc
    ##   the enum loc   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return SocketFeatureBuilder.APIEnumLoc
    @property
    def EnumLoc(self) -> SocketFeatureBuilder.APIEnumLoc:
        """
        Getter for property: (@link SocketFeatureBuilder.APIEnumLoc NXOpen.Vsa.SocketFeatureBuilder.APIEnumLoc@endlink) EnumLoc
          the enum loc   
            
         
        """
        pass
    
    ## Setter for property: (@link SocketFeatureBuilder.APIEnumLoc NXOpen.Vsa.SocketFeatureBuilder.APIEnumLoc@endlink) EnumLoc

    ##   the enum loc   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @EnumLoc.setter
    def EnumLoc(self, enumLoc: SocketFeatureBuilder.APIEnumLoc):
        """
        Setter for property: (@link SocketFeatureBuilder.APIEnumLoc NXOpen.Vsa.SocketFeatureBuilder.APIEnumLoc@endlink) EnumLoc
          the enum loc   
            
         
        """
        pass
    
    ## Getter for property: (@link SocketFeatureBuilder.APIEnumSize NXOpen.Vsa.SocketFeatureBuilder.APIEnumSize@endlink) EnumSize
    ##   the enum size   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return SocketFeatureBuilder.APIEnumSize
    @property
    def EnumSize(self) -> SocketFeatureBuilder.APIEnumSize:
        """
        Getter for property: (@link SocketFeatureBuilder.APIEnumSize NXOpen.Vsa.SocketFeatureBuilder.APIEnumSize@endlink) EnumSize
          the enum size   
            
         
        """
        pass
    
    ## Setter for property: (@link SocketFeatureBuilder.APIEnumSize NXOpen.Vsa.SocketFeatureBuilder.APIEnumSize@endlink) EnumSize

    ##   the enum size   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @EnumSize.setter
    def EnumSize(self, enumSize: SocketFeatureBuilder.APIEnumSize):
        """
        Setter for property: (@link SocketFeatureBuilder.APIEnumSize NXOpen.Vsa.SocketFeatureBuilder.APIEnumSize@endlink) EnumSize
          the enum size   
            
         
        """
        pass
    
    ## Getter for property: (str) StringDescription
    ##   the string description   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return str
    @property
    def StringDescription(self) -> str:
        """
        Getter for property: (str) StringDescription
          the string description   
            
         
        """
        pass
    
    ## Setter for property: (str) StringDescription

    ##   the string description   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @StringDescription.setter
    def StringDescription(self, stringDescription: str):
        """
        Setter for property: (str) StringDescription
          the string description   
            
         
        """
        pass
    
    ## Getter for property: (str) StringName
    ##   the string name   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return str
    @property
    def StringName(self) -> str:
        """
        Getter for property: (str) StringName
          the string name   
            
         
        """
        pass
    
    ## Setter for property: (str) StringName

    ##   the string name   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @StringName.setter
    def StringName(self, stringName: str):
        """
        Setter for property: (str) StringName
          the string name   
            
         
        """
        pass
    
import NXOpen
##  Represents a Socket feature  <br> To create or edit an instance of this class, use @link NXOpen::Vsa::SocketFeatureBuilder  NXOpen::Vsa::SocketFeatureBuilder @endlink  <br> 
## 
##  <br>  Usable only on Windows <br>  
## 
##   <br>  Created in NX2306.0.0  <br> 

class SocketFeature(NXOpen.NXObject): 
    """ Represents a Socket feature """
    pass


import NXOpen
## 
##     
##      <br> To create a new instance of this class, use @link NXOpen::Vsa::VsaManager::CreateSlotFeatureBuilder  NXOpen::Vsa::VsaManager::CreateSlotFeatureBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## DoubleKurtosisForm </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleKurtosisLoc </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleKurtosisSize </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleSkewnessForm </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleSkewnessLoc </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleSkewnessSize </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## EnumForm </term> <description> 
##  
## Normal </description> </item> 
## 
## <item><term> 
##  
## EnumLoc </term> <description> 
##  
## Normal </description> </item> 
## 
## <item><term> 
##  
## EnumSize </term> <description> 
##  
## Normal </description> </item> 
## 
## </list> 

## 
##  <br>  Usable only on Windows <br>  
## 
##   <br>  Created in NX1899.0.0  <br> 

class TabFeatureBuilder(NXOpen.Builder): 
    """
    
    """


    ## 
    ##         
    ##         
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Normal</term><description> 
    ## </description> </item><item><term> 
    ## Uniform</term><description> 
    ## </description> </item><item><term> 
    ## Extreme</term><description> 
    ## </description> </item><item><term> 
    ## Pearson</term><description> 
    ## </description> </item><item><term> 
    ## Trapeziodal</term><description> 
    ## </description> </item></list>
    class APIEnumForm(Enum):
        """
        Members Include: <Normal> <Uniform> <Extreme> <Pearson> <Trapeziodal>
        """
        Normal: int
        Uniform: int
        Extreme: int
        Pearson: int
        Trapeziodal: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> TabFeatureBuilder.APIEnumForm:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## 
    ##         
    ##         
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Normal</term><description> 
    ## </description> </item><item><term> 
    ## Uniform</term><description> 
    ## </description> </item><item><term> 
    ## Extreme</term><description> 
    ## </description> </item><item><term> 
    ## Pearson</term><description> 
    ## </description> </item><item><term> 
    ## Trapeziodal</term><description> 
    ## </description> </item></list>
    class APIEnumLoc(Enum):
        """
        Members Include: <Normal> <Uniform> <Extreme> <Pearson> <Trapeziodal>
        """
        Normal: int
        Uniform: int
        Extreme: int
        Pearson: int
        Trapeziodal: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> TabFeatureBuilder.APIEnumLoc:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## 
    ##         
    ##         
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Normal</term><description> 
    ## </description> </item><item><term> 
    ## Uniform</term><description> 
    ## </description> </item><item><term> 
    ## Extreme</term><description> 
    ## </description> </item><item><term> 
    ## Pearson</term><description> 
    ## </description> </item><item><term> 
    ## Trapeziodal</term><description> 
    ## </description> </item></list>
    class APIEnumSize(Enum):
        """
        Members Include: <Normal> <Uniform> <Extreme> <Pearson> <Trapeziodal>
        """
        Normal: int
        Uniform: int
        Extreme: int
        Pearson: int
        Trapeziodal: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> TabFeatureBuilder.APIEnumSize:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (float) DoubleAnchorX
    ##   the property represents X value of anchor.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def DoubleAnchorX(self) -> float:
        """
        Getter for property: (float) DoubleAnchorX
          the property represents X value of anchor.  
             
         
        """
        pass
    
    ## Setter for property: (float) DoubleAnchorX

    ##   the property represents X value of anchor.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @DoubleAnchorX.setter
    def DoubleAnchorX(self, doubleAnchorX: float):
        """
        Setter for property: (float) DoubleAnchorX
          the property represents X value of anchor.  
             
         
        """
        pass
    
    ## Getter for property: (float) DoubleAnchorY
    ##   the property represents Y value of anchor.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def DoubleAnchorY(self) -> float:
        """
        Getter for property: (float) DoubleAnchorY
          the property represents Y value of anchor.  
             
         
        """
        pass
    
    ## Setter for property: (float) DoubleAnchorY

    ##   the property represents Y value of anchor.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @DoubleAnchorY.setter
    def DoubleAnchorY(self, doubleAnchorY: float):
        """
        Setter for property: (float) DoubleAnchorY
          the property represents Y value of anchor.  
             
         
        """
        pass
    
    ## Getter for property: (float) DoubleAnchorZ
    ##   the property represents Z value of anchor.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def DoubleAnchorZ(self) -> float:
        """
        Getter for property: (float) DoubleAnchorZ
          the property represents Z value of anchor.  
             
         
        """
        pass
    
    ## Setter for property: (float) DoubleAnchorZ

    ##   the property represents Z value of anchor.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @DoubleAnchorZ.setter
    def DoubleAnchorZ(self, doubleAnchorZ: float):
        """
        Setter for property: (float) DoubleAnchorZ
          the property represents Z value of anchor.  
             
         
        """
        pass
    
    ## Getter for property: (float) DoubleDepth
    ##   the property represents depth of tab.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def DoubleDepth(self) -> float:
        """
        Getter for property: (float) DoubleDepth
          the property represents depth of tab.  
             
         
        """
        pass
    
    ## Setter for property: (float) DoubleDepth

    ##   the property represents depth of tab.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @DoubleDepth.setter
    def DoubleDepth(self, height: float):
        """
        Setter for property: (float) DoubleDepth
          the property represents depth of tab.  
             
         
        """
        pass
    
    ## Getter for property: (float) DoubleDirectionI
    ##   the property represents X value of normal.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def DoubleDirectionI(self) -> float:
        """
        Getter for property: (float) DoubleDirectionI
          the property represents X value of normal.  
             
         
        """
        pass
    
    ## Setter for property: (float) DoubleDirectionI

    ##   the property represents X value of normal.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @DoubleDirectionI.setter
    def DoubleDirectionI(self, doubleDirectionI: float):
        """
        Setter for property: (float) DoubleDirectionI
          the property represents X value of normal.  
             
         
        """
        pass
    
    ## Getter for property: (float) DoubleDirectionJ
    ##   the property represents Y value of normal.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def DoubleDirectionJ(self) -> float:
        """
        Getter for property: (float) DoubleDirectionJ
          the property represents Y value of normal.  
             
         
        """
        pass
    
    ## Setter for property: (float) DoubleDirectionJ

    ##   the property represents Y value of normal.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @DoubleDirectionJ.setter
    def DoubleDirectionJ(self, doubleDirectionJ: float):
        """
        Setter for property: (float) DoubleDirectionJ
          the property represents Y value of normal.  
             
         
        """
        pass
    
    ## Getter for property: (float) DoubleDirectionK
    ##   the property represents Z value of normal.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def DoubleDirectionK(self) -> float:
        """
        Getter for property: (float) DoubleDirectionK
          the property represents Z value of normal.  
             
         
        """
        pass
    
    ## Setter for property: (float) DoubleDirectionK

    ##   the property represents Z value of normal.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @DoubleDirectionK.setter
    def DoubleDirectionK(self, doubleDirectionK: float):
        """
        Setter for property: (float) DoubleDirectionK
          the property represents Z value of normal.  
             
         
        """
        pass
    
    ## Getter for property: (float) DoubleKurtosisForm
    ##   the property represents Form distribution Kurtosis.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def DoubleKurtosisForm(self) -> float:
        """
        Getter for property: (float) DoubleKurtosisForm
          the property represents Form distribution Kurtosis.  
             
         
        """
        pass
    
    ## Setter for property: (float) DoubleKurtosisForm

    ##   the property represents Form distribution Kurtosis.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @DoubleKurtosisForm.setter
    def DoubleKurtosisForm(self, doubleKurtosisForm: float):
        """
        Setter for property: (float) DoubleKurtosisForm
          the property represents Form distribution Kurtosis.  
             
         
        """
        pass
    
    ## Getter for property: (float) DoubleKurtosisLoc
    ##   the property represents Loc distribution Kurtosis.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def DoubleKurtosisLoc(self) -> float:
        """
        Getter for property: (float) DoubleKurtosisLoc
          the property represents Loc distribution Kurtosis.  
             
         
        """
        pass
    
    ## Setter for property: (float) DoubleKurtosisLoc

    ##   the property represents Loc distribution Kurtosis.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @DoubleKurtosisLoc.setter
    def DoubleKurtosisLoc(self, doubleKurtosisLoc: float):
        """
        Setter for property: (float) DoubleKurtosisLoc
          the property represents Loc distribution Kurtosis.  
             
         
        """
        pass
    
    ## Getter for property: (float) DoubleKurtosisSize
    ##   the property represents Size distribution Kurtosis.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def DoubleKurtosisSize(self) -> float:
        """
        Getter for property: (float) DoubleKurtosisSize
          the property represents Size distribution Kurtosis.  
             
         
        """
        pass
    
    ## Setter for property: (float) DoubleKurtosisSize

    ##   the property represents Size distribution Kurtosis.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @DoubleKurtosisSize.setter
    def DoubleKurtosisSize(self, doubleKurtosisSize: float):
        """
        Setter for property: (float) DoubleKurtosisSize
          the property represents Size distribution Kurtosis.  
             
         
        """
        pass
    
    ## Getter for property: (float) DoubleLength
    ##   the property represents length of tab.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def DoubleLength(self) -> float:
        """
        Getter for property: (float) DoubleLength
          the property represents length of tab.  
             
         
        """
        pass
    
    ## Setter for property: (float) DoubleLength

    ##   the property represents length of tab.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @DoubleLength.setter
    def DoubleLength(self, distance: float):
        """
        Setter for property: (float) DoubleLength
          the property represents length of tab.  
             
         
        """
        pass
    
    ## Getter for property: (float) DoubleLengthVectorI
    ##   the property represents X value of length vector.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def DoubleLengthVectorI(self) -> float:
        """
        Getter for property: (float) DoubleLengthVectorI
          the property represents X value of length vector.  
             
         
        """
        pass
    
    ## Setter for property: (float) DoubleLengthVectorI

    ##   the property represents X value of length vector.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @DoubleLengthVectorI.setter
    def DoubleLengthVectorI(self, doubleLengthVectorI: float):
        """
        Setter for property: (float) DoubleLengthVectorI
          the property represents X value of length vector.  
             
         
        """
        pass
    
    ## Getter for property: (float) DoubleLengthVectorJ
    ##   the property represents Y value of length vector.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def DoubleLengthVectorJ(self) -> float:
        """
        Getter for property: (float) DoubleLengthVectorJ
          the property represents Y value of length vector.  
             
         
        """
        pass
    
    ## Setter for property: (float) DoubleLengthVectorJ

    ##   the property represents Y value of length vector.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @DoubleLengthVectorJ.setter
    def DoubleLengthVectorJ(self, doubleLengthVectorJ: float):
        """
        Setter for property: (float) DoubleLengthVectorJ
          the property represents Y value of length vector.  
             
         
        """
        pass
    
    ## Getter for property: (float) DoubleLengthVectorK
    ##   the property represents Z value of length vector.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def DoubleLengthVectorK(self) -> float:
        """
        Getter for property: (float) DoubleLengthVectorK
          the property represents Z value of length vector.  
             
         
        """
        pass
    
    ## Setter for property: (float) DoubleLengthVectorK

    ##   the property represents Z value of length vector.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @DoubleLengthVectorK.setter
    def DoubleLengthVectorK(self, doubleLengthVectorK: float):
        """
        Setter for property: (float) DoubleLengthVectorK
          the property represents Z value of length vector.  
             
         
        """
        pass
    
    ## Getter for property: (float) DoubleSkewnessForm
    ##   the property represents Form distribution Skewness.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def DoubleSkewnessForm(self) -> float:
        """
        Getter for property: (float) DoubleSkewnessForm
          the property represents Form distribution Skewness.  
             
         
        """
        pass
    
    ## Setter for property: (float) DoubleSkewnessForm

    ##   the property represents Form distribution Skewness.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @DoubleSkewnessForm.setter
    def DoubleSkewnessForm(self, doubleSkewnessForm: float):
        """
        Setter for property: (float) DoubleSkewnessForm
          the property represents Form distribution Skewness.  
             
         
        """
        pass
    
    ## Getter for property: (float) DoubleSkewnessLoc
    ##   the property represents Loc distribution Skewness.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def DoubleSkewnessLoc(self) -> float:
        """
        Getter for property: (float) DoubleSkewnessLoc
          the property represents Loc distribution Skewness.  
             
         
        """
        pass
    
    ## Setter for property: (float) DoubleSkewnessLoc

    ##   the property represents Loc distribution Skewness.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @DoubleSkewnessLoc.setter
    def DoubleSkewnessLoc(self, doubleSkewnessLoc: float):
        """
        Setter for property: (float) DoubleSkewnessLoc
          the property represents Loc distribution Skewness.  
             
         
        """
        pass
    
    ## Getter for property: (float) DoubleSkewnessSize
    ##   the property represents Size distribution Skewness.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def DoubleSkewnessSize(self) -> float:
        """
        Getter for property: (float) DoubleSkewnessSize
          the property represents Size distribution Skewness.  
             
         
        """
        pass
    
    ## Setter for property: (float) DoubleSkewnessSize

    ##   the property represents Size distribution Skewness.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @DoubleSkewnessSize.setter
    def DoubleSkewnessSize(self, doubleSkewnessSize: float):
        """
        Setter for property: (float) DoubleSkewnessSize
          the property represents Size distribution Skewness.  
             
         
        """
        pass
    
    ## Getter for property: (float) DoubleWidth
    ##   the property represents width of tab.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def DoubleWidth(self) -> float:
        """
        Getter for property: (float) DoubleWidth
          the property represents width of tab.  
             
         
        """
        pass
    
    ## Setter for property: (float) DoubleWidth

    ##   the property represents width of tab.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @DoubleWidth.setter
    def DoubleWidth(self, height: float):
        """
        Setter for property: (float) DoubleWidth
          the property represents width of tab.  
             
         
        """
        pass
    
    ## Getter for property: (@link TabFeatureBuilder.APIEnumForm NXOpen.Vsa.TabFeatureBuilder.APIEnumForm@endlink) EnumForm
    ##   the property represents Form distribution type.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return TabFeatureBuilder.APIEnumForm
    @property
    def EnumForm(self) -> TabFeatureBuilder.APIEnumForm:
        """
        Getter for property: (@link TabFeatureBuilder.APIEnumForm NXOpen.Vsa.TabFeatureBuilder.APIEnumForm@endlink) EnumForm
          the property represents Form distribution type.  
             
         
        """
        pass
    
    ## Setter for property: (@link TabFeatureBuilder.APIEnumForm NXOpen.Vsa.TabFeatureBuilder.APIEnumForm@endlink) EnumForm

    ##   the property represents Form distribution type.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @EnumForm.setter
    def EnumForm(self, enumForm: TabFeatureBuilder.APIEnumForm):
        """
        Setter for property: (@link TabFeatureBuilder.APIEnumForm NXOpen.Vsa.TabFeatureBuilder.APIEnumForm@endlink) EnumForm
          the property represents Form distribution type.  
             
         
        """
        pass
    
    ## Getter for property: (@link TabFeatureBuilder.APIEnumLoc NXOpen.Vsa.TabFeatureBuilder.APIEnumLoc@endlink) EnumLoc
    ##   the property represents Loc distribution type.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return TabFeatureBuilder.APIEnumLoc
    @property
    def EnumLoc(self) -> TabFeatureBuilder.APIEnumLoc:
        """
        Getter for property: (@link TabFeatureBuilder.APIEnumLoc NXOpen.Vsa.TabFeatureBuilder.APIEnumLoc@endlink) EnumLoc
          the property represents Loc distribution type.  
             
         
        """
        pass
    
    ## Setter for property: (@link TabFeatureBuilder.APIEnumLoc NXOpen.Vsa.TabFeatureBuilder.APIEnumLoc@endlink) EnumLoc

    ##   the property represents Loc distribution type.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @EnumLoc.setter
    def EnumLoc(self, enumLoc: TabFeatureBuilder.APIEnumLoc):
        """
        Setter for property: (@link TabFeatureBuilder.APIEnumLoc NXOpen.Vsa.TabFeatureBuilder.APIEnumLoc@endlink) EnumLoc
          the property represents Loc distribution type.  
             
         
        """
        pass
    
    ## Getter for property: (@link TabFeatureBuilder.APIEnumSize NXOpen.Vsa.TabFeatureBuilder.APIEnumSize@endlink) EnumSize
    ##   the property represents Size distribution type.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return TabFeatureBuilder.APIEnumSize
    @property
    def EnumSize(self) -> TabFeatureBuilder.APIEnumSize:
        """
        Getter for property: (@link TabFeatureBuilder.APIEnumSize NXOpen.Vsa.TabFeatureBuilder.APIEnumSize@endlink) EnumSize
          the property represents Size distribution type.  
             
         
        """
        pass
    
    ## Setter for property: (@link TabFeatureBuilder.APIEnumSize NXOpen.Vsa.TabFeatureBuilder.APIEnumSize@endlink) EnumSize

    ##   the property represents Size distribution type.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @EnumSize.setter
    def EnumSize(self, enumSize: TabFeatureBuilder.APIEnumSize):
        """
        Setter for property: (@link TabFeatureBuilder.APIEnumSize NXOpen.Vsa.TabFeatureBuilder.APIEnumSize@endlink) EnumSize
          the property represents Size distribution type.  
             
         
        """
        pass
    
    ## Getter for property: (str) StringDescription
    ##   the property represents tab feature discription.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return str
    @property
    def StringDescription(self) -> str:
        """
        Getter for property: (str) StringDescription
          the property represents tab feature discription.  
             
         
        """
        pass
    
    ## Setter for property: (str) StringDescription

    ##   the property represents tab feature discription.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @StringDescription.setter
    def StringDescription(self, stringDescription: str):
        """
        Setter for property: (str) StringDescription
          the property represents tab feature discription.  
             
         
        """
        pass
    
    ## Getter for property: (str) StringName
    ##   the property represents tab feature name.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return str
    @property
    def StringName(self) -> str:
        """
        Getter for property: (str) StringName
          the property represents tab feature name.  
             
         
        """
        pass
    
    ## Setter for property: (str) StringName

    ##   the property represents tab feature name.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @StringName.setter
    def StringName(self, stringName: str):
        """
        Setter for property: (str) StringName
          the property represents tab feature name.  
             
         
        """
        pass
    
    ## Getter for property: (bool) ToggleSwap
    ##   the property represents value of swap length and depth.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return bool
    @property
    def ToggleSwap(self) -> bool:
        """
        Getter for property: (bool) ToggleSwap
          the property represents value of swap length and depth.  
             
         
        """
        pass
    
    ## Setter for property: (bool) ToggleSwap

    ##   the property represents value of swap length and depth.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @ToggleSwap.setter
    def ToggleSwap(self, boolSwap: bool):
        """
        Setter for property: (bool) ToggleSwap
          the property represents value of swap length and depth.  
             
         
        """
        pass
    
import NXOpen
##  Represents a Tab feature  <br> To create or edit an instance of this class, use @link NXOpen::Vsa::TabFeatureBuilder  NXOpen::Vsa::TabFeatureBuilder @endlink  <br> 
## 
##  <br>  Usable only on Windows <br>  
## 
##   <br>  Created in NX1899.0.0  <br> 

class TabFeature(NXOpen.NXObject): 
    """ Represents a Tab feature """
    pass


import NXOpen
## 
##     
##      <br> To create a new instance of this class, use @link NXOpen::Vsa::VsaManager::CreateTaperedHoleFeatureBuilder  NXOpen::Vsa::VsaManager::CreateTaperedHoleFeatureBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## DoubleAnchorX </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleAnchorY </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleAnchorZ </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleDiameter1 </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleDiameter2 </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleDirectionI </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleDirectionJ </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleDirectionK </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleHeight </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleKurtosisForm </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleKurtosisLoc </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleKurtosisSize </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleSkewnessForm </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleSkewnessLoc </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleSkewnessSize </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## EnumForm </term> <description> 
##  
## Normal </description> </item> 
## 
## <item><term> 
##  
## EnumLoc </term> <description> 
##  
## Normal </description> </item> 
## 
## <item><term> 
##  
## EnumSize </term> <description> 
##  
## Normal </description> </item> 
## 
## </list> 

## 
##  <br>  Usable only on Windows <br>  
## 
##   <br>  Created in NX1926.0.0  <br> 

class TaperedHoleFeatureBuilder(NXOpen.Builder): 
    """
    
    """


    ## 
    ##         
    ##         
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Normal</term><description> 
    ## </description> </item><item><term> 
    ## Uniform</term><description> 
    ## </description> </item><item><term> 
    ## Extreme</term><description> 
    ## </description> </item><item><term> 
    ## Pearson</term><description> 
    ## </description> </item><item><term> 
    ## Trapeziodal</term><description> 
    ## </description> </item></list>
    class APIEnumForm(Enum):
        """
        Members Include: <Normal> <Uniform> <Extreme> <Pearson> <Trapeziodal>
        """
        Normal: int
        Uniform: int
        Extreme: int
        Pearson: int
        Trapeziodal: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> TaperedHoleFeatureBuilder.APIEnumForm:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## 
    ##         
    ##         
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Normal</term><description> 
    ## </description> </item><item><term> 
    ## Uniform</term><description> 
    ## </description> </item><item><term> 
    ## Extreme</term><description> 
    ## </description> </item><item><term> 
    ## Pearson</term><description> 
    ## </description> </item><item><term> 
    ## Trapeziodal</term><description> 
    ## </description> </item></list>
    class APIEnumLoc(Enum):
        """
        Members Include: <Normal> <Uniform> <Extreme> <Pearson> <Trapeziodal>
        """
        Normal: int
        Uniform: int
        Extreme: int
        Pearson: int
        Trapeziodal: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> TaperedHoleFeatureBuilder.APIEnumLoc:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## 
    ##         
    ##         
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Normal</term><description> 
    ## </description> </item><item><term> 
    ## Uniform</term><description> 
    ## </description> </item><item><term> 
    ## Extreme</term><description> 
    ## </description> </item><item><term> 
    ## Pearson</term><description> 
    ## </description> </item><item><term> 
    ## Trapeziodal</term><description> 
    ## </description> </item></list>
    class APIEnumSize(Enum):
        """
        Members Include: <Normal> <Uniform> <Extreme> <Pearson> <Trapeziodal>
        """
        Normal: int
        Uniform: int
        Extreme: int
        Pearson: int
        Trapeziodal: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> TaperedHoleFeatureBuilder.APIEnumSize:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (float) DoubleAnchorX
    ##   the double anchor x   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def DoubleAnchorX(self) -> float:
        """
        Getter for property: (float) DoubleAnchorX
          the double anchor x   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleAnchorX

    ##   the double anchor x   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @DoubleAnchorX.setter
    def DoubleAnchorX(self, doubleAnchorX: float):
        """
        Setter for property: (float) DoubleAnchorX
          the double anchor x   
            
         
        """
        pass
    
    ## Getter for property: (float) DoubleAnchorY
    ##   the double anchor y   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def DoubleAnchorY(self) -> float:
        """
        Getter for property: (float) DoubleAnchorY
          the double anchor y   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleAnchorY

    ##   the double anchor y   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @DoubleAnchorY.setter
    def DoubleAnchorY(self, doubleAnchorY: float):
        """
        Setter for property: (float) DoubleAnchorY
          the double anchor y   
            
         
        """
        pass
    
    ## Getter for property: (float) DoubleAnchorZ
    ##   the double anchor z   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def DoubleAnchorZ(self) -> float:
        """
        Getter for property: (float) DoubleAnchorZ
          the double anchor z   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleAnchorZ

    ##   the double anchor z   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @DoubleAnchorZ.setter
    def DoubleAnchorZ(self, doubleAnchorZ: float):
        """
        Setter for property: (float) DoubleAnchorZ
          the double anchor z   
            
         
        """
        pass
    
    ## Getter for property: (float) DoubleDiameter1
    ##   the double diameter1   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def DoubleDiameter1(self) -> float:
        """
        Getter for property: (float) DoubleDiameter1
          the double diameter1   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleDiameter1

    ##   the double diameter1   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @DoubleDiameter1.setter
    def DoubleDiameter1(self, doubleDiameter1: float):
        """
        Setter for property: (float) DoubleDiameter1
          the double diameter1   
            
         
        """
        pass
    
    ## Getter for property: (float) DoubleDiameter2
    ##   the double diameter2   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def DoubleDiameter2(self) -> float:
        """
        Getter for property: (float) DoubleDiameter2
          the double diameter2   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleDiameter2

    ##   the double diameter2   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @DoubleDiameter2.setter
    def DoubleDiameter2(self, doubleDiameter2: float):
        """
        Setter for property: (float) DoubleDiameter2
          the double diameter2   
            
         
        """
        pass
    
    ## Getter for property: (float) DoubleDirectionI
    ##   the double direction i   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def DoubleDirectionI(self) -> float:
        """
        Getter for property: (float) DoubleDirectionI
          the double direction i   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleDirectionI

    ##   the double direction i   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @DoubleDirectionI.setter
    def DoubleDirectionI(self, doubleDirectionI: float):
        """
        Setter for property: (float) DoubleDirectionI
          the double direction i   
            
         
        """
        pass
    
    ## Getter for property: (float) DoubleDirectionJ
    ##   the double direction j   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def DoubleDirectionJ(self) -> float:
        """
        Getter for property: (float) DoubleDirectionJ
          the double direction j   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleDirectionJ

    ##   the double direction j   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @DoubleDirectionJ.setter
    def DoubleDirectionJ(self, doubleDirectionJ: float):
        """
        Setter for property: (float) DoubleDirectionJ
          the double direction j   
            
         
        """
        pass
    
    ## Getter for property: (float) DoubleDirectionK
    ##   the double direction k   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def DoubleDirectionK(self) -> float:
        """
        Getter for property: (float) DoubleDirectionK
          the double direction k   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleDirectionK

    ##   the double direction k   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @DoubleDirectionK.setter
    def DoubleDirectionK(self, doubleDirectionK: float):
        """
        Setter for property: (float) DoubleDirectionK
          the double direction k   
            
         
        """
        pass
    
    ## Getter for property: (float) DoubleHeight
    ##   the double height   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def DoubleHeight(self) -> float:
        """
        Getter for property: (float) DoubleHeight
          the double height   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleHeight

    ##   the double height   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @DoubleHeight.setter
    def DoubleHeight(self, doubleHeight: float):
        """
        Setter for property: (float) DoubleHeight
          the double height   
            
         
        """
        pass
    
    ## Getter for property: (float) DoubleKurtosisForm
    ##   the double kurtosis form   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def DoubleKurtosisForm(self) -> float:
        """
        Getter for property: (float) DoubleKurtosisForm
          the double kurtosis form   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleKurtosisForm

    ##   the double kurtosis form   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @DoubleKurtosisForm.setter
    def DoubleKurtosisForm(self, doubleKurtosisForm: float):
        """
        Setter for property: (float) DoubleKurtosisForm
          the double kurtosis form   
            
         
        """
        pass
    
    ## Getter for property: (float) DoubleKurtosisLoc
    ##   the double kurtosis loc   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def DoubleKurtosisLoc(self) -> float:
        """
        Getter for property: (float) DoubleKurtosisLoc
          the double kurtosis loc   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleKurtosisLoc

    ##   the double kurtosis loc   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @DoubleKurtosisLoc.setter
    def DoubleKurtosisLoc(self, doubleKurtosisLoc: float):
        """
        Setter for property: (float) DoubleKurtosisLoc
          the double kurtosis loc   
            
         
        """
        pass
    
    ## Getter for property: (float) DoubleKurtosisSize
    ##   the double kurtosis size   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def DoubleKurtosisSize(self) -> float:
        """
        Getter for property: (float) DoubleKurtosisSize
          the double kurtosis size   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleKurtosisSize

    ##   the double kurtosis size   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @DoubleKurtosisSize.setter
    def DoubleKurtosisSize(self, doubleKurtosisSize: float):
        """
        Setter for property: (float) DoubleKurtosisSize
          the double kurtosis size   
            
         
        """
        pass
    
    ## Getter for property: (float) DoubleSkewnessForm
    ##   the double skewness form   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def DoubleSkewnessForm(self) -> float:
        """
        Getter for property: (float) DoubleSkewnessForm
          the double skewness form   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleSkewnessForm

    ##   the double skewness form   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @DoubleSkewnessForm.setter
    def DoubleSkewnessForm(self, doubleSkewnessForm: float):
        """
        Setter for property: (float) DoubleSkewnessForm
          the double skewness form   
            
         
        """
        pass
    
    ## Getter for property: (float) DoubleSkewnessLoc
    ##   the double skewness loc   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def DoubleSkewnessLoc(self) -> float:
        """
        Getter for property: (float) DoubleSkewnessLoc
          the double skewness loc   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleSkewnessLoc

    ##   the double skewness loc   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @DoubleSkewnessLoc.setter
    def DoubleSkewnessLoc(self, doubleSkewnessLoc: float):
        """
        Setter for property: (float) DoubleSkewnessLoc
          the double skewness loc   
            
         
        """
        pass
    
    ## Getter for property: (float) DoubleSkewnessSize
    ##   the double skewness size   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def DoubleSkewnessSize(self) -> float:
        """
        Getter for property: (float) DoubleSkewnessSize
          the double skewness size   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleSkewnessSize

    ##   the double skewness size   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @DoubleSkewnessSize.setter
    def DoubleSkewnessSize(self, doubleSkewnessSize: float):
        """
        Setter for property: (float) DoubleSkewnessSize
          the double skewness size   
            
         
        """
        pass
    
    ## Getter for property: (@link TaperedHoleFeatureBuilder.APIEnumForm NXOpen.Vsa.TaperedHoleFeatureBuilder.APIEnumForm@endlink) EnumForm
    ##   the enum form   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return TaperedHoleFeatureBuilder.APIEnumForm
    @property
    def EnumForm(self) -> TaperedHoleFeatureBuilder.APIEnumForm:
        """
        Getter for property: (@link TaperedHoleFeatureBuilder.APIEnumForm NXOpen.Vsa.TaperedHoleFeatureBuilder.APIEnumForm@endlink) EnumForm
          the enum form   
            
         
        """
        pass
    
    ## Setter for property: (@link TaperedHoleFeatureBuilder.APIEnumForm NXOpen.Vsa.TaperedHoleFeatureBuilder.APIEnumForm@endlink) EnumForm

    ##   the enum form   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @EnumForm.setter
    def EnumForm(self, enumForm: TaperedHoleFeatureBuilder.APIEnumForm):
        """
        Setter for property: (@link TaperedHoleFeatureBuilder.APIEnumForm NXOpen.Vsa.TaperedHoleFeatureBuilder.APIEnumForm@endlink) EnumForm
          the enum form   
            
         
        """
        pass
    
    ## Getter for property: (@link TaperedHoleFeatureBuilder.APIEnumLoc NXOpen.Vsa.TaperedHoleFeatureBuilder.APIEnumLoc@endlink) EnumLoc
    ##   the enum loc   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return TaperedHoleFeatureBuilder.APIEnumLoc
    @property
    def EnumLoc(self) -> TaperedHoleFeatureBuilder.APIEnumLoc:
        """
        Getter for property: (@link TaperedHoleFeatureBuilder.APIEnumLoc NXOpen.Vsa.TaperedHoleFeatureBuilder.APIEnumLoc@endlink) EnumLoc
          the enum loc   
            
         
        """
        pass
    
    ## Setter for property: (@link TaperedHoleFeatureBuilder.APIEnumLoc NXOpen.Vsa.TaperedHoleFeatureBuilder.APIEnumLoc@endlink) EnumLoc

    ##   the enum loc   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @EnumLoc.setter
    def EnumLoc(self, enumLoc: TaperedHoleFeatureBuilder.APIEnumLoc):
        """
        Setter for property: (@link TaperedHoleFeatureBuilder.APIEnumLoc NXOpen.Vsa.TaperedHoleFeatureBuilder.APIEnumLoc@endlink) EnumLoc
          the enum loc   
            
         
        """
        pass
    
    ## Getter for property: (@link TaperedHoleFeatureBuilder.APIEnumSize NXOpen.Vsa.TaperedHoleFeatureBuilder.APIEnumSize@endlink) EnumSize
    ##   the enum size   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return TaperedHoleFeatureBuilder.APIEnumSize
    @property
    def EnumSize(self) -> TaperedHoleFeatureBuilder.APIEnumSize:
        """
        Getter for property: (@link TaperedHoleFeatureBuilder.APIEnumSize NXOpen.Vsa.TaperedHoleFeatureBuilder.APIEnumSize@endlink) EnumSize
          the enum size   
            
         
        """
        pass
    
    ## Setter for property: (@link TaperedHoleFeatureBuilder.APIEnumSize NXOpen.Vsa.TaperedHoleFeatureBuilder.APIEnumSize@endlink) EnumSize

    ##   the enum size   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @EnumSize.setter
    def EnumSize(self, enumSize: TaperedHoleFeatureBuilder.APIEnumSize):
        """
        Setter for property: (@link TaperedHoleFeatureBuilder.APIEnumSize NXOpen.Vsa.TaperedHoleFeatureBuilder.APIEnumSize@endlink) EnumSize
          the enum size   
            
         
        """
        pass
    
    ## Getter for property: (str) StringDescription
    ##   the string description   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return str
    @property
    def StringDescription(self) -> str:
        """
        Getter for property: (str) StringDescription
          the string description   
            
         
        """
        pass
    
    ## Setter for property: (str) StringDescription

    ##   the string description   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @StringDescription.setter
    def StringDescription(self, stringDescription: str):
        """
        Setter for property: (str) StringDescription
          the string description   
            
         
        """
        pass
    
    ## Getter for property: (str) StringName
    ##   the string name   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return str
    @property
    def StringName(self) -> str:
        """
        Getter for property: (str) StringName
          the string name   
            
         
        """
        pass
    
    ## Setter for property: (str) StringName

    ##   the string name   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @StringName.setter
    def StringName(self, stringName: str):
        """
        Setter for property: (str) StringName
          the string name   
            
         
        """
        pass
    
import NXOpen
##  Represents a Tapered Hole feature  <br> To create or edit an instance of this class, use @link NXOpen::Vsa::TaperedHoleFeatureBuilder  NXOpen::Vsa::TaperedHoleFeatureBuilder @endlink  <br> 
## 
##  <br>  Usable only on Windows <br>  
## 
##   <br>  Created in NX1926.0.0  <br> 

class TaperedHoleFeature(NXOpen.NXObject): 
    """ Represents a Tapered Hole feature """
    pass


import NXOpen
## 
##     
##      <br> To create a new instance of this class, use @link NXOpen::Vsa::VsaManager::CreateTaperedHolePatternFeatureBuilder  NXOpen::Vsa::VsaManager::CreateTaperedHolePatternFeatureBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## DoubleKurtosisForm </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleKurtosisLoc </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleKurtosisSize </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleSkewnessForm </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleSkewnessLoc </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleSkewnessSize </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## EnumForm </term> <description> 
##  
## Normal </description> </item> 
## 
## <item><term> 
##  
## EnumLoc </term> <description> 
##  
## Normal </description> </item> 
## 
## <item><term> 
##  
## EnumSize </term> <description> 
##  
## Normal </description> </item> 
## 
## </list> 

## 
##  <br>  Usable only on Windows <br>  
## 
##   <br>  Created in NX1926.0.0  <br> 

class TaperedHolePatternFeatureBuilder(NXOpen.Builder): 
    """
    
    """


    ## 
    ##         
    ##         
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Normal</term><description> 
    ## </description> </item><item><term> 
    ## Uniform</term><description> 
    ## </description> </item><item><term> 
    ## Extreme</term><description> 
    ## </description> </item><item><term> 
    ## Pearson</term><description> 
    ## </description> </item><item><term> 
    ## Trapeziodal</term><description> 
    ## </description> </item></list>
    class APIEnumForm(Enum):
        """
        Members Include: <Normal> <Uniform> <Extreme> <Pearson> <Trapeziodal>
        """
        Normal: int
        Uniform: int
        Extreme: int
        Pearson: int
        Trapeziodal: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> TaperedHolePatternFeatureBuilder.APIEnumForm:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## 
    ##         
    ##         
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Normal</term><description> 
    ## </description> </item><item><term> 
    ## Uniform</term><description> 
    ## </description> </item><item><term> 
    ## Extreme</term><description> 
    ## </description> </item><item><term> 
    ## Pearson</term><description> 
    ## </description> </item><item><term> 
    ## Trapeziodal</term><description> 
    ## </description> </item></list>
    class APIEnumLoc(Enum):
        """
        Members Include: <Normal> <Uniform> <Extreme> <Pearson> <Trapeziodal>
        """
        Normal: int
        Uniform: int
        Extreme: int
        Pearson: int
        Trapeziodal: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> TaperedHolePatternFeatureBuilder.APIEnumLoc:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## 
    ##         
    ##         
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Normal</term><description> 
    ## </description> </item><item><term> 
    ## Uniform</term><description> 
    ## </description> </item><item><term> 
    ## Extreme</term><description> 
    ## </description> </item><item><term> 
    ## Pearson</term><description> 
    ## </description> </item><item><term> 
    ## Trapeziodal</term><description> 
    ## </description> </item></list>
    class APIEnumSize(Enum):
        """
        Members Include: <Normal> <Uniform> <Extreme> <Pearson> <Trapeziodal>
        """
        Normal: int
        Uniform: int
        Extreme: int
        Pearson: int
        Trapeziodal: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> TaperedHolePatternFeatureBuilder.APIEnumSize:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (float) DoubleKurtosisForm
    ##   the double kurtosis form   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def DoubleKurtosisForm(self) -> float:
        """
        Getter for property: (float) DoubleKurtosisForm
          the double kurtosis form   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleKurtosisForm

    ##   the double kurtosis form   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @DoubleKurtosisForm.setter
    def DoubleKurtosisForm(self, doubleKurtosisForm: float):
        """
        Setter for property: (float) DoubleKurtosisForm
          the double kurtosis form   
            
         
        """
        pass
    
    ## Getter for property: (float) DoubleKurtosisLoc
    ##   the double kurtosis loc   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def DoubleKurtosisLoc(self) -> float:
        """
        Getter for property: (float) DoubleKurtosisLoc
          the double kurtosis loc   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleKurtosisLoc

    ##   the double kurtosis loc   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @DoubleKurtosisLoc.setter
    def DoubleKurtosisLoc(self, doubleKurtosisLoc: float):
        """
        Setter for property: (float) DoubleKurtosisLoc
          the double kurtosis loc   
            
         
        """
        pass
    
    ## Getter for property: (float) DoubleKurtosisSize
    ##   the double kurtosis size   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def DoubleKurtosisSize(self) -> float:
        """
        Getter for property: (float) DoubleKurtosisSize
          the double kurtosis size   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleKurtosisSize

    ##   the double kurtosis size   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @DoubleKurtosisSize.setter
    def DoubleKurtosisSize(self, doubleKurtosisSize: float):
        """
        Setter for property: (float) DoubleKurtosisSize
          the double kurtosis size   
            
         
        """
        pass
    
    ## Getter for property: (float) DoubleSkewnessForm
    ##   the double skewness form   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def DoubleSkewnessForm(self) -> float:
        """
        Getter for property: (float) DoubleSkewnessForm
          the double skewness form   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleSkewnessForm

    ##   the double skewness form   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @DoubleSkewnessForm.setter
    def DoubleSkewnessForm(self, doubleSkewnessForm: float):
        """
        Setter for property: (float) DoubleSkewnessForm
          the double skewness form   
            
         
        """
        pass
    
    ## Getter for property: (float) DoubleSkewnessLoc
    ##   the double skewness loc   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def DoubleSkewnessLoc(self) -> float:
        """
        Getter for property: (float) DoubleSkewnessLoc
          the double skewness loc   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleSkewnessLoc

    ##   the double skewness loc   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @DoubleSkewnessLoc.setter
    def DoubleSkewnessLoc(self, doubleSkewnessLoc: float):
        """
        Setter for property: (float) DoubleSkewnessLoc
          the double skewness loc   
            
         
        """
        pass
    
    ## Getter for property: (float) DoubleSkewnessSize
    ##   the double skewness size   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def DoubleSkewnessSize(self) -> float:
        """
        Getter for property: (float) DoubleSkewnessSize
          the double skewness size   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleSkewnessSize

    ##   the double skewness size   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @DoubleSkewnessSize.setter
    def DoubleSkewnessSize(self, doubleSkewnessSize: float):
        """
        Setter for property: (float) DoubleSkewnessSize
          the double skewness size   
            
         
        """
        pass
    
    ## Getter for property: (@link TaperedHolePatternFeatureBuilder.APIEnumForm NXOpen.Vsa.TaperedHolePatternFeatureBuilder.APIEnumForm@endlink) EnumForm
    ##   the enum form   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return TaperedHolePatternFeatureBuilder.APIEnumForm
    @property
    def EnumForm(self) -> TaperedHolePatternFeatureBuilder.APIEnumForm:
        """
        Getter for property: (@link TaperedHolePatternFeatureBuilder.APIEnumForm NXOpen.Vsa.TaperedHolePatternFeatureBuilder.APIEnumForm@endlink) EnumForm
          the enum form   
            
         
        """
        pass
    
    ## Setter for property: (@link TaperedHolePatternFeatureBuilder.APIEnumForm NXOpen.Vsa.TaperedHolePatternFeatureBuilder.APIEnumForm@endlink) EnumForm

    ##   the enum form   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @EnumForm.setter
    def EnumForm(self, enumForm: TaperedHolePatternFeatureBuilder.APIEnumForm):
        """
        Setter for property: (@link TaperedHolePatternFeatureBuilder.APIEnumForm NXOpen.Vsa.TaperedHolePatternFeatureBuilder.APIEnumForm@endlink) EnumForm
          the enum form   
            
         
        """
        pass
    
    ## Getter for property: (@link TaperedHolePatternFeatureBuilder.APIEnumLoc NXOpen.Vsa.TaperedHolePatternFeatureBuilder.APIEnumLoc@endlink) EnumLoc
    ##   the enum loc   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return TaperedHolePatternFeatureBuilder.APIEnumLoc
    @property
    def EnumLoc(self) -> TaperedHolePatternFeatureBuilder.APIEnumLoc:
        """
        Getter for property: (@link TaperedHolePatternFeatureBuilder.APIEnumLoc NXOpen.Vsa.TaperedHolePatternFeatureBuilder.APIEnumLoc@endlink) EnumLoc
          the enum loc   
            
         
        """
        pass
    
    ## Setter for property: (@link TaperedHolePatternFeatureBuilder.APIEnumLoc NXOpen.Vsa.TaperedHolePatternFeatureBuilder.APIEnumLoc@endlink) EnumLoc

    ##   the enum loc   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @EnumLoc.setter
    def EnumLoc(self, enumLoc: TaperedHolePatternFeatureBuilder.APIEnumLoc):
        """
        Setter for property: (@link TaperedHolePatternFeatureBuilder.APIEnumLoc NXOpen.Vsa.TaperedHolePatternFeatureBuilder.APIEnumLoc@endlink) EnumLoc
          the enum loc   
            
         
        """
        pass
    
    ## Getter for property: (@link TaperedHolePatternFeatureBuilder.APIEnumSize NXOpen.Vsa.TaperedHolePatternFeatureBuilder.APIEnumSize@endlink) EnumSize
    ##   the enum size   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return TaperedHolePatternFeatureBuilder.APIEnumSize
    @property
    def EnumSize(self) -> TaperedHolePatternFeatureBuilder.APIEnumSize:
        """
        Getter for property: (@link TaperedHolePatternFeatureBuilder.APIEnumSize NXOpen.Vsa.TaperedHolePatternFeatureBuilder.APIEnumSize@endlink) EnumSize
          the enum size   
            
         
        """
        pass
    
    ## Setter for property: (@link TaperedHolePatternFeatureBuilder.APIEnumSize NXOpen.Vsa.TaperedHolePatternFeatureBuilder.APIEnumSize@endlink) EnumSize

    ##   the enum size   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @EnumSize.setter
    def EnumSize(self, enumSize: TaperedHolePatternFeatureBuilder.APIEnumSize):
        """
        Setter for property: (@link TaperedHolePatternFeatureBuilder.APIEnumSize NXOpen.Vsa.TaperedHolePatternFeatureBuilder.APIEnumSize@endlink) EnumSize
          the enum size   
            
         
        """
        pass
    
    ## Getter for property: (int) NumInstanceCount
    ##   the enum size   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return int
    @property
    def NumInstanceCount(self) -> int:
        """
        Getter for property: (int) NumInstanceCount
          the enum size   
            
         
        """
        pass
    
    ## Setter for property: (int) NumInstanceCount

    ##   the enum size   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @NumInstanceCount.setter
    def NumInstanceCount(self, numInstanceCount: int):
        """
        Setter for property: (int) NumInstanceCount
          the enum size   
            
         
        """
        pass
    
    ## Getter for property: (str) StringDescription
    ##   the string description   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return str
    @property
    def StringDescription(self) -> str:
        """
        Getter for property: (str) StringDescription
          the string description   
            
         
        """
        pass
    
    ## Setter for property: (str) StringDescription

    ##   the string description   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @StringDescription.setter
    def StringDescription(self, stringDescription: str):
        """
        Setter for property: (str) StringDescription
          the string description   
            
         
        """
        pass
    
    ## Getter for property: (str) StringName
    ##   the string name   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return str
    @property
    def StringName(self) -> str:
        """
        Getter for property: (str) StringName
          the string name   
            
         
        """
        pass
    
    ## Setter for property: (str) StringName

    ##   the string name   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @StringName.setter
    def StringName(self, stringName: str):
        """
        Setter for property: (str) StringName
          the string name   
            
         
        """
        pass
    
import NXOpen
##  Represents a Hole pattern feature  <br> To create or edit an instance of this class, use @link NXOpen::Vsa::TaperedHolePatternFeatureBuilder  NXOpen::Vsa::TaperedHolePatternFeatureBuilder @endlink  <br> 
## 
##  <br>  Usable only on Windows <br>  
## 
##   <br>  Created in NX1899.0.0  <br> 

class TaperedHolePatternFeature(NXOpen.NXObject): 
    """ Represents a Hole pattern feature """
    pass


import NXOpen
## 
##     
##      <br> To create a new instance of this class, use @link NXOpen::Vsa::VsaManager::CreateTaperedPinFeatureBuilder  NXOpen::Vsa::VsaManager::CreateTaperedPinFeatureBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## DoubleAnchorX </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleAnchorY </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleAnchorZ </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleDiameter1 </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleDiameter2 </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleDirectionI </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleDirectionJ </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleDirectionK </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleHeight </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleKurtosisForm </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleKurtosisLoc </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleKurtosisSize </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleSkewnessForm </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleSkewnessLoc </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleSkewnessSize </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## EnumForm </term> <description> 
##  
## Normal </description> </item> 
## 
## <item><term> 
##  
## EnumLoc </term> <description> 
##  
## Normal </description> </item> 
## 
## <item><term> 
##  
## EnumSize </term> <description> 
##  
## Normal </description> </item> 
## 
## </list> 

## 
##  <br>  Usable only on Windows <br>  
## 
##   <br>  Created in NX1926.0.0  <br> 

class TaperedPinFeatureBuilder(NXOpen.Builder): 
    """
    
    """


    ## 
    ##         
    ##         
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Normal</term><description> 
    ## </description> </item><item><term> 
    ## Uniform</term><description> 
    ## </description> </item><item><term> 
    ## Extreme</term><description> 
    ## </description> </item><item><term> 
    ## Pearson</term><description> 
    ## </description> </item><item><term> 
    ## Trapeziodal</term><description> 
    ## </description> </item></list>
    class APIEnumForm(Enum):
        """
        Members Include: <Normal> <Uniform> <Extreme> <Pearson> <Trapeziodal>
        """
        Normal: int
        Uniform: int
        Extreme: int
        Pearson: int
        Trapeziodal: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> TaperedPinFeatureBuilder.APIEnumForm:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## 
    ##         
    ##         
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Normal</term><description> 
    ## </description> </item><item><term> 
    ## Uniform</term><description> 
    ## </description> </item><item><term> 
    ## Extreme</term><description> 
    ## </description> </item><item><term> 
    ## Pearson</term><description> 
    ## </description> </item><item><term> 
    ## Trapeziodal</term><description> 
    ## </description> </item></list>
    class APIEnumLoc(Enum):
        """
        Members Include: <Normal> <Uniform> <Extreme> <Pearson> <Trapeziodal>
        """
        Normal: int
        Uniform: int
        Extreme: int
        Pearson: int
        Trapeziodal: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> TaperedPinFeatureBuilder.APIEnumLoc:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## 
    ##         
    ##         
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Normal</term><description> 
    ## </description> </item><item><term> 
    ## Uniform</term><description> 
    ## </description> </item><item><term> 
    ## Extreme</term><description> 
    ## </description> </item><item><term> 
    ## Pearson</term><description> 
    ## </description> </item><item><term> 
    ## Trapeziodal</term><description> 
    ## </description> </item></list>
    class APIEnumSize(Enum):
        """
        Members Include: <Normal> <Uniform> <Extreme> <Pearson> <Trapeziodal>
        """
        Normal: int
        Uniform: int
        Extreme: int
        Pearson: int
        Trapeziodal: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> TaperedPinFeatureBuilder.APIEnumSize:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (float) DoubleAnchorX
    ##   the double anchor x   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def DoubleAnchorX(self) -> float:
        """
        Getter for property: (float) DoubleAnchorX
          the double anchor x   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleAnchorX

    ##   the double anchor x   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @DoubleAnchorX.setter
    def DoubleAnchorX(self, doubleAnchorX: float):
        """
        Setter for property: (float) DoubleAnchorX
          the double anchor x   
            
         
        """
        pass
    
    ## Getter for property: (float) DoubleAnchorY
    ##   the double anchor y   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def DoubleAnchorY(self) -> float:
        """
        Getter for property: (float) DoubleAnchorY
          the double anchor y   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleAnchorY

    ##   the double anchor y   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @DoubleAnchorY.setter
    def DoubleAnchorY(self, doubleAnchorY: float):
        """
        Setter for property: (float) DoubleAnchorY
          the double anchor y   
            
         
        """
        pass
    
    ## Getter for property: (float) DoubleAnchorZ
    ##   the double anchor z   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def DoubleAnchorZ(self) -> float:
        """
        Getter for property: (float) DoubleAnchorZ
          the double anchor z   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleAnchorZ

    ##   the double anchor z   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @DoubleAnchorZ.setter
    def DoubleAnchorZ(self, doubleAnchorZ: float):
        """
        Setter for property: (float) DoubleAnchorZ
          the double anchor z   
            
         
        """
        pass
    
    ## Getter for property: (float) DoubleDiameter1
    ##   the double diameter1   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def DoubleDiameter1(self) -> float:
        """
        Getter for property: (float) DoubleDiameter1
          the double diameter1   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleDiameter1

    ##   the double diameter1   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @DoubleDiameter1.setter
    def DoubleDiameter1(self, doubleDiameter1: float):
        """
        Setter for property: (float) DoubleDiameter1
          the double diameter1   
            
         
        """
        pass
    
    ## Getter for property: (float) DoubleDiameter2
    ##   the double diameter2   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def DoubleDiameter2(self) -> float:
        """
        Getter for property: (float) DoubleDiameter2
          the double diameter2   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleDiameter2

    ##   the double diameter2   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @DoubleDiameter2.setter
    def DoubleDiameter2(self, doubleDiameter2: float):
        """
        Setter for property: (float) DoubleDiameter2
          the double diameter2   
            
         
        """
        pass
    
    ## Getter for property: (float) DoubleDirectionI
    ##   the double direction i   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def DoubleDirectionI(self) -> float:
        """
        Getter for property: (float) DoubleDirectionI
          the double direction i   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleDirectionI

    ##   the double direction i   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @DoubleDirectionI.setter
    def DoubleDirectionI(self, doubleDirectionI: float):
        """
        Setter for property: (float) DoubleDirectionI
          the double direction i   
            
         
        """
        pass
    
    ## Getter for property: (float) DoubleDirectionJ
    ##   the double direction j   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def DoubleDirectionJ(self) -> float:
        """
        Getter for property: (float) DoubleDirectionJ
          the double direction j   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleDirectionJ

    ##   the double direction j   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @DoubleDirectionJ.setter
    def DoubleDirectionJ(self, doubleDirectionJ: float):
        """
        Setter for property: (float) DoubleDirectionJ
          the double direction j   
            
         
        """
        pass
    
    ## Getter for property: (float) DoubleDirectionK
    ##   the double direction k   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def DoubleDirectionK(self) -> float:
        """
        Getter for property: (float) DoubleDirectionK
          the double direction k   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleDirectionK

    ##   the double direction k   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @DoubleDirectionK.setter
    def DoubleDirectionK(self, doubleDirectionK: float):
        """
        Setter for property: (float) DoubleDirectionK
          the double direction k   
            
         
        """
        pass
    
    ## Getter for property: (float) DoubleHeight
    ##   the double height   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def DoubleHeight(self) -> float:
        """
        Getter for property: (float) DoubleHeight
          the double height   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleHeight

    ##   the double height   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @DoubleHeight.setter
    def DoubleHeight(self, doubleHeight: float):
        """
        Setter for property: (float) DoubleHeight
          the double height   
            
         
        """
        pass
    
    ## Getter for property: (float) DoubleKurtosisForm
    ##   the double kurtosis form   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def DoubleKurtosisForm(self) -> float:
        """
        Getter for property: (float) DoubleKurtosisForm
          the double kurtosis form   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleKurtosisForm

    ##   the double kurtosis form   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @DoubleKurtosisForm.setter
    def DoubleKurtosisForm(self, doubleKurtosisForm: float):
        """
        Setter for property: (float) DoubleKurtosisForm
          the double kurtosis form   
            
         
        """
        pass
    
    ## Getter for property: (float) DoubleKurtosisLoc
    ##   the double kurtosis loc   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def DoubleKurtosisLoc(self) -> float:
        """
        Getter for property: (float) DoubleKurtosisLoc
          the double kurtosis loc   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleKurtosisLoc

    ##   the double kurtosis loc   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @DoubleKurtosisLoc.setter
    def DoubleKurtosisLoc(self, doubleKurtosisLoc: float):
        """
        Setter for property: (float) DoubleKurtosisLoc
          the double kurtosis loc   
            
         
        """
        pass
    
    ## Getter for property: (float) DoubleKurtosisSize
    ##   the double kurtosis size   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def DoubleKurtosisSize(self) -> float:
        """
        Getter for property: (float) DoubleKurtosisSize
          the double kurtosis size   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleKurtosisSize

    ##   the double kurtosis size   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @DoubleKurtosisSize.setter
    def DoubleKurtosisSize(self, doubleKurtosisSize: float):
        """
        Setter for property: (float) DoubleKurtosisSize
          the double kurtosis size   
            
         
        """
        pass
    
    ## Getter for property: (float) DoubleSkewnessForm
    ##   the double skewness form   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def DoubleSkewnessForm(self) -> float:
        """
        Getter for property: (float) DoubleSkewnessForm
          the double skewness form   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleSkewnessForm

    ##   the double skewness form   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @DoubleSkewnessForm.setter
    def DoubleSkewnessForm(self, doubleSkewnessForm: float):
        """
        Setter for property: (float) DoubleSkewnessForm
          the double skewness form   
            
         
        """
        pass
    
    ## Getter for property: (float) DoubleSkewnessLoc
    ##   the double skewness loc   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def DoubleSkewnessLoc(self) -> float:
        """
        Getter for property: (float) DoubleSkewnessLoc
          the double skewness loc   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleSkewnessLoc

    ##   the double skewness loc   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @DoubleSkewnessLoc.setter
    def DoubleSkewnessLoc(self, doubleSkewnessLoc: float):
        """
        Setter for property: (float) DoubleSkewnessLoc
          the double skewness loc   
            
         
        """
        pass
    
    ## Getter for property: (float) DoubleSkewnessSize
    ##   the double skewness size   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def DoubleSkewnessSize(self) -> float:
        """
        Getter for property: (float) DoubleSkewnessSize
          the double skewness size   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleSkewnessSize

    ##   the double skewness size   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @DoubleSkewnessSize.setter
    def DoubleSkewnessSize(self, doubleSkewnessSize: float):
        """
        Setter for property: (float) DoubleSkewnessSize
          the double skewness size   
            
         
        """
        pass
    
    ## Getter for property: (@link TaperedPinFeatureBuilder.APIEnumForm NXOpen.Vsa.TaperedPinFeatureBuilder.APIEnumForm@endlink) EnumForm
    ##   the enum form   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return TaperedPinFeatureBuilder.APIEnumForm
    @property
    def EnumForm(self) -> TaperedPinFeatureBuilder.APIEnumForm:
        """
        Getter for property: (@link TaperedPinFeatureBuilder.APIEnumForm NXOpen.Vsa.TaperedPinFeatureBuilder.APIEnumForm@endlink) EnumForm
          the enum form   
            
         
        """
        pass
    
    ## Setter for property: (@link TaperedPinFeatureBuilder.APIEnumForm NXOpen.Vsa.TaperedPinFeatureBuilder.APIEnumForm@endlink) EnumForm

    ##   the enum form   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @EnumForm.setter
    def EnumForm(self, enumForm: TaperedPinFeatureBuilder.APIEnumForm):
        """
        Setter for property: (@link TaperedPinFeatureBuilder.APIEnumForm NXOpen.Vsa.TaperedPinFeatureBuilder.APIEnumForm@endlink) EnumForm
          the enum form   
            
         
        """
        pass
    
    ## Getter for property: (@link TaperedPinFeatureBuilder.APIEnumLoc NXOpen.Vsa.TaperedPinFeatureBuilder.APIEnumLoc@endlink) EnumLoc
    ##   the enum loc   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return TaperedPinFeatureBuilder.APIEnumLoc
    @property
    def EnumLoc(self) -> TaperedPinFeatureBuilder.APIEnumLoc:
        """
        Getter for property: (@link TaperedPinFeatureBuilder.APIEnumLoc NXOpen.Vsa.TaperedPinFeatureBuilder.APIEnumLoc@endlink) EnumLoc
          the enum loc   
            
         
        """
        pass
    
    ## Setter for property: (@link TaperedPinFeatureBuilder.APIEnumLoc NXOpen.Vsa.TaperedPinFeatureBuilder.APIEnumLoc@endlink) EnumLoc

    ##   the enum loc   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @EnumLoc.setter
    def EnumLoc(self, enumLoc: TaperedPinFeatureBuilder.APIEnumLoc):
        """
        Setter for property: (@link TaperedPinFeatureBuilder.APIEnumLoc NXOpen.Vsa.TaperedPinFeatureBuilder.APIEnumLoc@endlink) EnumLoc
          the enum loc   
            
         
        """
        pass
    
    ## Getter for property: (@link TaperedPinFeatureBuilder.APIEnumSize NXOpen.Vsa.TaperedPinFeatureBuilder.APIEnumSize@endlink) EnumSize
    ##   the enum size   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return TaperedPinFeatureBuilder.APIEnumSize
    @property
    def EnumSize(self) -> TaperedPinFeatureBuilder.APIEnumSize:
        """
        Getter for property: (@link TaperedPinFeatureBuilder.APIEnumSize NXOpen.Vsa.TaperedPinFeatureBuilder.APIEnumSize@endlink) EnumSize
          the enum size   
            
         
        """
        pass
    
    ## Setter for property: (@link TaperedPinFeatureBuilder.APIEnumSize NXOpen.Vsa.TaperedPinFeatureBuilder.APIEnumSize@endlink) EnumSize

    ##   the enum size   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @EnumSize.setter
    def EnumSize(self, enumSize: TaperedPinFeatureBuilder.APIEnumSize):
        """
        Setter for property: (@link TaperedPinFeatureBuilder.APIEnumSize NXOpen.Vsa.TaperedPinFeatureBuilder.APIEnumSize@endlink) EnumSize
          the enum size   
            
         
        """
        pass
    
    ## Getter for property: (str) StringDescription
    ##   the string description   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return str
    @property
    def StringDescription(self) -> str:
        """
        Getter for property: (str) StringDescription
          the string description   
            
         
        """
        pass
    
    ## Setter for property: (str) StringDescription

    ##   the string description   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @StringDescription.setter
    def StringDescription(self, stringDescription: str):
        """
        Setter for property: (str) StringDescription
          the string description   
            
         
        """
        pass
    
    ## Getter for property: (str) StringName
    ##   the string name   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return str
    @property
    def StringName(self) -> str:
        """
        Getter for property: (str) StringName
          the string name   
            
         
        """
        pass
    
    ## Setter for property: (str) StringName

    ##   the string name   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @StringName.setter
    def StringName(self, stringName: str):
        """
        Setter for property: (str) StringName
          the string name   
            
         
        """
        pass
    
import NXOpen
##  Represents a Tapered Pin feature  <br> To create or edit an instance of this class, use @link NXOpen::Vsa::TaperedPinFeatureBuilder  NXOpen::Vsa::TaperedPinFeatureBuilder @endlink  <br> 
## 
##  <br>  Usable only on Windows <br>  
## 
##   <br>  Created in NX1926.0.0  <br> 

class TaperedPinFeature(NXOpen.NXObject): 
    """ Represents a Tapered Pin feature """
    pass


import NXOpen
## 
##     
##      <br> To create a new instance of this class, use @link NXOpen::Vsa::VsaManager::CreateTaperedPinPatternFeatureBuilder  NXOpen::Vsa::VsaManager::CreateTaperedPinPatternFeatureBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## DoubleKurtosisForm </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleKurtosisLoc </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleKurtosisSize </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleSkewnessForm </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleSkewnessLoc </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleSkewnessSize </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## EnumForm </term> <description> 
##  
## Normal </description> </item> 
## 
## <item><term> 
##  
## EnumLoc </term> <description> 
##  
## Normal </description> </item> 
## 
## <item><term> 
##  
## EnumSize </term> <description> 
##  
## Normal </description> </item> 
## 
## </list> 

## 
##  <br>  Usable only on Windows <br>  
## 
##   <br>  Created in NX1926.0.0  <br> 

class TaperedPinPatternFeatureBuilder(NXOpen.Builder): 
    """
    
    """


    ## 
    ##         
    ##         
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Normal</term><description> 
    ## </description> </item><item><term> 
    ## Uniform</term><description> 
    ## </description> </item><item><term> 
    ## Extreme</term><description> 
    ## </description> </item><item><term> 
    ## Pearson</term><description> 
    ## </description> </item><item><term> 
    ## Trapeziodal</term><description> 
    ## </description> </item></list>
    class APIEnumForm(Enum):
        """
        Members Include: <Normal> <Uniform> <Extreme> <Pearson> <Trapeziodal>
        """
        Normal: int
        Uniform: int
        Extreme: int
        Pearson: int
        Trapeziodal: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> TaperedPinPatternFeatureBuilder.APIEnumForm:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## 
    ##         
    ##         
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Normal</term><description> 
    ## </description> </item><item><term> 
    ## Uniform</term><description> 
    ## </description> </item><item><term> 
    ## Extreme</term><description> 
    ## </description> </item><item><term> 
    ## Pearson</term><description> 
    ## </description> </item><item><term> 
    ## Trapeziodal</term><description> 
    ## </description> </item></list>
    class APIEnumLoc(Enum):
        """
        Members Include: <Normal> <Uniform> <Extreme> <Pearson> <Trapeziodal>
        """
        Normal: int
        Uniform: int
        Extreme: int
        Pearson: int
        Trapeziodal: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> TaperedPinPatternFeatureBuilder.APIEnumLoc:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## 
    ##         
    ##         
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Normal</term><description> 
    ## </description> </item><item><term> 
    ## Uniform</term><description> 
    ## </description> </item><item><term> 
    ## Extreme</term><description> 
    ## </description> </item><item><term> 
    ## Pearson</term><description> 
    ## </description> </item><item><term> 
    ## Trapeziodal</term><description> 
    ## </description> </item></list>
    class APIEnumSize(Enum):
        """
        Members Include: <Normal> <Uniform> <Extreme> <Pearson> <Trapeziodal>
        """
        Normal: int
        Uniform: int
        Extreme: int
        Pearson: int
        Trapeziodal: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> TaperedPinPatternFeatureBuilder.APIEnumSize:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (float) DoubleKurtosisForm
    ##   the double kurtosis form   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def DoubleKurtosisForm(self) -> float:
        """
        Getter for property: (float) DoubleKurtosisForm
          the double kurtosis form   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleKurtosisForm

    ##   the double kurtosis form   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @DoubleKurtosisForm.setter
    def DoubleKurtosisForm(self, doubleKurtosisForm: float):
        """
        Setter for property: (float) DoubleKurtosisForm
          the double kurtosis form   
            
         
        """
        pass
    
    ## Getter for property: (float) DoubleKurtosisLoc
    ##   the double kurtosis loc   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def DoubleKurtosisLoc(self) -> float:
        """
        Getter for property: (float) DoubleKurtosisLoc
          the double kurtosis loc   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleKurtosisLoc

    ##   the double kurtosis loc   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @DoubleKurtosisLoc.setter
    def DoubleKurtosisLoc(self, doubleKurtosisLoc: float):
        """
        Setter for property: (float) DoubleKurtosisLoc
          the double kurtosis loc   
            
         
        """
        pass
    
    ## Getter for property: (float) DoubleKurtosisSize
    ##   the double kurtosis size   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def DoubleKurtosisSize(self) -> float:
        """
        Getter for property: (float) DoubleKurtosisSize
          the double kurtosis size   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleKurtosisSize

    ##   the double kurtosis size   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @DoubleKurtosisSize.setter
    def DoubleKurtosisSize(self, doubleKurtosisSize: float):
        """
        Setter for property: (float) DoubleKurtosisSize
          the double kurtosis size   
            
         
        """
        pass
    
    ## Getter for property: (float) DoubleSkewnessForm
    ##   the double skewness form   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def DoubleSkewnessForm(self) -> float:
        """
        Getter for property: (float) DoubleSkewnessForm
          the double skewness form   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleSkewnessForm

    ##   the double skewness form   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @DoubleSkewnessForm.setter
    def DoubleSkewnessForm(self, doubleSkewnessForm: float):
        """
        Setter for property: (float) DoubleSkewnessForm
          the double skewness form   
            
         
        """
        pass
    
    ## Getter for property: (float) DoubleSkewnessLoc
    ##   the double skewness loc   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def DoubleSkewnessLoc(self) -> float:
        """
        Getter for property: (float) DoubleSkewnessLoc
          the double skewness loc   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleSkewnessLoc

    ##   the double skewness loc   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @DoubleSkewnessLoc.setter
    def DoubleSkewnessLoc(self, doubleSkewnessLoc: float):
        """
        Setter for property: (float) DoubleSkewnessLoc
          the double skewness loc   
            
         
        """
        pass
    
    ## Getter for property: (float) DoubleSkewnessSize
    ##   the double skewness size   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def DoubleSkewnessSize(self) -> float:
        """
        Getter for property: (float) DoubleSkewnessSize
          the double skewness size   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleSkewnessSize

    ##   the double skewness size   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @DoubleSkewnessSize.setter
    def DoubleSkewnessSize(self, doubleSkewnessSize: float):
        """
        Setter for property: (float) DoubleSkewnessSize
          the double skewness size   
            
         
        """
        pass
    
    ## Getter for property: (@link TaperedPinPatternFeatureBuilder.APIEnumForm NXOpen.Vsa.TaperedPinPatternFeatureBuilder.APIEnumForm@endlink) EnumForm
    ##   the enum form   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return TaperedPinPatternFeatureBuilder.APIEnumForm
    @property
    def EnumForm(self) -> TaperedPinPatternFeatureBuilder.APIEnumForm:
        """
        Getter for property: (@link TaperedPinPatternFeatureBuilder.APIEnumForm NXOpen.Vsa.TaperedPinPatternFeatureBuilder.APIEnumForm@endlink) EnumForm
          the enum form   
            
         
        """
        pass
    
    ## Setter for property: (@link TaperedPinPatternFeatureBuilder.APIEnumForm NXOpen.Vsa.TaperedPinPatternFeatureBuilder.APIEnumForm@endlink) EnumForm

    ##   the enum form   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @EnumForm.setter
    def EnumForm(self, enumForm: TaperedPinPatternFeatureBuilder.APIEnumForm):
        """
        Setter for property: (@link TaperedPinPatternFeatureBuilder.APIEnumForm NXOpen.Vsa.TaperedPinPatternFeatureBuilder.APIEnumForm@endlink) EnumForm
          the enum form   
            
         
        """
        pass
    
    ## Getter for property: (@link TaperedPinPatternFeatureBuilder.APIEnumLoc NXOpen.Vsa.TaperedPinPatternFeatureBuilder.APIEnumLoc@endlink) EnumLoc
    ##   the enum loc   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return TaperedPinPatternFeatureBuilder.APIEnumLoc
    @property
    def EnumLoc(self) -> TaperedPinPatternFeatureBuilder.APIEnumLoc:
        """
        Getter for property: (@link TaperedPinPatternFeatureBuilder.APIEnumLoc NXOpen.Vsa.TaperedPinPatternFeatureBuilder.APIEnumLoc@endlink) EnumLoc
          the enum loc   
            
         
        """
        pass
    
    ## Setter for property: (@link TaperedPinPatternFeatureBuilder.APIEnumLoc NXOpen.Vsa.TaperedPinPatternFeatureBuilder.APIEnumLoc@endlink) EnumLoc

    ##   the enum loc   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @EnumLoc.setter
    def EnumLoc(self, enumLoc: TaperedPinPatternFeatureBuilder.APIEnumLoc):
        """
        Setter for property: (@link TaperedPinPatternFeatureBuilder.APIEnumLoc NXOpen.Vsa.TaperedPinPatternFeatureBuilder.APIEnumLoc@endlink) EnumLoc
          the enum loc   
            
         
        """
        pass
    
    ## Getter for property: (@link TaperedPinPatternFeatureBuilder.APIEnumSize NXOpen.Vsa.TaperedPinPatternFeatureBuilder.APIEnumSize@endlink) EnumSize
    ##   the enum size   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return TaperedPinPatternFeatureBuilder.APIEnumSize
    @property
    def EnumSize(self) -> TaperedPinPatternFeatureBuilder.APIEnumSize:
        """
        Getter for property: (@link TaperedPinPatternFeatureBuilder.APIEnumSize NXOpen.Vsa.TaperedPinPatternFeatureBuilder.APIEnumSize@endlink) EnumSize
          the enum size   
            
         
        """
        pass
    
    ## Setter for property: (@link TaperedPinPatternFeatureBuilder.APIEnumSize NXOpen.Vsa.TaperedPinPatternFeatureBuilder.APIEnumSize@endlink) EnumSize

    ##   the enum size   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @EnumSize.setter
    def EnumSize(self, enumSize: TaperedPinPatternFeatureBuilder.APIEnumSize):
        """
        Setter for property: (@link TaperedPinPatternFeatureBuilder.APIEnumSize NXOpen.Vsa.TaperedPinPatternFeatureBuilder.APIEnumSize@endlink) EnumSize
          the enum size   
            
         
        """
        pass
    
    ## Getter for property: (int) NumInstanceCount
    ##   the enum size   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return int
    @property
    def NumInstanceCount(self) -> int:
        """
        Getter for property: (int) NumInstanceCount
          the enum size   
            
         
        """
        pass
    
    ## Setter for property: (int) NumInstanceCount

    ##   the enum size   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @NumInstanceCount.setter
    def NumInstanceCount(self, numInstanceCount: int):
        """
        Setter for property: (int) NumInstanceCount
          the enum size   
            
         
        """
        pass
    
    ## Getter for property: (str) StringDescription
    ##   the string description   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return str
    @property
    def StringDescription(self) -> str:
        """
        Getter for property: (str) StringDescription
          the string description   
            
         
        """
        pass
    
    ## Setter for property: (str) StringDescription

    ##   the string description   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @StringDescription.setter
    def StringDescription(self, stringDescription: str):
        """
        Setter for property: (str) StringDescription
          the string description   
            
         
        """
        pass
    
    ## Getter for property: (str) StringName
    ##   the string name   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return str
    @property
    def StringName(self) -> str:
        """
        Getter for property: (str) StringName
          the string name   
            
         
        """
        pass
    
    ## Setter for property: (str) StringName

    ##   the string name   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @StringName.setter
    def StringName(self, stringName: str):
        """
        Setter for property: (str) StringName
          the string name   
            
         
        """
        pass
    
import NXOpen
##  Represents a Pin pattern feature  <br> To create or edit an instance of this class, use @link NXOpen::Vsa::TaperedPinPatternFeatureBuilder  NXOpen::Vsa::TaperedPinPatternFeatureBuilder @endlink  <br> 
## 
##  <br>  Usable only on Windows <br>  
## 
##   <br>  Created in NX1899.0.0  <br> 

class TaperedPinPatternFeature(NXOpen.NXObject): 
    """ Represents a Pin pattern feature """
    pass


import NXOpen
## 
##     
##      <br> To create a new instance of this class, use @link NXOpen::Vsa::VsaManager::CreateSlotFeatureBuilder  NXOpen::Vsa::VsaManager::CreateSlotFeatureBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## DoubleKurtosisForm </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleKurtosisLoc </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleKurtosisSize </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleSkewnessForm </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleSkewnessLoc </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleSkewnessSize </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## EnumForm </term> <description> 
##  
## Normal </description> </item> 
## 
## <item><term> 
##  
## EnumLoc </term> <description> 
##  
## Normal </description> </item> 
## 
## <item><term> 
##  
## EnumSize </term> <description> 
##  
## Normal </description> </item> 
## 
## </list> 

## 
##  <br>  Usable only on Windows <br>  
## 
##   <br>  Created in NX1926.0.0  <br> 

class TaperedSlotFeatureBuilder(NXOpen.Builder): 
    """
    
    """


    ## 
    ##         
    ##         
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Normal</term><description> 
    ## </description> </item><item><term> 
    ## Uniform</term><description> 
    ## </description> </item><item><term> 
    ## Extreme</term><description> 
    ## </description> </item><item><term> 
    ## Pearson</term><description> 
    ## </description> </item><item><term> 
    ## Trapeziodal</term><description> 
    ## </description> </item></list>
    class APIEnumForm(Enum):
        """
        Members Include: <Normal> <Uniform> <Extreme> <Pearson> <Trapeziodal>
        """
        Normal: int
        Uniform: int
        Extreme: int
        Pearson: int
        Trapeziodal: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> TaperedSlotFeatureBuilder.APIEnumForm:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## 
    ##         
    ##         
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Normal</term><description> 
    ## </description> </item><item><term> 
    ## Uniform</term><description> 
    ## </description> </item><item><term> 
    ## Extreme</term><description> 
    ## </description> </item><item><term> 
    ## Pearson</term><description> 
    ## </description> </item><item><term> 
    ## Trapeziodal</term><description> 
    ## </description> </item></list>
    class APIEnumLoc(Enum):
        """
        Members Include: <Normal> <Uniform> <Extreme> <Pearson> <Trapeziodal>
        """
        Normal: int
        Uniform: int
        Extreme: int
        Pearson: int
        Trapeziodal: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> TaperedSlotFeatureBuilder.APIEnumLoc:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## 
    ##         
    ##         
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Normal</term><description> 
    ## </description> </item><item><term> 
    ## Uniform</term><description> 
    ## </description> </item><item><term> 
    ## Extreme</term><description> 
    ## </description> </item><item><term> 
    ## Pearson</term><description> 
    ## </description> </item><item><term> 
    ## Trapeziodal</term><description> 
    ## </description> </item></list>
    class APIEnumSize(Enum):
        """
        Members Include: <Normal> <Uniform> <Extreme> <Pearson> <Trapeziodal>
        """
        Normal: int
        Uniform: int
        Extreme: int
        Pearson: int
        Trapeziodal: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> TaperedSlotFeatureBuilder.APIEnumSize:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (float) DoubleAnchorX
    ##   the property represents  X value of anchor.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def DoubleAnchorX(self) -> float:
        """
        Getter for property: (float) DoubleAnchorX
          the property represents  X value of anchor.  
             
         
        """
        pass
    
    ## Setter for property: (float) DoubleAnchorX

    ##   the property represents  X value of anchor.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @DoubleAnchorX.setter
    def DoubleAnchorX(self, doubleAnchorX: float):
        """
        Setter for property: (float) DoubleAnchorX
          the property represents  X value of anchor.  
             
         
        """
        pass
    
    ## Getter for property: (float) DoubleAnchorY
    ##   the property represents  Y value of anchor.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def DoubleAnchorY(self) -> float:
        """
        Getter for property: (float) DoubleAnchorY
          the property represents  Y value of anchor.  
             
         
        """
        pass
    
    ## Setter for property: (float) DoubleAnchorY

    ##   the property represents  Y value of anchor.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @DoubleAnchorY.setter
    def DoubleAnchorY(self, doubleAnchorY: float):
        """
        Setter for property: (float) DoubleAnchorY
          the property represents  Y value of anchor.  
             
         
        """
        pass
    
    ## Getter for property: (float) DoubleAnchorZ
    ##   the property represents  Z value of anchor.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def DoubleAnchorZ(self) -> float:
        """
        Getter for property: (float) DoubleAnchorZ
          the property represents  Z value of anchor.  
             
         
        """
        pass
    
    ## Setter for property: (float) DoubleAnchorZ

    ##   the property represents  Z value of anchor.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @DoubleAnchorZ.setter
    def DoubleAnchorZ(self, doubleAnchorZ: float):
        """
        Setter for property: (float) DoubleAnchorZ
          the property represents  Z value of anchor.  
             
         
        """
        pass
    
    ## Getter for property: (float) DoubleAngle
    ##   the property represents  Angle of slot.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def DoubleAngle(self) -> float:
        """
        Getter for property: (float) DoubleAngle
          the property represents  Angle of slot.  
             
         
        """
        pass
    
    ## Setter for property: (float) DoubleAngle

    ##   the property represents  Angle of slot.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @DoubleAngle.setter
    def DoubleAngle(self, angle: float):
        """
        Setter for property: (float) DoubleAngle
          the property represents  Angle of slot.  
             
         
        """
        pass
    
    ## Getter for property: (float) DoubleDepth
    ##   the property represents  depth of slot.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def DoubleDepth(self) -> float:
        """
        Getter for property: (float) DoubleDepth
          the property represents  depth of slot.  
             
         
        """
        pass
    
    ## Setter for property: (float) DoubleDepth

    ##   the property represents  depth of slot.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @DoubleDepth.setter
    def DoubleDepth(self, height: float):
        """
        Setter for property: (float) DoubleDepth
          the property represents  depth of slot.  
             
         
        """
        pass
    
    ## Getter for property: (float) DoubleDirectionI
    ##   the property represents  X value of normal.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def DoubleDirectionI(self) -> float:
        """
        Getter for property: (float) DoubleDirectionI
          the property represents  X value of normal.  
             
         
        """
        pass
    
    ## Setter for property: (float) DoubleDirectionI

    ##   the property represents  X value of normal.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @DoubleDirectionI.setter
    def DoubleDirectionI(self, doubleDirectionI: float):
        """
        Setter for property: (float) DoubleDirectionI
          the property represents  X value of normal.  
             
         
        """
        pass
    
    ## Getter for property: (float) DoubleDirectionJ
    ##   the property represents  Y value of normal.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def DoubleDirectionJ(self) -> float:
        """
        Getter for property: (float) DoubleDirectionJ
          the property represents  Y value of normal.  
             
         
        """
        pass
    
    ## Setter for property: (float) DoubleDirectionJ

    ##   the property represents  Y value of normal.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @DoubleDirectionJ.setter
    def DoubleDirectionJ(self, doubleDirectionJ: float):
        """
        Setter for property: (float) DoubleDirectionJ
          the property represents  Y value of normal.  
             
         
        """
        pass
    
    ## Getter for property: (float) DoubleDirectionK
    ##   the property represents  Z value of normal.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def DoubleDirectionK(self) -> float:
        """
        Getter for property: (float) DoubleDirectionK
          the property represents  Z value of normal.  
             
         
        """
        pass
    
    ## Setter for property: (float) DoubleDirectionK

    ##   the property represents  Z value of normal.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @DoubleDirectionK.setter
    def DoubleDirectionK(self, doubleDirectionK: float):
        """
        Setter for property: (float) DoubleDirectionK
          the property represents  Z value of normal.  
             
         
        """
        pass
    
    ## Getter for property: (float) DoubleKurtosisForm
    ##   the property represents  Form distribution Kurtosis.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def DoubleKurtosisForm(self) -> float:
        """
        Getter for property: (float) DoubleKurtosisForm
          the property represents  Form distribution Kurtosis.  
             
         
        """
        pass
    
    ## Setter for property: (float) DoubleKurtosisForm

    ##   the property represents  Form distribution Kurtosis.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @DoubleKurtosisForm.setter
    def DoubleKurtosisForm(self, doubleKurtosisForm: float):
        """
        Setter for property: (float) DoubleKurtosisForm
          the property represents  Form distribution Kurtosis.  
             
         
        """
        pass
    
    ## Getter for property: (float) DoubleKurtosisLoc
    ##   the property represents  Loc distribution Kurtosis.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def DoubleKurtosisLoc(self) -> float:
        """
        Getter for property: (float) DoubleKurtosisLoc
          the property represents  Loc distribution Kurtosis.  
             
         
        """
        pass
    
    ## Setter for property: (float) DoubleKurtosisLoc

    ##   the property represents  Loc distribution Kurtosis.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @DoubleKurtosisLoc.setter
    def DoubleKurtosisLoc(self, doubleKurtosisLoc: float):
        """
        Setter for property: (float) DoubleKurtosisLoc
          the property represents  Loc distribution Kurtosis.  
             
         
        """
        pass
    
    ## Getter for property: (float) DoubleKurtosisSize
    ##   the property represents  Size distribution Kurtosis.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def DoubleKurtosisSize(self) -> float:
        """
        Getter for property: (float) DoubleKurtosisSize
          the property represents  Size distribution Kurtosis.  
             
         
        """
        pass
    
    ## Setter for property: (float) DoubleKurtosisSize

    ##   the property represents  Size distribution Kurtosis.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @DoubleKurtosisSize.setter
    def DoubleKurtosisSize(self, doubleKurtosisSize: float):
        """
        Setter for property: (float) DoubleKurtosisSize
          the property represents  Size distribution Kurtosis.  
             
         
        """
        pass
    
    ## Getter for property: (float) DoubleLength
    ##   the property represents  length of slot.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def DoubleLength(self) -> float:
        """
        Getter for property: (float) DoubleLength
          the property represents  length of slot.  
             
         
        """
        pass
    
    ## Setter for property: (float) DoubleLength

    ##   the property represents  length of slot.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @DoubleLength.setter
    def DoubleLength(self, distance: float):
        """
        Setter for property: (float) DoubleLength
          the property represents  length of slot.  
             
         
        """
        pass
    
    ## Getter for property: (float) DoubleLengthVectorI
    ##   the property represents  X value of length vector.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def DoubleLengthVectorI(self) -> float:
        """
        Getter for property: (float) DoubleLengthVectorI
          the property represents  X value of length vector.  
             
         
        """
        pass
    
    ## Setter for property: (float) DoubleLengthVectorI

    ##   the property represents  X value of length vector.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @DoubleLengthVectorI.setter
    def DoubleLengthVectorI(self, doubleLengthVectorI: float):
        """
        Setter for property: (float) DoubleLengthVectorI
          the property represents  X value of length vector.  
             
         
        """
        pass
    
    ## Getter for property: (float) DoubleLengthVectorJ
    ##   the property represents  Y value of length vector.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def DoubleLengthVectorJ(self) -> float:
        """
        Getter for property: (float) DoubleLengthVectorJ
          the property represents  Y value of length vector.  
             
         
        """
        pass
    
    ## Setter for property: (float) DoubleLengthVectorJ

    ##   the property represents  Y value of length vector.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @DoubleLengthVectorJ.setter
    def DoubleLengthVectorJ(self, doubleLengthVectorJ: float):
        """
        Setter for property: (float) DoubleLengthVectorJ
          the property represents  Y value of length vector.  
             
         
        """
        pass
    
    ## Getter for property: (float) DoubleLengthVectorK
    ##   the property represents  Z value of length vector.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def DoubleLengthVectorK(self) -> float:
        """
        Getter for property: (float) DoubleLengthVectorK
          the property represents  Z value of length vector.  
             
         
        """
        pass
    
    ## Setter for property: (float) DoubleLengthVectorK

    ##   the property represents  Z value of length vector.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @DoubleLengthVectorK.setter
    def DoubleLengthVectorK(self, doubleLengthVectorK: float):
        """
        Setter for property: (float) DoubleLengthVectorK
          the property represents  Z value of length vector.  
             
         
        """
        pass
    
    ## Getter for property: (float) DoubleSkewnessForm
    ##   the property represents  Form distribution Skewness.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def DoubleSkewnessForm(self) -> float:
        """
        Getter for property: (float) DoubleSkewnessForm
          the property represents  Form distribution Skewness.  
             
         
        """
        pass
    
    ## Setter for property: (float) DoubleSkewnessForm

    ##   the property represents  Form distribution Skewness.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @DoubleSkewnessForm.setter
    def DoubleSkewnessForm(self, doubleSkewnessForm: float):
        """
        Setter for property: (float) DoubleSkewnessForm
          the property represents  Form distribution Skewness.  
             
         
        """
        pass
    
    ## Getter for property: (float) DoubleSkewnessLoc
    ##   the property represents  Loc distribution Skewness.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def DoubleSkewnessLoc(self) -> float:
        """
        Getter for property: (float) DoubleSkewnessLoc
          the property represents  Loc distribution Skewness.  
             
         
        """
        pass
    
    ## Setter for property: (float) DoubleSkewnessLoc

    ##   the property represents  Loc distribution Skewness.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @DoubleSkewnessLoc.setter
    def DoubleSkewnessLoc(self, doubleSkewnessLoc: float):
        """
        Setter for property: (float) DoubleSkewnessLoc
          the property represents  Loc distribution Skewness.  
             
         
        """
        pass
    
    ## Getter for property: (float) DoubleSkewnessSize
    ##   the property represents  Size distribution Skewness.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def DoubleSkewnessSize(self) -> float:
        """
        Getter for property: (float) DoubleSkewnessSize
          the property represents  Size distribution Skewness.  
             
         
        """
        pass
    
    ## Setter for property: (float) DoubleSkewnessSize

    ##   the property represents  Size distribution Skewness.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @DoubleSkewnessSize.setter
    def DoubleSkewnessSize(self, doubleSkewnessSize: float):
        """
        Setter for property: (float) DoubleSkewnessSize
          the property represents  Size distribution Skewness.  
             
         
        """
        pass
    
    ## Getter for property: (float) DoubleWidth
    ##   the property represents  width of slot.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def DoubleWidth(self) -> float:
        """
        Getter for property: (float) DoubleWidth
          the property represents  width of slot.  
             
         
        """
        pass
    
    ## Setter for property: (float) DoubleWidth

    ##   the property represents  width of slot.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @DoubleWidth.setter
    def DoubleWidth(self, width: float):
        """
        Setter for property: (float) DoubleWidth
          the property represents  width of slot.  
             
         
        """
        pass
    
    ## Getter for property: (float) DoubleWidth2
    ##   the property represents  width2 of slot.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def DoubleWidth2(self) -> float:
        """
        Getter for property: (float) DoubleWidth2
          the property represents  width2 of slot.  
             
         
        """
        pass
    
    ## Setter for property: (float) DoubleWidth2

    ##   the property represents  width2 of slot.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @DoubleWidth2.setter
    def DoubleWidth2(self, width2: float):
        """
        Setter for property: (float) DoubleWidth2
          the property represents  width2 of slot.  
             
         
        """
        pass
    
    ## Getter for property: (@link TaperedSlotFeatureBuilder.APIEnumForm NXOpen.Vsa.TaperedSlotFeatureBuilder.APIEnumForm@endlink) EnumForm
    ##   the property represents  Form distribution type.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return TaperedSlotFeatureBuilder.APIEnumForm
    @property
    def EnumForm(self) -> TaperedSlotFeatureBuilder.APIEnumForm:
        """
        Getter for property: (@link TaperedSlotFeatureBuilder.APIEnumForm NXOpen.Vsa.TaperedSlotFeatureBuilder.APIEnumForm@endlink) EnumForm
          the property represents  Form distribution type.  
             
         
        """
        pass
    
    ## Setter for property: (@link TaperedSlotFeatureBuilder.APIEnumForm NXOpen.Vsa.TaperedSlotFeatureBuilder.APIEnumForm@endlink) EnumForm

    ##   the property represents  Form distribution type.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @EnumForm.setter
    def EnumForm(self, enumForm: TaperedSlotFeatureBuilder.APIEnumForm):
        """
        Setter for property: (@link TaperedSlotFeatureBuilder.APIEnumForm NXOpen.Vsa.TaperedSlotFeatureBuilder.APIEnumForm@endlink) EnumForm
          the property represents  Form distribution type.  
             
         
        """
        pass
    
    ## Getter for property: (@link TaperedSlotFeatureBuilder.APIEnumLoc NXOpen.Vsa.TaperedSlotFeatureBuilder.APIEnumLoc@endlink) EnumLoc
    ##   the property represents  Loc distribution type.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return TaperedSlotFeatureBuilder.APIEnumLoc
    @property
    def EnumLoc(self) -> TaperedSlotFeatureBuilder.APIEnumLoc:
        """
        Getter for property: (@link TaperedSlotFeatureBuilder.APIEnumLoc NXOpen.Vsa.TaperedSlotFeatureBuilder.APIEnumLoc@endlink) EnumLoc
          the property represents  Loc distribution type.  
             
         
        """
        pass
    
    ## Setter for property: (@link TaperedSlotFeatureBuilder.APIEnumLoc NXOpen.Vsa.TaperedSlotFeatureBuilder.APIEnumLoc@endlink) EnumLoc

    ##   the property represents  Loc distribution type.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @EnumLoc.setter
    def EnumLoc(self, enumLoc: TaperedSlotFeatureBuilder.APIEnumLoc):
        """
        Setter for property: (@link TaperedSlotFeatureBuilder.APIEnumLoc NXOpen.Vsa.TaperedSlotFeatureBuilder.APIEnumLoc@endlink) EnumLoc
          the property represents  Loc distribution type.  
             
         
        """
        pass
    
    ## Getter for property: (@link TaperedSlotFeatureBuilder.APIEnumSize NXOpen.Vsa.TaperedSlotFeatureBuilder.APIEnumSize@endlink) EnumSize
    ##   the property represents  Size distribution type.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return TaperedSlotFeatureBuilder.APIEnumSize
    @property
    def EnumSize(self) -> TaperedSlotFeatureBuilder.APIEnumSize:
        """
        Getter for property: (@link TaperedSlotFeatureBuilder.APIEnumSize NXOpen.Vsa.TaperedSlotFeatureBuilder.APIEnumSize@endlink) EnumSize
          the property represents  Size distribution type.  
             
         
        """
        pass
    
    ## Setter for property: (@link TaperedSlotFeatureBuilder.APIEnumSize NXOpen.Vsa.TaperedSlotFeatureBuilder.APIEnumSize@endlink) EnumSize

    ##   the property represents  Size distribution type.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @EnumSize.setter
    def EnumSize(self, enumSize: TaperedSlotFeatureBuilder.APIEnumSize):
        """
        Setter for property: (@link TaperedSlotFeatureBuilder.APIEnumSize NXOpen.Vsa.TaperedSlotFeatureBuilder.APIEnumSize@endlink) EnumSize
          the property represents  Size distribution type.  
             
         
        """
        pass
    
    ## Getter for property: (str) StringDescription
    ##   the property represents  slot feature discription.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return str
    @property
    def StringDescription(self) -> str:
        """
        Getter for property: (str) StringDescription
          the property represents  slot feature discription.  
             
         
        """
        pass
    
    ## Setter for property: (str) StringDescription

    ##   the property represents  slot feature discription.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @StringDescription.setter
    def StringDescription(self, stringDescription: str):
        """
        Setter for property: (str) StringDescription
          the property represents  slot feature discription.  
             
         
        """
        pass
    
    ## Getter for property: (str) StringName
    ##   the property represents  slot feature name.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return str
    @property
    def StringName(self) -> str:
        """
        Getter for property: (str) StringName
          the property represents  slot feature name.  
             
         
        """
        pass
    
    ## Setter for property: (str) StringName

    ##   the property represents  slot feature name.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @StringName.setter
    def StringName(self, stringName: str):
        """
        Setter for property: (str) StringName
          the property represents  slot feature name.  
             
         
        """
        pass
    
import NXOpen
##  Represents a Slot feature  <br> To create or edit an instance of this class, use @link NXOpen::Vsa::TaperedSlotFeatureBuilder  NXOpen::Vsa::TaperedSlotFeatureBuilder @endlink  <br> 
## 
##  <br>  Usable only on Windows <br>  
## 
##   <br>  Created in NX1926.0.0  <br> 

class TaperedSlotFeature(NXOpen.NXObject): 
    """ Represents a Slot feature """
    pass


import NXOpen
## 
##     
##      <br> To create a new instance of this class, use @link NXOpen::Vsa::VsaManager::CreateTabFeatureBuilder  NXOpen::Vsa::VsaManager::CreateTabFeatureBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## DoubleKurtosisForm </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleKurtosisLoc </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleKurtosisSize </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleSkewnessForm </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleSkewnessLoc </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DoubleSkewnessSize </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## EnumForm </term> <description> 
##  
## Normal </description> </item> 
## 
## <item><term> 
##  
## EnumLoc </term> <description> 
##  
## Normal </description> </item> 
## 
## <item><term> 
##  
## EnumSize </term> <description> 
##  
## Normal </description> </item> 
## 
## </list> 

## 
##  <br>  Usable only on Windows <br>  
## 
##   <br>  Created in NX1926.0.0  <br> 

class TaperedTabFeatureBuilder(NXOpen.Builder): 
    """
    
    """


    ## 
    ##         
    ##         
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Normal</term><description> 
    ## </description> </item><item><term> 
    ## Uniform</term><description> 
    ## </description> </item><item><term> 
    ## Extreme</term><description> 
    ## </description> </item><item><term> 
    ## Pearson</term><description> 
    ## </description> </item><item><term> 
    ## Trapeziodal</term><description> 
    ## </description> </item></list>
    class APIEnumForm(Enum):
        """
        Members Include: <Normal> <Uniform> <Extreme> <Pearson> <Trapeziodal>
        """
        Normal: int
        Uniform: int
        Extreme: int
        Pearson: int
        Trapeziodal: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> TaperedTabFeatureBuilder.APIEnumForm:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## 
    ##         
    ##         
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Normal</term><description> 
    ## </description> </item><item><term> 
    ## Uniform</term><description> 
    ## </description> </item><item><term> 
    ## Extreme</term><description> 
    ## </description> </item><item><term> 
    ## Pearson</term><description> 
    ## </description> </item><item><term> 
    ## Trapeziodal</term><description> 
    ## </description> </item></list>
    class APIEnumLoc(Enum):
        """
        Members Include: <Normal> <Uniform> <Extreme> <Pearson> <Trapeziodal>
        """
        Normal: int
        Uniform: int
        Extreme: int
        Pearson: int
        Trapeziodal: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> TaperedTabFeatureBuilder.APIEnumLoc:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## 
    ##         
    ##         
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Normal</term><description> 
    ## </description> </item><item><term> 
    ## Uniform</term><description> 
    ## </description> </item><item><term> 
    ## Extreme</term><description> 
    ## </description> </item><item><term> 
    ## Pearson</term><description> 
    ## </description> </item><item><term> 
    ## Trapeziodal</term><description> 
    ## </description> </item></list>
    class APIEnumSize(Enum):
        """
        Members Include: <Normal> <Uniform> <Extreme> <Pearson> <Trapeziodal>
        """
        Normal: int
        Uniform: int
        Extreme: int
        Pearson: int
        Trapeziodal: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> TaperedTabFeatureBuilder.APIEnumSize:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (float) DoubleAnchorX
    ##   the property represents  X value of anchor.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def DoubleAnchorX(self) -> float:
        """
        Getter for property: (float) DoubleAnchorX
          the property represents  X value of anchor.  
             
         
        """
        pass
    
    ## Setter for property: (float) DoubleAnchorX

    ##   the property represents  X value of anchor.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @DoubleAnchorX.setter
    def DoubleAnchorX(self, doubleAnchorX: float):
        """
        Setter for property: (float) DoubleAnchorX
          the property represents  X value of anchor.  
             
         
        """
        pass
    
    ## Getter for property: (float) DoubleAnchorY
    ##   the property represents  Y value of anchor.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def DoubleAnchorY(self) -> float:
        """
        Getter for property: (float) DoubleAnchorY
          the property represents  Y value of anchor.  
             
         
        """
        pass
    
    ## Setter for property: (float) DoubleAnchorY

    ##   the property represents  Y value of anchor.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @DoubleAnchorY.setter
    def DoubleAnchorY(self, doubleAnchorY: float):
        """
        Setter for property: (float) DoubleAnchorY
          the property represents  Y value of anchor.  
             
         
        """
        pass
    
    ## Getter for property: (float) DoubleAnchorZ
    ##   the property represents  Z value of anchor.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def DoubleAnchorZ(self) -> float:
        """
        Getter for property: (float) DoubleAnchorZ
          the property represents  Z value of anchor.  
             
         
        """
        pass
    
    ## Setter for property: (float) DoubleAnchorZ

    ##   the property represents  Z value of anchor.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @DoubleAnchorZ.setter
    def DoubleAnchorZ(self, doubleAnchorZ: float):
        """
        Setter for property: (float) DoubleAnchorZ
          the property represents  Z value of anchor.  
             
         
        """
        pass
    
    ## Getter for property: (float) DoubleAngle
    ##   the property represents  Angle of tab.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def DoubleAngle(self) -> float:
        """
        Getter for property: (float) DoubleAngle
          the property represents  Angle of tab.  
             
         
        """
        pass
    
    ## Setter for property: (float) DoubleAngle

    ##   the property represents  Angle of tab.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @DoubleAngle.setter
    def DoubleAngle(self, angle: float):
        """
        Setter for property: (float) DoubleAngle
          the property represents  Angle of tab.  
             
         
        """
        pass
    
    ## Getter for property: (float) DoubleDepth
    ##   the property represents  depth of tab.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def DoubleDepth(self) -> float:
        """
        Getter for property: (float) DoubleDepth
          the property represents  depth of tab.  
             
         
        """
        pass
    
    ## Setter for property: (float) DoubleDepth

    ##   the property represents  depth of tab.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @DoubleDepth.setter
    def DoubleDepth(self, height: float):
        """
        Setter for property: (float) DoubleDepth
          the property represents  depth of tab.  
             
         
        """
        pass
    
    ## Getter for property: (float) DoubleDirectionI
    ##   the property represents  X value of normal.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def DoubleDirectionI(self) -> float:
        """
        Getter for property: (float) DoubleDirectionI
          the property represents  X value of normal.  
             
         
        """
        pass
    
    ## Setter for property: (float) DoubleDirectionI

    ##   the property represents  X value of normal.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @DoubleDirectionI.setter
    def DoubleDirectionI(self, doubleDirectionI: float):
        """
        Setter for property: (float) DoubleDirectionI
          the property represents  X value of normal.  
             
         
        """
        pass
    
    ## Getter for property: (float) DoubleDirectionJ
    ##   the property represents  Y value of normal.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def DoubleDirectionJ(self) -> float:
        """
        Getter for property: (float) DoubleDirectionJ
          the property represents  Y value of normal.  
             
         
        """
        pass
    
    ## Setter for property: (float) DoubleDirectionJ

    ##   the property represents  Y value of normal.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @DoubleDirectionJ.setter
    def DoubleDirectionJ(self, doubleDirectionJ: float):
        """
        Setter for property: (float) DoubleDirectionJ
          the property represents  Y value of normal.  
             
         
        """
        pass
    
    ## Getter for property: (float) DoubleDirectionK
    ##   the property represents  Z value of normal.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def DoubleDirectionK(self) -> float:
        """
        Getter for property: (float) DoubleDirectionK
          the property represents  Z value of normal.  
             
         
        """
        pass
    
    ## Setter for property: (float) DoubleDirectionK

    ##   the property represents  Z value of normal.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @DoubleDirectionK.setter
    def DoubleDirectionK(self, doubleDirectionK: float):
        """
        Setter for property: (float) DoubleDirectionK
          the property represents  Z value of normal.  
             
         
        """
        pass
    
    ## Getter for property: (float) DoubleKurtosisForm
    ##   the property represents  Form distribution Kurtosis.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def DoubleKurtosisForm(self) -> float:
        """
        Getter for property: (float) DoubleKurtosisForm
          the property represents  Form distribution Kurtosis.  
             
         
        """
        pass
    
    ## Setter for property: (float) DoubleKurtosisForm

    ##   the property represents  Form distribution Kurtosis.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @DoubleKurtosisForm.setter
    def DoubleKurtosisForm(self, doubleKurtosisForm: float):
        """
        Setter for property: (float) DoubleKurtosisForm
          the property represents  Form distribution Kurtosis.  
             
         
        """
        pass
    
    ## Getter for property: (float) DoubleKurtosisLoc
    ##   the property represents  Loc distribution Kurtosis.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def DoubleKurtosisLoc(self) -> float:
        """
        Getter for property: (float) DoubleKurtosisLoc
          the property represents  Loc distribution Kurtosis.  
             
         
        """
        pass
    
    ## Setter for property: (float) DoubleKurtosisLoc

    ##   the property represents  Loc distribution Kurtosis.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @DoubleKurtosisLoc.setter
    def DoubleKurtosisLoc(self, doubleKurtosisLoc: float):
        """
        Setter for property: (float) DoubleKurtosisLoc
          the property represents  Loc distribution Kurtosis.  
             
         
        """
        pass
    
    ## Getter for property: (float) DoubleKurtosisSize
    ##   the property represents  Size distribution Kurtosis.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def DoubleKurtosisSize(self) -> float:
        """
        Getter for property: (float) DoubleKurtosisSize
          the property represents  Size distribution Kurtosis.  
             
         
        """
        pass
    
    ## Setter for property: (float) DoubleKurtosisSize

    ##   the property represents  Size distribution Kurtosis.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @DoubleKurtosisSize.setter
    def DoubleKurtosisSize(self, doubleKurtosisSize: float):
        """
        Setter for property: (float) DoubleKurtosisSize
          the property represents  Size distribution Kurtosis.  
             
         
        """
        pass
    
    ## Getter for property: (float) DoubleLength
    ##   the property represents  length of tab.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def DoubleLength(self) -> float:
        """
        Getter for property: (float) DoubleLength
          the property represents  length of tab.  
             
         
        """
        pass
    
    ## Setter for property: (float) DoubleLength

    ##   the property represents  length of tab.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @DoubleLength.setter
    def DoubleLength(self, distance: float):
        """
        Setter for property: (float) DoubleLength
          the property represents  length of tab.  
             
         
        """
        pass
    
    ## Getter for property: (float) DoubleLengthVectorI
    ##   the property represents  X value of length vector.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def DoubleLengthVectorI(self) -> float:
        """
        Getter for property: (float) DoubleLengthVectorI
          the property represents  X value of length vector.  
             
         
        """
        pass
    
    ## Setter for property: (float) DoubleLengthVectorI

    ##   the property represents  X value of length vector.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @DoubleLengthVectorI.setter
    def DoubleLengthVectorI(self, doubleLengthVectorI: float):
        """
        Setter for property: (float) DoubleLengthVectorI
          the property represents  X value of length vector.  
             
         
        """
        pass
    
    ## Getter for property: (float) DoubleLengthVectorJ
    ##   the property represents  Y value of length vector.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def DoubleLengthVectorJ(self) -> float:
        """
        Getter for property: (float) DoubleLengthVectorJ
          the property represents  Y value of length vector.  
             
         
        """
        pass
    
    ## Setter for property: (float) DoubleLengthVectorJ

    ##   the property represents  Y value of length vector.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @DoubleLengthVectorJ.setter
    def DoubleLengthVectorJ(self, doubleLengthVectorJ: float):
        """
        Setter for property: (float) DoubleLengthVectorJ
          the property represents  Y value of length vector.  
             
         
        """
        pass
    
    ## Getter for property: (float) DoubleLengthVectorK
    ##   the property represents  Z value of length vector.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def DoubleLengthVectorK(self) -> float:
        """
        Getter for property: (float) DoubleLengthVectorK
          the property represents  Z value of length vector.  
             
         
        """
        pass
    
    ## Setter for property: (float) DoubleLengthVectorK

    ##   the property represents  Z value of length vector.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @DoubleLengthVectorK.setter
    def DoubleLengthVectorK(self, doubleLengthVectorK: float):
        """
        Setter for property: (float) DoubleLengthVectorK
          the property represents  Z value of length vector.  
             
         
        """
        pass
    
    ## Getter for property: (float) DoubleSkewnessForm
    ##   the property represents  Form distribution Skewness.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def DoubleSkewnessForm(self) -> float:
        """
        Getter for property: (float) DoubleSkewnessForm
          the property represents  Form distribution Skewness.  
             
         
        """
        pass
    
    ## Setter for property: (float) DoubleSkewnessForm

    ##   the property represents  Form distribution Skewness.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @DoubleSkewnessForm.setter
    def DoubleSkewnessForm(self, doubleSkewnessForm: float):
        """
        Setter for property: (float) DoubleSkewnessForm
          the property represents  Form distribution Skewness.  
             
         
        """
        pass
    
    ## Getter for property: (float) DoubleSkewnessLoc
    ##   the property represents  Loc distribution Skewness.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def DoubleSkewnessLoc(self) -> float:
        """
        Getter for property: (float) DoubleSkewnessLoc
          the property represents  Loc distribution Skewness.  
             
         
        """
        pass
    
    ## Setter for property: (float) DoubleSkewnessLoc

    ##   the property represents  Loc distribution Skewness.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @DoubleSkewnessLoc.setter
    def DoubleSkewnessLoc(self, doubleSkewnessLoc: float):
        """
        Setter for property: (float) DoubleSkewnessLoc
          the property represents  Loc distribution Skewness.  
             
         
        """
        pass
    
    ## Getter for property: (float) DoubleSkewnessSize
    ##   the property represents  Size distribution Skewness.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def DoubleSkewnessSize(self) -> float:
        """
        Getter for property: (float) DoubleSkewnessSize
          the property represents  Size distribution Skewness.  
             
         
        """
        pass
    
    ## Setter for property: (float) DoubleSkewnessSize

    ##   the property represents  Size distribution Skewness.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @DoubleSkewnessSize.setter
    def DoubleSkewnessSize(self, doubleSkewnessSize: float):
        """
        Setter for property: (float) DoubleSkewnessSize
          the property represents  Size distribution Skewness.  
             
         
        """
        pass
    
    ## Getter for property: (float) DoubleWidth
    ##   the property represents  width of tab.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def DoubleWidth(self) -> float:
        """
        Getter for property: (float) DoubleWidth
          the property represents  width of tab.  
             
         
        """
        pass
    
    ## Setter for property: (float) DoubleWidth

    ##   the property represents  width of tab.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @DoubleWidth.setter
    def DoubleWidth(self, width: float):
        """
        Setter for property: (float) DoubleWidth
          the property represents  width of tab.  
             
         
        """
        pass
    
    ## Getter for property: (float) DoubleWidth2
    ##   the property represents  width2 of tab.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def DoubleWidth2(self) -> float:
        """
        Getter for property: (float) DoubleWidth2
          the property represents  width2 of tab.  
             
         
        """
        pass
    
    ## Setter for property: (float) DoubleWidth2

    ##   the property represents  width2 of tab.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @DoubleWidth2.setter
    def DoubleWidth2(self, width2: float):
        """
        Setter for property: (float) DoubleWidth2
          the property represents  width2 of tab.  
             
         
        """
        pass
    
    ## Getter for property: (@link TaperedTabFeatureBuilder.APIEnumForm NXOpen.Vsa.TaperedTabFeatureBuilder.APIEnumForm@endlink) EnumForm
    ##   the property represents  Form distribution type.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return TaperedTabFeatureBuilder.APIEnumForm
    @property
    def EnumForm(self) -> TaperedTabFeatureBuilder.APIEnumForm:
        """
        Getter for property: (@link TaperedTabFeatureBuilder.APIEnumForm NXOpen.Vsa.TaperedTabFeatureBuilder.APIEnumForm@endlink) EnumForm
          the property represents  Form distribution type.  
             
         
        """
        pass
    
    ## Setter for property: (@link TaperedTabFeatureBuilder.APIEnumForm NXOpen.Vsa.TaperedTabFeatureBuilder.APIEnumForm@endlink) EnumForm

    ##   the property represents  Form distribution type.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @EnumForm.setter
    def EnumForm(self, enumForm: TaperedTabFeatureBuilder.APIEnumForm):
        """
        Setter for property: (@link TaperedTabFeatureBuilder.APIEnumForm NXOpen.Vsa.TaperedTabFeatureBuilder.APIEnumForm@endlink) EnumForm
          the property represents  Form distribution type.  
             
         
        """
        pass
    
    ## Getter for property: (@link TaperedTabFeatureBuilder.APIEnumLoc NXOpen.Vsa.TaperedTabFeatureBuilder.APIEnumLoc@endlink) EnumLoc
    ##   the property represents  Loc distribution type.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return TaperedTabFeatureBuilder.APIEnumLoc
    @property
    def EnumLoc(self) -> TaperedTabFeatureBuilder.APIEnumLoc:
        """
        Getter for property: (@link TaperedTabFeatureBuilder.APIEnumLoc NXOpen.Vsa.TaperedTabFeatureBuilder.APIEnumLoc@endlink) EnumLoc
          the property represents  Loc distribution type.  
             
         
        """
        pass
    
    ## Setter for property: (@link TaperedTabFeatureBuilder.APIEnumLoc NXOpen.Vsa.TaperedTabFeatureBuilder.APIEnumLoc@endlink) EnumLoc

    ##   the property represents  Loc distribution type.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @EnumLoc.setter
    def EnumLoc(self, enumLoc: TaperedTabFeatureBuilder.APIEnumLoc):
        """
        Setter for property: (@link TaperedTabFeatureBuilder.APIEnumLoc NXOpen.Vsa.TaperedTabFeatureBuilder.APIEnumLoc@endlink) EnumLoc
          the property represents  Loc distribution type.  
             
         
        """
        pass
    
    ## Getter for property: (@link TaperedTabFeatureBuilder.APIEnumSize NXOpen.Vsa.TaperedTabFeatureBuilder.APIEnumSize@endlink) EnumSize
    ##   the property represents  Size distribution type.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return TaperedTabFeatureBuilder.APIEnumSize
    @property
    def EnumSize(self) -> TaperedTabFeatureBuilder.APIEnumSize:
        """
        Getter for property: (@link TaperedTabFeatureBuilder.APIEnumSize NXOpen.Vsa.TaperedTabFeatureBuilder.APIEnumSize@endlink) EnumSize
          the property represents  Size distribution type.  
             
         
        """
        pass
    
    ## Setter for property: (@link TaperedTabFeatureBuilder.APIEnumSize NXOpen.Vsa.TaperedTabFeatureBuilder.APIEnumSize@endlink) EnumSize

    ##   the property represents  Size distribution type.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @EnumSize.setter
    def EnumSize(self, enumSize: TaperedTabFeatureBuilder.APIEnumSize):
        """
        Setter for property: (@link TaperedTabFeatureBuilder.APIEnumSize NXOpen.Vsa.TaperedTabFeatureBuilder.APIEnumSize@endlink) EnumSize
          the property represents  Size distribution type.  
             
         
        """
        pass
    
    ## Getter for property: (str) StringDescription
    ##   the property represents  tab feature discription.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return str
    @property
    def StringDescription(self) -> str:
        """
        Getter for property: (str) StringDescription
          the property represents  tab feature discription.  
             
         
        """
        pass
    
    ## Setter for property: (str) StringDescription

    ##   the property represents  tab feature discription.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @StringDescription.setter
    def StringDescription(self, stringDescription: str):
        """
        Setter for property: (str) StringDescription
          the property represents  tab feature discription.  
             
         
        """
        pass
    
    ## Getter for property: (str) StringName
    ##   the property represents  tab feature name.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return str
    @property
    def StringName(self) -> str:
        """
        Getter for property: (str) StringName
          the property represents  tab feature name.  
             
         
        """
        pass
    
    ## Setter for property: (str) StringName

    ##   the property represents  tab feature name.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @StringName.setter
    def StringName(self, stringName: str):
        """
        Setter for property: (str) StringName
          the property represents  tab feature name.  
             
         
        """
        pass
    
import NXOpen
##  Represents a Tab feature  <br> To create or edit an instance of this class, use @link NXOpen::Vsa::TaperedTabFeatureBuilder  NXOpen::Vsa::TaperedTabFeatureBuilder @endlink  <br> 
## 
##  <br>  Usable only on Windows <br>  
## 
##   <br>  Created in NX1926.0.0  <br> 

class TaperedTabFeature(NXOpen.NXObject): 
    """ Represents a Tab feature """
    pass


import NXOpen
## 
##     
##      <br> Use the static method in this class to obtain an instance.  <br> 
## 
##  <br>  Usable only on Windows <br>  
## 
##   <br>  Created in NX1899.0.0  <br> 

class Utils(NXOpen.Object): 
    """
    
    """


    ##  The routine creates a point. 
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: None.
    ## <param name="assemblyTag"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    @staticmethod
    def AddFixtureNode(assemblyTag: NXOpen.NXObject) -> None:
        """
         The routine creates a point. 
        """
        pass
    
    ##  The routine creates vsa model. 
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    ## <param name="rootObject"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    def CreateModel(rootObject: NXOpen.NXObject) -> None:
        """
         The routine creates vsa model. 
        """
        pass
    
    ##  The routine creates a point. 
    ##  @return pointTag (@link NXOpen.NXObject NXOpen.NXObject@endlink): .
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: None.
    def CreatePoint() -> NXOpen.NXObject:
        """
         The routine creates a point. 
         @return pointTag (@link NXOpen.NXObject NXOpen.NXObject@endlink): .
        """
        pass
    
    ##  The routine creates points on plane. 
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_vsa_build (" Building VSA model")
    ## <param name="ptrParentFeat"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    def CreateindivisualpointOnFace(ptrParentFeat: NXOpen.NXObject) -> None:
        """
         The routine creates points on plane. 
        """
        pass
    
    ##  The routine deletes all the nodes. 
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def DeleteAllNodes() -> None:
        """
         The routine deletes all the nodes. 
        """
        pass
    
    ##  The routine Deletes Assembly Operation. 
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    ## <param name="assemblyOperation"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    @staticmethod
    def DeleteAssemblyOperation(assemblyOperation: NXOpen.NXObject) -> None:
        """
         The routine Deletes Assembly Operation. 
        """
        pass
    
    ##  The routine Deletes Feature. 
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: None.
    ## <param name="vsaFeature"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    @staticmethod
    def DeleteFeature(vsaFeature: NXOpen.NXObject) -> None:
        """
         The routine Deletes Feature. 
        """
        pass
    
    ##  The routine Deletes Fixture.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: None.
    ## <param name="vsaFixtureTag"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    @staticmethod
    def DeleteFixture(vsaFixtureTag: NXOpen.NXObject) -> None:
        """
         The routine Deletes Fixture.
        """
        pass
    
    ##  The routine Deletes GDTMeasurement Operation. 
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    ## <param name="gdtmeasurementOperation"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    @staticmethod
    def DeleteGDTMeasurementOperation(gdtmeasurementOperation: NXOpen.NXObject) -> None:
        """
         The routine Deletes GDTMeasurement Operation. 
        """
        pass
    
    ##  The routine Deletes Measurement Operation. 
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    ## <param name="measurementOperation"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    @staticmethod
    def DeleteMeasurementOperation(measurementOperation: NXOpen.NXObject) -> None:
        """
         The routine Deletes Measurement Operation. 
        """
        pass
    
    ##  The routine Deletes SubFeature Point. 
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    ## <param name="subFeaturePointTag"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    @staticmethod
    def DeleteSubFeaturePoint(subFeaturePointTag: NXOpen.NXObject) -> None:
        """
         The routine Deletes SubFeature Point. 
        """
        pass
    
    ##  The routine Deletes Tolerance. 
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: None.
    ## <param name="vsaFeature"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    @staticmethod
    def DeleteTolerance(vsaFeature: NXOpen.NXObject) -> None:
        """
         The routine Deletes Tolerance. 
        """
        pass
    
    ##  The routine edit points on plane. 
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_vsa_build (" Building VSA model")
    ## <param name="tagPointSubFeat"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    @staticmethod
    def EditindivisualpointOnFace(tagPointSubFeat: NXOpen.NXObject) -> None:
        """
         The routine edit points on plane. 
        """
        pass
    
    ##  The routine moves Assembly children. 
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    ## <param name="vsaPartTag"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    ## <param name="sourceIndex"> (int) </param>
    ## <param name="targetIndex"> (int) </param>
    def MoveAssemblyChildren(vsaPartTag: NXOpen.NXObject, sourceIndex: int, targetIndex: int) -> None:
        """
         The routine moves Assembly children. 
        """
        pass
    
    ##  The routine moves the fixture element at sourceIndex to targetIndex.
    ##         If sourceIndex is 4 and the targetIndex is 1, the fixture at index 4 will be moved to index number 1.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: None.
    ## <param name="vsaFixtureTag"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    ## <param name="sourceIndex"> (int) </param>
    ## <param name="targetIndex"> (int) </param>
    def MoveFixtureChildren(vsaFixtureTag: NXOpen.NXObject, sourceIndex: int, targetIndex: int) -> None:
        """
         The routine moves the fixture element at sourceIndex to targetIndex.
                If sourceIndex is 4 and the targetIndex is 1, the fixture at index 4 will be moved to index number 1.
        """
        pass
    
    ##  The routine moves part children. 
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    ## <param name="vsaPartTag"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    ## <param name="sourceIndex"> (int) </param>
    ## <param name="targetIndex"> (int) </param>
    def MovePartChildren(vsaPartTag: NXOpen.NXObject, sourceIndex: int, targetIndex: int) -> None:
        """
         The routine moves part children. 
        """
        pass
    
    ##  The routine moves root process children. 
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: None.
    ## <param name="vsaRootProcessTag"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    ## <param name="sourceIndex"> (int) </param>
    ## <param name="targetIndex"> (int) </param>
    def MoveRootProcessChildren(vsaRootProcessTag: NXOpen.NXObject, sourceIndex: int, targetIndex: int) -> None:
        """
         The routine moves root process children. 
        """
        pass
    
    ##  The routine populates vsa model in navigator. 
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def PopulateModelToNavigator() -> None:
        """
         The routine populates vsa model in navigator. 
        """
        pass
    
    ##  The routine refreshes nevigator. 
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def RefreshAllNavigatorViews() -> None:
        """
         The routine refreshes nevigator. 
        """
        pass
    
    ##  The routine renames Assembly Operation. 
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    ## <param name="subFeaturePointTag"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    ## <param name="pstrName"> (str) </param>
    def RenameAssemblyOperation(subFeaturePointTag: NXOpen.NXObject, pstrName: str) -> None:
        """
         The routine renames Assembly Operation. 
        """
        pass
    
    ##  The routine renames Feature. 
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    ## <param name="subFeaturePointTag"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    ## <param name="pstrName"> (str) </param>
    def RenameFeature(subFeaturePointTag: NXOpen.NXObject, pstrName: str) -> None:
        """
         The routine renames Feature. 
        """
        pass
    
    ##  The routine supresses/unpresses GDT Measurement Operation. 
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: None.
    ## <param name="vsaFixture"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    ## <param name="pstrName"> (str) </param>
    def RenameFixture(vsaFixture: NXOpen.NXObject, pstrName: str) -> None:
        """
         The routine supresses/unpresses GDT Measurement Operation. 
        """
        pass
    
    ##  The routine renames Measurement Operation. 
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    ## <param name="subFeaturePointTag"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    ## <param name="pstrName"> (str) </param>
    def RenameMeasurementOperation(subFeaturePointTag: NXOpen.NXObject, pstrName: str) -> None:
        """
         The routine renames Measurement Operation. 
        """
        pass
    
    ##  The routine Rename SubFeature Point. 
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    ## <param name="subFeaturePointTag"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    ## <param name="pstrName"> (str) </param>
    def RenameSubFeaturePoint(subFeaturePointTag: NXOpen.NXObject, pstrName: str) -> None:
        """
         The routine Rename SubFeature Point. 
        """
        pass
    
    ##  The routine validates vsa model. 
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    ## <param name="rootObject"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    @staticmethod
    def SimulateModel(rootObject: NXOpen.NXObject) -> None:
        """
         The routine validates vsa model. 
        """
        pass
    
    ##  The routine supresses/unpresses Assembly Operation. 
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: None.
    ## <param name="assemblyOperation"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    @staticmethod
    def SupressUnsupressAssemblyOperation(assemblyOperation: NXOpen.NXObject) -> None:
        """
         The routine supresses/unpresses Assembly Operation. 
        """
        pass
    
    ##  The routine supresses/unpresses GDT Measurement Operation. 
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: None.
    ## <param name="gdtMeasurementOperation"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    @staticmethod
    def SupressUnsupressGDTMeasurementOperation(gdtMeasurementOperation: NXOpen.NXObject) -> None:
        """
         The routine supresses/unpresses GDT Measurement Operation. 
        """
        pass
    
    ##  The routine supresses/unpresses Measurement Operation. 
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: None.
    ## <param name="measurementOperation"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    @staticmethod
    def SupressUnsupressMeasurementOperation(measurementOperation: NXOpen.NXObject) -> None:
        """
         The routine supresses/unpresses Measurement Operation. 
        """
        pass
    
    ##  The routine validates vsa model. 
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    ## <param name="rootObject"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    @staticmethod
    def ValidateModel(rootObject: NXOpen.NXObject) -> None:
        """
         The routine validates vsa model. 
        """
        pass
    
import NXOpen
## 
##     
##      <br> To create a new instance of this class, use @link NXOpen::Vsa::VsaManager::CreateVsaExportResultBuilder  NXOpen::Vsa::VsaManager::CreateVsaExportResultBuilder @endlink  <br> 
## 
##  <br>  Usable only on Windows <br>  
## 
##   <br>  Created in NX1953.0.0  <br> 

class VsaExportResultBuilder(NXOpen.Builder): 
    """
    
    """


    ## Getter for property: (bool) ContributionMatix
    ##   the property represents Contribution Matix.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return bool
    @property
    def ContributionMatix(self) -> bool:
        """
        Getter for property: (bool) ContributionMatix
          the property represents Contribution Matix.  
             
         
        """
        pass
    
    ## Setter for property: (bool) ContributionMatix

    ##   the property represents Contribution Matix.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @ContributionMatix.setter
    def ContributionMatix(self, boolSwap: bool):
        """
        Setter for property: (bool) ContributionMatix
          the property represents Contribution Matix.  
             
         
        """
        pass
    
    ## Getter for property: (str) FolderPath
    ##   the property represents Folder Path   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return str
    @property
    def FolderPath(self) -> str:
        """
        Getter for property: (str) FolderPath
          the property represents Folder Path   
            
         
        """
        pass
    
    ## Setter for property: (str) FolderPath

    ##   the property represents Folder Path   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @FolderPath.setter
    def FolderPath(self, name: str):
        """
        Setter for property: (str) FolderPath
          the property represents Folder Path   
            
         
        """
        pass
    
    ## Getter for property: (bool) MeasurementValues
    ##   the property represents Measurement Values.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return bool
    @property
    def MeasurementValues(self) -> bool:
        """
        Getter for property: (bool) MeasurementValues
          the property represents Measurement Values.  
             
         
        """
        pass
    
    ## Setter for property: (bool) MeasurementValues

    ##   the property represents Measurement Values.  
    ##      
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @MeasurementValues.setter
    def MeasurementValues(self, boolSwap: bool):
        """
        Setter for property: (bool) MeasurementValues
          the property represents Measurement Values.  
             
         
        """
        pass
    
    ## Getter for property: (bool) StatisticalParamenter
    ##   the property represents Folder Statistical Paramenter   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return bool
    @property
    def StatisticalParamenter(self) -> bool:
        """
        Getter for property: (bool) StatisticalParamenter
          the property represents Folder Statistical Paramenter   
            
         
        """
        pass
    
    ## Setter for property: (bool) StatisticalParamenter

    ##   the property represents Folder Statistical Paramenter   
    ##     
    ##  
    ## Setter License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @StatisticalParamenter.setter
    def StatisticalParamenter(self, boolSwap: bool):
        """
        Setter for property: (bool) StatisticalParamenter
          the property represents Folder Statistical Paramenter   
            
         
        """
        pass
    
    ##  To print measurement statistics in report
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ## <param name="folderpath"> (str) </param>
    def PrintMeasurementStatistics(builder: VsaExportResultBuilder, folderpath: str) -> None:
        """
         To print measurement statistics in report
        """
        pass
    
    ##  To print measurement values in report
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ## <param name="folderpath"> (str) </param>
    def PrintMeasurementValues(builder: VsaExportResultBuilder, folderpath: str) -> None:
        """
         To print measurement values in report
        """
        pass
    
    ##  To print Total tolerance cotribution in report
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_vsa_build (" Building VSA model")
    ## 
    ## <param name="folderpath"> (str) </param>
    def PrintTotalToleranceContribution(builder: VsaExportResultBuilder, folderpath: str) -> None:
        """
         To print Total tolerance cotribution in report
        """
        pass
    
import NXOpen
##  Represents a Export Result  <br> To create or edit an instance of this class, use @link NXOpen::Vsa::VsaExportResultBuilder  NXOpen::Vsa::VsaExportResultBuilder @endlink  <br> 
## 
##  <br>  Usable only on Windows <br>  
## 
##   <br>  Created in NX1953.0.0  <br> 

class VsaExportResult(NXOpen.NXObject): 
    """ Represents a Export Result """
    pass


## @package NXOpen.Vsa
## Classes, Enums and Structs under NXOpen.Vsa namespace

##  @link AssemblyOperationBuilderAPIEnumDistributionFloatType NXOpen.Vsa.AssemblyOperationBuilderAPIEnumDistributionFloatType @endlink is an alias for @link AssemblyOperationBuilder.APIEnumDistributionFloatType NXOpen.Vsa.AssemblyOperationBuilder.APIEnumDistributionFloatType@endlink
AssemblyOperationBuilderAPIEnumDistributionFloatType = AssemblyOperationBuilder.APIEnumDistributionFloatType


##  @link BallFeatureBuilderAPIEnumForm NXOpen.Vsa.BallFeatureBuilderAPIEnumForm @endlink is an alias for @link BallFeatureBuilder.APIEnumForm NXOpen.Vsa.BallFeatureBuilder.APIEnumForm@endlink
BallFeatureBuilderAPIEnumForm = BallFeatureBuilder.APIEnumForm


##  @link BallFeatureBuilderAPIEnumLoc NXOpen.Vsa.BallFeatureBuilderAPIEnumLoc @endlink is an alias for @link BallFeatureBuilder.APIEnumLoc NXOpen.Vsa.BallFeatureBuilder.APIEnumLoc@endlink
BallFeatureBuilderAPIEnumLoc = BallFeatureBuilder.APIEnumLoc


##  @link BallFeatureBuilderAPIEnumSize NXOpen.Vsa.BallFeatureBuilderAPIEnumSize @endlink is an alias for @link BallFeatureBuilder.APIEnumSize NXOpen.Vsa.BallFeatureBuilder.APIEnumSize@endlink
BallFeatureBuilderAPIEnumSize = BallFeatureBuilder.APIEnumSize


##  @link FixturePlaneFeatureBuilderAPIFormType NXOpen.Vsa.FixturePlaneFeatureBuilderAPIFormType @endlink is an alias for @link FixturePlaneFeatureBuilder.APIFormType NXOpen.Vsa.FixturePlaneFeatureBuilder.APIFormType@endlink
FixturePlaneFeatureBuilderAPIFormType = FixturePlaneFeatureBuilder.APIFormType


##  @link FixturePlaneFeatureBuilderAPILocType NXOpen.Vsa.FixturePlaneFeatureBuilderAPILocType @endlink is an alias for @link FixturePlaneFeatureBuilder.APILocType NXOpen.Vsa.FixturePlaneFeatureBuilder.APILocType@endlink
FixturePlaneFeatureBuilderAPILocType = FixturePlaneFeatureBuilder.APILocType


##  @link FixturePlaneFeatureBuilderAPISizeType NXOpen.Vsa.FixturePlaneFeatureBuilderAPISizeType @endlink is an alias for @link FixturePlaneFeatureBuilder.APISizeType NXOpen.Vsa.FixturePlaneFeatureBuilder.APISizeType@endlink
FixturePlaneFeatureBuilderAPISizeType = FixturePlaneFeatureBuilder.APISizeType


##  @link GDTMeasurementOperationBuilderAPIEnumNameFormat NXOpen.Vsa.GDTMeasurementOperationBuilderAPIEnumNameFormat @endlink is an alias for @link GDTMeasurementOperationBuilder.APIEnumNameFormat NXOpen.Vsa.GDTMeasurementOperationBuilder.APIEnumNameFormat@endlink
GDTMeasurementOperationBuilderAPIEnumNameFormat = GDTMeasurementOperationBuilder.APIEnumNameFormat


##  @link GDTMeasurementOperationBuilderAPIGeometricChar NXOpen.Vsa.GDTMeasurementOperationBuilderAPIGeometricChar @endlink is an alias for @link GDTMeasurementOperationBuilder.APIGeometricChar NXOpen.Vsa.GDTMeasurementOperationBuilder.APIGeometricChar@endlink
GDTMeasurementOperationBuilderAPIGeometricChar = GDTMeasurementOperationBuilder.APIGeometricChar


##  @link GeneralSurfaceFeatureBuilderAPIEnumForm NXOpen.Vsa.GeneralSurfaceFeatureBuilderAPIEnumForm @endlink is an alias for @link GeneralSurfaceFeatureBuilder.APIEnumForm NXOpen.Vsa.GeneralSurfaceFeatureBuilder.APIEnumForm@endlink
GeneralSurfaceFeatureBuilderAPIEnumForm = GeneralSurfaceFeatureBuilder.APIEnumForm


##  @link GeneralSurfaceFeatureBuilderAPIEnumLoc NXOpen.Vsa.GeneralSurfaceFeatureBuilderAPIEnumLoc @endlink is an alias for @link GeneralSurfaceFeatureBuilder.APIEnumLoc NXOpen.Vsa.GeneralSurfaceFeatureBuilder.APIEnumLoc@endlink
GeneralSurfaceFeatureBuilderAPIEnumLoc = GeneralSurfaceFeatureBuilder.APIEnumLoc


##  @link GeneralSurfaceFeatureBuilderAPIEnumSize NXOpen.Vsa.GeneralSurfaceFeatureBuilderAPIEnumSize @endlink is an alias for @link GeneralSurfaceFeatureBuilder.APIEnumSize NXOpen.Vsa.GeneralSurfaceFeatureBuilder.APIEnumSize@endlink
GeneralSurfaceFeatureBuilderAPIEnumSize = GeneralSurfaceFeatureBuilder.APIEnumSize


##  @link HoleFeatureBuilderAPIEnumForm NXOpen.Vsa.HoleFeatureBuilderAPIEnumForm @endlink is an alias for @link HoleFeatureBuilder.APIEnumForm NXOpen.Vsa.HoleFeatureBuilder.APIEnumForm@endlink
HoleFeatureBuilderAPIEnumForm = HoleFeatureBuilder.APIEnumForm


##  @link HoleFeatureBuilderAPIEnumLoc NXOpen.Vsa.HoleFeatureBuilderAPIEnumLoc @endlink is an alias for @link HoleFeatureBuilder.APIEnumLoc NXOpen.Vsa.HoleFeatureBuilder.APIEnumLoc@endlink
HoleFeatureBuilderAPIEnumLoc = HoleFeatureBuilder.APIEnumLoc


##  @link HoleFeatureBuilderAPIEnumSize NXOpen.Vsa.HoleFeatureBuilderAPIEnumSize @endlink is an alias for @link HoleFeatureBuilder.APIEnumSize NXOpen.Vsa.HoleFeatureBuilder.APIEnumSize@endlink
HoleFeatureBuilderAPIEnumSize = HoleFeatureBuilder.APIEnumSize


##  @link HolePatternFeatureBuilderAPIEnumForm NXOpen.Vsa.HolePatternFeatureBuilderAPIEnumForm @endlink is an alias for @link HolePatternFeatureBuilder.APIEnumForm NXOpen.Vsa.HolePatternFeatureBuilder.APIEnumForm@endlink
HolePatternFeatureBuilderAPIEnumForm = HolePatternFeatureBuilder.APIEnumForm


##  @link HolePatternFeatureBuilderAPIEnumLoc NXOpen.Vsa.HolePatternFeatureBuilderAPIEnumLoc @endlink is an alias for @link HolePatternFeatureBuilder.APIEnumLoc NXOpen.Vsa.HolePatternFeatureBuilder.APIEnumLoc@endlink
HolePatternFeatureBuilderAPIEnumLoc = HolePatternFeatureBuilder.APIEnumLoc


##  @link HolePatternFeatureBuilderAPIEnumSize NXOpen.Vsa.HolePatternFeatureBuilderAPIEnumSize @endlink is an alias for @link HolePatternFeatureBuilder.APIEnumSize NXOpen.Vsa.HolePatternFeatureBuilder.APIEnumSize@endlink
HolePatternFeatureBuilderAPIEnumSize = HolePatternFeatureBuilder.APIEnumSize


##  @link MeasurementOperationBuilderAPIEnumLimitType NXOpen.Vsa.MeasurementOperationBuilderAPIEnumLimitType @endlink is an alias for @link MeasurementOperationBuilder.APIEnumLimitType NXOpen.Vsa.MeasurementOperationBuilder.APIEnumLimitType@endlink
MeasurementOperationBuilderAPIEnumLimitType = MeasurementOperationBuilder.APIEnumLimitType


##  @link MeasurementOperationBuilderAPIEnumMeasurementType NXOpen.Vsa.MeasurementOperationBuilderAPIEnumMeasurementType @endlink is an alias for @link MeasurementOperationBuilder.APIEnumMeasurementType NXOpen.Vsa.MeasurementOperationBuilder.APIEnumMeasurementType@endlink
MeasurementOperationBuilderAPIEnumMeasurementType = MeasurementOperationBuilder.APIEnumMeasurementType


##  @link MeasurementOperationBuilderAPIEnumNameFormat NXOpen.Vsa.MeasurementOperationBuilderAPIEnumNameFormat @endlink is an alias for @link MeasurementOperationBuilder.APIEnumNameFormat NXOpen.Vsa.MeasurementOperationBuilder.APIEnumNameFormat@endlink
MeasurementOperationBuilderAPIEnumNameFormat = MeasurementOperationBuilder.APIEnumNameFormat


##  @link PinFeatureBuilderAPIEnumForm NXOpen.Vsa.PinFeatureBuilderAPIEnumForm @endlink is an alias for @link PinFeatureBuilder.APIEnumForm NXOpen.Vsa.PinFeatureBuilder.APIEnumForm@endlink
PinFeatureBuilderAPIEnumForm = PinFeatureBuilder.APIEnumForm


##  @link PinFeatureBuilderAPIEnumLoc NXOpen.Vsa.PinFeatureBuilderAPIEnumLoc @endlink is an alias for @link PinFeatureBuilder.APIEnumLoc NXOpen.Vsa.PinFeatureBuilder.APIEnumLoc@endlink
PinFeatureBuilderAPIEnumLoc = PinFeatureBuilder.APIEnumLoc


##  @link PinFeatureBuilderAPIEnumSize NXOpen.Vsa.PinFeatureBuilderAPIEnumSize @endlink is an alias for @link PinFeatureBuilder.APIEnumSize NXOpen.Vsa.PinFeatureBuilder.APIEnumSize@endlink
PinFeatureBuilderAPIEnumSize = PinFeatureBuilder.APIEnumSize


##  @link PinPatternFeatureBuilderAPIEnumForm NXOpen.Vsa.PinPatternFeatureBuilderAPIEnumForm @endlink is an alias for @link PinPatternFeatureBuilder.APIEnumForm NXOpen.Vsa.PinPatternFeatureBuilder.APIEnumForm@endlink
PinPatternFeatureBuilderAPIEnumForm = PinPatternFeatureBuilder.APIEnumForm


##  @link PinPatternFeatureBuilderAPIEnumLoc NXOpen.Vsa.PinPatternFeatureBuilderAPIEnumLoc @endlink is an alias for @link PinPatternFeatureBuilder.APIEnumLoc NXOpen.Vsa.PinPatternFeatureBuilder.APIEnumLoc@endlink
PinPatternFeatureBuilderAPIEnumLoc = PinPatternFeatureBuilder.APIEnumLoc


##  @link PinPatternFeatureBuilderAPIEnumSize NXOpen.Vsa.PinPatternFeatureBuilderAPIEnumSize @endlink is an alias for @link PinPatternFeatureBuilder.APIEnumSize NXOpen.Vsa.PinPatternFeatureBuilder.APIEnumSize@endlink
PinPatternFeatureBuilderAPIEnumSize = PinPatternFeatureBuilder.APIEnumSize


##  @link PlaneFeatureBuilderAPIEnumForm NXOpen.Vsa.PlaneFeatureBuilderAPIEnumForm @endlink is an alias for @link PlaneFeatureBuilder.APIEnumForm NXOpen.Vsa.PlaneFeatureBuilder.APIEnumForm@endlink
PlaneFeatureBuilderAPIEnumForm = PlaneFeatureBuilder.APIEnumForm


##  @link PlaneFeatureBuilderAPIEnumLoc NXOpen.Vsa.PlaneFeatureBuilderAPIEnumLoc @endlink is an alias for @link PlaneFeatureBuilder.APIEnumLoc NXOpen.Vsa.PlaneFeatureBuilder.APIEnumLoc@endlink
PlaneFeatureBuilderAPIEnumLoc = PlaneFeatureBuilder.APIEnumLoc


##  @link PlaneFeatureBuilderAPIEnumSize NXOpen.Vsa.PlaneFeatureBuilderAPIEnumSize @endlink is an alias for @link PlaneFeatureBuilder.APIEnumSize NXOpen.Vsa.PlaneFeatureBuilder.APIEnumSize@endlink
PlaneFeatureBuilderAPIEnumSize = PlaneFeatureBuilder.APIEnumSize


##  @link PointFeatureBuilderAPIEnumForm NXOpen.Vsa.PointFeatureBuilderAPIEnumForm @endlink is an alias for @link PointFeatureBuilder.APIEnumForm NXOpen.Vsa.PointFeatureBuilder.APIEnumForm@endlink
PointFeatureBuilderAPIEnumForm = PointFeatureBuilder.APIEnumForm


##  @link PointFeatureBuilderAPIEnumLoc NXOpen.Vsa.PointFeatureBuilderAPIEnumLoc @endlink is an alias for @link PointFeatureBuilder.APIEnumLoc NXOpen.Vsa.PointFeatureBuilder.APIEnumLoc@endlink
PointFeatureBuilderAPIEnumLoc = PointFeatureBuilder.APIEnumLoc


##  @link PointFeatureBuilderAPIEnumSize NXOpen.Vsa.PointFeatureBuilderAPIEnumSize @endlink is an alias for @link PointFeatureBuilder.APIEnumSize NXOpen.Vsa.PointFeatureBuilder.APIEnumSize@endlink
PointFeatureBuilderAPIEnumSize = PointFeatureBuilder.APIEnumSize


##  @link PointSubFeatureBuilderAPIEnumPointType NXOpen.Vsa.PointSubFeatureBuilderAPIEnumPointType @endlink is an alias for @link PointSubFeatureBuilder.APIEnumPointType NXOpen.Vsa.PointSubFeatureBuilder.APIEnumPointType@endlink
PointSubFeatureBuilderAPIEnumPointType = PointSubFeatureBuilder.APIEnumPointType


##  @link SimulationPreferencesBuilderAPIEnumDistributionFloatType NXOpen.Vsa.SimulationPreferencesBuilderAPIEnumDistributionFloatType @endlink is an alias for @link SimulationPreferencesBuilder.APIEnumDistributionFloatType NXOpen.Vsa.SimulationPreferencesBuilder.APIEnumDistributionFloatType@endlink
SimulationPreferencesBuilderAPIEnumDistributionFloatType = SimulationPreferencesBuilder.APIEnumDistributionFloatType


##  @link SlotFeatureBuilderAPIEnumForm NXOpen.Vsa.SlotFeatureBuilderAPIEnumForm @endlink is an alias for @link SlotFeatureBuilder.APIEnumForm NXOpen.Vsa.SlotFeatureBuilder.APIEnumForm@endlink
SlotFeatureBuilderAPIEnumForm = SlotFeatureBuilder.APIEnumForm


##  @link SlotFeatureBuilderAPIEnumLoc NXOpen.Vsa.SlotFeatureBuilderAPIEnumLoc @endlink is an alias for @link SlotFeatureBuilder.APIEnumLoc NXOpen.Vsa.SlotFeatureBuilder.APIEnumLoc@endlink
SlotFeatureBuilderAPIEnumLoc = SlotFeatureBuilder.APIEnumLoc


##  @link SlotFeatureBuilderAPIEnumSize NXOpen.Vsa.SlotFeatureBuilderAPIEnumSize @endlink is an alias for @link SlotFeatureBuilder.APIEnumSize NXOpen.Vsa.SlotFeatureBuilder.APIEnumSize@endlink
SlotFeatureBuilderAPIEnumSize = SlotFeatureBuilder.APIEnumSize


##  @link SocketFeatureBuilderAPIEnumForm NXOpen.Vsa.SocketFeatureBuilderAPIEnumForm @endlink is an alias for @link SocketFeatureBuilder.APIEnumForm NXOpen.Vsa.SocketFeatureBuilder.APIEnumForm@endlink
SocketFeatureBuilderAPIEnumForm = SocketFeatureBuilder.APIEnumForm


##  @link SocketFeatureBuilderAPIEnumLoc NXOpen.Vsa.SocketFeatureBuilderAPIEnumLoc @endlink is an alias for @link SocketFeatureBuilder.APIEnumLoc NXOpen.Vsa.SocketFeatureBuilder.APIEnumLoc@endlink
SocketFeatureBuilderAPIEnumLoc = SocketFeatureBuilder.APIEnumLoc


##  @link SocketFeatureBuilderAPIEnumSize NXOpen.Vsa.SocketFeatureBuilderAPIEnumSize @endlink is an alias for @link SocketFeatureBuilder.APIEnumSize NXOpen.Vsa.SocketFeatureBuilder.APIEnumSize@endlink
SocketFeatureBuilderAPIEnumSize = SocketFeatureBuilder.APIEnumSize


##  @link TabFeatureBuilderAPIEnumForm NXOpen.Vsa.TabFeatureBuilderAPIEnumForm @endlink is an alias for @link TabFeatureBuilder.APIEnumForm NXOpen.Vsa.TabFeatureBuilder.APIEnumForm@endlink
TabFeatureBuilderAPIEnumForm = TabFeatureBuilder.APIEnumForm


##  @link TabFeatureBuilderAPIEnumLoc NXOpen.Vsa.TabFeatureBuilderAPIEnumLoc @endlink is an alias for @link TabFeatureBuilder.APIEnumLoc NXOpen.Vsa.TabFeatureBuilder.APIEnumLoc@endlink
TabFeatureBuilderAPIEnumLoc = TabFeatureBuilder.APIEnumLoc


##  @link TabFeatureBuilderAPIEnumSize NXOpen.Vsa.TabFeatureBuilderAPIEnumSize @endlink is an alias for @link TabFeatureBuilder.APIEnumSize NXOpen.Vsa.TabFeatureBuilder.APIEnumSize@endlink
TabFeatureBuilderAPIEnumSize = TabFeatureBuilder.APIEnumSize


##  @link TaperedHoleFeatureBuilderAPIEnumForm NXOpen.Vsa.TaperedHoleFeatureBuilderAPIEnumForm @endlink is an alias for @link TaperedHoleFeatureBuilder.APIEnumForm NXOpen.Vsa.TaperedHoleFeatureBuilder.APIEnumForm@endlink
TaperedHoleFeatureBuilderAPIEnumForm = TaperedHoleFeatureBuilder.APIEnumForm


##  @link TaperedHoleFeatureBuilderAPIEnumLoc NXOpen.Vsa.TaperedHoleFeatureBuilderAPIEnumLoc @endlink is an alias for @link TaperedHoleFeatureBuilder.APIEnumLoc NXOpen.Vsa.TaperedHoleFeatureBuilder.APIEnumLoc@endlink
TaperedHoleFeatureBuilderAPIEnumLoc = TaperedHoleFeatureBuilder.APIEnumLoc


##  @link TaperedHoleFeatureBuilderAPIEnumSize NXOpen.Vsa.TaperedHoleFeatureBuilderAPIEnumSize @endlink is an alias for @link TaperedHoleFeatureBuilder.APIEnumSize NXOpen.Vsa.TaperedHoleFeatureBuilder.APIEnumSize@endlink
TaperedHoleFeatureBuilderAPIEnumSize = TaperedHoleFeatureBuilder.APIEnumSize


##  @link TaperedHolePatternFeatureBuilderAPIEnumForm NXOpen.Vsa.TaperedHolePatternFeatureBuilderAPIEnumForm @endlink is an alias for @link TaperedHolePatternFeatureBuilder.APIEnumForm NXOpen.Vsa.TaperedHolePatternFeatureBuilder.APIEnumForm@endlink
TaperedHolePatternFeatureBuilderAPIEnumForm = TaperedHolePatternFeatureBuilder.APIEnumForm


##  @link TaperedHolePatternFeatureBuilderAPIEnumLoc NXOpen.Vsa.TaperedHolePatternFeatureBuilderAPIEnumLoc @endlink is an alias for @link TaperedHolePatternFeatureBuilder.APIEnumLoc NXOpen.Vsa.TaperedHolePatternFeatureBuilder.APIEnumLoc@endlink
TaperedHolePatternFeatureBuilderAPIEnumLoc = TaperedHolePatternFeatureBuilder.APIEnumLoc


##  @link TaperedHolePatternFeatureBuilderAPIEnumSize NXOpen.Vsa.TaperedHolePatternFeatureBuilderAPIEnumSize @endlink is an alias for @link TaperedHolePatternFeatureBuilder.APIEnumSize NXOpen.Vsa.TaperedHolePatternFeatureBuilder.APIEnumSize@endlink
TaperedHolePatternFeatureBuilderAPIEnumSize = TaperedHolePatternFeatureBuilder.APIEnumSize


##  @link TaperedPinFeatureBuilderAPIEnumForm NXOpen.Vsa.TaperedPinFeatureBuilderAPIEnumForm @endlink is an alias for @link TaperedPinFeatureBuilder.APIEnumForm NXOpen.Vsa.TaperedPinFeatureBuilder.APIEnumForm@endlink
TaperedPinFeatureBuilderAPIEnumForm = TaperedPinFeatureBuilder.APIEnumForm


##  @link TaperedPinFeatureBuilderAPIEnumLoc NXOpen.Vsa.TaperedPinFeatureBuilderAPIEnumLoc @endlink is an alias for @link TaperedPinFeatureBuilder.APIEnumLoc NXOpen.Vsa.TaperedPinFeatureBuilder.APIEnumLoc@endlink
TaperedPinFeatureBuilderAPIEnumLoc = TaperedPinFeatureBuilder.APIEnumLoc


##  @link TaperedPinFeatureBuilderAPIEnumSize NXOpen.Vsa.TaperedPinFeatureBuilderAPIEnumSize @endlink is an alias for @link TaperedPinFeatureBuilder.APIEnumSize NXOpen.Vsa.TaperedPinFeatureBuilder.APIEnumSize@endlink
TaperedPinFeatureBuilderAPIEnumSize = TaperedPinFeatureBuilder.APIEnumSize


##  @link TaperedPinPatternFeatureBuilderAPIEnumForm NXOpen.Vsa.TaperedPinPatternFeatureBuilderAPIEnumForm @endlink is an alias for @link TaperedPinPatternFeatureBuilder.APIEnumForm NXOpen.Vsa.TaperedPinPatternFeatureBuilder.APIEnumForm@endlink
TaperedPinPatternFeatureBuilderAPIEnumForm = TaperedPinPatternFeatureBuilder.APIEnumForm


##  @link TaperedPinPatternFeatureBuilderAPIEnumLoc NXOpen.Vsa.TaperedPinPatternFeatureBuilderAPIEnumLoc @endlink is an alias for @link TaperedPinPatternFeatureBuilder.APIEnumLoc NXOpen.Vsa.TaperedPinPatternFeatureBuilder.APIEnumLoc@endlink
TaperedPinPatternFeatureBuilderAPIEnumLoc = TaperedPinPatternFeatureBuilder.APIEnumLoc


##  @link TaperedPinPatternFeatureBuilderAPIEnumSize NXOpen.Vsa.TaperedPinPatternFeatureBuilderAPIEnumSize @endlink is an alias for @link TaperedPinPatternFeatureBuilder.APIEnumSize NXOpen.Vsa.TaperedPinPatternFeatureBuilder.APIEnumSize@endlink
TaperedPinPatternFeatureBuilderAPIEnumSize = TaperedPinPatternFeatureBuilder.APIEnumSize


##  @link TaperedSlotFeatureBuilderAPIEnumForm NXOpen.Vsa.TaperedSlotFeatureBuilderAPIEnumForm @endlink is an alias for @link TaperedSlotFeatureBuilder.APIEnumForm NXOpen.Vsa.TaperedSlotFeatureBuilder.APIEnumForm@endlink
TaperedSlotFeatureBuilderAPIEnumForm = TaperedSlotFeatureBuilder.APIEnumForm


##  @link TaperedSlotFeatureBuilderAPIEnumLoc NXOpen.Vsa.TaperedSlotFeatureBuilderAPIEnumLoc @endlink is an alias for @link TaperedSlotFeatureBuilder.APIEnumLoc NXOpen.Vsa.TaperedSlotFeatureBuilder.APIEnumLoc@endlink
TaperedSlotFeatureBuilderAPIEnumLoc = TaperedSlotFeatureBuilder.APIEnumLoc


##  @link TaperedSlotFeatureBuilderAPIEnumSize NXOpen.Vsa.TaperedSlotFeatureBuilderAPIEnumSize @endlink is an alias for @link TaperedSlotFeatureBuilder.APIEnumSize NXOpen.Vsa.TaperedSlotFeatureBuilder.APIEnumSize@endlink
TaperedSlotFeatureBuilderAPIEnumSize = TaperedSlotFeatureBuilder.APIEnumSize


##  @link TaperedTabFeatureBuilderAPIEnumForm NXOpen.Vsa.TaperedTabFeatureBuilderAPIEnumForm @endlink is an alias for @link TaperedTabFeatureBuilder.APIEnumForm NXOpen.Vsa.TaperedTabFeatureBuilder.APIEnumForm@endlink
TaperedTabFeatureBuilderAPIEnumForm = TaperedTabFeatureBuilder.APIEnumForm


##  @link TaperedTabFeatureBuilderAPIEnumLoc NXOpen.Vsa.TaperedTabFeatureBuilderAPIEnumLoc @endlink is an alias for @link TaperedTabFeatureBuilder.APIEnumLoc NXOpen.Vsa.TaperedTabFeatureBuilder.APIEnumLoc@endlink
TaperedTabFeatureBuilderAPIEnumLoc = TaperedTabFeatureBuilder.APIEnumLoc


##  @link TaperedTabFeatureBuilderAPIEnumSize NXOpen.Vsa.TaperedTabFeatureBuilderAPIEnumSize @endlink is an alias for @link TaperedTabFeatureBuilder.APIEnumSize NXOpen.Vsa.TaperedTabFeatureBuilder.APIEnumSize@endlink
TaperedTabFeatureBuilderAPIEnumSize = TaperedTabFeatureBuilder.APIEnumSize


