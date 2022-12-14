#ifndef NXOpen_ROUTING_DESIGNRULEVIOLATIONLOCATION_HXX_INCLUDED
#define NXOpen_ROUTING_DESIGNRULEVIOLATIONLOCATION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Routing_DesignRuleViolationLocation.ja
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
#include <NXOpen/NXObject.hxx>
#include <NXOpen/Routing_DesignRuleViolationLocationCollection.hxx>
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
        class DesignRuleViolationLocation;
    }
    class NXObject;
    namespace Routing
    {
        class _DesignRuleViolationLocationBuilder;
        class DesignRuleViolationLocationImpl;
        /** Represents @link Routing::DesignRuleViolationLocation Routing::DesignRuleViolationLocation@endlink  object  <br> Design Rule Violation Location object get created automatically during design rule check  <br> 
         <br>  Created in NX6.0.0.  <br>  
        */
        class NXOPENCPP_ROUTINGEXPORT  DesignRuleViolationLocation : public NXObject
        {
            private: DesignRuleViolationLocationImpl * m_designruleviolationlocation_impl;
            private: friend class  _DesignRuleViolationLocationBuilder;
            protected: DesignRuleViolationLocation();
            public: ~DesignRuleViolationLocation();
            /**Returns  the function returns delete location objects, 
                        which is an option for deletion of violation location objects. 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
            public: NXOpen::Routing::DesignRuleViolationLocationCollection::DeleteOption DeleteLocationObjects
            (
            );
            /**Sets  the function returns delete location objects, 
                        which is an option for deletion of violation location objects. 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
            public: void SetDeleteLocationObjects
            (
                NXOpen::Routing::DesignRuleViolationLocationCollection::DeleteOption deleteLocationObjects /** Option to delete object at violation location*/
            );
            /** This function returns an array of all Objects at a violation location along with its count.  @return  Location objects  array.  
             <br>  Created in NX6.0.2.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
            public: std::vector<NXOpen::NXObject *> GetLocationObjects
            (
            );
            /**  
             <br>  Created in NX6.0.2.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
            public: void SetLocationObjects
            (
                const std::vector<NXOpen::NXObject *> & locationObjects /** Location objects  array.  */
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
