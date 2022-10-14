#ifndef NXOpen_CAE_VIEWLAMINATEBUILDER_HXX_INCLUDED
#define NXOpen_CAE_VIEWLAMINATEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_ViewLaminateBuilder.ja
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
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAE
    {
        class ViewLaminateBuilder;
    }
    class Builder;
    namespace CAE
    {
        class _ViewLaminateBuilderBuilder;
        class ViewLaminateBuilderImpl;
        /** Represents a View Laminate Builder.  <br> To create a new instance of this class, use @link CAE::LaminateGlobalLayupMgr::CreateViewLaminateBuilder CAE::LaminateGlobalLayupMgr::CreateViewLaminateBuilder@endlink  <br> */
        class NXOPENCPPEXPORT  ViewLaminateBuilder : public Builder
        {
            private: ViewLaminateBuilderImpl * m_viewlaminatebuilder_impl;
            private: friend class  _ViewLaminateBuilderBuilder;
            protected: ViewLaminateBuilder();
            public: ~ViewLaminateBuilder();
        };
    }
}
#undef EXPORTLIBRARY
#endif