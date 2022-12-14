#ifndef NXOpen_ROUTING_INSTANCENAMELOOKUPBUILDER_HXX_INCLUDED
#define NXOpen_ROUTING_INSTANCENAMELOOKUPBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Routing_InstanceNameLookupBuilder.ja
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
#include <NXOpen/Routing_InstanceNameLookupBuilder.hxx>
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
        class InstanceNameLookupBuilder;
    }
    class Builder;
    namespace Routing
    {
        class _InstanceNameLookupBuilderBuilder;
        class InstanceNameLookupBuilderImpl;
        /** Represents a @link Routing::InstanceNameLookupBuilder Routing::InstanceNameLookupBuilder@endlink . 
                Routing.InstanceNameLookupBuilder is used to look up the matching part to place
                based on the criteria defined in the INSTANCE_NAME_LOOKUP node and the ship 
                identifier specified in the customer defaults. <br> To create a new instance of this class, use @link Routing::RouteManager::CreateInstanceNameLookupBuilder  Routing::RouteManager::CreateInstanceNameLookupBuilder @endlink  <br> 
         <br>  Created in NX8.0.0.  <br>  
        */
        class NXOPENCPP_ROUTINGEXPORT  InstanceNameLookupBuilder : public Builder
        {
            private: InstanceNameLookupBuilderImpl * m_instancenamelookupbuilder_impl;
            private: friend class  _InstanceNameLookupBuilderBuilder;
            protected: InstanceNameLookupBuilder();
            public: ~InstanceNameLookupBuilder();
            /**Returns  the instance name 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : routing_pipetube ("Routing Piping and Tubing") */
            public: NXString InstanceNameCombo
            (
            );
            /**Sets  the instance name 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : routing_pipetube ("Routing Piping and Tubing") */
            public: void SetInstanceNameCombo
            (
                const NXString & instanceNameCombo /** instancenamecombo */ 
            );
            /**Sets  the instance name 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : routing_pipetube ("Routing Piping and Tubing") */
            void SetInstanceNameCombo
            (
                const char * instanceNameCombo /** instancenamecombo */ 
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
