#ifndef NXOpen_ASSEMBLIES_SEARCHRESULTELEMENT_HXX_INCLUDED
#define NXOpen_ASSEMBLIES_SEARCHRESULTELEMENT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Assemblies_SearchResultElement.ja
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
#include <NXOpen/Assemblies_SearchResultElement.hxx>
#include <NXOpen/NXObject.hxx>
#include <NXOpen/PDM_ModelElementRevision.hxx>
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
        class SearchResultElement;
    }
    class NXObject;
    namespace PDM
    {
        class ModelElementRevision;
    }
    namespace Assemblies
    {
        class _SearchResultElementBuilder;
        class SearchResultElementImpl;
        /**
                A search result element can be produced as the result of a search performed in the context of a @link Assemblies::SubsetBuilder Assemblies::SubsetBuilder@endlink .
                They can be found through @link Assemblies::SubsetBuilder::SearchResults Assemblies::SubsetBuilder::SearchResults@endlink .
             <br> Instances of this object can be accessed through @link Assemblies::SubsetBuilder::SearchResults Assemblies::SubsetBuilder::SearchResults@endlink .  <br> 
         <br>  Created in NX8.5.0.  <br>  
        */
        class NXOPENCPP_ASSEMBLIESEXPORT  SearchResultElement : public NXObject
        {
            private: SearchResultElementImpl * m_searchresultelement_impl;
            private: friend class  _SearchResultElementBuilder;
            protected: SearchResultElement();
            public: ~SearchResultElement();
            /**Returns 
                        the underlying design model revision associated with this search element.
                    
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::PDM::ModelElementRevision * ModelElementRevision
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
