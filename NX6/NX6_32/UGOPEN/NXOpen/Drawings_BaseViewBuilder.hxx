#ifndef NXOpen_DRAWINGS_BASEVIEWBUILDER_HXX_INCLUDED
#define NXOpen_DRAWINGS_BASEVIEWBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Drawings_BaseViewBuilder.ja
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
#include <NXOpen/Builder.hxx>
#include <NXOpen/Drawings_BaseViewBuilder.hxx>
#include <NXOpen/Drawings_HiddenObjectsBuilder.hxx>
#include <NXOpen/Drawings_SelectModelViewBuilder.hxx>
#include <NXOpen/Drawings_ViewPlacementBuilder.hxx>
#include <NXOpen/Drawings_ViewScaleBuilder.hxx>
#include <NXOpen/Drawings_ViewStyleBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Drawings
    {
        class BaseViewBuilder;
    }
    class Builder;
    namespace Drawings
    {
        class HiddenObjectsBuilder;
    }
    namespace Drawings
    {
        class SelectModelViewBuilder;
    }
    namespace Drawings
    {
        class ViewPlacementBuilder;
    }
    namespace Drawings
    {
        class ViewScaleBuilder;
    }
    namespace Drawings
    {
        class ViewStyleBuilder;
    }
    namespace Drawings
    {
        class _BaseViewBuilderBuilder;
        /** Represents a @link Drawings::BaseView Drawings::BaseView@endlink  builder  <br> To create a new instance of this class, use @link Drawings::DraftingViewCollection::CreateBaseViewBuilder Drawings::DraftingViewCollection::CreateBaseViewBuilder@endlink  <br> 
        Default values:
        Placement.AlignmentMethod: Infer
        Placement.AlignmentOption: ToView
        Scale.Denominator: 1.0
        Scale.Numerator: 1.0
        Scale.ScaleType: Ratio
        Style.ViewStyleOrientation.HingeLine.ReverseDirection: false
        Style.ViewStyleOrientation.HingeLine.VectorOption: Inferred
        Style.ViewStyleOrientation.Ovt.AssociativeOrientation: 0
        */
        class NXOPENCPPEXPORT BaseViewBuilder : public Builder
        {
            private: friend class  _BaseViewBuilderBuilder;
            protected: BaseViewBuilder();
            /**Returns  the view placement  <br> License requirements : None */
            public: NXOpen::Drawings::ViewPlacementBuilder * Placement
            (
            );
            /**Returns  the model view  <br> License requirements : None */
            public: NXOpen::Drawings::SelectModelViewBuilder * SelectModelView
            (
            );
            /**Returns  the view scale  <br> License requirements : None */
            public: NXOpen::Drawings::ViewScaleBuilder * Scale
            (
            );
            /**Returns  the view style  <br> License requirements : None */
            public: NXOpen::Drawings::ViewStyleBuilder * Style
            (
            );
            /**Returns  the list of objects to not show in the view  <br> License requirements : None */
            public: NXOpen::Drawings::HiddenObjectsBuilder * HiddenObjects
            (
            );
            /**Returns  the list of objects to not section in the view  <br> License requirements : None */
            public: NXOpen::Drawings::HiddenObjectsBuilder * NonSectionedObjects
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
