#ifndef NXOpen_ROUTINGCOMMON_MERGEBUILDER_HXX_INCLUDED
#define NXOpen_ROUTINGCOMMON_MERGEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     RoutingCommon_MergeBuilder.ja
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
#include <NXOpen/Routing_RouteObjectCollector.hxx>
#include <NXOpen/libnxopencpp_routingcommon_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace RoutingCommon
    {
        class MergeBuilder;
    }
    class Builder;
    namespace Routing
    {
        class RouteObjectCollector;
    }
    namespace RoutingCommon
    {
        class _MergeBuilderBuilder;
        class MergeBuilderImpl;
        /** the Builder to Merge Component  <br> To create a new instance of this class, use @link NXOpen::RoutingCommon::BuilderFactory::CreateMergeBuilder  NXOpen::RoutingCommon::BuilderFactory::CreateMergeBuilder @endlink  <br> 
         <br>  Created in NX11.0.1.  <br>  
        */
        class NXOPENCPP_ROUTINGCOMMONEXPORT  MergeBuilder : public NXOpen::Builder
        {
            private: MergeBuilderImpl * m_mergebuilder_impl;
            private: friend class  _MergeBuilderBuilder;
            protected: MergeBuilder();
            public: ~MergeBuilder();
            /**Returns  the routing component collector that collects target stock component 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: NXOpen::Routing::RouteObjectCollector * TargetStockComponentCollector
            (
            );
            /**Returns  the routing component collector that collects candidate stock component to merge with target component 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: NXOpen::Routing::RouteObjectCollector * CandidateStockComponentCollector
            (
            );
            /**Returns  the simplify path setting 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: bool SimplifyPath
            (
            );
            /**Sets  the simplify path setting 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void SetSimplifyPath
            (
                bool simplifyPath /** simplifypath */ 
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
