#ifndef NXOpen_ROUTING_FEATUREPORT_HXX_INCLUDED
#define NXOpen_ROUTING_FEATUREPORT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Routing_FeaturePort.ja
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
#include <NXOpen/Features_Feature.hxx>
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
        class FeaturePort;
    }
    namespace Features
    {
        class Feature;
    }
    namespace Routing
    {
        class _FeaturePortBuilder;
        class FeaturePortImpl;
        /** @link Routing::FeaturePort Routing::FeaturePort@endlink  is a @link Features::Feature Features::Feature@endlink  associated
                with @link Routing::Port Routing::Port@endlink .  <br> Creator not available  <br> 
         <br>  Created in NX6.0.0.  <br>  
        */
        class NXOPENCPP_ROUTINGEXPORT  FeaturePort : public Features::Feature
        {
            private: FeaturePortImpl * m_featureport_impl;
            private: friend class  _FeaturePortBuilder;
            protected: FeaturePort();
            public: ~FeaturePort();
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