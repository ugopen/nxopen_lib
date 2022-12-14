#ifndef NXOpen_TOOLDESIGNER_SEARCHDATUMSBUILDER_HXX_INCLUDED
#define NXOpen_TOOLDESIGNER_SEARCHDATUMSBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     ToolDesigner_SearchDatumsBuilder.ja
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
#include <NXOpen/libtooldesigneropencpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace ToolDesigner
    {
        class SearchDatumsBuilder;
    }
    class Builder;
    namespace ToolDesigner
    {
        class _SearchDatumsBuilderBuilder;
        class SearchDatumsBuilderImpl;
        /** SearchDatumsBuilder  <br> To create a new instance of this class, use @link NXOpen::ToolDesigner::ToolDesignerManager::CreateSearchDatumsBuilder  NXOpen::ToolDesigner::ToolDesignerManager::CreateSearchDatumsBuilder @endlink  <br> 
         <br>  Created in NX10.0.0.  <br>  
        */
        class TOOLDESIGNEROPENCPPEXPORT  SearchDatumsBuilder : public NXOpen::Builder
        {
            private: SearchDatumsBuilderImpl * m_searchdatumsbuilder_impl;
            private: friend class  _SearchDatumsBuilderBuilder;
            protected: SearchDatumsBuilder();
            public: ~SearchDatumsBuilder();
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
