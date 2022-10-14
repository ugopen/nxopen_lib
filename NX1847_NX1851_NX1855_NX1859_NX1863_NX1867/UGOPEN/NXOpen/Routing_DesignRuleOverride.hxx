#ifndef NXOpen_ROUTING_DESIGNRULEOVERRIDE_HXX_INCLUDED
#define NXOpen_ROUTING_DESIGNRULEOVERRIDE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Routing_DesignRuleOverride.ja
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
        class DesignRuleOverride;
    }
    class NXObject;
    namespace Routing
    {
        class DesignRuleViolation;
    }
    namespace Routing
    {
        class _DesignRuleOverrideBuilder;
        class DesignRuleOverrideImpl;
        /** Represents Routing DesignRuleOverride object  <br> Creator not available in KF.  <br> 
         <br>  Created in NX4.0.2.  <br>  
        */
        class NXOPENCPP_ROUTINGEXPORT  DesignRuleOverride : public NXOpen::NXObject
        {
            private: DesignRuleOverrideImpl * m_designruleoverride_impl;
            private: friend class  _DesignRuleOverrideBuilder;
            protected: DesignRuleOverride();
            public: ~DesignRuleOverride();
            /**Returns  the user of the design rule override is returned 
             <br>  Created in NX4.0.2.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
            public: NXString User
            (
            );
            /**Sets  the user of the design rule override is returned 
             <br>  Created in NX4.0.2.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
            public: void SetUser
            (
                const NXString & user /** user */ 
            );
            /**Sets  the user of the design rule override is returned 
             <br>  Created in NX4.0.2.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
            void SetUser
            (
                const char * user /** user */ 
            );
            /**Returns  the reason of the design rule override is returned 
             <br>  Created in NX4.0.2.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
            public: NXString Reason
            (
            );
            /**Sets  the reason of the design rule override is returned 
             <br>  Created in NX4.0.2.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
            public: void SetReason
            (
                const NXString & name /** name */ 
            );
            /**Sets  the reason of the design rule override is returned 
             <br>  Created in NX4.0.2.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
            void SetReason
            (
                const char * name /** name */ 
            );
            /**Returns  the time stamp of the design rule override is returned 
             <br>  Created in NX4.0.2.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
            public: int TimeStamp
            (
            );
            /**Sets  the time stamp of the design rule override is returned 
             <br>  Created in NX4.0.2.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
            public: void SetTimeStamp
            (
                int timeStamp /** timestamp */ 
            );
            /** Returns the violation of this override. 
             <br>  Created in NX12.0.1.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
            public: NXOpen::Routing::DesignRuleViolation * GetViolation
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