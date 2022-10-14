#ifndef NXOpen_ROUTING_STOCKPORT_HXX_INCLUDED
#define NXOpen_ROUTING_STOCKPORT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Routing_StockPort.ja
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
#include <NXOpen/Routing_Port.hxx>
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
        class StockPort;
    }
    namespace Routing
    {
        class ExtractPort;
    }
    namespace Routing
    {
        class Port;
    }
    namespace Routing
    {
        class Stock;
    }
    namespace Routing
    {
        class _StockPortBuilder;
        class StockPortImpl;
        /** @link Routing::StockPort Routing::StockPort@endlink  objects are automatically created and updated by
              @link Routing::Stock Routing::Stock@endlink  objects.  <br> Instances of this class are created by @link Routing::Stock Routing::Stock@endlink .  <br> 
         <br>  Created in NX4.0.0.  <br>  
        */
        class NXOPENCPP_ROUTINGEXPORT  StockPort : public Routing::Port
        {
            private: StockPortImpl * m_stockport_impl;
            private: friend class  _StockPortBuilder;
            protected: StockPort();
            public: ~StockPort();
            /** Gets the @link Routing::Stock Routing::Stock@endlink  that owns this object.   @return  
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: NXOpen::Routing::Stock * GetStock
            (
            );
            /** For Stock As Components, returns the @link Routing::ExtractPort Routing::ExtractPort@endlink 
                        of this @link Routing::StockPort Routing::StockPort@endlink  using the @link Routing::StockPort Routing::StockPort@endlink 's
                        occurrence in the work part. Returns NULL if the given @link StockPort StockPort@endlink 
                        does not have a port occurrence in the work part.  @return  Extract port that represents the occurrence of
                                                                                            the @link Routing::StockPort Routing::StockPort@endlink  in the work part. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: NXOpen::Routing::ExtractPort * GetExtractPort
            (
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