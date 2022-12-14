#ifndef NXOpen_ROUTING_OVERSTOCKDEVICE_HXX_INCLUDED
#define NXOpen_ROUTING_OVERSTOCKDEVICE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Routing_OverstockDevice.ja
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
#include <NXOpen/Routing_StockDevice.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Routing
    {
        class OverstockDevice;
    }
    namespace Routing
    {
        class StockDevice;
    }
    namespace Routing
    {
        class _OverstockDeviceBuilder;
        /**
                 <br> 
                The @link Routing::OverstockDevice Routing::OverstockDevice@endlink  corresponds to an overstock instance
                of @link Routing::StockDevice Routing::StockDevice@endlink .
                @link Routing::OverstockDevice Routing::OverstockDevice@endlink  is used as a covering over other
                @link Routing::StockDevice Routing::StockDevice@endlink s.
                 <br> 
                 <br> 
                @link Routing::OverstockDevice Routing::OverstockDevice@endlink s are currently unused in the logical
                electrical data model.
                 <br> 
                 <br> 
                See NX Routing help for the Connectivity data model documentation.
                 <br> 
             <br> Creator not available in KF. <br> */
        class NXOPENCPPEXPORT OverstockDevice : public Routing::StockDevice
        {
            private: friend class  _OverstockDeviceBuilder;
            protected: OverstockDevice();
        };
    }
}
#undef EXPORTLIBRARY
#endif
