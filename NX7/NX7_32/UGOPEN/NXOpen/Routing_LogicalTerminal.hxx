#ifndef NXOpen_ROUTING_LOGICALTERMINAL_HXX_INCLUDED
#define NXOpen_ROUTING_LOGICALTERMINAL_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Routing_LogicalTerminal.ja
//
//  Generated by:
//     apiwrap
//
//  WARNING:
//    This file is automatically generated - do not edit by hand
//
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/Routing_RouteObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Routing
    {
        class LogicalTerminal;
    }
    namespace Routing
    {
        class InterfaceTerminalShadow;
    }
    namespace Routing
    {
        class Port;
    }
    namespace Routing
    {
        class RouteObject;
    }
    namespace Routing
    {
        class SingleDevice;
    }
    namespace Routing
    {
        class _LogicalTerminalBuilder;
        /** 
                Assembly instance of a @link Routing::InterfaceTerminalBase Routing::InterfaceTerminalBase@endlink .
                
                 <br> 
                @link Routing::LogicalTerminal Routing::LogicalTerminal@endlink  corresponds to NX
                occurrences of @link Routing::MultiPort Routing::MultiPort@endlink s,
                @link Routing::TerminalPort Routing::TerminalPort@endlink s or
                @link Routing::FittingPort Routing::FittingPort@endlink s.  Multiple ports can be
                associated to a single
                @link Routing::LogicalTerminal Routing::LogicalTerminal@endlink .
                 <br> 
                 <br> 
                See NX Routing help for the Connectivity data model documentation.
                 <br> 
             <br> Creator not available in KF. <br> */
        class NXOPENCPPEXPORT LogicalTerminal : public Routing::RouteObject
        {
            private: friend class  _LogicalTerminalBuilder;
            protected: LogicalTerminal();
            /**Returns  the @link Routing::InterfaceTerminalShadow Routing::InterfaceTerminalShadow@endlink  corresponding to @link Routing::Port Routing::Port@endlink  in piece part.
                     <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: NXOpen::Routing::InterfaceTerminalShadow * InterfaceTerminalShadow
            (
            );
            /**Returns  the physical @link Routing::Port Routing::Port@endlink  associated with the terminal.
                         <br> 
                        The physical @link Routing::Port Routing::Port@endlink  corresponds to a port occurrence.
                         <br> 
                     <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: NXOpen::Routing::Port * Port
            (
            );
            /** Get the physical @link Routing::Port Routing::Port@endlink s associated with the terminal.
                         <br> 
                        The physical @link Routing::Port Routing::Port@endlink  corresponds to a port occurrence.
                         <br> 
                        Depricated in NX4.
                     @return    <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: std::vector<NXOpen::Routing::Port *> GetPorts
            (
            );
            /** Add a physical @link Routing::Port Routing::Port@endlink  to the
                        terminal.  If NULL, nothing is added.
                         <br> 
                        The physical @link Routing::Port Routing::Port@endlink  corresponds to a port occurrence.
                         <br> 
                     <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: void AddPort
            (
                NXOpen::Routing::Port * port /** Port to add to the terminal */
            );
            /** Remove a physical @link Routing::Port Routing::Port@endlink  from the
                        terminal.  If the @link Routing::Port Routing::Port@endlink  is not
                        associated to the @link Routing::LogicalTerminal Routing::LogicalTerminal@endlink 
                        or is NULL, nothing is done.
                         <br> 
                        The physical @link Routing::Port Routing::Port@endlink  corresponds to a port occurrence.
                         <br> 
                     <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: void RemovePort
            (
                NXOpen::Routing::Port * port /** Port to remove from the terminal */
            );
            /** Clears the @link Routing::Port Routing::Port@endlink  of all
                        @link Routing::Port Routing::Port@endlink s.
                     <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: void ClearAllPorts
            (
            );
            /** The physical connector associated with the @link Routing::Port Routing::Port@endlink .
                         <br> 
                        Assumes that a @link Routing::Port Routing::Port@endlink  cannot be associated to more than one physical connector at any time.
                         <br> 
                     @return   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: NXOpen::Routing::SingleDevice * GetParentConnector
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
