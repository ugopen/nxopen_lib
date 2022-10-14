#ifndef NXOpen_DRAWINGS_BASEVIEW_HXX_INCLUDED
#define NXOpen_DRAWINGS_BASEVIEW_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Drawings_BaseView.ja
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
        class BaseView;
    }
    namespace Drawings
    {
        class DraftingView;
    }
    namespace Drawings
    {
        class _BaseViewBuilder;
        class BaseViewImpl;
        /** Represents a Base View. 
                A base view is a modeling view that you import onto a drawing.
                The base view can be a standalone view or a parent view
                for other drawings types such as a section view. */
        class NXOPENCPPEXPORT  BaseView : public Drawings::DraftingView
        {
            private: BaseViewImpl * m_baseview_impl;
            private: friend class  _BaseViewBuilder;
            protected: BaseView();
            public: ~BaseView();
        };
    }
}
#undef EXPORTLIBRARY
#endif