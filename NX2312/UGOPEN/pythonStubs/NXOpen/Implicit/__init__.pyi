from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
##  
##     Represents a Implicit.BlockBuilder.
##     It will create a block inside the Implicit task environment.
##      <br> To create a new instance of this class, use @link NXOpen::Implicit::ImplicitOperationCollection::CreateBlockBuilder  NXOpen::Implicit::ImplicitOperationCollection::CreateBlockBuilder @endlink  <br> 
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
## Height.Value </term> <description> 
##  
## 100 (millimeters part), 4 (inches part) </description> </item> 
## 
## <item><term> 
##  
## Length.Value </term> <description> 
##  
## 100 (millimeters part), 4 (inches part) </description> </item> 
## 
## <item><term> 
##  
## Width.Value </term> <description> 
##  
## 100 (millimeters part), 4 (inches part) </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX1953.0.0  <br> 

class BlockBuilder(OperationBuilder): 
    """ 
    Represents a Implicit.BlockBuilder.
    It will create a block inside the Implicit task environment.
    """


    ## Getter for property: (bool) Associative
    ##   the option to keep the block associative with the specified Origin And Orientation.  
    ##   
    ##             this does not apply to selection methods Dynamic, Inferred, Absolute CSYS, and CSYS of Current View.
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return bool
    @property
    def Associative(self) -> bool:
        """
        Getter for property: (bool) Associative
          the option to keep the block associative with the specified Origin And Orientation.  
          
                    this does not apply to selection methods Dynamic, Inferred, Absolute CSYS, and CSYS of Current View.
                  
         
        """
        pass
    
    ## Setter for property: (bool) Associative

    ##   the option to keep the block associative with the specified Origin And Orientation.  
    ##   
    ##             this does not apply to selection methods Dynamic, Inferred, Absolute CSYS, and CSYS of Current View.
    ##           
    ##  
    ## Setter License requirements: nx_implicit (" NX Implicit Modeling")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @Associative.setter
    def Associative(self, associativeOrigin: bool):
        """
        Setter for property: (bool) Associative
          the option to keep the block associative with the specified Origin And Orientation.  
          
                    this does not apply to selection methods Dynamic, Inferred, Absolute CSYS, and CSYS of Current View.
                  
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Height
    ##   the height ZC   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Height(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Height
          the height ZC   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Length
    ##   the length XC   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Length(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Length
          the length XC   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.CartesianCoordinateSystem NXOpen.CartesianCoordinateSystem@endlink) OriginAndOrientation
    ##   the origin Point   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.CartesianCoordinateSystem
    @property
    def OriginAndOrientation(self) -> NXOpen.CartesianCoordinateSystem:
        """
        Getter for property: (@link NXOpen.CartesianCoordinateSystem NXOpen.CartesianCoordinateSystem@endlink) OriginAndOrientation
          the origin Point   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.CartesianCoordinateSystem NXOpen.CartesianCoordinateSystem@endlink) OriginAndOrientation

    ##   the origin Point   
    ##     
    ##  
    ## Setter License requirements: nx_implicit (" NX Implicit Modeling")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @OriginAndOrientation.setter
    def OriginAndOrientation(self, csys: NXOpen.CartesianCoordinateSystem):
        """
        Setter for property: (@link NXOpen.CartesianCoordinateSystem NXOpen.CartesianCoordinateSystem@endlink) OriginAndOrientation
          the origin Point   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Width
    ##   the width YC   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Width(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Width
          the width YC   
            
         
        """
        pass
    
##  Represents a Block Implicit Operation.  <br> To create or edit an instance of this class, use @link NXOpen::Implicit::BlockBuilder  NXOpen::Implicit::BlockBuilder @endlink  <br> 
## 
##   <br>  Created in NX1953.0.0  <br> 

class Block(ImplicitOperation): 
    """ Represents a Block Implicit Operation. """
    pass


import NXOpen
## 
##     Represents an Implicit.BooleanBuilder.
##     It will create a boolean operation (Unite, Subtract or Intersect) on the selected bodies.
##      <br> This is abstract class.  <br> 
## 
##   <br>  Created in NX1953.0.0  <br> 

class BooleanBuilder(OperationBuilder): 
    """
    Represents an Implicit.BooleanBuilder.
    It will create a boolean operation (Unite, Subtract or Intersect) on the selected bodies.
    """


    ## Getter for property: (int) BlendFactor
    ##   the blend factor   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return int
    @property
    def BlendFactor(self) -> int:
        """
        Getter for property: (int) BlendFactor
          the blend factor   
            
         
        """
        pass
    
    ## Setter for property: (int) BlendFactor

    ##   the blend factor   
    ##     
    ##  
    ## Setter License requirements: nx_implicit (" NX Implicit Modeling")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @BlendFactor.setter
    def BlendFactor(self, blendFactor: int):
        """
        Setter for property: (int) BlendFactor
          the blend factor   
            
         
        """
        pass
    
    ## Getter for property: (bool) CreateBlends
    ##   the create blends option  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX1980.0.0.  Use @link NXOpen::Implicit::BooleanBuilder::BlendFactor NXOpen::Implicit::BooleanBuilder::BlendFactor@endlink  instead. If this returns value greater than 0 means blends were created.  <br> 

    ## @return bool
    @property
    def CreateBlends(self) -> bool:
        """
        Getter for property: (bool) CreateBlends
          the create blends option  
            
         
        """
        pass
    
    ## Setter for property: (bool) CreateBlends

    ##   the create blends option  
    ##     
    ##  
    ## Setter License requirements: nx_implicit (" NX Implicit Modeling")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX1980.0.0.  Use @link NXOpen::Implicit::BooleanBuilder::BlendFactor NXOpen::Implicit::BooleanBuilder::BlendFactor@endlink  instead. Given any value greater than 0 indicates we need to create blends.  <br> 

    @CreateBlends.setter
    def CreateBlends(self, createBlends: bool):
        """
        Setter for property: (bool) CreateBlends
          the create blends option  
            
         
        """
        pass
    
    ## Getter for property: (bool) KeepTarget
    ##   the keep target option  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return bool
    @property
    def KeepTarget(self) -> bool:
        """
        Getter for property: (bool) KeepTarget
          the keep target option  
            
         
        """
        pass
    
    ## Setter for property: (bool) KeepTarget

    ##   the keep target option  
    ##     
    ##  
    ## Setter License requirements: nx_implicit (" NX Implicit Modeling")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @KeepTarget.setter
    def KeepTarget(self, keepTarget: bool):
        """
        Setter for property: (bool) KeepTarget
          the keep target option  
            
         
        """
        pass
    
    ## Getter for property: (bool) KeepTool
    ##   the keep tool option  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return bool
    @property
    def KeepTool(self) -> bool:
        """
        Getter for property: (bool) KeepTool
          the keep tool option  
            
         
        """
        pass
    
    ## Setter for property: (bool) KeepTool

    ##   the keep tool option  
    ##     
    ##  
    ## Setter License requirements: nx_implicit (" NX Implicit Modeling")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @KeepTool.setter
    def KeepTool(self, keepTool: bool):
        """
        Setter for property: (bool) KeepTool
          the keep tool option  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) TargetBody
    ##   the target body   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.ScCollector
    @property
    def TargetBody(self) -> NXOpen.ScCollector:
        """
        Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) TargetBody
          the target body   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) ToolBody
    ##   the tool body   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.ScCollector
    @property
    def ToolBody(self) -> NXOpen.ScCollector:
        """
        Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) ToolBody
          the tool body   
            
         
        """
        pass
    
##  Represents a Boolean Implicit Operation.  <br> This is an abstract class, and cannot be instantiated.  <br> 
## 
##   <br>  Created in NX1953.0.0  <br> 

class Boolean(ImplicitOperation): 
    """ Represents a Boolean Implicit Operation. """
    pass


import NXOpen
## 
##     Represents a Implicit.CartesianPatternBuilder.
##     The unit cell body will be scaled to the specified unit cell size and patterned in X, Y and Z orientation until it fills the boundary body (or it voids).
##      <br> To create a new instance of this class, use @link NXOpen::Implicit::ImplicitOperationCollection::CreateCartesianPatternBuilder  NXOpen::Implicit::ImplicitOperationCollection::CreateCartesianPatternBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## BlendFactor </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## BoundaryConditionOption </term> <description> 
##  
## SolidVolume </description> </item> 
## 
## <item><term> 
##  
## EdgeLength.Value </term> <description> 
##  
## 10 (millimeters part), 0.4 (inches part) </description> </item> 
## 
## <item><term> 
##  
## SizeX.Value </term> <description> 
##  
## 10 (millimeters part), 0.4 (inches part) </description> </item> 
## 
## <item><term> 
##  
## SizeY.Value </term> <description> 
##  
## 10 (millimeters part), 0.4 (inches part) </description> </item> 
## 
## <item><term> 
##  
## SizeZ.Value </term> <description> 
##  
## 10 (millimeters part), 0.4 (inches part) </description> </item> 
## 
## <item><term> 
##  
## UniformCubeFlag </term> <description> 
##  
## true </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX2007.0.0  <br> 

class CartesianPatternBuilder(OperationBuilder): 
    """
    Represents a Implicit.CartesianPatternBuilder.
    The unit cell body will be scaled to the specified unit cell size and patterned in X, Y and Z orientation until it fills the boundary body (or it voids).
    """


    ##  Boundary Condition options
    ##  Solid region 
    class BoundaryConditionOptionType(Enum):
        """
        Members Include: <SolidVolume> <VoidVolume> <VoidVolumeAndUnite>
        """
        SolidVolume: int
        VoidVolume: int
        VoidVolumeAndUnite: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> CartesianPatternBuilder.BoundaryConditionOptionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (int) BlendFactor
    ##   the blend factor.  
    ##   
    ##         factor to adjust the blend of intersections between tool and target body. 
    ##         No Blend(0) - to - large Blends(100)
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return int
    @property
    def BlendFactor(self) -> int:
        """
        Getter for property: (int) BlendFactor
          the blend factor.  
          
                factor to adjust the blend of intersections between tool and target body. 
                No Blend(0) - to - large Blends(100)
                  
         
        """
        pass
    
    ## Setter for property: (int) BlendFactor

    ##   the blend factor.  
    ##   
    ##         factor to adjust the blend of intersections between tool and target body. 
    ##         No Blend(0) - to - large Blends(100)
    ##           
    ##  
    ## Setter License requirements: nx_implicit (" NX Implicit Modeling")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @BlendFactor.setter
    def BlendFactor(self, blendFactor: int):
        """
        Setter for property: (int) BlendFactor
          the blend factor.  
          
                factor to adjust the blend of intersections between tool and target body. 
                No Blend(0) - to - large Blends(100)
                  
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) BoundaryBody
    ##   the input body.  
    ##   
    ##         As boundary body a solid body that is either an implicit body (within feature/TE)
    ##         or a parametric body from outside the TE can be provided.
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return NXOpen.ScCollector
    @property
    def BoundaryBody(self) -> NXOpen.ScCollector:
        """
        Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) BoundaryBody
          the input body.  
          
                As boundary body a solid body that is either an implicit body (within feature/TE)
                or a parametric body from outside the TE can be provided.
                  
         
        """
        pass
    
    ## Getter for property: (@link CartesianPatternBuilder.BoundaryConditionOptionType NXOpen.Implicit.CartesianPatternBuilder.BoundaryConditionOptionType@endlink) BoundaryConditionOption
    ##   the Boundary Condition Option
    ##         Solid volume fill, void volume fill or void volume fill with unite to outer body
    ##           
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return CartesianPatternBuilder.BoundaryConditionOptionType
    @property
    def BoundaryConditionOption(self) -> CartesianPatternBuilder.BoundaryConditionOptionType:
        """
        Getter for property: (@link CartesianPatternBuilder.BoundaryConditionOptionType NXOpen.Implicit.CartesianPatternBuilder.BoundaryConditionOptionType@endlink) BoundaryConditionOption
          the Boundary Condition Option
                Solid volume fill, void volume fill or void volume fill with unite to outer body
                  
            
         
        """
        pass
    
    ## Setter for property: (@link CartesianPatternBuilder.BoundaryConditionOptionType NXOpen.Implicit.CartesianPatternBuilder.BoundaryConditionOptionType@endlink) BoundaryConditionOption

    ##   the Boundary Condition Option
    ##         Solid volume fill, void volume fill or void volume fill with unite to outer body
    ##           
    ##     
    ##  
    ## Setter License requirements: nx_implicit (" NX Implicit Modeling")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @BoundaryConditionOption.setter
    def BoundaryConditionOption(self, boundaryConditionOption: CartesianPatternBuilder.BoundaryConditionOptionType):
        """
        Setter for property: (@link CartesianPatternBuilder.BoundaryConditionOptionType NXOpen.Implicit.CartesianPatternBuilder.BoundaryConditionOptionType@endlink) BoundaryConditionOption
          the Boundary Condition Option
                Solid volume fill, void volume fill or void volume fill with unite to outer body
                  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) EdgeLength
    ##   the edge length.  
    ##   
    ##         Edge length in X, Y and Z direction if it is a uniform cube.
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def EdgeLength(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) EdgeLength
          the edge length.  
          
                Edge length in X, Y and Z direction if it is a uniform cube.
                  
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) LocationAndOrientation
    ##   the location and orientation of the seed cell.  
    ##   
    ##         The orientation can be inferred from objects inside or outside the TE.
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return NXOpen.CoordinateSystem
    @property
    def LocationAndOrientation(self) -> NXOpen.CoordinateSystem:
        """
        Getter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) LocationAndOrientation
          the location and orientation of the seed cell.  
          
                The orientation can be inferred from objects inside or outside the TE.
                  
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) LocationAndOrientation

    ##   the location and orientation of the seed cell.  
    ##   
    ##         The orientation can be inferred from objects inside or outside the TE.
    ##           
    ##  
    ## Setter License requirements: nx_implicit (" NX Implicit Modeling")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @LocationAndOrientation.setter
    def LocationAndOrientation(self, locationAndOrientation: NXOpen.CoordinateSystem):
        """
        Setter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) LocationAndOrientation
          the location and orientation of the seed cell.  
          
                The orientation can be inferred from objects inside or outside the TE.
                  
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) SizeX
    ##   the size x.  
    ##   
    ##         Edge length in X if it is a non-uniform cube.
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def SizeX(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) SizeX
          the size x.  
          
                Edge length in X if it is a non-uniform cube.
                  
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) SizeY
    ##   the size y.  
    ##   
    ##         Edge length in Y if it is a non-uniform cube.
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def SizeY(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) SizeY
          the size y.  
          
                Edge length in Y if it is a non-uniform cube.
                  
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) SizeZ
    ##   the size z.  
    ##   
    ##         Edge length in Z if it is a non-uniform cube.
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def SizeZ(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) SizeZ
          the size z.  
          
                Edge length in Z if it is a non-uniform cube.
                  
         
        """
        pass
    
    ## Getter for property: (bool) UniformCubeFlag
    ##   the uniform cube toggle.  
    ##   
    ##         A uniform cube with one edge length in all three
    ##         directions can be defined or specify the length for each axis separately.
    ##         ture for uniform cube false otherwise.
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return bool
    @property
    def UniformCubeFlag(self) -> bool:
        """
        Getter for property: (bool) UniformCubeFlag
          the uniform cube toggle.  
          
                A uniform cube with one edge length in all three
                directions can be defined or specify the length for each axis separately.
                ture for uniform cube false otherwise.
                  
         
        """
        pass
    
    ## Setter for property: (bool) UniformCubeFlag

    ##   the uniform cube toggle.  
    ##   
    ##         A uniform cube with one edge length in all three
    ##         directions can be defined or specify the length for each axis separately.
    ##         ture for uniform cube false otherwise.
    ##           
    ##  
    ## Setter License requirements: nx_implicit (" NX Implicit Modeling")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @UniformCubeFlag.setter
    def UniformCubeFlag(self, uniformCubeFlag: bool):
        """
        Setter for property: (bool) UniformCubeFlag
          the uniform cube toggle.  
          
                A uniform cube with one edge length in all three
                directions can be defined or specify the length for each axis separately.
                ture for uniform cube false otherwise.
                  
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) UnitCellBody
    ##   the unit cell body.  
    ##   
    ##         The unit cell body will be scaled to the specified unit cell size.
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return NXOpen.ScCollector
    @property
    def UnitCellBody(self) -> NXOpen.ScCollector:
        """
        Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) UnitCellBody
          the unit cell body.  
          
                The unit cell body will be scaled to the specified unit cell size.
                  
         
        """
        pass
    
##  Represents a Cartesian Pattern Implicit Operation.  <br> To create or edit an instance of this class, use @link NXOpen::Implicit::CartesianPatternBuilder  NXOpen::Implicit::CartesianPatternBuilder @endlink  <br> 
## 
##   <br>  Created in NX2007.0.0  <br> 

class CartesianPattern(ImplicitOperation): 
    """ Represents a Cartesian Pattern Implicit Operation. """
    pass


import NXOpen
##  
##     Represents a Implicit.ConeBuilder.
##     It will create a cone inside the Implicit task environment.
##      <br> To create a new instance of this class, use @link NXOpen::Implicit::ImplicitOperationCollection::CreateConeBuilder  NXOpen::Implicit::ImplicitOperationCollection::CreateConeBuilder @endlink  <br> 
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
## BaseDiameter.Value </term> <description> 
##  
## 50 (millimeters part), 2 (inches part) </description> </item> 
## 
## <item><term> 
##  
## Height.Value </term> <description> 
##  
## 25 (millimeters part), 1 (inches part) </description> </item> 
## 
## <item><term> 
##  
## TopDiameter.Value </term> <description> 
##  
## 0 (millimeters part), 0 (inches part) </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX1953.0.0  <br> 

class ConeBuilder(OperationBuilder): 
    """ 
    Represents a Implicit.ConeBuilder.
    It will create a cone inside the Implicit task environment.
    """


    ## Getter for property: (bool) Associative
    ##   the option to keep the cone associative with the specified Center And Orientation.  
    ##   
    ##             this does not apply to selection methods Dynamic, Inferred, Absolute CSYS, and CSYS of Current View.
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return bool
    @property
    def Associative(self) -> bool:
        """
        Getter for property: (bool) Associative
          the option to keep the cone associative with the specified Center And Orientation.  
          
                    this does not apply to selection methods Dynamic, Inferred, Absolute CSYS, and CSYS of Current View.
                  
         
        """
        pass
    
    ## Setter for property: (bool) Associative

    ##   the option to keep the cone associative with the specified Center And Orientation.  
    ##   
    ##             this does not apply to selection methods Dynamic, Inferred, Absolute CSYS, and CSYS of Current View.
    ##           
    ##  
    ## Setter License requirements: nx_implicit (" NX Implicit Modeling")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @Associative.setter
    def Associative(self, associativeCenter: bool):
        """
        Setter for property: (bool) Associative
          the option to keep the cone associative with the specified Center And Orientation.  
          
                    this does not apply to selection methods Dynamic, Inferred, Absolute CSYS, and CSYS of Current View.
                  
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) BaseDiameter
    ##   the cone base diameter   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def BaseDiameter(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) BaseDiameter
          the cone base diameter   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.CartesianCoordinateSystem NXOpen.CartesianCoordinateSystem@endlink) CenterAndOrientation
    ##   the origin Point   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.CartesianCoordinateSystem
    @property
    def CenterAndOrientation(self) -> NXOpen.CartesianCoordinateSystem:
        """
        Getter for property: (@link NXOpen.CartesianCoordinateSystem NXOpen.CartesianCoordinateSystem@endlink) CenterAndOrientation
          the origin Point   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.CartesianCoordinateSystem NXOpen.CartesianCoordinateSystem@endlink) CenterAndOrientation

    ##   the origin Point   
    ##     
    ##  
    ## Setter License requirements: nx_implicit (" NX Implicit Modeling")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @CenterAndOrientation.setter
    def CenterAndOrientation(self, csys: NXOpen.CartesianCoordinateSystem):
        """
        Setter for property: (@link NXOpen.CartesianCoordinateSystem NXOpen.CartesianCoordinateSystem@endlink) CenterAndOrientation
          the origin Point   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Height
    ##   the height   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Height(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Height
          the height   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) TopDiameter
    ##   the cone top diameter   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def TopDiameter(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) TopDiameter
          the cone top diameter   
            
         
        """
        pass
    
##  Represents a Cone Implicit Operation.  <br> To create or edit an instance of this class, use @link NXOpen::Implicit::ConeBuilder  NXOpen::Implicit::ConeBuilder @endlink  <br> 
## 
##   <br>  Created in NX1953.0.0  <br> 

class Cone(ImplicitOperation): 
    """ Represents a Cone Implicit Operation. """
    pass


import NXOpen
##  
##     Represents a Implicit.CylinderBuilder.
##     It will create a cylinder inside the Implicit task environment.
##      <br> To create a new instance of this class, use @link NXOpen::Implicit::ImplicitOperationCollection::CreateCylinderBuilder  NXOpen::Implicit::ImplicitOperationCollection::CreateCylinderBuilder @endlink  <br> 
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
## Diameter.Value </term> <description> 
##  
## 50 (millimeters part), 2 (inches part) </description> </item> 
## 
## <item><term> 
##  
## Height.Value </term> <description> 
##  
## 100 (millimeters part), 4 (inches part) </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX1953.0.0  <br> 

class CylinderBuilder(OperationBuilder): 
    """ 
    Represents a Implicit.CylinderBuilder.
    It will create a cylinder inside the Implicit task environment.
    """


    ## Getter for property: (bool) Associative
    ##   the option to keep the cylinder associative with the specified Center And Orientation.  
    ##   
    ##             this does not apply to selection methods Dynamic, Inferred, Absolute CSYS, and CSYS of Current View.
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return bool
    @property
    def Associative(self) -> bool:
        """
        Getter for property: (bool) Associative
          the option to keep the cylinder associative with the specified Center And Orientation.  
          
                    this does not apply to selection methods Dynamic, Inferred, Absolute CSYS, and CSYS of Current View.
                  
         
        """
        pass
    
    ## Setter for property: (bool) Associative

    ##   the option to keep the cylinder associative with the specified Center And Orientation.  
    ##   
    ##             this does not apply to selection methods Dynamic, Inferred, Absolute CSYS, and CSYS of Current View.
    ##           
    ##  
    ## Setter License requirements: nx_implicit (" NX Implicit Modeling")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @Associative.setter
    def Associative(self, associativeCenter: bool):
        """
        Setter for property: (bool) Associative
          the option to keep the cylinder associative with the specified Center And Orientation.  
          
                    this does not apply to selection methods Dynamic, Inferred, Absolute CSYS, and CSYS of Current View.
                  
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.CartesianCoordinateSystem NXOpen.CartesianCoordinateSystem@endlink) CenterAndOrientation
    ##   the origin Point   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.CartesianCoordinateSystem
    @property
    def CenterAndOrientation(self) -> NXOpen.CartesianCoordinateSystem:
        """
        Getter for property: (@link NXOpen.CartesianCoordinateSystem NXOpen.CartesianCoordinateSystem@endlink) CenterAndOrientation
          the origin Point   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.CartesianCoordinateSystem NXOpen.CartesianCoordinateSystem@endlink) CenterAndOrientation

    ##   the origin Point   
    ##     
    ##  
    ## Setter License requirements: nx_implicit (" NX Implicit Modeling")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @CenterAndOrientation.setter
    def CenterAndOrientation(self, csys: NXOpen.CartesianCoordinateSystem):
        """
        Setter for property: (@link NXOpen.CartesianCoordinateSystem NXOpen.CartesianCoordinateSystem@endlink) CenterAndOrientation
          the origin Point   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Diameter
    ##   the cylinder diameter   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Diameter(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Diameter
          the cylinder diameter   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Height
    ##   the height   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Height(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Height
          the height   
            
         
        """
        pass
    
##  Represents a Cylinder Implicit Operation.  <br> To create or edit an instance of this class, use @link NXOpen::Implicit::CylinderBuilder  NXOpen::Implicit::CylinderBuilder @endlink  <br> 
## 
##   <br>  Created in NX1953.0.0  <br> 

class Cylinder(ImplicitOperation): 
    """ Represents a Cylinder Implicit Operation. """
    pass


import NXOpen
## 
##     Represents a Implicit.CylindricalPatternBuilder.
##     The Unit cell will be patterned around the cylinder circumference in unit cell x direction, 
##     along cylinder axis in unit cell y direction and 
##     stacked up radial with the specified number of layers in unit cell z direction.
##      <br> To create a new instance of this class, use @link NXOpen::Implicit::ImplicitOperationCollection::CreateCylindricalPatternBuilder  NXOpen::Implicit::ImplicitOperationCollection::CreateCylindricalPatternBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## Diameter.Value </term> <description> 
##  
## 50 (millimeters part), 2 (inches part) </description> </item> 
## 
## <item><term> 
##  
## Height.Value </term> <description> 
##  
## 100 (millimeters part), 4 (inches part) </description> </item> 
## 
## <item><term> 
##  
## NumberOfCellsAroundCircumferenceExp.Value </term> <description> 
##  
## 10 </description> </item> 
## 
## <item><term> 
##  
## NumberOfRadialLayersExp.Value </term> <description> 
##  
## 1 </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX2007.0.0  <br> 

class CylindricalPatternBuilder(OperationBuilder): 
    """
    Represents a Implicit.CylindricalPatternBuilder.
    The Unit cell will be patterned around the cylinder circumference in unit cell x direction, 
    along cylinder axis in unit cell y direction and 
    stacked up radial with the specified number of layers in unit cell z direction.
    """


    ## Getter for property: (@link NXOpen.CartesianCoordinateSystem NXOpen.CartesianCoordinateSystem@endlink) CenterAndOrientation
    ##   the specified Point 
    ##         Allows you to locate and orient the cylinder.  
    ##   
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return NXOpen.CartesianCoordinateSystem
    @property
    def CenterAndOrientation(self) -> NXOpen.CartesianCoordinateSystem:
        """
        Getter for property: (@link NXOpen.CartesianCoordinateSystem NXOpen.CartesianCoordinateSystem@endlink) CenterAndOrientation
          the specified Point 
                Allows you to locate and orient the cylinder.  
          
                  
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.CartesianCoordinateSystem NXOpen.CartesianCoordinateSystem@endlink) CenterAndOrientation

    ##   the specified Point 
    ##         Allows you to locate and orient the cylinder.  
    ##   
    ##           
    ##  
    ## Setter License requirements: nx_implicit (" NX Implicit Modeling")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @CenterAndOrientation.setter
    def CenterAndOrientation(self, csys: NXOpen.CartesianCoordinateSystem):
        """
        Setter for property: (@link NXOpen.CartesianCoordinateSystem NXOpen.CartesianCoordinateSystem@endlink) CenterAndOrientation
          the specified Point 
                Allows you to locate and orient the cylinder.  
          
                  
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Diameter
    ##   the cylinder diameter   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Diameter(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Diameter
          the cylinder diameter   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Height
    ##   the cylinder height   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Height(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Height
          the cylinder height   
            
         
        """
        pass
    
    ## Getter for property: (int) NumberOfCellsAroundCircumference
    ##   the cell count around circumference 
    ##         the number of cells around the circumference of the specified inner cylinder.  
    ##   
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return int
    @property
    def NumberOfCellsAroundCircumference(self) -> int:
        """
        Getter for property: (int) NumberOfCellsAroundCircumference
          the cell count around circumference 
                the number of cells around the circumference of the specified inner cylinder.  
          
                  
         
        """
        pass
    
    ## Setter for property: (int) NumberOfCellsAroundCircumference

    ##   the cell count around circumference 
    ##         the number of cells around the circumference of the specified inner cylinder.  
    ##   
    ##           
    ##  
    ## Setter License requirements: nx_implicit (" NX Implicit Modeling")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @NumberOfCellsAroundCircumference.setter
    def NumberOfCellsAroundCircumference(self, numCellsAroundCircumference: int):
        """
        Setter for property: (int) NumberOfCellsAroundCircumference
          the cell count around circumference 
                the number of cells around the circumference of the specified inner cylinder.  
          
                  
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) NumberOfCellsAroundCircumferenceExp
    ##   the cell count around circumference in expression
    ##         the number of cells around the circumference of the specified inner cylinder.  
    ##   
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def NumberOfCellsAroundCircumferenceExp(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) NumberOfCellsAroundCircumferenceExp
          the cell count around circumference in expression
                the number of cells around the circumference of the specified inner cylinder.  
          
                  
         
        """
        pass
    
    ## Getter for property: (int) NumberOfRadialLayers
    ##   the radial layers 
    ##         the layers to be stacked up on the outside of the specified inner cylinder.  
    ##   
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return int
    @property
    def NumberOfRadialLayers(self) -> int:
        """
        Getter for property: (int) NumberOfRadialLayers
          the radial layers 
                the layers to be stacked up on the outside of the specified inner cylinder.  
          
                  
         
        """
        pass
    
    ## Setter for property: (int) NumberOfRadialLayers

    ##   the radial layers 
    ##         the layers to be stacked up on the outside of the specified inner cylinder.  
    ##   
    ##           
    ##  
    ## Setter License requirements: nx_implicit (" NX Implicit Modeling")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @NumberOfRadialLayers.setter
    def NumberOfRadialLayers(self, numRadialLayers: int):
        """
        Setter for property: (int) NumberOfRadialLayers
          the radial layers 
                the layers to be stacked up on the outside of the specified inner cylinder.  
          
                  
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) NumberOfRadialLayersExp
    ##   the radial layers in expression
    ##         the layers to be stacked up on the outside of the specified inner cylinder.  
    ##   
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def NumberOfRadialLayersExp(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) NumberOfRadialLayersExp
          the radial layers in expression
                the layers to be stacked up on the outside of the specified inner cylinder.  
          
                  
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) UnitCellBody
    ##   the unit cell body.  
    ##   
    ##         The unit cell body will be scaled uniform so that cell size is around circumference divided by cell count.
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return NXOpen.ScCollector
    @property
    def UnitCellBody(self) -> NXOpen.ScCollector:
        """
        Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) UnitCellBody
          the unit cell body.  
          
                The unit cell body will be scaled uniform so that cell size is around circumference divided by cell count.
                  
         
        """
        pass
    
##  Represents a Cylindrical Pattern Implicit Operation.  <br> To create or edit an instance of this class, use @link NXOpen::Implicit::CylindricalPatternBuilder  NXOpen::Implicit::CylindricalPatternBuilder @endlink  <br> 
## 
##   <br>  Created in NX2007.0.0  <br> 

class CylindricalPattern(ImplicitOperation): 
    """ Represents a Cylindrical Pattern Implicit Operation. """
    pass


##  Represents a Diamond Implicit Operation.  <br> To create or edit an instance of this class, use @link NXOpen::Implicit::EquationOperationBuilder  NXOpen::Implicit::EquationOperationBuilder @endlink  <br> 
## 
##   <br>  Created in NX1953.0.0  <br> 

class Diamond(EquationOperation): 
    """ Represents a Diamond Implicit Operation. """
    pass


import NXOpen
##  
##     Represents a Implicit.EllipsoidBuilder.
##     It will create an Ellipsoid inside the Implicit task environment.
##      <br> To create a new instance of this class, use @link NXOpen::Implicit::ImplicitOperationCollection::CreateEllipsoidBuilder  NXOpen::Implicit::ImplicitOperationCollection::CreateEllipsoidBuilder @endlink  <br> 
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
## Height.Value </term> <description> 
##  
## 100 (millimeters part), 4 (inches part) </description> </item> 
## 
## <item><term> 
##  
## Length.Value </term> <description> 
##  
## 100 (millimeters part), 4 (inches part) </description> </item> 
## 
## <item><term> 
##  
## Width.Value </term> <description> 
##  
## 100 (millimeters part), 4 (inches part) </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX1953.0.0  <br> 

class EllipsoidBuilder(OperationBuilder): 
    """ 
    Represents a Implicit.EllipsoidBuilder.
    It will create an Ellipsoid inside the Implicit task environment.
    """


    ## Getter for property: (bool) Associative
    ##   the option to keep the ellipsoid associative with the specified Center Point and Orientation.  
    ##   
    ##             this does not apply to selection methods Dynamic, Inferred, Absolute CSYS, and CSYS of Current View.
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return bool
    @property
    def Associative(self) -> bool:
        """
        Getter for property: (bool) Associative
          the option to keep the ellipsoid associative with the specified Center Point and Orientation.  
          
                    this does not apply to selection methods Dynamic, Inferred, Absolute CSYS, and CSYS of Current View.
                  
         
        """
        pass
    
    ## Setter for property: (bool) Associative

    ##   the option to keep the ellipsoid associative with the specified Center Point and Orientation.  
    ##   
    ##             this does not apply to selection methods Dynamic, Inferred, Absolute CSYS, and CSYS of Current View.
    ##           
    ##  
    ## Setter License requirements: nx_implicit (" NX Implicit Modeling")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @Associative.setter
    def Associative(self, associativeCenterPoint: bool):
        """
        Setter for property: (bool) Associative
          the option to keep the ellipsoid associative with the specified Center Point and Orientation.  
          
                    this does not apply to selection methods Dynamic, Inferred, Absolute CSYS, and CSYS of Current View.
                  
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.CartesianCoordinateSystem NXOpen.CartesianCoordinateSystem@endlink) CenterAndOrientation
    ##   the origin Point   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.CartesianCoordinateSystem
    @property
    def CenterAndOrientation(self) -> NXOpen.CartesianCoordinateSystem:
        """
        Getter for property: (@link NXOpen.CartesianCoordinateSystem NXOpen.CartesianCoordinateSystem@endlink) CenterAndOrientation
          the origin Point   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.CartesianCoordinateSystem NXOpen.CartesianCoordinateSystem@endlink) CenterAndOrientation

    ##   the origin Point   
    ##     
    ##  
    ## Setter License requirements: nx_implicit (" NX Implicit Modeling")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @CenterAndOrientation.setter
    def CenterAndOrientation(self, csys: NXOpen.CartesianCoordinateSystem):
        """
        Setter for property: (@link NXOpen.CartesianCoordinateSystem NXOpen.CartesianCoordinateSystem@endlink) CenterAndOrientation
          the origin Point   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Height
    ##   the height along Z Axis    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Height(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Height
          the height along Z Axis    
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Length
    ##   the length along X Axis    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Length(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Length
          the length along X Axis    
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Width
    ##   the width along Y Axis    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Width(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Width
          the width along Y Axis    
            
         
        """
        pass
    
##  Represents a Ellipsoid Implicit Operation.  <br> To create or edit an instance of this class, use @link NXOpen::Implicit::EllipsoidBuilder  NXOpen::Implicit::EllipsoidBuilder @endlink  <br> 
## 
##   <br>  Created in NX1953.0.0  <br> 

class Ellipsoid(ImplicitOperation): 
    """ Represents a Ellipsoid Implicit Operation. """
    pass


import NXOpen
import NXOpen.ModlUtils
## 
##     Represents a Implicit.EquationOperationBuilder.
##     It will create an Implicit surfaces derived from equations with three variables (x, y, and z) in the 3D space.
##     The definition of an implicit surface is that a coordinate is located on the surface if the equation results in zero.
##      <br> To create a new instance of this class, use @link NXOpen::Implicit::ImplicitOperationCollection::CreateEquationOperationBuilder  NXOpen::Implicit::ImplicitOperationCollection::CreateEquationOperationBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## BlendFactor </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## BoundaryConditionOption </term> <description> 
##  
## SolidVolume </description> </item> 
## 
## <item><term> 
##  
## EdgeLength.Value </term> <description> 
##  
## 10 (millimeters part), 0.4 (inches part) </description> </item> 
## 
## <item><term> 
##  
## KFactor </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## SizeX.Value </term> <description> 
##  
## 10 (millimeters part), 0.4 (inches part) </description> </item> 
## 
## <item><term> 
##  
## SizeY.Value </term> <description> 
##  
## 10 (millimeters part), 0.4 (inches part) </description> </item> 
## 
## <item><term> 
##  
## SizeZ.Value </term> <description> 
##  
## 10 (millimeters part), 0.4 (inches part) </description> </item> 
## 
## <item><term> 
##  
## Thickness.Value </term> <description> 
##  
## 1.0 (millimeters part), 0.04 (inches part) </description> </item> 
## 
## <item><term> 
##  
## ThicknessFactor.Value </term> <description> 
##  
## 0.5 </description> </item> 
## 
## <item><term> 
##  
## ThicknessMethod </term> <description> 
##  
## Absolute </description> </item> 
## 
## <item><term> 
##  
## TypeOfEquation </term> <description> 
##  
## Gyroid </description> </item> 
## 
## <item><term> 
##  
## UniformCubeFlag </term> <description> 
##  
## true </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX1926.0.0  <br> 

class EquationOperationBuilder(OperationBuilder): 
    """
    Represents a Implicit.EquationOperationBuilder.
    It will create an Implicit surfaces derived from equations with three variables (x, y, and z) in the 3D space.
    The definition of an implicit surface is that a coordinate is located on the surface if the equation results in zero.
    """


    ##  Boundary Condition options
    ##  Solid region 
    class BoundaryConditionOptionType(Enum):
        """
        Members Include: <SolidVolume> <VoidVolume> <VoidVolumeAndUnite>
        """
        SolidVolume: int
        VoidVolume: int
        VoidVolumeAndUnite: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> EquationOperationBuilder.BoundaryConditionOptionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Implicit Operation type 
    ##  Gyroid  
    class EquationType(Enum):
        """
        Members Include: <Gyroid> <Schwarz> <Diamond> <Neovius> <Schoen> <Scherk> <Lidinoid> <SplitP>
        """
        Gyroid: int
        Schwarz: int
        Diamond: int
        Neovius: int
        Schoen: int
        Scherk: int
        Lidinoid: int
        SplitP: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> EquationOperationBuilder.EquationType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Thickness methods
    ##  Absolute thickness 
    class ThicknessMethodType(Enum):
        """
        Members Include: <Absolute> <AbsoluteVariable> <Relative> <Approximate>
        """
        Absolute: int
        AbsoluteVariable: int
        Relative: int
        Approximate: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> EquationOperationBuilder.ThicknessMethodType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (int) BlendFactor
    ##   the blend factor.  
    ##   
    ##         factor to adjust the blend of intersections between tool and target body. 
    ##         No Blend(0) - to - large Blends(100)
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return int
    @property
    def BlendFactor(self) -> int:
        """
        Getter for property: (int) BlendFactor
          the blend factor.  
          
                factor to adjust the blend of intersections between tool and target body. 
                No Blend(0) - to - large Blends(100)
                  
         
        """
        pass
    
    ## Setter for property: (int) BlendFactor

    ##   the blend factor.  
    ##   
    ##         factor to adjust the blend of intersections between tool and target body. 
    ##         No Blend(0) - to - large Blends(100)
    ##           
    ##  
    ## Setter License requirements: nx_implicit (" NX Implicit Modeling")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @BlendFactor.setter
    def BlendFactor(self, blendFactor: int):
        """
        Setter for property: (int) BlendFactor
          the blend factor.  
          
                factor to adjust the blend of intersections between tool and target body. 
                No Blend(0) - to - large Blends(100)
                  
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) BoundaryBody
    ##   the input body.  
    ##   
    ##         Since the equation itself is defined infinitely a boundary body needs to limit its shape.
    ##         As boundary body a solid body that is either an implicit body (within feature/TE)
    ##         or a parametric body from outside the TE can be provided.
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.ScCollector
    @property
    def BoundaryBody(self) -> NXOpen.ScCollector:
        """
        Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) BoundaryBody
          the input body.  
          
                Since the equation itself is defined infinitely a boundary body needs to limit its shape.
                As boundary body a solid body that is either an implicit body (within feature/TE)
                or a parametric body from outside the TE can be provided.
                  
         
        """
        pass
    
    ## Getter for property: (@link EquationOperationBuilder.BoundaryConditionOptionType NXOpen.Implicit.EquationOperationBuilder.BoundaryConditionOptionType@endlink) BoundaryConditionOption
    ##   the Boundary Condition Option
    ##         Solid volume fill, void volume fill or void volume fill with unite to outer body
    ##           
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return EquationOperationBuilder.BoundaryConditionOptionType
    @property
    def BoundaryConditionOption(self) -> EquationOperationBuilder.BoundaryConditionOptionType:
        """
        Getter for property: (@link EquationOperationBuilder.BoundaryConditionOptionType NXOpen.Implicit.EquationOperationBuilder.BoundaryConditionOptionType@endlink) BoundaryConditionOption
          the Boundary Condition Option
                Solid volume fill, void volume fill or void volume fill with unite to outer body
                  
            
         
        """
        pass
    
    ## Setter for property: (@link EquationOperationBuilder.BoundaryConditionOptionType NXOpen.Implicit.EquationOperationBuilder.BoundaryConditionOptionType@endlink) BoundaryConditionOption

    ##   the Boundary Condition Option
    ##         Solid volume fill, void volume fill or void volume fill with unite to outer body
    ##           
    ##     
    ##  
    ## Setter License requirements: nx_implicit (" NX Implicit Modeling")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @BoundaryConditionOption.setter
    def BoundaryConditionOption(self, boundaryConditionOption: EquationOperationBuilder.BoundaryConditionOptionType):
        """
        Setter for property: (@link EquationOperationBuilder.BoundaryConditionOptionType NXOpen.Implicit.EquationOperationBuilder.BoundaryConditionOptionType@endlink) BoundaryConditionOption
          the Boundary Condition Option
                Solid volume fill, void volume fill or void volume fill with unite to outer body
                  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) EdgeLength
    ##   the edge length.  
    ##   
    ##         Edge length in X, Y and Z direction if it is a uniform cube.
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def EdgeLength(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) EdgeLength
          the edge length.  
          
                Edge length in X, Y and Z direction if it is a uniform cube.
                  
         
        """
        pass
    
    ## Getter for property: (float) KFactor
    ##   the k factor.  
    ##   
    ##         The porosity of the structure can be controlled by a dimensionless "k Factor".
    ##         The lower the k Factor "thicker" the structure gets. Increasing the k Factor 
    ##         the structure gets thinner and thinner until it splits into multiple regions 
    ##         and finally disappears.
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def KFactor(self) -> float:
        """
        Getter for property: (float) KFactor
          the k factor.  
          
                The porosity of the structure can be controlled by a dimensionless "k Factor".
                The lower the k Factor "thicker" the structure gets. Increasing the k Factor 
                the structure gets thinner and thinner until it splits into multiple regions 
                and finally disappears.
                  
         
        """
        pass
    
    ## Setter for property: (float) KFactor

    ##   the k factor.  
    ##   
    ##         The porosity of the structure can be controlled by a dimensionless "k Factor".
    ##         The lower the k Factor "thicker" the structure gets. Increasing the k Factor 
    ##         the structure gets thinner and thinner until it splits into multiple regions 
    ##         and finally disappears.
    ##           
    ##  
    ## Setter License requirements: nx_implicit (" NX Implicit Modeling")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @KFactor.setter
    def KFactor(self, kFactor: float):
        """
        Setter for property: (float) KFactor
          the k factor.  
          
                The porosity of the structure can be controlled by a dimensionless "k Factor".
                The lower the k Factor "thicker" the structure gets. Increasing the k Factor 
                the structure gets thinner and thinner until it splits into multiple regions 
                and finally disappears.
                  
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) LocationAndOrientation
    ##   the location and orientation of the seed cell.  
    ##   
    ##         The orientation can be inferred from objects inside or outside the TE.
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.CoordinateSystem
    @property
    def LocationAndOrientation(self) -> NXOpen.CoordinateSystem:
        """
        Getter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) LocationAndOrientation
          the location and orientation of the seed cell.  
          
                The orientation can be inferred from objects inside or outside the TE.
                  
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) LocationAndOrientation

    ##   the location and orientation of the seed cell.  
    ##   
    ##         The orientation can be inferred from objects inside or outside the TE.
    ##           
    ##  
    ## Setter License requirements: nx_implicit (" NX Implicit Modeling")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @LocationAndOrientation.setter
    def LocationAndOrientation(self, locationAndOrientation: NXOpen.CoordinateSystem):
        """
        Setter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) LocationAndOrientation
          the location and orientation of the seed cell.  
          
                The orientation can be inferred from objects inside or outside the TE.
                  
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) SizeX
    ##   the size x.  
    ##   
    ##         Edge length in X if it is a non-uniform cube.
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def SizeX(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) SizeX
          the size x.  
          
                Edge length in X if it is a non-uniform cube.
                  
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) SizeY
    ##   the size y.  
    ##   
    ##         Edge length in Y if it is a non-uniform cube.
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def SizeY(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) SizeY
          the size y.  
          
                Edge length in Y if it is a non-uniform cube.
                  
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) SizeZ
    ##   the size z.  
    ##   
    ##         Edge length in Z if it is a non-uniform cube.
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def SizeZ(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) SizeZ
          the size z.  
          
                Edge length in Z if it is a non-uniform cube.
                  
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Thickness
    ##   the thickness.  
    ##   
    ##         The equation creates just a surface. To create a solid body the user needs to specify a thickness.
    ##         The surface will be thickened with 50% of that value in both directions.
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Thickness(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Thickness
          the thickness.  
          
                The equation creates just a surface. To create a solid body the user needs to specify a thickness.
                The surface will be thickened with 50% of that value in both directions.
                  
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ThicknessFactor
    ##   the thickness factor.  
    ##   
    ##         The factor for the relative thickness method.
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def ThicknessFactor(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ThicknessFactor
          the thickness factor.  
          
                The factor for the relative thickness method.
                  
         
        """
        pass
    
    ## Getter for property: (@link EquationOperationBuilder.ThicknessMethodType NXOpen.Implicit.EquationOperationBuilder.ThicknessMethodType@endlink) ThicknessMethod
    ##   the thickness method
    ##         Methods of adding thickness to the TPMS structure : Absolute, Absolute variable, Relative
    ##           
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return EquationOperationBuilder.ThicknessMethodType
    @property
    def ThicknessMethod(self) -> EquationOperationBuilder.ThicknessMethodType:
        """
        Getter for property: (@link EquationOperationBuilder.ThicknessMethodType NXOpen.Implicit.EquationOperationBuilder.ThicknessMethodType@endlink) ThicknessMethod
          the thickness method
                Methods of adding thickness to the TPMS structure : Absolute, Absolute variable, Relative
                  
            
         
        """
        pass
    
    ## Setter for property: (@link EquationOperationBuilder.ThicknessMethodType NXOpen.Implicit.EquationOperationBuilder.ThicknessMethodType@endlink) ThicknessMethod

    ##   the thickness method
    ##         Methods of adding thickness to the TPMS structure : Absolute, Absolute variable, Relative
    ##           
    ##     
    ##  
    ## Setter License requirements: nx_implicit (" NX Implicit Modeling")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @ThicknessMethod.setter
    def ThicknessMethod(self, thicknessMethod: EquationOperationBuilder.ThicknessMethodType):
        """
        Setter for property: (@link EquationOperationBuilder.ThicknessMethodType NXOpen.Implicit.EquationOperationBuilder.ThicknessMethodType@endlink) ThicknessMethod
          the thickness method
                Methods of adding thickness to the TPMS structure : Absolute, Absolute variable, Relative
                  
            
         
        """
        pass
    
    ## Getter for property: (@link EquationOperationBuilder.EquationType NXOpen.Implicit.EquationOperationBuilder.EquationType@endlink) TypeOfEquation
    ##   the type of equation   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return EquationOperationBuilder.EquationType
    @property
    def TypeOfEquation(self) -> EquationOperationBuilder.EquationType:
        """
        Getter for property: (@link EquationOperationBuilder.EquationType NXOpen.Implicit.EquationOperationBuilder.EquationType@endlink) TypeOfEquation
          the type of equation   
            
         
        """
        pass
    
    ## Setter for property: (@link EquationOperationBuilder.EquationType NXOpen.Implicit.EquationOperationBuilder.EquationType@endlink) TypeOfEquation

    ##   the type of equation   
    ##     
    ##  
    ## Setter License requirements: nx_implicit (" NX Implicit Modeling")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @TypeOfEquation.setter
    def TypeOfEquation(self, typeOfEquation: EquationOperationBuilder.EquationType):
        """
        Setter for property: (@link EquationOperationBuilder.EquationType NXOpen.Implicit.EquationOperationBuilder.EquationType@endlink) TypeOfEquation
          the type of equation   
            
         
        """
        pass
    
    ## Getter for property: (bool) UniformCubeFlag
    ##   the uniform cube toggle.  
    ##   
    ##         Since the equation is periodic in 2PI the shape can be defined in a cube of (2PI*2PI*2PI)
    ##         that will be patterned in X, Y, and Z. A uniform cube with one edge length in all three
    ##         directions can be defined or specify the length for each axis separately.
    ##         ture for uniform cube false otherwise.
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return bool
    @property
    def UniformCubeFlag(self) -> bool:
        """
        Getter for property: (bool) UniformCubeFlag
          the uniform cube toggle.  
          
                Since the equation is periodic in 2PI the shape can be defined in a cube of (2PI*2PI*2PI)
                that will be patterned in X, Y, and Z. A uniform cube with one edge length in all three
                directions can be defined or specify the length for each axis separately.
                ture for uniform cube false otherwise.
                  
         
        """
        pass
    
    ## Setter for property: (bool) UniformCubeFlag

    ##   the uniform cube toggle.  
    ##   
    ##         Since the equation is periodic in 2PI the shape can be defined in a cube of (2PI*2PI*2PI)
    ##         that will be patterned in X, Y, and Z. A uniform cube with one edge length in all three
    ##         directions can be defined or specify the length for each axis separately.
    ##         ture for uniform cube false otherwise.
    ##           
    ##  
    ## Setter License requirements: nx_implicit (" NX Implicit Modeling")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @UniformCubeFlag.setter
    def UniformCubeFlag(self, uniformCubeFlag: bool):
        """
        Setter for property: (bool) UniformCubeFlag
          the uniform cube toggle.  
          
                Since the equation is periodic in 2PI the shape can be defined in a cube of (2PI*2PI*2PI)
                that will be patterned in X, Y, and Z. A uniform cube with one edge length in all three
                directions can be defined or specify the length for each axis separately.
                ture for uniform cube false otherwise.
                  
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.ModlUtils.SelectObjectDimList NXOpen.ModlUtils.SelectObjectDimList@endlink) VariableThicknessList
    ##   the variable thickness list, in order to assign variable thickness to the TPMS.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return NXOpen.ModlUtils.SelectObjectDimList
    @property
    def VariableThicknessList(self) -> NXOpen.ModlUtils.SelectObjectDimList:
        """
        Getter for property: (@link NXOpen.ModlUtils.SelectObjectDimList NXOpen.ModlUtils.SelectObjectDimList@endlink) VariableThicknessList
          the variable thickness list, in order to assign variable thickness to the TPMS.  
             
         
        """
        pass
    
##  Represents a Equation based Implicit Operation.  <br> This is an abstract class, and cannot be instantiated.  <br> 
## 
##   <br>  Created in NX1953.0.0  <br> 

class EquationOperation(ImplicitOperation): 
    """ Represents a Equation based Implicit Operation. """
    pass


import NXOpen
import NXOpen.ModlUtils
## 
##     Represents a Implicit.GeneralEquationOperationBuilder.
##     It will create an Implicit surfaces derived from given equation in the 3D space.
##     The definition of an implicit surface is that a coordinate is located on the surface if the equation results in zero.
##      <br> To create a new instance of this class, use @link NXOpen::Implicit::ImplicitOperationCollection::CreateGeneralEquationOperationBuilder  NXOpen::Implicit::ImplicitOperationCollection::CreateGeneralEquationOperationBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## BoundaryOption </term> <description> 
##  
## CartesianRange </description> </item> 
## 
## <item><term> 
##  
## SizeX.Value </term> <description> 
##  
## 10 (millimeters part), 0.4 (inches part) </description> </item> 
## 
## <item><term> 
##  
## SizeY.Value </term> <description> 
##  
## 10 (millimeters part), 0.4 (inches part) </description> </item> 
## 
## <item><term> 
##  
## SizeZ.Value </term> <description> 
##  
## 10 (millimeters part), 0.4 (inches part) </description> </item> 
## 
## <item><term> 
##  
## Thickness.Value </term> <description> 
##  
## 0 (millimeters part), 0 (inches part) </description> </item> 
## 
## <item><term> 
##  
## ThicknessFactor.Value </term> <description> 
##  
## 0.5 </description> </item> 
## 
## <item><term> 
##  
## ThicknessMethod </term> <description> 
##  
## Absolute </description> </item> 
## 
## <item><term> 
##  
## UniformRange </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## UniformSize.Value </term> <description> 
##  
## 10 (millimeters part), 0.4 (inches part) </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX1953.0.0  <br> 

class GeneralEquationOperationBuilder(OperationBuilder): 
    """
    Represents a Implicit.GeneralEquationOperationBuilder.
    It will create an Implicit surfaces derived from given equation in the 3D space.
    The definition of an implicit surface is that a coordinate is located on the surface if the equation results in zero.
    """


    ##  Boundary option 
    ##  Cartesian Range 
    class BoundaryOptionsEnum(Enum):
        """
        Members Include: <CartesianRange> <BoundaryBody>
        """
        CartesianRange: int
        BoundaryBody: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> GeneralEquationOperationBuilder.BoundaryOptionsEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Thickness methods
    ##  Absolute thickness 
    class ThicknessMethodType(Enum):
        """
        Members Include: <Absolute> <Relative>
        """
        Absolute: int
        Relative: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> GeneralEquationOperationBuilder.ThicknessMethodType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) BoundaryBody
    ##   the Boundary Body   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.ScCollector
    @property
    def BoundaryBody(self) -> NXOpen.ScCollector:
        """
        Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) BoundaryBody
          the Boundary Body   
            
         
        """
        pass
    
    ## Getter for property: (@link GeneralEquationOperationBuilder.BoundaryOptionsEnum NXOpen.Implicit.GeneralEquationOperationBuilder.BoundaryOptionsEnum@endlink) BoundaryOption
    ##   the Boundary Options   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return GeneralEquationOperationBuilder.BoundaryOptionsEnum
    @property
    def BoundaryOption(self) -> GeneralEquationOperationBuilder.BoundaryOptionsEnum:
        """
        Getter for property: (@link GeneralEquationOperationBuilder.BoundaryOptionsEnum NXOpen.Implicit.GeneralEquationOperationBuilder.BoundaryOptionsEnum@endlink) BoundaryOption
          the Boundary Options   
            
         
        """
        pass
    
    ## Setter for property: (@link GeneralEquationOperationBuilder.BoundaryOptionsEnum NXOpen.Implicit.GeneralEquationOperationBuilder.BoundaryOptionsEnum@endlink) BoundaryOption

    ##   the Boundary Options   
    ##     
    ##  
    ## Setter License requirements: nx_implicit (" NX Implicit Modeling")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @BoundaryOption.setter
    def BoundaryOption(self, boundaryOptions: GeneralEquationOperationBuilder.BoundaryOptionsEnum):
        """
        Setter for property: (@link GeneralEquationOperationBuilder.BoundaryOptionsEnum NXOpen.Implicit.GeneralEquationOperationBuilder.BoundaryOptionsEnum@endlink) BoundaryOption
          the Boundary Options   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) LocationAndOrientation
    ##   the Location and Orientation
    ##         locate the origin and orient the CSYS for the equation.  
    ##   
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.CoordinateSystem
    @property
    def LocationAndOrientation(self) -> NXOpen.CoordinateSystem:
        """
        Getter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) LocationAndOrientation
          the Location and Orientation
                locate the origin and orient the CSYS for the equation.  
          
                  
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) LocationAndOrientation

    ##   the Location and Orientation
    ##         locate the origin and orient the CSYS for the equation.  
    ##   
    ##           
    ##  
    ## Setter License requirements: nx_implicit (" NX Implicit Modeling")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @LocationAndOrientation.setter
    def LocationAndOrientation(self, locationAndOrientation: NXOpen.CoordinateSystem):
        """
        Setter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) LocationAndOrientation
          the Location and Orientation
                locate the origin and orient the CSYS for the equation.  
          
                  
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) SizeX
    ##   the Size in X direction 
    ##         Range will be centered around the origin.  
    ##   
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def SizeX(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) SizeX
          the Size in X direction 
                Range will be centered around the origin.  
          
                  
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) SizeY
    ##   the Size in Y direction
    ##         Range will be centered around the origin.  
    ##   
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def SizeY(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) SizeY
          the Size in Y direction
                Range will be centered around the origin.  
          
                  
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) SizeZ
    ##   the Size in Z direction
    ##         Range will be centered around the origin.  
    ##   
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def SizeZ(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) SizeZ
          the Size in Z direction
                Range will be centered around the origin.  
          
                  
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Thickness
    ##   the thickness
    ##         Thickness to be used for equation surface.  
    ##   
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Thickness(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Thickness
          the thickness
                Thickness to be used for equation surface.  
          
                  
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ThicknessFactor
    ##   the thickness factor.  
    ##   
    ##         The factor for the relative thickness method.
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def ThicknessFactor(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ThicknessFactor
          the thickness factor.  
          
                The factor for the relative thickness method.
                  
         
        """
        pass
    
    ## Getter for property: (@link GeneralEquationOperationBuilder.ThicknessMethodType NXOpen.Implicit.GeneralEquationOperationBuilder.ThicknessMethodType@endlink) ThicknessMethod
    ##   the thickness method
    ##         Methods of adding thickness to structure created by general equation : Absolute, Relative
    ##           
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return GeneralEquationOperationBuilder.ThicknessMethodType
    @property
    def ThicknessMethod(self) -> GeneralEquationOperationBuilder.ThicknessMethodType:
        """
        Getter for property: (@link GeneralEquationOperationBuilder.ThicknessMethodType NXOpen.Implicit.GeneralEquationOperationBuilder.ThicknessMethodType@endlink) ThicknessMethod
          the thickness method
                Methods of adding thickness to structure created by general equation : Absolute, Relative
                  
            
         
        """
        pass
    
    ## Setter for property: (@link GeneralEquationOperationBuilder.ThicknessMethodType NXOpen.Implicit.GeneralEquationOperationBuilder.ThicknessMethodType@endlink) ThicknessMethod

    ##   the thickness method
    ##         Methods of adding thickness to structure created by general equation : Absolute, Relative
    ##           
    ##     
    ##  
    ## Setter License requirements: nx_implicit (" NX Implicit Modeling")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @ThicknessMethod.setter
    def ThicknessMethod(self, thicknessMethod: GeneralEquationOperationBuilder.ThicknessMethodType):
        """
        Setter for property: (@link GeneralEquationOperationBuilder.ThicknessMethodType NXOpen.Implicit.GeneralEquationOperationBuilder.ThicknessMethodType@endlink) ThicknessMethod
          the thickness method
                Methods of adding thickness to structure created by general equation : Absolute, Relative
                  
            
         
        """
        pass
    
    ## Getter for property: (bool) UniformRange
    ##   the Uniform Flag
    ##         Uniform boundary range inside which the implicit surface for given equation will be created.  
    ##   
    ##         Range will be centered around the origin.
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return bool
    @property
    def UniformRange(self) -> bool:
        """
        Getter for property: (bool) UniformRange
          the Uniform Flag
                Uniform boundary range inside which the implicit surface for given equation will be created.  
          
                Range will be centered around the origin.
                  
         
        """
        pass
    
    ## Setter for property: (bool) UniformRange

    ##   the Uniform Flag
    ##         Uniform boundary range inside which the implicit surface for given equation will be created.  
    ##   
    ##         Range will be centered around the origin.
    ##           
    ##  
    ## Setter License requirements: nx_implicit (" NX Implicit Modeling")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @UniformRange.setter
    def UniformRange(self, uniform: bool):
        """
        Setter for property: (bool) UniformRange
          the Uniform Flag
                Uniform boundary range inside which the implicit surface for given equation will be created.  
          
                Range will be centered around the origin.
                  
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) UniformSize
    ##   the Uniform Size
    ##         Uniform range in X, Y and Z directions.  
    ##   
    ##         Range will be centered around the origin.
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def UniformSize(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) UniformSize
          the Uniform Size
                Uniform range in X, Y and Z directions.  
          
                Range will be centered around the origin.
                  
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.ModlUtils.EquationEditorBuilder NXOpen.ModlUtils.EquationEditorBuilder@endlink) UserExpression
    ##   the user expression from whch implicit surface will be created  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.ModlUtils.EquationEditorBuilder
    @property
    def UserExpression(self) -> NXOpen.ModlUtils.EquationEditorBuilder:
        """
        Getter for property: (@link NXOpen.ModlUtils.EquationEditorBuilder NXOpen.ModlUtils.EquationEditorBuilder@endlink) UserExpression
          the user expression from whch implicit surface will be created  
            
         
        """
        pass
    
##  Represents a Implicit General Equation Operation.  <br> To create or edit an instance of this class, use @link NXOpen::Implicit::GeneralEquationOperationBuilder  NXOpen::Implicit::GeneralEquationOperationBuilder @endlink  <br> 
## 
##   <br>  Created in NX1953.0.0  <br> 

class GeneralEquationOperation(ImplicitOperation): 
    """ Represents a Implicit General Equation Operation. """
    pass


##  Represents a Gyroid Implicit Operation.  <br> To create or edit an instance of this class, use @link NXOpen::Implicit::EquationOperationBuilder  NXOpen::Implicit::EquationOperationBuilder @endlink  <br> 
## 
##   <br>  Created in NX1953.0.0  <br> 

class Gyroid(EquationOperation): 
    """ Represents a Gyroid Implicit Operation. """
    pass


import NXOpen
##  Represents an implicit feature. Output of this feature is convergent body.  <br> To create a new instance of this class, use @link NXOpen::Implicit::ImplicitOperationCollection::CreateImplicitModelingPreferencesBuilder  NXOpen::Implicit::ImplicitOperationCollection::CreateImplicitModelingPreferencesBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## ChordalTolerance </term> <description> 
##  
## 0.1 (millimeters part), 0.005 (inches part) </description> </item> 
## 
## <item><term> 
##  
## MaxFacetSize.Value </term> <description> 
##  
## 10 (millimeters part), 0.5 (inches part) </description> </item> 
## 
## <item><term> 
##  
## RemeshFlag </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## VoxelSize.Value </term> <description> 
##  
## 1 (millimeters part), 0.05 (inches part) </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX1926.0.0  <br> 

class ImplicitModelingPreferencesBuilder(NXOpen.Builder): 
    """ Represents an implicit feature. Output of this feature is convergent body. """


    ## Getter for property: (float) ChordalTolerance
    ##   the maximum chordal deviation between the original mesh and the output mesh.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def ChordalTolerance(self) -> float:
        """
        Getter for property: (float) ChordalTolerance
          the maximum chordal deviation between the original mesh and the output mesh.  
             
         
        """
        pass
    
    ## Setter for property: (float) ChordalTolerance

    ##   the maximum chordal deviation between the original mesh and the output mesh.  
    ##      
    ##  
    ## Setter License requirements: nx_implicit (" NX Implicit Modeling")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @ChordalTolerance.setter
    def ChordalTolerance(self, chordalTolerance: float):
        """
        Setter for property: (float) ChordalTolerance
          the maximum chordal deviation between the original mesh and the output mesh.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxFacetSize
    ##   the maximum facet size in areas of low face curvature.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def MaxFacetSize(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxFacetSize
          the maximum facet size in areas of low face curvature.  
             
         
        """
        pass
    
    ## Getter for property: (bool) RemeshFlag
    ##   the flag to remesh the implict body.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return bool
    @property
    def RemeshFlag(self) -> bool:
        """
        Getter for property: (bool) RemeshFlag
          the flag to remesh the implict body.  
             
         
        """
        pass
    
    ## Setter for property: (bool) RemeshFlag

    ##   the flag to remesh the implict body.  
    ##      
    ##  
    ## Setter License requirements: nx_implicit (" NX Implicit Modeling")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @RemeshFlag.setter
    def RemeshFlag(self, remeshFlag: bool):
        """
        Setter for property: (bool) RemeshFlag
          the flag to remesh the implict body.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) VoxelSize
    ##   the voxel size for implicit feature.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def VoxelSize(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) VoxelSize
          the voxel size for implicit feature.  
             
         
        """
        pass
    
import NXOpen
## 
##          Represents the collection of @link NXOpen::Implicit::ImplicitOperation NXOpen::Implicit::ImplicitOperation@endlink  object.
##      <br> To obtain an instance of this class, refer to @link NXOpen::BasePart  NXOpen::BasePart @endlink  <br> 
## 
##   <br>  Created in NX1926.0.0  <br> 

class ImplicitOperationCollection(NXOpen.TaggedObjectCollection): 
    """
         Represents the collection of <ja_class>NXOpen.Implicit.ImplicitOperation</ja_class> object.
    """


    ##  Creates an object of @link NXOpen::Implicit::BlockBuilder NXOpen::Implicit::BlockBuilder@endlink  
    ##  @return blockBuilder (@link BlockBuilder NXOpen.Implicit.BlockBuilder@endlink):  the implicit block builder .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_implicit (" NX Implicit Modeling")
    ##  the @link NXOpen::Implicit::Block NXOpen::Implicit::Block@endlink  implicit operation 
    def CreateBlockBuilder(owningPart: ImplicitOperationCollection, implicitOperation: Block) -> BlockBuilder:
        """
         Creates an object of @link NXOpen::Implicit::BlockBuilder NXOpen::Implicit::BlockBuilder@endlink  
         @return blockBuilder (@link BlockBuilder NXOpen.Implicit.BlockBuilder@endlink):  the implicit block builder .
        """
        pass
    
    ##  Creates an object of @link NXOpen::Implicit::CartesianPatternBuilder NXOpen::Implicit::CartesianPatternBuilder@endlink  
    ##  @return cartesianPatternBuilder (@link CartesianPatternBuilder NXOpen.Implicit.CartesianPatternBuilder@endlink):  the cartesian pattern based implicit operation builder .
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: nx_implicit (" NX Implicit Modeling")
    ##  the @link NXOpen::Implicit::CartesianPattern NXOpen::Implicit::CartesianPattern@endlink  cartesian pattern based implicit operation 
    def CreateCartesianPatternBuilder(owningPart: ImplicitOperationCollection, implicitOperation: CartesianPattern) -> CartesianPatternBuilder:
        """
         Creates an object of @link NXOpen::Implicit::CartesianPatternBuilder NXOpen::Implicit::CartesianPatternBuilder@endlink  
         @return cartesianPatternBuilder (@link CartesianPatternBuilder NXOpen.Implicit.CartesianPatternBuilder@endlink):  the cartesian pattern based implicit operation builder .
        """
        pass
    
    ##  Creates an object of @link NXOpen::Implicit::ConeBuilder NXOpen::Implicit::ConeBuilder@endlink  
    ##  @return coneBuilder (@link ConeBuilder NXOpen.Implicit.ConeBuilder@endlink):  the implicit cone builder .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_implicit (" NX Implicit Modeling")
    ##  the @link NXOpen::Implicit::Cone NXOpen::Implicit::Cone@endlink  implicit operation 
    def CreateConeBuilder(owningPart: ImplicitOperationCollection, implicitOperation: Cone) -> ConeBuilder:
        """
         Creates an object of @link NXOpen::Implicit::ConeBuilder NXOpen::Implicit::ConeBuilder@endlink  
         @return coneBuilder (@link ConeBuilder NXOpen.Implicit.ConeBuilder@endlink):  the implicit cone builder .
        """
        pass
    
    ##  Creates an object of @link NXOpen::Implicit::CylinderBuilder NXOpen::Implicit::CylinderBuilder@endlink  
    ##  @return cylinderBuilder (@link CylinderBuilder NXOpen.Implicit.CylinderBuilder@endlink):  the implicit cylinder builder .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_implicit (" NX Implicit Modeling")
    ##  the @link NXOpen::Implicit::Cylinder NXOpen::Implicit::Cylinder@endlink  implicit operation 
    def CreateCylinderBuilder(owningPart: ImplicitOperationCollection, implicitOperation: Cylinder) -> CylinderBuilder:
        """
         Creates an object of @link NXOpen::Implicit::CylinderBuilder NXOpen::Implicit::CylinderBuilder@endlink  
         @return cylinderBuilder (@link CylinderBuilder NXOpen.Implicit.CylinderBuilder@endlink):  the implicit cylinder builder .
        """
        pass
    
    ##  Creates an object of @link NXOpen::Implicit::CylindricalPatternBuilder NXOpen::Implicit::CylindricalPatternBuilder@endlink  
    ##  @return cylindricalPatternBuilder (@link CylindricalPatternBuilder NXOpen.Implicit.CylindricalPatternBuilder@endlink):  the cylindrical pattern based implicit operation builder .
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: nx_implicit (" NX Implicit Modeling")
    ##  the @link NXOpen::Implicit::CylindricalPattern NXOpen::Implicit::CylindricalPattern@endlink  cylindrical pattern based implicit operation 
    def CreateCylindricalPatternBuilder(owningPart: ImplicitOperationCollection, implicitOperation: CylindricalPattern) -> CylindricalPatternBuilder:
        """
         Creates an object of @link NXOpen::Implicit::CylindricalPatternBuilder NXOpen::Implicit::CylindricalPatternBuilder@endlink  
         @return cylindricalPatternBuilder (@link CylindricalPatternBuilder NXOpen.Implicit.CylindricalPatternBuilder@endlink):  the cylindrical pattern based implicit operation builder .
        """
        pass
    
    ##  Creates an object of @link NXOpen::Implicit::EllipsoidBuilder NXOpen::Implicit::EllipsoidBuilder@endlink  
    ##  @return ellipsoidBuilder (@link EllipsoidBuilder NXOpen.Implicit.EllipsoidBuilder@endlink):  the implicit ellipsoid builder .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_implicit (" NX Implicit Modeling")
    ##  the @link NXOpen::Implicit::Ellipsoid NXOpen::Implicit::Ellipsoid@endlink  implicit operation 
    def CreateEllipsoidBuilder(owningPart: ImplicitOperationCollection, implicitOperation: Ellipsoid) -> EllipsoidBuilder:
        """
         Creates an object of @link NXOpen::Implicit::EllipsoidBuilder NXOpen::Implicit::EllipsoidBuilder@endlink  
         @return ellipsoidBuilder (@link EllipsoidBuilder NXOpen.Implicit.EllipsoidBuilder@endlink):  the implicit ellipsoid builder .
        """
        pass
    
    ##  Creates an object of @link NXOpen::Implicit::EquationOperationBuilder NXOpen::Implicit::EquationOperationBuilder@endlink  
    ##  @return equationOperationBuilder (@link EquationOperationBuilder NXOpen.Implicit.EquationOperationBuilder@endlink):  the equation based implicit operation builder .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_implicit (" NX Implicit Modeling")
    ##  the @link NXOpen::Implicit::EquationOperation NXOpen::Implicit::EquationOperation@endlink  equation based implicit operation 
    def CreateEquationOperationBuilder(owningPart: ImplicitOperationCollection, implicitOperation: EquationOperation) -> EquationOperationBuilder:
        """
         Creates an object of @link NXOpen::Implicit::EquationOperationBuilder NXOpen::Implicit::EquationOperationBuilder@endlink  
         @return equationOperationBuilder (@link EquationOperationBuilder NXOpen.Implicit.EquationOperationBuilder@endlink):  the equation based implicit operation builder .
        """
        pass
    
    ##  Creates an object of @link NXOpen::Implicit::GeneralEquationOperationBuilder NXOpen::Implicit::GeneralEquationOperationBuilder@endlink  
    ##  @return generalEquationOperationBuilder (@link GeneralEquationOperationBuilder NXOpen.Implicit.GeneralEquationOperationBuilder@endlink):  the general equation based implicit operation builder .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_implicit (" NX Implicit Modeling")
    ##  the general equation based implicit operation 
    def CreateGeneralEquationOperationBuilder(owningPart: ImplicitOperationCollection, implicitOperation: GeneralEquationOperation) -> GeneralEquationOperationBuilder:
        """
         Creates an object of @link NXOpen::Implicit::GeneralEquationOperationBuilder NXOpen::Implicit::GeneralEquationOperationBuilder@endlink  
         @return generalEquationOperationBuilder (@link GeneralEquationOperationBuilder NXOpen.Implicit.GeneralEquationOperationBuilder@endlink):  the general equation based implicit operation builder .
        """
        pass
    
    ##  Creates an object of @link NXOpen::Implicit::ImplicitModelingPreferencesBuilder NXOpen::Implicit::ImplicitModelingPreferencesBuilder@endlink  
    ##  @return implicitModelPreferencesBuilder (@link ImplicitModelingPreferencesBuilder NXOpen.Implicit.ImplicitModelingPreferencesBuilder@endlink):  the implicit model preference builder .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_implicit (" NX Implicit Modeling")
    ##  the implicit model feature.
    def CreateImplicitModelingPreferencesBuilder(owningPart: ImplicitOperationCollection, implicitFeature: Feature) -> ImplicitModelingPreferencesBuilder:
        """
         Creates an object of @link NXOpen::Implicit::ImplicitModelingPreferencesBuilder NXOpen::Implicit::ImplicitModelingPreferencesBuilder@endlink  
         @return implicitModelPreferencesBuilder (@link ImplicitModelingPreferencesBuilder NXOpen.Implicit.ImplicitModelingPreferencesBuilder@endlink):  the implicit model preference builder .
        """
        pass
    
    ##  Creates an object of @link NXOpen::Implicit::ImportSolidBodyBuilder NXOpen::Implicit::ImportSolidBodyBuilder@endlink  
    ##  @return importSolidBodyBuilder (@link ImportSolidBodyBuilder NXOpen.Implicit.ImportSolidBodyBuilder@endlink):  the import solid body implicit operation builder .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_implicit (" NX Implicit Modeling")
    ##  the @link NXOpen::Implicit::ImportSolidBody NXOpen::Implicit::ImportSolidBody@endlink  implicit operation 
    def CreateImportSoildBodyBuilder(owningPart: ImplicitOperationCollection, implicitOperation: ImportSolidBody) -> ImportSolidBodyBuilder:
        """
         Creates an object of @link NXOpen::Implicit::ImportSolidBodyBuilder NXOpen::Implicit::ImportSolidBodyBuilder@endlink  
         @return importSolidBodyBuilder (@link ImportSolidBodyBuilder NXOpen.Implicit.ImportSolidBodyBuilder@endlink):  the import solid body implicit operation builder .
        """
        pass
    
    ##  Creates an object of @link NXOpen::Implicit::IntersectBuilder NXOpen::Implicit::IntersectBuilder@endlink  
    ##  @return intersectBuilder (@link IntersectBuilder NXOpen.Implicit.IntersectBuilder@endlink):  the implicit intersect builder .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_implicit (" NX Implicit Modeling")
    ##  the @link NXOpen::Implicit::Intersect NXOpen::Implicit::Intersect@endlink  implicit operation 
    def CreateIntersectBuilder(owningPart: ImplicitOperationCollection, implicitOperation: Intersect) -> IntersectBuilder:
        """
         Creates an object of @link NXOpen::Implicit::IntersectBuilder NXOpen::Implicit::IntersectBuilder@endlink  
         @return intersectBuilder (@link IntersectBuilder NXOpen.Implicit.IntersectBuilder@endlink):  the implicit intersect builder .
        """
        pass
    
    ##  Creates an object of @link NXOpen::Implicit::ShellBuilder NXOpen::Implicit::ShellBuilder@endlink  
    ##  @return offsetBuilder (@link ShellBuilder NXOpen.Implicit.ShellBuilder@endlink):  the implicit shell builder .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_implicit (" NX Implicit Modeling")
    ##  the @link NXOpen::Implicit::Shell NXOpen::Implicit::Shell@endlink  implicit operation 
    def CreateShellBuilder(owningPart: ImplicitOperationCollection, implicitOperation: Shell) -> ShellBuilder:
        """
         Creates an object of @link NXOpen::Implicit::ShellBuilder NXOpen::Implicit::ShellBuilder@endlink  
         @return offsetBuilder (@link ShellBuilder NXOpen.Implicit.ShellBuilder@endlink):  the implicit shell builder .
        """
        pass
    
    ##  Creates an object of @link NXOpen::Implicit::SphereBuilder NXOpen::Implicit::SphereBuilder@endlink  
    ##  @return sphereBuilder (@link SphereBuilder NXOpen.Implicit.SphereBuilder@endlink):  the implicit sphere builder .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_implicit (" NX Implicit Modeling")
    ##  the @link NXOpen::Implicit::Sphere NXOpen::Implicit::Sphere@endlink  implicit operation 
    def CreateSphereBuilder(owningPart: ImplicitOperationCollection, implicitOperation: Sphere) -> SphereBuilder:
        """
         Creates an object of @link NXOpen::Implicit::SphereBuilder NXOpen::Implicit::SphereBuilder@endlink  
         @return sphereBuilder (@link SphereBuilder NXOpen.Implicit.SphereBuilder@endlink):  the implicit sphere builder .
        """
        pass
    
    ##  Creates an object of @link NXOpen::Implicit::SubtractBuilder NXOpen::Implicit::SubtractBuilder@endlink  
    ##  @return subtractBuilder (@link SubtractBuilder NXOpen.Implicit.SubtractBuilder@endlink):  the implicit subtract builder .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_implicit (" NX Implicit Modeling")
    ##  the @link NXOpen::Implicit::Subtract NXOpen::Implicit::Subtract@endlink  implicit operation 
    def CreateSubtractBuilder(owningPart: ImplicitOperationCollection, implicitOperation: Subtract) -> SubtractBuilder:
        """
         Creates an object of @link NXOpen::Implicit::SubtractBuilder NXOpen::Implicit::SubtractBuilder@endlink  
         @return subtractBuilder (@link SubtractBuilder NXOpen.Implicit.SubtractBuilder@endlink):  the implicit subtract builder .
        """
        pass
    
    ##  Creates an object of @link NXOpen::Implicit::ThickenBuilder NXOpen::Implicit::ThickenBuilder@endlink  
    ##  @return thickenBuilder (@link ThickenBuilder NXOpen.Implicit.ThickenBuilder@endlink):  the implicit thicken builder .
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: nx_implicit (" NX Implicit Modeling")
    ##  the @link NXOpen::Implicit::Thicken NXOpen::Implicit::Thicken@endlink  implicit operation 
    def CreateThickenBuilder(owningPart: ImplicitOperationCollection, implicitOperation: Thicken) -> ThickenBuilder:
        """
         Creates an object of @link NXOpen::Implicit::ThickenBuilder NXOpen::Implicit::ThickenBuilder@endlink  
         @return thickenBuilder (@link ThickenBuilder NXOpen.Implicit.ThickenBuilder@endlink):  the implicit thicken builder .
        """
        pass
    
    ##  Creates an object of @link NXOpen::Implicit::TorusBuilder NXOpen::Implicit::TorusBuilder@endlink  
    ##  @return torusBuilder (@link TorusBuilder NXOpen.Implicit.TorusBuilder@endlink):  the implicit torus builder .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_implicit (" NX Implicit Modeling")
    ##  the @link NXOpen::Implicit::Torus NXOpen::Implicit::Torus@endlink  implicit operation 
    def CreateTorusBuilder(owningPart: ImplicitOperationCollection, implicitOperation: Torus) -> TorusBuilder:
        """
         Creates an object of @link NXOpen::Implicit::TorusBuilder NXOpen::Implicit::TorusBuilder@endlink  
         @return torusBuilder (@link TorusBuilder NXOpen.Implicit.TorusBuilder@endlink):  the implicit torus builder .
        """
        pass
    
    ##  Creates an object of @link NXOpen::Implicit::UniteBuilder NXOpen::Implicit::UniteBuilder@endlink  
    ##  @return uniteBuilder (@link UniteBuilder NXOpen.Implicit.UniteBuilder@endlink):  the implicit unite builder .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_implicit (" NX Implicit Modeling")
    ##  the @link NXOpen::Implicit::Unite NXOpen::Implicit::Unite@endlink  implicit operation 
    def CreateUniteBuilder(owningPart: ImplicitOperationCollection, implicitOperation: Unite) -> UniteBuilder:
        """
         Creates an object of @link NXOpen::Implicit::UniteBuilder NXOpen::Implicit::UniteBuilder@endlink  
         @return uniteBuilder (@link UniteBuilder NXOpen.Implicit.UniteBuilder@endlink):  the implicit unite builder .
        """
        pass
    
import NXOpen
## 
##         Represents the base class for an NX Implicit Operation.
##      <br> This is an abstract class, and cannot be instantiated.  <br> 
## 
##   <br>  Created in NX1926.0.0  <br> 

class ImplicitOperation(NXOpen.NXObject): 
    """
        Represents the base class for an NX Implicit Operation.
    """


    ## Getter for property: (int) Timestamp
    ##   the timestamp of the feature   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return int
    @property
    def Timestamp(self) -> int:
        """
        Getter for property: (int) Timestamp
          the timestamp of the feature   
            
         
        """
        pass
    
    ##  Returns the expressions created by the implicit operation. The order in which expressions are returned is not significant and may change 
    ##  @return expressions (@link NXOpen.Expression List[NXOpen.Expression]@endlink):  the expressions created by implicit operation.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetExpressions(implicit_operation: ImplicitOperation) -> List[NXOpen.Expression]:
        """
         Returns the expressions created by the implicit operation. The order in which expressions are returned is not significant and may change 
         @return expressions (@link NXOpen.Expression List[NXOpen.Expression]@endlink):  the expressions created by implicit operation.
        """
        pass
    
    ##  Returns the immediate parent of implicit operations. The order in which parents are returned is not significant and may change 
    ##  @return parent_implicit_operations (@link ImplicitOperation List[NXOpen.Implicit.ImplicitOperation]@endlink):  the parents of implicit operation.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetParents(implicit_operation: ImplicitOperation) -> List[ImplicitOperation]:
        """
         Returns the immediate parent of implicit operations. The order in which parents are returned is not significant and may change 
         @return parent_implicit_operations (@link ImplicitOperation List[NXOpen.Implicit.ImplicitOperation]@endlink):  the parents of implicit operation.
        """
        pass
    
import NXOpen
##  Represents an import solid body @link Implicit::ImportSolidBody Implicit::ImportSolidBody@endlink  builder  <br> To create a new instance of this class, use @link NXOpen::Implicit::ImplicitOperationCollection::CreateImportSoildBodyBuilder  NXOpen::Implicit::ImplicitOperationCollection::CreateImportSoildBodyBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## HideInputBody </term> <description> 
##  
## true </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX1953.0.0  <br> 

class ImportSolidBodyBuilder(OperationBuilder): 
    """ Represents an import solid body <ja_class>Implicit.ImportSolidBody</ja_class> builder """


    ## Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) BodiesOrFacesToImport
    ##   the solid bodies or faces to import from outside the task environment  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.ScCollector
    @property
    def BodiesOrFacesToImport(self) -> NXOpen.ScCollector:
        """
        Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) BodiesOrFacesToImport
          the solid bodies or faces to import from outside the task environment  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) BodiesToImport
    ##   the solid bodies to import from outside the task environment  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX1980.0.0.  Use @link NXOpen::Implicit::ImportSolidBodyBuilder::BodiesOrFacesToImport NXOpen::Implicit::ImportSolidBodyBuilder::BodiesOrFacesToImport@endlink  instead.  <br> 

    ## @return NXOpen.ScCollector
    @property
    def BodiesToImport(self) -> NXOpen.ScCollector:
        """
        Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) BodiesToImport
          the solid bodies to import from outside the task environment  
            
         
        """
        pass
    
    ## Getter for property: (bool) HideInputBody
    ##   the hide input body option   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return bool
    @property
    def HideInputBody(self) -> bool:
        """
        Getter for property: (bool) HideInputBody
          the hide input body option   
            
         
        """
        pass
    
    ## Setter for property: (bool) HideInputBody

    ##   the hide input body option   
    ##     
    ##  
    ## Setter License requirements: nx_implicit (" NX Implicit Modeling")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @HideInputBody.setter
    def HideInputBody(self, hideInputBody: bool):
        """
        Setter for property: (bool) HideInputBody
          the hide input body option   
            
         
        """
        pass
    
##  Represents a Import Body Implicit Operation.  <br> To create or edit an instance of this class, use @link NXOpen::Implicit::ImportSolidBodyBuilder  NXOpen::Implicit::ImportSolidBodyBuilder @endlink  <br> 
## 
##   <br>  Created in NX1953.0.0  <br> 

class ImportSolidBody(ImplicitOperation): 
    """ Represents a Import Body Implicit Operation. """
    pass


## 
##     Represents an Implicit.IntersectBuilder.
##     It will create an intersect operation on the selected bodies.
##      <br> To create a new instance of this class, use @link NXOpen::Implicit::ImplicitOperationCollection::CreateIntersectBuilder  NXOpen::Implicit::ImplicitOperationCollection::CreateIntersectBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## BlendFactor </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## CreateBlends (deprecated) </term> <description> 
##  
## 0 </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX1953.0.0  <br> 

class IntersectBuilder(BooleanBuilder): 
    """
    Represents an Implicit.IntersectBuilder.
    It will create an intersect operation on the selected bodies.
    """
    pass


##  Represents an Intersect Implicit Operation.  <br> To create or edit an instance of this class, use @link NXOpen::Implicit::BooleanBuilder  NXOpen::Implicit::BooleanBuilder @endlink  <br> 
## 
##   <br>  Created in NX1953.0.0  <br> 

class Intersect(Boolean): 
    """ Represents an Intersect Implicit Operation. """
    pass


##  Represents a Lidinoid Implicit Operation.  <br> To create or edit an instance of this class, use @link NXOpen::Implicit::EquationOperationBuilder  NXOpen::Implicit::EquationOperationBuilder @endlink  <br> 
## 
##   <br>  Created in NX2007.0.0  <br> 

class Lidinoid(EquationOperation): 
    """ Represents a Lidinoid Implicit Operation. """
    pass


##  Represents a Neovius Implicit Operation.  <br> To create or edit an instance of this class, use @link NXOpen::Implicit::EquationOperationBuilder  NXOpen::Implicit::EquationOperationBuilder @endlink  <br> 
## 
##   <br>  Created in NX1953.0.0  <br> 

class Neovius(EquationOperation): 
    """ Represents a Neovius Implicit Operation. """
    pass


import NXOpen
## 
##     Represents a Implicit.OffsetBuilder.
##     It will Offset the selected body inside Implicit Task Environment.
##      <br> This is abstract class.  <br> 
## 
##   <br>  Created in NX1953.0.0  <br> 

class OffsetBuilder(OperationBuilder): 
    """
    Represents a Implicit.OffsetBuilder.
    It will Offset the selected body inside Implicit Task Environment.
    """


    ## Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) BodyToOffset
    ##   the body to offset   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.ScCollector
    @property
    def BodyToOffset(self) -> NXOpen.ScCollector:
        """
        Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) BodyToOffset
          the body to offset   
            
         
        """
        pass
    
    ## Getter for property: (bool) DefaultThicknessDirectionReversed
    ##   the default thickness directions is reversed   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return bool
    @property
    def DefaultThicknessDirectionReversed(self) -> bool:
        """
        Getter for property: (bool) DefaultThicknessDirectionReversed
          the default thickness directions is reversed   
            
         
        """
        pass
    
    ## Setter for property: (bool) DefaultThicknessDirectionReversed

    ##   the default thickness directions is reversed   
    ##     
    ##  
    ## Setter License requirements: nx_implicit (" NX Implicit Modeling")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @DefaultThicknessDirectionReversed.setter
    def DefaultThicknessDirectionReversed(self, reverseDirection: bool):
        """
        Setter for property: (bool) DefaultThicknessDirectionReversed
          the default thickness directions is reversed   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Thickness
    ##   the thickness - offset distance  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Thickness(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Thickness
          the thickness - offset distance  
            
         
        """
        pass
    
##  Represents a Offset Implicit Operation.  <br> To create or edit an instance of this class, use @link NXOpen::Implicit::OffsetBuilder  NXOpen::Implicit::OffsetBuilder @endlink  <br> 
## 
##   <br>  Created in NX1953.0.0  <br> 

class Offset(ImplicitOperation): 
    """ Represents a Offset Implicit Operation. """
    pass


import NXOpen
## 
##     Represents a Implicit.OperationBuilder. This is an abstract class.
##     This is the base class of all Implicit operations builder classes.
##      <br> This is abstract class.  <br> 
## 
##   <br>  Created in NX1926.0.0  <br> 

class OperationBuilder(NXOpen.Builder): 
    """
    Represents a Implicit.OperationBuilder. This is an abstract class.
    This is the base class of all Implicit operations builder classes.
    """


    ## Getter for property: (bool) DisplayVoxel
    ##   the voxel display toggle.  
    ##   
    ##         This toggle is used only for graphics display of voxel visualization scale
    ##         and has no impact on operation output.
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return bool
    @property
    def DisplayVoxel(self) -> bool:
        """
        Getter for property: (bool) DisplayVoxel
          the voxel display toggle.  
          
                This toggle is used only for graphics display of voxel visualization scale
                and has no impact on operation output.
                  
         
        """
        pass
    
    ## Setter for property: (bool) DisplayVoxel

    ##   the voxel display toggle.  
    ##   
    ##         This toggle is used only for graphics display of voxel visualization scale
    ##         and has no impact on operation output.
    ##           
    ##  
    ## Setter License requirements: nx_implicit (" NX Implicit Modeling")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @DisplayVoxel.setter
    def DisplayVoxel(self, displayVoxelFlag: bool):
        """
        Setter for property: (bool) DisplayVoxel
          the voxel display toggle.  
          
                This toggle is used only for graphics display of voxel visualization scale
                and has no impact on operation output.
                  
         
        """
        pass
    
    ## Getter for property: (float) Smoothness
    ##   the smoothness.  
    ##   
    ##         This value is used to specifies the level of smoothness of the output geometry.
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return float
    @property
    def Smoothness(self) -> float:
        """
        Getter for property: (float) Smoothness
          the smoothness.  
          
                This value is used to specifies the level of smoothness of the output geometry.
                  
         
        """
        pass
    
    ## Setter for property: (float) Smoothness

    ##   the smoothness.  
    ##   
    ##         This value is used to specifies the level of smoothness of the output geometry.
    ##           
    ##  
    ## Setter License requirements: nx_implicit (" NX Implicit Modeling")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @Smoothness.setter
    def Smoothness(self, smoothness: float):
        """
        Setter for property: (float) Smoothness
          the smoothness.  
          
                This value is used to specifies the level of smoothness of the output geometry.
                  
         
        """
        pass
    
    ## Getter for property: (bool) UpdateDefaultVoxelSizeBasedOnFirstOperation
    ##   the flag to update default voxel size based on the size of first operation
    ##          <br> 
    ##         This API is now deprecated.  
    ##   
    ##         Please use @link NXOpen::Implicit::OperationBuilder::VoxelSizePercent NXOpen::Implicit::OperationBuilder::VoxelSizePercent@endlink  instead.
    ##          <br> 
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX1980.0.0.  Please use @link NXOpen::Implicit::OperationBuilder::VoxelSizePercent NXOpen::Implicit::OperationBuilder::VoxelSizePercent@endlink  instead.  <br> 

    ## @return bool
    @property
    def UpdateDefaultVoxelSizeBasedOnFirstOperation(self) -> bool:
        """
        Getter for property: (bool) UpdateDefaultVoxelSizeBasedOnFirstOperation
          the flag to update default voxel size based on the size of first operation
                 <br> 
                This API is now deprecated.  
          
                Please use @link NXOpen::Implicit::OperationBuilder::VoxelSizePercent NXOpen::Implicit::OperationBuilder::VoxelSizePercent@endlink  instead.
                 <br> 
                  
         
        """
        pass
    
    ## Setter for property: (bool) UpdateDefaultVoxelSizeBasedOnFirstOperation

    ##   the flag to update default voxel size based on the size of first operation
    ##          <br> 
    ##         This API is now deprecated.  
    ##   
    ##         Please use @link NXOpen::Implicit::OperationBuilder::VoxelSizePercent NXOpen::Implicit::OperationBuilder::VoxelSizePercent@endlink  instead.
    ##          <br> 
    ##           
    ##  
    ## Setter License requirements: nx_implicit (" NX Implicit Modeling")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX1980.0.0.  Please use @link NXOpen::Implicit::OperationBuilder::VoxelSizePercent NXOpen::Implicit::OperationBuilder::VoxelSizePercent@endlink  instead.  <br> 

    @UpdateDefaultVoxelSizeBasedOnFirstOperation.setter
    def UpdateDefaultVoxelSizeBasedOnFirstOperation(self, updateVoxelSize: bool):
        """
        Setter for property: (bool) UpdateDefaultVoxelSizeBasedOnFirstOperation
          the flag to update default voxel size based on the size of first operation
                 <br> 
                This API is now deprecated.  
          
                Please use @link NXOpen::Implicit::OperationBuilder::VoxelSizePercent NXOpen::Implicit::OperationBuilder::VoxelSizePercent@endlink  instead.
                 <br> 
                  
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) VoxelSizePercent
    ##   the size of voxels in percentage of body size  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def VoxelSizePercent(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) VoxelSizePercent
          the size of voxels in percentage of body size  
            
         
        """
        pass
    
##  Represents a Scherk Implicit Operation.  <br> To create or edit an instance of this class, use @link NXOpen::Implicit::EquationOperationBuilder  NXOpen::Implicit::EquationOperationBuilder @endlink  <br> 
## 
##   <br>  Created in NX1953.0.0  <br> 

class Scherk(EquationOperation): 
    """ Represents a Scherk Implicit Operation. """
    pass


##  Represents a Schoen Implicit Operation.  <br> To create or edit an instance of this class, use @link NXOpen::Implicit::EquationOperationBuilder  NXOpen::Implicit::EquationOperationBuilder @endlink  <br> 
## 
##   <br>  Created in NX1953.0.0  <br> 

class Schoen(EquationOperation): 
    """ Represents a Schoen Implicit Operation. """
    pass


##  Represents a Schwarz Implicit Operation.  <br> To create or edit an instance of this class, use @link NXOpen::Implicit::EquationOperationBuilder  NXOpen::Implicit::EquationOperationBuilder @endlink  <br> 
## 
##   <br>  Created in NX1953.0.0  <br> 

class Schwarz(EquationOperation): 
    """ Represents a Schwarz Implicit Operation. """
    pass


import NXOpen
## 
##     Represents a Implicit.ShellBuilder.
##     It will shell the selected body inside Implicit Task Environment.
##      <br> To create a new instance of this class, use @link NXOpen::Implicit::ImplicitOperationCollection::CreateShellBuilder  NXOpen::Implicit::ImplicitOperationCollection::CreateShellBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## Thickness.Value </term> <description> 
##  
## 5.0 (millimeters part), 0.2 (inches part) </description> </item> 
## 
## <item><term> 
##  
## TypeOfShell </term> <description> 
##  
## Closed </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX1953.0.0  <br> 

class ShellBuilder(OperationBuilder): 
    """
    Represents a Implicit.ShellBuilder.
    It will shell the selected body inside Implicit Task Environment.
    """


    ##  Type of Shell 
    ##  Creates a closed Shell 
    class Type(Enum):
        """
        Members Include: <Closed> <Open>
        """
        Closed: int
        Open: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ShellBuilder.Type:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link NXOpen.ExpressionCollectorSetList NXOpen.ExpressionCollectorSetList@endlink) AlternateThicknessList
    ##   the alternate thickness list, in order to give different thickness for different faces.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.ExpressionCollectorSetList
    @property
    def AlternateThicknessList(self) -> NXOpen.ExpressionCollectorSetList:
        """
        Getter for property: (@link NXOpen.ExpressionCollectorSetList NXOpen.ExpressionCollectorSetList@endlink) AlternateThicknessList
          the alternate thickness list, in order to give different thickness for different faces.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) BodyToOffset
    ##   the body to shell   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.ScCollector
    @property
    def BodyToOffset(self) -> NXOpen.ScCollector:
        """
        Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) BodyToOffset
          the body to shell   
            
         
        """
        pass
    
    ## Getter for property: (bool) DefaultThicknessDirectionReversed
    ##   the default thickness directions is reversed   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return bool
    @property
    def DefaultThicknessDirectionReversed(self) -> bool:
        """
        Getter for property: (bool) DefaultThicknessDirectionReversed
          the default thickness directions is reversed   
            
         
        """
        pass
    
    ## Setter for property: (bool) DefaultThicknessDirectionReversed

    ##   the default thickness directions is reversed   
    ##     
    ##  
    ## Setter License requirements: nx_implicit (" NX Implicit Modeling")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @DefaultThicknessDirectionReversed.setter
    def DefaultThicknessDirectionReversed(self, reverseDirection: bool):
        """
        Setter for property: (bool) DefaultThicknessDirectionReversed
          the default thickness directions is reversed   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) FacesToOpen
    ##   the faces for open region of shell   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.ScCollector
    @property
    def FacesToOpen(self) -> NXOpen.ScCollector:
        """
        Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) FacesToOpen
          the faces for open region of shell   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Thickness
    ##   the thickness - offset distance  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Thickness(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Thickness
          the thickness - offset distance  
            
         
        """
        pass
    
    ## Getter for property: (@link ShellBuilder.Type NXOpen.Implicit.ShellBuilder.Type@endlink) TypeOfShell
    ##   the shell type, which is open or closed.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return ShellBuilder.Type
    @property
    def TypeOfShell(self) -> ShellBuilder.Type:
        """
        Getter for property: (@link ShellBuilder.Type NXOpen.Implicit.ShellBuilder.Type@endlink) TypeOfShell
          the shell type, which is open or closed.  
             
         
        """
        pass
    
    ## Setter for property: (@link ShellBuilder.Type NXOpen.Implicit.ShellBuilder.Type@endlink) TypeOfShell

    ##   the shell type, which is open or closed.  
    ##      
    ##  
    ## Setter License requirements: nx_implicit (" NX Implicit Modeling")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @TypeOfShell.setter
    def TypeOfShell(self, shellType: ShellBuilder.Type):
        """
        Setter for property: (@link ShellBuilder.Type NXOpen.Implicit.ShellBuilder.Type@endlink) TypeOfShell
          the shell type, which is open or closed.  
             
         
        """
        pass
    
##  Represents a Shell Implicit Operation.  <br> To create or edit an instance of this class, use @link NXOpen::Implicit::ShellBuilder  NXOpen::Implicit::ShellBuilder @endlink  <br> 
## 
##   <br>  Created in NX1953.0.0  <br> 

class Shell(ImplicitOperation): 
    """ Represents a Shell Implicit Operation. """
    pass


import NXOpen
##  
##     Represents a Implicit.SphereBuilder.
##     It will create a sphere inside the Implicit task environment.
##      <br> To create a new instance of this class, use @link NXOpen::Implicit::ImplicitOperationCollection::CreateSphereBuilder  NXOpen::Implicit::ImplicitOperationCollection::CreateSphereBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## AssociativeOrigin </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## Diameter.Value </term> <description> 
##  
## 100 (millimeters part), 4 (inches part) </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX1953.0.0  <br> 

class SphereBuilder(OperationBuilder): 
    """ 
    Represents a Implicit.SphereBuilder.
    It will create a sphere inside the Implicit task environment.
    """


    ## Getter for property: (bool) AssociativeOrigin
    ##   the option to keep the sphere associative with the specified Origin  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return bool
    @property
    def AssociativeOrigin(self) -> bool:
        """
        Getter for property: (bool) AssociativeOrigin
          the option to keep the sphere associative with the specified Origin  
            
         
        """
        pass
    
    ## Setter for property: (bool) AssociativeOrigin

    ##   the option to keep the sphere associative with the specified Origin  
    ##     
    ##  
    ## Setter License requirements: nx_implicit (" NX Implicit Modeling")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @AssociativeOrigin.setter
    def AssociativeOrigin(self, associativeOrigin: bool):
        """
        Setter for property: (bool) AssociativeOrigin
          the option to keep the sphere associative with the specified Origin  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) CenterPoint
    ##   the center Point   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Point
    @property
    def CenterPoint(self) -> NXOpen.Point:
        """
        Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) CenterPoint
          the center Point   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) CenterPoint

    ##   the center Point   
    ##     
    ##  
    ## Setter License requirements: nx_implicit (" NX Implicit Modeling")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @CenterPoint.setter
    def CenterPoint(self, centerPoint: NXOpen.Point):
        """
        Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) CenterPoint
          the center Point   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Diameter
    ##   the diameter   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Diameter(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Diameter
          the diameter   
            
         
        """
        pass
    
##  Represents a Sphere Implicit Operation.  <br> To create or edit an instance of this class, use @link NXOpen::Implicit::SphereBuilder  NXOpen::Implicit::SphereBuilder @endlink  <br> 
## 
##   <br>  Created in NX1953.0.0  <br> 

class Sphere(ImplicitOperation): 
    """ Represents a Sphere Implicit Operation. """
    pass


##  Represents a Split P Implicit Operation.  <br> To create or edit an instance of this class, use @link NXOpen::Implicit::EquationOperationBuilder  NXOpen::Implicit::EquationOperationBuilder @endlink  <br> 
## 
##   <br>  Created in NX2007.0.0  <br> 

class SplitP(EquationOperation): 
    """ Represents a Split P Implicit Operation. """
    pass


## 
##     Represents an Implicit.SubtractBuilder.
##     It will create a subtract operation on the selected bodies.
##      <br> To create a new instance of this class, use @link NXOpen::Implicit::ImplicitOperationCollection::CreateSubtractBuilder  NXOpen::Implicit::ImplicitOperationCollection::CreateSubtractBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## BlendFactor </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## CreateBlends (deprecated) </term> <description> 
##  
## 0 </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX1953.0.0  <br> 

class SubtractBuilder(BooleanBuilder): 
    """
    Represents an Implicit.SubtractBuilder.
    It will create a subtract operation on the selected bodies.
    """
    pass


##  Represents a Subtract Implicit Operation.  <br> To create or edit an instance of this class, use @link NXOpen::Implicit::BooleanBuilder  NXOpen::Implicit::BooleanBuilder @endlink  <br> 
## 
##   <br>  Created in NX1953.0.0  <br> 

class Subtract(Boolean): 
    """ Represents a Subtract Implicit Operation. """
    pass


import NXOpen
## 
##     Represents a Implicit.ThickenBuilder.
##     It will Thicken the selected body inside Implicit Task Environment.
##      <br> To create a new instance of this class, use @link NXOpen::Implicit::ImplicitOperationCollection::CreateThickenBuilder  NXOpen::Implicit::ImplicitOperationCollection::CreateThickenBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## Thickness.Value </term> <description> 
##  
## 5.0 (millimeters part), 0.2 (inches part) </description> </item> 
## 
## <item><term> 
##  
## ThicknessMethod </term> <description> 
##  
## Constant </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX1980.0.0  <br> 

class ThickenBuilder(OperationBuilder): 
    """
    Represents a Implicit.ThickenBuilder.
    It will Thicken the selected body inside Implicit Task Environment.
    """


    ##  Thickness methods
    ##  Constant thickness 
    class ThicknessMethodType(Enum):
        """
        Members Include: <Constant> <Variable>
        """
        Constant: int
        Variable: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ThickenBuilder.ThicknessMethodType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) FacesToThicken
    ##   the faces to thicken   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.ScCollector
    @property
    def FacesToThicken(self) -> NXOpen.ScCollector:
        """
        Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) FacesToThicken
          the faces to thicken   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Thickness
    ##   the thickness - Symmetric offset distance  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Thickness(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Thickness
          the thickness - Symmetric offset distance  
            
         
        """
        pass
    
    ## Getter for property: (@link ThickenBuilder.ThicknessMethodType NXOpen.Implicit.ThickenBuilder.ThicknessMethodType@endlink) ThicknessMethod
    ##   the thickness method
    ##         Methods of adding thickness : Constant and Variable
    ##           
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return ThickenBuilder.ThicknessMethodType
    @property
    def ThicknessMethod(self) -> ThickenBuilder.ThicknessMethodType:
        """
        Getter for property: (@link ThickenBuilder.ThicknessMethodType NXOpen.Implicit.ThickenBuilder.ThicknessMethodType@endlink) ThicknessMethod
          the thickness method
                Methods of adding thickness : Constant and Variable
                  
            
         
        """
        pass
    
    ## Setter for property: (@link ThickenBuilder.ThicknessMethodType NXOpen.Implicit.ThickenBuilder.ThicknessMethodType@endlink) ThicknessMethod

    ##   the thickness method
    ##         Methods of adding thickness : Constant and Variable
    ##           
    ##     
    ##  
    ## Setter License requirements: nx_implicit (" NX Implicit Modeling")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @ThicknessMethod.setter
    def ThicknessMethod(self, thicknessMethod: ThickenBuilder.ThicknessMethodType):
        """
        Setter for property: (@link ThickenBuilder.ThicknessMethodType NXOpen.Implicit.ThickenBuilder.ThicknessMethodType@endlink) ThicknessMethod
          the thickness method
                Methods of adding thickness : Constant and Variable
                  
            
         
        """
        pass
    
##  Represents a Thicken Implicit Operation.  <br> To create or edit an instance of this class, use @link NXOpen::Implicit::ThickenBuilder  NXOpen::Implicit::ThickenBuilder @endlink  <br> 
## 
##   <br>  Created in NX1980.0.0  <br> 

class Thicken(ImplicitOperation): 
    """ Represents a Thicken Implicit Operation. """
    pass


import NXOpen
##  
##     Represents a Implicit.TorusBuilder.
##     It will create a torus inside the Implicit task environment.
##      <br> To create a new instance of this class, use @link NXOpen::Implicit::ImplicitOperationCollection::CreateTorusBuilder  NXOpen::Implicit::ImplicitOperationCollection::CreateTorusBuilder @endlink  <br> 
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
## InnerDimension.Value </term> <description> 
##  
## 50 (millimeters part), 2 (inches part) </description> </item> 
## 
## <item><term> 
##  
## OuterDimension.Value </term> <description> 
##  
## 100 (millimeters part), 4 (inches part) </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX1953.0.0  <br> 

class TorusBuilder(OperationBuilder): 
    """ 
    Represents a Implicit.TorusBuilder.
    It will create a torus inside the Implicit task environment.
    """


    ## Getter for property: (bool) Associative
    ##   the option to keep the Torus associative with the specified Center Point and Orientation.  
    ##   
    ##             this does not apply to selection methods Dynamic, Inferred, Absolute CSYS, and CSYS of Current View.
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return bool
    @property
    def Associative(self) -> bool:
        """
        Getter for property: (bool) Associative
          the option to keep the Torus associative with the specified Center Point and Orientation.  
          
                    this does not apply to selection methods Dynamic, Inferred, Absolute CSYS, and CSYS of Current View.
                  
         
        """
        pass
    
    ## Setter for property: (bool) Associative

    ##   the option to keep the Torus associative with the specified Center Point and Orientation.  
    ##   
    ##             this does not apply to selection methods Dynamic, Inferred, Absolute CSYS, and CSYS of Current View.
    ##           
    ##  
    ## Setter License requirements: nx_implicit (" NX Implicit Modeling")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @Associative.setter
    def Associative(self, associativeCenterPoint: bool):
        """
        Setter for property: (bool) Associative
          the option to keep the Torus associative with the specified Center Point and Orientation.  
          
                    this does not apply to selection methods Dynamic, Inferred, Absolute CSYS, and CSYS of Current View.
                  
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.CartesianCoordinateSystem NXOpen.CartesianCoordinateSystem@endlink) CenterAndOrientation
    ##   the centerPoint Point   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.CartesianCoordinateSystem
    @property
    def CenterAndOrientation(self) -> NXOpen.CartesianCoordinateSystem:
        """
        Getter for property: (@link NXOpen.CartesianCoordinateSystem NXOpen.CartesianCoordinateSystem@endlink) CenterAndOrientation
          the centerPoint Point   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.CartesianCoordinateSystem NXOpen.CartesianCoordinateSystem@endlink) CenterAndOrientation

    ##   the centerPoint Point   
    ##     
    ##  
    ## Setter License requirements: nx_implicit (" NX Implicit Modeling")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @CenterAndOrientation.setter
    def CenterAndOrientation(self, csys: NXOpen.CartesianCoordinateSystem):
        """
        Setter for property: (@link NXOpen.CartesianCoordinateSystem NXOpen.CartesianCoordinateSystem@endlink) CenterAndOrientation
          the centerPoint Point   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) InnerDimension
    ##   the inner dimension   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def InnerDimension(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) InnerDimension
          the inner dimension   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) OuterDimension
    ##   the outer dimension   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def OuterDimension(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) OuterDimension
          the outer dimension   
            
         
        """
        pass
    
##  Represents a Torus Implicit Operation.  <br> To create or edit an instance of this class, use @link NXOpen::Implicit::TorusBuilder  NXOpen::Implicit::TorusBuilder @endlink  <br> 
## 
##   <br>  Created in NX1953.0.0  <br> 

class Torus(ImplicitOperation): 
    """ Represents a Torus Implicit Operation. """
    pass


## 
##     Represents an Implicit.UniteBuilder.
##     It will create an unite operation on the selected bodies.
##      <br> To create a new instance of this class, use @link NXOpen::Implicit::ImplicitOperationCollection::CreateUniteBuilder  NXOpen::Implicit::ImplicitOperationCollection::CreateUniteBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## BlendFactor </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## CreateBlends (deprecated) </term> <description> 
##  
## false </description> </item> 
## 
## <item><term> 
##  
## KeepTarget </term> <description> 
##  
## false </description> </item> 
## 
## <item><term> 
##  
## KeepTool </term> <description> 
##  
## false </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX1953.0.0  <br> 

class UniteBuilder(BooleanBuilder): 
    """
    Represents an Implicit.UniteBuilder.
    It will create an unite operation on the selected bodies.
    """
    pass


##  Represents a Unite Implicit Operation.  <br> To create or edit an instance of this class, use @link NXOpen::Implicit::BooleanBuilder  NXOpen::Implicit::BooleanBuilder @endlink  <br> 
## 
##   <br>  Created in NX1953.0.0  <br> 

class Unite(Boolean): 
    """ Represents a Unite Implicit Operation. """
    pass


## @package NXOpen.Implicit
## Classes, Enums and Structs under NXOpen.Implicit namespace

##  @link CartesianPatternBuilderBoundaryConditionOptionType NXOpen.Implicit.CartesianPatternBuilderBoundaryConditionOptionType @endlink is an alias for @link CartesianPatternBuilder.BoundaryConditionOptionType NXOpen.Implicit.CartesianPatternBuilder.BoundaryConditionOptionType@endlink
CartesianPatternBuilderBoundaryConditionOptionType = CartesianPatternBuilder.BoundaryConditionOptionType


##  @link EquationOperationBuilderBoundaryConditionOptionType NXOpen.Implicit.EquationOperationBuilderBoundaryConditionOptionType @endlink is an alias for @link EquationOperationBuilder.BoundaryConditionOptionType NXOpen.Implicit.EquationOperationBuilder.BoundaryConditionOptionType@endlink
EquationOperationBuilderBoundaryConditionOptionType = EquationOperationBuilder.BoundaryConditionOptionType


##  @link EquationOperationBuilderEquationType NXOpen.Implicit.EquationOperationBuilderEquationType @endlink is an alias for @link EquationOperationBuilder.EquationType NXOpen.Implicit.EquationOperationBuilder.EquationType@endlink
EquationOperationBuilderEquationType = EquationOperationBuilder.EquationType


##  @link EquationOperationBuilderThicknessMethodType NXOpen.Implicit.EquationOperationBuilderThicknessMethodType @endlink is an alias for @link EquationOperationBuilder.ThicknessMethodType NXOpen.Implicit.EquationOperationBuilder.ThicknessMethodType@endlink
EquationOperationBuilderThicknessMethodType = EquationOperationBuilder.ThicknessMethodType


##  @link GeneralEquationOperationBuilderBoundaryOptionsEnum NXOpen.Implicit.GeneralEquationOperationBuilderBoundaryOptionsEnum @endlink is an alias for @link GeneralEquationOperationBuilder.BoundaryOptionsEnum NXOpen.Implicit.GeneralEquationOperationBuilder.BoundaryOptionsEnum@endlink
GeneralEquationOperationBuilderBoundaryOptionsEnum = GeneralEquationOperationBuilder.BoundaryOptionsEnum


##  @link GeneralEquationOperationBuilderThicknessMethodType NXOpen.Implicit.GeneralEquationOperationBuilderThicknessMethodType @endlink is an alias for @link GeneralEquationOperationBuilder.ThicknessMethodType NXOpen.Implicit.GeneralEquationOperationBuilder.ThicknessMethodType@endlink
GeneralEquationOperationBuilderThicknessMethodType = GeneralEquationOperationBuilder.ThicknessMethodType


##  @link ShellBuilderType NXOpen.Implicit.ShellBuilderType @endlink is an alias for @link ShellBuilder.Type NXOpen.Implicit.ShellBuilder.Type@endlink
ShellBuilderType = ShellBuilder.Type


##  @link ThickenBuilderThicknessMethodType NXOpen.Implicit.ThickenBuilderThicknessMethodType @endlink is an alias for @link ThickenBuilder.ThicknessMethodType NXOpen.Implicit.ThickenBuilder.ThicknessMethodType@endlink
ThickenBuilderThicknessMethodType = ThickenBuilder.ThicknessMethodType


