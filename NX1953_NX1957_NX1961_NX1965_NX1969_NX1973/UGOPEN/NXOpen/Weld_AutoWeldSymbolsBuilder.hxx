#ifndef NXOpen_WELD_AUTOWELDSYMBOLSBUILDER_HXX_INCLUDED
#define NXOpen_WELD_AUTOWELDSYMBOLSBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Weld_AutoWeldSymbolsBuilder.ja
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
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/libnxopencpp_weld_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Weld
    {
        class AutoWeldSymbolsBuilder;
    }
    class Builder;
    namespace Drawings
    {
        class SelectDraftingViewList;
    }
    class SelectNXObjectList;
    namespace Weld
    {
        class _AutoWeldSymbolsBuilderBuilder;
        class AutoWeldSymbolsBuilderImpl;
        /** Represents a @link NXOpen::Weld::AutoWeldSymbolsBuilder NXOpen::Weld::AutoWeldSymbolsBuilder@endlink  builder  <br> To create a new instance of this class, use @link NXOpen::Weld::WeldManager::CreateAutoWeldSymbolsBuilder  NXOpen::Weld::WeldManager::CreateAutoWeldSymbolsBuilder @endlink  <br> 
         <br>  Created in NX8.0.0.  <br>  
        */
        class NXOPENCPP_WELDEXPORT  AutoWeldSymbolsBuilder : public NXOpen::Builder
        {
            private: AutoWeldSymbolsBuilderImpl * m_autoweldsymbolsbuilder_impl;
            private: friend class  _AutoWeldSymbolsBuilderBuilder;
            protected: AutoWeldSymbolsBuilder();
            public: ~AutoWeldSymbolsBuilder();
            /**Returns  the candidate views for weld symbol creation  
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Drawings::SelectDraftingViewList * DraftingViews
            (
            );
            /**Returns  the weld objects used to create the weld symbols in the drafting views 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectNXObjectList * Welds
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
