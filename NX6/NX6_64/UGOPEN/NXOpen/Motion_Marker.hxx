#ifndef NXOpen_MOTION_MARKER_HXX_INCLUDED
#define NXOpen_MOTION_MARKER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Motion_Marker.ja
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
#include <NXOpen/DisplayableObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Motion
    {
        class Marker;
    }
    class DisplayableObject;
    namespace Motion
    {
        class Link;
    }
    class NXMatrix;
    class Point;
    namespace Motion
    {
        class _MarkerBuilder;
        /** Represents the Motion Marker class.  A Marker defines a point with
            orientations to request motion results at, and must be associated
            with a Motion Link. */
        class NXOPENCPPEXPORT Marker : public DisplayableObject
        {
            /** Marker subtype */
            public: enum MarkerType
            {
                MarkerTypeUndefined/** undefined */ ,
                MarkerTypeInertia/** Defines the center of inertia for a link.  
                                                                 It will be automatically created for a link. */,
                MarkerTypeUserDefined/** User created marker. It can be attached to any motion object. */,
                MarkerTypeCenterOfMass/** Defines the center of mass for a link.  
                                                                 It will be automatically created for a link. */
            };

            private: friend class  _MarkerBuilder;
            protected: Marker();
            /**Returns  the @link  Motion::Marker   Motion::Marker @endlink  name. 
             @deprecated Deprecated in NX6 <br> 
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: NXString MarkerName
            (
            );
            /**Sets  the @link  Motion::Marker   Motion::Marker @endlink  name. 
             @deprecated Deprecated in NX6 <br> 
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetMarkerName
            (
                const NXString & name /** name */ 
            );
            /**Returns  the @link  Motion::Marker   Motion::Marker @endlink  subtype that is defined at @link  Motion::Marker::MarkerType   Motion::Marker::MarkerType @endlink . 
             @deprecated Deprecated in NX6 <br> 
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: NXOpen::Motion::Marker::MarkerType Type
            (
            );
            /**Sets  the @link  Motion::Marker   Motion::Marker @endlink  subtype that is defined at @link  Motion::Marker::MarkerType   Motion::Marker::MarkerType @endlink . 
             @deprecated Deprecated in NX6 <br> 
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetType
            (
                NXOpen::Motion::Marker::MarkerType subtype /** subtype */ 
            );
            /**Returns  the @link  Motion::Link   Motion::Link @endlink  attached to @link  Motion::Marker   Motion::Marker @endlink . 
             @deprecated Deprecated in NX6 <br> 
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: NXOpen::Motion::Link * Link
            (
            );
            /**Sets  the @link  Motion::Link   Motion::Link @endlink  attached to @link  Motion::Marker   Motion::Marker @endlink . 
             @deprecated Deprecated in NX6 <br> 
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetLink
            (
                NXOpen::Motion::Link * link /** link */ 
            );
            /**Returns  the @link  Motion::Marker   Motion::Marker @endlink  origin point. 
             @deprecated Deprecated in NX6 <br> 
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: NXOpen::Point * Origin
            (
            );
            /**Sets  the @link  Motion::Marker   Motion::Marker @endlink  origin point. 
             @deprecated Deprecated in NX6 <br> 
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetOrigin
            (
                NXOpen::Point * origin /** origin */ 
            );
            /**Returns  the @link  Motion::Marker   Motion::Marker @endlink  orientation matrix object. 
             @deprecated Deprecated in NX6 <br> 
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: NXOpen::NXMatrix * Orientation
            (
            );
            /**Sets  the @link  Motion::Marker   Motion::Marker @endlink  orientation matrix object. 
             @deprecated Deprecated in NX6 <br> 
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetOrientation
            (
                NXOpen::NXMatrix * orientation /** orientation */ 
            );
            /**Returns  the @link  Motion::Marker   Motion::Marker @endlink  display scale. 
             @deprecated Deprecated in NX6 <br> 
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: double DisplayScale
            (
            );
            /**Sets  the @link  Motion::Marker   Motion::Marker @endlink  display scale. 
             @deprecated Deprecated in NX6 <br> 
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetDisplayScale
            (
                double displayScale /** display scale */ 
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif