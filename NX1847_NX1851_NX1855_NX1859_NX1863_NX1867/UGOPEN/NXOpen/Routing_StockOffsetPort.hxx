#ifndef NXOpen_ROUTING_STOCKOFFSETPORT_HXX_INCLUDED
#define NXOpen_ROUTING_STOCKOFFSETPORT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Routing_StockOffsetPort.ja
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
        class StockOffsetPort;
    }
    namespace Routing
    {
        class Port;
    }
    namespace Routing
    {
        class _StockOffsetPortBuilder;
        class StockOffsetPortImpl;
        /** @link NXOpen::Routing::StockOffsetPort NXOpen::Routing::StockOffsetPort@endlink  class handles the relationship
                between a component part's port occurrence and the dumb offset port in
                the work part. The dumb port offsets based on expressions that use
                the stock diameter.  <br> Use @link NXOpen::Routing::StockOffsetPortCollection::CreateStockOffsetPort NXOpen::Routing::StockOffsetPortCollection::CreateStockOffsetPort@endlink  to create an instance of this class.  <br> 
         <br>  Created in NX7.5.4.  <br>  
        */
        class NXOPENCPP_ROUTINGEXPORT  StockOffsetPort : public NXOpen::Routing::Port
        {
            private: StockOffsetPortImpl * m_stockoffsetport_impl;
            private: friend class  _StockOffsetPortBuilder;
            protected: StockOffsetPort();
            public: ~StockOffsetPort();
            /** Returns the original port occurrence from which the dumb port was extracted.
                        Returns NULL if the occurrence is not available because it is not loaded, or not in the current reference set, etc. 
             <br>  Created in NX7.5.4.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: NXOpen::Routing::Port * GetPortOccurrence
            (
            );
            /** Returns the @link NXOpen::Routing::StockOffsetPort NXOpen::Routing::StockOffsetPort@endlink  in the work part that was created from the original port occurrence. 
             <br>  Created in NX7.5.4.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: NXOpen::Routing::Port * GetOffsetPort
            (
            );
            /** Returns the diameter of all the stock on the path at this @link NXOpen::Routing::StockOffsetPort NXOpen::Routing::StockOffsetPort@endlink .
                    NOTE: This value may change in the next update cycle. 
             <br>  Created in NX7.5.5.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: double GetMaxPathStockDiameter
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
