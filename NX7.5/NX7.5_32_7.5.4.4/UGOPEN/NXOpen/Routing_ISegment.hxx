#ifndef NXOpen_ROUTING_ISEGMENT_HXX_INCLUDED
#define NXOpen_ROUTING_ISEGMENT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Routing_ISegment.ja
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
#include <NXOpen/Routing_ICharacteristic.hxx>
#include <NXOpen/Routing_SegmentManager.hxx>
#include <NXOpen/ugmath.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Routing
    {
        class ISegment;
    }
    namespace Assemblies
    {
        class Component;
    }
    class Curve;
    namespace Routing
    {
        class ControlPoint;
    }
    namespace Routing
    {
        namespace Electrical
        {
            class CableDevice;
        }
    }
    namespace Routing
    {
        namespace Electrical
        {
            class CablewaysLayoutView;
        }
    }
    namespace Routing
    {
        class ICharacteristic;
    }
    namespace Routing
    {
        class Stock;
    }
    namespace Routing
    {
        /** Interface class for all routing segments [Line/Arc/Spline] */
        class NXOPENCPPEXPORT  ISegment : public virtual Routing::ICharacteristic
        {
            public: virtual ~ISegment() {}
            /**  Return of segment end control points.
                         The @link Routing::ControlPoint Routing::ControlPoint@endlink  defines an end of a segment  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: virtual void GetEndRcps
            (
                NXOpen::Routing::ControlPoint ** startRcp /** RCP defining start of segment */,
                NXOpen::Routing::ControlPoint ** endRcp /** RCP defining end of segment */
            ) = 0;
            /**  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: virtual void SetEndRcps
            (
                NXOpen::Routing::ControlPoint * startRcp /** RCP defining start of segment */,
                NXOpen::Routing::ControlPoint * endRcp /** RCP defining end of segment */
            ) = 0;
            /**  Get the current location of the segment ends in ABS coordinates.  This value is
                         overridden by the coordinates of the end RCPs associated with this segment.  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: virtual void GetEndPoints
            (
                NXOpen::Point3d* startPoint /** Location of end 0 in ABS coordinates */,
                NXOpen::Point3d* endPoint /** Location of end 1 in ABS coordinates */
            ) = 0;
            /**  Set the current location of the segment ends in ABS coordinates.  This value is
                         overridden by the coordinates of the end RCPs associated with this segment.  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: virtual void SetEndPoints
            (
                const NXOpen::Point3d & startPoint /** New location of end 0 in ABS coordinates */,
                const NXOpen::Point3d & endPoint /** New location of end 1 in ABS coordinates */
            ) = 0;
            /**Returns   the segment follow curve.  NULL object indicates segment has no follow curve  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: virtual NXOpen::Curve * FollowCurve
            (
            ) = 0;
            /** Is given segment a terminal segment?  @return  Is segment a terminal segment?  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: virtual NXOpen::Routing::Terminal GetIsTerminalSegment
            (
            ) = 0;
            /** Set given segment to be a terminal segment?  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: virtual void SetIsTerminalSegment
            (
                NXOpen::Routing::Terminal isTerminal /** Set as terminal segment? */
            ) = 0;
            /** Query if a segment is interior to any part  @return  Is segment interior?  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: virtual NXOpen::Routing::Interior GetIsSegmentInterior
            (
            ) = 0;
            /** Set a segment to be interior to supplied part  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: virtual void SetSegmentInteriorPart
            (
                NXOpen::Assemblies::Component * interiorPart /** Part segment interior? */
            ) = 0;
            /** Returns all stocks that directly reference this segment as part of the path defining the stock.  @return   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: virtual std::vector<NXOpen::Routing::Stock *> GetSegmentStock
            (
            ) = 0;
            /** Returns @link Routing::Stock Routing::Stock@endlink  as well as @link Routing::Overstock Routing::Overstock@endlink 
                        objects from the @link Routing::ISegment Routing::ISegment@endlink .  @return  Array of stocks/overstocks.  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: virtual std::vector<NXOpen::Routing::Stock *> GetSegmentAllStocks
            (
            ) = 0;
            /** Returns @link Routing::Electrical::CablewaysLayoutView Routing::Electrical::CablewaysLayoutView@endlink  objects
                           from the @link Routing::ISegment Routing::ISegment@endlink .  @return  Array of cableways layout views.  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") */
            public: virtual std::vector<NXOpen::Routing::Electrical::CablewaysLayoutView *> GetCablewaysLayoutViews
            (
            ) = 0;
            /** Returns @link Routing::Electrical::CableDevice Routing::Electrical::CableDevice@endlink  objects
                           from @link Routing::ISegment Routing::ISegment@endlink .  @return  Array of cable devices.  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") */
            public: virtual std::vector<NXOpen::Routing::Electrical::CableDevice *> GetCableDevices
            (
            ) = 0;
        };
    }
}
#undef EXPORTLIBRARY
#endif