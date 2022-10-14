#ifndef NXOpen_ROUTING_OVERSTOCKAPPLICATION_HXX_INCLUDED
#define NXOpen_ROUTING_OVERSTOCKAPPLICATION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Routing_OverstockApplication.ja
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
#include <NXOpen/NXObject.hxx>
#include <NXOpen/Routing_OverstockApplicationCollection.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Routing
    {
        class OverstockApplication;
    }
    class Curve;
    class NXObject;
    class Point;
    namespace Routing
    {
        class ControlPoint;
    }
    namespace Routing
    {
        class ISegment;
    }
    namespace Routing
    {
        class Overstock;
    }
    namespace Routing
    {
        class Stock;
    }
    namespace Routing
    {
        class _OverstockApplicationBuilder;
        /** Represents a collection of @link Routing::OverstockApplication Routing::OverstockApplication@endlink  objects. */
        class NXOPENCPPEXPORT OverstockApplication : public NXObject
        {
            private: friend class  _OverstockApplicationBuilder;
            protected: OverstockApplication();
            /**  Returns the set of segments over which the overstock is applied.  @return  the contiguous set of segments this overstock
                                                                                          application is covering.   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: std::vector<NXOpen::Routing::ISegment *> GetSegments
            (
            );
            /**Returns   the start control point of the path over which the overstock is applied.  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: NXOpen::Routing::ControlPoint * StartOfPath
            (
            );
            /**Returns   the method used to define the overstock application.  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: NXOpen::Routing::Method Definition
            (
            );
            /**Returns   the start point of overstock on the path.  Used in
                         Interval, Point to Point, and Point and Length definition
                         methods.  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: NXOpen::Point * StartPointOfOverstock
            (
            );
            /**Returns   the end point of overstock on the path.  Used in the Point to Point definition method.  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: NXOpen::Point * EndPointOfOverstock
            (
            );
            /**Returns   the mid point of overstock on the path.  Used in Point and Length definition
                         method.  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: NXOpen::Point * MidPointOfOverstock
            (
            );
            /** Gets the cross sections controlled by this object.  These
                     * cross sections could be used for a custom bundling algorithm.   @return  Cross sections.   <br> License requirements : routing_mechanical ("Routing Mechanical") OR routing_electrical ("Routing Electrical") OR routing_combined ("Routing Combined") */
            public: std::vector<NXOpen::Curve *> GetCrossSections
            (
            );
            /** Gets the @link Routing::Stock Routing::Stock@endlink  and
                     * @link Routing::OverstockApplication Routing::OverstockApplication@endlink  that this
                     * @link Routing::OverstockApplication Routing::OverstockApplication@endlink  covers.  @return  Covered stocks.   <br> License requirements : routing_mechanical ("Routing Mechanical") OR routing_electrical ("Routing Electrical") OR routing_combined ("Routing Combined") */
            public: std::vector<NXOpen::Routing::Stock *> GetCoveredStocks
            (
            );
            /** Sets the @link Routing::Stock Routing::Stock@endlink  and
                     * @link Routing::OverstockApplication Routing::OverstockApplication@endlink  that this
                     * @link Routing::OverstockApplication Routing::OverstockApplication@endlink  covers.  <br> License requirements : routing_mechanical ("Routing Mechanical") OR routing_electrical ("Routing Electrical") OR routing_combined ("Routing Combined") */
            public: void SetCoveredStocks
            (
                const std::vector<NXOpen::Routing::Stock *> & coveredStocks /** Stocks to cover */
            );
            /** Returns @link Routing::Overstock Routing::Overstock@endlink  objects covering this @link Routing::OverstockApplication Routing::OverstockApplication@endlink .  @return   <br> License requirements : routing_mechanical ("Routing Mechanical") OR routing_electrical ("Routing Electrical") OR routing_combined ("Routing Combined") */
            public: std::vector<NXOpen::Routing::Overstock *> GetOverstocks
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif