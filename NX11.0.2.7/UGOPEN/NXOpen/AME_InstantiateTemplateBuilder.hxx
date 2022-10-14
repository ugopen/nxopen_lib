#ifndef NXOpen_AME_INSTANTIATETEMPLATEBUILDER_HXX_INCLUDED
#define NXOpen_AME_INSTANTIATETEMPLATEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     AME_InstantiateTemplateBuilder.ja
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
#include <NXOpen/AME_AspectDetailsBuilder.hxx>
#include <NXOpen/AME_InstantiateTemplateBuilder.hxx>
#include <NXOpen/AME_MultipleObjectsBuilder.hxx>
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
        class InstantiateTemplateBuilder;
    }
    namespace AME
    {
        class AspectDetailsBuilder;
    }
    namespace AME
    {
        class MultipleObjectsBuilder;
    }
    namespace Tooling
    {
        class SelectReuseLibraryItemBuilder;
    }
    namespace AME
    {
        class _InstantiateTemplateBuilderBuilder;
        class InstantiateTemplateBuilderImpl;
        /** JA class for the insert Eng object dialog <br> To create a new instance of this class, use @link NXOpen::AME::AMEManager::CreateInstantiateTemplateBuilder  NXOpen::AME::AMEManager::CreateInstantiateTemplateBuilder @endlink  <br> 
         <br>  Created in NX11.0.0.  <br>  
        */
        class AMEOPENCPPEXPORT  InstantiateTemplateBuilder : public NXOpen::AME::MultipleObjectsBuilder
        {
            private: InstantiateTemplateBuilderImpl * m_instantiatetemplatebuilder_impl;
            private: friend class  _InstantiateTemplateBuilderBuilder;
            protected: InstantiateTemplateBuilder();
            public: ~InstantiateTemplateBuilder();
            /**Returns  the reuse library selection item
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXOpen::Tooling::SelectReuseLibraryItemBuilder * ReuseLibraryItem
            (
            );
            /**Returns  the aspect details ui block
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXOpen::AME::AspectDetailsBuilder * AspectDetails
            (
            );
            /**Returns  the unload template flag to indicate if template should be unloaded after instantiation
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: bool UnloadTemplate
            (
            );
            /**Sets  the unload template flag to indicate if template should be unloaded after instantiation
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetUnloadTemplate
            (
                bool unloadTemplate /** unloadtemplate */ 
            );
            /**Returns  the copy document structure flag to decide whether to copy document structure
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: bool CopyDocumentStructure
            (
            );
            /**Sets  the copy document structure flag to decide whether to copy document structure
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetCopyDocumentStructure
            (
                bool copyDocumentStructure /** copydocumentstructure */ 
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