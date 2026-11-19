from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
##  Represents a collection of layer categories  <br> To obtain an instance of this class, refer to @link NXOpen::BasePart  NXOpen::BasePart @endlink  <br> 
## 
##   <br>  Created in NX3.0.0  <br> 

class CategoryCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of layer categories """


    ##  Creates a new layer category 
    ##  @return layer_category (@link Category NXOpen.Layer.Category@endlink):  The new category .
    ## 
    ##   <br>  Created in NX3.0.0  <br> 

    ## License requirements: None.
    ##  The name must not NULL and 
    ##                             must not already be used by another layer category. 
    def CreateCategory(part: CategoryCollection, name: str, description: str, member_layers: List[int]) -> Category:
        """
         Creates a new layer category 
         @return layer_category (@link Category NXOpen.Layer.Category@endlink):  The new category .
        """
        pass
    
    ##  Finds the @link NXOpen::Layer::Category NXOpen::Layer::Category@endlink  with the given name. 
    ##         
    ##         An exception will be thrown if no object can be found with the given name.
    ##         
    ##  @return category (@link Category NXOpen.Layer.Category@endlink):  .
    ## 
    ##   <br>  Created in NX3.0.0  <br> 

    ## License requirements: None.
    ##  The name of the @link NXOpen::Layer::Category NXOpen::Layer::Category@endlink  
    def FindObject(part: CategoryCollection, name: str) -> Category:
        """
         Finds the @link NXOpen::Layer::Category NXOpen::Layer::Category@endlink  with the given name. 
                
                An exception will be thrown if no object can be found with the given name.
                
         @return category (@link Category NXOpen.Layer.Category@endlink):  .
        """
        pass
    
import NXOpen
##  Represents a layer category.  A layer category is a set of layers.  A layer
##     can belong to more than one category.  <br> To create a new instance of this class, use @link NXOpen::Layer::CategoryCollection::CreateCategory  NXOpen::Layer::CategoryCollection::CreateCategory @endlink  <br> 
## 
##   <br>  Created in NX3.0.0  <br> 

class Category(NXOpen.NXObject): 
    """ Represents a layer category.  A layer category is a set of layers.  A layer
    can belong to more than one category. """


    ## Getter for property: (str) Description
    ##   the category's description, if one exists   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX3.0.0  <br> 

    ## @return str
    @property
    def Description(self) -> str:
        """
        Getter for property: (str) Description
          the category's description, if one exists   
            
         
        """
        pass
    
    ## Setter for property: (str) Description

    ##   the category's description, if one exists   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX3.0.0  <br> 

    @Description.setter
    def Description(self, description: str):
        """
        Setter for property: (str) Description
          the category's description, if one exists   
            
         
        """
        pass
    
    ##  Returns all the layers that belong to the category 
    ##  @return layers (List[int]):  .
    ## 
    ##   <br>  Created in NX3.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetMemberLayers(categ: Category) -> List[int]:
        """
         Returns all the layers that belong to the category 
         @return layers (List[int]):  .
        """
        pass
    
    ##  Sets which layers belong to the category 
    ## 
    ##   <br>  Created in NX3.0.0  <br> 

    ## License requirements: None.
    ##  
    def SetMemberLayers(categ: Category, layers: List[int]) -> None:
        """
         Sets which layers belong to the category 
        """
        pass
    
    ##  Changes the state of every layer in the category to the
    ##         specified state, except the work layer 
    ## 
    ##   <br>  Created in NX3.0.0  <br> 

    ## License requirements: None.
    ##  new state for the category.  Must not be
    ##                                 @link Layer::StateWorkLayer Layer::StateWorkLayer@endlink  
    def SetState(categ: Category, state: State) -> None:
        """
         Changes the state of every layer in the category to the
                specified state, except the work layer 
        """
        pass
    
##  Constants for layers 
##  The number of the first layer.
##                                             Valid layers are numbered from @link Layer::ConstantsFirstLayer Layer::ConstantsFirstLayer@endlink 
##                                             to @link Layer::ConstantsLastLayer Layer::ConstantsLastLayer@endlink  
class Constants(Enum):
    """
    Members Include: <FirstLayer> <LastLayer>
    """
    FirstLayer: int
    LastLayer: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> Constants:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


import NXOpen
##  Represents an object that manages layers  <br> To obtain an instance of this class, refer to @link NXOpen::BasePart  NXOpen::BasePart @endlink  <br> 
## 
##   <br>  Created in NX3.0.0  <br> 

class LayerManager(NXOpen.Object): 
    """ Represents an object that manages layers """


    ## Getter for property: (int) WorkLayer
    ##   the work layer.  
    ##   
    ##         If you change the work layer, the old work layer is changed to Selectable.
    ##         The part must be the displayed part.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX3.0.0  <br> 

    ## @return int
    @property
    def WorkLayer(self) -> int:
        """
        Getter for property: (int) WorkLayer
          the work layer.  
          
                If you change the work layer, the old work layer is changed to Selectable.
                The part must be the displayed part.   
         
        """
        pass
    
    ## Setter for property: (int) WorkLayer

    ##   the work layer.  
    ##   
    ##         If you change the work layer, the old work layer is changed to Selectable.
    ##         The part must be the displayed part.   
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX3.0.0  <br> 

    @WorkLayer.setter
    def WorkLayer(self, new_work_layer: int):
        """
        Setter for property: (int) WorkLayer
          the work layer.  
          
                If you change the work layer, the old work layer is changed to Selectable.
                The part must be the displayed part.   
         
        """
        pass
    
    ##  Move the selected objects to the specified layer in their Owning Parts.
    ##         This only works when a single layer has been selected on the Layer Settings dialog.
    ##          <br>  The owning parts will be fully loaded if they are not already.
    ##          <br> 
    ##          <br>  Objects of class @link NXOpen::CAE::CAEEdge NXOpen::CAE::CAEEdge@endlink ,
    ##         @link NXOpen::CAE::CAEFace NXOpen::CAE::CAEFace@endlink , @link NXOpen::CAE::CAEVertex NXOpen::CAE::CAEVertex@endlink ,
    ##         @link NXOpen::Edge NXOpen::Edge@endlink , @link NXOpen::Face NXOpen::Face@endlink  or
    ##         @link NXOpen::View NXOpen::View@endlink  may not be moved.
    ##          <br>  
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ##  The layer in the owning parts to move the objects to 
    def ApplyMoveToLayerToOwningParts(disp_part: LayerManager, new_layer: int, object_array: List[NXOpen.DisplayableObject]) -> None:
        """
         Move the selected objects to the specified layer in their Owning Parts.
                This only works when a single layer has been selected on the Layer Settings dialog.
                 <br>  The owning parts will be fully loaded if they are not already.
                 <br> 
                 <br>  Objects of class @link NXOpen::CAE::CAEEdge NXOpen::CAE::CAEEdge@endlink ,
                @link NXOpen::CAE::CAEFace NXOpen::CAE::CAEFace@endlink , @link NXOpen::CAE::CAEVertex NXOpen::CAE::CAEVertex@endlink ,
                @link NXOpen::Edge NXOpen::Edge@endlink , @link NXOpen::Face NXOpen::Face@endlink  or
                @link NXOpen::View NXOpen::View@endlink  may not be moved.
                 <br>  
        """
        pass
    
    ##  Changes the states of the specified layers in the part. 
    ##         Note: there must be exactly one work layer.  If you change the work layer,
    ##         you must specify a new work layer.  If you set the work layer, the
    ##         old work layer will be changed to Selectable, unless you specify otherwise.
    ##         The part must be the displayed part.
    ##         
    ## 
    ##   <br>  Created in NX3.0.0  <br> 

    ## License requirements: None.
    ##  
    ##                 Indicates the new states for the layers. 
    @overload
    def ChangeStates(self, part: LayerManager, state_array: List[StateInfo], fitAll: bool) -> None:
        """
         Changes the states of the specified layers in the part. 
                Note: there must be exactly one work layer.  If you change the work layer,
                you must specify a new work layer.  If you set the work layer, the
                old work layer will be changed to Selectable, unless you specify otherwise.
                The part must be the displayed part.
                
        """
        pass
    
    ##  Changes the states of the specified layers in the part. 
    ##         Note: there must be exactly one work layer.  If you change the work layer,
    ##         you must specify a new work layer.  If you set the work layer, the
    ##         old work layer will be changed to Selectable, unless you specify otherwise.
    ##         The part must be the displayed part.
    ##         
    ## 
    ##   <br>  Created in NX3.0.0  <br> 

    ## License requirements: None.
    ##  
    ##                 Indicates the new states for the layers. 
    @overload
    def ChangeStates(self, part: LayerManager, state_array: List[StateInfo]) -> None:
        """
         Changes the states of the specified layers in the part. 
                Note: there must be exactly one work layer.  If you change the work layer,
                you must specify a new work layer.  If you set the work layer, the
                old work layer will be changed to Selectable, unless you specify otherwise.
                The part must be the displayed part.
                
        """
        pass
    
    ##  Copies objects to the specified layer
    ##          <br>  Objects of class @link NXOpen::Assemblies::Component NXOpen::Assemblies::Component@endlink ,
    ##         @link NXOpen::DatumAxis NXOpen::DatumAxis@endlink , @link NXOpen::DatumPlane NXOpen::DatumPlane@endlink 
    ##         @link NXOpen::Edge NXOpen::Edge@endlink , @link NXOpen::Face NXOpen::Face@endlink ,
    ##         @link NXOpen::Features::Feature NXOpen::Features::Feature@endlink  or @link NXOpen::View NXOpen::View@endlink ,
    ##         may not be copied. <br> 
    ##          <br>  Objects of type UF_cs2_vertex_type may not be copied.  <br> 
    ##          <br>  The part must be the work part.  <br> 
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: solid_modeling ("SOLIDS MODELING") OR drafting ("DRAFTING")
    ##  The layer to move the objects to 
    def CopyObjects(part: LayerManager, new_layer: int, object_array: List[NXOpen.NXObject]) -> None:
        """
         Copies objects to the specified layer
                 <br>  Objects of class @link NXOpen::Assemblies::Component NXOpen::Assemblies::Component@endlink ,
                @link NXOpen::DatumAxis NXOpen::DatumAxis@endlink , @link NXOpen::DatumPlane NXOpen::DatumPlane@endlink 
                @link NXOpen::Edge NXOpen::Edge@endlink , @link NXOpen::Face NXOpen::Face@endlink ,
                @link NXOpen::Features::Feature NXOpen::Features::Feature@endlink  or @link NXOpen::View NXOpen::View@endlink ,
                may not be copied. <br> 
                 <br>  Objects of type UF_cs2_vertex_type may not be copied.  <br> 
                 <br>  The part must be the work part.  <br> 
        """
        pass
    
    ##  Returns all objects on the specified layer. 
    ##         This includes objects which are not counted as objects on the layer by the "Layer Settings" dialog.
    ##          <br>  The part must be the displayed part.  <br>  
    ##  @return objects (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink):  All the objects on the specified layer .
    ## 
    ##   <br>  Created in NX3.0.0  <br> 

    ## License requirements: None.
    ##  
    def GetAllObjectsOnLayer(part: LayerManager, layer: int) -> List[NXOpen.NXObject]:
        """
         Returns all objects on the specified layer. 
                This includes objects which are not counted as objects on the layer by the "Layer Settings" dialog.
                 <br>  The part must be the displayed part.  <br>  
         @return objects (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink):  All the objects on the specified layer .
        """
        pass
    
    ##  Gets the state of the specified layer.  The part must be the displayed part. 
    ##  @return state (@link State NXOpen.Layer.State@endlink):  .
    ## 
    ##   <br>  Created in NX3.0.0  <br> 

    ## License requirements: None.
    ##  
    def GetState(part: LayerManager, layer: int) -> State:
        """
         Gets the state of the specified layer.  The part must be the displayed part. 
         @return state (@link State NXOpen.Layer.State@endlink):  .
        """
        pass
    
    ##  Gets the states for all layers in the part. The part must be the displayed part. 
    ##  @return state_collection (@link StateCollection NXOpen.Layer.StateCollection@endlink):  Indicates the states for all layers in the part. .
    ## 
    ##   <br>  Created in NX3.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetStates(part: LayerManager) -> StateCollection:
        """
         Gets the states for all layers in the part. The part must be the displayed part. 
         @return state_collection (@link StateCollection NXOpen.Layer.StateCollection@endlink):  Indicates the states for all layers in the part. .
        """
        pass
    
    ##  Gets the visibility of all layers in a specified view.
    ##         The part must be the displayed part. 
    ##  @return state_array (@link StateInfo List[NXOpen.Layer.StateInfo]@endlink):  The current states for the layers.
    ##                                                 The returned states can only be
    ##                                                 @link Layer::StateVisible Layer::StateVisible@endlink  and
    ##                                                 @link Layer::StateHidden Layer::StateHidden@endlink .
    ##                                                 state_array[i] is for layer i+1 .
    ## 
    ##   <br>  Created in NX4.0.3  <br> 

    ## License requirements: None.
    ##  The view object being queried 
    def GetVisibilitiesInView(part: LayerManager, view: NXOpen.View) -> List[StateInfo]:
        """
         Gets the visibility of all layers in a specified view.
                The part must be the displayed part. 
         @return state_array (@link StateInfo List[NXOpen.Layer.StateInfo]@endlink):  The current states for the layers.
                                                        The returned states can only be
                                                        @link Layer::StateVisible Layer::StateVisible@endlink  and
                                                        @link Layer::StateHidden Layer::StateHidden@endlink .
                                                        state_array[i] is for layer i+1 .
        """
        pass
    
    ##  Moves displayable objects to the specified layer.
    ##         The specified part may be the displayed part or the work part.  If it is
    ##         the work part but not the displayed part, then none of the objects to be
    ##         moved may be currently displayed.
    ##          <br> This method is the preferred way to change the layer of one or more objects,
    ##         because @link NXOpen::DisplayableObject::SetLayer NXOpen::DisplayableObject::SetLayer@endlink  does not correct
    ##         the display of the objects and does not work as expected for sketches and
    ##         components, because it does not move the members of the sketch or component. <br> 
    ##          <br>  Objects of class @link NXOpen::CAE::CAEEdge NXOpen::CAE::CAEEdge@endlink ,
    ##         @link NXOpen::CAE::CAEFace NXOpen::CAE::CAEFace@endlink , @link NXOpen::CAE::CAEVertex NXOpen::CAE::CAEVertex@endlink ,
    ##         @link NXOpen::Edge NXOpen::Edge@endlink , @link NXOpen::Face NXOpen::Face@endlink  or
    ##         @link NXOpen::View NXOpen::View@endlink  may not be moved. <br>  
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  The layer to move the objects to 
    def MoveDisplayableObjects(part: LayerManager, new_layer: int, object_array: List[NXOpen.DisplayableObject]) -> None:
        """
         Moves displayable objects to the specified layer.
                The specified part may be the displayed part or the work part.  If it is
                the work part but not the displayed part, then none of the objects to be
                moved may be currently displayed.
                 <br> This method is the preferred way to change the layer of one or more objects,
                because @link NXOpen::DisplayableObject::SetLayer NXOpen::DisplayableObject::SetLayer@endlink  does not correct
                the display of the objects and does not work as expected for sketches and
                components, because it does not move the members of the sketch or component. <br> 
                 <br>  Objects of class @link NXOpen::CAE::CAEEdge NXOpen::CAE::CAEEdge@endlink ,
                @link NXOpen::CAE::CAEFace NXOpen::CAE::CAEFace@endlink , @link NXOpen::CAE::CAEVertex NXOpen::CAE::CAEVertex@endlink ,
                @link NXOpen::Edge NXOpen::Edge@endlink , @link NXOpen::Face NXOpen::Face@endlink  or
                @link NXOpen::View NXOpen::View@endlink  may not be moved. <br>  
        """
        pass
    
    ##  Resets a view's layer visibility to the global states.
    ##         The part must be the displayed part. 
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ##  The view object 
    def ResetViewVisibilityToGlobal(part: LayerManager, view: NXOpen.View) -> None:
        """
         Resets a view's layer visibility to the global states.
                The part must be the displayed part. 
        """
        pass
    
    ##  Sets specified layer(s) visibility in a specified view.
    ##         The part must be the displayed part. 
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ##  The view object being modified 
    def SetObjectsVisibilityOnLayer(part: LayerManager, view: NXOpen.View, state_array: List[StateInfo], do_update: bool) -> None:
        """
         Sets specified layer(s) visibility in a specified view.
                The part must be the displayed part. 
        """
        pass
    
    ##  Sets the state of the specified layer.
    ##         The specified layer must not be the work layer.
    ##         If you are changing the state of the layer to Work,
    ##         the old work layer will be changed to Selectable.
    ##         The part must be the displayed part.
    ##         
    ## 
    ##   <br>  Created in NX3.0.0  <br> 

    ## License requirements: None.
    ##  
    @overload
    def SetState(self, part: LayerManager, layer: int, state: State) -> None:
        """
         Sets the state of the specified layer.
                The specified layer must not be the work layer.
                If you are changing the state of the layer to Work,
                the old work layer will be changed to Selectable.
                The part must be the displayed part.
                
        """
        pass
    
    ##  Sets the state of the specified layer.
    ##         The specified layer must not be the work layer.
    ##         If you are changing the state of the layer to Work,
    ##         the old work layer will be changed to Selectable.
    ##         The part must be the displayed part.
    ##         
    ## 
    ##   <br>  Created in NX3.0.0  <br> 

    ## License requirements: None.
    ##  
    @overload
    def SetState(self, part: LayerManager, layer: int, state: State, fitAll: bool) -> None:
        """
         Sets the state of the specified layer.
                The specified layer must not be the work layer.
                If you are changing the state of the layer to Work,
                the old work layer will be changed to Selectable.
                The part must be the displayed part.
                
        """
        pass
    
    ##  Sets the states for all layers in the part.  The part must be the displayed part.
    ##             Note: there must be exactly one work layer. 
    ## 
    ##   <br>  Created in NX3.0.0  <br> 

    ## License requirements: None.
    ##  The states for all layers in the part.  
    @overload
    def SetStates(self, part: LayerManager, state_collection: StateCollection, fitAll: bool) -> None:
        """
         Sets the states for all layers in the part.  The part must be the displayed part.
                    Note: there must be exactly one work layer. 
        """
        pass
    
    ##  Sets the states for all layers in the part.  The part must be the displayed part.
    ##             Note: there must be exactly one work layer. 
    ## 
    ##   <br>  Created in NX3.0.0  <br> 

    ## License requirements: None.
    ##  The states for all layers in the part.  
    @overload
    def SetStates(self, part: LayerManager, state_collection: StateCollection) -> None:
        """
         Sets the states for all layers in the part.  The part must be the displayed part.
                    Note: there must be exactly one work layer. 
        """
        pass
    
import NXOpen
##  Represents a copy of the layer states.  You can manipulate the 
##     StateCollection without affecting the actual layer states in the part.
##     Your changes to the StateCollection will not be applied to the part until you
##     apply them through the method @link Layer::LayerManager::SetStates Layer::LayerManager::SetStates@endlink . 
## 
##   <br>  Created in NX3.0.0  <br> 

class StateCollection(NXOpen.TransientObject): 
    """ Represents a copy of the layer states.  You can manipulate the 
    StateCollection without affecting the actual layer states in the part.
    Your changes to the StateCollection will not be applied to the part until you
    apply them through the method <ja_method>Layer.LayerManager.SetStates</ja_method>. """


    ##  Frees the object from memory.  After this method is called,
    ##         it is illegal to use the object.  In .NET, this method is automatically
    ##         called when the object is deleted by the garbage collector.  
    ## 
    ##   <br>  Created in NX3.0.0  <br> 

    ## License requirements: None.
    def Dispose(self) -> None:
        """
         Frees the object from memory.  After this method is called,
                it is illegal to use the object.  In .NET, this method is automatically
                called when the object is deleted by the garbage collector.  
        """
        pass
    
    ##  Returns the state of the specified layer 
    ##  @return state (@link State NXOpen.Layer.State@endlink):  .
    ## 
    ##   <br>  Created in NX3.0.0  <br> 

    ## License requirements: None.
    ##  
    def GetState(self, layer: int) -> State:
        """
         Returns the state of the specified layer 
         @return state (@link State NXOpen.Layer.State@endlink):  .
        """
        pass
    
    ##  Sets the state of the specified layer 
    ## 
    ##   <br>  Created in NX3.0.0  <br> 

    ## License requirements: None.
    ##  
    def SetState(self, layer: int, state: State) -> None:
        """
         Sets the state of the specified layer 
        """
        pass
    
    ##  Sets the state of every layer in the category to the
    ##         specified state, except the work layer  
    ## 
    ##   <br>  Created in NX3.0.0  <br> 

    ## License requirements: None.
    ##  
    def SetStateOfCategory(self, category: Category, state: State) -> None:
        """
         Sets the state of every layer in the category to the
                specified state, except the work layer  
        """
        pass
    
##  Used in several methods that get or set the state of a layer 
class StateInfo:
    """
     Used in several methods that get or set the state of a layer 
    """
    ## Getter for property :(int) Layer
    ## Layer number
    ## @return int
    @property
    def Layer(self) -> int:
        """
        Getter for property Layer
        Layer number

        """
        pass
    
    ## Setter for property :(int) Layer
    @Layer.setter
    def Layer(self, value: int):
        """
        Getter for property Layer
        Layer number
        Setter for property Layer
        Layer number

        """
        pass
    
    ## Getter for property :(@link State NXOpen.Layer.State@endlink) State
    ## The state of the layer
    ## @return @link State NXOpen.Layer.State@endlink
    @property
    def State(self) -> State:
        """
        Getter for property State
        The state of the layer

        """
        pass
    
    ## Setter for property :(@link State NXOpen.Layer.State@endlink) State
    @State.setter
    def State(self, value: State):
        """
        Getter for property State
        The state of the layer
        Setter for property State
        The state of the layer

        """
        pass
    


##  Represents the state of the layer 
##  Work layer.  All newly created objects are placed on the work layer.
class State(Enum):
    """
    Members Include: <WorkLayer> <Selectable> <Visible> <Hidden>
    """
    WorkLayer: int
    Selectable: int
    Visible: int
    Hidden: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> State:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


## @package NXOpen.Layer
## Classes, Enums and Structs under NXOpen.Layer namespace

