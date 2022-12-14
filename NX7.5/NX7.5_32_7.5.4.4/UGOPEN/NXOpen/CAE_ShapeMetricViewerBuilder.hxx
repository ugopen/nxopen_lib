#ifndef NXOpen_CAE_SHAPEMETRICVIEWERBUILDER_HXX_INCLUDED
#define NXOpen_CAE_SHAPEMETRICVIEWERBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_ShapeMetricViewerBuilder.ja
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
        class ShapeMetricViewerBuilder;
    }
    class Builder;
    namespace CAE
    {
        class _ShapeMetricViewerBuilderBuilder;
        class ShapeMetricViewerBuilderImpl;
        /** Represents the correlation Shape metrics viewer builder  <br> To create a new instance of this class, use @link CAE::CorrelSolutionCollection::CreateShapeMetricViewerBuilder CAE::CorrelSolutionCollection::CreateShapeMetricViewerBuilder@endlink  <br> */
        class NXOPENCPPEXPORT  ShapeMetricViewerBuilder : public Builder
        {
            private: ShapeMetricViewerBuilderImpl * m_shapemetricviewerbuilder_impl;
            private: friend class  _ShapeMetricViewerBuilderBuilder;
            protected: ShapeMetricViewerBuilder();
            public: ~ShapeMetricViewerBuilder();
        };
    }
}
#undef EXPORTLIBRARY
#endif
