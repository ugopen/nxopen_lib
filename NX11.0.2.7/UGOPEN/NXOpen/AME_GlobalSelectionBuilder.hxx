#ifndef NXOpen_AME_GLOBALSELECTIONBUILDER_HXX_INCLUDED
#define NXOpen_AME_GLOBALSELECTIONBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     AME_GlobalSelectionBuilder.ja
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
#include <NXOpen/AME_GlobalSelectionBuilder.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/SelectObjectList.hxx>
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
        class GlobalSelectionBuilder;
    }
    class Builder;
    class SelectNXObjectList;
    namespace AME
    {
        class _GlobalSelectionBuilderBuilder;
        class GlobalSelectionBuilderImpl;
        /** GlobalSelectionBuilder  <br> To create a new instance of this class, use @link NXOpen::AME::AMEManager::CreateGlobalSelectionBuilder  NXOpen::AME::AMEManager::CreateGlobalSelectionBuilder @endlink  <br> 
         <br>  Created in NX11.0.0.  <br>  
        */
        class AMEOPENCPPEXPORT  GlobalSelectionBuilder : public NXOpen::Builder
        {
            private: GlobalSelectionBuilderImpl * m_globalselectionbuilder_impl;
            private: friend class  _GlobalSelectionBuilderBuilder;
            protected: GlobalSelectionBuilder();
            public: ~GlobalSelectionBuilder();
            /**Returns  the selected objects 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXOpen::SelectNXObjectList * Selection
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