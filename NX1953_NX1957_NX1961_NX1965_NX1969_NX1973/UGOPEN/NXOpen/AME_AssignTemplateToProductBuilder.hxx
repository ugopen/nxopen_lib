#ifndef NXOpen_AME_ASSIGNTEMPLATETOPRODUCTBUILDER_HXX_INCLUDED
#define NXOpen_AME_ASSIGNTEMPLATETOPRODUCTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     AME_AssignTemplateToProductBuilder.ja
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
#include <NXOpen/AME_AMEBaseBuilder.hxx>
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
        class AssignTemplateToProductBuilder;
    }
    namespace AME
    {
        class AMEBaseBuilder;
    }
    namespace Tooling
    {
        class SelectReuseLibraryItemBuilder;
    }
    namespace AME
    {
        class _AssignTemplateToProductBuilderBuilder;
        class AssignTemplateToProductBuilderImpl;
        /** Builder class to assign a template object to @link NXOpen::AME::ProductDefinition NXOpen::AME::ProductDefinition@endlink  <br> To create a new instance of this class, use @link NXOpen::AME::AMEManager::CreateAssignTemplateToProductBuilder  NXOpen::AME::AMEManager::CreateAssignTemplateToProductBuilder @endlink  <br> 
         <br>  Created in NX12.0.0.  <br>  
        */
        class AMEOPENCPPEXPORT  AssignTemplateToProductBuilder : public NXOpen::AME::AMEBaseBuilder
        {
            private: AssignTemplateToProductBuilderImpl * m_assigntemplatetoproductbuilder_impl;
            private: friend class  _AssignTemplateToProductBuilderBuilder;
            protected: AssignTemplateToProductBuilder();
            public: ~AssignTemplateToProductBuilder();
            /**Returns  the reuse library item
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXOpen::Tooling::SelectReuseLibraryItemBuilder * ReuseLibraryItem
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
