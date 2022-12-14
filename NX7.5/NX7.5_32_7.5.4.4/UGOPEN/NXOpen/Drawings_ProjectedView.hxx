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
#ifdef _MSC_VER
#pragma once
#endif

#include <NXOpen/NXDeprecation.hxx>
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
        class ProjectedViewImpl;
        /** Represents a Projected View. This can be Auxilary View or Orthographic View */
        class NXOPENCPPEXPORT  ProjectedView : public Drawings::DraftingView
        {
            private: ProjectedViewImpl * m_projectedview_impl;
            private: friend class  _ProjectedViewBuilder;
            protected: ProjectedView();
            public: ~ProjectedView();
        };
    }
}
#undef EXPORTLIBRARY
#endif
