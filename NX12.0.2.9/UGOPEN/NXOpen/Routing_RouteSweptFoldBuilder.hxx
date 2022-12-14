#ifndef NXOpen_ROUTING_ROUTESWEPTFOLDBUILDER_HXX_INCLUDED
#define NXOpen_ROUTING_ROUTESWEPTFOLDBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Routing_RouteSweptFoldBuilder.ja
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
#include <NXOpen/Expression.hxx>
#include <NXOpen/GeometricUtilities_OnPathDimensionBuilder.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/SelectObject.hxx>
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
        class RouteSweptFoldBuilder;
    }
    class Builder;
    class Curve;
    class Expression;
    namespace GeometricUtilities
    {
        class OnPathDimensionBuilder;
    }
    namespace Routing
    {
        class Stock;
    }
    class SelectBody;
    namespace Routing
    {
        class _RouteSweptFoldBuilderBuilder;
        class RouteSweptFoldBuilderImpl;
        /** Represents a Rout Swept Fold Builder  <br> To create a new instance of this class, use @link NXOpen::Routing::RouteManager::CreateRouteSweptFoldBuilder  NXOpen::Routing::RouteManager::CreateRouteSweptFoldBuilder @endlink  <br> 
         <br>  Created in NX7.0.0.  <br>  
        */
        class NXOPENCPP_ROUTINGEXPORT  RouteSweptFoldBuilder : public NXOpen::Builder
        {
            private: RouteSweptFoldBuilderImpl * m_routesweptfoldbuilder_impl;
            private: friend class  _RouteSweptFoldBuilderBuilder;
            protected: RouteSweptFoldBuilder();
            public: ~RouteSweptFoldBuilder();
            /**Returns  the stock selection. This will be the solid body
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : routing_harness ("Routing Harness") */
            public: NXOpen::SelectBody * StockSelection
            (
            );
            /**Returns  the fold location 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : routing_harness ("Routing Harness") */
            public: NXOpen::GeometricUtilities::OnPathDimensionBuilder * FoldLocation
            (
            );
            /**Returns  the reverse fixed segment 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : routing_harness ("Routing Harness") */
            public: bool ReverseFixedSegment
            (
            );
            /**Sets  the reverse fixed segment 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : routing_harness ("Routing Harness") */
            public: void SetReverseFixedSegment
            (
                bool reverseFixedSegment /** reversefixedsegment */ 
            );
            /**Returns  the fold rotation angle 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : routing_harness ("Routing Harness") */
            public: NXOpen::Expression * FoldRotationAngle
            (
            );
            /**Returns  the reverse fold rotation angle 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : routing_harness ("Routing Harness") */
            public: bool ReverseFoldRotationAngle
            (
            );
            /**Sets  the reverse fold rotation angle 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : routing_harness ("Routing Harness") */
            public: void SetReverseFoldRotationAngle
            (
                bool reverseFoldRotationAngle /** reversefoldrotationangle */ 
            );
            /**Returns  the bend angle 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : routing_harness ("Routing Harness") */
            public: NXOpen::Expression * BendAngle
            (
            );
            /**Returns  the reverse bend angle 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : routing_harness ("Routing Harness") */
            public: bool ReverseBendAngle
            (
            );
            /**Sets  the reverse bend angle 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : routing_harness ("Routing Harness") */
            public: void SetReverseBendAngle
            (
                bool reverseBendAngle /** reversebendangle */ 
            );
            /**Returns  the fold start rotation angle 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : routing_harness ("Routing Harness") */
            public: NXOpen::Expression * FoldStartRotationAngle
            (
            );
            /**Returns  the bend radius 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : routing_harness ("Routing Harness") */
            public: NXOpen::Expression * BendRadius
            (
            );
            /**Returns  the length adjustment 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : routing_harness ("Routing Harness") */
            public: NXOpen::Expression * LengthAdjustment
            (
            );
            /** Sets the value of stock, stock width and stock thickness to the builder. This will set the stock only if it has rectangular cross section. 
                        After setting the stock it will create and set the spline for the builder. It will also set the spline curves for the builder
                        if the stock has more than one segments. 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : routing_harness ("Routing Harness") */
            public: void SetStock
            (
                NXOpen::Routing::Stock * stock /** Selected Stock */
            );
            /**Returns  the spline stored in the builder. 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : routing_harness ("Routing Harness") */
            public: NXOpen::Curve * Spline
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
