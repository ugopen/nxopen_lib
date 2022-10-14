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
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Callback.hxx>
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
        class ViewStyle;
    }
    class IFitTo;
    class INXObject;
    class NXObject;
    class View;
    namespace Drawings
    {
        class _DraftingViewBuilder;
        /** Represents a drafting view.  <br> To obtain an instance of this class, see 
                @link Drawings::DrawingSheet::GetDraftingViews Drawings::DrawingSheet::GetDraftingViews@endlink  <br> */
        class NXOPENCPPEXPORT DraftingView : public View, public virtual IFitTo
        {
            private: friend class  _DraftingViewBuilder;
            protected: DraftingView();
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


            private: NXOpen::Drawings::ViewStyle *style;
            /** Returns object to View Style */
            public: NXOpen::Drawings::ViewStyle *Style()
            {
                return style;
            }
            public: virtual void initialize();
        };
    }
}
#undef EXPORTLIBRARY
#endif