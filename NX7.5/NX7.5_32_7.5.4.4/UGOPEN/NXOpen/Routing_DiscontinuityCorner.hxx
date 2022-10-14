#ifndef NXOpen_ROUTING_DISCONTINUITYCORNER_HXX_INCLUDED
#define NXOpen_ROUTING_DISCONTINUITYCORNER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Routing_DiscontinuityCorner.ja
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
#include <NXOpen/Routing_Corner.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Routing
    {
        class DiscontinuityCorner;
    }
    namespace Routing
    {
        class Corner;
    }
    namespace Routing
    {
        class ISegment;
    }
    namespace Routing
    {
        class _DiscontinuityCornerBuilder;
        class DiscontinuityCornerImpl;
        /** 
                A discontinuity corner is a corner that forces @link Routing::Stock Routing::Stock@endlink  objects
                to split as they cover the segments attached to the discontinuity corner.  
                The discontinuity specifies over which two segments (at a junction of 2 or more segments)
                that the break should occur.
              <br> To create a new instance of this class, use @link Routing::DiscontinuityCornerCollection::Create Routing::DiscontinuityCornerCollection::Create@endlink  <br> */
        class NXOPENCPPEXPORT  DiscontinuityCorner : public Routing::Corner
        {
            private: DiscontinuityCornerImpl * m_discontinuitycorner_impl;
            private: friend class  _DiscontinuityCornerBuilder;
            protected: DiscontinuityCorner();
            public: ~DiscontinuityCorner();
            /**Returns  the first segment of a discontinuity corner, segment must be
                     attached to the @link Routing::ControlPoint Routing::ControlPoint@endlink  that
                     defines this corner.   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: NXOpen::Routing::ISegment * FirstSegment
            (
            );
            /**Sets  the first segment of a discontinuity corner, segment must be
                     attached to the @link Routing::ControlPoint Routing::ControlPoint@endlink  that
                     defines this corner.   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: void SetFirstSegment
            (
                NXOpen::Routing::ISegment * segment /** segment */ 
            );
            /**Returns  the second segment of a discontinuity corner, segment must be
                     attached to the @link Routing::ControlPoint Routing::ControlPoint@endlink  that
                     defines this corner.   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: NXOpen::Routing::ISegment * SecondSegment
            (
            );
            /**Sets  the second segment of a discontinuity corner, segment must be
                     attached to the @link Routing::ControlPoint Routing::ControlPoint@endlink  that
                     defines this corner.   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: void SetSecondSegment
            (
                NXOpen::Routing::ISegment * segment /** segment */ 
            );
            /** Removes (deletes) the input discontinuity corner. <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: void Remove
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif