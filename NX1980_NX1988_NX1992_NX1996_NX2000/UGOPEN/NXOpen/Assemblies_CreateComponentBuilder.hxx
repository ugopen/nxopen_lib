#ifndef NXOpen_ASSEMBLIES_CREATECOMPONENTBUILDER_HXX_INCLUDED
#define NXOpen_ASSEMBLIES_CREATECOMPONENTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Assemblies_CreateComponentBuilder.ja
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
        class CreateComponentBuilder;
    }
    class Builder;
    namespace Assemblies
    {
        class _CreateComponentBuilderBuilder;
        class CreateComponentBuilderImpl;
        /** Represents a @link NXOpen::Assemblies::CreateComponentBuilder NXOpen::Assemblies::CreateComponentBuilder@endlink  builder class.
            This builder class will perform various component creation operations under assembly, workset or subset.  <br> To create a new instance of this class, use @link NXOpen::Assemblies::AssemblyManager::CreateCreateComponentBuilder  NXOpen::Assemblies::AssemblyManager::CreateCreateComponentBuilder @endlink  <br> 
         <br>  Created in NX12.0.0.  <br>  
        */
        class NXOPENCPP_ASSEMBLIESEXPORT  CreateComponentBuilder : public NXOpen::Builder
        {
            private: CreateComponentBuilderImpl * m_createcomponentbuilder_impl;
            private: friend class  _CreateComponentBuilderBuilder;
            protected: CreateComponentBuilder();
            public: ~CreateComponentBuilder();
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