#ifndef NXOpen_CAE_PRETESTDOFSETBUILDER_HXX_INCLUDED
#define NXOpen_CAE_PRETESTDOFSETBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_PreTestDofSetBuilder.ja
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
#include <NXOpen/CAE_PreTestDofSetBuilder.hxx>
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAE
    {
        class PreTestDofSetBuilder;
    }
    class Builder;
    namespace CAE
    {
        class CaeDOFSet;
    }
    namespace CAE
    {
        class SelectFENodeList;
    }
    namespace CAE
    {
        class _PreTestDofSetBuilderBuilder;
        class PreTestDofSetBuilderImpl;
        /** Represents a @link CAE::PreTestDofSet CAE::PreTestDofSet@endlink  builder  <br> To create a new instance of this class, use @link CAE::PreTestSolutionCollection::CreatePretestDofsetBuilder CAE::PreTestSolutionCollection::CreatePretestDofsetBuilder@endlink  <br> */
        class NXOPENCPPEXPORT  PreTestDofSetBuilder : public Builder
        {
            private: PreTestDofSetBuilderImpl * m_pretestdofsetbuilder_impl;
            private: friend class  _PreTestDofSetBuilderBuilder;
            protected: PreTestDofSetBuilder();
            public: ~PreTestDofSetBuilder();
            /**Returns  the referrenced @link CAE::CaeDOFSet CAE::CaeDOFSet@endlink   <br> License requirements : nx_correl_base ("FE Correlation") */
            public: NXOpen::CAE::CaeDOFSet * DofSetSelect
            (
            );
            /**Sets  the referrenced @link CAE::CaeDOFSet CAE::CaeDOFSet@endlink   <br> License requirements : nx_correl_base ("FE Correlation") */
            public: void SetDofSetSelect
            (
                NXOpen::CAE::CaeDOFSet * dofSetSelect /** dofsetselect */ 
            );
            /**Returns  the manual selection toggle value  <br> License requirements : nx_correl_base ("FE Correlation") */
            public: bool NodesEnabled
            (
            );
            /**Sets  the manual selection toggle value  <br> License requirements : nx_correl_base ("FE Correlation") */
            public: void SetNodesEnabled
            (
                bool nodesEnabled /** nodesenabled */ 
            );
            /**Returns  the selected nodes  <br> License requirements : nx_correl_base ("FE Correlation") */
            public: NXOpen::CAE::SelectFENodeList * Nodes
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif