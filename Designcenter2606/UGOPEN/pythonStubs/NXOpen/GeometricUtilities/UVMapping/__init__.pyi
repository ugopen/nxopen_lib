from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
class MakeSymmetricParameterizationData(NXOpen.Builder): 
    """ Make UV parameterization symmetric. """
    class Types(Enum):
        """
        Members Include: 
         |SymmetryInU|  Symmetric about U 
         |SymmetryInV|  Symmetric about V 

        """
        SymmetryInU: int
        SymmetryInV: int
        @staticmethod
        def ValueOf(value: int) -> MakeSymmetricParameterizationData.Types:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Point(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) Point
         Returns the point of symmetry.  
             
         
        """
        pass
    @Point.setter
    def Point(self, point0: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) Point
         Returns the point of symmetry.  
             
         
        """
        pass
    @property
    def ReverseDirection(self) -> bool:
        """
        Getter for property: (bool) ReverseDirection
         Returns the reverse direction   
            
         
        """
        pass
    @ReverseDirection.setter
    def ReverseDirection(self, reverseDirection: bool):
        """
        Setter for property: (bool) ReverseDirection
         Returns the reverse direction   
            
         
        """
        pass
    @property
    def Type(self) -> MakeSymmetricParameterizationData.Types:
        """
        Getter for property: ( MakeSymmetricParameterizationData.Types NXOpen.GeometricU) Type
         Returns the type   
            
         
        """
        pass
    @Type.setter
    def Type(self, type: MakeSymmetricParameterizationData.Types):
        """
        Setter for property: ( MakeSymmetricParameterizationData.Types NXOpen.GeometricU) Type
         Returns the type   
            
         
        """
        pass
    @property
    def UVPatches(self) -> NXOpen.SelectNXObject:
        """
        Getter for property: ( NXOpen.SelectNXObject) UVPatches
         Returns the uv patches   
            
         
        """
        pass
import NXOpen
class ReverseUVParameterizationData(NXOpen.Builder): 
    """ Reverse UV parameterization. """
    @property
    def CanReverseU(self) -> bool:
        """
        Getter for property: (bool) CanReverseU
         Returns the flag indicating if U direction to be reversed.  
             
         
        """
        pass
    @CanReverseU.setter
    def CanReverseU(self, reverse: bool):
        """
        Setter for property: (bool) CanReverseU
         Returns the flag indicating if U direction to be reversed.  
             
         
        """
        pass
    @property
    def CanReverseV(self) -> bool:
        """
        Getter for property: (bool) CanReverseV
         Returns the flag indicating if V direction to be reversed.  
             
         
        """
        pass
    @CanReverseV.setter
    def CanReverseV(self, reverse: bool):
        """
        Setter for property: (bool) CanReverseV
         Returns the flag indicating if V direction to be reversed.  
             
         
        """
        pass
    @property
    def Patches(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: ( NXOpen.SelectDisplayableObjectList) Patches
         Returns the object list.  
             
         
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class SelectUVMeshObjectData(NXOpen.TaggedObject): 
    """ Represents UV mesh topology object selection. """
    @property
    def SelectionList(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: ( NXOpen.SelectDisplayableObjectList) SelectionList
         Returns the object list.  
             
         
        """
        pass
    def ClearAndAdd(self, objects: List[NXOpen.NXObject], view: NXOpen.View, point: NXOpen.Point3d) -> None:
        """
         Clears the currently present objects and adds new objects. 
        """
        pass
    def SetCursorLocation(self, point: NXOpen.Point3d) -> None:
        """
         Sets the cursor location in absolute coordinates. 
        """
        pass
    def SetViewDirection(self, direction: NXOpen.Vector3d) -> None:
        """
         Sets the view direction. 
        """
        pass
import NXOpen
class TransformUVParameterizationData(NXOpen.Builder): 
    """ Transform UV parameterization by transforming patches in UV spaces. """
    @property
    def CanMoveToolOnly(self) -> bool:
        """
        Getter for property: (bool) CanMoveToolOnly
         Returns the flag indicating if only the transformation tool can be moved without affecting UV patches.  
             
         
        """
        pass
    @CanMoveToolOnly.setter
    def CanMoveToolOnly(self, canMoveToolOnly: bool):
        """
        Setter for property: (bool) CanMoveToolOnly
         Returns the flag indicating if only the transformation tool can be moved without affecting UV patches.  
             
         
        """
        pass
    @property
    def CanRelocateToolToSelection(self) -> bool:
        """
        Getter for property: (bool) CanRelocateToolToSelection
         Returns the flat indicating if transformation tool can be relocated based on selected entities.  
             
         
        """
        pass
    @CanRelocateToolToSelection.setter
    def CanRelocateToolToSelection(self, canRelocateToolToSelection: bool):
        """
        Setter for property: (bool) CanRelocateToolToSelection
         Returns the flat indicating if transformation tool can be relocated based on selected entities.  
             
         
        """
        pass
    @property
    def CanReorientToolToSelection(self) -> bool:
        """
        Getter for property: (bool) CanReorientToolToSelection
         Returns the flat indicating if transformation tool can be reoriented based on selected entities.  
             
         
        """
        pass
    @CanReorientToolToSelection.setter
    def CanReorientToolToSelection(self, canReorientToolToSelection: bool):
        """
        Setter for property: (bool) CanReorientToolToSelection
         Returns the flat indicating if transformation tool can be reoriented based on selected entities.  
             
         
        """
        pass
    @property
    def CanScaleUniformly(self) -> bool:
        """
        Getter for property: (bool) CanScaleUniformly
         Returns the flag indicating if UV patches can be scaled uniformly.  
             
         
        """
        pass
    @CanScaleUniformly.setter
    def CanScaleUniformly(self, canScaleUniformly: bool):
        """
        Setter for property: (bool) CanScaleUniformly
         Returns the flag indicating if UV patches can be scaled uniformly.  
             
         
        """
        pass
    @property
    def UVMeshManipulator(self) -> UVMeshManipulatorData:
        """
        Getter for property: ( UVMeshManipulatorData NXOpen.GeometricU) UVMeshManipulator
         Returns the UV mesh manipulation Tool.  
             
         
        """
        pass
    def Update(self) -> None:
        """
         Updates the parameterization by applying the transformation. 
        """
        pass
import NXOpen
class UVMappingCollection(NXOpen.Object): 
    """ This class contains the methods for creating and manipulating a UVMapping object. """
    def CreateMakeSymmetricParameterizationData(self) -> MakeSymmetricParameterizationData:
        """
         Creates a NXOpen.GeometricUtilities.UVMapping.MakeSymmetricParameterizationData 
         Returns builder ( MakeSymmetricParameterizationData NXOpen.GeometricU): .
        """
        pass
    def CreateReverseUVParameterizationData(self) -> ReverseUVParameterizationData:
        """
         Creates a NXOpen.GeometricUtilities.UVMapping.ReverseUVParameterizationData 
         Returns builder ( ReverseUVParameterizationData NXOpen.GeometricU): .
        """
        pass
    def CreateTransformUVParameterizationData(self) -> TransformUVParameterizationData:
        """
         Creates a NXOpen.GeometricUtilities.UVMapping.TransformUVParameterizationData 
         Returns builder ( TransformUVParameterizationData NXOpen.GeometricU): .
        """
        pass
    def CreateUVParameterizationBuilder(self) -> UVParameterizationBuilder:
        """
         Creates a GeometricUtilities.UVMapping.UVParameterizationBuilder 
         Returns builder ( UVParameterizationBuilder NXOpen.GeometricU): .
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class UVMeshManipulatorData(SelectUVMeshObjectData): 
    """ UV Mesh manipulation tool.
        """
    class ObjectSelectionData:
        """
         Contains object selection information. 
         UVMeshManipulatorDataObjectSelectionData_Struct NXOpen.GeometricU is an alias for  UVMeshManipulatorData.ObjectSelectionData NXOpen.GeometricU.
        """
        @property
        def SelectedObject(self) -> NXOpen.NXObject:
            """
            Getter for property SelectedObject
            The selected object.

            """
            pass
        @SelectedObject.setter
        def SelectedObject(self, value: NXOpen.NXObject):
            """
            Getter for property SelectedObject
            The selected object.
            Setter for property SelectedObject
            The selected object.

            """
            pass
        @property
        def SelectionPosition(self) -> NXOpen.Point3d:
            """
            Getter for property SelectionPosition
            The point at which object is selected, the point                                                         under the cursor when seen in view direction.

            """
            pass
        @SelectionPosition.setter
        def SelectionPosition(self, value: NXOpen.Point3d):
            """
            Getter for property SelectionPosition
            The point at which object is selected, the point                                                         under the cursor when seen in view direction.
            Setter for property SelectionPosition
            The point at which object is selected, the point                                                         under the cursor when seen in view direction.

            """
            pass
        @property
        def ViewDirection(self) -> NXOpen.Vector3d:
            """
            Getter for property ViewDirection
            The view direction.

            """
            pass
        @ViewDirection.setter
        def ViewDirection(self, value: NXOpen.Vector3d):
            """
            Getter for property ViewDirection
            The view direction.
            Setter for property ViewDirection
            The view direction.

            """
            pass
        @property
        def IsSnappedPosition(self) -> bool:
            """
            Getter for property IsSnappedPosition
            Is SelectionPosition a snapped location.

            """
            pass
        @IsSnappedPosition.setter
        def IsSnappedPosition(self, value: bool):
            """
            Getter for property IsSnappedPosition
            Is SelectionPosition a snapped location.
            Setter for property IsSnappedPosition
            Is SelectionPosition a snapped location.

            """
            pass
    @property
    def Transformer(self) -> NXOpen.GeometricUtilities.TransformerData:
        """
        Getter for property: ( NXOpen.GeometricUtilities.TransformerData) Transformer
         Returns the transformation tool.  
             
         
        """
        pass
    def SetTransformerToObject(self, selectionData: UVMeshManipulatorData.ObjectSelectionData) -> None:
        """
         Repositions the NXOpen.GeometricUtilities.TransformerData to the specified entity. 
        """
        pass
    def SetUAxisDirection(self, canAlignToUDirection: bool) -> None:
        """
         Aligns the U axis to U or V direction. 
        """
        pass
    def SetVAxisDirection(self, canAlignToVDirection: bool) -> None:
        """
         Aligns the V axis to U or V direction. 
        """
        pass
import NXOpen
class UVParameterizationBuilder(NXOpen.Builder): 
    """ Represents a UVParameterization builder """
    class ConstraintOptions(Enum):
        """
        Members Include: 
         |NotSet|   No Constraint, UV aligned automatically 
         |Edges|  UV Aligned to edges 

        """
        NotSet: int
        Edges: int
        @staticmethod
        def ValueOf(value: int) -> UVParameterizationBuilder.ConstraintOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ParameterizationTypes(Enum):
        """
        Members Include: 
         |ShapePreserving|  Preserves shape. Deprecated in NX1899. Use  NXOpen.GeometricUtilities.UVMapping.UVParameterizationBuilder.ParameterizationTypes.LengthPreserving  instead. 
         |LengthPreserving|  Preserves length. Deprecated in NX2406. Use  NXOpen.GeometricUtilities.UVMapping.UVParameterizationBuilder.ParameterizationTypes.Generic  instead.
         |Generic|   Generic 
         |Cylindrical|  Cylindrical 

        """
        ShapePreserving: int
        LengthPreserving: int
        Generic: int
        Cylindrical: int
        @staticmethod
        def ValueOf(value: int) -> UVParameterizationBuilder.ParameterizationTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class TessellationResolutions(Enum):
        """
        Members Include: 
         |Coarse| 
         |Standard| 
         |Fine| 
         |ExtraFine| 

        """
        Coarse: int
        Standard: int
        Fine: int
        ExtraFine: int
        @staticmethod
        def ValueOf(value: int) -> UVParameterizationBuilder.TessellationResolutions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ConstraintOption(self) -> UVParameterizationBuilder.ConstraintOptions:
        """
        Getter for property: ( UVParameterizationBuilder.ConstraintOptions NXOpen.GeometricU) ConstraintOption
         Returns the option of uv alignment   
            
         
        """
        pass
    @ConstraintOption.setter
    def ConstraintOption(self, constraintOption: UVParameterizationBuilder.ConstraintOptions):
        """
        Setter for property: ( UVParameterizationBuilder.ConstraintOptions NXOpen.GeometricU) ConstraintOption
         Returns the option of uv alignment   
            
         
        """
        pass
    @property
    def Faces(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) Faces
         Returns the faces   
            
         
        """
        pass
    @property
    def NumberOfGridLines(self) -> int:
        """
        Getter for property: (int) NumberOfGridLines
         Returns the number of grid lines   
            
         
        """
        pass
    @NumberOfGridLines.setter
    def NumberOfGridLines(self, numGridLines: int):
        """
        Setter for property: (int) NumberOfGridLines
         Returns the number of grid lines   
            
         
        """
        pass
    @property
    def OuterBoundarySeedEdge(self) -> NXOpen.SelectEdge:
        """
        Getter for property: ( NXOpen.SelectEdge) OuterBoundarySeedEdge
         Returns the seed edge   
            
         
        """
        pass
    @property
    def RipEdges(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) RipEdges
         Returns the rip edges   
            
         
        """
        pass
    @property
    def TessellationResolution(self) -> UVParameterizationBuilder.TessellationResolutions:
        """
        Getter for property: ( UVParameterizationBuilder.TessellationResolutions NXOpen.GeometricU) TessellationResolution
         Returns the tessellation resolution   
            
         
        """
        pass
    @TessellationResolution.setter
    def TessellationResolution(self, tessellationResolution: UVParameterizationBuilder.TessellationResolutions):
        """
        Setter for property: ( UVParameterizationBuilder.TessellationResolutions NXOpen.GeometricU) TessellationResolution
         Returns the tessellation resolution   
            
         
        """
        pass
    @property
    def Type(self) -> UVParameterizationBuilder.ParameterizationTypes:
        """
        Getter for property: ( UVParameterizationBuilder.ParameterizationTypes NXOpen.GeometricU) Type
         Returns the type   
            
         
        """
        pass
    @Type.setter
    def Type(self, type: UVParameterizationBuilder.ParameterizationTypes):
        """
        Setter for property: ( UVParameterizationBuilder.ParameterizationTypes NXOpen.GeometricU) Type
         Returns the type   
            
         
        """
        pass
    @property
    def U1Edges(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) U1Edges
         Returns the U1 edges   
            
         
        """
        pass
    @property
    def U2Edges(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) U2Edges
         Returns the U2 edges   
            
         
        """
        pass
    @property
    def UDirectionCurve(self) -> NXOpen.SelectTaggedObject:
        """
        Getter for property: ( NXOpen.SelectTaggedObject) UDirectionCurve
         Returns a single edge or curve used to define U direction.  
           
                    If an edge is specified, it has to belong to selected faces. 
                    If a curve is specified, it has to be one from selected curves for ripping.   
         
        """
        pass
    @property
    def V1Edges(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) V1Edges
         Returns the V1 edges   
            
         
        """
        pass
    @property
    def V2Edges(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) V2Edges
         Returns the V2 edges   
            
         
        """
        pass
    def Evaluate(self) -> None:
        """
         Evaluates parameterization 
        """
        pass
