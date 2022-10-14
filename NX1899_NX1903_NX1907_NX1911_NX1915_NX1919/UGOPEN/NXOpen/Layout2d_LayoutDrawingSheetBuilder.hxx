#ifndef NXOpen_LAYOUT2D_LAYOUTDRAWINGSHEETBUILDER_HXX_INCLUDED
#define NXOpen_LAYOUT2D_LAYOUTDRAWINGSHEETBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Layout2d_LayoutDrawingSheetBuilder.ja
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
#include <NXOpen/Drawings_DrawingSheetBuilder.hxx>
#include <NXOpen/libnxopencpp_layout2d_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Layout2d
    {
        class LayoutDrawingSheetBuilder;
    }
    namespace Drawings
    {
        class DrawingSheetBuilder;
    }
    namespace Layout2d
    {
        class _LayoutDrawingSheetBuilderBuilder;
        class LayoutDrawingSheetBuilderImpl;
        /** Represents a Builder for creating @link Layout2d::LayoutDrawingSheet Layout2d::LayoutDrawingSheet@endlink s  <br> To create a new instance of this class, use @link NXOpen::Layout2d::LayoutDrawingSheetCollection::CreateLayoutDrawingSheetBuilder  NXOpen::Layout2d::LayoutDrawingSheetCollection::CreateLayoutDrawingSheetBuilder @endlink  <br> 
         <br>  Created in NX12.0.0.  <br>  
        */
        class NXOPENCPP_LAYOUT2DEXPORT  LayoutDrawingSheetBuilder : public NXOpen::Drawings::DrawingSheetBuilder
        {
            private: LayoutDrawingSheetBuilderImpl * m_layoutdrawingsheetbuilder_impl;
            private: friend class  _LayoutDrawingSheetBuilderBuilder;
            protected: LayoutDrawingSheetBuilder();
            public: ~LayoutDrawingSheetBuilder();
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