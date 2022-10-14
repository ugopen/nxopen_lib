#ifndef NXOpen_MOTION_MARKERBUILDER_HXX_INCLUDED
#define NXOpen_MOTION_MARKERBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Motion_MarkerBuilder.ja
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
#include <NXOpen/Builder.hxx>
#include <NXOpen/Motion_MarkerBuilder.hxx>
#include <NXOpen/SelectObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Motion
    {
        class MarkerBuilder;
    }
    class Builder;
    class CoordinateSystem;
    class Point;
    class SelectNXObject;
    namespace Motion
    {
        class _MarkerBuilderBuilder;
        /** Represents a builder of Marker  <br> To create a new instance of this class, use @link Motion::MarkerCollection::CreateMarkerBuilder Motion::MarkerCollection::CreateMarkerBuilder@endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        DisplayScale </td> <td> 
         
        1 </td> </tr> 

        </table>  
        */
        class NXOPENCPPEXPORT MarkerBuilder : public Builder
        {
            private: friend class  _MarkerBuilderBuilder;
            protected: MarkerBuilder();
            /**Returns  the select link  <br> License requirements : None */
            public: NXOpen::SelectNXObject * SelectLink
            (
            );
            /**Returns  the origin point  <br> License requirements : None */
            public: NXOpen::Point * OriginPoint
            (
            );
            /**Sets  the origin point  <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetOriginPoint
            (
                NXOpen::Point * originPoint /** originpoint */ 
            );
            /**Returns  the csys  <br> License requirements : None */
            public: NXOpen::CoordinateSystem * Csys
            (
            );
            /**Sets  the csys  <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetCsys
            (
                NXOpen::CoordinateSystem * csys /** csys */ 
            );
            /**Returns  the display scale  <br> License requirements : None */
            public: double DisplayScale
            (
            );
            /**Sets  the display scale  <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetDisplayScale
            (
                double displayScale /** displayscale */ 
            );
            /**Returns  the name  <br> License requirements : None */
            public: NXString Name
            (
            );
            /**Sets  the name  <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetName
            (
                const NXString & name /** name */ 
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif