#ifndef NXOpen_CAE_CORRELBASEBUILDER_HXX_INCLUDED
#define NXOpen_CAE_CORRELBASEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_CorrelBaseBuilder.ja
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
        class CorrelBaseBuilder;
    }
    class Builder;
    namespace CAE
    {
        class _CorrelBaseBuilderBuilder;
        class CorrelBaseBuilderImpl;
        /** Represents the abstract builder class for all objects defined in correl meta solution  <br> This is an abstract class, and cannot be created. <br> */
        class NXOPENCPPEXPORT  CorrelBaseBuilder : public Builder
        {
            private: CorrelBaseBuilderImpl * m_correlbasebuilder_impl;
            private: friend class  _CorrelBaseBuilderBuilder;
            protected: CorrelBaseBuilder();
            public: ~CorrelBaseBuilder();
        };
    }
}
#undef EXPORTLIBRARY
#endif