#ifndef NXOpen_DRAWINGS_DRAFTINGVIEW_HXX_INCLUDED
#define NXOpen_DRAWINGS_DRAFTINGVIEW_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Drawings_DraftingView.ja
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
#include <NXOpen/Drawings_FlatPatternObject.hxx>
#include <NXOpen/IFitTo.hxx>
#include <NXOpen/INXObject.hxx>
#include <NXOpen/View.hxx>
#include <NXOpen/ugmath.hxx>
#include <NXOpen/libnxopencpp_drawings_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Drawings
    {
        class DraftingView;
    }
    namespace Assemblies
    {
        class Component;
    }
    class BasePart;
    namespace Drawings
    {
        class DraftingBodyCollection;
    }
    namespace Drawings
    {
        class FlatPatternObject;
    }
    namespace Drawings
    {
        class ViewBreakCollection;
    }
    namespace Drawings
    {
        class ViewStyle;
    }
    class IFitTo;
    class INXObject;
    class NXObject;
    class View;
    namespace Drawings
    {
        class _DraftingViewBuilder;
        class DraftingViewImpl;
        /** Represents a drafting view.  <br> To obtain an instance of this class, use @link NXOpen::Drawings::DrawingSheet::SheetDraftingViews NXOpen::Drawings::DrawingSheet::SheetDraftingViews@endlink  or @link NXOpen::Part::DraftingViews NXOpen::Part::DraftingViews@endlink   <br> 
         <br>  Created in NX3.0.0.  <br>  
        */
        class NXOPENCPP_DRAWINGSEXPORT  DraftingView : public NXOpen::View, public virtual NXOpen::IFitTo
        {
            private: DraftingViewImpl * m_draftingview_impl;
            private: friend class  _DraftingViewBuilder;
            protected: DraftingView();
            public: ~DraftingView();
            /** Updates the drawing member view on a drawing. The view update
                        process includes updating the view bounds, resectioning section views,
                        updating silhouettes, and updating hidden line display when
                        applicable.
                    
             <br>  Created in NX3.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void Update
            (
            );
            /**Returns  the status on whether this @link NXOpen::Drawings::DraftingView NXOpen::Drawings::DraftingView@endlink  is out of date. 
             <br>  Created in NX3.0.0.  <br>  
             <br> License requirements : None */
            public: bool IsOutOfDate
            (
            );
            /** Returns the view origin(location). @return  View origin(location) 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: NXOpen::Point3d GetDrawingReferencePoint
            (
            );
            /** Sets the view origin at the provided location.
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetDrawingReferencePoint
            (
                const NXOpen::Point3d & drawingReferencePoint /** New view origin(location) */
            );
            /** Sets the view origin at the provided location. This method is quite similar 
                        @link NXOpen::Drawings::DraftingView::SetDrawingReferencePoint NXOpen::Drawings::DraftingView::SetDrawingReferencePoint@endlink  and 
                        handles section views and broken views cases also.
                    
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void MoveView
            (
                const NXOpen::Point3d & drawingReferencePoint /** New view origin(location) */
            );
            /** Hides the specified components in the view.
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void HideComponents
            (
                const std::vector<NXOpen::NXObject *> & components /** Components */
            );
            /** Shows the specified components in the view.
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void ShowComponents
            (
                const std::vector<NXOpen::NXObject *> & components /** Components */
            );
            /** Sets this drafting view as the active sketch view. 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void ActivateForSketching
            (
            );
            /**Returns  true if this view is the active sketch view.  
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: bool IsActiveForSketching
            (
            );
            /** Commits and applies all the settings like @link NXOpen::Drawings::ViewStyle NXOpen::Drawings::ViewStyle@endlink  to the View.This must be called on the view after creation or edit to reflect all the settings on it
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void Commit
            (
            );
            /** Returns an array of pointers to objects representing the tool markers in the
                        view. Pertains to flat pattern views. Other views return zero objects. 
             <br>  Created in NX6.0.3.  <br>  
             <br> License requirements : drafting ("DRAFTING") OR sheet_metal ("SHEET METAL DESIGN") */
            public: void GetToolMarkers
            (
                std::vector<NXOpen::Drawings::FlatPatternObject *> & markers /** markers */ 
            );
            /** Restores the view border from the dashed line to the normal line for cut operation
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void RestoreViewBorder
            (
            );
            /** Checks the view's validity by looking at the parent model view 
             <br>  Created in NX8.0.3.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void CheckForInvalidParentModelView
            (
            );
            /**Returns  the status on whether this @link NXOpen::Drawings::DraftingView NXOpen::Drawings::DraftingView@endlink  is broken. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: bool IsBroken
            (
            );
            /**Returns  the status on whether this @link NXOpen::Drawings::DraftingView NXOpen::Drawings::DraftingView@endlink  is slave. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: bool IsSlave
            (
            );
            /**Returns  the status on whether this @link NXOpen::Drawings::DraftingView NXOpen::Drawings::DraftingView@endlink  is decoration. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: bool IsDecoration
            (
            );
            /** Return the master view of a slave or a decoration view. return NULL for other type of view.  @return  
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Drawings::DraftingView * GetBrokenViewMaster
            (
            );
            /** Return the decoration view of a slave or a master view. If the view is a decoration view, return this view. return NULL for other type of view.  @return  
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Drawings::DraftingView * GetBrokenViewDecoration
            (
            );
            /** Returns an array of views representing the internal views of broken view. Other views return zero objects. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void GetBrokenViewInternalViews
            (
                std::vector<NXOpen::Drawings::DraftingView *> & views /** views */ 
            );
            /** Hide the view border of the view. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void HideViewBorder
            (
            );
            /** Show the view border of the view. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void ShowViewBorder
            (
            );
            /** Set the section line delete option, If false section line will not be deleted with section view 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetDeleteSectionLine
            (
                bool deleteSectionLine /** deletesectionline */ 
            );
            /** Recalculates and updates the view boundary of a drawing member view
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void UpdateAutomaticViewBound
            (
            );


            /** Returns object to View Style 
             <br>  Created in NX3.0.0.  <br>  
            */
            public: NXOpen::Drawings::ViewStyle *Style();
            /** Returns the ViewBreakCollection instance belonging to this view 
             <br>  Created in NX7.5.0.  <br>  
            */
            public: NXOpen::Drawings::ViewBreakCollection *ViewBreaks();
            /** Returns the DraftingBodyCollection 
             <br>  Created in NX8.5.0.  <br>  
            */
            public: NXOpen::Drawings::DraftingBodyCollection *DraftingBodies();
        };
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