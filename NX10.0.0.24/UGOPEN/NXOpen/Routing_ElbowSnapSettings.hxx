#ifndef NXOpen_ROUTING_ELBOWSNAPSETTINGS_HXX_INCLUDED
#define NXOpen_ROUTING_ELBOWSNAPSETTINGS_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Routing_ElbowSnapSettings.ja
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
#include <NXOpen/Routing_ElbowSnapSettings.hxx>
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
        class ElbowSnapSettings;
    }
    class Builder;
    namespace Routing
    {
        class _ElbowSnapSettingsBuilder;
        class ElbowSnapSettingsImpl;
        /** Helper object used the by @link Routing::LinearPathBuilder Routing::LinearPathBuilder@endlink  builder. 
                Determines whether or not elbow snapping should occur in the "Create Linear Path"
                UI, and if so, what the angle tolerance should be.
             <br> To create a new instance of this class, use @link NXOpen::Routing::RouteManager::CreateElbowSnapSettings  NXOpen::Routing::RouteManager::CreateElbowSnapSettings @endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        AngleTolerance </td> <td> 
         
        5.0 </td> </tr> 

        <tr><td> 
         
        SnapToElbowAngles </td> <td> 
         
        True </td> </tr> 

        </table>  

         <br>  Created in NX5.0.0.  <br>  
        */
        class NXOPENCPP_ROUTINGEXPORT  ElbowSnapSettings : public NXOpen::Builder
        {
            private: ElbowSnapSettingsImpl * m_elbowsnapsettings_impl;
            private: friend class  _ElbowSnapSettingsBuilder;
            protected: ElbowSnapSettings();
            public: ~ElbowSnapSettings();
            /**Returns  whether or not to snap control points to the nearest valid elbow angle. 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: bool SnapToElbowAngles
            (
            );
            /**Sets  whether or not to snap control points to the nearest valid elbow angle. 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void SetSnapToElbowAngles
            (
                bool doSnap /** do snap */ 
            );
            /**Returns  the tolerance within which to search for elbow angles. 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: double AngleTolerance
            (
            );
            /**Sets  the tolerance within which to search for elbow angles. 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void SetAngleTolerance
            (
                double tolerance /** tolerance */ 
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