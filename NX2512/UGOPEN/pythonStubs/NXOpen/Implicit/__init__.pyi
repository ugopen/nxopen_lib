from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
class BlockBuilder(OperationBuilder): 
    """ 
    Represents a Implicit.BlockBuilder.
    It will create a block inside the Implicit task environment.
    """
    @property
    def Associative(self) -> bool:
        """
        Getter for property: (bool) Associative
         Returns the option to keep the block associative with the specified Origin And Orientation.  
          
                    this does not apply to selection methods Dynamic, Inferred, Absolute CSYS, and CSYS of Current View.
                  
         
        """
        pass
    @Associative.setter
    def Associative(self, associativeOrigin: bool):
        """
        Setter for property: (bool) Associative
         Returns the option to keep the block associative with the specified Origin And Orientation.  
          
                    this does not apply to selection methods Dynamic, Inferred, Absolute CSYS, and CSYS of Current View.
                  
         
        """
        pass
    @property
    def Height(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Height
         Returns the height ZC   
            
         
        """
        pass
    @property
    def Length(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Length
         Returns the length XC   
            
         
        """
        pass
    @property
    def OriginAndOrientation(self) -> NXOpen.CartesianCoordinateSystem:
        """
        Getter for property: ( NXOpen.CartesianCoordinateSystem) OriginAndOrientation
         Returns the origin Point   
            
         
        """
        pass
    @OriginAndOrientation.setter
    def OriginAndOrientation(self, csys: NXOpen.CartesianCoordinateSystem):
        """
        Setter for property: ( NXOpen.CartesianCoordinateSystem) OriginAndOrientation
         Returns the origin Point   
            
         
        """
        pass
    @property
    def Width(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Width
         Returns the width YC   
            
         
        """
        pass
class Block(ImplicitOperation): 
    """ Represents a Block Implicit Operation. """
    pass
import NXOpen
class BooleanBuilder(OperationBuilder): 
    """
    Represents an Implicit.BooleanBuilder.
    It will create a boolean operation (Unite, Subtract or Intersect) on the selected bodies.
    """
    class BlendMethodType(Enum):
        """
        Members Include: 
         |Continuous|  Creates a nearly curvature continuous blend. 
         |Round|  Creates a rolling ball like blend. 
         |Chamfer| 

        """
        Continuous: int
        Round: int
        Chamfer: int
        @staticmethod
        def ValueOf(value: int) -> BooleanBuilder.BlendMethodType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def BlendFactor(self) -> int:
        """
        Getter for property: (int) BlendFactor
         Returns the blend factor   
            
         
        """
        pass
    @BlendFactor.setter
    def BlendFactor(self, blendFactor: int):
        """
        Setter for property: (int) BlendFactor
         Returns the blend factor   
            
         
        """
        pass
    @property
    def BlendMethod(self) -> BooleanBuilder.BlendMethodType:
        """
        Getter for property: ( BooleanBuilder.BlendMethodType NXOpen.) BlendMethod
         Returns the blend method   
            
         
        """
        pass
    @BlendMethod.setter
    def BlendMethod(self, blendMethod: BooleanBuilder.BlendMethodType):
        """
        Setter for property: ( BooleanBuilder.BlendMethodType NXOpen.) BlendMethod
         Returns the blend method   
            
         
        """
        pass
    @property
    def CreateBlends(self) -> bool:
        """
        Getter for property: (bool) CreateBlends
         Returns the create blends option  
            
         
        """
        pass
    @CreateBlends.setter
    def CreateBlends(self, createBlends: bool):
        """
        Setter for property: (bool) CreateBlends
         Returns the create blends option  
            
         
        """
        pass
    @property
    def KeepTarget(self) -> bool:
        """
        Getter for property: (bool) KeepTarget
         Returns the keep target option  
            
         
        """
        pass
    @KeepTarget.setter
    def KeepTarget(self, keepTarget: bool):
        """
        Setter for property: (bool) KeepTarget
         Returns the keep target option  
            
         
        """
        pass
    @property
    def KeepTool(self) -> bool:
        """
        Getter for property: (bool) KeepTool
         Returns the keep tool option  
            
         
        """
        pass
    @KeepTool.setter
    def KeepTool(self, keepTool: bool):
        """
        Setter for property: (bool) KeepTool
         Returns the keep tool option  
            
         
        """
        pass
    @property
    def TargetBody(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) TargetBody
         Returns the target body   
            
         
        """
        pass
    @property
    def ToolBody(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) ToolBody
         Returns the tool body   
            
         
        """
        pass
    def ComputeBlendRegion(self) -> float:
        """
         The blend region
         Returns blendRegion (float): .
        """
        pass
class Boolean(ImplicitOperation): 
    """ Represents a Boolean Implicit Operation. """
    pass
import NXOpen
class CapChannelBuilder(OperationBuilder): 
    """ Represents a Cap Channel Implicit Operation. """
    class ThicknessMethodType(Enum):
        """
        Members Include: 
         |Inferred| 
         |Constant| 

        """
        Inferred: int
        Constant: int
        @staticmethod
        def ValueOf(value: int) -> CapChannelBuilder.ThicknessMethodType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def BlendFactor(self) -> int:
        """
        Getter for property: (int) BlendFactor
         Returns the blend factor   
            
         
        """
        pass
    @BlendFactor.setter
    def BlendFactor(self, blendFactor: int):
        """
        Setter for property: (int) BlendFactor
         Returns the blend factor   
            
         
        """
        pass
    @property
    def BodyToCap(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) BodyToCap
         Returns the body to cap   
            
         
        """
        pass
    @property
    def PrimaryCapFaces(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) PrimaryCapFaces
         Returns the faces for capping regions of the primary channel   
            
         
        """
        pass
    @property
    def ReverseCapping(self) -> bool:
        """
        Getter for property: (bool) ReverseCapping
         Returns the default primary and secondary cap channel is reversed   
            
         
        """
        pass
    @ReverseCapping.setter
    def ReverseCapping(self, reverseCapping: bool):
        """
        Setter for property: (bool) ReverseCapping
         Returns the default primary and secondary cap channel is reversed   
            
         
        """
        pass
    @property
    def SecondaryCapFaces(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) SecondaryCapFaces
         Returns the faces for capping regions of the secondary channel   
            
         
        """
        pass
    @property
    def Thickness(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Thickness
         Returns the thickness   
            
         
        """
        pass
    @property
    def ThicknessMethod(self) -> CapChannelBuilder.ThicknessMethodType:
        """
        Getter for property: ( CapChannelBuilder.ThicknessMethodType NXOpen.) ThicknessMethod
         Returns the thickness type   
            
         
        """
        pass
    @ThicknessMethod.setter
    def ThicknessMethod(self, thicknessType: CapChannelBuilder.ThicknessMethodType):
        """
        Setter for property: ( CapChannelBuilder.ThicknessMethodType NXOpen.) ThicknessMethod
         Returns the thickness type   
            
         
        """
        pass
class CapChannel(ImplicitOperation): 
    """ Represents a CapChannel Implicit Operation. """
    pass
import NXOpen
class CartesianPatternBuilder(OperationBuilder): 
    """
    Represents a Implicit.CartesianPatternBuilder.
    The unit cell body will be scaled to the specified unit cell size and patterned in X, Y and Z orientation until it fills the boundary body (or it voids).
    """
    class BoundaryConditionOptionType(Enum):
        """
        Members Include: 
         |SolidVolume|  Solid region 
         |VoidVolume|  Void region 
         |VoidVolumeAndUnite| 

        """
        SolidVolume: int
        VoidVolume: int
        VoidVolumeAndUnite: int
        @staticmethod
        def ValueOf(value: int) -> CartesianPatternBuilder.BoundaryConditionOptionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def BlendFactor(self) -> int:
        """
        Getter for property: (int) BlendFactor
         Returns the blend factor.  
          
                factor to adjust the blend of intersections between tool and target body. 
                No Blend(0) - to - large Blends(100)
                  
         
        """
        pass
    @BlendFactor.setter
    def BlendFactor(self, blendFactor: int):
        """
        Setter for property: (int) BlendFactor
         Returns the blend factor.  
          
                factor to adjust the blend of intersections between tool and target body. 
                No Blend(0) - to - large Blends(100)
                  
         
        """
        pass
    @property
    def BoundaryBody(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) BoundaryBody
         Returns the input body.  
          
                As boundary body a solid body that is either an implicit body (within featureTE)
                or a parametric body from outside the TE can be provided.
                  
         
        """
        pass
    @property
    def BoundaryConditionOption(self) -> CartesianPatternBuilder.BoundaryConditionOptionType:
        """
        Getter for property: ( CartesianPatternBuilder.BoundaryConditionOptionType NXOpen.) BoundaryConditionOption
         Returns the Boundary Condition Option
                Solid volume fill, void volume fill or void volume fill with unite to outer body
                  
            
         
        """
        pass
    @BoundaryConditionOption.setter
    def BoundaryConditionOption(self, boundaryConditionOption: CartesianPatternBuilder.BoundaryConditionOptionType):
        """
        Setter for property: ( CartesianPatternBuilder.BoundaryConditionOptionType NXOpen.) BoundaryConditionOption
         Returns the Boundary Condition Option
                Solid volume fill, void volume fill or void volume fill with unite to outer body
                  
            
         
        """
        pass
    @property
    def EdgeLength(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) EdgeLength
         Returns the edge length.  
          
                Edge length in X, Y and Z direction if it is a uniform cube.
                  
         
        """
        pass
    @property
    def LocationAndOrientation(self) -> NXOpen.CoordinateSystem:
        """
        Getter for property: ( NXOpen.CoordinateSystem) LocationAndOrientation
         Returns the location and orientation of the seed cell.  
          
                The orientation can be inferred from objects inside or outside the TE.
                  
         
        """
        pass
    @LocationAndOrientation.setter
    def LocationAndOrientation(self, locationAndOrientation: NXOpen.CoordinateSystem):
        """
        Setter for property: ( NXOpen.CoordinateSystem) LocationAndOrientation
         Returns the location and orientation of the seed cell.  
          
                The orientation can be inferred from objects inside or outside the TE.
                  
         
        """
        pass
    @property
    def SizeX(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) SizeX
         Returns the size x.  
          
                Edge length in X if it is a non-uniform cube.
                  
         
        """
        pass
    @property
    def SizeY(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) SizeY
         Returns the size y.  
          
                Edge length in Y if it is a non-uniform cube.
                  
         
        """
        pass
    @property
    def SizeZ(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) SizeZ
         Returns the size z.  
          
                Edge length in Z if it is a non-uniform cube.
                  
         
        """
        pass
    @property
    def UniformCubeFlag(self) -> bool:
        """
        Getter for property: (bool) UniformCubeFlag
         Returns the uniform cube toggle.  
          
                A uniform cube with one edge length in all three
                directions can be defined or specify the length for each axis separately.
                ture for uniform cube false otherwise.
                  
         
        """
        pass
    @UniformCubeFlag.setter
    def UniformCubeFlag(self, uniformCubeFlag: bool):
        """
        Setter for property: (bool) UniformCubeFlag
         Returns the uniform cube toggle.  
          
                A uniform cube with one edge length in all three
                directions can be defined or specify the length for each axis separately.
                ture for uniform cube false otherwise.
                  
         
        """
        pass
    @property
    def UnitCellBody(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) UnitCellBody
         Returns the unit cell body.  
          
                The unit cell body will be scaled to the specified unit cell size.
                  
         
        """
        pass
class CartesianPattern(ImplicitOperation): 
    """ Represents a Cartesian Pattern Implicit Operation. """
    pass
import NXOpen
class ChannelPlotBuilder(NXOpen.Builder): 
    """ Represents command to colorize the two channels of TPMS bodies. """
    @property
    def FacetFace(self) -> NXOpen.DisplayableObject:
        """
        Getter for property: ( NXOpen.DisplayableObject) FacetFace
         Returns the collector of facets on the channel to colorize.  
             
         
        """
        pass
    @FacetFace.setter
    def FacetFace(self, facetFace: NXOpen.DisplayableObject):
        """
        Setter for property: ( NXOpen.DisplayableObject) FacetFace
         Returns the collector of facets on the channel to colorize.  
             
         
        """
        pass
    @property
    def PrimaryColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) PrimaryColor
         Returns the primary color   
            
         
        """
        pass
    @PrimaryColor.setter
    def PrimaryColor(self, primaryColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) PrimaryColor
         Returns the primary color   
            
         
        """
        pass
    @property
    def SecondaryColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) SecondaryColor
         Returns the secondary color   
            
         
        """
        pass
    @SecondaryColor.setter
    def SecondaryColor(self, secondaryColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) SecondaryColor
         Returns the secondary color   
            
         
        """
        pass
    @property
    def SelectedPoint(self) -> GeometricConstraintDataManager:
        """
        Getter for property: ( GeometricConstraintDataManager NXOpen.) SelectedPoint
         Returns the selected points.  
             
         
        """
        pass
import NXOpen
class ChannelPlot(NXOpen.Object): 
    """ Represents command to set channel plot """
    def RemoveAllChannelPlots(implicit_model: Feature) -> None:
        """
         Remove all channel plots of Implicit Model 
        """
        pass
import NXOpen
class ConeBuilder(OperationBuilder): 
    """ 
    Represents a Implicit.ConeBuilder.
    It will create a cone inside the Implicit task environment.
    """
    @property
    def Associative(self) -> bool:
        """
        Getter for property: (bool) Associative
         Returns the option to keep the cone associative with the specified Center And Orientation.  
          
                    this does not apply to selection methods Dynamic, Inferred, Absolute CSYS, and CSYS of Current View.
                  
         
        """
        pass
    @Associative.setter
    def Associative(self, associativeCenter: bool):
        """
        Setter for property: (bool) Associative
         Returns the option to keep the cone associative with the specified Center And Orientation.  
          
                    this does not apply to selection methods Dynamic, Inferred, Absolute CSYS, and CSYS of Current View.
                  
         
        """
        pass
    @property
    def BaseDiameter(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) BaseDiameter
         Returns the cone base diameter   
            
         
        """
        pass
    @property
    def CenterAndOrientation(self) -> NXOpen.CartesianCoordinateSystem:
        """
        Getter for property: ( NXOpen.CartesianCoordinateSystem) CenterAndOrientation
         Returns the origin Point   
            
         
        """
        pass
    @CenterAndOrientation.setter
    def CenterAndOrientation(self, csys: NXOpen.CartesianCoordinateSystem):
        """
        Setter for property: ( NXOpen.CartesianCoordinateSystem) CenterAndOrientation
         Returns the origin Point   
            
         
        """
        pass
    @property
    def Height(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Height
         Returns the height   
            
         
        """
        pass
    @property
    def TopDiameter(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) TopDiameter
         Returns the cone top diameter   
            
         
        """
        pass
class Cone(ImplicitOperation): 
    """ Represents a Cone Implicit Operation. """
    pass
import NXOpen
class CylinderBuilder(OperationBuilder): 
    """ 
    Represents a Implicit.CylinderBuilder.
    It will create a cylinder inside the Implicit task environment.
    """
    @property
    def Associative(self) -> bool:
        """
        Getter for property: (bool) Associative
         Returns the option to keep the cylinder associative with the specified Center And Orientation.  
          
                    this does not apply to selection methods Dynamic, Inferred, Absolute CSYS, and CSYS of Current View.
                  
         
        """
        pass
    @Associative.setter
    def Associative(self, associativeCenter: bool):
        """
        Setter for property: (bool) Associative
         Returns the option to keep the cylinder associative with the specified Center And Orientation.  
          
                    this does not apply to selection methods Dynamic, Inferred, Absolute CSYS, and CSYS of Current View.
                  
         
        """
        pass
    @property
    def CenterAndOrientation(self) -> NXOpen.CartesianCoordinateSystem:
        """
        Getter for property: ( NXOpen.CartesianCoordinateSystem) CenterAndOrientation
         Returns the origin Point   
            
         
        """
        pass
    @CenterAndOrientation.setter
    def CenterAndOrientation(self, csys: NXOpen.CartesianCoordinateSystem):
        """
        Setter for property: ( NXOpen.CartesianCoordinateSystem) CenterAndOrientation
         Returns the origin Point   
            
         
        """
        pass
    @property
    def Diameter(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Diameter
         Returns the cylinder diameter   
            
         
        """
        pass
    @property
    def Height(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Height
         Returns the height   
            
         
        """
        pass
class Cylinder(ImplicitOperation): 
    """ Represents a Cylinder Implicit Operation. """
    pass
import NXOpen
class CylindricalPatternBuilder(OperationBuilder): 
    """
    Represents a Implicit.CylindricalPatternBuilder.
    The Unit cell will be patterned around the cylinder circumference in unit cell x direction, 
    along cylinder axis in unit cell y direction and 
    stacked up radial with the specified number of layers in unit cell z direction.
    """
    @property
    def CenterAndOrientation(self) -> NXOpen.CartesianCoordinateSystem:
        """
        Getter for property: ( NXOpen.CartesianCoordinateSystem) CenterAndOrientation
         Returns the specified Point 
                Allows you to locate and orient the cylinder.  
          
                  
         
        """
        pass
    @CenterAndOrientation.setter
    def CenterAndOrientation(self, csys: NXOpen.CartesianCoordinateSystem):
        """
        Setter for property: ( NXOpen.CartesianCoordinateSystem) CenterAndOrientation
         Returns the specified Point 
                Allows you to locate and orient the cylinder.  
          
                  
         
        """
        pass
    @property
    def Diameter(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Diameter
         Returns the cylinder diameter   
            
         
        """
        pass
    @property
    def Height(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Height
         Returns the cylinder height   
            
         
        """
        pass
    @property
    def NumberOfCellsAroundCircumference(self) -> int:
        """
        Getter for property: (int) NumberOfCellsAroundCircumference
         Returns the cell count around circumference 
                the number of cells around the circumference of the specified inner cylinder.  
          
                  
         
        """
        pass
    @NumberOfCellsAroundCircumference.setter
    def NumberOfCellsAroundCircumference(self, numCellsAroundCircumference: int):
        """
        Setter for property: (int) NumberOfCellsAroundCircumference
         Returns the cell count around circumference 
                the number of cells around the circumference of the specified inner cylinder.  
          
                  
         
        """
        pass
    @property
    def NumberOfCellsAroundCircumferenceExp(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) NumberOfCellsAroundCircumferenceExp
         Returns the cell count around circumference in expression
                the number of cells around the circumference of the specified inner cylinder.  
          
                  
         
        """
        pass
    @property
    def NumberOfRadialLayers(self) -> int:
        """
        Getter for property: (int) NumberOfRadialLayers
         Returns the radial layers 
                the layers to be stacked up on the outside of the specified inner cylinder.  
          
                  
         
        """
        pass
    @NumberOfRadialLayers.setter
    def NumberOfRadialLayers(self, numRadialLayers: int):
        """
        Setter for property: (int) NumberOfRadialLayers
         Returns the radial layers 
                the layers to be stacked up on the outside of the specified inner cylinder.  
          
                  
         
        """
        pass
    @property
    def NumberOfRadialLayersExp(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) NumberOfRadialLayersExp
         Returns the radial layers in expression
                the layers to be stacked up on the outside of the specified inner cylinder.  
          
                  
         
        """
        pass
    @property
    def UnitCellBody(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) UnitCellBody
         Returns the unit cell body.  
          
                The unit cell body will be scaled uniform so that cell size is around circumference divided by cell count.
                  
         
        """
        pass
class CylindricalPattern(ImplicitOperation): 
    """ Represents a Cylindrical Pattern Implicit Operation. """
    pass
class Diamond(EquationOperation): 
    """ Represents a Diamond Implicit Operation. """
    pass
import NXOpen
class EllipsoidBuilder(OperationBuilder): 
    """ 
    Represents a Implicit.EllipsoidBuilder.
    It will create an Ellipsoid inside the Implicit task environment.
    """
    @property
    def Associative(self) -> bool:
        """
        Getter for property: (bool) Associative
         Returns the option to keep the ellipsoid associative with the specified Center Point and Orientation.  
          
                    this does not apply to selection methods Dynamic, Inferred, Absolute CSYS, and CSYS of Current View.
                  
         
        """
        pass
    @Associative.setter
    def Associative(self, associativeCenterPoint: bool):
        """
        Setter for property: (bool) Associative
         Returns the option to keep the ellipsoid associative with the specified Center Point and Orientation.  
          
                    this does not apply to selection methods Dynamic, Inferred, Absolute CSYS, and CSYS of Current View.
                  
         
        """
        pass
    @property
    def CenterAndOrientation(self) -> NXOpen.CartesianCoordinateSystem:
        """
        Getter for property: ( NXOpen.CartesianCoordinateSystem) CenterAndOrientation
         Returns the origin Point   
            
         
        """
        pass
    @CenterAndOrientation.setter
    def CenterAndOrientation(self, csys: NXOpen.CartesianCoordinateSystem):
        """
        Setter for property: ( NXOpen.CartesianCoordinateSystem) CenterAndOrientation
         Returns the origin Point   
            
         
        """
        pass
    @property
    def Height(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Height
         Returns the height along Z Axis    
            
         
        """
        pass
    @property
    def Length(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Length
         Returns the length along X Axis    
            
         
        """
        pass
    @property
    def Width(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Width
         Returns the width along Y Axis    
            
         
        """
        pass
class Ellipsoid(ImplicitOperation): 
    """ Represents a Ellipsoid Implicit Operation. """
    pass
import NXOpen
import NXOpen.ModlUtils
class EquationOperationBuilder(OperationBuilder): 
    """
    Represents a Implicit.EquationOperationBuilder.
    It will create an Implicit surfaces derived from equations with three variables (x, y, and z) in the 3D space.
    The definition of an implicit surface is that a coordinate is located on the surface if the equation results in zero.
    """
    class BoundaryConditionOptionType(Enum):
        """
        Members Include: 
         |SolidVolume|  Solid region 
         |VoidVolume|  Void region 
         |VoidVolumeAndUnite| 
         |SolidVolumeAndUnite|  Solid region and unite 

        """
        SolidVolume: int
        VoidVolume: int
        VoidVolumeAndUnite: int
        SolidVolumeAndUnite: int
        @staticmethod
        def ValueOf(value: int) -> EquationOperationBuilder.BoundaryConditionOptionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class EquationType(Enum):
        """
        Members Include: 
         |Gyroid|  Gyroid  
         |Schwarz|  Schwarz 
         |Diamond|  Diamond 
         |Neovius|  Neovius 
         |Schoen|  Schoen  
         |Scherk|  Scherk  
         |Lidinoid|  Lidinoid 
         |SplitP|  Split P 

        """
        Gyroid: int
        Schwarz: int
        Diamond: int
        Neovius: int
        Schoen: int
        Scherk: int
        Lidinoid: int
        SplitP: int
        @staticmethod
        def ValueOf(value: int) -> EquationOperationBuilder.EquationType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ThicknessMethodType(Enum):
        """
        Members Include: 
         |Absolute|  Absolute thickness 
         |AbsoluteVariable|  Variable Thickness 
         |Relative| 
         |Approximate| 

        """
        Absolute: int
        AbsoluteVariable: int
        Relative: int
        Approximate: int
        @staticmethod
        def ValueOf(value: int) -> EquationOperationBuilder.ThicknessMethodType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def BlendFactor(self) -> int:
        """
        Getter for property: (int) BlendFactor
         Returns the blend factor.  
          
                factor to adjust the blend of intersections between tool and target body. 
                No Blend(0) - to - large Blends(100)
                  
         
        """
        pass
    @BlendFactor.setter
    def BlendFactor(self, blendFactor: int):
        """
        Setter for property: (int) BlendFactor
         Returns the blend factor.  
          
                factor to adjust the blend of intersections between tool and target body. 
                No Blend(0) - to - large Blends(100)
                  
         
        """
        pass
    @property
    def BoundaryBody(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) BoundaryBody
         Returns the input body.  
          
                Since the equation itself is defined infinitely a boundary body needs to limit its shape.
                As boundary body a solid body that is either an implicit body (within featureTE)
                or a parametric body from outside the TE can be provided.
                  
         
        """
        pass
    @property
    def BoundaryConditionOption(self) -> EquationOperationBuilder.BoundaryConditionOptionType:
        """
        Getter for property: ( EquationOperationBuilder.BoundaryConditionOptionType NXOpen.) BoundaryConditionOption
         Returns the Boundary Condition Option
                Solid volume fill, void volume fill or void volume fill with unite to outer body
                  
            
         
        """
        pass
    @BoundaryConditionOption.setter
    def BoundaryConditionOption(self, boundaryConditionOption: EquationOperationBuilder.BoundaryConditionOptionType):
        """
        Setter for property: ( EquationOperationBuilder.BoundaryConditionOptionType NXOpen.) BoundaryConditionOption
         Returns the Boundary Condition Option
                Solid volume fill, void volume fill or void volume fill with unite to outer body
                  
            
         
        """
        pass
    @property
    def EdgeLength(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) EdgeLength
         Returns the edge length.  
          
                Edge length in X, Y and Z direction if it is a uniform cube.
                  
         
        """
        pass
    @property
    def IsUnitCell(self) -> bool:
        """
        Getter for property: (bool) IsUnitCell
         Returns the flag indiciating if operation represents a unit cell.  
           A unit cell is a triply periodic body with one period.   
         
        """
        pass
    @IsUnitCell.setter
    def IsUnitCell(self, isUnitCell: bool):
        """
        Setter for property: (bool) IsUnitCell
         Returns the flag indiciating if operation represents a unit cell.  
           A unit cell is a triply periodic body with one period.   
         
        """
        pass
    @property
    def KFactor(self) -> float:
        """
        Getter for property: (float) KFactor
         Returns the k factor.  
          
                The porosity of the structure can be controlled by a dimensionless "k Factor".
                The lower the k Factor "thicker" the structure gets. Increasing the k Factor 
                the structure gets thinner and thinner until it splits into multiple regions 
                and finally disappears.
                  
         
        """
        pass
    @KFactor.setter
    def KFactor(self, kFactor: float):
        """
        Setter for property: (float) KFactor
         Returns the k factor.  
          
                The porosity of the structure can be controlled by a dimensionless "k Factor".
                The lower the k Factor "thicker" the structure gets. Increasing the k Factor 
                the structure gets thinner and thinner until it splits into multiple regions 
                and finally disappears.
                  
         
        """
        pass
    @property
    def LocationAndOrientation(self) -> NXOpen.CoordinateSystem:
        """
        Getter for property: ( NXOpen.CoordinateSystem) LocationAndOrientation
         Returns the location and orientation of the seed cell.  
          
                The orientation can be inferred from objects inside or outside the TE.
                  
         
        """
        pass
    @LocationAndOrientation.setter
    def LocationAndOrientation(self, locationAndOrientation: NXOpen.CoordinateSystem):
        """
        Setter for property: ( NXOpen.CoordinateSystem) LocationAndOrientation
         Returns the location and orientation of the seed cell.  
          
                The orientation can be inferred from objects inside or outside the TE.
                  
         
        """
        pass
    @property
    def SizeX(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) SizeX
         Returns the size x.  
          
                Edge length in X if it is a non-uniform cube.
                  
         
        """
        pass
    @property
    def SizeY(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) SizeY
         Returns the size y.  
          
                Edge length in Y if it is a non-uniform cube.
                  
         
        """
        pass
    @property
    def SizeZ(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) SizeZ
         Returns the size z.  
          
                Edge length in Z if it is a non-uniform cube.
                  
         
        """
        pass
    @property
    def TargetBody(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) TargetBody
         Returns the target body for Solid Volume and Unite option.  
          
                Target bodies to be united with the equation body within Boundary Body.
                  
         
        """
        pass
    @property
    def Thickness(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Thickness
         Returns the thickness.  
          
                The equation creates just a surface. To create a solid body the user needs to specify a thickness.
                The surface will be thickened with 50% of that value in both directions.
                  
         
        """
        pass
    @property
    def ThicknessFactor(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ThicknessFactor
         Returns the thickness factor.  
          
                The factor for the relative thickness method.
                  
         
        """
        pass
    @property
    def ThicknessMethod(self) -> EquationOperationBuilder.ThicknessMethodType:
        """
        Getter for property: ( EquationOperationBuilder.ThicknessMethodType NXOpen.) ThicknessMethod
         Returns the thickness method
                Methods of adding thickness to the TPMS structure : Absolute, Absolute variable, Relative
                  
            
         
        """
        pass
    @ThicknessMethod.setter
    def ThicknessMethod(self, thicknessMethod: EquationOperationBuilder.ThicknessMethodType):
        """
        Setter for property: ( EquationOperationBuilder.ThicknessMethodType NXOpen.) ThicknessMethod
         Returns the thickness method
                Methods of adding thickness to the TPMS structure : Absolute, Absolute variable, Relative
                  
            
         
        """
        pass
    @property
    def TypeOfEquation(self) -> EquationOperationBuilder.EquationType:
        """
        Getter for property: ( EquationOperationBuilder.EquationType NXOpen.) TypeOfEquation
         Returns the type of equation   
            
         
        """
        pass
    @TypeOfEquation.setter
    def TypeOfEquation(self, typeOfEquation: EquationOperationBuilder.EquationType):
        """
        Setter for property: ( EquationOperationBuilder.EquationType NXOpen.) TypeOfEquation
         Returns the type of equation   
            
         
        """
        pass
    @property
    def UniformCubeFlag(self) -> bool:
        """
        Getter for property: (bool) UniformCubeFlag
         Returns the uniform cube toggle.  
          
                Since the equation is periodic in 2PI the shape can be defined in a cube of (2PI2PI2PI)
                that will be patterned in X, Y, and Z. A uniform cube with one edge length in all three
                directions can be defined or specify the length for each axis separately.
                ture for uniform cube false otherwise.
                  
         
        """
        pass
    @UniformCubeFlag.setter
    def UniformCubeFlag(self, uniformCubeFlag: bool):
        """
        Setter for property: (bool) UniformCubeFlag
         Returns the uniform cube toggle.  
          
                Since the equation is periodic in 2PI the shape can be defined in a cube of (2PI2PI2PI)
                that will be patterned in X, Y, and Z. A uniform cube with one edge length in all three
                directions can be defined or specify the length for each axis separately.
                ture for uniform cube false otherwise.
                  
         
        """
        pass
    @property
    def VariableThicknessList(self) -> NXOpen.ModlUtils.SelectObjectDimList:
        """
        Getter for property: ( NXOpen.ModlUtils.SelectObjectDimList) VariableThicknessList
         Returns the variable thickness list, in order to assign variable thickness to the TPMS.  
             
         
        """
        pass
    def GetKFactorRange(self) -> Tuple[float, float]:
        """
         Returns the range of K Factor 
         Returns A tuple consisting of (minKFactor, maxKFactor). 
         - minKFactor is: float.
         - maxKFactor is: float.

        """
        pass
class EquationOperation(ImplicitOperation): 
    """ Represents a Equation based Implicit Operation. """
    pass
import NXOpen
import NXOpen.ModlUtils
class GeneralEquationOperationBuilder(OperationBuilder): 
    """
    Represents a Implicit.GeneralEquationOperationBuilder.
    It will create an Implicit surfaces derived from given equation in the 3D space.
    The definition of an implicit surface is that a coordinate is located on the surface if the equation results in zero.
    """
    class BoundaryOptionsEnum(Enum):
        """
        Members Include: 
         |CartesianRange|  Cartesian Range 
         |BoundaryBody|  Boundary Body 

        """
        CartesianRange: int
        BoundaryBody: int
        @staticmethod
        def ValueOf(value: int) -> GeneralEquationOperationBuilder.BoundaryOptionsEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ThicknessMethodType(Enum):
        """
        Members Include: 
         |Absolute|  Absolute thickness 
         |Relative| 

        """
        Absolute: int
        Relative: int
        @staticmethod
        def ValueOf(value: int) -> GeneralEquationOperationBuilder.ThicknessMethodType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def BoundaryBody(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) BoundaryBody
         Returns the Boundary Body   
            
         
        """
        pass
    @property
    def BoundaryOption(self) -> GeneralEquationOperationBuilder.BoundaryOptionsEnum:
        """
        Getter for property: ( GeneralEquationOperationBuilder.BoundaryOptionsEnum NXOpen.) BoundaryOption
         Returns the Boundary Options   
            
         
        """
        pass
    @BoundaryOption.setter
    def BoundaryOption(self, boundaryOptions: GeneralEquationOperationBuilder.BoundaryOptionsEnum):
        """
        Setter for property: ( GeneralEquationOperationBuilder.BoundaryOptionsEnum NXOpen.) BoundaryOption
         Returns the Boundary Options   
            
         
        """
        pass
    @property
    def LocationAndOrientation(self) -> NXOpen.CoordinateSystem:
        """
        Getter for property: ( NXOpen.CoordinateSystem) LocationAndOrientation
         Returns the Location and Orientation
                locate the origin and orient the CSYS for the equation.  
          
                  
         
        """
        pass
    @LocationAndOrientation.setter
    def LocationAndOrientation(self, locationAndOrientation: NXOpen.CoordinateSystem):
        """
        Setter for property: ( NXOpen.CoordinateSystem) LocationAndOrientation
         Returns the Location and Orientation
                locate the origin and orient the CSYS for the equation.  
          
                  
         
        """
        pass
    @property
    def SizeX(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) SizeX
         Returns the Size in X direction 
                Range will be centered around the origin.  
          
                  
         
        """
        pass
    @property
    def SizeY(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) SizeY
         Returns the Size in Y direction
                Range will be centered around the origin.  
          
                  
         
        """
        pass
    @property
    def SizeZ(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) SizeZ
         Returns the Size in Z direction
                Range will be centered around the origin.  
          
                  
         
        """
        pass
    @property
    def Thickness(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Thickness
         Returns the thickness
                Thickness to be used for equation surface.  
          
                  
         
        """
        pass
    @property
    def ThicknessFactor(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ThicknessFactor
         Returns the thickness factor.  
          
                The factor for the relative thickness method.
                  
         
        """
        pass
    @property
    def ThicknessMethod(self) -> GeneralEquationOperationBuilder.ThicknessMethodType:
        """
        Getter for property: ( GeneralEquationOperationBuilder.ThicknessMethodType NXOpen.) ThicknessMethod
         Returns the thickness method
                Methods of adding thickness to structure created by general equation : Absolute, Relative
                  
            
         
        """
        pass
    @ThicknessMethod.setter
    def ThicknessMethod(self, thicknessMethod: GeneralEquationOperationBuilder.ThicknessMethodType):
        """
        Setter for property: ( GeneralEquationOperationBuilder.ThicknessMethodType NXOpen.) ThicknessMethod
         Returns the thickness method
                Methods of adding thickness to structure created by general equation : Absolute, Relative
                  
            
         
        """
        pass
    @property
    def UniformRange(self) -> bool:
        """
        Getter for property: (bool) UniformRange
         Returns the Uniform Flag
                Uniform boundary range inside which the implicit surface for given equation will be created.  
          
                Range will be centered around the origin.
                  
         
        """
        pass
    @UniformRange.setter
    def UniformRange(self, uniform: bool):
        """
        Setter for property: (bool) UniformRange
         Returns the Uniform Flag
                Uniform boundary range inside which the implicit surface for given equation will be created.  
          
                Range will be centered around the origin.
                  
         
        """
        pass
    @property
    def UniformSize(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) UniformSize
         Returns the Uniform Size
                Uniform range in X, Y and Z directions.  
          
                Range will be centered around the origin.
                  
         
        """
        pass
    @property
    def UserExpression(self) -> NXOpen.ModlUtils.EquationEditorBuilder:
        """
        Getter for property: ( NXOpen.ModlUtils.EquationEditorBuilder) UserExpression
         Returns the user expression from whch implicit surface will be created  
            
         
        """
        pass
class GeneralEquationOperation(ImplicitOperation): 
    """ Represents a Implicit General Equation Operation. """
    pass
class Gyroid(EquationOperation): 
    """ Represents a Gyroid Implicit Operation. """
    pass
import NXOpen
class ImplicitModelingPreferencesBuilder(NXOpen.Builder): 
    """ Represents an implicit feature. Output of this feature is convergent body. """
    @property
    def ChordalTolerance(self) -> float:
        """
        Getter for property: (float) ChordalTolerance
         Returns the maximum chordal deviation between the original mesh and the output mesh.  
             
         
        """
        pass
    @ChordalTolerance.setter
    def ChordalTolerance(self, chordalTolerance: float):
        """
        Setter for property: (float) ChordalTolerance
         Returns the maximum chordal deviation between the original mesh and the output mesh.  
             
         
        """
        pass
    @property
    def MaxFacetSize(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MaxFacetSize
         Returns the maximum facet size in areas of low face curvature.  
             
         
        """
        pass
    @property
    def RemeshFlag(self) -> bool:
        """
        Getter for property: (bool) RemeshFlag
         Returns the flag to remesh the implict body.  
             
         
        """
        pass
    @RemeshFlag.setter
    def RemeshFlag(self, remeshFlag: bool):
        """
        Setter for property: (bool) RemeshFlag
         Returns the flag to remesh the implict body.  
             
         
        """
        pass
    @property
    def VoxelSize(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) VoxelSize
         Returns the voxel size for implicit feature.  
             
         
        """
        pass
import NXOpen
class ImplicitOperationCollection(NXOpen.TaggedObjectCollection): 
    """
         Represents the collection of NXOpen.Implicit.ImplicitOperation object.
    """
    def CreateBlockBuilder(self, implicitOperation: Block) -> BlockBuilder:
        """
         Creates an object of NXOpen.Implicit.BlockBuilder 
         Returns blockBuilder ( BlockBuilder NXOpen.):  the implicit block builder .
        """
        pass
    def CreateBlockBuilder1(self, implicitOperation: Block) -> BlockBuilder:
        """
         Creates an object of NXOpen.Implicit.BlockBuilder 
         Returns blockBuilder ( BlockBuilder NXOpen.):  the implicit block builder .
        """
        pass
    def CreateCapChannelBuilder(self, implicitOperation: CapChannel) -> CapChannelBuilder:
        """
         Creates an object of NXOpen.Implicit.CapChannelBuilder 
         Returns capChannelBuilder ( CapChannelBuilder NXOpen.):  the cap channel based implicit operation builder .
        """
        pass
    def CreateCartesianPatternBuilder(self, implicitOperation: CartesianPattern) -> CartesianPatternBuilder:
        """
         Creates an object of NXOpen.Implicit.CartesianPatternBuilder 
         Returns cartesianPatternBuilder ( CartesianPatternBuilder NXOpen.):  the cartesian pattern based implicit operation builder .
        """
        pass
    def CreateCartesianPatternBuilder1(self, implicitOperation: CartesianPattern) -> CartesianPatternBuilder:
        """
         Creates an object of NXOpen.Implicit.CartesianPatternBuilder 
         Returns cartesianPatternBuilder ( CartesianPatternBuilder NXOpen.):  the cartesian pattern based implicit operation builder .
        """
        pass
    def CreateChannelPlotBuilder(self, implicitFeature: Feature) -> ChannelPlotBuilder:
        """
         Creates an object of NXOpen.Implicit.ChannelPlotBuilder 
         Returns channelPlotBuilder ( ChannelPlotBuilder NXOpen.):  the channel plot based implicit operation builder .
        """
        pass
    def CreateConeBuilder(self, implicitOperation: Cone) -> ConeBuilder:
        """
         Creates an object of NXOpen.Implicit.ConeBuilder 
         Returns coneBuilder ( ConeBuilder NXOpen.):  the implicit cone builder .
        """
        pass
    def CreateConeBuilder1(self, implicitOperation: Cone) -> ConeBuilder:
        """
         Creates an object of NXOpen.Implicit.ConeBuilder 
         Returns coneBuilder ( ConeBuilder NXOpen.):  the implicit cone builder .
        """
        pass
    def CreateCylinderBuilder(self, implicitOperation: Cylinder) -> CylinderBuilder:
        """
         Creates an object of NXOpen.Implicit.CylinderBuilder 
         Returns cylinderBuilder ( CylinderBuilder NXOpen.):  the implicit cylinder builder .
        """
        pass
    def CreateCylinderBuilder1(self, implicitOperation: Cylinder) -> CylinderBuilder:
        """
         Creates an object of NXOpen.Implicit.CylinderBuilder 
         Returns cylinderBuilder ( CylinderBuilder NXOpen.):  the implicit cylinder builder .
        """
        pass
    def CreateCylindricalPatternBuilder(self, implicitOperation: CylindricalPattern) -> CylindricalPatternBuilder:
        """
         Creates an object of NXOpen.Implicit.CylindricalPatternBuilder 
         Returns cylindricalPatternBuilder ( CylindricalPatternBuilder NXOpen.):  the cylindrical pattern based implicit operation builder .
        """
        pass
    def CreateCylindricalPatternBuilder1(self, implicitOperation: CylindricalPattern) -> CylindricalPatternBuilder:
        """
         Creates an object of NXOpen.Implicit.CylindricalPatternBuilder 
         Returns cylindricalPatternBuilder ( CylindricalPatternBuilder NXOpen.):  the cylindrical pattern based implicit operation builder .
        """
        pass
    def CreateEllipsoidBuilder(self, implicitOperation: Ellipsoid) -> EllipsoidBuilder:
        """
         Creates an object of NXOpen.Implicit.EllipsoidBuilder 
         Returns ellipsoidBuilder ( EllipsoidBuilder NXOpen.):  the implicit ellipsoid builder .
        """
        pass
    def CreateEllipsoidBuilder1(self, implicitOperation: Ellipsoid) -> EllipsoidBuilder:
        """
         Creates an object of NXOpen.Implicit.EllipsoidBuilder 
         Returns ellipsoidBuilder ( EllipsoidBuilder NXOpen.):  the implicit ellipsoid builder .
        """
        pass
    def CreateEquationOperationBuilder(self, implicitOperation: EquationOperation) -> EquationOperationBuilder:
        """
         Creates an object of NXOpen.Implicit.EquationOperationBuilder 
         Returns equationOperationBuilder ( EquationOperationBuilder NXOpen.):  the equation based implicit operation builder .
        """
        pass
    def CreateEquationOperationBuilder1(self, implicitOperation: EquationOperation) -> EquationOperationBuilder:
        """
         Creates an object of NXOpen.Implicit.EquationOperationBuilder 
         Returns equationOperationBuilder ( EquationOperationBuilder NXOpen.):  the equation based implicit operation builder .
        """
        pass
    def CreateGeneralEquationOperationBuilder(self, implicitOperation: GeneralEquationOperation) -> GeneralEquationOperationBuilder:
        """
         Creates an object of NXOpen.Implicit.GeneralEquationOperationBuilder 
         Returns generalEquationOperationBuilder ( GeneralEquationOperationBuilder NXOpen.):  the general equation based implicit operation builder .
        """
        pass
    def CreateGeneralEquationOperationBuilder1(self, implicitOperation: GeneralEquationOperation) -> GeneralEquationOperationBuilder:
        """
         Creates an object of NXOpen.Implicit.GeneralEquationOperationBuilder 
         Returns generalEquationOperationBuilder ( GeneralEquationOperationBuilder NXOpen.):  the general equation based implicit operation builder .
        """
        pass
    def CreateImplicitModelingPreferencesBuilder(self, implicitFeature: Feature) -> ImplicitModelingPreferencesBuilder:
        """
         Creates an object of NXOpen.Implicit.ImplicitModelingPreferencesBuilder 
         Returns implicitModelPreferencesBuilder ( ImplicitModelingPreferencesBuilder NXOpen.):  the implicit model preference builder .
        """
        pass
    def CreateImportSoildBodyBuilder(self, implicitOperation: ImportSolidBody) -> ImportSolidBodyBuilder:
        """
         Creates an object of NXOpen.Implicit.ImportSolidBodyBuilder 
         Returns importSolidBodyBuilder ( ImportSolidBodyBuilder NXOpen.):  the import solid body implicit operation builder .
        """
        pass
    def CreateImportSolidBodyBuilder1(self, implicitOperation: ImportSolidBody) -> ImportSolidBodyBuilder:
        """
         Creates an object of NXOpen.Implicit.ImportSolidBodyBuilder 
         Returns importSolidBodyBuilder ( ImportSolidBodyBuilder NXOpen.):  the import solid body implicit operation builder .
        """
        pass
    def CreateIntersectBuilder(self, implicitOperation: Intersect) -> IntersectBuilder:
        """
         Creates an object of NXOpen.Implicit.IntersectBuilder 
         Returns intersectBuilder ( IntersectBuilder NXOpen.):  the implicit intersect builder .
        """
        pass
    def CreateIntersectBuilder1(self, implicitOperation: Intersect) -> IntersectBuilder:
        """
         Creates an object of NXOpen.Implicit.IntersectBuilder 
         Returns intersectBuilder ( IntersectBuilder NXOpen.):  the implicit intersect builder .
        """
        pass
    def CreateSetResolutionBuilder(self, implicitFeature: Feature) -> SetResolutionBuilder:
        """
         Creates an object of NXOpen.Implicit.SetResolutionBuilder 
         Returns setResoltionBuilder ( SetResolutionBuilder NXOpen.):  the set resolution based implicit operation builder .
        """
        pass
    def CreateShellBuilder(self, implicitOperation: Shell) -> ShellBuilder:
        """
         Creates an object of NXOpen.Implicit.ShellBuilder 
         Returns offsetBuilder ( ShellBuilder NXOpen.):  the implicit shell builder .
        """
        pass
    def CreateShellBuilder1(self, implicitOperation: Shell) -> ShellBuilder:
        """
         Creates an object of NXOpen.Implicit.ShellBuilder 
         Returns offsetBuilder ( ShellBuilder NXOpen.):  the implicit shell builder .
        """
        pass
    def CreateSphereBuilder(self, implicitOperation: Sphere) -> SphereBuilder:
        """
         Creates an object of NXOpen.Implicit.SphereBuilder 
         Returns sphereBuilder ( SphereBuilder NXOpen.):  the implicit sphere builder .
        """
        pass
    def CreateSphereBuilder1(self, implicitOperation: Sphere) -> SphereBuilder:
        """
         Creates an object of NXOpen.Implicit.SphereBuilder 
         Returns sphereBuilder ( SphereBuilder NXOpen.):  the implicit sphere builder .
        """
        pass
    def CreateSubtractBuilder(self, implicitOperation: Subtract) -> SubtractBuilder:
        """
         Creates an object of NXOpen.Implicit.SubtractBuilder 
         Returns subtractBuilder ( SubtractBuilder NXOpen.):  the implicit subtract builder .
        """
        pass
    def CreateSubtractBuilder1(self, implicitOperation: Subtract) -> SubtractBuilder:
        """
         Creates an object of NXOpen.Implicit.SubtractBuilder 
         Returns subtractBuilder ( SubtractBuilder NXOpen.):  the implicit subtract builder .
        """
        pass
    def CreateThickenBuilder(self, implicitOperation: Thicken) -> ThickenBuilder:
        """
         Creates an object of NXOpen.Implicit.ThickenBuilder 
         Returns thickenBuilder ( ThickenBuilder NXOpen.):  the implicit thicken builder .
        """
        pass
    def CreateThickenBuilder1(self, implicitOperation: Thicken) -> ThickenBuilder:
        """
         Creates an object of NXOpen.Implicit.ThickenBuilder 
         Returns thickenBuilder ( ThickenBuilder NXOpen.):  the implicit thicken builder .
        """
        pass
    def CreateTorusBuilder(self, implicitOperation: Torus) -> TorusBuilder:
        """
         Creates an object of NXOpen.Implicit.TorusBuilder 
         Returns torusBuilder ( TorusBuilder NXOpen.):  the implicit torus builder .
        """
        pass
    def CreateTorusBuilder1(self, implicitOperation: Torus) -> TorusBuilder:
        """
         Creates an object of NXOpen.Implicit.TorusBuilder 
         Returns torusBuilder ( TorusBuilder NXOpen.):  the implicit torus builder .
        """
        pass
    def CreateUniteBuilder(self, implicitOperation: Unite) -> UniteBuilder:
        """
         Creates an object of NXOpen.Implicit.UniteBuilder 
         Returns uniteBuilder ( UniteBuilder NXOpen.):  the implicit unite builder .
        """
        pass
    def CreateUniteBuilder1(self, implicitOperation: Unite) -> UniteBuilder:
        """
         Creates an object of NXOpen.Implicit.UniteBuilder 
         Returns uniteBuilder ( UniteBuilder NXOpen.):  the implicit unite builder .
        """
        pass
import NXOpen
class ImplicitOperation(NXOpen.NXObject): 
    """
        Represents the base class for an NX Implicit Operation.
    """
    @property
    def Timestamp(self) -> int:
        """
        Getter for property: (int) Timestamp
         Returns the timestamp of the feature   
            
         
        """
        pass
    def GetExpressions(self) -> List[NXOpen.Expression]:
        """
         Returns the expressions created by the implicit operation. The order in which expressions are returned is not significant and may change 
         Returns expressions ( NXOpen.Expression Li):  the expressions created by implicit operation.
        """
        pass
    def GetParents(self) -> List[ImplicitOperation]:
        """
         Returns the immediate parent of implicit operations. The order in which parents are returned is not significant and may change 
         Returns parent_implicit_operations ( ImplicitOperation List[NXOpe):  the parents of implicit operation.
        """
        pass
import NXOpen
class ImportSolidBodyBuilder(OperationBuilder): 
    """ Represents an import solid body Implicit.ImportSolidBody builder """
    @property
    def BodiesOrFacesToImport(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) BodiesOrFacesToImport
         Returns the solid bodies or faces to import from outside the task environment  
            
         
        """
        pass
    @property
    def BodiesToImport(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) BodiesToImport
         Returns the solid bodies to import from outside the task environment  
            
         
        """
        pass
    @property
    def HideInputBody(self) -> bool:
        """
        Getter for property: (bool) HideInputBody
         Returns the hide input body option   
            
         
        """
        pass
    @HideInputBody.setter
    def HideInputBody(self, hideInputBody: bool):
        """
        Setter for property: (bool) HideInputBody
         Returns the hide input body option   
            
         
        """
        pass
class ImportSolidBody(ImplicitOperation): 
    """ Represents a Import Body Implicit Operation. """
    pass
class IntersectBuilder(BooleanBuilder): 
    """
    Represents an Implicit.IntersectBuilder.
    It will create an intersect operation on the selected bodies.
    """
    pass
class Intersect(Boolean): 
    """ Represents an Intersect Implicit Operation. """
    pass
class Lidinoid(EquationOperation): 
    """ Represents a Lidinoid Implicit Operation. """
    pass
class Neovius(EquationOperation): 
    """ Represents a Neovius Implicit Operation. """
    pass
import NXOpen
class OffsetBuilder(OperationBuilder): 
    """
    Represents a Implicit.OffsetBuilder.
    It will Offset the selected body inside Implicit Task Environment.
    """
    @property
    def BodyToOffset(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) BodyToOffset
         Returns the body to offset   
            
         
        """
        pass
    @property
    def DefaultThicknessDirectionReversed(self) -> bool:
        """
        Getter for property: (bool) DefaultThicknessDirectionReversed
         Returns the default thickness directions is reversed   
            
         
        """
        pass
    @DefaultThicknessDirectionReversed.setter
    def DefaultThicknessDirectionReversed(self, reverseDirection: bool):
        """
        Setter for property: (bool) DefaultThicknessDirectionReversed
         Returns the default thickness directions is reversed   
            
         
        """
        pass
    @property
    def Thickness(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Thickness
         Returns the thickness - offset distance  
            
         
        """
        pass
class Offset(ImplicitOperation): 
    """ Represents a Offset Implicit Operation. """
    pass
import NXOpen
class OperationBuilder(NXOpen.Builder): 
    """
    Represents a Implicit.OperationBuilder. This is an abstract class.
    This is the base class of all Implicit operations builder classes.
    """
    @property
    def DisplayVoxel(self) -> bool:
        """
        Getter for property: (bool) DisplayVoxel
         Returns the voxel display toggle.  
          
                This toggle is used only for graphics display of voxel visualization scale
                and has no impact on operation output.
                  
         
        """
        pass
    @DisplayVoxel.setter
    def DisplayVoxel(self, displayVoxelFlag: bool):
        """
        Setter for property: (bool) DisplayVoxel
         Returns the voxel display toggle.  
          
                This toggle is used only for graphics display of voxel visualization scale
                and has no impact on operation output.
                  
         
        """
        pass
    @property
    def Smoothness(self) -> float:
        """
        Getter for property: (float) Smoothness
         Returns the smoothness.  
          
                This value is used to specifies the level of smoothness of the output geometry.
                  
         
        """
        pass
    @Smoothness.setter
    def Smoothness(self, smoothness: float):
        """
        Setter for property: (float) Smoothness
         Returns the smoothness.  
          
                This value is used to specifies the level of smoothness of the output geometry.
                  
         
        """
        pass
    @property
    def UpdateDefaultVoxelSizeBasedOnFirstOperation(self) -> bool:
        """
        Getter for property: (bool) UpdateDefaultVoxelSizeBasedOnFirstOperation
         Returns the flag to update default voxel size based on the size of first operation
                  
                This API is now deprecated.  
          
                Please use  NXOpen::Implicit::OperationBuilder::VoxelSizePercent  instead.
                  
                  
         
        """
        pass
    @UpdateDefaultVoxelSizeBasedOnFirstOperation.setter
    def UpdateDefaultVoxelSizeBasedOnFirstOperation(self, updateVoxelSize: bool):
        """
        Setter for property: (bool) UpdateDefaultVoxelSizeBasedOnFirstOperation
         Returns the flag to update default voxel size based on the size of first operation
                  
                This API is now deprecated.  
          
                Please use  NXOpen::Implicit::OperationBuilder::VoxelSizePercent  instead.
                  
                  
         
        """
        pass
    @property
    def VoxelSizeAbsolute(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) VoxelSizeAbsolute
         Returns the absolute size of voxels  
            
         
        """
        pass
    @property
    def VoxelSizePercent(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) VoxelSizePercent
         Returns the size of voxels in percentage of body size   
            
         
        """
        pass
class Scherk(EquationOperation): 
    """ Represents a Scherk Implicit Operation. """
    pass
class Schoen(EquationOperation): 
    """ Represents a Schoen Implicit Operation. """
    pass
class Schwarz(EquationOperation): 
    """ Represents a Schwarz Implicit Operation. """
    pass
import NXOpen
class SetResolutionBuilder(NXOpen.Builder): 
    """ Represents command to set the voxel size for selected bodies """
    @property
    def ImplicitBodies(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) ImplicitBodies
         Returns the body to set resolution   
            
         
        """
        pass
    @property
    def VoxelSize(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) VoxelSize
         Returns the voxel size for implicit feature.  
             
         
        """
        pass
import NXOpen
class ShellBuilder(OperationBuilder): 
    """
    Represents a Implicit.ShellBuilder.
    It will shell the selected body inside Implicit Task Environment.
    """
    class Type(Enum):
        """
        Members Include: 
         |Closed|  Creates a closed Shell 
         |Open|  Creates an open Shell

        """
        Closed: int
        Open: int
        @staticmethod
        def ValueOf(value: int) -> ShellBuilder.Type:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AlternateThicknessList(self) -> NXOpen.ExpressionCollectorSetList:
        """
        Getter for property: ( NXOpen.ExpressionCollectorSetList) AlternateThicknessList
         Returns the alternate thickness list, in order to give different thickness for different faces.  
             
         
        """
        pass
    @property
    def BodyToOffset(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) BodyToOffset
         Returns the body to shell   
            
         
        """
        pass
    @property
    def DefaultThicknessDirectionReversed(self) -> bool:
        """
        Getter for property: (bool) DefaultThicknessDirectionReversed
         Returns the default thickness directions is reversed   
            
         
        """
        pass
    @DefaultThicknessDirectionReversed.setter
    def DefaultThicknessDirectionReversed(self, reverseDirection: bool):
        """
        Setter for property: (bool) DefaultThicknessDirectionReversed
         Returns the default thickness directions is reversed   
            
         
        """
        pass
    @property
    def FacesToOpen(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) FacesToOpen
         Returns the faces for open region of shell   
            
         
        """
        pass
    @property
    def Thickness(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Thickness
         Returns the thickness - offset distance  
            
         
        """
        pass
    @property
    def TypeOfShell(self) -> ShellBuilder.Type:
        """
        Getter for property: ( ShellBuilder.Type NXOpen.) TypeOfShell
         Returns the shell type, which is open or closed.  
             
         
        """
        pass
    @TypeOfShell.setter
    def TypeOfShell(self, shellType: ShellBuilder.Type):
        """
        Setter for property: ( ShellBuilder.Type NXOpen.) TypeOfShell
         Returns the shell type, which is open or closed.  
             
         
        """
        pass
class Shell(ImplicitOperation): 
    """ Represents a Shell Implicit Operation. """
    pass
import NXOpen
class SphereBuilder(OperationBuilder): 
    """ 
    Represents a Implicit.SphereBuilder.
    It will create a sphere inside the Implicit task environment.
    """
    @property
    def AssociativeOrigin(self) -> bool:
        """
        Getter for property: (bool) AssociativeOrigin
         Returns the option to keep the sphere associative with the specified Origin  
            
         
        """
        pass
    @AssociativeOrigin.setter
    def AssociativeOrigin(self, associativeOrigin: bool):
        """
        Setter for property: (bool) AssociativeOrigin
         Returns the option to keep the sphere associative with the specified Origin  
            
         
        """
        pass
    @property
    def CenterPoint(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) CenterPoint
         Returns the center Point   
            
         
        """
        pass
    @CenterPoint.setter
    def CenterPoint(self, centerPoint: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) CenterPoint
         Returns the center Point   
            
         
        """
        pass
    @property
    def Diameter(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Diameter
         Returns the diameter   
            
         
        """
        pass
class Sphere(ImplicitOperation): 
    """ Represents a Sphere Implicit Operation. """
    pass
class SplitP(EquationOperation): 
    """ Represents a Split P Implicit Operation. """
    pass
class SubtractBuilder(BooleanBuilder): 
    """
    Represents an Implicit.SubtractBuilder.
    It will create a subtract operation on the selected bodies.
    """
    pass
class Subtract(Boolean): 
    """ Represents a Subtract Implicit Operation. """
    pass
import NXOpen
class ThickenBuilder(OperationBuilder): 
    """
    Represents a Implicit.ThickenBuilder.
    It will Thicken the selected body inside Implicit Task Environment.
    """
    class ThicknessMethodType(Enum):
        """
        Members Include: 
         |Constant|  Constant thickness 
         |Variable|  Variable Thickness 

        """
        Constant: int
        Variable: int
        @staticmethod
        def ValueOf(value: int) -> ThickenBuilder.ThicknessMethodType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def FacesToThicken(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) FacesToThicken
         Returns the faces to thicken   
            
         
        """
        pass
    @property
    def Thickness(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Thickness
         Returns the thickness - Symmetric offset distance  
            
         
        """
        pass
    @property
    def ThicknessMethod(self) -> ThickenBuilder.ThicknessMethodType:
        """
        Getter for property: ( ThickenBuilder.ThicknessMethodType NXOpen.) ThicknessMethod
         Returns the thickness method
                Methods of adding thickness : Constant and Variable
                  
            
         
        """
        pass
    @ThicknessMethod.setter
    def ThicknessMethod(self, thicknessMethod: ThickenBuilder.ThicknessMethodType):
        """
        Setter for property: ( ThickenBuilder.ThicknessMethodType NXOpen.) ThicknessMethod
         Returns the thickness method
                Methods of adding thickness : Constant and Variable
                  
            
         
        """
        pass
class Thicken(ImplicitOperation): 
    """ Represents a Thicken Implicit Operation. """
    pass
import NXOpen
class TorusBuilder(OperationBuilder): 
    """ 
    Represents a Implicit.TorusBuilder.
    It will create a torus inside the Implicit task environment.
    """
    @property
    def Associative(self) -> bool:
        """
        Getter for property: (bool) Associative
         Returns the option to keep the Torus associative with the specified Center Point and Orientation.  
          
                    this does not apply to selection methods Dynamic, Inferred, Absolute CSYS, and CSYS of Current View.
                  
         
        """
        pass
    @Associative.setter
    def Associative(self, associativeCenterPoint: bool):
        """
        Setter for property: (bool) Associative
         Returns the option to keep the Torus associative with the specified Center Point and Orientation.  
          
                    this does not apply to selection methods Dynamic, Inferred, Absolute CSYS, and CSYS of Current View.
                  
         
        """
        pass
    @property
    def CenterAndOrientation(self) -> NXOpen.CartesianCoordinateSystem:
        """
        Getter for property: ( NXOpen.CartesianCoordinateSystem) CenterAndOrientation
         Returns the centerPoint Point   
            
         
        """
        pass
    @CenterAndOrientation.setter
    def CenterAndOrientation(self, csys: NXOpen.CartesianCoordinateSystem):
        """
        Setter for property: ( NXOpen.CartesianCoordinateSystem) CenterAndOrientation
         Returns the centerPoint Point   
            
         
        """
        pass
    @property
    def InnerDimension(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) InnerDimension
         Returns the inner dimension   
            
         
        """
        pass
    @property
    def OuterDimension(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) OuterDimension
         Returns the outer dimension   
            
         
        """
        pass
class Torus(ImplicitOperation): 
    """ Represents a Torus Implicit Operation. """
    pass
class UnitCell(EquationOperation): 
    """ Represents a UnitCell Implicit Operation. """
    pass
class UniteBuilder(BooleanBuilder): 
    """
    Represents an Implicit.UniteBuilder.
    It will create an unite operation on the selected bodies.
    """
    pass
class Unite(Boolean): 
    """ Represents a Unite Implicit Operation. """
    pass
