#ifndef NXOpen_ROUTING_WINDCATCHER_HXX_INCLUDED
#define NXOpen_ROUTING_WINDCATCHER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Routing_WindCatcher.ja
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
#include <NXOpen/Features_BodyFeature.hxx>
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
        class WindCatcher;
    }
    namespace Features
    {
        class BodyFeature;
    }
    namespace Routing
    {
        class _WindCatcherBuilder;
        class WindCatcherImpl;
        /** Represents a Wind Catcher feature.
                Use the @link Routing::WindCatcherBuilder Routing::WindCatcherBuilder@endlink  class to create a Wind Catcher feature.  <br> To create or edit an instance of this class, use @link Routing::WindCatcherBuilder  Routing::WindCatcherBuilder @endlink  <br> 
         <br>  Created in NX8.5.0.  <br>  
        */
        class NXOPENCPP_ROUTINGEXPORT  WindCatcher : public Features::BodyFeature
        {
            private: WindCatcherImpl * m_windcatcher_impl;
            private: friend class  _WindCatcherBuilder;
            protected: WindCatcher();
            public: ~WindCatcher();
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