#ifndef NXOpen_GEOMETRICUTILITIES_REPLACEMATCHLISTITEM_HXX_INCLUDED
#define NXOpen_GEOMETRICUTILITIES_REPLACEMATCHLISTITEM_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     GeometricUtilities_ReplaceMatchListItem.ja
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
#include <NXOpen/libnxopencpp_geometricutilities_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace GeometricUtilities
    {
        class ReplaceMatchListItem;
    }
    class Builder;
    namespace GeometricUtilities
    {
        class _ReplaceMatchListItemBuilder;
        class ReplaceMatchListItemImpl;
        /**Used to select matches for Replace Design Part Manual Match Dialog  <br> To create a new instance of this class, use @link NXOpen::GeometricUtilities::ReplaceManualMatchBuilder::CreateReplaceMatchListItem  NXOpen::GeometricUtilities::ReplaceManualMatchBuilder::CreateReplaceMatchListItem @endlink  <br> 
         <br>  Created in NX2007.0.0.  <br>  
        */
        class NXOPENCPP_GEOMETRICUTILITIESEXPORT  ReplaceMatchListItem : public NXOpen::Builder
        {
            private: ReplaceMatchListItemImpl * m_replacematchlistitem_impl;
            private: friend class  _ReplaceMatchListItemBuilder;
            protected: ReplaceMatchListItem();
            public: ~ReplaceMatchListItem();
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
