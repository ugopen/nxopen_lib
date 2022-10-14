#ifndef NXOpen_ASSEMBLIES_PROXIMITYSEARCHTERM_HXX_INCLUDED
#define NXOpen_ASSEMBLIES_PROXIMITYSEARCHTERM_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Assemblies_ProximitySearchTerm.ja
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
#include <NXOpen/Assemblies_SearchTerm.hxx>
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
        class ProximitySearchTerm;
    }
    namespace Assemblies
    {
        class SearchTerm;
    }
    namespace Assemblies
    {
        class _ProximitySearchTermBuilder;
        class ProximitySearchTermImpl;
        /**
                A proximity search term within a @link Assemblies::SubsetRecipe Assemblies::SubsetRecipe@endlink .
             <br> To create or edit an instance of this class, use @link Assemblies::ProximitySearchTermBuilder  Assemblies::ProximitySearchTermBuilder @endlink  <br> 
         <br>  Created in NX8.5.0.  <br>  
        */
        class NXOPENCPP_ASSEMBLIESEXPORT  ProximitySearchTerm : public Assemblies::SearchTerm
        {
            private: ProximitySearchTermImpl * m_proximitysearchterm_impl;
            private: friend class  _ProximitySearchTermBuilder;
            protected: ProximitySearchTerm();
            public: ~ProximitySearchTerm();
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