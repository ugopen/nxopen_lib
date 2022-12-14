#ifndef NXOpen_AME_SELECTREUSELIBRARYITEMBUILDER_HXX_INCLUDED
#define NXOpen_AME_SELECTREUSELIBRARYITEMBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     AME_SelectReuseLibraryItemBuilder.ja
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
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/Tooling_SelectReuseLibraryItemBuilder.hxx>
#include <NXOpen/libameopencpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace AME
    {
        class SelectReuseLibraryItemBuilder;
    }
    namespace Tooling
    {
        class SelectReuseLibraryItemBuilder;
    }
    namespace AME
    {
        class _SelectReuseLibraryItemBuilderBuilder;
        class SelectReuseLibraryItemBuilderImpl;
        /** Builder for selecting base definition <br> this is a block  <br> 
         <br>  Created in NX1847.0.0.  <br>  
        */
        class AMEOPENCPPEXPORT  SelectReuseLibraryItemBuilder : public NXOpen::TaggedObject
        {
            private: SelectReuseLibraryItemBuilderImpl * m_selectreuselibraryitembuilder_impl;
            private: friend class  _SelectReuseLibraryItemBuilderBuilder;
            protected: SelectReuseLibraryItemBuilder();
            public: ~SelectReuseLibraryItemBuilder();
            /**Returns  the reuse library item selection
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXOpen::Tooling::SelectReuseLibraryItemBuilder * ReuseLibraryItemBuilder
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
