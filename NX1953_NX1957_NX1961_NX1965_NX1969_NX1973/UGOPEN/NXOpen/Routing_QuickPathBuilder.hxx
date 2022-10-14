#ifndef NXOpen_ROUTING_QUICKPATHBUILDER_HXX_INCLUDED
#define NXOpen_ROUTING_QUICKPATHBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Routing_QuickPathBuilder.ja
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
#include <NXOpen/ErrorList.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/ObjectList.hxx>
#include <NXOpen/ugmath.hxx>
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
        class QuickPathBuilder;
    }
    class Builder;
    class Curve;
    class ErrorList;
    class PointList;
    namespace Routing
    {
        class LinearPathSettings;
    }
    namespace Routing
    {
        class PathStockBuilder;
    }
    namespace Routing
    {
        class _QuickPathBuilderBuilder;
        class QuickPathBuilderImpl;
        /** 
                Builder for creating a path between user selected points.

                After invoking the commit method, invoke the 
                @link NXOpen::Routing::QuickPathBuilder::PathErrors NXOpen::Routing::QuickPathBuilder::PathErrors@endlink  method to find
                out which sections between points contained errors.  
             <br> To create a new instance of this class, use @link NXOpen::Routing::RouteManager::CreateQuickPathBuilder  NXOpen::Routing::RouteManager::CreateQuickPathBuilder @endlink  <br> 
        Default values.
        <list type="table"> 
         
        <listheader><term> 
        Property</term>  <description> 
        Value</description> </listheader>
        <item><term> 
         
        PathSettings.LockToSelectedObject </term> <description> 
         
        True </description> </item> 

        </list> 

         <br>  Created in NX6.0.0.  <br>  
        */
        class NXOPENCPP_ROUTINGEXPORT  QuickPathBuilder : public NXOpen::Builder
        {
            private: QuickPathBuilderImpl * m_quickpathbuilder_impl;
            private: friend class  _QuickPathBuilderBuilder;
            protected: QuickPathBuilder();
            public: ~QuickPathBuilder();
            /**Returns  the list of path points.  
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
            public: NXOpen::PointList * PointList
            (
            );
            /**Returns  the stock settings for this path.  
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
            public: NXOpen::Routing::PathStockBuilder * StockSettings
            (
            );
            /**Returns  the errors associated with this path. The list will be NULL if the
                        commit method has not been invoked yet. 
                    
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
            public: NXOpen::ErrorList * PathErrors
            (
            );
            /**Returns  the routing segment managed by the builder, if it exists. 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: NXOpen::Curve * RouteSegment
            (
            );
            /**Returns  the linear path settings for this path.  
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
            public: NXOpen::Routing::LinearPathSettings * PathSettings
            (
            );
            /** Save a point or extension point to the list of all points to draw on the screen.  
             <br>  Created in NX8.5.3.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void SetListOfPointsToDraw
            (
                int index /** The index in the list of points to draw. */,
                const NXOpen::Point3d & point /** Point representing the position. */
            );
            /** Set the number of elements in the list of all points to draw on the screen.  
             <br>  Created in NX10.0.2.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void SetListOfPointsToDrawCount
            (
                int count /** The number of points in list. */
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