#ifndef NXOpen_LAYER_LAYERMANAGER_HXX_INCLUDED
#define NXOpen_LAYER_LAYERMANAGER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Layer_LayerManager.ja
//
//  Generated by:
//     apiwrap
//
//  WARNING:
//    This file is automatically generated - do not edit by hand
//
#ifdef _MSC_VER
#pragma once
#endif

#include <NXOpen/NXDeprecation.hxx>
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/Layer.hxx>
#include <NXOpen/Layer_StateCollection.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_layer_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Layer
    {
        class LayerManager;
    }
    class BasePart;
    class DisplayableObject;
    namespace Layer
    {
        class StateCollection;
    }
    class NXObject;
    class View;
    namespace Layer
    {
        class LayerManagerImpl;
        /** Represents an object that manages layers  <br> To obtain an instance of this class, refer to @link NXOpen::BasePart  NXOpen::BasePart @endlink  <br> 
         <br>  Created in NX3.0.0.  <br>  
        */
        class NXOPENCPP_LAYEREXPORT  LayerManager
        {
            private: LayerManagerImpl * m_layermanager_impl;
            private: NXOpen::BasePart* m_owner;
            /// \cond NX_NO_DOC 
            public: explicit LayerManager(NXOpen::BasePart *owner);


            /// \endcond 
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            public: ~LayerManager();
            /**Sets  the work layer.
                    If you change the work layer, the old work layer is changed to Selectable.
                    The part must be the displayed part. 
             <br>  Created in NX3.0.0.  <br>  
             <br> License requirements : None */
            public: void SetWorkLayer
            (
                int newWorkLayer /** Layer number for the new work layer */
            );
            /**Returns  the work layer.
                    If you change the work layer, the old work layer is changed to Selectable.
                    The part must be the displayed part. 
             <br>  Created in NX3.0.0.  <br>  
             <br> License requirements : None */
            public: int WorkLayer
            (
            );
            /** Changes the states of the specified layers in the part. 
                    Note: there must be exactly one work layer.  If you change the work layer,
                    you must specify a new work layer.  If you set the work layer, the
                    old work layer will be changed to Selectable, unless you specify otherwise.
                    The part must be the displayed part.
                    
             <br>  Created in NX3.0.0.  <br>  
             <br> License requirements : None */
            public: void ChangeStates
            (
                const std::vector<NXOpen::Layer::StateInfo> & stateArray /** 
                                Indicates the new states for the layers. */,
                bool fitAll /** Whether to refit the view to what is visible after the layer states have been changed */
            );
            /** Changes the states of the specified layers in the part. 
                    Note: there must be exactly one work layer.  If you change the work layer,
                    you must specify a new work layer.  If you set the work layer, the
                    old work layer will be changed to Selectable, unless you specify otherwise.
                    The part must be the displayed part.
                    
             <br>  Created in NX3.0.0.  <br>  
             <br> License requirements : None */
            public: void ChangeStates
            (
                const std::vector<NXOpen::Layer::StateInfo> & stateArray /** 
                                Indicates the new states for the layers. */
            );
            /** Gets the states for all layers in the part. The part must be the displayed part.  @return  Indicates the states for all layers in the part. 
             <br>  Created in NX3.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Layer::StateCollection * GetStates
            (
            );
            /** Sets the states for all layers in the part.  The part must be the displayed part.
                        Note: there must be exactly one work layer. 
             <br>  Created in NX3.0.0.  <br>  
             <br> License requirements : None */
            public: void SetStates
            (
                NXOpen::Layer::StateCollection * stateCollection /** The states for all layers in the part.  */,
                bool fitAll /** Whether to refit the view to what is visible after the layer states have been changed */
            );
            /** Sets the states for all layers in the part.  The part must be the displayed part.
                        Note: there must be exactly one work layer. 
             <br>  Created in NX3.0.0.  <br>  
             <br> License requirements : None */
            public: void SetStates
            (
                NXOpen::Layer::StateCollection * stateCollection /** The states for all layers in the part.  */
            );
            /** Sets the state of the specified layer.
                    The specified layer must not be the work layer.
                    If you are changing the state of the layer to Work,
                    the old work layer will be changed to Selectable.
                    The part must be the displayed part.
                    
             <br>  Created in NX3.0.0.  <br>  
             <br> License requirements : None */
            public: void SetState
            (
                int layer /** layer */ ,
                NXOpen::Layer::State state /** state */ 
            );
            /** Sets the state of the specified layer.
                    The specified layer must not be the work layer.
                    If you are changing the state of the layer to Work,
                    the old work layer will be changed to Selectable.
                    The part must be the displayed part.
                    
             <br>  Created in NX3.0.0.  <br>  
             <br> License requirements : None */
            public: void SetState
            (
                int layer /** layer */ ,
                NXOpen::Layer::State state /** state */ ,
                bool fitAll /** Whether to refit the view to what is visible after the layer state has been changed */
            );
            /** Gets the state of the specified layer.  The part must be the displayed part.  @return  
             <br>  Created in NX3.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Layer::State GetState
            (
                int layer /** layer */ 
            );
            /** Moves displayable objects to the specified layer.
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
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR drafting ("DRAFTING") */
            public: void MoveDisplayableObjects
            (
                int newLayer /** The layer to move the objects to */,
                const std::vector<NXOpen::DisplayableObject *> & objectArray /** The objects to be moved */
            );
            /** Move the selected objects to the specified layer in their Owning Parts.
                    This only works when a single layer has been selected on the Layer Settings dialog.
                     <br>  The owning parts will be fully loaded if they are not already.
                     <br> 
                     <br>  Objects of class @link NXOpen::CAE::CAEEdge NXOpen::CAE::CAEEdge@endlink ,
                    @link NXOpen::CAE::CAEFace NXOpen::CAE::CAEFace@endlink , @link NXOpen::CAE::CAEVertex NXOpen::CAE::CAEVertex@endlink ,
                    @link NXOpen::Edge NXOpen::Edge@endlink , @link NXOpen::Face NXOpen::Face@endlink  or
                    @link NXOpen::View NXOpen::View@endlink  may not be moved.
                     <br>  
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR drafting ("DRAFTING") */
            public: void ApplyMoveToLayerToOwningParts
            (
                int newLayer /** The layer in the owning parts to move the objects to */,
                const std::vector<NXOpen::DisplayableObject *> & objectArray /** The objects to be moved */
            );
            /** Returns all objects on the specified layer. 
                    This includes objects which are not counted as objects on the layer by the "Layer Settings" dialog.
                     <br>  The part must be the displayed part.  <br>   @return  All the objects on the specified layer 
             <br>  Created in NX3.0.0.  <br>  
             <br> License requirements : None */
            public: std::vector<NXOpen::NXObject *> GetAllObjectsOnLayer
            (
                int layer /** layer */ 
            );
            /** Copies objects to the specified layer
                     <br>  Objects of class @link NXOpen::Assemblies::Component NXOpen::Assemblies::Component@endlink ,
                    @link NXOpen::DatumAxis NXOpen::DatumAxis@endlink , @link NXOpen::DatumPlane NXOpen::DatumPlane@endlink 
                    @link NXOpen::Edge NXOpen::Edge@endlink , @link NXOpen::Face NXOpen::Face@endlink ,
                    @link NXOpen::Features::Feature NXOpen::Features::Feature@endlink  or @link NXOpen::View NXOpen::View@endlink ,
                    may not be copied. <br> 
                     <br>  Objects of type UF_cs2_vertex_type may not be copied.  <br> 
                     <br>  The part must be the work part.  <br> 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR drafting ("DRAFTING") */
            public: void CopyObjects
            (
                int newLayer /** The layer to move the objects to */,
                const std::vector<NXOpen::NXObject *> & objectArray /** The objects to be copied */
            );
            /** Gets the visibility of all layers in a specified view.
                    The part must be the displayed part. 
             <br>  Created in NX4.0.3.  <br>  
             <br> License requirements : None */
            public: void GetVisibilitiesInView
            (
                NXOpen::View * view /** The view object being queried */,
                std::vector<NXOpen::Layer::StateInfo> & stateArray /** The current states for the layers.
                                                                The returned states can only be
                                                                @link Layer::StateVisible Layer::StateVisible@endlink  and
                                                                @link Layer::StateHidden Layer::StateHidden@endlink .
                                                                state_array[i] is for layer i+1 */
            );
            /** Sets specified layer(s) visibility in a specified view.
                    The part must be the displayed part. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public: void SetObjectsVisibilityOnLayer
            (
                NXOpen::View * view /** The view object being modified */,
                const std::vector<NXOpen::Layer::StateInfo> & stateArray /** The new states for the layers.
                                                             The given states may only be
                                                             @link Layer::StateVisible Layer::StateVisible@endlink  and
                                                             @link Layer::StateHidden Layer::StateHidden@endlink . */,
                bool doUpdate /** Whether to update the view(s) after the layer states have been changed */
            );
            /** Resets a view's layer visibility to the global states.
                    The part must be the displayed part. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public: void ResetViewVisibilityToGlobal
            (
                NXOpen::View * view /** The view object */
            );
        }; //lint !e1712 default constructor not defined for class  

    }
}

#ifdef _MSC_VER
#pragma warning(pop)
#endif
#ifdef __GNUC__
#ifndef NX_NO_GCC_DEPRECATION_WARNINGS
#pragma GCC diagnostic warning "-Wdeprecated-declarations"
#endif
#endif

#undef EXPORTLIBRARY
#endif
