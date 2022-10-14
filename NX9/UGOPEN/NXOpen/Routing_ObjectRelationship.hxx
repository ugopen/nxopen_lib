#ifndef NXOpen_ROUTING_OBJECTRELATIONSHIP_HXX_INCLUDED
#define NXOpen_ROUTING_OBJECTRELATIONSHIP_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Routing_ObjectRelationship.ja
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
#include <NXOpen/Routing_RootObject.hxx>
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
        class ObjectRelationship;
    }
    namespace Routing
    {
        class RootObject;
    }
    namespace Routing
    {
        class _ObjectRelationshipBuilder;
        class ObjectRelationshipImpl;
        /** @brief 
                 Represents a relationship between Routing objects.
                

         
                <br> 
                 ObjectRelationship is the abstract base class for @link InterfaceTerminalRelationshipBase InterfaceTerminalRelationshipBase@endlink 
                 and @link DeviceRelationship DeviceRelationship@endlink .  This class is reserved for future use.
                <br>  
             <br> No creator is available in KF because this is an abstract class.  <br> 
         <br>  Created in NX4.0.2.  <br>  
        */
        class NXOPENCPP_ROUTINGEXPORT  ObjectRelationship : public Routing::RootObject
        {
            private: ObjectRelationshipImpl * m_objectrelationship_impl;
            private: friend class  _ObjectRelationshipBuilder;
            protected: ObjectRelationship();
            public: ~ObjectRelationship();
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