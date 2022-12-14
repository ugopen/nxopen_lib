#ifndef NXOpen_ROUTING_SIMPLIFYPATHBUILDER_HXX_INCLUDED
#define NXOpen_ROUTING_SIMPLIFYPATHBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Routing_SimplifyPathBuilder.ja
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
#include <NXOpen/Builder.hxx>
#include <NXOpen/Routing_RouteObjectCollector.hxx>
#include <NXOpen/Routing_SimplifyPathBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Routing
    {
        class SimplifyPathBuilder;
    }
    class Builder;
    namespace Routing
    {
        class RouteObjectCollector;
    }
    namespace Routing
    {
        class _SimplifyPathBuilderBuilder;
        /**
            Represents a @link Routing::SimplifyPathBuilder Routing::SimplifyPathBuilder@endlink  for Simplify Path operation.
            Merges collinear segments (with no follow curves) together.  Also merges segments that 
            share a follow curve.
             <br> To create a new instance of this class, use @link Routing::RouteManager::CreateSimplifyPathBuilder Routing::RouteManager::CreateSimplifyPathBuilder@endlink  <br> */
        class NXOPENCPPEXPORT SimplifyPathBuilder : public Builder
        {
            private: friend class  _SimplifyPathBuilderBuilder;
            protected: SimplifyPathBuilder();
            /**Returns  the routing object collector that collects the segments to simplify. <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: NXOpen::Routing::RouteObjectCollector * SegmentCollector
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
