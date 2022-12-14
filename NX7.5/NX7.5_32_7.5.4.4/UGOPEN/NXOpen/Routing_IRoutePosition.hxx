#ifndef NXOpen_ROUTING_IROUTEPOSITION_HXX_INCLUDED
#define NXOpen_ROUTING_IROUTEPOSITION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Routing_IRoutePosition.ja
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
#include <NXOpen/ugmath.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Routing
    {
        class IRoutePosition;
    }
    class Point;
    namespace Routing
    {
        class ICharacteristic;
    }
    namespace Routing
    {
        /** 
                Interface class for all routing objects that specify a single (possibly associative) location
                in space.
             */
        class NXOPENCPPEXPORT  IRoutePosition : public virtual Routing::ICharacteristic
        {
            public: virtual ~IRoutePosition() {}
            /**Returns   the current location of the object in ABS coordinates.  This value is
                          overridden by the coordinates of the point associated with this object.  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: virtual NXOpen::Point3d Position
            (
            ) = 0;
            /**Sets   the current location of the object in ABS coordinates.  This value is
                          overridden by the coordinates of the point associated with this object.  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: virtual void SetPosition
            (
                const NXOpen::Point3d & position /** New location of object in ABS coordinates */
            ) = 0;
            /**Returns  the @link Point Point@endlink  that specifies the location of the
                        @link Routing::IRoutePosition Routing::IRoutePosition@endlink  object.  A NULL object indicates that this
                        object is not associated to any point.   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: virtual NXOpen::Point * Point
            (
            ) = 0;
            /**Sets  the @link Point Point@endlink  that specifies the location of the
                        @link Routing::IRoutePosition Routing::IRoutePosition@endlink  object.  A NULL object indicates that this
                        object is not associated to any point.   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: virtual void SetPoint
            (
                NXOpen::Point * point /** New location of object in ABS coordinates */
            ) = 0;
        };
    }
}
#undef EXPORTLIBRARY
#endif
