#ifndef NXOpen_SKETCHINDRAFTINGBUILDER_HXX_INCLUDED
#define NXOpen_SKETCHINDRAFTINGBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     SketchInDraftingBuilder.ja
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
#include <NXOpen/Builder.hxx>
#include <NXOpen/SelectObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    class SketchInDraftingBuilder;
    class Builder;
    class SelectView;
    class _SketchInDraftingBuilderBuilder;
    class SketchInDraftingBuilderImpl;
    /**
            Use the @link NXOpen::SketchInDraftingBuilder NXOpen::SketchInDraftingBuilder@endlink  to create a @link NXOpen::Sketch NXOpen::Sketch@endlink  on a @link NXOpen::Drawings::DraftingView NXOpen::Drawings::DraftingView@endlink  or @link NXOpen::Drawings::DrawingSheet NXOpen::Drawings::DrawingSheet@endlink .
         <br> To create a new instance of this class, use @link NXOpen::SketchCollection::CreateSketchInDraftingBuilder  NXOpen::SketchCollection::CreateSketchInDraftingBuilder @endlink  <br> 
     <br>  Created in NX5.0.0.  <br>  
    */
    class NXOPENCPPEXPORT  SketchInDraftingBuilder : public NXOpen::Builder
    {
        private: SketchInDraftingBuilderImpl * m_sketchindraftingbuilder_impl;
        private: friend class  _SketchInDraftingBuilderBuilder;
        protected: SketchInDraftingBuilder();
        public: ~SketchInDraftingBuilder();
        /**Returns  the selected view.  If unset, the current @link NXOpen::Drawings::DrawingSheet NXOpen::Drawings::DrawingSheet@endlink  will be used.  
         <br>  Created in NX5.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::SelectView * View
        (
        );
    };
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