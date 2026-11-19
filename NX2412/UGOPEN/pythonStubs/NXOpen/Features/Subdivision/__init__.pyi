from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
class CageFromFacetBodyBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Features.Subdivision.CageFromFacetBodyBuilder builder.  """
    @property
    def AverageSize(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) AverageSize
         Returns the average size   
            
         
        """
        pass
    @property
    def FacetRegion(self) -> NXOpen.FacetCollector:
        """
        Getter for property: ( NXOpen.FacetCollector) FacetRegion
         Returns the facets to be subdivisioned   
            
         
        """
        pass
    @property
    def ShowDeviationPlot(self) -> bool:
        """
        Getter for property: (bool) ShowDeviationPlot
         Returns the deviation toggle  
            
         
        """
        pass
    @ShowDeviationPlot.setter
    def ShowDeviationPlot(self, isShowDeviationPlot: bool):
        """
        Setter for property: (bool) ShowDeviationPlot
         Returns the deviation toggle  
            
         
        """
        pass
import NXOpen
import NXOpen.Display
import NXOpen.GeometricUtilities
class CageManipulatorData(SelectCageObjectData): 
    """ Subdivision cage manipulation tool.
        """
    class ObjectMoveData:
        """
         Contains object movement information. 
         CageManipulatorDataObjectMoveData_Struct NXOpen.Featur is an alias for  CageManipulatorData.ObjectMoveData NXOpen.Featur.
        """
        @property
        def DraggedObject(self) -> NXOpen.NXObject:
            """
            Getter for property DraggedObject
            The dragged object.

            """
            pass
        @DraggedObject.setter
        def DraggedObject(self, value: NXOpen.NXObject):
            """
            Getter for property DraggedObject
            The dragged object.
            Setter for property DraggedObject
            The dragged object.

            """
            pass
        @property
        def BeginDragCursorPosition(self) -> NXOpen.Point3d:
            """
            Getter for property BeginDragCursorPosition
            The point from which object dragging is initiated, the point                                                              under the cursor when seen in view direction.

            """
            pass
        @BeginDragCursorPosition.setter
        def BeginDragCursorPosition(self, value: NXOpen.Point3d):
            """
            Getter for property BeginDragCursorPosition
            The point from which object dragging is initiated, the point                                                              under the cursor when seen in view direction.
            Setter for property BeginDragCursorPosition
            The point from which object dragging is initiated, the point                                                              under the cursor when seen in view direction.

            """
            pass
        @property
        def BeginDragObjectPosition(self) -> NXOpen.Point3d:
            """
            Getter for property BeginDragObjectPosition
            The point on object near cursor from which object dragging is initiated

            """
            pass
        @BeginDragObjectPosition.setter
        def BeginDragObjectPosition(self, value: NXOpen.Point3d):
            """
            Getter for property BeginDragObjectPosition
            The point on object near cursor from which object dragging is initiated
            Setter for property BeginDragObjectPosition
            The point on object near cursor from which object dragging is initiated

            """
            pass
        @property
        def View(self) -> NXOpen.Display.NXOpen.View:
            """
            Getter for property View
            The view in which object is dragged.

            """
            pass
        @View.setter
        def View(self, value: NXOpen.Display.NXOpen.View):
            """
            Getter for property View
            The view in which object is dragged.
            Setter for property View
            The view in which object is dragged.

            """
            pass
        @property
        def MicropositioningScale(self) -> float:
            """
            Getter for property MicropositioningScale
            The micropositioning scale.

            """
            pass
        @MicropositioningScale.setter
        def MicropositioningScale(self, value: float):
            """
            Getter for property MicropositioningScale
            The micropositioning scale.
            Setter for property MicropositioningScale
            The micropositioning scale.

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
    class ObjectSelectionData:
        """
         Contains object selection information. 
         CageManipulatorDataObjectSelectionData_Struct NXOpen.Featur is an alias for  CageManipulatorData.ObjectSelectionData NXOpen.Featur.
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
    def EndMove(self) -> None:
        """
         Releases the data prepared at the beginning of the move. 
        """
        pass
    @overload
    def Move(self, moveToPoint: NXOpen.Point3d, isSnapGesture: bool) -> None:
        """
         Moves the objects by dragging. 
        """
        pass
    @overload
    def Move(self, moveToPoint: NXOpen.Point3d, point: NXOpen.Point, isSnapGesture: bool) -> None:
        """
         Moves the objects by dragging. A constraint point can be assigned when moving a vertex. 
        """
        pass
    def PrepareToMove(self, moveData: CageManipulatorData.ObjectMoveData) -> None:
        """
         Prepares data to move the objects. 
        """
        pass
    def ResetTransformerToCentroidOfSelection(self) -> None:
        """
         Repositions the NXOpen.GeometricUtilities.TransformerData to the centroid of the selected entities. 
        """
        pass
    def ResetTransformerToLocation(self, location: NXOpen.Point3d) -> None:
        """
         Repositions the NXOpen.GeometricUtilities.TransformerData to the specified location. 
        """
        pass
    def SetTransformerToObject(self, selectionData: CageManipulatorData.ObjectSelectionData) -> None:
        """
         Repositions the NXOpen.GeometricUtilities.TransformerData to the specified entity. 
        """
        pass
    def StepMove(self, step: float) -> None:
        """
         Moves the objects by step value. 
        """
        pass
import NXOpen.Features
class CagePolylineBuilder(NXOpen.Features.PolylineBuilder): 
    """ Cage polyline builder class. """
    pass
import NXOpen
class CageSectionDataList(NXOpen.TaggedObject): 
    """ Represents a list of objects."""
    @property
    def Length(self) -> int:
        """
        Getter for property: (int) Length
         Returns the length of the list   
            
         
        """
        pass
    @overload
    def Append(self, objects: List[CageSectionData]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    @overload
    def Append(self, objectValue: CageSectionData) -> None:
        """
         Appends an object to the list
            
        """
        pass
    @overload
    def Clear(self) -> None:
        """
         Clears the entire list without deleting the objects.  The caller is responsible for 
                accounting for these objects.  If they are not used or deleted by the time the part is 
                closed (in other words, leaked) an error will occur 
        """
        pass
    def ClearIndex(self, delete_idx: int) -> None:
        """
         Deletes the item at the index specified.  The size of the list does
               not change, but the item at this index is set to NULL.
            
        """
        pass
    @overload
    def Clear(self, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Clears the entire list 
        """
        pass
    @overload
    def Erase(self, index: int) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to be. 
        """
        pass
    @overload
    def Erase(self, index: int, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object at the given position from the list.
                The list is shifted so that there isn't a null where the object used to be. 
        """
        pass
    @overload
    def Erase(self, obj: CageSectionData) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    @overload
    def Erase(self, obj: CageSectionData, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object from the list.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    def FindIndex(self, obj: CageSectionData) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
               -1 is returned.
            
         Returns index (int):  index of input object, -1 if not on list .
        """
        pass
    def FindItem(self, index: int) -> CageSectionData:
        """
         Returns the object at the input index.  May be NULL.
            
         Returns obj ( CageSectionData NXOpen.Featur):  object found at input index .
        """
        pass
    def GetContents(self) -> List[CageSectionData]:
        """
         Gets the contents of the entire list 
         Returns objects ( CageSectionData List[NXOpen.Feat):  The list contents .
        """
        pass
    def Insert(self, location: int, objectValue: CageSectionData) -> None:
        """
         Inserts an object at the specified location 
        """
        pass
    def MoveToBottom(self, index: int) -> None:
        """
         Move object at the specified location to the bottom of the list.
        """
        pass
    def MoveToTop(self, index: int) -> None:
        """
         Move object at the specified location to the top of the list.
        """
        pass
    def SetContents(self, objects: List[CageSectionData]) -> None:
        """
         Sets the contents of the entire list. This overwrites the previous contents of this list, 
                but does not delete any objects that were originally on the list.
             
        """
        pass
    @overload
    def Swap(self, index1: int, index2: int) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
    @overload
    def Swap(self, object1: CageSectionData, object2: CageSectionData) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class CageSectionData(NXOpen.TaggedObject): 
    """ Represents subdivision cage section selection. """
    @property
    def CanReverseDirection(self) -> bool:
        """
        Getter for property: (bool) CanReverseDirection
         Returns the flag indicating if section direction is reversed.  
             
         
        """
        pass
    @CanReverseDirection.setter
    def CanReverseDirection(self, reverse: bool):
        """
        Setter for property: (bool) CanReverseDirection
         Returns the flag indicating if section direction is reversed.  
             
         
        """
        pass
    @property
    def SelectionObject(self) -> SelectCageObjectData:
        """
        Getter for property: ( SelectCageObjectData NXOpen.Featur) SelectionObject
         Returns the selection object.  
             
         
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class CopyCageBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Features.Subdivision.CopyCageBuilder builder. """
    @property
    def CanMoveToolOnly(self) -> bool:
        """
        Getter for property: (bool) CanMoveToolOnly
         Returns the flag indicating if tool can be moved alone without moving selected topology   
            
         
        """
        pass
    @CanMoveToolOnly.setter
    def CanMoveToolOnly(self, canMoveToolOnly: bool):
        """
        Setter for property: (bool) CanMoveToolOnly
         Returns the flag indicating if tool can be moved alone without moving selected topology   
            
         
        """
        pass
    @property
    def CanRelocateToolToSelection(self) -> bool:
        """
        Getter for property: (bool) CanRelocateToolToSelection
         Returns the flag indicating if tool should relocate to selection   
            
         
        """
        pass
    @CanRelocateToolToSelection.setter
    def CanRelocateToolToSelection(self, canRelocateToolToSelection: bool):
        """
        Setter for property: (bool) CanRelocateToolToSelection
         Returns the flag indicating if tool should relocate to selection   
            
         
        """
        pass
    @property
    def CanReorientToolToSelection(self) -> bool:
        """
        Getter for property: (bool) CanReorientToolToSelection
         Returns the flag indicating if tool should reorient to selection   
            
         
        """
        pass
    @CanReorientToolToSelection.setter
    def CanReorientToolToSelection(self, canReorientToolToSelection: bool):
        """
        Setter for property: (bool) CanReorientToolToSelection
         Returns the flag indicating if tool should reorient to selection   
            
         
        """
        pass
    @property
    def NumberOfCopies(self) -> int:
        """
        Getter for property: (int) NumberOfCopies
         Returns the number of copies   
            
         
        """
        pass
    @NumberOfCopies.setter
    def NumberOfCopies(self, numberOfCopies: int):
        """
        Setter for property: (int) NumberOfCopies
         Returns the number of copies   
            
         
        """
        pass
    @property
    def Objects(self) -> SelectCageObjectData:
        """
        Getter for property: ( SelectCageObjectData NXOpen.Featur) Objects
         Returns the objects to be copied   
            
         
        """
        pass
    @property
    def Transformer(self) -> NXOpen.GeometricUtilities.TransformerData:
        """
        Getter for property: ( NXOpen.GeometricUtilities.TransformerData) Transformer
         Returns the transformation tool.  
             
         
        """
        pass
    def ResetTransformerToCentroidOfSelection(self) -> None:
        """
         Repositions the NXOpen.GeometricUtilities.TransformerData to the centroid of the selected entities. 
        """
        pass
    def SetTransformerToObject(self, selectionData: CageManipulatorData.ObjectSelectionData) -> None:
        """
         Repositions the NXOpen.GeometricUtilities.TransformerData to the specified entity. 
        """
        pass
import NXOpen
class CopyCageData(NXOpen.Builder): 
    """ Represents a NXOpen.Features.Subdivision.CopyCageData. 
            Copies Control Cage, Cage Face and Cage Polyline type objects on the clipboard.
        """
    def GetObjects(self) -> List[NXOpen.NXObject]:
        """
         Returns the objects to be copied. 
         Returns objects ( NXOpen.NXObject Li):  .
        """
        pass
    def SetObjects(self, objects: List[NXOpen.NXObject]) -> None:
        """
         Sets the objects to be copied. 
        """
        pass
import NXOpen
class DefineWorkRegionBuilder(NXOpen.Builder): 
    """ Represents a Features.Subdivision.DefineWorkRegionBuilder builder. """
    class FrozenRegionDefinitionMethods(Enum):
        """
        Members Include: 
         |Hidden|  Do not display the frozen region 
         |Colored|  Mark frozen region with color and do not allow its selection 

        """
        Hidden: int
        Colored: int
        @staticmethod
        def ValueOf(value: int) -> DefineWorkRegionBuilder.FrozenRegionDefinitionMethods:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class WorkRegionDefinitionMethods(Enum):
        """
        Members Include: 
         |All|  Treat all the region as work region 
         |Selected|  Specify a region as work region 

        """
        All: int
        Selected: int
        @staticmethod
        def ValueOf(value: int) -> DefineWorkRegionBuilder.WorkRegionDefinitionMethods:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def FrozenColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) FrozenColor
         Returns the frozen region color   
            
         
        """
        pass
    @FrozenColor.setter
    def FrozenColor(self, frozenColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) FrozenColor
         Returns the frozen region color   
            
         
        """
        pass
    @property
    def FrozenRegionDefinitionMethod(self) -> DefineWorkRegionBuilder.FrozenRegionDefinitionMethods:
        """
        Getter for property: ( DefineWorkRegionBuilder.FrozenRegionDefinitionMethods NXOpen.Featur) FrozenRegionDefinitionMethod
         Returns the frozen region method   
            
         
        """
        pass
    @FrozenRegionDefinitionMethod.setter
    def FrozenRegionDefinitionMethod(self, frozenRegionDefinitionMethod: DefineWorkRegionBuilder.FrozenRegionDefinitionMethods):
        """
        Setter for property: ( DefineWorkRegionBuilder.FrozenRegionDefinitionMethods NXOpen.Featur) FrozenRegionDefinitionMethod
         Returns the frozen region method   
            
         
        """
        pass
    @property
    def WorkRegionDefinitionMethod(self) -> DefineWorkRegionBuilder.WorkRegionDefinitionMethods:
        """
        Getter for property: ( DefineWorkRegionBuilder.WorkRegionDefinitionMethods NXOpen.Featur) WorkRegionDefinitionMethod
         Returns the work region definition method   
            
         
        """
        pass
    @WorkRegionDefinitionMethod.setter
    def WorkRegionDefinitionMethod(self, workRegionDefinitionMethod: DefineWorkRegionBuilder.WorkRegionDefinitionMethods):
        """
        Setter for property: ( DefineWorkRegionBuilder.WorkRegionDefinitionMethods NXOpen.Featur) WorkRegionDefinitionMethod
         Returns the work region definition method   
            
         
        """
        pass
    @property
    def WorkRegionObjects(self) -> SelectCageObjectData:
        """
        Getter for property: ( SelectCageObjectData NXOpen.Featur) WorkRegionObjects
         Returns the work region objects   
            
         
        """
        pass
import NXOpen
class DeleteConstraintBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Features.Subdivision.DeleteConstraintBuilder builder.  """
    @property
    def Objects(self) -> SelectCageObjectData:
        """
        Getter for property: ( SelectCageObjectData NXOpen.Featur) Objects
         Returns the constrained objects whose constraint to be deleted.  
             
         
        """
        pass
import NXOpen
class DrawCageData(NXOpen.Builder): 
    """ Represents a NXOpen.Features.Subdivision.DrawCageData data. """
    class FaceShapeType(Enum):
        """
        Members Include: 
         |Quad|  Quadrilateral shape 
         |Polygon|  General polygon 

        """
        Quad: int
        Polygon: int
        @staticmethod
        def ValueOf(value: int) -> DrawCageData.FaceShapeType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SelectionData:
        """
         Contains object selection information to be used to create a patch. 
         DrawCageDataSelectionData_Struct NXOpen.Featur is an alias for  DrawCageData.SelectionData NXOpen.Featur.
        """
        @property
        def SnappedObject(self) -> NXOpen.NXObject:
            """
            Getter for property SnappedObject
            The selected or snapped object, can be an existing vertex or a point

            """
            pass
        @SnappedObject.setter
        def SnappedObject(self, value: NXOpen.NXObject):
            """
            Getter for property SnappedObject
            The selected or snapped object, can be an existing vertex or a point
            Setter for property SnappedObject
            The selected or snapped object, can be an existing vertex or a point

            """
            pass
        @property
        def SnappedPosition(self) -> NXOpen.Point3d:
            """
            Getter for property SnappedPosition
            The point at which object is selected or snapped.

            """
            pass
        @SnappedPosition.setter
        def SnappedPosition(self, value: NXOpen.Point3d):
            """
            Getter for property SnappedPosition
            The point at which object is selected or snapped.
            Setter for property SnappedPosition
            The point at which object is selected or snapped.

            """
            pass
        @property
        def IsInferringPaused(self) -> bool:
            """
            Getter for property IsInferringPaused
            Flag indicating if inferring is paused.

            """
            pass
        @IsInferringPaused.setter
        def IsInferringPaused(self, value: bool):
            """
            Getter for property IsInferringPaused
            Flag indicating if inferring is paused.
            Setter for property IsInferringPaused
            Flag indicating if inferring is paused.

            """
            pass
    @property
    def CageManipulator(self) -> CageManipulatorData:
        """
        Getter for property: ( CageManipulatorData NXOpen.Featur) CageManipulator
         Returns the cage manipulation data.  
           Cage manipulator helps create new and edit existing vertices.   
         
        """
        pass
    @property
    def FaceShape(self) -> DrawCageData.FaceShapeType:
        """
        Getter for property: ( DrawCageData.FaceShapeType NXOpen.Featur) FaceShape
         Returns the face shape.  
             
         
        """
        pass
    @FaceShape.setter
    def FaceShape(self, shape: DrawCageData.FaceShapeType):
        """
        Setter for property: ( DrawCageData.FaceShapeType NXOpen.Featur) FaceShape
         Returns the face shape.  
             
         
        """
        pass
    def AddVertex(self, selectionData: DrawCageData.SelectionData) -> None:
        """
         Adds a vertex and creates a patch if possible. 
        """
        pass
    def ClosePolygon(self) -> None:
        """
         Closes the polygon and creates a patch. 
        """
        pass
    def ResetStartPoint(self) -> None:
        """
         Discards the current polygon and restarts new. 
        """
        pass
import NXOpen
import NXOpen.Features
class ExportSubdivisionGeometryBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Features.Subdivision.ExportSubdivisionGeometryBuilder builder. """
    @property
    def FeatureSet(self) -> NXOpen.Features.SelectFeatureList:
        """
        Getter for property: ( NXOpen.Features.SelectFeatureList) FeatureSet
         Returns the Feature to export   
            
         
        """
        pass
    @property
    def FileName(self) -> str:
        """
        Getter for property: (str) FileName
         Returns the file name.  
           The export file will only store the topology and geometry positions of the Subdivision Cage, and 
                        not contains auxiliary data of the Subdivision feature, such as the weights, sharpness and constraints.
                      
         
        """
        pass
    @FileName.setter
    def FileName(self, filename: str):
        """
        Setter for property: (str) FileName
         Returns the file name.  
           The export file will only store the topology and geometry positions of the Subdivision Cage, and 
                        not contains auxiliary data of the Subdivision feature, such as the weights, sharpness and constraints.
                      
         
        """
        pass
import NXOpen
class ExtractCagePolylineBuilder(NXOpen.Builder): 
    """ Extract cage polyline builder class. """
    class InputCurveOption(Enum):
        """
        Members Include: 
         |Keep|  Keep input curves as they are 
         |Hide|  Hide input curves 
         |Delete|  Delete input curves 

        """
        Keep: int
        Hide: int
        Delete: int
        @staticmethod
        def ValueOf(value: int) -> ExtractCagePolylineBuilder.InputCurveOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def CurveToExtract(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) CurveToExtract
         Returns the curve to extract   
            
         
        """
        pass
    @property
    def InputCurveOptions(self) -> ExtractCagePolylineBuilder.InputCurveOption:
        """
        Getter for property: ( ExtractCagePolylineBuilder.InputCurveOption NXOpen.Featur) InputCurveOptions
         Returns the input curve options   
            
         
        """
        pass
    @InputCurveOptions.setter
    def InputCurveOptions(self, inputCurveOptions: ExtractCagePolylineBuilder.InputCurveOption):
        """
        Setter for property: ( ExtractCagePolylineBuilder.InputCurveOption NXOpen.Featur) InputCurveOptions
         Returns the input curve options   
            
         
        """
        pass
    @property
    def NumberOfSegments(self) -> int:
        """
        Getter for property: (int) NumberOfSegments
         Returns the number of segments   
            
         
        """
        pass
    @NumberOfSegments.setter
    def NumberOfSegments(self, numberOfSegments: int):
        """
        Setter for property: (int) NumberOfSegments
         Returns the number of segments   
            
         
        """
        pass
import NXOpen
class ExtractVertexPointsBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Features.Subdivision.ExtractVertexPointsBuilder builder.  """
    @property
    def CageObject(self) -> SelectCageObjectData:
        """
        Getter for property: ( SelectCageObjectData NXOpen.Featur) CageObject
         Returns the Cage Object   
            
         
        """
        pass
import NXOpen
class ImportSubdivisionGeometryBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Features.Subdivision.ImportSubdivisionGeometryBuilder builder. """
    @property
    def CanCreateSingleFeature(self) -> bool:
        """
        Getter for property: (bool) CanCreateSingleFeature
         Returns the flag indicating if single feature should be created for all the disjoint regions of the subdivision geometry.  
           
                        When false, separate feature will be created for each disjoint region.   
         
        """
        pass
    @CanCreateSingleFeature.setter
    def CanCreateSingleFeature(self, canCreateSingleFeature: bool):
        """
        Setter for property: (bool) CanCreateSingleFeature
         Returns the flag indicating if single feature should be created for all the disjoint regions of the subdivision geometry.  
           
                        When false, separate feature will be created for each disjoint region.   
         
        """
        pass
    @property
    def FileName(self) -> str:
        """
        Getter for property: (str) FileName
         Returns the file name.  
           Expects a file in standard ASCII Wavefront OBJ format used for base mesh definition of a subdivision geometry. 
                        Usage of OBJ files representing triangulated polygon mesh, similar to ones used for graphical rendering or higher resolution
                        subdivision mesh is not recommended to be used. The solid model created from such mesh will have
                        excessive amount of topology and the import operation will be inefficient.
                      
         
        """
        pass
    @FileName.setter
    def FileName(self, filename: str):
        """
        Setter for property: (str) FileName
         Returns the file name.  
           Expects a file in standard ASCII Wavefront OBJ format used for base mesh definition of a subdivision geometry. 
                        Usage of OBJ files representing triangulated polygon mesh, similar to ones used for graphical rendering or higher resolution
                        subdivision mesh is not recommended to be used. The solid model created from such mesh will have
                        excessive amount of topology and the import operation will be inefficient.
                      
         
        """
        pass
import NXOpen
class MergeSubdivisionBodiesBuilder(NXOpen.Builder): 
    """ Represents a Features.Subdivision.MergeSubdivisionBodiesBuilder builder. """
    class InputBodyOptions(Enum):
        """
        Members Include: 
         |Keep|  Keep the features as they are 
         |Hide|  Hide the features 
         |Delete|  Delete the features 

        """
        Keep: int
        Hide: int
        Delete: int
        @staticmethod
        def ValueOf(value: int) -> MergeSubdivisionBodiesBuilder.InputBodyOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def InputBodyOption(self) -> MergeSubdivisionBodiesBuilder.InputBodyOptions:
        """
        Getter for property: ( MergeSubdivisionBodiesBuilder.InputBodyOptions NXOpen.Featur) InputBodyOption
         Returns the input body option   
            
         
        """
        pass
    @InputBodyOption.setter
    def InputBodyOption(self, inputBody: MergeSubdivisionBodiesBuilder.InputBodyOptions):
        """
        Setter for property: ( MergeSubdivisionBodiesBuilder.InputBodyOptions NXOpen.Featur) InputBodyOption
         Returns the input body option   
            
         
        """
        pass
    @property
    def SubdivisionBodiesToMerge(self) -> SelectSubdivisionBodyList:
        """
        Getter for property: ( SelectSubdivisionBodyList NXOpen.Featur) SubdivisionBodiesToMerge
         Returns the  Features::Subdivision::SubdivisionBody  features to merge   
            
         
        """
        pass
import NXOpen
class MirrorCageBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Features.Subdivision.MirrorCageBuilder builder. """
    @property
    def MirrorPlane(self) -> NXOpen.Plane:
        """
        Getter for property: ( NXOpen.Plane) MirrorPlane
         Returns the mirror plane   
            
         
        """
        pass
    @MirrorPlane.setter
    def MirrorPlane(self, plane: NXOpen.Plane):
        """
        Setter for property: ( NXOpen.Plane) MirrorPlane
         Returns the mirror plane   
            
         
        """
        pass
    @property
    def Objects(self) -> SelectCageObjectData:
        """
        Getter for property: ( SelectCageObjectData NXOpen.Featur) Objects
         Returns the objects to be mirrored   
            
         
        """
        pass
    def UpdateOnMirrorPlane(self) -> None:
        """
         Updates the builder based on changes in the mirror plane. 
        """
        pass
import NXOpen
class OffsetCageBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Features.Subdivision.OffsetCageBuilder builder. """
    @property
    def CanReverseOffsetDirection(self) -> bool:
        """
        Getter for property: (bool) CanReverseOffsetDirection
         Returns the flag indicating if offset direction can be reversed.  
             
         
        """
        pass
    @CanReverseOffsetDirection.setter
    def CanReverseOffsetDirection(self, reverse: bool):
        """
        Setter for property: (bool) CanReverseOffsetDirection
         Returns the flag indicating if offset direction can be reversed.  
             
         
        """
        pass
    @property
    def NumberOfCopies(self) -> int:
        """
        Getter for property: (int) NumberOfCopies
         Returns the number of copies to offset   
            
         
        """
        pass
    @NumberOfCopies.setter
    def NumberOfCopies(self, numberOfCopies: int):
        """
        Setter for property: (int) NumberOfCopies
         Returns the number of copies to offset   
            
         
        """
        pass
    @property
    def Objects(self) -> SelectCageObjectData:
        """
        Getter for property: ( SelectCageObjectData NXOpen.Featur) Objects
         Returns the objects to be offset   
            
         
        """
        pass
    @property
    def OffsetDistance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) OffsetDistance
         Returns the offset distance.  
             
         
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class PasteCageData(NXOpen.Builder): 
    """ Represents a NXOpen.Features.Subdivision.PasteCageData builder. """
    @property
    def CanMoveToolOnly(self) -> bool:
        """
        Getter for property: (bool) CanMoveToolOnly
         Returns the flag indicating if transformer tool can be moved without transforming the selected cage topology.  
             
         
        """
        pass
    @CanMoveToolOnly.setter
    def CanMoveToolOnly(self, canMove: bool):
        """
        Setter for property: (bool) CanMoveToolOnly
         Returns the flag indicating if transformer tool can be moved without transforming the selected cage topology.  
             
         
        """
        pass
    @property
    def Transformer(self) -> NXOpen.GeometricUtilities.TransformerData:
        """
        Getter for property: ( NXOpen.GeometricUtilities.TransformerData) Transformer
         Returns the transformation tool.  
           The tool allows user to transform the pasted topology.   
         
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class SectionTubeData(NXOpen.Builder): 
    """ Represents a NXOpen.Features.Subdivision.SectionTubeData builder. """
    class SelectionData:
        """
         Contains object selection information to be used to create a section. 
         SectionTubeDataSelectionData_Struct NXOpen.Featur is an alias for  SectionTubeData.SelectionData NXOpen.Featur.
        """
        @property
        def SnappedObject(self) -> NXOpen.NXObject:
            """
            Getter for property SnappedObject
            The selected cage face or convergent face of snapped vertex

            """
            pass
        @SnappedObject.setter
        def SnappedObject(self, value: NXOpen.NXObject):
            """
            Getter for property SnappedObject
            The selected cage face or convergent face of snapped vertex
            Setter for property SnappedObject
            The selected cage face or convergent face of snapped vertex

            """
            pass
        @property
        def IsSnapped(self) -> bool:
            """
            Getter for property IsSnapped
            Flag indicating if snapping to a vertex of convergent face

            """
            pass
        @IsSnapped.setter
        def IsSnapped(self, value: bool):
            """
            Getter for property IsSnapped
            Flag indicating if snapping to a vertex of convergent face
            Setter for property IsSnapped
            Flag indicating if snapping to a vertex of convergent face

            """
            pass
        @property
        def SnappedPosition(self) -> NXOpen.Point3d:
            """
            Getter for property SnappedPosition
            The point at which vertex of face is snapped.

            """
            pass
        @SnappedPosition.setter
        def SnappedPosition(self, value: NXOpen.Point3d):
            """
            Getter for property SnappedPosition
            The point at which vertex of face is snapped.
            Setter for property SnappedPosition
            The point at which vertex of face is snapped.

            """
            pass
    @property
    def Segments(self) -> int:
        """
        Getter for property: (int) Segments
         Returns the segments   
            
         
        """
        pass
    @Segments.setter
    def Segments(self, segments: int):
        """
        Setter for property: (int) Segments
         Returns the segments   
            
         
        """
        pass
    @property
    def Transformer(self) -> NXOpen.GeometricUtilities.TransformerData:
        """
        Getter for property: ( NXOpen.GeometricUtilities.TransformerData) Transformer
         Returns the transformation tool.  
             
         
        """
        pass
    def AddSection(self, selectionData: SectionTubeData.SelectionData) -> None:
        """
         Adds a vertex and creates a section if possible. 
        """
        pass
    def RefitSection(self) -> None:
        """
         Recreates the section that is fitted to the convergent body section at the current csys location. 
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class SelectCageObjectData(NXOpen.TaggedObject): 
    """ Represents subdivision cage topology object selection. """
    @property
    def CanDeselectObjectsAutomatically(self) -> bool:
        """
        Getter for property: (bool) CanDeselectObjectsAutomatically
         Returns the flag indicating if previously selected objects can be de-selected during selection of new objects.  
             
         
        """
        pass
    @CanDeselectObjectsAutomatically.setter
    def CanDeselectObjectsAutomatically(self, canDeselect: bool):
        """
        Setter for property: (bool) CanDeselectObjectsAutomatically
         Returns the flag indicating if previously selected objects can be de-selected during selection of new objects.  
             
         
        """
        pass
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
import NXOpen.GeometricUtilities
class SelectSubdivisionBodyList(NXOpen.TaggedObject): 
    """ Represents a list of objects on a selection list.
"""
    @property
    def DuplicatesAllowed(self) -> bool:
        """
        Getter for property: (bool) DuplicatesAllowed
         Returns whether duplicate objects are allowed in the selection list.  
          
              
         
        """
        pass
    @property
    def Size(self) -> int:
        """
        Getter for property: (int) Size
         Returns the number of objects in the list.  
          
              
         
        """
        pass
    @overload
    def Add(self, objectValue: SubdivisionBody) -> bool:
        """
         Adds an object to the list
            
         Returns added (bool):  True if successfully added to list;
                                          False if the object was already a member
                                          of the list and duplicates are not allowed .
        """
        pass
    def AddWithViews(self, objects: List[SubdivisionBody], views: List[NXOpen.View]) -> bool:
        """
         Adds a set of objects with views to the list
            
         Returns added (bool):  True if successfully added all objects to the list;
                                          False if there was at least one object that was already a
                                          member of the list and duplicates are not allowed .
        """
        pass
    @overload
    def Add(self, objects: List[SubdivisionBody]) -> bool:
        """
         Adds a set of objects to the list
            
         Returns added (bool):  True if successfully added all objects to the list;
                                          False if there was at least one object that was already a
                                          member of the list and duplicates are not allowed .
        """
        pass
    @overload
    def Add(self, input_selection_method: NXOpen.SelectionMethod) -> bool:
        """
         Adds the objects from a SelectionMethod to the list
            
         Returns added (bool):  True if successfully added all objects to the list;
                                          False if there was at least one object that was already a
                                          member of the list and duplicates are not allowed .
        """
        pass
    @overload
    def Add(self, selection: SubdivisionBody, view: NXOpen.View, point: NXOpen.Point3d) -> bool:
        """
         Adds the object with the objects view and objects point
            
         Returns added (bool):  True if successfully added to list;
                                          False if the object was already a member
                                          of the list and duplicates are not allowed .
        """
        pass
    @overload
    def Add(self, snap_type: NXOpen.InferSnapType.SnapType, selection1: SubdivisionBody, view1: NXOpen.View, point1: NXOpen.Point3d, selection2: SubdivisionBody, view2: NXOpen.View, point2: NXOpen.Point3d) -> bool:
        """
         The object being selected with the objects view and objects point and snap information.
            
         Returns added (bool):  True if successfully added all objects to the list;
                                          False if there was at least one object that was already a
                                          member of the list and duplicates are not allowed .
        """
        pass
    @overload
    def Add(self, selection: SubdivisionBody, cae_sub_type: NXOpen.CaeObjectType.CaeSubType, cae_sub_id: int) -> bool:
        """
         The object being selected with CAE set object information.
            
         Returns added (bool):  True if successfully added all objects to the list;
                                          False if there was at least one object that was already a
                                          member of the list and duplicates are not allowed .
        """
        pass
    def Clear(self) -> None:
        """
         Removes all items from the list.
            
        """
        pass
    def Contains(self, objectValue: SubdivisionBody) -> bool:
        """
         Returns whether the specified object is already in the list or not.
            
         Returns list_contains (bool):  true if object is in the list, false otherwise .
        """
        pass
    def GetArray(self) -> List[SubdivisionBody]:
        """
         Returns the list of objects in the selection list.
            
         Returns objects ( SubdivisionBody List[NXOpen.Feat):  items in list .
        """
        pass
    def GetSelectObjectArray(self) -> List[NXOpen.SelectObject]:
        """
         Returns the list of SelectObjects in the selection list.
            
         Returns objects ( NXOpen.SelectObject Li):  items in list .
        """
        pass
    @overload
    def Remove(self, objectValue: SubdivisionBody) -> bool:
        """
         Remove specified object from list.
            
         Returns removed (bool):  True if successfully removed from list;
                                            False if the object was not a member of the list .
        """
        pass
    def RemoveArray(self, objects: List[SubdivisionBody]) -> bool:
        """
         Remove specified objects from list.
            
         Returns removed (bool):  True if successfully removed from list;
                                            False if the object was not a member of the list .
        """
        pass
    @overload
    def Remove(self, objectValue: SubdivisionBody, view: NXOpen.View) -> bool:
        """
         Remove specified object from list.
            
         Returns removed (bool):  True if successfully removed from list;
                                            False if the object  view was not a member of the list .
        """
        pass
    @overload
    def Remove(self, snap_type: NXOpen.InferSnapType.SnapType, selection1: SubdivisionBody, view1: NXOpen.View, point1: NXOpen.Point3d, selection2: SubdivisionBody, view2: NXOpen.View, point2: NXOpen.Point3d) -> bool:
        """
         Remove specified object from list.
            
         Returns removed (bool):  True if successfully removed from list;
                                            False if the object was not a member of the list .
        """
        pass
    @overload
    def Remove(self, input_selection_method: NXOpen.SelectionMethod) -> bool:
        """
         Removes the objects from a SelectionMethod from the list
            
         Returns removed (bool):  True if successfully removed all objects from the list;
                                            False if there was at least one object that was not a
                                            member of the list .
        """
        pass
    def SetArray(self, objects: List[SubdivisionBody]) -> None:
        """
         Sets the list of objects in the selection list. This will clear any existing
            items in the list.
            
        """
        pass
import NXOpen
class SplitSubdivisionBodyBuilder(NXOpen.Builder): 
    """ Represents a Features.Subdivision.SplitSubdivisionBodyBuilder builder. """
    class InputBodyOptions(Enum):
        """
        Members Include: 
         |Keep|  Keep the feature as they are 
         |Hide|  Hide the features 
         |Delete|  Delete the features 

        """
        Keep: int
        Hide: int
        Delete: int
        @staticmethod
        def ValueOf(value: int) -> SplitSubdivisionBodyBuilder.InputBodyOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def InputBodyOption(self) -> SplitSubdivisionBodyBuilder.InputBodyOptions:
        """
        Getter for property: ( SplitSubdivisionBodyBuilder.InputBodyOptions NXOpen.Featur) InputBodyOption
         Returns the input body option   
            
         
        """
        pass
    @InputBodyOption.setter
    def InputBodyOption(self, inputBody: SplitSubdivisionBodyBuilder.InputBodyOptions):
        """
        Setter for property: ( SplitSubdivisionBodyBuilder.InputBodyOptions NXOpen.Featur) InputBodyOption
         Returns the input body option   
            
         
        """
        pass
    @property
    def SubdivisionBodiesToSplit(self) -> SelectSubdivisionBodyList:
        """
        Getter for property: ( SelectSubdivisionBodyList NXOpen.Featur) SubdivisionBodiesToSplit
         Returns the  Features::Subdivision::SubdivisionBody  features to split   
            
         
        """
        pass
import NXOpen
class StartSymmetricModelingBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Features.Subdivision.StartSymmetricModelingBuilder builder """
    class MirrorProcedureOption(Enum):
        """
        Members Include: 
         |CutBody|  Cuts the mesh 
         |ProjectEdge|  Projects the edges 

        """
        CutBody: int
        ProjectEdge: int
        @staticmethod
        def ValueOf(value: int) -> StartSymmetricModelingBuilder.MirrorProcedureOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def EdgesToProject(self) -> SelectCageObjectData:
        """
        Getter for property: ( SelectCageObjectData NXOpen.Featur) EdgesToProject
         Returns the edges to project   
            
         
        """
        pass
    @property
    def MirrorProcedureOptions(self) -> StartSymmetricModelingBuilder.MirrorProcedureOption:
        """
        Getter for property: ( StartSymmetricModelingBuilder.MirrorProcedureOption NXOpen.Featur) MirrorProcedureOptions
         Returns the mirror procedure options   
            
         
        """
        pass
    @MirrorProcedureOptions.setter
    def MirrorProcedureOptions(self, mirrorProcedureOptions: StartSymmetricModelingBuilder.MirrorProcedureOption):
        """
        Setter for property: ( StartSymmetricModelingBuilder.MirrorProcedureOption NXOpen.Featur) MirrorProcedureOptions
         Returns the mirror procedure options   
            
         
        """
        pass
    @property
    def Plane(self) -> NXOpen.Plane:
        """
        Getter for property: ( NXOpen.Plane) Plane
         Returns the plane   
            
         
        """
        pass
    @Plane.setter
    def Plane(self, plane: NXOpen.Plane):
        """
        Setter for property: ( NXOpen.Plane) Plane
         Returns the plane   
            
         
        """
        pass
    @property
    def SwitchSide(self) -> bool:
        """
        Getter for property: (bool) SwitchSide
         Returns the flag indicating if the mirror side should be switched   
            
         
        """
        pass
    @SwitchSide.setter
    def SwitchSide(self, switchSide: bool):
        """
        Setter for property: (bool) SwitchSide
         Returns the flag indicating if the mirror side should be switched   
            
         
        """
        pass
import NXOpen
class SubdivisionBodyCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of subdivision body feature tools. """
    @property
    def SubdivisionMeshExchange() -> SubdivisionMeshExchange:
        """
         Returns the SubdivisionMeshExchange instance belonging to this collection 
        """
        pass
    def CreateCageFromFacetBodyBuilder(self) -> CageFromFacetBodyBuilder:
        """
         Creates a NXOpen.Features.Subdivision.CageFromFacetBodyBuilder. 
         Returns builder ( CageFromFacetBodyBuilder NXOpen.Featur): .
        """
        pass
    def CreateCagePolylineBuilder(self, polyline: NXOpen.Polyline) -> CagePolylineBuilder:
        """
         Creates a NXOpen.Features.Subdivision.CagePolylineBuilder. 
         Returns builder ( CagePolylineBuilder NXOpen.Featur): .
        """
        pass
    def CreateCopyCageBuilder(self) -> CopyCageBuilder:
        """
         Creates a NXOpen.Features.Subdivision.CopyCageBuilder. 
         Returns builder ( CopyCageBuilder NXOpen.Featur): .
        """
        pass
    def CreateCopyCageData(self) -> CopyCageData:
        """
         Creates a NXOpen.Features.Subdivision.CopyCageData. 
         Returns data ( CopyCageData NXOpen.Featur): .
        """
        pass
    def CreateDefineWorkRegionBuilder(self) -> DefineWorkRegionBuilder:
        """
         Creates a NXOpen.Features.Subdivision.DefineWorkRegionBuilder. 
         Returns data ( DefineWorkRegionBuilder NXOpen.Featur): .
        """
        pass
    def CreateDeleteConstraintBuilder(self) -> DeleteConstraintBuilder:
        """
         Creates a NXOpen.Features.Subdivision.DeleteConstraintBuilder. 
         Returns builder ( DeleteConstraintBuilder NXOpen.Featur): .
        """
        pass
    def CreateDrawCageData(self) -> DrawCageData:
        """
         Creates a NXOpen.Features.Subdivision.DrawCageData. 
         Returns data ( DrawCageData NXOpen.Featur): .
        """
        pass
    def CreateEmptyCageSectionBuilder(self) -> CageSectionData:
        """
         Creates an empty cage section builder object. 
         Returns builder ( CageSectionData NXOpen.Featur): .
        """
        pass
    def CreateExportSubdivisionGeometryBuilder(self) -> ExportSubdivisionGeometryBuilder:
        """
         Creates a NXOpen.Features.Subdivision.ExportSubdivisionGeometryBuilder. 
         Returns builder ( ExportSubdivisionGeometryBuilder NXOpen.Featur): .
        """
        pass
    def CreateExtractCagePolylineBuilder(self) -> ExtractCagePolylineBuilder:
        """
         Creates a NXOpen.Features.Subdivision.ExtractCagePolylineBuilder. 
         Returns builder ( ExtractCagePolylineBuilder NXOpen.Featur): .
        """
        pass
    def CreateExtractVertexPointsBuilder(self) -> ExtractVertexPointsBuilder:
        """
         Creates a NXOpen.Features.Subdivision.ExtractVertexPointsBuilder. 
         Returns builder ( ExtractVertexPointsBuilder NXOpen.Featur): .
        """
        pass
    def CreateImportSubdivisionGeometryBuilder(self) -> ImportSubdivisionGeometryBuilder:
        """
         Creates a NXOpen.Features.Subdivision.ImportSubdivisionGeometryBuilder. 
         Returns builder ( ImportSubdivisionGeometryBuilder NXOpen.Featur): .
        """
        pass
    def CreateMergeSubdivisionBodiesBuilder(self) -> MergeSubdivisionBodiesBuilder:
        """
         Creates a NXOpen.Features.Subdivision.MergeSubdivisionBodiesBuilder. 
         Returns builder ( MergeSubdivisionBodiesBuilder NXOpen.Featur): .
        """
        pass
    def CreateMirrorCageBuilder(self) -> MirrorCageBuilder:
        """
         Creates a NXOpen.Features.Subdivision.MirrorCageBuilder. 
         Returns builder ( MirrorCageBuilder NXOpen.Featur): .
        """
        pass
    def CreateOffsetCageBuilder(self) -> OffsetCageBuilder:
        """
         Creates a NXOpen.Features.Subdivision.OffsetCageBuilder. 
         Returns builder ( OffsetCageBuilder NXOpen.Featur): .
        """
        pass
    def CreatePasteCageData(self) -> PasteCageData:
        """
         Creates a NXOpen.Features.Subdivision.PasteCageData. 
         Returns data ( PasteCageData NXOpen.Featur): .
        """
        pass
    def CreateSectionTubeData(self) -> SectionTubeData:
        """
         Creates a NXOpen.Features.Subdivision.SectionTubeData. 
         Returns data ( SectionTubeData NXOpen.Featur): .
        """
        pass
    def CreateSplitSubdivisionBodyBuilder(self) -> SplitSubdivisionBodyBuilder:
        """
         Creates a NXOpen.Features.Subdivision.SplitSubdivisionBodyBuilder. 
         Returns builder ( SplitSubdivisionBodyBuilder NXOpen.Featur): .
        """
        pass
    def CreateStartSymmetricModelingBuilder(self) -> StartSymmetricModelingBuilder:
        """
         Creates a NXOpen.Features.Subdivision.StartSymmetricModelingBuilder. 
         Returns builder ( StartSymmetricModelingBuilder NXOpen.Featur): .
        """
        pass
    def CreateSubdivisionBridgeFaceBuilder(self) -> SubdivisionBridgeFaceBuilder:
        """
         Creates a NXOpen.Features.Subdivision.SubdivisionBridgeFaceBuilder. 
         Returns builder ( SubdivisionBridgeFaceBuilder NXOpen.Featur): .
        """
        pass
    def CreateSubdivisionChamferCageBuilder(self) -> SubdivisionChamferCageBuilder:
        """
         Creates a NXOpen.Features.Subdivision.SubdivisionChamferCageBuilder. 
         Returns builder ( SubdivisionChamferCageBuilder NXOpen.Featur): .
        """
        pass
    def CreateSubdivisionConnectCageBuilder(self) -> SubdivisionConnectCageBuilder:
        """
         Creates a NXOpen.Features.Subdivision.SubdivisionConnectCageBuilder. 
         Returns builder ( SubdivisionConnectCageBuilder NXOpen.Featur): .
        """
        pass
    def CreateSubdivisionDeleteCageBuilder(self) -> SubdivisionDeleteCageBuilder:
        """
         Creates a NXOpen.Features.Subdivision.SubdivisionDeleteCageBuilder. 
         Returns builder ( SubdivisionDeleteCageBuilder NXOpen.Featur): .
        """
        pass
    def CreateSubdivisionDeleteFaceBuilder(self) -> SubdivisionDeleteFaceBuilder:
        """
         Creates a NXOpen.Features.Subdivision.SubdivisionDeleteFaceBuilder. 
         Returns builder ( SubdivisionDeleteFaceBuilder NXOpen.Featur): .
        """
        pass
    def CreateSubdivisionDeleteObjectBuilder(self) -> SubdivisionDeleteObjectBuilder:
        """
         Creates a NXOpen.Features.Subdivision.SubdivisionDeleteObjectBuilder. 
         Returns builder ( SubdivisionDeleteObjectBuilder NXOpen.Featur): .
        """
        pass
    def CreateSubdivisionExtrudeCageBuilder(self) -> SubdivisionExtrudeCageBuilder:
        """
         Creates a NXOpen.Features.Subdivision.SubdivisionExtrudeCageBuilder. 
         Returns builder ( SubdivisionExtrudeCageBuilder NXOpen.Featur): .
        """
        pass
    def CreateSubdivisionFillBuilder(self) -> SubdivisionFillBuilder:
        """
         Creates a NXOpen.Features.Subdivision.SubdivisionFillBuilder. 
         Returns builder ( SubdivisionFillBuilder NXOpen.Featur): .
        """
        pass
    def CreateSubdivisionLoftBuilder(self) -> SubdivisionLoftBuilder:
        """
         Creates a NXOpen.Features.Subdivision.SubdivisionLoftBuilder. 
         Returns builder ( SubdivisionLoftBuilder NXOpen.Featur): .
        """
        pass
    def CreateSubdivisionMergeFaceBuilder(self) -> SubdivisionMergeFaceBuilder:
        """
         Creates a NXOpen.Features.Subdivision.SubdivisionMergeFaceBuilder. 
         Returns builder ( SubdivisionMergeFaceBuilder NXOpen.Featur): .
        """
        pass
    def CreateSubdivisionPrimitiveShapeBuilder(self) -> SubdivisionPrimitiveShapeBuilder:
        """
         Creates a NXOpen.Features.Subdivision.SubdivisionPrimitiveShapeBuilder. 
         Returns builder ( SubdivisionPrimitiveShapeBuilder NXOpen.Featur): .
        """
        pass
    def CreateSubdivisionPrimitiveShapeBuilderEx(self) -> SubdivisionPrimitiveShapeBuilderEx:
        """
         Creates a NXOpen.Features.Subdivision.SubdivisionPrimitiveShapeBuilderEx. 
         Returns builder ( SubdivisionPrimitiveShapeBuilderEx NXOpen.Featur): .
        """
        pass
    def CreateSubdivisionProjectCageBuilder(self) -> SubdivisionProjectCageBuilder:
        """
         Creates a NXOpen.Features.Subdivision.SubdivisionProjectCageBuilder. 
         Returns builder ( SubdivisionProjectCageBuilder NXOpen.Featur): .
        """
        pass
    def CreateSubdivisionProjectCageBuilderEx(self) -> SubdivisionProjectCageBuilderEx:
        """
         Creates a NXOpen.Features.Subdivision.SubdivisionProjectCageBuilderEx. 
         Returns builder ( SubdivisionProjectCageBuilderEx NXOpen.Featur): .
        """
        pass
    def CreateSubdivisionRevolveBuilder(self) -> SubdivisionRevolveBuilder:
        """
         Creates a NXOpen.Features.Subdivision.SubdivisionRevolveBuilder. 
         Returns builder ( SubdivisionRevolveBuilder NXOpen.Featur): .
        """
        pass
    def CreateSubdivisionSetContinuityBuilder(self) -> SubdivisionSetContinuityBuilder:
        """
         Creates a NXOpen.Features.Subdivision.SubdivisionSetContinuityBuilder. 
         Returns builder ( SubdivisionSetContinuityBuilder NXOpen.Featur): .
        """
        pass
    def CreateSubdivisionSetWeightBuilder(self) -> SubdivisionSetWeightBuilder:
        """
         Creates a NXOpen.Features.Subdivision.SubdivisionSetWeightBuilder. 
         Returns builder ( SubdivisionSetWeightBuilder NXOpen.Featur): .
        """
        pass
    def CreateSubdivisionSewCageBuilder(self) -> SubdivisionSewCageBuilder:
        """
         Creates a NXOpen.Features.Subdivision.SubdivisionSewCageBuilder. 
         Returns builder ( SubdivisionSewCageBuilder NXOpen.Featur): .
        """
        pass
    def CreateSubdivisionSplitFaceBuilder(self) -> SubdivisionSplitFaceBuilder:
        """
         Creates a NXOpen.Features.Subdivision.SubdivisionSplitFaceBuilder. 
         Returns builder ( SubdivisionSplitFaceBuilder NXOpen.Featur): .
        """
        pass
    def CreateSubdivisionSubdivideFaceBuilder(self) -> SubdivisionSubdivideFaceBuilder:
        """
         Creates a NXOpen.Features.Subdivision.SubdivisionSubdivideFaceBuilder. 
         Returns builder ( SubdivisionSubdivideFaceBuilder NXOpen.Featur): .
        """
        pass
    def CreateSubdivisionSweepBuilder(self) -> SubdivisionSweepBuilder:
        """
         Creates a NXOpen.Features.Subdivision.SubdivisionSweepBuilder. 
         Returns builder ( SubdivisionSweepBuilder NXOpen.Featur): .
        """
        pass
    def CreateSubdivisionTubeBuilder(self) -> SubdivisionTubeBuilder:
        """
         Creates a NXOpen.Features.Subdivision.SubdivisionTubeBuilder. 
         Returns builder ( SubdivisionTubeBuilder NXOpen.Featur): .
        """
        pass
    def CreateTransformCageData(self) -> TransformCageData:
        """
         Creates a NXOpen.Features.Subdivision.TransformCageData. 
         Returns data ( TransformCageData NXOpen.Featur): .
        """
        pass
    def StopSymmetricModeling(self) -> None:
        """
         Stops the symmetric modeling. 
        """
        pass
import NXOpen.Features
class SubdivisionBody(NXOpen.Features.BodyFeature): 
    """ Represents a subdivision body feature. """
    pass
import NXOpen
class SubdivisionBridgeFaceBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Features.Subdivision.SubdivisionBridgeFaceBuilder builder.  """
    class ContinuityType(Enum):
        """
        Members Include: 
         |Smooth|  Smooth continuity 
         |Sharp|  Sharp continuity 

        """
        Smooth: int
        Sharp: int
        @staticmethod
        def ValueOf(value: int) -> SubdivisionBridgeFaceBuilder.ContinuityType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Continuity(self) -> SubdivisionBridgeFaceBuilder.ContinuityType:
        """
        Getter for property: ( SubdivisionBridgeFaceBuilder.ContinuityType NXOpen.Featur) Continuity
         Returns the continuity.  
           The continuity is used to specify creases in the limit surface corresponding to the outer
                        edges of the faces specified by  NXOpen::Features::Subdivision::SubdivisionBridgeFaceBuilder::FaceSet1  and 
                         NXOpen::Features::Subdivision::SubdivisionBridgeFaceBuilder::FaceSet2 .   
         
        """
        pass
    @Continuity.setter
    def Continuity(self, continuity: SubdivisionBridgeFaceBuilder.ContinuityType):
        """
        Setter for property: ( SubdivisionBridgeFaceBuilder.ContinuityType NXOpen.Featur) Continuity
         Returns the continuity.  
           The continuity is used to specify creases in the limit surface corresponding to the outer
                        edges of the faces specified by  NXOpen::Features::Subdivision::SubdivisionBridgeFaceBuilder::FaceSet1  and 
                         NXOpen::Features::Subdivision::SubdivisionBridgeFaceBuilder::FaceSet2 .   
         
        """
        pass
    @property
    def FaceSet1(self) -> SelectCageObjectData:
        """
        Getter for property: ( SelectCageObjectData NXOpen.Featur) FaceSet1
         Returns the first face set.  
             
         
        """
        pass
    @property
    def FaceSet2(self) -> SelectCageObjectData:
        """
        Getter for property: ( SelectCageObjectData NXOpen.Featur) FaceSet2
         Returns the second face set.  
             
         
        """
        pass
    @property
    def NumSegments(self) -> int:
        """
        Getter for property: (int) NumSegments
         Returns the number of segments in the output bridge faces   
            
         
        """
        pass
    @NumSegments.setter
    def NumSegments(self, numSegments: int):
        """
        Setter for property: (int) NumSegments
         Returns the number of segments in the output bridge faces   
            
         
        """
        pass
import NXOpen
class SubdivisionChamferCageBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Features.Subdivision.SubdivisionChamferCageBuilder builder """
    class ContinuityType(Enum):
        """
        Members Include: 
         |Smooth|  Smooth continuity 
         |Sharp|  Sharp continuity 

        """
        Smooth: int
        Sharp: int
        @staticmethod
        def ValueOf(value: int) -> SubdivisionChamferCageBuilder.ContinuityType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Continuity(self) -> SubdivisionChamferCageBuilder.ContinuityType:
        """
        Getter for property: ( SubdivisionChamferCageBuilder.ContinuityType NXOpen.Featur) Continuity
         Returns the continuity.  
             
         
        """
        pass
    @Continuity.setter
    def Continuity(self, continuity: SubdivisionChamferCageBuilder.ContinuityType):
        """
        Setter for property: ( SubdivisionChamferCageBuilder.ContinuityType NXOpen.Featur) Continuity
         Returns the continuity.  
             
         
        """
        pass
    @property
    def Distance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Distance
         Returns the distance.  
             
         
        """
        pass
    @property
    def SelectedEdges(self) -> SelectCageObjectData:
        """
        Getter for property: ( SelectCageObjectData NXOpen.Featur) SelectedEdges
         Returns the input edges   
            
         
        """
        pass
    @property
    def WeightPercent(self) -> int:
        """
        Getter for property: (int) WeightPercent
         Returns the weight.  
             
         
        """
        pass
    @WeightPercent.setter
    def WeightPercent(self, weightPercent: int):
        """
        Setter for property: (int) WeightPercent
         Returns the weight.  
             
         
        """
        pass
import NXOpen
class SubdivisionConnectCageBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Features.Subdivision.SubdivisionConnectCageBuilder builder.  """
    class ContinuityTypes(Enum):
        """
        Members Include: 
         |Smooth| 
         |Sharp| 

        """
        Smooth: int
        Sharp: int
        @staticmethod
        def ValueOf(value: int) -> SubdivisionConnectCageBuilder.ContinuityTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def CageEdgeToEdit(self) -> SelectCageObjectData:
        """
        Getter for property: ( SelectCageObjectData NXOpen.Featur) CageEdgeToEdit
         Returns the cage edge to edit   
            
         
        """
        pass
    @property
    def ContinuityType(self) -> SubdivisionConnectCageBuilder.ContinuityTypes:
        """
        Getter for property: ( SubdivisionConnectCageBuilder.ContinuityTypes NXOpen.Featur) ContinuityType
         Returns the continuity.  
             
         
        """
        pass
    @ContinuityType.setter
    def ContinuityType(self, continuityType: SubdivisionConnectCageBuilder.ContinuityTypes):
        """
        Setter for property: ( SubdivisionConnectCageBuilder.ContinuityTypes NXOpen.Featur) ContinuityType
         Returns the continuity.  
             
         
        """
        pass
    @property
    def ExternalReference(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) ExternalReference
         Returns the external edges   
            
         
        """
        pass
import NXOpen
class SubdivisionDeleteCageBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Features.Subdivision.SubdivisionDeleteCageBuilder builder.  """
    @property
    def SelectCageObject(self) -> SelectCageObjectData:
        """
        Getter for property: ( SelectCageObjectData NXOpen.Featur) SelectCageObject
         Returns the select cage object   
            
         
        """
        pass
import NXOpen
class SubdivisionDeleteFaceBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Features.Subdivision.SubdivisionDeleteFaceBuilder builder.  """
    @property
    def FaceToDelete(self) -> SelectCageObjectData:
        """
        Getter for property: ( SelectCageObjectData NXOpen.Featur) FaceToDelete
         Returns the face to delete.  
             
         
        """
        pass
import NXOpen
class SubdivisionDeleteObjectBuilder(NXOpen.Builder): 
    """ Represents a Features.Subdivision.SubdivisionDeleteObjectBuilder builder.  """
    @property
    def Objects(self) -> SelectCageObjectData:
        """
        Getter for property: ( SelectCageObjectData NXOpen.Featur) Objects
         Returns the objects to be deleted.  
             
         
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class SubdivisionExtrudeCageBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Features.Subdivision.SubdivisionExtrudeCageBuilder builder.  """
    class ContinuityType(Enum):
        """
        Members Include: 
         |Smooth|  Smooth continuity 
         |Sharp|  Sharp continuity 

        """
        Smooth: int
        Sharp: int
        @staticmethod
        def ValueOf(value: int) -> SubdivisionExtrudeCageBuilder.ContinuityType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class DirectionType(Enum):
        """
        Members Include: 
         |Inferred| 
         |Vector| 
         |Perpendicular| 

        """
        Inferred: int
        Vector: int
        Perpendicular: int
        @staticmethod
        def ValueOf(value: int) -> SubdivisionExtrudeCageBuilder.DirectionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ScalingMethodType(Enum):
        """
        Members Include: 
         |Linear|  Scale in the specified direction 
         |Planar|  Scale in the plane normal to specified direction 
         |Uniform|  Scale uniformly all the directions 

        """
        Linear: int
        Planar: int
        Uniform: int
        @staticmethod
        def ValueOf(value: int) -> SubdivisionExtrudeCageBuilder.ScalingMethodType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class TransformationMethodType(Enum):
        """
        Members Include: 
         |DragLinear|  Drag extruded topology in linear direction 
         |Transform|  Transform extruded topology  

        """
        DragLinear: int
        Transform: int
        @staticmethod
        def ValueOf(value: int) -> SubdivisionExtrudeCageBuilder.TransformationMethodType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def CanMoveToolOnly(self) -> bool:
        """
        Getter for property: (bool) CanMoveToolOnly
         Returns the flag indicating if transformer tool can be moved without transforming the selected cage topology.  
             
         
        """
        pass
    @CanMoveToolOnly.setter
    def CanMoveToolOnly(self, canMove: bool):
        """
        Setter for property: (bool) CanMoveToolOnly
         Returns the flag indicating if transformer tool can be moved without transforming the selected cage topology.  
             
         
        """
        pass
    @property
    def CanRelocateToolToSelection(self) -> bool:
        """
        Getter for property: (bool) CanRelocateToolToSelection
         Returns the flag indicating if transformer tool can be relocated based on cage topology selection.  
             
         
        """
        pass
    @CanRelocateToolToSelection.setter
    def CanRelocateToolToSelection(self, canRelocate: bool):
        """
        Setter for property: (bool) CanRelocateToolToSelection
         Returns the flag indicating if transformer tool can be relocated based on cage topology selection.  
             
         
        """
        pass
    @property
    def CanReorientToolToSelection(self) -> bool:
        """
        Getter for property: (bool) CanReorientToolToSelection
         Returns the flag indicating if transformer tool can be reoriented based on cage topology selection.  
             
         
        """
        pass
    @CanReorientToolToSelection.setter
    def CanReorientToolToSelection(self, canReorient: bool):
        """
        Setter for property: (bool) CanReorientToolToSelection
         Returns the flag indicating if transformer tool can be reoriented based on cage topology selection.  
             
         
        """
        pass
    @property
    def Continuity(self) -> SubdivisionExtrudeCageBuilder.ContinuityType:
        """
        Getter for property: ( SubdivisionExtrudeCageBuilder.ContinuityType NXOpen.Featur) Continuity
         Returns the continuity.  
           The continuity is used to specify creases in the limit surface corresponding to the outer
                        edges of the faces or boundary edges specified by  NXOpen::Features::Subdivision::SubdivisionExtrudeCageBuilder::SelectionObject .   
         
        """
        pass
    @Continuity.setter
    def Continuity(self, continuity: SubdivisionExtrudeCageBuilder.ContinuityType):
        """
        Setter for property: ( SubdivisionExtrudeCageBuilder.ContinuityType NXOpen.Featur) Continuity
         Returns the continuity.  
           The continuity is used to specify creases in the limit surface corresponding to the outer
                        edges of the faces or boundary edges specified by  NXOpen::Features::Subdivision::SubdivisionExtrudeCageBuilder::SelectionObject .   
         
        """
        pass
    @property
    def DirectionOption(self) -> SubdivisionExtrudeCageBuilder.DirectionType:
        """
        Getter for property: ( SubdivisionExtrudeCageBuilder.DirectionType NXOpen.Featur) DirectionOption
         Returns the direction option   
            
         
        """
        pass
    @DirectionOption.setter
    def DirectionOption(self, directionOption: SubdivisionExtrudeCageBuilder.DirectionType):
        """
        Setter for property: ( SubdivisionExtrudeCageBuilder.DirectionType NXOpen.Featur) DirectionOption
         Returns the direction option   
            
         
        """
        pass
    @property
    def Distance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Distance
         Returns the distance.  
             
         
        """
        pass
    @property
    def NumberOfSegments(self) -> int:
        """
        Getter for property: (int) NumberOfSegments
         Returns the number of segments.  
             
         
        """
        pass
    @NumberOfSegments.setter
    def NumberOfSegments(self, numOfSegments: int):
        """
        Setter for property: (int) NumberOfSegments
         Returns the number of segments.  
             
         
        """
        pass
    @property
    def ScalingMethod(self) -> SubdivisionExtrudeCageBuilder.ScalingMethodType:
        """
        Getter for property: ( SubdivisionExtrudeCageBuilder.ScalingMethodType NXOpen.Featur) ScalingMethod
         Returns the scaling method.  
             
         
        """
        pass
    @ScalingMethod.setter
    def ScalingMethod(self, scalingMethod: SubdivisionExtrudeCageBuilder.ScalingMethodType):
        """
        Setter for property: ( SubdivisionExtrudeCageBuilder.ScalingMethodType NXOpen.Featur) ScalingMethod
         Returns the scaling method.  
             
         
        """
        pass
    @property
    def SelectionObject(self) -> SelectCageObjectData:
        """
        Getter for property: ( SelectCageObjectData NXOpen.Featur) SelectionObject
         Returns the selection object.  
             
         
        """
        pass
    @property
    def TransformationMethod(self) -> SubdivisionExtrudeCageBuilder.TransformationMethodType:
        """
        Getter for property: ( SubdivisionExtrudeCageBuilder.TransformationMethodType NXOpen.Featur) TransformationMethod
         Returns the transformation method.  
             
         
        """
        pass
    @TransformationMethod.setter
    def TransformationMethod(self, method: SubdivisionExtrudeCageBuilder.TransformationMethodType):
        """
        Setter for property: ( SubdivisionExtrudeCageBuilder.TransformationMethodType NXOpen.Featur) TransformationMethod
         Returns the transformation method.  
             
         
        """
        pass
    @property
    def Transformer(self) -> NXOpen.GeometricUtilities.TransformerData:
        """
        Getter for property: ( NXOpen.GeometricUtilities.TransformerData) Transformer
         Returns the transformation tool.  
             
         
        """
        pass
    @property
    def Vector(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) Vector
         Returns the vector for extrude.  
             
         
        """
        pass
    @Vector.setter
    def Vector(self, vector: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) Vector
         Returns the vector for extrude.  
             
         
        """
        pass
    def Extrude(self) -> None:
        """
         Perform extrude operation. 
        """
        pass
import NXOpen
class SubdivisionFillBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Features.Subdivision.SubdivisionFillBuilder builder.  """
    class ContinuityType(Enum):
        """
        Members Include: 
         |Smooth|  Smooth continuity 
         |Sharp|  Sharp continuity 

        """
        Smooth: int
        Sharp: int
        @staticmethod
        def ValueOf(value: int) -> SubdivisionFillBuilder.ContinuityType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def CanConnectSymmetrically(self) -> bool:
        """
        Getter for property: (bool) CanConnectSymmetrically
         Returns the flag indicating if selected edges are to be connected with their symmetric counterpart.  
             
         
        """
        pass
    @CanConnectSymmetrically.setter
    def CanConnectSymmetrically(self, connectSymmetrically: bool):
        """
        Setter for property: (bool) CanConnectSymmetrically
         Returns the flag indicating if selected edges are to be connected with their symmetric counterpart.  
             
         
        """
        pass
    @property
    def Continuity(self) -> SubdivisionFillBuilder.ContinuityType:
        """
        Getter for property: ( SubdivisionFillBuilder.ContinuityType NXOpen.Featur) Continuity
         Returns the continuity.  
           The continuity is used to specify creases in the limit surface corresponding to edges
                        specified by  NXOpen::Features::Subdivision::SubdivisionFillBuilder::SelectedEdges .   
         
        """
        pass
    @Continuity.setter
    def Continuity(self, continuity: SubdivisionFillBuilder.ContinuityType):
        """
        Setter for property: ( SubdivisionFillBuilder.ContinuityType NXOpen.Featur) Continuity
         Returns the continuity.  
           The continuity is used to specify creases in the limit surface corresponding to edges
                        specified by  NXOpen::Features::Subdivision::SubdivisionFillBuilder::SelectedEdges .   
         
        """
        pass
    @property
    def SelectedEdges(self) -> SelectCageObjectData:
        """
        Getter for property: ( SelectCageObjectData NXOpen.Featur) SelectedEdges
         Returns the edges to form a face.  
             
         
        """
        pass
import NXOpen
class SubdivisionLoftBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Features.Subdivision.SubdivisionLoftBuilder builder. """
    class ContinuityType(Enum):
        """
        Members Include: 
         |Smooth|  Smooth continuity 
         |Sharp|  Sharp continuity 

        """
        Smooth: int
        Sharp: int
        @staticmethod
        def ValueOf(value: int) -> SubdivisionLoftBuilder.ContinuityType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def CanSew(self) -> bool:
        """
        Getter for property: (bool) CanSew
         Returns the value indicating if open edges of the loft mesh can be sewn with selected input open edges.  
            
         
        """
        pass
    @CanSew.setter
    def CanSew(self, canSew: bool):
        """
        Setter for property: (bool) CanSew
         Returns the value indicating if open edges of the loft mesh can be sewn with selected input open edges.  
            
         
        """
        pass
    @property
    def Continuity(self) -> SubdivisionLoftBuilder.ContinuityType:
        """
        Getter for property: ( SubdivisionLoftBuilder.ContinuityType NXOpen.Featur) Continuity
         Returns the continuity.  
           The continuity is used to specify creases in the limit surface corresponding to edges
                        of the lofted region that are sewn with the primary existing region.   
         
        """
        pass
    @Continuity.setter
    def Continuity(self, continuity: SubdivisionLoftBuilder.ContinuityType):
        """
        Setter for property: ( SubdivisionLoftBuilder.ContinuityType NXOpen.Featur) Continuity
         Returns the continuity.  
           The continuity is used to specify creases in the limit surface corresponding to edges
                        of the lofted region that are sewn with the primary existing region.   
         
        """
        pass
    @property
    def IsClosed(self) -> bool:
        """
        Getter for property: (bool) IsClosed
         Returns the value indicating if the output mesh is closed.  
            
         
        """
        pass
    @IsClosed.setter
    def IsClosed(self, isClosed: bool):
        """
        Setter for property: (bool) IsClosed
         Returns the value indicating if the output mesh is closed.  
            
         
        """
        pass
    @property
    def NumberOfSegments(self) -> int:
        """
        Getter for property: (int) NumberOfSegments
         Returns the number of segments   
            
         
        """
        pass
    @NumberOfSegments.setter
    def NumberOfSegments(self, numberOfSegments: int):
        """
        Setter for property: (int) NumberOfSegments
         Returns the number of segments   
            
         
        """
        pass
    @property
    def Sections(self) -> CageSectionDataList:
        """
        Getter for property: ( CageSectionDataList NXOpen.Featur) Sections
         Returns the section objects for lofting   
            
         
        """
        pass
import NXOpen
class SubdivisionMergeFaceBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Features.Subdivision.SubdivisionMergeFaceBuilder builder.  """
    @property
    def FacesToMerge(self) -> SelectCageObjectData:
        """
        Getter for property: ( SelectCageObjectData NXOpen.Featur) FacesToMerge
         Returns the faces to merge.  
             
         
        """
        pass
import NXOpen
class SubdivisionMeshExchange(NXOpen.Object): 
    """ Represents a class that facilitates subdivision mesh data exchange """
    class Unit(Enum):
        """
        Members Include: 
         |Default|  Unit of vertex coordinates is same as work part unit 
         |Millimeter| 
         |Inch| 
         |Meter| 
         |Centimeter| 
         |Foot| 
         |Micrometer| 

        """
        Default: int
        Millimeter: int
        Inch: int
        Meter: int
        Centimeter: int
        Foot: int
        Micrometer: int
        @staticmethod
        def ValueOf(value: int) -> SubdivisionMeshExchange.Unit:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ExportOptions:
        """
         Subdivision body export options 
         SubdivisionMeshExchangeExportOptions_Struct NXOpen.Featur is an alias for  SubdivisionMeshExchange.ExportOptions NXOpen.Featur.
        """
        @property
        def Unit(self) -> SubdivisionMeshExchange.Unit:
            """
            Getter for property Unit
            Unit of output mesh vertex positions

            """
            pass
        @Unit.setter
        def Unit(self, value: SubdivisionMeshExchange.Unit):
            """
            Getter for property Unit
            Unit of output mesh vertex positions
            Setter for property Unit
            Unit of output mesh vertex positions

            """
            pass
    class ImportOptions:
        """
         Subdivision body import options 
         SubdivisionMeshExchangeImportOptions_Struct NXOpen.Featur is an alias for  SubdivisionMeshExchange.ImportOptions NXOpen.Featur.
        """
        @property
        def Part(self) -> NXOpen.Part:
            """
            Getter for property Part
            Optional, part context to create new geometry in.

            """
            pass
        @Part.setter
        def Part(self, value: NXOpen.Part):
            """
            Getter for property Part
            Optional, part context to create new geometry in.
            Setter for property Part
            Optional, part context to create new geometry in.

            """
            pass
        @property
        def Unit(self) -> SubdivisionMeshExchange.Unit:
            """
            Getter for property Unit
            Unit of input mesh vertex positions

            """
            pass
        @Unit.setter
        def Unit(self, value: SubdivisionMeshExchange.Unit):
            """
            Getter for property Unit
            Unit of input mesh vertex positions
            Setter for property Unit
            Unit of input mesh vertex positions

            """
            pass
        @property
        def CreateSingleFeature(self) -> bool:
            """
            Getter for property CreateSingleFeature
            Flag inidicating if single feature is created for                                                 all the disjoint regions of the cage.

            """
            pass
        @CreateSingleFeature.setter
        def CreateSingleFeature(self, value: bool):
            """
            Getter for property CreateSingleFeature
            Flag inidicating if single feature is created for                                                 all the disjoint regions of the cage.
            Setter for property CreateSingleFeature
            Flag inidicating if single feature is created for                                                 all the disjoint regions of the cage.

            """
            pass
        @property
        def MergeSubdivisionBodyFacesIfPossible(self) -> bool:
            """
            Getter for property MergeSubdivisionBodyFacesIfPossible
            Flag inidicating if Subdivision Body faces                                                                 should be merged.

            """
            pass
        @MergeSubdivisionBodyFacesIfPossible.setter
        def MergeSubdivisionBodyFacesIfPossible(self, value: bool):
            """
            Getter for property MergeSubdivisionBodyFacesIfPossible
            Flag inidicating if Subdivision Body faces                                                                 should be merged.
            Setter for property MergeSubdivisionBodyFacesIfPossible
            Flag inidicating if Subdivision Body faces                                                                 should be merged.

            """
            pass
    def ExportMesh(self, subdivisionBody: SubdivisionBody, options: SubdivisionMeshExchange.ExportOptions) -> NXOpen.SubdivisionMeshBodyTopologyData:
        """
         Ouputs Subdivision Body feature mesh data 
         Returns meshTopoData ( NXOpen.SubdivisionMeshBodyTopologyData): .
        """
        pass
    def ImportMesh(self, meshTopoData: NXOpen.SubdivisionMeshBodyTopologyData, options: SubdivisionMeshExchange.ImportOptions) -> List[SubdivisionBody]:
        """
         Creates a Subdivision Body feature 
         Returns subdivisionBodies ( SubdivisionBody List[NXOpen.Feat):  .
        """
        pass
    def NewMeshBodyTopoData(self) -> NXOpen.SubdivisionMeshBodyTopologyData:
        """
         Constructs new empty SubdivisionMeshBodyTopologyData 
         Returns meshTopoData ( NXOpen.SubdivisionMeshBodyTopologyData): .
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class SubdivisionPrimitiveShapeBuilderEx(NXOpen.Builder): 
    """ Represents a Features.Subdivision.SubdivisionPrimitiveShapeBuilderEx builder. """
    class SphereSubdivisionLevel(Enum):
        """
        Members Include: 
         |Base| 
         |First| 
         |Second| 

        """
        Base: int
        First: int
        Second: int
        @staticmethod
        def ValueOf(value: int) -> SubdivisionPrimitiveShapeBuilderEx.SphereSubdivisionLevel:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Types(Enum):
        """
        Members Include: 
         |Sphere| 
         |Cylinder| 
         |Block| 
         |Circle| 
         |Rectangle| 
         |Torus| 

        """
        Sphere: int
        Cylinder: int
        Block: int
        Circle: int
        Rectangle: int
        Torus: int
        @staticmethod
        def ValueOf(value: int) -> SubdivisionPrimitiveShapeBuilderEx.Types:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def CircularSegments(self) -> int:
        """
        Getter for property: (int) CircularSegments
         Returns the number of segments in circular direction.  
             
         
        """
        pass
    @CircularSegments.setter
    def CircularSegments(self, numSegments: int):
        """
        Setter for property: (int) CircularSegments
         Returns the number of segments in circular direction.  
             
         
        """
        pass
    @property
    def Height(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Height
         Returns the height.  
             
         
        """
        pass
    @property
    def HeightZ(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) HeightZ
         Returns the height in Z direction.  
             
         
        """
        pass
    @property
    def InnerSize(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) InnerSize
         Returns the inner size of torus.  
             
         
        """
        pass
    @property
    def LengthX(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) LengthX
         Returns the length in X direction.  
             
         
        """
        pass
    @property
    def LinearSegments(self) -> int:
        """
        Getter for property: (int) LinearSegments
         Returns the number of segments in linear direction.  
             
         
        """
        pass
    @LinearSegments.setter
    def LinearSegments(self, numSegments: int):
        """
        Setter for property: (int) LinearSegments
         Returns the number of segments in linear direction.  
             
         
        """
        pass
    @property
    def Origin(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) Origin
         Returns the origin.  
             
         
        """
        pass
    @Origin.setter
    def Origin(self, origin: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) Origin
         Returns the origin.  
             
         
        """
        pass
    @property
    def OuterSize(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) OuterSize
         Returns the outer size of torus.  
             
         
        """
        pass
    @property
    def RadialSegments(self) -> int:
        """
        Getter for property: (int) RadialSegments
         Returns the number of segments in radial direction.  
             
         
        """
        pass
    @RadialSegments.setter
    def RadialSegments(self, numSegments: int):
        """
        Setter for property: (int) RadialSegments
         Returns the number of segments in radial direction.  
             
         
        """
        pass
    @property
    def Size(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Size
         Returns the size.  
             
         
        """
        pass
    @property
    def SphereSubdivisionLevelOption(self) -> SubdivisionPrimitiveShapeBuilderEx.SphereSubdivisionLevel:
        """
        Getter for property: ( SubdivisionPrimitiveShapeBuilderEx.SphereSubdivisionLevel NXOpen.Featur) SphereSubdivisionLevelOption
         Returns the subdivision level.  
             
         
        """
        pass
    @SphereSubdivisionLevelOption.setter
    def SphereSubdivisionLevelOption(self, level: SubdivisionPrimitiveShapeBuilderEx.SphereSubdivisionLevel):
        """
        Setter for property: ( SubdivisionPrimitiveShapeBuilderEx.SphereSubdivisionLevel NXOpen.Featur) SphereSubdivisionLevelOption
         Returns the subdivision level.  
             
         
        """
        pass
    @property
    def Transformer(self) -> NXOpen.GeometricUtilities.TransformerData:
        """
        Getter for property: ( NXOpen.GeometricUtilities.TransformerData) Transformer
         Returns the transformation tool.  
             
         
        """
        pass
    @property
    def Type(self) -> SubdivisionPrimitiveShapeBuilderEx.Types:
        """
        Getter for property: ( SubdivisionPrimitiveShapeBuilderEx.Types NXOpen.Featur) Type
         Returns the type.  
             
         
        """
        pass
    @Type.setter
    def Type(self, type: SubdivisionPrimitiveShapeBuilderEx.Types):
        """
        Setter for property: ( SubdivisionPrimitiveShapeBuilderEx.Types NXOpen.Featur) Type
         Returns the type.  
             
         
        """
        pass
    @property
    def WidthY(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) WidthY
         Returns the width in Y direction.  
             
         
        """
        pass
    @property
    def XSegments(self) -> int:
        """
        Getter for property: (int) XSegments
         Returns the number of segments in X direction.  
             
         
        """
        pass
    @XSegments.setter
    def XSegments(self, numSegments: int):
        """
        Setter for property: (int) XSegments
         Returns the number of segments in X direction.  
             
         
        """
        pass
    @property
    def YSegments(self) -> int:
        """
        Getter for property: (int) YSegments
         Returns the number of segments in Y direction.  
             
         
        """
        pass
    @YSegments.setter
    def YSegments(self, numSegments: int):
        """
        Setter for property: (int) YSegments
         Returns the number of segments in Y direction.  
             
         
        """
        pass
    @property
    def ZSegments(self) -> int:
        """
        Getter for property: (int) ZSegments
         Returns the number of segments in Z direction.  
             
         
        """
        pass
    @ZSegments.setter
    def ZSegments(self, numSegments: int):
        """
        Setter for property: (int) ZSegments
         Returns the number of segments in Z direction.  
             
         
        """
        pass
    def UpdateMesh(self) -> None:
        """
         Updates the mesh data after changes in the origin. 
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class SubdivisionPrimitiveShapeBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Features.Subdivision.SubdivisionPrimitiveShapeBuilder builder. """
    class Types(Enum):
        """
        Members Include: 
         |Sphere| 
         |Cylinder| 
         |Block| 
         |Circle| 
         |Rectangle| 
         |Torus| 

        """
        Sphere: int
        Cylinder: int
        Block: int
        Circle: int
        Rectangle: int
        Torus: int
        @staticmethod
        def ValueOf(value: int) -> SubdivisionPrimitiveShapeBuilder.Types:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def CircularSegments(self) -> int:
        """
        Getter for property: (int) CircularSegments
         Returns the number of segments in circular sectional direction of torus.  
             
         
        """
        pass
    @CircularSegments.setter
    def CircularSegments(self, numSegments: int):
        """
        Setter for property: (int) CircularSegments
         Returns the number of segments in circular sectional direction of torus.  
             
         
        """
        pass
    @property
    def Height(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Height
         Returns the height.  
             
         
        """
        pass
    @property
    def HeightZ(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) HeightZ
         Returns the height in z direction.  
             
         
        """
        pass
    @property
    def InnerSize(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) InnerSize
         Returns the inner size of torus.  
             
         
        """
        pass
    @property
    def LengthX(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) LengthX
         Returns the length in x direction.  
             
         
        """
        pass
    @property
    def Origin(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) Origin
         Returns the origin.  
             
         
        """
        pass
    @Origin.setter
    def Origin(self, origin: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) Origin
         Returns the origin.  
             
         
        """
        pass
    @property
    def OuterSize(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) OuterSize
         Returns the outer size of torus.  
             
         
        """
        pass
    @property
    def RadialSegments(self) -> int:
        """
        Getter for property: (int) RadialSegments
         Returns the number of segments in radial direction of torus.  
             
         
        """
        pass
    @RadialSegments.setter
    def RadialSegments(self, numSegments: int):
        """
        Setter for property: (int) RadialSegments
         Returns the number of segments in radial direction of torus.  
             
         
        """
        pass
    @property
    def Size(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Size
         Returns the size.  
             
         
        """
        pass
    @property
    def Transformer(self) -> NXOpen.GeometricUtilities.TransformerData:
        """
        Getter for property: ( NXOpen.GeometricUtilities.TransformerData) Transformer
         Returns the transformation tool.  
             
         
        """
        pass
    @property
    def Type(self) -> SubdivisionPrimitiveShapeBuilder.Types:
        """
        Getter for property: ( SubdivisionPrimitiveShapeBuilder.Types NXOpen.Featur) Type
         Returns the type.  
             
         
        """
        pass
    @Type.setter
    def Type(self, type: SubdivisionPrimitiveShapeBuilder.Types):
        """
        Setter for property: ( SubdivisionPrimitiveShapeBuilder.Types NXOpen.Featur) Type
         Returns the type.  
             
         
        """
        pass
    @property
    def WidthY(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) WidthY
         Returns the width in y direction.  
             
         
        """
        pass
    def UpdateMesh(self) -> None:
        """
         Updates the mesh data after changes in the origin. 
        """
        pass
import NXOpen
class SubdivisionProjectCageBuilderEx(NXOpen.Builder): 
    """ Represents a NXOpen.Features.Subdivision.SubdivisionProjectCageBuilderEx builder """
    class ModeOptions(Enum):
        """
        Members Include: 
         |Linear|  Fit a line 
         |Planar|  Fit a plane 

        """
        Linear: int
        Planar: int
        @staticmethod
        def ValueOf(value: int) -> SubdivisionProjectCageBuilderEx.ModeOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ProjectionDirectionTypes(Enum):
        """
        Members Include: 
         |AlongNormal|  Along normal 
         |AlongVector|  Along vector 

        """
        AlongNormal: int
        AlongVector: int
        @staticmethod
        def ValueOf(value: int) -> SubdivisionProjectCageBuilderEx.ProjectionDirectionTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class TargetTypes(Enum):
        """
        Members Include: 
         |InferredPlane|  Plane inferred from selected cage objects 
         |InferredAxis|  Axis inferred from selected cage objects 
         |DynamicPlane|  XY plane of a coordinate system 
         |Plane| 
         |Axis| 
         |Curve| 
         |Face| 

        """
        InferredPlane: int
        InferredAxis: int
        DynamicPlane: int
        Plane: int
        Axis: int
        Curve: int
        Face: int
        @staticmethod
        def ValueOf(value: int) -> SubdivisionProjectCageBuilderEx.TargetTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Types(Enum):
        """
        Members Include: 
         |ToTarget|  Project on target 
         |ToAverage|  Project using best fit plane or axis 
         |AlignNormal|  Align edges normal to the specified plane 

        """
        ToTarget: int
        ToAverage: int
        AlignNormal: int
        @staticmethod
        def ValueOf(value: int) -> SubdivisionProjectCageBuilderEx.Types:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Mode(self) -> SubdivisionProjectCageBuilderEx.ModeOptions:
        """
        Getter for property: ( SubdivisionProjectCageBuilderEx.ModeOptions NXOpen.Featur) Mode
         Returns the mode   
            
         
        """
        pass
    @Mode.setter
    def Mode(self, mode: SubdivisionProjectCageBuilderEx.ModeOptions):
        """
        Setter for property: ( SubdivisionProjectCageBuilderEx.ModeOptions NXOpen.Featur) Mode
         Returns the mode   
            
         
        """
        pass
    @property
    def ObjectsToProject(self) -> SelectCageObjectData:
        """
        Getter for property: ( SelectCageObjectData NXOpen.Featur) ObjectsToProject
         Returns the objects to project   
            
         
        """
        pass
    @property
    def ProjectBothSides(self) -> bool:
        """
        Getter for property: (bool) ProjectBothSides
         Returns the flag indicating if projection should be done in both the sides of vector direction.  
             
         
        """
        pass
    @ProjectBothSides.setter
    def ProjectBothSides(self, projectBothSides: bool):
        """
        Setter for property: (bool) ProjectBothSides
         Returns the flag indicating if projection should be done in both the sides of vector direction.  
             
         
        """
        pass
    @property
    def ProjectionDirectionType(self) -> SubdivisionProjectCageBuilderEx.ProjectionDirectionTypes:
        """
        Getter for property: ( SubdivisionProjectCageBuilderEx.ProjectionDirectionTypes NXOpen.Featur) ProjectionDirectionType
         Returns the type of projection on faces and facet body   
            
         
        """
        pass
    @ProjectionDirectionType.setter
    def ProjectionDirectionType(self, type: SubdivisionProjectCageBuilderEx.ProjectionDirectionTypes):
        """
        Setter for property: ( SubdivisionProjectCageBuilderEx.ProjectionDirectionTypes NXOpen.Featur) ProjectionDirectionType
         Returns the type of projection on faces and facet body   
            
         
        """
        pass
    @property
    def ProjectionVector(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) ProjectionVector
         Returns the projection direction vector   
            
         
        """
        pass
    @ProjectionVector.setter
    def ProjectionVector(self, vector: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) ProjectionVector
         Returns the projection direction vector   
            
         
        """
        pass
    @property
    def TargetAxis(self) -> NXOpen.Axis:
        """
        Getter for property: ( NXOpen.Axis) TargetAxis
         Returns the target axis   
            
         
        """
        pass
    @TargetAxis.setter
    def TargetAxis(self, axis: NXOpen.Axis):
        """
        Setter for property: ( NXOpen.Axis) TargetAxis
         Returns the target axis   
            
         
        """
        pass
    @property
    def TargetCageObjects(self) -> SelectCageObjectData:
        """
        Getter for property: ( SelectCageObjectData NXOpen.Featur) TargetCageObjects
         Returns the target cage objects to infer a plane or axis from   
            
         
        """
        pass
    @property
    def TargetCurves(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: ( NXOpen.SelectDisplayableObjectList) TargetCurves
         Returns the target curves   
            
         
        """
        pass
    @property
    def TargetDynamicPlane(self) -> NXOpen.CoordinateSystem:
        """
        Getter for property: ( NXOpen.CoordinateSystem) TargetDynamicPlane
         Returns the target dynamic plane   
            
         
        """
        pass
    @TargetDynamicPlane.setter
    def TargetDynamicPlane(self, csys: NXOpen.CoordinateSystem):
        """
        Setter for property: ( NXOpen.CoordinateSystem) TargetDynamicPlane
         Returns the target dynamic plane   
            
         
        """
        pass
    @property
    def TargetFaces(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: ( NXOpen.SelectDisplayableObjectList) TargetFaces
         Returns the target faces or facet body   
            
         
        """
        pass
    @property
    def TargetPlane(self) -> NXOpen.Plane:
        """
        Getter for property: ( NXOpen.Plane) TargetPlane
         Returns the target plane   
            
         
        """
        pass
    @TargetPlane.setter
    def TargetPlane(self, plane: NXOpen.Plane):
        """
        Setter for property: ( NXOpen.Plane) TargetPlane
         Returns the target plane   
            
         
        """
        pass
    @property
    def TargetType(self) -> SubdivisionProjectCageBuilderEx.TargetTypes:
        """
        Getter for property: ( SubdivisionProjectCageBuilderEx.TargetTypes NXOpen.Featur) TargetType
         Returns the target type   
            
         
        """
        pass
    @TargetType.setter
    def TargetType(self, targetType: SubdivisionProjectCageBuilderEx.TargetTypes):
        """
        Setter for property: ( SubdivisionProjectCageBuilderEx.TargetTypes NXOpen.Featur) TargetType
         Returns the target type   
            
         
        """
        pass
    @property
    def Type(self) -> SubdivisionProjectCageBuilderEx.Types:
        """
        Getter for property: ( SubdivisionProjectCageBuilderEx.Types NXOpen.Featur) Type
         Returns the type   
            
         
        """
        pass
    @Type.setter
    def Type(self, type: SubdivisionProjectCageBuilderEx.Types):
        """
        Setter for property: ( SubdivisionProjectCageBuilderEx.Types NXOpen.Featur) Type
         Returns the type   
            
         
        """
        pass
    def OnTargetAxis(self) -> None:
        """
         Update builder data based on target axis definition 
        """
        pass
    def OnTargetDynamicPlane(self) -> None:
        """
         Update builder data based on target dynamic plane definition 
        """
        pass
    def OnTargetPlane(self) -> None:
        """
         Update builder data based on target plane definition 
        """
        pass
import NXOpen
class SubdivisionProjectCageBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Features.Subdivision.SubdivisionProjectCageBuilder builder """
    class ModeOptions(Enum):
        """
        Members Include: 
         |Linear|  Fit a line 
         |Planar|  Fit a plane 

        """
        Linear: int
        Planar: int
        @staticmethod
        def ValueOf(value: int) -> SubdivisionProjectCageBuilder.ModeOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class TargetTypes(Enum):
        """
        Members Include: 
         |InferredPlane| 
         |InferredAxis| 
         |YcZcPlane| 
         |XcZcPlane| 
         |XcYcPlane| 
         |XcAxis| 
         |YcAxis| 
         |ZcAxis| 
         |Object| 
         |Plane| 
         |DynamicPlane| 

        """
        InferredPlane: int
        InferredAxis: int
        YcZcPlane: int
        XcZcPlane: int
        XcYcPlane: int
        XcAxis: int
        YcAxis: int
        ZcAxis: int
        Object: int
        Plane: int
        DynamicPlane: int
        @staticmethod
        def ValueOf(value: int) -> SubdivisionProjectCageBuilder.TargetTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Types(Enum):
        """
        Members Include: 
         |ToTarget|  Project on target 
         |ToAverage|  Project using best fit plane or axis 
         |AlignNormal|  Align edges normal to the specified plane 

        """
        ToTarget: int
        ToAverage: int
        AlignNormal: int
        @staticmethod
        def ValueOf(value: int) -> SubdivisionProjectCageBuilder.Types:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Mode(self) -> SubdivisionProjectCageBuilder.ModeOptions:
        """
        Getter for property: ( SubdivisionProjectCageBuilder.ModeOptions NXOpen.Featur) Mode
         Returns the mode   
            
         
        """
        pass
    @Mode.setter
    def Mode(self, mode: SubdivisionProjectCageBuilder.ModeOptions):
        """
        Setter for property: ( SubdivisionProjectCageBuilder.ModeOptions NXOpen.Featur) Mode
         Returns the mode   
            
         
        """
        pass
    @property
    def ObjectsToProject(self) -> SelectCageObjectData:
        """
        Getter for property: ( SelectCageObjectData NXOpen.Featur) ObjectsToProject
         Returns the objects to project   
            
         
        """
        pass
    @property
    def Target(self) -> NXOpen.SelectDisplayableObject:
        """
        Getter for property: ( NXOpen.SelectDisplayableObject) Target
         Returns the target   
            
         
        """
        pass
    @property
    def TargetCageObjects(self) -> SelectCageObjectData:
        """
        Getter for property: ( SelectCageObjectData NXOpen.Featur) TargetCageObjects
         Returns the target cage objects to infer a plane or axis from   
            
         
        """
        pass
    @property
    def TargetDynamicPlane(self) -> NXOpen.CoordinateSystem:
        """
        Getter for property: ( NXOpen.CoordinateSystem) TargetDynamicPlane
         Returns the target dynamic plane   
            
         
        """
        pass
    @TargetDynamicPlane.setter
    def TargetDynamicPlane(self, csys: NXOpen.CoordinateSystem):
        """
        Setter for property: ( NXOpen.CoordinateSystem) TargetDynamicPlane
         Returns the target dynamic plane   
            
         
        """
        pass
    @property
    def TargetPlane(self) -> NXOpen.Plane:
        """
        Getter for property: ( NXOpen.Plane) TargetPlane
         Returns the target plane   
            
         
        """
        pass
    @TargetPlane.setter
    def TargetPlane(self, plane: NXOpen.Plane):
        """
        Setter for property: ( NXOpen.Plane) TargetPlane
         Returns the target plane   
            
         
        """
        pass
    @property
    def TargetType(self) -> SubdivisionProjectCageBuilder.TargetTypes:
        """
        Getter for property: ( SubdivisionProjectCageBuilder.TargetTypes NXOpen.Featur) TargetType
         Returns the target type   
            
         
        """
        pass
    @TargetType.setter
    def TargetType(self, targetType: SubdivisionProjectCageBuilder.TargetTypes):
        """
        Setter for property: ( SubdivisionProjectCageBuilder.TargetTypes NXOpen.Featur) TargetType
         Returns the target type   
            
         
        """
        pass
    @property
    def Type(self) -> SubdivisionProjectCageBuilder.Types:
        """
        Getter for property: ( SubdivisionProjectCageBuilder.Types NXOpen.Featur) Type
         Returns the type   
            
         
        """
        pass
    @Type.setter
    def Type(self, type: SubdivisionProjectCageBuilder.Types):
        """
        Setter for property: ( SubdivisionProjectCageBuilder.Types NXOpen.Featur) Type
         Returns the type   
            
         
        """
        pass
    def OnTargetDynamicPlane(self) -> None:
        """
         Update builder data based on target dynamic plane definition 
        """
        pass
    def OnTargetPlane(self) -> None:
        """
         Update builder data based on target plane definition 
        """
        pass
import NXOpen
class SubdivisionRevolveBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Features.Subdivision.SubdivisionRevolveBuilder builder. """
    class ContinuityType(Enum):
        """
        Members Include: 
         |Smooth|  Smooth continuity 
         |Sharp|  Sharp continuity 

        """
        Smooth: int
        Sharp: int
        @staticmethod
        def ValueOf(value: int) -> SubdivisionRevolveBuilder.ContinuityType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AxisPoint(self) -> NXOpen.SelectNXObject:
        """
        Getter for property: ( NXOpen.SelectNXObject) AxisPoint
         Returns the origin of the axis of revolution.  
             
         
        """
        pass
    @property
    def AxisVector(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) AxisVector
         Returns the axis of revolution.  
             
         
        """
        pass
    @AxisVector.setter
    def AxisVector(self, axisVector: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) AxisVector
         Returns the axis of revolution.  
             
         
        """
        pass
    @property
    def CanSew(self) -> bool:
        """
        Getter for property: (bool) CanSew
         Returns the value indicating if open edges of the revolve mesh can be sewn with selected input open edges.  
            
         
        """
        pass
    @CanSew.setter
    def CanSew(self, canSew: bool):
        """
        Setter for property: (bool) CanSew
         Returns the value indicating if open edges of the revolve mesh can be sewn with selected input open edges.  
            
         
        """
        pass
    @property
    def Continuity(self) -> SubdivisionRevolveBuilder.ContinuityType:
        """
        Getter for property: ( SubdivisionRevolveBuilder.ContinuityType NXOpen.Featur) Continuity
         Returns the continuity.  
           The continuity is used to specify creases in the limit surface corresponding to edges
                        of the revolved region that are sewn with the primary existing region.   
         
        """
        pass
    @Continuity.setter
    def Continuity(self, continuity: SubdivisionRevolveBuilder.ContinuityType):
        """
        Setter for property: ( SubdivisionRevolveBuilder.ContinuityType NXOpen.Featur) Continuity
         Returns the continuity.  
           The continuity is used to specify creases in the limit surface corresponding to edges
                        of the revolved region that are sewn with the primary existing region.   
         
        """
        pass
    @property
    def EndAngle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) EndAngle
         Returns the end of angular dimension.  
             
         
        """
        pass
    @property
    def NumOfSegments(self) -> int:
        """
        Getter for property: (int) NumOfSegments
         Returns the number of segments.  
             
         
        """
        pass
    @NumOfSegments.setter
    def NumOfSegments(self, numOfSegments: int):
        """
        Setter for property: (int) NumOfSegments
         Returns the number of segments.  
             
         
        """
        pass
    @property
    def SectionObject(self) -> SelectCageObjectData:
        """
        Getter for property: ( SelectCageObjectData NXOpen.Featur) SectionObject
         Returns the section as revolving profile.  
             
         
        """
        pass
    @property
    def StartAngle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) StartAngle
         Returns the start of angular dimension.  
             
         
        """
        pass
import NXOpen
class SubdivisionSetContinuityBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Features.Subdivision.SubdivisionSetContinuityBuilder builder.  """
    class ContinuityTypes(Enum):
        """
        Members Include: 
         |Smooth| 
         |Sharp| 

        """
        Smooth: int
        Sharp: int
        @staticmethod
        def ValueOf(value: int) -> SubdivisionSetContinuityBuilder.ContinuityTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ContinuityType(self) -> SubdivisionSetContinuityBuilder.ContinuityTypes:
        """
        Getter for property: ( SubdivisionSetContinuityBuilder.ContinuityTypes NXOpen.Featur) ContinuityType
         Returns the continuity.  
           The continuity is used to specify creases in the limit surface.   
         
        """
        pass
    @ContinuityType.setter
    def ContinuityType(self, continuityType: SubdivisionSetContinuityBuilder.ContinuityTypes):
        """
        Setter for property: ( SubdivisionSetContinuityBuilder.ContinuityTypes NXOpen.Featur) ContinuityType
         Returns the continuity.  
           The continuity is used to specify creases in the limit surface.   
         
        """
        pass
    @property
    def TargetObject(self) -> SelectCageObjectData:
        """
        Getter for property: ( SelectCageObjectData NXOpen.Featur) TargetObject
         Returns the target object.  
             
         
        """
        pass
import NXOpen
class SubdivisionSetWeightBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Features.Subdivision.SubdivisionSetWeightBuilder builder.  """
    @property
    def TargetObject(self) -> SelectCageObjectData:
        """
        Getter for property: ( SelectCageObjectData NXOpen.Featur) TargetObject
         Returns the target object.  
             
         
        """
        pass
    @property
    def WeightPercent(self) -> int:
        """
        Getter for property: (int) WeightPercent
         Returns the value indicating percentage weight.  
           Weight defines attraction of the limit surface towards cage topology.   
         
        """
        pass
    @WeightPercent.setter
    def WeightPercent(self, weightPercent: int):
        """
        Setter for property: (int) WeightPercent
         Returns the value indicating percentage weight.  
           Weight defines attraction of the limit surface towards cage topology.   
         
        """
        pass
import NXOpen
class SubdivisionSewCageBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Features.Subdivision.SubdivisionSewCageBuilder builder """
    class MovementTypes(Enum):
        """
        Members Include: 
         |Average|  Both sides move and will be sewn in the middle. 
         |Side1Fixed|  Side 2 will move to side 1. 
         |Side2Fixed|  Side 1 will move to side 2. 

        """
        Average: int
        Side1Fixed: int
        Side2Fixed: int
        @staticmethod
        def ValueOf(value: int) -> SubdivisionSewCageBuilder.MovementTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def MovementType(self) -> SubdivisionSewCageBuilder.MovementTypes:
        """
        Getter for property: ( SubdivisionSewCageBuilder.MovementTypes NXOpen.Featur) MovementType
         Returns the movement type of two sides during sew.  
             
         
        """
        pass
    @MovementType.setter
    def MovementType(self, movementType: SubdivisionSewCageBuilder.MovementTypes):
        """
        Setter for property: ( SubdivisionSewCageBuilder.MovementTypes NXOpen.Featur) MovementType
         Returns the movement type of two sides during sew.  
             
         
        """
        pass
    @property
    def SelectedEdges1(self) -> SelectCageObjectData:
        """
        Getter for property: ( SelectCageObjectData NXOpen.Featur) SelectedEdges1
         Returns the first set of edges   
            
         
        """
        pass
    @property
    def SelectedEdges2(self) -> SelectCageObjectData:
        """
        Getter for property: ( SelectCageObjectData NXOpen.Featur) SelectedEdges2
         Returns the second set of edges   
            
         
        """
        pass
import NXOpen
class SubdivisionSplitFaceBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Features.Subdivision.SubdivisionSplitFaceBuilder builder. """
    class Types(Enum):
        """
        Members Include: 
         |Uniform|  Uniform split type. 
         |ThroughLines|  Through lines split type. 

        """
        Uniform: int
        ThroughLines: int
        @staticmethod
        def ValueOf(value: int) -> SubdivisionSplitFaceBuilder.Types:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def FacesToSplit(self) -> SelectCageObjectData:
        """
        Getter for property: ( SelectCageObjectData NXOpen.Featur) FacesToSplit
         Returns the faces to split.  
             
         
        """
        pass
    @property
    def Number(self) -> int:
        """
        Getter for property: (int) Number
         Returns the desired split number in one face.  
             
         
        """
        pass
    @Number.setter
    def Number(self, number: int):
        """
        Setter for property: (int) Number
         Returns the desired split number in one face.  
             
         
        """
        pass
    @property
    def ReferenceEdge(self) -> SelectCageObjectData:
        """
        Getter for property: ( SelectCageObjectData NXOpen.Featur) ReferenceEdge
         Returns the reference edges.  
             
         
        """
        pass
    @property
    def Type(self) -> SubdivisionSplitFaceBuilder.Types:
        """
        Getter for property: ( SubdivisionSplitFaceBuilder.Types NXOpen.Featur) Type
         Returns the split type.  
             
         
        """
        pass
    @Type.setter
    def Type(self, type: SubdivisionSplitFaceBuilder.Types):
        """
        Setter for property: ( SubdivisionSplitFaceBuilder.Types NXOpen.Featur) Type
         Returns the split type.  
             
         
        """
        pass
    def AddSplitPoint(self, location: NXOpen.Point3d, objectValue: NXOpen.DisplayableObject) -> None:
        """
         Add split face point. 
        """
        pass
    def ClearSplitPoints(self) -> None:
        """
         Clear split face point. 
        """
        pass
    def UpdateSplitPositions(self, splitLineIndex: int, positions: List[NXOpen.Point3d]) -> None:
        """
         Update split positions. 
        """
        pass
import NXOpen
class SubdivisionSubdivideFaceBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Features.Subdivision.SubdivisionSubdivideFaceBuilder builder.  """
    @property
    def FacesToSubdivide(self) -> SelectCageObjectData:
        """
        Getter for property: ( SelectCageObjectData NXOpen.Featur) FacesToSubdivide
         Returns the faces to subdivide.  
             
         
        """
        pass
    @property
    def Scale(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Scale
         Returns the scale factor.  
           The value is from 0 to 100. 0 refers to the original size of the face, 100 refers to the center of the face.   
         
        """
        pass
    def Subdivide(self) -> None:
        """
         Perform subdivide operation. 
        """
        pass
import NXOpen
class SubdivisionSweepBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Features.Subdivision.SubdivisionSweepBuilder builder. """
    class ContinuityType(Enum):
        """
        Members Include: 
         |Smooth|  Smooth continuity 
         |Sharp|  Sharp continuity 

        """
        Smooth: int
        Sharp: int
        @staticmethod
        def ValueOf(value: int) -> SubdivisionSweepBuilder.ContinuityType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def CanSew(self) -> bool:
        """
        Getter for property: (bool) CanSew
         Returns the value indicating if open edges of the swept mesh can be sewn with selected input open edges.  
            
         
        """
        pass
    @CanSew.setter
    def CanSew(self, canSew: bool):
        """
        Setter for property: (bool) CanSew
         Returns the value indicating if open edges of the swept mesh can be sewn with selected input open edges.  
            
         
        """
        pass
    @property
    def Continuity(self) -> SubdivisionSweepBuilder.ContinuityType:
        """
        Getter for property: ( SubdivisionSweepBuilder.ContinuityType NXOpen.Featur) Continuity
         Returns the continuity.  
           The continuity is used to specify creases in the limit surface corresponding to edges
                        of the swept region that are sewn with the primary existing region.   
         
        """
        pass
    @Continuity.setter
    def Continuity(self, continuity: SubdivisionSweepBuilder.ContinuityType):
        """
        Setter for property: ( SubdivisionSweepBuilder.ContinuityType NXOpen.Featur) Continuity
         Returns the continuity.  
           The continuity is used to specify creases in the limit surface corresponding to edges
                        of the swept region that are sewn with the primary existing region.   
         
        """
        pass
    @property
    def Guides(self) -> CageSectionDataList:
        """
        Getter for property: ( CageSectionDataList NXOpen.Featur) Guides
         Returns the guide objects.  
             
         
        """
        pass
    @property
    def Sections(self) -> CageSectionDataList:
        """
        Getter for property: ( CageSectionDataList NXOpen.Featur) Sections
         Returns the section objects.  
             
         
        """
        pass
import NXOpen
class SubdivisionTubeBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Features.Subdivision.SubdivisionTubeBuilder builder. """
    class EndCapsType(Enum):
        """
        Members Include: 
         |NotSet| 
         |Flat| 
         |Round| 

        """
        NotSet: int
        Flat: int
        Round: int
        @staticmethod
        def ValueOf(value: int) -> SubdivisionTubeBuilder.EndCapsType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Types(Enum):
        """
        Members Include: 
         |SinglePath|  Single Path 
         |BranchedPath|  Branched Path 

        """
        SinglePath: int
        BranchedPath: int
        @staticmethod
        def ValueOf(value: int) -> SubdivisionTubeBuilder.Types:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def CrossSection(self) -> int:
        """
        Getter for property: (int) CrossSection
         Returns the cross section   
            
         
        """
        pass
    @CrossSection.setter
    def CrossSection(self, crossSection: int):
        """
        Setter for property: (int) CrossSection
         Returns the cross section   
            
         
        """
        pass
    @property
    def EndCaps(self) -> SubdivisionTubeBuilder.EndCapsType:
        """
        Getter for property: ( SubdivisionTubeBuilder.EndCapsType NXOpen.Featur) EndCaps
         Returns the end capping type   
            
         
        """
        pass
    @EndCaps.setter
    def EndCaps(self, endCaps: SubdivisionTubeBuilder.EndCapsType):
        """
        Setter for property: ( SubdivisionTubeBuilder.EndCapsType NXOpen.Featur) EndCaps
         Returns the end capping type   
            
         
        """
        pass
    @property
    def FalloffDistance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) FalloffDistance
         Returns the falloff distance   
            
         
        """
        pass
    @property
    def GraphStructureObject(self) -> SelectCageObjectData:
        """
        Getter for property: ( SelectCageObjectData NXOpen.Featur) GraphStructureObject
         Returns the object as branched path of tube.  
             
         
        """
        pass
    @property
    def NodeSize(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) NodeSize
         Returns the node size   
            
         
        """
        pass
    @property
    def NumberOfSegments(self) -> int:
        """
        Getter for property: (int) NumberOfSegments
         Returns the number of segments.  
             
         
        """
        pass
    @NumberOfSegments.setter
    def NumberOfSegments(self, numberOfSegments: int):
        """
        Setter for property: (int) NumberOfSegments
         Returns the number of segments.  
             
         
        """
        pass
    @property
    def PathObject(self) -> SelectCageObjectData:
        """
        Getter for property: ( SelectCageObjectData NXOpen.Featur) PathObject
         Returns the object as path of tube.  
             
         
        """
        pass
    @property
    def Rod(self) -> int:
        """
        Getter for property: (int) Rod
         Returns the rod   
            
         
        """
        pass
    @Rod.setter
    def Rod(self, rod: int):
        """
        Setter for property: (int) Rod
         Returns the rod   
            
         
        """
        pass
    @property
    def RodSize(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RodSize
         Returns the rod size   
            
         
        """
        pass
    @property
    def Size(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Size
         Returns the size of tube in cross section.  
             
         
        """
        pass
    @property
    def Type(self) -> SubdivisionTubeBuilder.Types:
        """
        Getter for property: ( SubdivisionTubeBuilder.Types NXOpen.Featur) Type
         Returns the type   
            
         
        """
        pass
    @Type.setter
    def Type(self, type: SubdivisionTubeBuilder.Types):
        """
        Setter for property: ( SubdivisionTubeBuilder.Types NXOpen.Featur) Type
         Returns the type   
            
         
        """
        pass
import NXOpen
class TransformCageData(NXOpen.Builder): 
    """ Represents a NXOpen.Features.Subdivision.TransformCageData builder. """
    class FallOffMethodType(Enum):
        """
        Members Include: 
         |NotSet|  No falloff 
         |Selected|  Selected vertices falloff 
         |All|  All vertices falloff 

        """
        NotSet: int
        Selected: int
        All: int
        @staticmethod
        def ValueOf(value: int) -> TransformCageData.FallOffMethodType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class MovementMethodType(Enum):
        """
        Members Include: 
         |WCS|  Movement along WCS principal axis or plane 
         |View|  Movement in view plane 
         |Vector|  Movement along arbitrary direction 
         |Plane|  Movement in arbitrary plane 
         |Normal|  Movement along a face normal 
         |Edge|  Movement along an edge 

        """
        WCS: int
        View: int
        Vector: int
        Plane: int
        Normal: int
        Edge: int
        @staticmethod
        def ValueOf(value: int) -> TransformCageData.MovementMethodType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ScalingMethodType(Enum):
        """
        Members Include: 
         |Linear|  Scale in the specified direction 
         |Planar|  Scale in the plane normal to specified direction 
         |Uniform|  Scale uniformly all the directions 

        """
        Linear: int
        Planar: int
        Uniform: int
        @staticmethod
        def ValueOf(value: int) -> TransformCageData.ScalingMethodType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class TransformationMethodType(Enum):
        """
        Members Include: 
         |Drag|  Edit cage topology by direct dragging 
         |Transform|  Edit cage topology by transformations 

        """
        Drag: int
        Transform: int
        @staticmethod
        def ValueOf(value: int) -> TransformCageData.TransformationMethodType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class WCSOptionType(Enum):
        """
        Members Include: 
         |InferredAxis|  Along axis inferred during movement 
         |X|  Along X axis 
         |Y|  Along Y axis 
         |Z|  Along Z axis 
         |YZ|  In YZ plane 
         |XZ|  In XZ plane 
         |XY|  In XY plane 

        """
        InferredAxis: int
        X: int
        Y: int
        Z: int
        YZ: int
        XZ: int
        XY: int
        @staticmethod
        def ValueOf(value: int) -> TransformCageData.WCSOptionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def CageManipulator(self) -> CageManipulatorData:
        """
        Getter for property: ( CageManipulatorData NXOpen.Featur) CageManipulator
         Returns the cage manipulation data.  
             
         
        """
        pass
    @property
    def CanMoveToolOnly(self) -> bool:
        """
        Getter for property: (bool) CanMoveToolOnly
         Returns the flag indicating if transformer tool can be moved without transforming the selected cage topology.  
             
         
        """
        pass
    @CanMoveToolOnly.setter
    def CanMoveToolOnly(self, canMove: bool):
        """
        Setter for property: (bool) CanMoveToolOnly
         Returns the flag indicating if transformer tool can be moved without transforming the selected cage topology.  
             
         
        """
        pass
    @property
    def CanRelocateToolToSelection(self) -> bool:
        """
        Getter for property: (bool) CanRelocateToolToSelection
         Returns the flag indicating if transformer tool can be relocated based on cage topology selection.  
             
         
        """
        pass
    @CanRelocateToolToSelection.setter
    def CanRelocateToolToSelection(self, canRelocate: bool):
        """
        Setter for property: (bool) CanRelocateToolToSelection
         Returns the flag indicating if transformer tool can be relocated based on cage topology selection.  
             
         
        """
        pass
    @property
    def CanReorientToolToSelection(self) -> bool:
        """
        Getter for property: (bool) CanReorientToolToSelection
         Returns the flag indicating if transformer tool can be reoriented based on cage topology selection.  
             
         
        """
        pass
    @CanReorientToolToSelection.setter
    def CanReorientToolToSelection(self, canReorient: bool):
        """
        Setter for property: (bool) CanReorientToolToSelection
         Returns the flag indicating if transformer tool can be reoriented based on cage topology selection.  
             
         
        """
        pass
    @property
    def FallOffFactor(self) -> float:
        """
        Getter for property: (float) FallOffFactor
         Returns the falloff factor.  
             
         
        """
        pass
    @FallOffFactor.setter
    def FallOffFactor(self, factor: float):
        """
        Setter for property: (float) FallOffFactor
         Returns the falloff factor.  
             
         
        """
        pass
    @property
    def FallOffMethod(self) -> TransformCageData.FallOffMethodType:
        """
        Getter for property: ( TransformCageData.FallOffMethodType NXOpen.Featur) FallOffMethod
         Returns the falloff method.  
             
         
        """
        pass
    @FallOffMethod.setter
    def FallOffMethod(self, fallOffMethod: TransformCageData.FallOffMethodType):
        """
        Setter for property: ( TransformCageData.FallOffMethodType NXOpen.Featur) FallOffMethod
         Returns the falloff method.  
             
         
        """
        pass
    @property
    def FallOffObjects(self) -> SelectCageObjectData:
        """
        Getter for property: ( SelectCageObjectData NXOpen.Featur) FallOffObjects
         Returns the falloff objects.  
             
         
        """
        pass
    @property
    def MovementMethod(self) -> TransformCageData.MovementMethodType:
        """
        Getter for property: ( TransformCageData.MovementMethodType NXOpen.Featur) MovementMethod
         Returns the movement method.  
             
         
        """
        pass
    @MovementMethod.setter
    def MovementMethod(self, movementMethod: TransformCageData.MovementMethodType):
        """
        Setter for property: ( TransformCageData.MovementMethodType NXOpen.Featur) MovementMethod
         Returns the movement method.  
             
         
        """
        pass
    @property
    def MovementPlane(self) -> NXOpen.Plane:
        """
        Getter for property: ( NXOpen.Plane) MovementPlane
         Returns the movement plane.  
             
         
        """
        pass
    @MovementPlane.setter
    def MovementPlane(self, movementPlane: NXOpen.Plane):
        """
        Setter for property: ( NXOpen.Plane) MovementPlane
         Returns the movement plane.  
             
         
        """
        pass
    @property
    def MovementVector(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) MovementVector
         Returns the movement vector.  
             
         
        """
        pass
    @MovementVector.setter
    def MovementVector(self, movementVector: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) MovementVector
         Returns the movement vector.  
             
         
        """
        pass
    @property
    def ScalingMethod(self) -> TransformCageData.ScalingMethodType:
        """
        Getter for property: ( TransformCageData.ScalingMethodType NXOpen.Featur) ScalingMethod
         Returns the scaling method.  
             
         
        """
        pass
    @ScalingMethod.setter
    def ScalingMethod(self, scalingMethod: TransformCageData.ScalingMethodType):
        """
        Setter for property: ( TransformCageData.ScalingMethodType NXOpen.Featur) ScalingMethod
         Returns the scaling method.  
             
         
        """
        pass
    @property
    def TransformationMethod(self) -> TransformCageData.TransformationMethodType:
        """
        Getter for property: ( TransformCageData.TransformationMethodType NXOpen.Featur) TransformationMethod
         Returns the transformation method.  
             
         
        """
        pass
    @TransformationMethod.setter
    def TransformationMethod(self, method: TransformCageData.TransformationMethodType):
        """
        Setter for property: ( TransformCageData.TransformationMethodType NXOpen.Featur) TransformationMethod
         Returns the transformation method.  
             
         
        """
        pass
    @property
    def WCSOption(self) -> TransformCageData.WCSOptionType:
        """
        Getter for property: ( TransformCageData.WCSOptionType NXOpen.Featur) WCSOption
         Returns the WCS option.  
             
         
        """
        pass
    @WCSOption.setter
    def WCSOption(self, wcsOption: TransformCageData.WCSOptionType):
        """
        Setter for property: ( TransformCageData.WCSOptionType NXOpen.Featur) WCSOption
         Returns the WCS option.  
             
         
        """
        pass
    def ResetFallOffToLinear(self) -> None:
        """
         Resets the falloff scale to linear. 
        """
        pass
