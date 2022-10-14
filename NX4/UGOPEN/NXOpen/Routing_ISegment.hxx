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
#include <vector>
#include <NXOpen/NXString.hxx>
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
        class ICharacteristic;
    }
    namespace Routing
    {
        /** Interface class for all routing segments [Line/Arc/Spline] */
        class NXOPENCPPEXPORT ISegment : public virtual Routing::ICharacteristic
        {
            /**  Return of segment end control points.
                         The @link Routing::ControlPoint Routing::ControlPoint@endlink  defines an end of a segment  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: virtual void GetEndRcps
            (
                NXOpen::Routing::ControlPoint ** start_rcp /** RCP defining start of segment */,
                NXOpen::Routing::ControlPoint ** end_rcp /** RCP defining end of segment */
            ) = 0;
            /**  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: virtual void SetEndRcps
            (
                NXOpen::Routing::ControlPoint * start_rcp /** RCP defining start of segment */,
                NXOpen::Routing::ControlPoint * end_rcp /** RCP defining end of segment */
            ) = 0;
            /**  Get the current location of the segment ends in ABS coordinates.  This value is
                         overridden by the coordinates of the end RCPs associated with this segment.  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: virtual void GetEndPoints
            (
                NXOpen::Point3d* start_point /** Location of end 0 in ABS coordinates */,
                NXOpen::Point3d* end_point /** Location of end 1 in ABS coordinates */
            ) = 0;
            /**  Set the current location of the segment ends in ABS coordinates.  This value is
                         overridden by the coordinates of the end RCPs associated with this segment.  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: virtual void SetEndPoints
            (
                const NXOpen::Point3d & start_point /** New location of end 0 in ABS coordinates */,
                const NXOpen::Point3d & end_point /** New location of end 1 in ABS coordinates */
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
                NXOpen::Routing::Terminal is_terminal /** Set as terminal segment? */
            ) = 0;
            /** Query if a segment is interior to any part  @return  Is segment interior?  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: virtual NXOpen::Routing::Interior GetIsSegmentInterior
            (
            ) = 0;
            /** Set a segment to be interior to supplied part  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: virtual void SetSegmentInteriorPart
            (
                NXOpen::Assemblies::Component * interior_part /** Part segment interior? */
            ) = 0;
        };
    }
}
#undef EXPORTLIBRARY
#endif