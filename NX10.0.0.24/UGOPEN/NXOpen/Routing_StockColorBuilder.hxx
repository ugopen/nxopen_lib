#ifndef NXOpen_ROUTING_STOCKCOLORBUILDER_HXX_INCLUDED
#define NXOpen_ROUTING_STOCKCOLORBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Routing_StockColorBuilder.ja
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
#include <NXOpen/Routing_StockColorBuilder.hxx>
#include <NXOpen/ScCollector.hxx>
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
        class StockColorBuilder;
    }
    class Builder;
    class NXColor;
    class ScCollector;
    namespace Routing
    {
        class _StockColorBuilderBuilder;
        class StockColorBuilderImpl;
        /**
            Represents a @link Routing::StockColorBuilder Routing::StockColorBuilder@endlink . This is used 
            to assign color to the face of stocks having rectangular cross section.
             <br> To create a new instance of this class, use @link NXOpen::Routing::RouteManager::CreateStockColorBuilder  NXOpen::Routing::RouteManager::CreateStockColorBuilder @endlink  <br> 
         <br>  Created in NX7.5.0.  <br>  
        */
        class NXOPENCPP_ROUTINGEXPORT  StockColorBuilder : public NXOpen::Builder
        {
            private: StockColorBuilderImpl * m_stockcolorbuilder_impl;
            private: friend class  _StockColorBuilderBuilder;
            protected: StockColorBuilder();
            public: ~StockColorBuilder();
            /**Returns  the route stock select stock face 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : routing_harness ("Routing Harness") */
            public: NXOpen::ScCollector * RouteStockSelectStockFace
            (
            );
            /**Returns  the route stock pick color 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : routing_harness ("Routing Harness") */
            public: NXOpen::NXColor * RouteStockPickColor
            (
            );
            /**Sets  the route stock pick color 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : routing_harness ("Routing Harness") */
            public: void SetRouteStockPickColor
            (
                NXOpen::NXColor * routeStockPickColor /** routestockpickcolor */ 
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