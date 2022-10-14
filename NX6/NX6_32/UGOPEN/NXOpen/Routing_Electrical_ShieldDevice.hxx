#ifndef NXOpen_ROUTING_ELECTRICAL_SHIELDDEVICE_HXX_INCLUDED
#define NXOpen_ROUTING_ELECTRICAL_SHIELDDEVICE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Routing_Electrical_ShieldDevice.ja
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
#include <NXOpen/Routing_Electrical_CableDevice.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Routing
    {
        namespace Electrical
        {
            class ShieldDevice;
        }
    }
    namespace Routing
    {
        namespace Electrical
        {
            class CableDevice;
        }
    }
    namespace Routing
    {
        namespace Electrical
        {
            class _ShieldDeviceBuilder;
            /**
                        The Electrical ShieldDevice corresponds to a shield instance of
                        @link Routing::Electrical::ElectricalStockDevice Routing::Electrical::ElectricalStockDevice@endlink . 
                        An electrical shield device is both an assembly definition and a electrical stock device.
                     <br> Creator not available in KF. <br> */
            class NXOPENCPPEXPORT ShieldDevice : public Routing::Electrical::CableDevice
            {
                private: friend class  _ShieldDeviceBuilder;
                protected: ShieldDevice();
            };
        }
    }
}
#undef EXPORTLIBRARY
#endif