#ifndef NXOpen_LAYOUT2D_CONVERTSHEETTOLAYOUTBUILDER_HXX_INCLUDED
#define NXOpen_LAYOUT2D_CONVERTSHEETTOLAYOUTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Layout2d_ConvertSheetToLayoutBuilder.ja
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
#include <NXOpen/Layout2d_LayoutDrawingSheetBuilder.hxx>
#include <NXOpen/SelectObject.hxx>
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
        class ConvertSheetToLayoutBuilder;
    }
    namespace Layout2d
    {
        class LayoutDrawingSheetBuilder;
    }
    class SelectView;
    namespace Layout2d
    {
        class _ConvertSheetToLayoutBuilderBuilder;
        class ConvertSheetToLayoutBuilderImpl;
        /** Represents a Builder for converting a drawing sheet to Layout  <br> To create a new instance of this class, use @link NXOpen::Layout2d::LayoutDrawingSheetCollection::CreateConvertSheetToLayoutBuilder  NXOpen::Layout2d::LayoutDrawingSheetCollection::CreateConvertSheetToLayoutBuilder @endlink  <br> 
         <br>  Created in NX12.0.0.  <br>  
        */
        class NXOPENCPP_LAYOUT2DEXPORT  ConvertSheetToLayoutBuilder : public NXOpen::Layout2d::LayoutDrawingSheetBuilder
        {
            private: ConvertSheetToLayoutBuilderImpl * m_convertsheettolayoutbuilder_impl;
            private: friend class  _ConvertSheetToLayoutBuilderBuilder;
            protected: ConvertSheetToLayoutBuilder();
            public: ~ConvertSheetToLayoutBuilder();
            /**Returns  the select drawing sheet to convert
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectView * SelectSheetView
            (
            );
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
