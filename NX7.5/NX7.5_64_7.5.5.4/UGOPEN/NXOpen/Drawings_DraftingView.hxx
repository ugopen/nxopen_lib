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
#include <NXOpen/libnxopencpp_exports.hxx>
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
        /** Represents a drafting view.  <br> To obtain an instance of this class, see 
                @link Drawings::DrawingSheet::GetDraftingViews Drawings::DrawingSheet::GetDraftingViews@endlink  <br> */
        class NXOPENCPPEXPORT  DraftingView : public View, public virtual IFitTo
        {
            private: DraftingViewImpl * m_draftingview_impl;
            private: friend class  _DraftingViewBuilder;
            protected: DraftingView();
            public: ~DraftingView();
            /** Updates the drawing member view on a drawing. The view update
                        process includes updating the view bounds, resectioning section views,
                        updating silhouettes, and updating hidden line display when
                        applicable.
                     <br> License requirements : drafting ("DRAFTING") */
            public: void Update
            (
            );
            /**Returns  the status on whether this @link DraftingView DraftingView@endlink  is out of date.  <br> License requirements : None */
            public: bool IsOutOfDate
            (
            );
            /** Returns the view origin(location). @return  View origin(location)  <br> License requirements : drafting ("DRAFTING") */
            public: NXOpen::Point3d GetDrawingReferencePoint
            (
            );
            /** Sets the view origin at the provided location. <br> License requirements : drafting ("DRAFTING") */
            public: void SetDrawingReferencePoint
            (
                const NXOpen::Point3d & drawingReferencePoint /** New view origin(location) */
            );
            /** Sets the view origin at the provided location. <br> License requirements : drafting ("DRAFTING") */
            public: void MoveView
            (
                const NXOpen::Point3d & drawingReferencePoint /** New view origin(location) */
            );
            /** Sets the view origin at the provided location. <br> License requirements : drafting ("DRAFTING") */
            public: void HideComponents
            (
                const std::vector<NXOpen::NXObject *> & components /** Components */
            );
            /** Sets the view origin at the provided location. <br> License requirements : drafting ("DRAFTING") */
            public: void ShowComponents
            (
                const std::vector<NXOpen::NXObject *> & components /** Components */
            );
            /** Sets this drafting view as the active sketch view.  <br> License requirements : drafting ("DRAFTING") */
            public: void ActivateForSketching
            (
            );
            /**Returns  true if this view is the active sketch view.   <br> License requirements : drafting ("DRAFTING") */
            public: bool IsActiveForSketching
            (
            );
            /** Commits and applies all the settings like @link Drawings::ViewStyle Drawings::ViewStyle@endlink  to the View.This must be called on the view after creation or edit to reflect all the settings on it <br> License requirements : drafting ("DRAFTING") */
            public: void Commit
            (
            );
            /** Returns an array of pointers to objects representing the tool markers in the
                        view. Pertains to flat pattern views. Other views return zero objects.  <br> License requirements : drafting ("DRAFTING") OR sheet_metal ("SHEET METAL DESIGN") */
            public: void GetToolMarkers
            (
                std::vector<NXOpen::Drawings::FlatPatternObject *> & markers /** markers */ 
            );
            /** Checks the view's validity by looking at the parent model view  <br> License requirements : drafting ("DRAFTING") */
            public: void CheckForInvalidParentModelView
            (
            );


            /** Returns object to View Style */
            public: NXOpen::Drawings::ViewStyle *Style();
            /** Returns the ViewBreakCollection instance belonging to this view */
            public: NXOpen::Drawings::ViewBreakCollection *ViewBreaks();
        };
    }
}
#undef EXPORTLIBRARY
#endif