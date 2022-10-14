#ifndef NXOpen_ROUTING_STOCKDEVICE_HXX_INCLUDED
#define NXOpen_ROUTING_STOCKDEVICE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Routing_StockDevice.ja
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
#include <NXOpen/Routing_SingleDevice.hxx>
#include <NXOpen/libnxopencpp_routing_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Routing
    {
        class StockDevice;
    }
    class Part;
    namespace Routing
    {
        class SingleDevice;
    }
    namespace Routing
    {
        class StockDefinition;
    }
    namespace Routing
    {
        class _StockDeviceBuilder;
        class StockDeviceImpl;
        /** 
                The Routing StockDevice corresponds to a generic stock instance 
                of @link Routing::SingleDevice Routing::SingleDevice@endlink .
             <br> Creator not available in KF.  <br> 
         <br>  Created in NX4.0.2.  <br>  
        */
        class NXOPENCPP_ROUTINGEXPORT  StockDevice : public NXOpen::Routing::SingleDevice
        {
            private: StockDeviceImpl * m_stockdevice_impl;
            private: friend class  _StockDeviceBuilder;
            protected: StockDevice();
            public: ~StockDevice();
            /**Returns  the stock length. 
             <br>  Created in NX4.0.2.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
            public: double StockLength
            (
            );
            /**Sets  the stock length. 
             <br>  Created in NX4.0.2.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
            public: void SetStockLength
            (
                double stockLength /** stock length */ 
            );
            /**Returns  the stock definition. 
             <br>  Created in NX4.0.2.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
            public: NXOpen::Routing::StockDefinition * StockDefinition
            (
            );
            /**Sets  the stock definition. 
             <br>  Created in NX4.0.2.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
            public: void SetStockDefinition
            (
                NXOpen::Routing::StockDefinition * routeStockDefinition /** route stock definition */ 
            );
            /** Log stock device's wire and its segment for concurrency 
             <br>  Created in NX10.0.3.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
            public: void LogStockDeviceWiresforConcurrency
            (
                NXOpen::Part * partTag /** parttag */ 
            );
        };
    }
}

#ifdef _MSC_VER
#pragma warning(pop)
#endif
#ifdef __GNUC__
#ifndef NX_NO_GCC_DEPRECATION_WARNINGS
#pragma GCC diagnostic warning "-Wdeprecated-declarations"
#endif
#endif

#undef EXPORTLIBRARY
#endif