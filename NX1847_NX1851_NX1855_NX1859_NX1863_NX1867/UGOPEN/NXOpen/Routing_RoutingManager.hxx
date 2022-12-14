#ifndef NXOpen_ROUTING_ROUTINGMANAGER_HXX_INCLUDED
#define NXOpen_ROUTING_ROUTINGMANAGER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Routing_RoutingManager.ja
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
#include <NXOpen/TaggedObject.hxx>
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
        class RoutingManager;
    }
    class Session;
    namespace Routing
    {
        class BuilderFactory;
    }
    namespace Routing
    {
        class InsulationService;
    }
    namespace Routing
    {
        class RoutingManagerImpl;
        /** Represents an @link NXOpen::Routing::RoutingManager NXOpen::Routing::RoutingManager@endlink  object.   <br> To obtain an instance of this class, refer to @link NXOpen::Session  NXOpen::Session @endlink  <br> 
         <br>  Created in NX1847.0.0.  <br>  
        */
        class NXOPENCPP_ROUTINGEXPORT  RoutingManager
        {
            private: RoutingManagerImpl * m_routingmanager_impl;
            private: NXOpen::Session* m_owner;
            /// \cond NX_NO_DOC 
            public: explicit RoutingManager(NXOpen::Session *owner);


            /// \endcond 
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            private: static RoutingManager* theRoutingManager;
            /** Returns the RoutingManager object for the running session which serves as the 'gateway' class for the application API.  
                References to all other objects in this API are obtained either directly or indirectly via methods and properties on this class.  
                Platform Session should be initialized using 'GetSession' method from NXOpen API prior to this call.  
            */
            public: static RoutingManager* GetRoutingManager(NXOpen::Session *owner);
            public: ~RoutingManager();


            /**  Returns a @link NXOpen::Routing::BuilderFactory NXOpen::Routing::BuilderFactory@endlink  object.  Use this object
                         to create specific routing builders.
                    
             <br>  Created in NX1847.0.0.  <br>  
            */
            public: NXOpen::Routing::BuilderFactory *BuilderFactory();
            /**  Returns a @link NXOpen::Routing::InsulationService NXOpen::Routing::InsulationService@endlink  object.  Use this object
                         for specific Routing  Insulation service
                    
             <br>  Created in NX1847.0.0.  <br>  
            */
            public: NXOpen::Routing::InsulationService *InsulationService();
        }; //lint !e1712 default constructor not defined for class  

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
