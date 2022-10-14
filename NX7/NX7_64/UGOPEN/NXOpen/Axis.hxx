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
#include <NXOpen/Callback.hxx>
#include <NXOpen/SmartObject.hxx>
#include <NXOpen/ugmath.hxx>
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
        /** Defines types of axes based on their associativity */
        public: enum Types
        {
            TypesNonAssociative/** non-associative */,
            TypesPointAndDirection/** the axis is defined by a @link Point Point@endlink  and @link Direction Direction@endlink  */,
            TypesOther/** the type is not one of the other enumerated types */
        };

        private: friend class  _AxisBuilder;
        protected: Axis();
        /**Returns  the associativity type for the axis  <br> License requirements : None */
        public: NXOpen::Axis::Types Type
        (
        );
        /**Sets  the point that defines the origin of the axis for an axis with type 
                @link Axis::TypesPointAndDirection Axis::TypesPointAndDirection@endlink .
                An exception is thrown if the axis type is not @link Axis::TypesPointAndDirection Axis::TypesPointAndDirection@endlink , 
                If the axis type is point and direction and the point is not specified,
                the point is inferred from the direction.
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: void SetPoint
        (
            NXOpen::Point * point /** point */ 
        );
        /**Sets  the direction that the axis points for an axis with type 
            @link Axis::TypesPointAndDirection Axis::TypesPointAndDirection@endlink .
            An exception is thrown if the axis type is not @link Axis::TypesPointAndDirection Axis::TypesPointAndDirection@endlink , 
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: void SetDirection
        (
            NXOpen::Direction * direction /** This parameter may not be NULL.*/
        );
        /**Returns  the point that defines the origin of the axis for an axis with type 
                @link Axis::TypesPointAndDirection Axis::TypesPointAndDirection@endlink .
                An exception is thrown if the axis type is not @link Axis::TypesPointAndDirection Axis::TypesPointAndDirection@endlink , 
                If the axis type is point and direction and the point is not specified,
                the point is inferred from the direction.
             <br> License requirements : None */
        public: NXOpen::Point * Point
        (
        );
        /**Returns  the direction that the axis points for an axis with type 
            @link Axis::TypesPointAndDirection Axis::TypesPointAndDirection@endlink .
            An exception is thrown if the axis type is not @link Axis::TypesPointAndDirection Axis::TypesPointAndDirection@endlink , 
             <br> License requirements : None */
        public: NXOpen::Direction * Direction
        (
        );
        /**Returns  the origin
             <br> License requirements : None */
        public: NXOpen::Point3d Origin
        (
        );
        /** Sets the origin for a non-associative axis.  This method does nothing if the
            axis is associative  <br> License requirements : None */
        public: void SetOrigin
        (
            const NXOpen::Point3d & origin /** origin */ 
        );
        /**Returns  the direction vector
             <br> License requirements : None */
        public: NXOpen::Vector3d DirectionVector
        (
        );
        /** Sets the direction vector for a non-associative axis.  This method does nothing if the
            axis is associative  <br> License requirements : None */
        public: void SetDirectionVector
        (
            const NXOpen::Vector3d & vector /** vector */ 
        );
    };
}
#undef EXPORTLIBRARY
#endif