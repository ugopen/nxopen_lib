#ifndef NXOpen_ROUTING_STOCKTRANSITION_HXX_INCLUDED
#define NXOpen_ROUTING_STOCKTRANSITION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Routing_StockTransition.ja
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
#include <NXOpen/Routing_Stock.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Routing
    {
        class StockTransition;
    }
    namespace Routing
    {
        class Stock;
    }
    namespace Routing
    {
        class _StockTransitionBuilder;
        class StockTransitionImpl;
        /** Represents @link Routing::StockTransition Routing::StockTransition@endlink  object. @link Routing::StockTransition Routing::StockTransition@endlink  covers C1 continuous @link Routing::ISegment Routing::ISegment@endlink  
            in between two stocks. It acts as transition from @link Routing::CrossSection Routing::CrossSection@endlink  of one @link Routing::Stock Routing::Stock@endlink  to another. 
            When two different @link Routing::Stock Routing::Stock@endlink  are connected with set of segments, then a stockTransition can be used to cover
            it in such a way that @link Routing::CrossSection Routing::CrossSection@endlink  at each end of this segments matches with the stock at that location.
            These segments can be a routing path, or just a collection of segments.
            @link Routing::Stock Routing::Stock@endlink  covers segments, and @link Routing::StockTransition Routing::StockTransition@endlink  inherits
            that behavior.  However, @link Routing::StockTransition Routing::StockTransition@endlink  refers to two end @link Routing::Stock Routing::Stock@endlink  and the @link Routing::CrossSection Routing::CrossSection@endlink 
            of @link Routing::StockTransition Routing::StockTransition@endlink  object varies from one end to another.    <br> Creator not available in KF because transient objects are not supported. <br> */
        class NXOPENCPPEXPORT  StockTransition : public Routing::Stock
        {
            private: StockTransitionImpl * m_stocktransition_impl;
            private: friend class  _StockTransitionBuilder;
            protected: StockTransition();
            public: ~StockTransition();
        };
    }
}
#undef EXPORTLIBRARY
#endif
