#ifndef NXOpen_ROUTING_WIRE_HXX_INCLUDED
#define NXOpen_ROUTING_WIRE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Routing_Wire.ja
//
//  Generated by:
//     apiwrap
//
//  WARNING:
//    This file is automatically generated - do not edit by hand
//
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Routing_IPath.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Routing
    {
        class Wire;
    }
    namespace Routing
    {
        class IPath;
    }
    namespace Routing
    {
        class Stock;
    }
    namespace Routing
    {
        /** The Routing Wire object is the set of information needed to define
             * a ROUTE_wire.  */
        class NXOPENCPPEXPORT Wire : public virtual Routing::IPath
        {
            /**Returns  the stocks for the wire.  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: virtual std::vector<NXOpen::Routing::Stock *> Stock
            (
            ) = 0;
        };
    }
}
#undef EXPORTLIBRARY
#endif
