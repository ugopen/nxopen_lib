#ifndef NXOpen_ROUTING_ROUTINGMEASUREDISTANCEBUILDER_HXX_INCLUDED
#define NXOpen_ROUTING_ROUTINGMEASUREDISTANCEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Routing_RoutingMeasureDistanceBuilder.ja
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
#include <NXOpen/MeasureDistanceBuilder.hxx>
#include <NXOpen/Routing_RouteObjectCollector.hxx>
#include <NXOpen/Routing_RoutingMeasureDistanceBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Routing
    {
        class RoutingMeasureDistanceBuilder;
    }
    class MeasureDistanceBuilder;
    class NXObject;
    namespace Routing
    {
        class RouteObjectCollector;
    }
    namespace Routing
    {
        class _RoutingMeasureDistanceBuilderBuilder;
        class RoutingMeasureDistanceBuilderImpl;
        /** Represents a @link RoutingMeasureDistanceBuilder RoutingMeasureDistanceBuilder@endlink   <br> Creator not available in KF because transient objects are not supported. <br> */
        class NXOPENCPPEXPORT  RoutingMeasureDistanceBuilder : public MeasureDistanceBuilder
        {
            private: RoutingMeasureDistanceBuilderImpl * m_routingmeasuredistancebuilder_impl;
            private: friend class  _RoutingMeasureDistanceBuilderBuilder;
            protected: RoutingMeasureDistanceBuilder();
            public: ~RoutingMeasureDistanceBuilder();
            /**Returns  the @link Routing::RouteObjectCollector Routing::RouteObjectCollector@endlink   <br> License requirements : None */
            public: NXOpen::Routing::RouteObjectCollector * RoutingSelection
            (
            );
            /**Sets  the @link Routing::RouteObjectCollector Routing::RouteObjectCollector@endlink   <br> License requirements : None */
            public: void SetRoutingSelection
            (
                NXOpen::Routing::RouteObjectCollector * selectionBuilder /** selectionbuilder */ 
            );
            /** The routing objects used for path length  @return  the routing objects used for path length  <br> License requirements : None */
            public: std::vector<NXOpen::NXObject *> GetRoutingObjects
            (
            );
            /** The routing objects used for path length  <br> License requirements : None */
            public: void SetRoutingObjects
            (
                const std::vector<NXOpen::NXObject *> & routingObjects /** the routing objects to set for path length */
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
