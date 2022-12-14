#ifndef NXOpen_ROUTING_ROUTELOGICALASSOCIATION_HXX_INCLUDED
#define NXOpen_ROUTING_ROUTELOGICALASSOCIATION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Routing_RouteLogicalAssociation.ja
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
        class RouteLogicalAssociation;
    }
    class NXObject;
    namespace Routing
    {
        class _RouteLogicalAssociationBuilder;
        class RouteLogicalAssociationImpl;
        /** RouteLogicalAssociation object associates non-electrical components to 
                electrical components. Logical Associations have control objects and 
                target objects.  Meeting control object's condition applies actions to 
                target objects. Example: Control object is a @link NXOpen::Routing::ISegment NXOpen::Routing::ISegment@endlink 
                and the target object is a clip or clamp which supports the harness. When
                the segment is routed (i.e. condition on control object is satisfied), 
                the action is to suppress the target (clip or clamp)  <br> To obtain an instance of this class use @link NXOpen::Routing::RouteLogicalAssociationCollection NXOpen::Routing::RouteLogicalAssociationCollection@endlink   <br> 
         <br>  Created in NX4.0.0.  <br>  
        */
        class NXOPENCPP_ROUTINGEXPORT  RouteLogicalAssociation : public NXOpen::NXObject
        {
            private: RouteLogicalAssociationImpl * m_routelogicalassociation_impl;
            private: friend class  _RouteLogicalAssociationBuilder;
            protected: RouteLogicalAssociation();
            public: ~RouteLogicalAssociation();
            /** Performs the specified action (suppress or unsuppress) on the 
                        RouteLogicalAssociation Object 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : routing_harness ("Routing Harness") */
            public: void Perform
            (
            );
            /** Removes the RouteLogicalAssociation object 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : routing_harness ("Routing Harness") */
            public: void Remove
            (
            );
            /** Retrieves the control for LogicalAssocition  @return  Control 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : routing_harness ("Routing Harness") */
            public: NXOpen::NXObject * GetControl
            (
            );
            /** Sets the control for LogicalAssocition 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : routing_harness ("Routing Harness") */
            public: void SetControl
            (
                NXOpen::NXObject * control /** Control */
            );
            /** Get all the targets LogicalAssocition  @return  Targets of current logical association  
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : routing_harness ("Routing Harness") */
            public: std::vector<NXOpen::NXObject *> GetTargets
            (
            );
            /** Adds target to Logical Assocition 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : routing_harness ("Routing Harness") */
            public: void AddTarget
            (
                NXOpen::NXObject * target /** Target to add */
            );
            /** Removes the target from Logical Assocition 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : routing_harness ("Routing Harness") */
            public: void RemoveTarget
            (
                NXOpen::NXObject * target /** Target to remove */
            );
            /** Get the routed condition of a logical association object.  
                      * The routed condition evaluates the state of the control object.
                      * True if condition is ROUTED, False if UNROUTED 
                       @return   
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : routing_harness ("Routing Harness") */
            public: bool GetRoutedCondition
            (
            );
            /** Set the routed condition of a logical association object 
                      * The routed condition evaluates the state of the control object.
                      * True if condition is ROUTED, False if UNROUTED 
                      
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : routing_harness ("Routing Harness") */
            public: void SetRoutedCondition
            (
                bool condition /** condition */ 
            );
            /** Set Logical Association to enabled state or disabled state.                 
                      * True sets LAO to enabled state, False sets LAO to disabled state.
                      
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : routing_harness ("Routing Harness") */
            public: void EnableLogicalAssociation
            (
                bool enable /** True or False */
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
