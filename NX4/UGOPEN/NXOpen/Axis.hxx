#ifndef NXOpen_AXIS_HXX_INCLUDED
#define NXOpen_AXIS_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Axis.ja
//
//  Generated by:
//     apiwrap
//
//  WARNING:
//    This file is automatically generated - do not edit by hand
//
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/SmartObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    class Axis;
    class Direction;
    class Point;
    class SmartObject;
    class _AxisBuilder;
    /** Represents an @link Axis Axis@endlink  class. 
     <br> To create a new instance of this class, use @link AxisCollection::CreateAxis AxisCollection::CreateAxis@endlink  <br> */
    class NXOPENCPPEXPORT Axis : public SmartObject
    {
        private: friend class  _AxisBuilder;
        protected: Axis();
        /**Sets  the point that defines the origin of the axis. If this is not specified,
                then the point is inferred from the direction.
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: void SetPoint
        (
            NXOpen::Point * point /** */
        );
        /**Sets  the direction that the axis points
        	 <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: void SetDirection
        (
            NXOpen::Direction * direction /** This parameter may not be NULL.*/
        );
        /**Returns  the point that defines the origin of the axis. If this is not specified,
                then the point is inferred from the direction.
             <br> License requirements : None */
        public: NXOpen::Point * Point
        (
        );
        /** <b>Deprecated</b>:<br>
        &nbsp;&nbsp;&nbsp;Use @link Point() Point@endlink instead.
        @deprecated
        */
        public: NXOpen::Point * GetPoint
        (
        ) { return this->Point(); }
        /**Returns  the direction that the axis points
        	 <br> License requirements : None */
        public: NXOpen::Direction * Direction
        (
        );
        /** <b>Deprecated</b>:<br>
        &nbsp;&nbsp;&nbsp;Use @link Direction() Direction@endlink instead.
        @deprecated
        */
        public: NXOpen::Direction * GetDirection
        (
        ) { return this->Direction(); }
    };
}
#undef EXPORTLIBRARY
#endif
