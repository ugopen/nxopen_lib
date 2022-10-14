/*
================================================================================

          Copyright (c) 1998-2000 Unigraphics Solutions Inc.
                    Unpublished - All rights reserved

================================================================================
  File description:
    
    Header file for Geometric NX Arc C++ class definitions.

================================================================================

*/

#ifndef UG_ARC_INCLUDED
#define UG_ARC_INCLUDED

// ****************************************************************************
// Include files for base classes and other needed types
// ****************************************************************************

#include <ug_session.hxx>
#include <ug_conic.hxx>
#include <ug_part.hxx>

#include <arc.hxx>
#include <libopenpp_exports.hxx>

// ****************************************************************************
// Forward declarations for classes
// ****************************************************************************

class CoordSys;
class Matrix3;
class Point3;
class UgAssemblyNode;

// This class defines the interface for the creation and manipulation of
// NX arc objects.
class OPENPPEXPORT UgArc : public UgConicObject,
                                public Arc
{

    UG_DECLARE_INTERNAL_CLASS ( UgArc )

    public:

        // Create a UgArc object by specifying the start angle, end angle,
        // center, radius, and matrix.
        static UgArc *create 
        ( 
            double           radius,        // <I>
                                            // The radius of the arc
            double           start_angle,   // <I>
                                            // The start angle ( in radians )
                                            // of the arc
            double           end_angle,     // <I>
                                            // The end angle ( in radians )
                                            // of the arc
            const CoordSys  &csys,          // <I>
                                            // The coordinate system of the arc.  The
                                            // origin of the coordinate system defines
                                            // the center of the arc in Absolute
                                            // Coordinate System coordinates, and the matrix
                                            // of the coordinate system defines the
                                            // orientation of the arc in Absolute
                                            // Coordinate System coordinates.
            const UgObject  *part_or_object = UgSession::getWorkPart ( )
                                            // <I>
                                            // This argument defines the owning part of
                                            // the new object.  If the argument is a
                                            // UgPart object, the argument is the owning
                                            // part of the new object.  If the argument
                                            // is not a UgPart object, the part that owns
                                            // the argument is the owning part of the new
                                            // object.
        );

        // Create a UgArc object by specifying three points to define the arc.
        // The object created will either be a full circle that passes through
        // the given points, or an arc that starts at the first point, passes
        // through the second point, and ends at the third point.
        static UgArc *create 
        (
            bool             create_circle, // <I>
                                            // If true, a full circle will be created.
                                            // If false, an arc will be created.
            const Point3    &point1,        // <I>
                                            // The first point in Absolute Coordinate
                                            // System coordinates.
            const Point3    &point2,        // <I>
                                            // The second point in Absolute Coordinate
                                            // System coordinates.
            const Point3    &point3,        // <I>
                                            // The third point in Absolute Coordinate
                                            // System coordinates.
            const UgObject  *part_or_object = UgSession::getWorkPart ( )
                                            // <I>
                                            // This argument defines the owning part of
                                            // the new object.  If the argument is a
                                            // UgPart object, the argument is the owning
                                            // part of the new object.  If the argument
                                            // is not a UgPart object, the part that owns
                                            // the argument is the owning part of the new
                                            // object.
        );

        // Return the orientation matrix of the invoking object.
        const Matrix3 getMatrix ( ) const;

        // Edit the radius of the invoking object.
        void setRadius
        (
            double           radius         // <I>
                                            // The new radius of the arc
        );

        // Edit the start angle of the invoking object
        void setStartAngle
        (
            double           start_angle    // <I>
                                            // The new start angle ( in radians )
                                            // of the arc
        );

        // Edit the end angle of the invoking object.
        void setEndAngle
        (
            double           end_angle      // <I>
                                            // The new end angle ( in radians )
                                            // of the arc
        );

        // Edit the center point of the invoking object
        void setCenterPoint
        (
            const Point3    &center_point   // <I>
                                            // The new center point ( in Absolute
                                            // Coordinate System coordinates )
                                            // of the arc
        );

        // Return the prototype object of the invoking object if the invoking object
        // is an occurrence.  Return the invoking object if the invoking object is 
        // not an occurrence
        // 
        UgArc *askPrototype ( ) const;

        // Return the occurrence object that corresponds to the invoking prototype
        // object and is owned by the given UgAssemblyNode object. Return 0 if the
        // invoking object is not a prototype object, or if the occurrence object can
        // not be found.
        // 
        UgArc *askOccurrence 
        (
             const UgAssemblyNode *node  // <I> 
                                         // The owning object of the returned occurrence
                                         // object.
        ) const;

        // Return a std::vector object that contains all of the occurrences of the
        // invoking prototype object in all of the UgAssemblyNode objects in the
        // session.  Return a zero-length std::vector if the invoking object is not a
        // prototype object, or if the invoking object has no occurrences.
        // 
        const std::vector < UgArc * > askAllOccurrences ( ) const;
         
    protected:

        // Initialize a UgArc object by actually creating an NX database arc
        // by specifying the start angle, end angle, center, radius, and matrix.
        void initialize 
        (
            double           radius,        // <I>
                                            // The radius of the arc
            double           start_angle,   // <I>
                                            // The start angle ( in radians )
                                            // of the arc
            double           end_angle,     // <I>
                                            // The end angle ( in radians )
                                            // of the arc
            const CoordSys  &csys,          // <I>
                                            // The coordinate system of the arc.  The
                                            // origin of the coordinate system defines
                                            // the center of the arc in Absolute
                                            // Coordinate System coordinates, and the matrix
                                            // of the coordinate system defines the
                                            // orientation of the arc in Absolute
                                            // Coordinate System coordinates.
            const UgObject  *part_or_object = UgSession::getWorkPart ( )
                                            // <I>
                                            // This argument defines the owning part of
                                            // the new object.  If the argument is a
                                            // UgPart object, the argument is the owning
                                            // part of the new object.  If the argument
                                            // is not a UgPart object, the part that owns
                                            // the argument is the owning part of the new
                                            // object.
        );

        // Initialize a UgArc object by actually creating an NX database arc
        // by specifying three points to define the arc.
        // The object created will either be a full circle that passes through
        // the given points, or an arc that starts at the first point, passes
        // through the second point, and ends at the third point.
        void initialize 
        (
            bool             create_circle, // <I>
                                            // If true, a full circle will be created.
                                            // If false, an arc will be created.
            const Point3    &point1,        // <I>
                                            // The first point in Absolute Coordinate
                                            // System coordinates.
            const Point3    &point2,        // <I>
                                            // The second point in Absolute Coordinate
                                            // System coordinates.
            const Point3    &point3,        // <I>
                                            // The third point in Absolute Coordinate
                                            // System coordinates.
            const UgObject  *part_or_object = UgSession::getWorkPart ( )
                                            // <I>
                                            // This argument defines the owning part of
                                            // the new object.  If the argument is a
                                            // UgPart object, the argument is the owning
                                            // part of the new object.  If the argument
                                            // is not a UgPart object, the part that owns
                                            // the argument is the owning part of the new
                                            // object.
        );

        // Construct a UgArc object
        UgArc
        (
            tag_t tag = NULL_TAG            // The tag of the NX database arc that the
                                            // UgArc object corresponds to.
        );

        // Destroy a UgArc object
        virtual ~UgArc ( );

    public:

        // Return the Curve object that represents the invoking object.
        // 
        const Curve *askCurve ( ) const;

    protected:

        // Return the UgEvaluatableObject object that represents the invoking object.
        // 
        const UgEvaluatableObject *askEvaluatableObject ( ) const;

    private:

        // Edit all of the arc data of the invoking object via an Open API struct.
        void setArcDefinition
        (
            const UF_EVAL_arc_t   &arc      // <I>
                                            // The Open API struct that specifies
                                            // all of the arc data.
        );

};

#undef EXPORTLIBRARY

#endif  // UG_ARC_INCLUDED
