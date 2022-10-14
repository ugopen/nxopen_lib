#ifndef NXOpen_CAE_MESHPOINTONCURVEBUILDER_HXX_INCLUDED
#define NXOpen_CAE_MESHPOINTONCURVEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_MeshPointOnCurveBuilder.ja
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
#include <NXOpen/CAE_MeshPointOnCurveBuilder.hxx>
#include <NXOpen/Expression.hxx>
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAE
    {
        class MeshPointOnCurveBuilder;
    }
    class Builder;
    class Expression;
    class SelectIBaseCurveList;
    namespace CAE
    {
        class _MeshPointOnCurveBuilderBuilder;
        class MeshPointOnCurveBuilderImpl;
        /**
            Represents a @link CAE::MeshPointOnCurveBuilder CAE::MeshPointOnCurveBuilder@endlink 
             <br> To create a new instance of this class, use @link CAE::MeshPointCollection::CreateMeshpointOnCurveBuilder CAE::MeshPointCollection::CreateMeshpointOnCurveBuilder@endlink  <br> */
        class NXOPENCPPEXPORT  MeshPointOnCurveBuilder : public Builder
        {
            private: MeshPointOnCurveBuilderImpl * m_meshpointoncurvebuilder_impl;
            private: friend class  _MeshPointOnCurveBuilderBuilder;
            protected: MeshPointOnCurveBuilder();
            public: ~MeshPointOnCurveBuilder();
            /**Returns  the node  <br> License requirements : None */
            public: NXOpen::SelectIBaseCurveList * Curve
            (
            );
            /**Returns  the t parameter  <br> License requirements : None */
            public: NXOpen::Expression * TParameter
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif