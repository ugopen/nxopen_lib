#ifndef NXOpen_DIAGRAMMING_SHEETSIZEBUILDER_HXX_INCLUDED
#define NXOpen_DIAGRAMMING_SHEETSIZEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Diagramming_SheetSizeBuilder.ja
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
#include <NXOpen/libnxopencpp_diagramming_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Diagramming
    {
        class SheetSizeBuilder;
    }
    class Builder;
    namespace Diagramming
    {
        class _SheetSizeBuilderBuilder;
        class SheetSizeBuilderImpl;
        /** Represents a @link NXOpen::Diagramming::SheetSizeBuilder NXOpen::Diagramming::SheetSizeBuilder@endlink  builder, and the builder is used to model a sheet size.  <br> To create a new instance of this class, use @link NXOpen::Diagramming::DiagrammingManager::CreateSheetSizeBuilder  NXOpen::Diagramming::DiagrammingManager::CreateSheetSizeBuilder @endlink  <br> 
         <br>  Created in NX1980.0.0.  <br>  
        */
        class NXOPENCPP_DIAGRAMMINGEXPORT  SheetSizeBuilder : public NXOpen::Builder
        {
            private: SheetSizeBuilderImpl * m_sheetsizebuilder_impl;
            private: friend class  _SheetSizeBuilderBuilder;
            protected: SheetSizeBuilder();
            public: ~SheetSizeBuilder();
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
