#ifndef NXOpen_DRAWINGS_PROJECTEDVIEW_HXX_INCLUDED
#define NXOpen_DRAWINGS_PROJECTEDVIEW_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Drawings_ProjectedView.ja
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
#include <NXOpen/Drawings_DraftingView.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Drawings
    {
        class ProjectedView;
    }
    namespace Drawings
    {
        class DraftingView;
    }
    namespace Drawings
    {
        class _ProjectedViewBuilder;
        /** Represents a Projected View. This can be Auxilary View or Orthographic View
              <br> To create this, use the method @link Drawings::SheetDraftingViewCollection::CreateProjectedView  Drawings::SheetDraftingViewCollection::CreateProjectedView @endlink  <br> 
              <br> To edit the view use  @link Drawings::DraftingView::StyleDrawings::DraftingView::Style @endlink and @link Drawings::DraftingView::SetStyleDrawings::DraftingView::SetStyle @endlink  property of type @link Drawings::ViewStyle Drawings::ViewStyle@endlink   <br> 
             Either after creation or edit of ProjectedView,Call the method @link Drawings::DraftingView::Commit Drawings::DraftingView::Commit@endlink 
              <br> To obtain an instance of this class, see 
                @link Drawings::SheetDraftingViewCollection Drawings::SheetDraftingViewCollection@endlink  <br> */
        class NXOPENCPPEXPORT ProjectedView : public Drawings::DraftingView
        {
            private: friend class  _ProjectedViewBuilder;
            protected: ProjectedView();
        };
    }
}
#undef EXPORTLIBRARY
#endif