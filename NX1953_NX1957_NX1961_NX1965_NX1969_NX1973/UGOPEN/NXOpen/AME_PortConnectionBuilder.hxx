#ifndef NXOpen_AME_PORTCONNECTIONBUILDER_HXX_INCLUDED
#define NXOpen_AME_PORTCONNECTIONBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     AME_PortConnectionBuilder.ja
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
#include <NXOpen/SelectObject.hxx>
#include <NXOpen/libameopencpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace AME
    {
        class PortConnectionBuilder;
    }
    namespace AME
    {
        class SelectAMEBaseNode;
    }
    class Builder;
    class NXObject;
    namespace AME
    {
        class _PortConnectionBuilderBuilder;
        class PortConnectionBuilderImpl;
        /** builder for the port connector dialog <br> To create a new instance of this class, use @link NXOpen::AME::AMEManager::CreatePortConnectionBuilder  NXOpen::AME::AMEManager::CreatePortConnectionBuilder @endlink  <br> 
         <br>  Created in NX11.0.0.  <br>  
        */
        class AMEOPENCPPEXPORT  PortConnectionBuilder : public NXOpen::Builder
        {
            private: PortConnectionBuilderImpl * m_portconnectionbuilder_impl;
            private: friend class  _PortConnectionBuilderBuilder;
            protected: PortConnectionBuilder();
            public: ~PortConnectionBuilder();
            /**Returns  the source port 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXOpen::AME::SelectAMEBaseNode * SelectedSourcePort
            (
            );
            /** Sets ports to connect 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetTargetPorts
            (
                const std::vector<NXOpen::NXObject *> & ports /** The ports tag array*/
            );
            /** Disconnects given ports each other
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void Disconnect
            (
                NXOpen::NXObject * port1 /** port1 */ ,
                NXOpen::NXObject * port2 /** port2 */ 
            );
            /** Disconnects given port
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void Disconnect
            (
                NXOpen::NXObject * portToDisconnect /** porttodisconnect */ 
            );
            /**Returns  
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: bool AutoLinked
            (
            );
            /**Sets  
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetAutoLinked
            (
                bool autoLinked /** autolinked */ 
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
