#ifndef NXOpen_DRAWINGS_VIEWCOPYTO3DBUILDER_HXX_INCLUDED
#define NXOpen_DRAWINGS_VIEWCOPYTO3DBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Drawings_ViewCopyTo3dBuilder.ja
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
#include <NXOpen/Drawings_ViewCopyTo3dBuilder.hxx>
#include <NXOpen/GeometricUtilities_IComponentBuilder.hxx>
#include <NXOpen/SelectObject.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Drawings
    {
        class ViewCopyTo3dBuilder;
    }
    namespace Drawings
    {
        class DrawingView;
    }
    namespace Drawings
    {
        class SelectDrawingView;
    }
    namespace GeometricUtilities
    {
        class IComponentBuilder;
    }
    namespace Drawings
    {
        class _ViewCopyTo3dBuilderBuilder;
        /**
            Represents a @link Drawings::ViewCopyTo3dBuilder Drawings::ViewCopyTo3dBuilder@endlink .  This class
            is used to copy the contents of a drawing view to modeling space
             <br> To create a new instance of this class, use @link Drawings::DraftingViewCollection::CreateCopyTo3dBuilder Drawings::DraftingViewCollection::CreateCopyTo3dBuilder@endlink  <br> */
        class NXOPENCPPEXPORT ViewCopyTo3dBuilder : public TaggedObject, public virtual GeometricUtilities::IComponentBuilder
        {
            private: friend class  _ViewCopyTo3dBuilderBuilder;
            protected: ViewCopyTo3dBuilder();
            /**Returns  the selected view  <br> License requirements : nx_drafting_plus ("Drafting Plus") */
            public: NXOpen::Drawings::SelectDrawingView * View
            (
            );
            /** Specify the drawing view to process  <br> License requirements : nx_drafting_plus ("Drafting Plus") */
            public: void SelectView
            (
                NXOpen::Drawings::DrawingView * view /** the view to copy from */
            );
            /** Send the selected view to modeling  <br> License requirements : nx_drafting_plus ("Drafting Plus") */
            public: void Commit
            (
                double offset /** offset from origin */,
                bool curves /** process curves */,
                bool sketches /** process sketch curves */,
                bool dimensions /** process dimensions */
            );
            /** Returns true if the inputs to the component are sufficient for 
                        commit to be called.  For example, if the component requires
                        you to set some property, this method will return false if
                        you haven't set it.  This method throws a not-yet-implemented
                        NXException for some components.
                     @return  Was self validation successful  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: virtual bool Validate
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
