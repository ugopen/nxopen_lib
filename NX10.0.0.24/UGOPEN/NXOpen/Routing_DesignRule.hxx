#ifndef NXOpen_ROUTING_DESIGNRULE_HXX_INCLUDED
#define NXOpen_ROUTING_DESIGNRULE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Routing_DesignRule.ja
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
        class DesignRule;
    }
    class NXObject;
    namespace Routing
    {
        class DesignRuleViolation;
    }
    namespace Routing
    {
        class _DesignRuleBuilder;
        class DesignRuleImpl;
        /** Represents @link NXOpen::Routing::DesignRule NXOpen::Routing::DesignRule@endlink  object  <br> Creator not available in KF.  <br> 
         <br>  Created in NX4.0.2.  <br>  
        */
        class NXOPENCPP_ROUTINGEXPORT  DesignRule : public NXOpen::NXObject
        {
            private: DesignRuleImpl * m_designrule_impl;
            private: friend class  _DesignRuleBuilder;
            protected: DesignRule();
            public: ~DesignRule();
            /**Returns  the name of the design rule is returned 
             <br>  Created in NX4.0.2.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
            public: NXString Drname
            (
            );
            /**Returns  the description of the design rule is returned 
             <br>  Created in NX4.0.2.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
            public: NXString Description
            (
            );
            /**Returns  the application of the design rule that it belongs to is returned 
             <br>  Created in NX4.0.2.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
            public: NXString Application
            (
            );
            /** Violation of the design rule are returned  @return  
             <br>  Created in NX4.0.2.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
            public: std::vector<NXOpen::Routing::DesignRuleViolation *> GetViolations
            (
            );
            /** Violation are added to the design rule 
             <br>  Created in NX4.0.2.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
            public: void AddViolations
            (
                const std::vector<NXOpen::Routing::DesignRuleViolation *> & violations /** violations */ 
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