#ifndef NXOpen_MPA_UPDATEDIAGRAMBUILDER_HXX_INCLUDED
#define NXOpen_MPA_UPDATEDIAGRAMBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     MPA_UpdateDiagramBuilder.ja
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
#include <NXOpen/libmpaopencpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace MPA
    {
        class UpdateDiagramBuilder;
    }
    class Builder;
    namespace MPA
    {
        class _UpdateDiagramBuilderBuilder;
        class UpdateDiagramBuilderImpl;
        /** Represents a Builder class for creating object of to manage update of the diagram    <br> To create a new instance of this class, use @link NXOpen::MPA::MpaManager::CreateUpdateDiagramBuilder  NXOpen::MPA::MpaManager::CreateUpdateDiagramBuilder @endlink  <br> 
         <br>  Created in NX1953.0.0.  <br>  
        */
        class MPAOPENCPPEXPORT  UpdateDiagramBuilder : public NXOpen::Builder
        {
            private: UpdateDiagramBuilderImpl * m_updatediagrambuilder_impl;
            private: friend class  _UpdateDiagramBuilderBuilder;
            protected: UpdateDiagramBuilder();
            public: ~UpdateDiagramBuilder();
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