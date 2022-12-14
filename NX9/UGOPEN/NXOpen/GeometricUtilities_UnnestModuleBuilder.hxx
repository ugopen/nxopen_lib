#ifndef NXOpen_GEOMETRICUTILITIES_UNNESTMODULEBUILDER_HXX_INCLUDED
#define NXOpen_GEOMETRICUTILITIES_UNNESTMODULEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     GeometricUtilities_UnnestModuleBuilder.ja
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
#include <NXOpen/GeometricUtilities_UnnestModuleBuilder.hxx>
#include <NXOpen/SelectObject.hxx>
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
        class UnnestModuleBuilder;
    }
    class Builder;
    namespace Features
    {
        class SelectFeature;
    }
    namespace GeometricUtilities
    {
        class _UnnestModuleBuilderBuilder;
        class UnnestModuleBuilderImpl;
        /** Represents a @link GeometricUtilities::UnnestModuleBuilder GeometricUtilities::UnnestModuleBuilder@endlink   <br> To create a new instance of this class, use @link Features::FeatureCollection::CreateUnnestModuleBuilder  Features::FeatureCollection::CreateUnnestModuleBuilder @endlink  <br> 
         <br>  Created in NX9.0.0.  <br>  
        */
        class NXOPENCPP_GEOMETRICUTILITIESEXPORT  UnnestModuleBuilder : public Builder
        {
            private: UnnestModuleBuilderImpl * m_unnestmodulebuilder_impl;
            private: friend class  _UnnestModuleBuilderBuilder;
            protected: UnnestModuleBuilder();
            public: ~UnnestModuleBuilder();
            /**Returns  the module to unnest 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Features::SelectFeature * ModuleToUnnest
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
