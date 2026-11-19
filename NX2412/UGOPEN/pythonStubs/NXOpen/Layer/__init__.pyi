from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
class CategoryCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of layer categories """
    def CreateCategory(self, name: str, description: str, member_layers: List[int]) -> Category:
        """
         Creates a new layer category 
         Returns layer_category ( Category NXOpe):  The new category .
        """
        pass
    def FindObject(self, name: str) -> Category:
        """
         Finds the NXOpen.Layer.Category with the given name. 
                
                An exception will be thrown if no object can be found with the given name.
                
         Returns category ( Category NXOpe):  .
        """
        pass
import NXOpen
class Category(NXOpen.NXObject): 
    """ Represents a layer category.  A layer category is a set of layers.  A layer
    can belong to more than one category. """
    @property
    def Description(self) -> str:
        """
        Getter for property: (str) Description
         Returns the category's description, if one exists   
            
         
        """
        pass
    @Description.setter
    def Description(self, description: str):
        """
        Setter for property: (str) Description
         Returns the category's description, if one exists   
            
         
        """
        pass
    def GetMemberLayers(self) -> List[int]:
        """
         Returns all the layers that belong to the category 
         Returns layers (List[int]):  .
        """
        pass
    def SetMemberLayers(self, layers: List[int]) -> None:
        """
         Sets which layers belong to the category 
        """
        pass
    def SetState(self, state: State) -> None:
        """
         Changes the state of every layer in the category to the
                specified state, except the work layer 
        """
        pass
class Constants(Enum):
    """
    Members Include: 
     |FirstLayer|  The number of the first layer.
                                                Valid layers are numbered from Layer.Constants.FirstLayer
                                                to Layer.Constants.LastLayer 
     |LastLayer|  The number of the last layer.
                                                Valid layers are numbered from Layer.Constants.FirstLayer
                                                to Layer.Constants.LastLayer 

    """
    FirstLayer: int
    LastLayer: int
    @staticmethod
    def ValueOf(value: int) -> Constants:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
class LayerManager(NXOpen.Object): 
    """ Represents an object that manages layers """
    @property
    def WorkLayer(self) -> int:
        """
        Getter for property: (int) WorkLayer
         Returns the work layer.  
          
                If you change the work layer, the old work layer is changed to Selectable.
                The part must be the displayed part.   
         
        """
        pass
    @WorkLayer.setter
    def WorkLayer(self, new_work_layer: int):
        """
        Setter for property: (int) WorkLayer
         Returns the work layer.  
          
                If you change the work layer, the old work layer is changed to Selectable.
                The part must be the displayed part.   
         
        """
        pass
    def ApplyMoveToLayerToOwningParts(self, new_layer: int, object_array: List[NXOpen.DisplayableObject]) -> None:
        """
         Move the selected objects to the specified layer in their Owning Parts.
                This only works when a single layer has been selected on the Layer Settings dialog.
                 The owning parts will be fully loaded if they are not already.
                
                 Objects of class NXOpen.CAE.CAEEdge,
                NXOpen.CAE.CAEFace, NXOpen.CAE.CAEVertex,
                NXOpen.Edge, NXOpen.Face or
                NXOpen.View may not be moved.
                 
        """
        pass
    @overload
    def ChangeStates(self, state_array: List[StateInfo], fitAll: bool) -> None:
        """
         Changes the states of the specified layers in the part. 
                Note: there must be exactly one work layer.  If you change the work layer,
                you must specify a new work layer.  If you set the work layer, the
                old work layer will be changed to Selectable, unless you specify otherwise.
                The part must be the displayed part.
                
        """
        pass
    @overload
    def ChangeStates(self, state_array: List[StateInfo]) -> None:
        """
         Changes the states of the specified layers in the part. 
                Note: there must be exactly one work layer.  If you change the work layer,
                you must specify a new work layer.  If you set the work layer, the
                old work layer will be changed to Selectable, unless you specify otherwise.
                The part must be the displayed part.
                
        """
        pass
    def CopyObjects(self, new_layer: int, object_array: List[NXOpen.NXObject]) -> None:
        """
         Copies objects to the specified layer
                 Objects of class NXOpen.Assemblies.Component,
                NXOpen.DatumAxis, NXOpen.DatumPlane
                NXOpen.Edge, NXOpen.Face,
                NXOpen.Features.Feature or NXOpen.View,
                may not be copied.
                 Objects of type UF_cs2_vertex_type may not be copied. 
                 The part must be the work part. 
        """
        pass
    def GetAllObjectsOnLayer(self, layer: int) -> List[NXOpen.NXObject]:
        """
         Returns all objects on the specified layer. 
                This includes objects which are not counted as objects on the layer by the "Layer Settings" dialog.
                 The part must be the displayed part.  
         Returns objects ( NXOpen.NXObject Li):  All the objects on the specified layer .
        """
        pass
    def GetState(self, layer: int) -> State:
        """
         Gets the state of the specified layer.  The part must be the displayed part. 
         Returns state ( State NXOpe):  .
        """
        pass
    def GetStates(self) -> StateCollection:
        """
         Gets the states for all layers in the part. The part must be the displayed part. 
         Returns state_collection ( StateCollection NXOpe):  Indicates the states for all layers in the part. .
        """
        pass
    def GetVisibilitiesInView(self, view: NXOpen.View) -> List[StateInfo]:
        """
         Gets the visibility of all layers in a specified view.
                The part must be the displayed part. 
         Returns state_array ( StateInfo List[NXO):  The current states for the layers.
                                                        The returned states can only be
                                                        Layer.State.Visible and
                                                        Layer.State.Hidden.
                                                        state_array[i] is for layer i+1 .
        """
        pass
    def MoveDisplayableObjects(self, new_layer: int, object_array: List[NXOpen.DisplayableObject]) -> None:
        """
         Moves displayable objects to the specified layer.
                The specified part may be the displayed part or the work part.  If it is
                the work part but not the displayed part, then none of the objects to be
                moved may be currently displayed.
                This method is the preferred way to change the layer of one or more objects,
                because NXOpen.DisplayableObject.Layer does not correct
                the display of the objects and does not work as expected for sketches and
                components, because it does not move the members of the sketch or component.
                 Objects of class NXOpen.CAE.CAEEdge,
                NXOpen.CAE.CAEFace, NXOpen.CAE.CAEVertex,
                NXOpen.Edge, NXOpen.Face or
                NXOpen.View may not be moved. 
        """
        pass
    def ResetViewVisibilityToGlobal(self, view: NXOpen.View) -> None:
        """
         Resets a view's layer visibility to the global states.
                The part must be the displayed part. 
        """
        pass
    def SetObjectsVisibilityOnLayer(self, view: NXOpen.View, state_array: List[StateInfo], do_update: bool) -> None:
        """
         Sets specified layer(s) visibility in a specified view.
                The part must be the displayed part. 
        """
        pass
    @overload
    def SetState(self, layer: int, state: State) -> None:
        """
         Sets the state of the specified layer.
                The specified layer must not be the work layer.
                If you are changing the state of the layer to Work,
                the old work layer will be changed to Selectable.
                The part must be the displayed part.
                
        """
        pass
    @overload
    def SetState(self, layer: int, state: State, fitAll: bool) -> None:
        """
         Sets the state of the specified layer.
                The specified layer must not be the work layer.
                If you are changing the state of the layer to Work,
                the old work layer will be changed to Selectable.
                The part must be the displayed part.
                
        """
        pass
    @overload
    def SetStates(self, state_collection: StateCollection, fitAll: bool) -> None:
        """
         Sets the states for all layers in the part.  The part must be the displayed part.
                    Note: there must be exactly one work layer. 
        """
        pass
    @overload
    def SetStates(self, state_collection: StateCollection) -> None:
        """
         Sets the states for all layers in the part.  The part must be the displayed part.
                    Note: there must be exactly one work layer. 
        """
        pass
import NXOpen
class StateCollection(NXOpen.TransientObject): 
    """ Represents a copy of the layer states.  You can manipulate the 
    StateCollection without affecting the actual layer states in the part.
    Your changes to the StateCollection will not be applied to the part until you
    apply them through the method Layer.LayerManager.SetStates. """
    def Dispose(self) -> None:
        """
         Frees the object from memory.  After this method is called,
                it is illegal to use the object.  In .NET, this method is automatically
                called when the object is deleted by the garbage collector.  
        """
        pass
    def GetState(self, layer: int) -> State:
        """
         Returns the state of the specified layer 
         Returns state ( State NXOpe):  .
        """
        pass
    def SetState(self, layer: int, state: State) -> None:
        """
         Sets the state of the specified layer 
        """
        pass
    def SetStateOfCategory(self, category: Category, state: State) -> None:
        """
         Sets the state of every layer in the category to the
                specified state, except the work layer  
        """
        pass
class StateInfo:
    """
     Used in several methods that get or set the state of a layer 
    """
    @property
    def Layer(self) -> int:
        """
        Getter for property Layer
        Layer number

        """
        pass
    @Layer.setter
    def Layer(self, value: int):
        """
        Getter for property Layer
        Layer number
        Setter for property Layer
        Layer number

        """
        pass
    @property
    def State(self) -> State:
        """
        Getter for property State
        The state of the layer

        """
        pass
    @State.setter
    def State(self, value: State):
        """
        Getter for property State
        The state of the layer
        Setter for property State
        The state of the layer

        """
        pass
class State(Enum):
    """
    Members Include: 
     |WorkLayer|  Work layer.  All newly created objects are placed on the work layer.
     |Selectable|  Objects on the layer are selectable 
     |Visible|  Objects on the layer are visible but not selectable 
     |Hidden|  Objects on the layer are not visible and not selectable 

    """
    WorkLayer: int
    Selectable: int
    Visible: int
    Hidden: int
    @staticmethod
    def ValueOf(value: int) -> State:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
