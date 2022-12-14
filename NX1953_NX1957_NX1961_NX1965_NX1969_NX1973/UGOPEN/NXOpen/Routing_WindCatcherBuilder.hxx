#ifndef NXOpen_ROUTING_WINDCATCHERBUILDER_HXX_INCLUDED
#define NXOpen_ROUTING_WINDCATCHERBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Routing_WindCatcherBuilder.ja
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
        class WindCatcherBuilder;
    }
    class Builder;
    class Expression;
    namespace Routing
    {
        class LineSegment;
    }
    namespace Routing
    {
        class Stock;
    }
    namespace Routing
    {
        class _WindCatcherBuilderBuilder;
        class WindCatcherBuilderImpl;
        /** Builder class for Wind Catcher feature. See @link NXOpen::Routing::WindCatcher NXOpen::Routing::WindCatcher@endlink 
                for the Wind Catcher class documentation.
             <br> To create a new instance of this class, use @link NXOpen::Routing::RouteManager::CreateWindCatcherBuilder  NXOpen::Routing::RouteManager::CreateWindCatcherBuilder @endlink  <br> 
         <br>  Created in NX8.5.0.  <br>  
        */
        class NXOPENCPP_ROUTINGEXPORT  WindCatcherBuilder : public NXOpen::Builder
        {
            /** Specifies the type of Wind Catcher. */
            public: enum WindCatcherType
            {
                WindCatcherTypeArc/** arc */ ,
                WindCatcherTypeTriangle/** triangle */ 
            };

            private: WindCatcherBuilderImpl * m_windcatcherbuilder_impl;
            private: friend class  _WindCatcherBuilderBuilder;
            protected: WindCatcherBuilder();
            public: ~WindCatcherBuilder();
            /**Returns  the type of Wind Catcher. 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : routing_hvac ("Routing HVAC") */
            public: NXOpen::Routing::WindCatcherBuilder::WindCatcherType Type
            (
            );
            /**Sets  the type of Wind Catcher. 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : routing_hvac ("Routing HVAC") */
            public: void SetType
            (
                NXOpen::Routing::WindCatcherBuilder::WindCatcherType windCatcherType /** windcatchertype */ 
            );
            /**Returns  the duct from which the Wind Catcher derives the wind direction. 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : routing_hvac ("Routing HVAC") */
            public: NXOpen::Routing::Stock * ParentDuct
            (
            );
            /**Sets  the duct from which the Wind Catcher derives the wind direction. 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : routing_hvac ("Routing HVAC") */
            public: void SetParentDuct
            (
                NXOpen::Routing::Stock * parentDuct /** parentduct */ 
            );
            /**Returns  the duct on which the Wind Catcher attaches. 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : routing_hvac ("Routing HVAC") */
            public: NXOpen::Routing::Stock * WindCatcherDuct
            (
            );
            /**Sets  the duct on which the Wind Catcher attaches. 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : routing_hvac ("Routing HVAC") */
            public: void SetWindCatcherDuct
            (
                NXOpen::Routing::Stock * windCatcherDuct /** windcatcherduct */ 
            );
            /**Returns  the flag that indicates whether the wind direction is reversed from its normal direction.
                    **  The normal direction for the wind either matches the flow direction, if the parent stock
                    **  is part of a Run, or matches the parent stock's segment direction from the start control point
                    **  to the end control point.
                    
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : routing_hvac ("Routing HVAC") */
            public: bool ReverseWindDirection
            (
            );
            /**Returns  the angle in degrees between the wind direction vector and the open face of the Wind Catcher.
                    
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : routing_hvac ("Routing HVAC") */
            public: NXOpen::Expression * EndAngleExpression
            (
            );
            /**Sets  the flag that indicates whether the wind direction is reversed from its normal direction.
                    **  The normal direction for the wind either matches the flow direction, if the parent stock
                    **  is part of a Run, or matches the parent stock's segment direction from the start control point
                    **  to the end control point.
                    
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : routing_hvac ("Routing HVAC") */
            public: void SetReverseWindDirection
            (
                bool windDirection /** winddirection */ 
            );
            /**Returns  the flag that indicates whether the Wind Catcher's duct should be trimmed back to the top of the parent duct. 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : routing_hvac ("Routing HVAC") */
            public: bool TrimToParentDuct
            (
            );
            /**Sets  the flag that indicates whether the Wind Catcher's duct should be trimmed back to the top of the parent duct. 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : routing_hvac ("Routing HVAC") */
            public: void SetTrimToParentDuct
            (
                bool trim /** trim */ 
            );
            /** Returns the linear segment under the Parent Duct that is closest to the Wind Catcher. 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : routing_hvac ("Routing HVAC") */
            public: NXOpen::Routing::LineSegment * GetClosestParentDuctSegment
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
