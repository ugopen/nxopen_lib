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
             
         <br>  Created in NX4.0.0.  <br>  
        */
        class NXOPENCPP_ROUTINGEXPORT  IRoutePosition : public virtual NXOpen::Routing::ICharacteristic
        {
            public: virtual ~IRoutePosition() {}
            /**Returns   the current location of the object in ABS coordinates.  This value is
                          overridden by the coordinates of the point associated with this object. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: virtual NXOpen::Point3d Position
            (
            ) = 0;
            /**Sets   the current location of the object in ABS coordinates.  This value is
                          overridden by the coordinates of the point associated with this object. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: virtual void SetPosition
            (
                const NXOpen::Point3d & position /** New location of object in ABS coordinates */
            ) = 0;
            /**Returns  the @link NXOpen::Point NXOpen::Point@endlink  that specifies the location of the
                        @link NXOpen::Routing::IRoutePosition NXOpen::Routing::IRoutePosition@endlink  object.  A NULL object indicates that this
                        object is not associated to any point.  
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: virtual NXOpen::Point * Point
            (
            ) = 0;
            /**Sets  the @link NXOpen::Point NXOpen::Point@endlink  that specifies the location of the
                        @link NXOpen::Routing::IRoutePosition NXOpen::Routing::IRoutePosition@endlink  object.  A NULL object indicates that this
                        object is not associated to any point.  
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: virtual void SetPoint
            (
                NXOpen::Point * point /** New location of object in ABS coordinates */
            ) = 0;
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
