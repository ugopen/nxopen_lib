#ifndef NXOpen_ROUTING_ROUTEOBJECTCOLLECTOR_HXX_INCLUDED
#define NXOpen_ROUTING_ROUTEOBJECTCOLLECTOR_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Routing_RouteObjectCollector.ja
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
#include <NXOpen/GeometricUtilities_IComponentBuilder.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/SelectObjectList.hxx>
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
        class RouteObjectCollector;
    }
    namespace GeometricUtilities
    {
        class IComponentBuilder;
    }
    class SelectNXObjectList;
    namespace Routing
    {
        class _RouteObjectCollectorBuilder;
        class RouteObjectCollectorImpl;
        /** Represents a @link NXOpen::Routing::RouteObjectCollector NXOpen::Routing::RouteObjectCollector@endlink  class
                to create objects for getting routing objects.
            
         <br>  Created in NX6.0.0.  <br>  
        */
        class NXOPENCPP_ROUTINGEXPORT  RouteObjectCollector : public NXOpen::TaggedObject, public virtual NXOpen::GeometricUtilities::IComponentBuilder
        {
            private: RouteObjectCollectorImpl * m_routeobjectcollector_impl;
            private: friend class  _RouteObjectCollectorBuilder;
            protected: RouteObjectCollector();
            public: ~RouteObjectCollector();
            /**Returns  the selected routing object list 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: NXOpen::SelectNXObjectList * RoutingObjects
            (
            );
            /** Validate whether the inputs to the component are sufficient for 
                        commit to be called.  If the component is not in a state to commit
                        then an exception is thrown.  For example, if the component requires
                        you to set some property, this method will throw an exception if
                        you haven't set it.  This method throws a not yet implemented
                        NXException for some components.
                     @return  Was self validation successful 
             <br>  Created in NX3.0.1.  <br>  
             <br> License requirements : None */
            public: virtual bool Validate
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
