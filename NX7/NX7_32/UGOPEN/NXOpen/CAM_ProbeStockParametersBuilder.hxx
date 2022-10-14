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
        /** Represents the Probe Stock Parameters Builder */
        class NXOPENCPPEXPORT ProbeStockParametersBuilder : public TaggedObject
        {
            private: friend class  _ProbeStockParametersBuilderBuilder;
            protected: ProbeStockParametersBuilder();
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