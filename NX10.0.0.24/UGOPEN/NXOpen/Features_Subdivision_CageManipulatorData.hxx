#ifndef NXOpen_FEATURES_SUBDIVISION_CAGEMANIPULATORDATA_HXX_INCLUDED
#define NXOpen_FEATURES_SUBDIVISION_CAGEMANIPULATORDATA_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_Subdivision_CageManipulatorData.ja
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
#include <NXOpen/Features_Subdivision_CageManipulatorData.hxx>
#include <NXOpen/GeometricUtilities_TransformerData.hxx>
#include <NXOpen/Features_Subdivision_SelectCageObjectData.hxx>
#include <NXOpen/ugmath.hxx>
#include <NXOpen/libnxopencpp_features_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Features
    {
        namespace Subdivision
        {
            class CageManipulatorData;
        }
    }
    namespace Features
    {
        namespace Subdivision
        {
            class SelectCageObjectData;
        }
    }
    namespace GeometricUtilities
    {
        class TransformerData;
    }
    class NXObject;
    class Point;
    class View;
    namespace Features
    {
        namespace Subdivision
        {
            class _CageManipulatorDataBuilder;
            class CageManipulatorDataImpl;
            /** Subdivision cage manipulation tool.
                    
             <br>  Created in NX9.0.0.  <br>  
            */
            class NXOPENCPP_FEATURESEXPORT  CageManipulatorData : public NXOpen::Features::Subdivision::SelectCageObjectData
            {
                 /** Contains object movement information. 
                 <br>  Created in NX9.0.0.  <br>  
                */
                public:
                struct  ObjectMoveData
                {
                    public: /** The dragged object. */NXOpen::NXObject * DraggedObject;
                    public: /** The point from which object dragging is initiated, the point
                                                                                  under the cursor when seen in view direction. */NXOpen::Point3d BeginDragCursorPosition;
                    public: /** The point on object near cursor from which object dragging is initiated */NXOpen::Point3d BeginDragObjectPosition;
                    public: /** The view in which object is dragged. */NXOpen::View * View;
                    public: /** The micropositioning scale. */double MicropositioningScale;
                    public: /** The view direction. */NXOpen::Vector3d ViewDirection;
                    public: ObjectMoveData() :
                        DraggedObject(),
                        BeginDragCursorPosition(),
                        BeginDragObjectPosition(),
                        View(),
                        MicropositioningScale(),
                        ViewDirection()
                    {
                    }
                    /** Constructor for the ObjectMoveData struct. */ 
                    public: ObjectMoveData(NXOpen::NXObject * draggedObjectInitial /** The dragged object. */, 
                            const NXOpen::Point3d &beginDragCursorPositionInitial /** The point from which object dragging is initiated, the point
                                                                                          under the cursor when seen in view direction. */, 
                            const NXOpen::Point3d &beginDragObjectPositionInitial /** The point on object near cursor from which object dragging is initiated */, 
                            NXOpen::View * viewInitial /** The view in which object is dragged. */, 
                            double micropositioningScaleInitial /** The micropositioning scale. */, 
                            const NXOpen::Vector3d &viewDirectionInitial /** The view direction. */) :
                        DraggedObject(draggedObjectInitial),
                        BeginDragCursorPosition(beginDragCursorPositionInitial),
                        BeginDragObjectPosition(beginDragObjectPositionInitial),
                        View(viewInitial),
                        MicropositioningScale(micropositioningScaleInitial),
                        ViewDirection(viewDirectionInitial)
                    {
                    }
                };

                 /** Contains object selection information. 
                 <br>  Created in NX9.0.0.  <br>  
                */
                public:
                struct  ObjectSelectionData
                {
                    public: /** The selected object. */NXOpen::NXObject * SelectedObject;
                    public: /** The point at which object is selected, the point
                                                                             under the cursor when seen in view direction.
                                                                         */NXOpen::Point3d SelectionPosition;
                    public: /** The view direction.
                                                                         */NXOpen::Vector3d ViewDirection;
                    public: /** Is SelectionPosition a snapped location. */bool IsSnappedPosition;
                    public: ObjectSelectionData() :
                        SelectedObject(),
                        SelectionPosition(),
                        ViewDirection(),
                        IsSnappedPosition()
                    {
                    }
                    /** Constructor for the ObjectSelectionData struct. */ 
                    public: ObjectSelectionData(NXOpen::NXObject * selectedObjectInitial /** The selected object. */, 
                            const NXOpen::Point3d &selectionPositionInitial /** The point at which object is selected, the point
                                                                                     under the cursor when seen in view direction.
                                                                                 */, 
                            const NXOpen::Vector3d &viewDirectionInitial /** The view direction.
                                                                                 */, 
                            bool isSnappedPositionInitial /** Is SelectionPosition a snapped location. */) :
                        SelectedObject(selectedObjectInitial),
                        SelectionPosition(selectionPositionInitial),
                        ViewDirection(viewDirectionInitial),
                        IsSnappedPosition(isSnappedPositionInitial)
                    {
                    }
                };

                private: CageManipulatorDataImpl * m_cagemanipulatordata_impl;
                private: friend class  _CageManipulatorDataBuilder;
                protected: CageManipulatorData();
                public: ~CageManipulatorData();
                /**Returns  the transformation tool. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::GeometricUtilities::TransformerData * Transformer
                (
                );
                /** Prepares data to move the objects. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_subdivision (" NX SUBDIVISION") */
                public: void PrepareToMove
                (
                    const NXOpen::Features::Subdivision::CageManipulatorData::ObjectMoveData & moveData /** movedata */ 
                );
                /** Moves the objects by dragging. 
                 <br>  @deprecated Deprecated in NX10.0.0.  Use @link NXOpen::Features::Subdivision::CageManipulatorData::Move NXOpen::Features::Subdivision::CageManipulatorData::Move@endlink  with optional constraint point instead. <br>  

                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_subdivision (" NX SUBDIVISION") */
                public:  NX_DEPRECATED("Deprecated in NX10.0.0.  Use NXOpen::Features::Subdivision::CageManipulatorData::Move with optional constraint point instead.") void Move
                (
                    const NXOpen::Point3d & moveToPoint /** movetopoint */ ,
                    bool isSnapGesture /** Are we processing a snap gesture. */
                );
                /** Moves the objects by dragging. A constraint point can be assigned when moving a vertex. 
                 <br>  Created in NX10.0.0.  <br>  
                 <br> License requirements : nx_subdivision (" NX SUBDIVISION") */
                public: void Move
                (
                    const NXOpen::Point3d & moveToPoint /** movetopoint */ ,
                    NXOpen::Point * point /** Optional constraint point */,
                    bool isSnapGesture /** Are we processing a snap gesture. */
                );
                /** Releases the data prepared at the beginning of the move. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_subdivision (" NX SUBDIVISION") */
                public: void EndMove
                (
                );
                /** Moves the objects by step value. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_subdivision (" NX SUBDIVISION") */
                public: void StepMove
                (
                    double step /** step */ 
                );
                /** Repositions the @link NXOpen::GeometricUtilities::TransformerData NXOpen::GeometricUtilities::TransformerData@endlink  to the centroid of the selected entities. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_subdivision (" NX SUBDIVISION") */
                public: void ResetTransformerToCentroidOfSelection
                (
                );
                /** Repositions the @link NXOpen::GeometricUtilities::TransformerData NXOpen::GeometricUtilities::TransformerData@endlink  to the specified entity. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_subdivision (" NX SUBDIVISION") */
                public: void SetTransformerToObject
                (
                    const NXOpen::Features::Subdivision::CageManipulatorData::ObjectSelectionData & selectionData /** selectiondata */ 
                );
            };
        }
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
