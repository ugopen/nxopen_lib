#ifndef NXOpen_CAE_MODELUPDATESOLUTIONBUILDER_HXX_INCLUDED
#define NXOpen_CAE_MODELUPDATESOLUTIONBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_ModelUpdateSolutionBuilder.ja
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
#include <NXOpen/CAE_CorrelSolutionBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAE
    {
        class ModelUpdateSolutionBuilder;
    }
    namespace CAE
    {
        class CorrelSolutionBuilder;
    }
    namespace CAE
    {
        class _ModelUpdateSolutionBuilderBuilder;
        class ModelUpdateSolutionBuilderImpl;
        /** Represents a @link CAE::ModelUpdateSolutionBuilder CAE::ModelUpdateSolutionBuilder@endlink   <br> To create a new instance of this class, use @link CAE::ModelUpdateSolutionCollection::CreateSolutionBuilder CAE::ModelUpdateSolutionCollection::CreateSolutionBuilder@endlink  <br> */
        class NXOPENCPPEXPORT  ModelUpdateSolutionBuilder : public CAE::CorrelSolutionBuilder
        {
            private: ModelUpdateSolutionBuilderImpl * m_modelupdatesolutionbuilder_impl;
            private: friend class  _ModelUpdateSolutionBuilderBuilder;
            protected: ModelUpdateSolutionBuilder();
            public: ~ModelUpdateSolutionBuilder();
        };
    }
}
#undef EXPORTLIBRARY
#endif