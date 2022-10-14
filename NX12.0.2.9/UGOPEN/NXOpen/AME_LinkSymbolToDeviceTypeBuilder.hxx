#ifndef NXOpen_AME_LINKSYMBOLTODEVICETYPEBUILDER_HXX_INCLUDED
#define NXOpen_AME_LINKSYMBOLTODEVICETYPEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     AME_LinkSymbolToDeviceTypeBuilder.ja
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
#include <NXOpen/AME_SelectProductOrEoDefinitionBuilder.hxx>
#include <NXOpen/Builder.hxx>
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
        class LinkSymbolToDeviceTypeBuilder;
    }
    namespace AME
    {
        class SelectProductOrEoDefinitionBuilder;
    }
    class Builder;
    namespace Tooling
    {
        class SelectReuseLibraryItemBuilder;
    }
    namespace AME
    {
        class _LinkSymbolToDeviceTypeBuilderBuilder;
        class LinkSymbolToDeviceTypeBuilderImpl;
        /** JA class for LinkSymbolToDeviceTypeBuilder dialog <br> To create a new instance of this class, use @link NXOpen::AME::AMEManager::CreateLinkSymbolToDeviceTypeBuilder  NXOpen::AME::AMEManager::CreateLinkSymbolToDeviceTypeBuilder @endlink  <br> 
         <br>  Created in NX11.0.0.  <br>  
        */
        class AMEOPENCPPEXPORT  LinkSymbolToDeviceTypeBuilder : public NXOpen::Builder
        {
            private: LinkSymbolToDeviceTypeBuilderImpl * m_linksymboltodevicetypebuilder_impl;
            private: friend class  _LinkSymbolToDeviceTypeBuilderBuilder;
            protected: LinkSymbolToDeviceTypeBuilder();
            public: ~LinkSymbolToDeviceTypeBuilder();
            /**Returns  the schematic symbol item
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXOpen::Tooling::SelectReuseLibraryItemBuilder * SelectSchematicSymbol
            (
            );
            /**Returns  the product or engineering object definition
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXOpen::AME::SelectProductOrEoDefinitionBuilder * SelectProductOrEoDef
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