#ifndef NXOpen_CAM_PROBESTOCKPARAMETERSBUILDER_HXX_INCLUDED
#define NXOpen_CAM_PROBESTOCKPARAMETERSBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_ProbeStockParametersBuilder.ja
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
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAM
    {
        class ProbeStockParametersBuilder;
    }
    namespace CAM
    {
        class _ProbeStockParametersBuilderBuilder;
        class ProbeStockParametersBuilderImpl;
        /** Represents the Probe Stock Parameters Builder */
        class NXOPENCPPEXPORT  ProbeStockParametersBuilder : public TaggedObject
        {
            private: ProbeStockParametersBuilderImpl * m_probestockparametersbuilder_impl;
            private: friend class  _ProbeStockParametersBuilderBuilder;
            protected: ProbeStockParametersBuilder();
            public: ~ProbeStockParametersBuilder();
            /**Returns  the stock allowance  <br> License requirements : None */
            public: double StockAllowance
            (
            );
            /**Sets  the stock allowance  <br> License requirements : None */
            public: void SetStockAllowance
            (
                double stock /** stock */ 
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif