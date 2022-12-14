#ifndef NXOpen_ASSEMBLIES_SEARCHTERMBUILDER_HXX_INCLUDED
#define NXOpen_ASSEMBLIES_SEARCHTERMBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Assemblies_SearchTermBuilder.ja
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
#include <NXOpen/libnxopencpp_assemblies_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Assemblies
    {
        class SearchTermBuilder;
    }
    class Builder;
    namespace Assemblies
    {
        class _SearchTermBuilderBuilder;
        class SearchTermBuilderImpl;
        /**
                A SearchTermBuilder is used to create or edit an @link Assemblies::SearchTerm Assemblies::SearchTerm@endlink .
                This is the abstract base class for builders used to create search terms.
             <br> No creator is available because this is an abstract class.  <br> 
         <br>  Created in NX8.5.0.  <br>  
        */
        class NXOPENCPP_ASSEMBLIESEXPORT  SearchTermBuilder : public NXOpen::Builder
        {
            private: SearchTermBuilderImpl * m_searchtermbuilder_impl;
            private: friend class  _SearchTermBuilderBuilder;
            protected: SearchTermBuilder();
            public: ~SearchTermBuilder();
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
