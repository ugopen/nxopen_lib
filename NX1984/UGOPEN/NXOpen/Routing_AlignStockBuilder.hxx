#ifndef NXOpen_ROUTING_ALIGNSTOCKBUILDER_HXX_INCLUDED
#define NXOpen_ROUTING_ALIGNSTOCKBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Routing_AlignStockBuilder.ja
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
        class AlignStockBuilder;
    }
    class Builder;
    class Direction;
    namespace Routing
    {
        class RouteObjectCollector;
    }
    namespace Routing
    {
        class _AlignStockBuilderBuilder;
        class AlignStockBuilderImpl;
        /** Represents a @link Routing::AlignStockBuilder Routing::AlignStockBuilder@endlink 
            Builder for aligning non-circular stocks.
                Two methods are provided to user to make stocks alignment:
                    Routing Object: specify the referencing routing object and deriving the reference rotate vector from it,
                    Vector to Vector: specify the to vector as reference and the from vector as the target, then align them.
             <br> To create a new instance of this class, use @link NXOpen::Routing::RouteManager::CreateAlignStockBuilder  NXOpen::Routing::RouteManager::CreateAlignStockBuilder @endlink  <br> 
        Default values.
        <list type="table"> 
         
        <listheader><term> 
        Property</term>  <description> 
        Value</description> </listheader>
        <item><term> 
         
        AlignmentMethod </term> <description> 
         
        RoutingObject </description> </item> 

        </list> 

         <br>  Created in NX9.0.3.  <br>  
        */
        class NXOPENCPP_ROUTINGEXPORT  AlignStockBuilder : public NXOpen::Builder
        {
            /** Methods of aligning stocks.*/
            public: enum StockAlignmentMethod
            {
                StockAlignmentMethodRoutingObject/** routing object */ ,
                StockAlignmentMethodVectorToVector/** vector to vector */ 
            };

            private: AlignStockBuilderImpl * m_alignstockbuilder_impl;
            private: friend class  _AlignStockBuilderBuilder;
            protected: AlignStockBuilder();
            public: ~AlignStockBuilder();
            /**Returns  the alignment method. 
             <br>  Created in NX9.0.3.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: NXOpen::Routing::AlignStockBuilder::StockAlignmentMethod AlignmentMethod
            (
            );
            /**Sets  the alignment method. 
             <br>  Created in NX9.0.3.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void SetAlignmentMethod
            (
                NXOpen::Routing::AlignStockBuilder::StockAlignmentMethod alignmentMethod /** alignmentmethod */ 
            );
            /**Returns  the reference object. The reference object could be a stock or a qualified part.
             <br>  Created in NX9.0.3.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: NXOpen::Routing::RouteObjectCollector * ReferenceObject
            (
            );
            /**Returns  the target vector. 
             <br>  Created in NX9.0.3.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: NXOpen::Direction * TargetVector
            (
            );
            /**Sets  the target vector. 
             <br>  Created in NX9.0.3.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void SetTargetVector
            (
                NXOpen::Direction * fromVector /** fromvector */ 
            );
            /**Returns   the reference vector. 
             <br>  Created in NX9.0.3.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: NXOpen::Direction * ReferenceVector
            (
            );
            /**Sets   the reference vector. 
             <br>  Created in NX9.0.3.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void SetReferenceVector
            (
                NXOpen::Direction * toVector /** tovector */ 
            );
            /**Returns   a collection of stocks to align. 
             <br>  Created in NX9.0.3.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: NXOpen::Routing::RouteObjectCollector * StocksToAlign
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