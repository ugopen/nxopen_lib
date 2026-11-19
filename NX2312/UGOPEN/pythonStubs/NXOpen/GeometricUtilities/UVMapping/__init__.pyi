from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
##  Make UV parameterization symmetric.  <br> To create a new instance of this class, use @link NXOpen::GeometricUtilities::UVMapping::UVMappingCollection::CreateMakeSymmetricParameterizationData  NXOpen::GeometricUtilities::UVMapping::UVMappingCollection::CreateMakeSymmetricParameterizationData @endlink  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class MakeSymmetricParameterizationData(NXOpen.Builder): 
    """ Make UV parameterization symmetric. """


    ##  Options to make parameterization symmetric about. 
    ##  Symmetric about U 
    class Types(Enum):
        """
        Members Include: <SymmetryInU> <SymmetryInV>
        """
        SymmetryInU: int
        SymmetryInV: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> MakeSymmetricParameterizationData.Types:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) Point
    ##   the point of symmetry.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.Point
    @property
    def Point(self) -> NXOpen.Point:
        """
        Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) Point
          the point of symmetry.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) Point

    ##   the point of symmetry.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @Point.setter
    def Point(self, point0: NXOpen.Point):
        """
        Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) Point
          the point of symmetry.  
             
         
        """
        pass
    
    ## Getter for property: (bool) ReverseDirection
    ##   the reverse direction   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return bool
    @property
    def ReverseDirection(self) -> bool:
        """
        Getter for property: (bool) ReverseDirection
          the reverse direction   
            
         
        """
        pass
    
    ## Setter for property: (bool) ReverseDirection

    ##   the reverse direction   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @ReverseDirection.setter
    def ReverseDirection(self, reverseDirection: bool):
        """
        Setter for property: (bool) ReverseDirection
          the reverse direction   
            
         
        """
        pass
    
    ## Getter for property: (@link MakeSymmetricParameterizationData.Types NXOpen.GeometricUtilities.UVMapping.MakeSymmetricParameterizationData.Types@endlink) Type
    ##   the type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return MakeSymmetricParameterizationData.Types
    @property
    def Type(self) -> MakeSymmetricParameterizationData.Types:
        """
        Getter for property: (@link MakeSymmetricParameterizationData.Types NXOpen.GeometricUtilities.UVMapping.MakeSymmetricParameterizationData.Types@endlink) Type
          the type   
            
         
        """
        pass
    
    ## Setter for property: (@link MakeSymmetricParameterizationData.Types NXOpen.GeometricUtilities.UVMapping.MakeSymmetricParameterizationData.Types@endlink) Type

    ##   the type   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @Type.setter
    def Type(self, type: MakeSymmetricParameterizationData.Types):
        """
        Setter for property: (@link MakeSymmetricParameterizationData.Types NXOpen.GeometricUtilities.UVMapping.MakeSymmetricParameterizationData.Types@endlink) Type
          the type   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectNXObject NXOpen.SelectNXObject@endlink) UVPatches
    ##   the uv patches   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.SelectNXObject
    @property
    def UVPatches(self) -> NXOpen.SelectNXObject:
        """
        Getter for property: (@link NXOpen.SelectNXObject NXOpen.SelectNXObject@endlink) UVPatches
          the uv patches   
            
         
        """
        pass
    
import NXOpen
##  Reverse UV parameterization.  <br> To create a new instance of this class, use @link NXOpen::GeometricUtilities::UVMapping::UVMappingCollection::CreateReverseUVParameterizationData  NXOpen::GeometricUtilities::UVMapping::UVMappingCollection::CreateReverseUVParameterizationData @endlink  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class ReverseUVParameterizationData(NXOpen.Builder): 
    """ Reverse UV parameterization. """


    ## Getter for property: (bool) CanReverseU
    ##   the flag indicating if U direction to be reversed.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return bool
    @property
    def CanReverseU(self) -> bool:
        """
        Getter for property: (bool) CanReverseU
          the flag indicating if U direction to be reversed.  
             
         
        """
        pass
    
    ## Setter for property: (bool) CanReverseU

    ##   the flag indicating if U direction to be reversed.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @CanReverseU.setter
    def CanReverseU(self, reverse: bool):
        """
        Setter for property: (bool) CanReverseU
          the flag indicating if U direction to be reversed.  
             
         
        """
        pass
    
    ## Getter for property: (bool) CanReverseV
    ##   the flag indicating if V direction to be reversed.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return bool
    @property
    def CanReverseV(self) -> bool:
        """
        Getter for property: (bool) CanReverseV
          the flag indicating if V direction to be reversed.  
             
         
        """
        pass
    
    ## Setter for property: (bool) CanReverseV

    ##   the flag indicating if V direction to be reversed.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @CanReverseV.setter
    def CanReverseV(self, reverse: bool):
        """
        Setter for property: (bool) CanReverseV
          the flag indicating if V direction to be reversed.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) Patches
    ##   the object list.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.SelectDisplayableObjectList
    @property
    def Patches(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) Patches
          the object list.  
             
         
        """
        pass
    
import NXOpen
import NXOpen.GeometricUtilities
##  Represents UV mesh topology object selection. 
## 
##   <br>  Created in NX1847.0.0  <br> 

class SelectUVMeshObjectData(NXOpen.TaggedObject): 
    """ Represents UV mesh topology object selection. """


    ## Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) SelectionList
    ##   the object list.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.SelectDisplayableObjectList
    @property
    def SelectionList(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) SelectionList
          the object list.  
             
         
        """
        pass
    
    ##  Clears the currently present objects and adds new objects. 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ##  Objects to process. 
    def ClearAndAdd(builder: SelectUVMeshObjectData, objects: List[NXOpen.NXObject], view: NXOpen.View, point: NXOpen.Point3d) -> None:
        """
         Clears the currently present objects and adds new objects. 
        """
        pass
    
    ##  Sets the cursor location in absolute coordinates. 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ##  
    def SetCursorLocation(builder: SelectUVMeshObjectData, point: NXOpen.Point3d) -> None:
        """
         Sets the cursor location in absolute coordinates. 
        """
        pass
    
    ##  Sets the view direction. 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ##  
    def SetViewDirection(builder: SelectUVMeshObjectData, direction: NXOpen.Vector3d) -> None:
        """
         Sets the view direction. 
        """
        pass
    
import NXOpen
##  Transform UV parameterization by transforming patches in UV spaces.  <br> To create a new instance of this class, use @link NXOpen::GeometricUtilities::UVMapping::UVMappingCollection::CreateTransformUVParameterizationData  NXOpen::GeometricUtilities::UVMapping::UVMappingCollection::CreateTransformUVParameterizationData @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## CanRelocateToolToSelection </term> <description> 
##  
## true </description> </item> 
## 
## <item><term> 
##  
## CanReorientToolToSelection </term> <description> 
##  
## true </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX1847.0.0  <br> 

class TransformUVParameterizationData(NXOpen.Builder): 
    """ Transform UV parameterization by transforming patches in UV spaces. """


    ## Getter for property: (bool) CanMoveToolOnly
    ##   the flag indicating if only the transformation tool can be moved without affecting UV patches.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return bool
    @property
    def CanMoveToolOnly(self) -> bool:
        """
        Getter for property: (bool) CanMoveToolOnly
          the flag indicating if only the transformation tool can be moved without affecting UV patches.  
             
         
        """
        pass
    
    ## Setter for property: (bool) CanMoveToolOnly

    ##   the flag indicating if only the transformation tool can be moved without affecting UV patches.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @CanMoveToolOnly.setter
    def CanMoveToolOnly(self, canMoveToolOnly: bool):
        """
        Setter for property: (bool) CanMoveToolOnly
          the flag indicating if only the transformation tool can be moved without affecting UV patches.  
             
         
        """
        pass
    
    ## Getter for property: (bool) CanRelocateToolToSelection
    ##   the flat indicating if transformation tool can be relocated based on selected entities.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return bool
    @property
    def CanRelocateToolToSelection(self) -> bool:
        """
        Getter for property: (bool) CanRelocateToolToSelection
          the flat indicating if transformation tool can be relocated based on selected entities.  
             
         
        """
        pass
    
    ## Setter for property: (bool) CanRelocateToolToSelection

    ##   the flat indicating if transformation tool can be relocated based on selected entities.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @CanRelocateToolToSelection.setter
    def CanRelocateToolToSelection(self, canRelocateToolToSelection: bool):
        """
        Setter for property: (bool) CanRelocateToolToSelection
          the flat indicating if transformation tool can be relocated based on selected entities.  
             
         
        """
        pass
    
    ## Getter for property: (bool) CanReorientToolToSelection
    ##   the flat indicating if transformation tool can be reoriented based on selected entities.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return bool
    @property
    def CanReorientToolToSelection(self) -> bool:
        """
        Getter for property: (bool) CanReorientToolToSelection
          the flat indicating if transformation tool can be reoriented based on selected entities.  
             
         
        """
        pass
    
    ## Setter for property: (bool) CanReorientToolToSelection

    ##   the flat indicating if transformation tool can be reoriented based on selected entities.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @CanReorientToolToSelection.setter
    def CanReorientToolToSelection(self, canReorientToolToSelection: bool):
        """
        Setter for property: (bool) CanReorientToolToSelection
          the flat indicating if transformation tool can be reoriented based on selected entities.  
             
         
        """
        pass
    
    ## Getter for property: (bool) CanScaleUniformly
    ##   the flag indicating if UV patches can be scaled uniformly.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return bool
    @property
    def CanScaleUniformly(self) -> bool:
        """
        Getter for property: (bool) CanScaleUniformly
          the flag indicating if UV patches can be scaled uniformly.  
             
         
        """
        pass
    
    ## Setter for property: (bool) CanScaleUniformly

    ##   the flag indicating if UV patches can be scaled uniformly.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @CanScaleUniformly.setter
    def CanScaleUniformly(self, canScaleUniformly: bool):
        """
        Setter for property: (bool) CanScaleUniformly
          the flag indicating if UV patches can be scaled uniformly.  
             
         
        """
        pass
    
    ## Getter for property: (@link UVMeshManipulatorData NXOpen.GeometricUtilities.UVMapping.UVMeshManipulatorData@endlink) UVMeshManipulator
    ##   the UV mesh manipulation Tool.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return UVMeshManipulatorData
    @property
    def UVMeshManipulator(self) -> UVMeshManipulatorData:
        """
        Getter for property: (@link UVMeshManipulatorData NXOpen.GeometricUtilities.UVMapping.UVMeshManipulatorData@endlink) UVMeshManipulator
          the UV mesh manipulation Tool.  
             
         
        """
        pass
    
    ##  Updates the parameterization by applying the transformation. 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def Update(builder: TransformUVParameterizationData) -> None:
        """
         Updates the parameterization by applying the transformation. 
        """
        pass
    
import NXOpen
##  This class contains the methods for creating and manipulating a UVMapping object.  <br> To obtain an instance of this class, refer to @link NXOpen::Part  NXOpen::Part @endlink  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class UVMappingCollection(NXOpen.Object): 
    """ This class contains the methods for creating and manipulating a UVMapping object. """


    ##  Creates a @link NXOpen::GeometricUtilities::UVMapping::MakeSymmetricParameterizationData NXOpen::GeometricUtilities::UVMapping::MakeSymmetricParameterizationData@endlink  
    ##  @return builder (@link MakeSymmetricParameterizationData NXOpen.GeometricUtilities.UVMapping.MakeSymmetricParameterizationData@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    def CreateMakeSymmetricParameterizationData(part: UVMappingCollection) -> MakeSymmetricParameterizationData:
        """
         Creates a @link NXOpen::GeometricUtilities::UVMapping::MakeSymmetricParameterizationData NXOpen::GeometricUtilities::UVMapping::MakeSymmetricParameterizationData@endlink  
         @return builder (@link MakeSymmetricParameterizationData NXOpen.GeometricUtilities.UVMapping.MakeSymmetricParameterizationData@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::GeometricUtilities::UVMapping::ReverseUVParameterizationData NXOpen::GeometricUtilities::UVMapping::ReverseUVParameterizationData@endlink  
    ##  @return builder (@link ReverseUVParameterizationData NXOpen.GeometricUtilities.UVMapping.ReverseUVParameterizationData@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    def CreateReverseUVParameterizationData(part: UVMappingCollection) -> ReverseUVParameterizationData:
        """
         Creates a @link NXOpen::GeometricUtilities::UVMapping::ReverseUVParameterizationData NXOpen::GeometricUtilities::UVMapping::ReverseUVParameterizationData@endlink  
         @return builder (@link ReverseUVParameterizationData NXOpen.GeometricUtilities.UVMapping.ReverseUVParameterizationData@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::GeometricUtilities::UVMapping::TransformUVParameterizationData NXOpen::GeometricUtilities::UVMapping::TransformUVParameterizationData@endlink  
    ##  @return builder (@link TransformUVParameterizationData NXOpen.GeometricUtilities.UVMapping.TransformUVParameterizationData@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    def CreateTransformUVParameterizationData(part: UVMappingCollection) -> TransformUVParameterizationData:
        """
         Creates a @link NXOpen::GeometricUtilities::UVMapping::TransformUVParameterizationData NXOpen::GeometricUtilities::UVMapping::TransformUVParameterizationData@endlink  
         @return builder (@link TransformUVParameterizationData NXOpen.GeometricUtilities.UVMapping.TransformUVParameterizationData@endlink): .
        """
        pass
    
    ##  Creates a @link GeometricUtilities::UVMapping::UVParameterizationBuilder GeometricUtilities::UVMapping::UVParameterizationBuilder@endlink  
    ##  @return builder (@link UVParameterizationBuilder NXOpen.GeometricUtilities.UVMapping.UVParameterizationBuilder@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    def CreateUVParameterizationBuilder(part: UVMappingCollection) -> UVParameterizationBuilder:
        """
         Creates a @link GeometricUtilities::UVMapping::UVParameterizationBuilder GeometricUtilities::UVMapping::UVParameterizationBuilder@endlink  
         @return builder (@link UVParameterizationBuilder NXOpen.GeometricUtilities.UVMapping.UVParameterizationBuilder@endlink): .
        """
        pass
    
import NXOpen
import NXOpen.GeometricUtilities
##  UV Mesh manipulation tool.
##         
## 
##   <br>  Created in NX1847.0.0  <br> 

class UVMeshManipulatorData(SelectUVMeshObjectData): 
    """ UV Mesh manipulation tool.
        """


    ##  Contains object selection information. 
    class ObjectSelectionData:
        """
         Contains object selection information. 
        """
        ## Getter for property :(@link NXOpen.NXObject NXOpen.NXObject@endlink) SelectedObject
        ## The selected object.
        ## @return @link NXOpen.NXObject NXOpen.NXObject@endlink
        @property
        def SelectedObject(self) -> NXOpen.NXObject:
            """
            Getter for property SelectedObject
            The selected object.

            """
            pass
        
        ## Setter for property :(@link NXOpen.NXObject NXOpen.NXObject@endlink) SelectedObject
        @SelectedObject.setter
        def SelectedObject(self, value: NXOpen.NXObject):
            """
            Getter for property SelectedObject
            The selected object.
            Setter for property SelectedObject
            The selected object.

            """
            pass
        
        ## Getter for property :(@link NXOpen.Point3d NXOpen.Point3d@endlink) SelectionPosition
        ## The point at which object is selected, the point                                                         under the cursor when seen in view direction.
        ## @return @link NXOpen.Point3d NXOpen.Point3d@endlink
        @property
        def SelectionPosition(self) -> NXOpen.Point3d:
            """
            Getter for property SelectionPosition
            The point at which object is selected, the point                                                         under the cursor when seen in view direction.

            """
            pass
        
        ## Setter for property :(@link NXOpen.Point3d NXOpen.Point3d@endlink) SelectionPosition
        @SelectionPosition.setter
        def SelectionPosition(self, value: NXOpen.Point3d):
            """
            Getter for property SelectionPosition
            The point at which object is selected, the point                                                         under the cursor when seen in view direction.
            Setter for property SelectionPosition
            The point at which object is selected, the point                                                         under the cursor when seen in view direction.

            """
            pass
        
        ## Getter for property :(@link NXOpen.Vector3d NXOpen.Vector3d@endlink) ViewDirection
        ## The view direction.
        ## @return @link NXOpen.Vector3d NXOpen.Vector3d@endlink
        @property
        def ViewDirection(self) -> NXOpen.Vector3d:
            """
            Getter for property ViewDirection
            The view direction.

            """
            pass
        
        ## Setter for property :(@link NXOpen.Vector3d NXOpen.Vector3d@endlink) ViewDirection
        @ViewDirection.setter
        def ViewDirection(self, value: NXOpen.Vector3d):
            """
            Getter for property ViewDirection
            The view direction.
            Setter for property ViewDirection
            The view direction.

            """
            pass
        
        ## Getter for property :(bool) IsSnappedPosition
        ## Is SelectionPosition a snapped location.
        ## @return bool
        @property
        def IsSnappedPosition(self) -> bool:
            """
            Getter for property IsSnappedPosition
            Is SelectionPosition a snapped location.

            """
            pass
        
        ## Setter for property :(bool) IsSnappedPosition
        @IsSnappedPosition.setter
        def IsSnappedPosition(self, value: bool):
            """
            Getter for property IsSnappedPosition
            Is SelectionPosition a snapped location.
            Setter for property IsSnappedPosition
            Is SelectionPosition a snapped location.

            """
            pass
        
    
    
    ## Getter for property: (@link NXOpen.GeometricUtilities.TransformerData NXOpen.GeometricUtilities.TransformerData@endlink) Transformer
    ##   the transformation tool.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.GeometricUtilities.TransformerData
    @property
    def Transformer(self) -> NXOpen.GeometricUtilities.TransformerData:
        """
        Getter for property: (@link NXOpen.GeometricUtilities.TransformerData NXOpen.GeometricUtilities.TransformerData@endlink) Transformer
          the transformation tool.  
             
         
        """
        pass
    
    ##  Repositions the @link NXOpen::GeometricUtilities::TransformerData NXOpen::GeometricUtilities::TransformerData@endlink  to the specified entity. 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ##  
    def SetTransformerToObject(builder: UVMeshManipulatorData, selectionData: UVMeshManipulatorData.ObjectSelectionData) -> None:
        """
         Repositions the @link NXOpen::GeometricUtilities::TransformerData NXOpen::GeometricUtilities::TransformerData@endlink  to the specified entity. 
        """
        pass
    
    ##  Aligns the U axis to U or V direction. 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ##  
    def SetUAxisDirection(builder: UVMeshManipulatorData, canAlignToUDirection: bool) -> None:
        """
         Aligns the U axis to U or V direction. 
        """
        pass
    
    ##  Aligns the V axis to U or V direction. 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ##  
    def SetVAxisDirection(builder: UVMeshManipulatorData, canAlignToVDirection: bool) -> None:
        """
         Aligns the V axis to U or V direction. 
        """
        pass
    
import NXOpen
##  Represents a UVParameterization builder  <br> To create a new instance of this class, use @link NXOpen::GeometricUtilities::UVMapping::UVMappingCollection::CreateUVParameterizationBuilder  NXOpen::GeometricUtilities::UVMapping::UVMappingCollection::CreateUVParameterizationBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## TessellationResolution </term> <description> 
##  
## Standard </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX1847.0.0  <br> 

class UVParameterizationBuilder(NXOpen.Builder): 
    """ Represents a UVParameterization builder """


    ##  the perserving type 
    ##  Preserves shape. Deprecated in NX1899. Use @link  NXOpen::GeometricUtilities::UVMapping::UVParameterizationBuilder::ParameterizationTypesLengthPreserving   NXOpen::GeometricUtilities::UVMapping::UVParameterizationBuilder::ParameterizationTypesLengthPreserving @endlink  instead. 
    class ParameterizationTypes(Enum):
        """
        Members Include: <ShapePreserving> <LengthPreserving>
        """
        ShapePreserving: int
        LengthPreserving: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> UVParameterizationBuilder.ParameterizationTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  the tessellation resolution 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Coarse</term><description> 
    ## </description> </item><item><term> 
    ## Standard</term><description> 
    ## </description> </item><item><term> 
    ## Fine</term><description> 
    ## </description> </item><item><term> 
    ## ExtraFine</term><description> 
    ## </description> </item></list>
    class TessellationResolutions(Enum):
        """
        Members Include: <Coarse> <Standard> <Fine> <ExtraFine>
        """
        Coarse: int
        Standard: int
        Fine: int
        ExtraFine: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> UVParameterizationBuilder.TessellationResolutions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) Faces
    ##   the faces   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.ScCollector
    @property
    def Faces(self) -> NXOpen.ScCollector:
        """
        Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) Faces
          the faces   
            
         
        """
        pass
    
    ## Getter for property: (int) NumberOfGridLines
    ##   the number of grid lines   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return int
    @property
    def NumberOfGridLines(self) -> int:
        """
        Getter for property: (int) NumberOfGridLines
          the number of grid lines   
            
         
        """
        pass
    
    ## Setter for property: (int) NumberOfGridLines

    ##   the number of grid lines   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @NumberOfGridLines.setter
    def NumberOfGridLines(self, numGridLines: int):
        """
        Setter for property: (int) NumberOfGridLines
          the number of grid lines   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectEdge NXOpen.SelectEdge@endlink) OuterBoundarySeedEdge
    ##   the seed edge   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.SelectEdge
    @property
    def OuterBoundarySeedEdge(self) -> NXOpen.SelectEdge:
        """
        Getter for property: (@link NXOpen.SelectEdge NXOpen.SelectEdge@endlink) OuterBoundarySeedEdge
          the seed edge   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Section NXOpen.Section@endlink) RipEdges
    ##   the rip edges   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.Section
    @property
    def RipEdges(self) -> NXOpen.Section:
        """
        Getter for property: (@link NXOpen.Section NXOpen.Section@endlink) RipEdges
          the rip edges   
            
         
        """
        pass
    
    ## Getter for property: (@link UVParameterizationBuilder.TessellationResolutions NXOpen.GeometricUtilities.UVMapping.UVParameterizationBuilder.TessellationResolutions@endlink) TessellationResolution
    ##   the tessellation resolution   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return UVParameterizationBuilder.TessellationResolutions
    @property
    def TessellationResolution(self) -> UVParameterizationBuilder.TessellationResolutions:
        """
        Getter for property: (@link UVParameterizationBuilder.TessellationResolutions NXOpen.GeometricUtilities.UVMapping.UVParameterizationBuilder.TessellationResolutions@endlink) TessellationResolution
          the tessellation resolution   
            
         
        """
        pass
    
    ## Setter for property: (@link UVParameterizationBuilder.TessellationResolutions NXOpen.GeometricUtilities.UVMapping.UVParameterizationBuilder.TessellationResolutions@endlink) TessellationResolution

    ##   the tessellation resolution   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @TessellationResolution.setter
    def TessellationResolution(self, tessellationResolution: UVParameterizationBuilder.TessellationResolutions):
        """
        Setter for property: (@link UVParameterizationBuilder.TessellationResolutions NXOpen.GeometricUtilities.UVMapping.UVParameterizationBuilder.TessellationResolutions@endlink) TessellationResolution
          the tessellation resolution   
            
         
        """
        pass
    
    ## Getter for property: (@link UVParameterizationBuilder.ParameterizationTypes NXOpen.GeometricUtilities.UVMapping.UVParameterizationBuilder.ParameterizationTypes@endlink) Type
    ##   the preserving type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return UVParameterizationBuilder.ParameterizationTypes
    @property
    def Type(self) -> UVParameterizationBuilder.ParameterizationTypes:
        """
        Getter for property: (@link UVParameterizationBuilder.ParameterizationTypes NXOpen.GeometricUtilities.UVMapping.UVParameterizationBuilder.ParameterizationTypes@endlink) Type
          the preserving type   
            
         
        """
        pass
    
    ## Setter for property: (@link UVParameterizationBuilder.ParameterizationTypes NXOpen.GeometricUtilities.UVMapping.UVParameterizationBuilder.ParameterizationTypes@endlink) Type

    ##   the preserving type   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @Type.setter
    def Type(self, type: UVParameterizationBuilder.ParameterizationTypes):
        """
        Setter for property: (@link UVParameterizationBuilder.ParameterizationTypes NXOpen.GeometricUtilities.UVMapping.UVParameterizationBuilder.ParameterizationTypes@endlink) Type
          the preserving type   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectTaggedObject NXOpen.SelectTaggedObject@endlink) UDirectionCurve
    ##   a single edge or curve used to define U direction.  
    ##    
    ##             If an edge is specified, it has to belong to selected faces. 
    ##             If a curve is specified, it has to be one from selected curves for ripping.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.SelectTaggedObject
    @property
    def UDirectionCurve(self) -> NXOpen.SelectTaggedObject:
        """
        Getter for property: (@link NXOpen.SelectTaggedObject NXOpen.SelectTaggedObject@endlink) UDirectionCurve
          a single edge or curve used to define U direction.  
           
                    If an edge is specified, it has to belong to selected faces. 
                    If a curve is specified, it has to be one from selected curves for ripping.   
         
        """
        pass
    
    ##  Evaluates parameterization 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def Evaluate(builder: UVParameterizationBuilder) -> None:
        """
         Evaluates parameterization 
        """
        pass
    
## @package NXOpen.GeometricUtilities.UVMapping
## Classes, Enums and Structs under NXOpen.GeometricUtilities.UVMapping namespace

##  @link MakeSymmetricParameterizationDataTypes NXOpen.GeometricUtilities.UVMapping.MakeSymmetricParameterizationDataTypes @endlink is an alias for @link MakeSymmetricParameterizationData.Types NXOpen.GeometricUtilities.UVMapping.MakeSymmetricParameterizationData.Types@endlink
MakeSymmetricParameterizationDataTypes = MakeSymmetricParameterizationData.Types


## @link UVMeshManipulatorDataObjectSelectionData_Struct NXOpen.GeometricUtilities.UVMapping.UVMeshManipulatorDataObjectSelectionData_Struct@endlink is an alias for @link UVMeshManipulatorData.ObjectSelectionData NXOpen.GeometricUtilities.UVMapping.UVMeshManipulatorData.ObjectSelectionData@endlink.
UVMeshManipulatorDataObjectSelectionData_Struct = UVMeshManipulatorData.ObjectSelectionData


##  @link UVParameterizationBuilderParameterizationTypes NXOpen.GeometricUtilities.UVMapping.UVParameterizationBuilderParameterizationTypes @endlink is an alias for @link UVParameterizationBuilder.ParameterizationTypes NXOpen.GeometricUtilities.UVMapping.UVParameterizationBuilder.ParameterizationTypes@endlink
UVParameterizationBuilderParameterizationTypes = UVParameterizationBuilder.ParameterizationTypes


##  @link UVParameterizationBuilderTessellationResolutions NXOpen.GeometricUtilities.UVMapping.UVParameterizationBuilderTessellationResolutions @endlink is an alias for @link UVParameterizationBuilder.TessellationResolutions NXOpen.GeometricUtilities.UVMapping.UVParameterizationBuilder.TessellationResolutions@endlink
UVParameterizationBuilderTessellationResolutions = UVParameterizationBuilder.TessellationResolutions


