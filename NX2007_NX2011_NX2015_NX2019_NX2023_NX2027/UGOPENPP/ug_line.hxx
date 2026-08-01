/*
================================================================================

          Copyright (c) 1998-2000 Unigraphics Solutions Inc.
                    Unpublished - All rights reserved

================================================================================
  File description:

    Header file for Geometric NX Line C++ class definitions.

================================================================================

*/

#ifndef UG_LINE_INCLUDED
#define UG_LINE_INCLUDED

// ****************************************************************************
// Include files for base classes and other needed types
// ****************************************************************************

#include <ug_curve.hxx>
#include <line.hxx>
#include <ug_session.hxx>
#include <ug_part.hxx>
#include <ug_vector.hxx>
#include <libopenpp_exports.hxx>

// ****************************************************************************
// Forward declarations for classes
// ****************************************************************************

class Point3;
class UgAssemblyNode;

// This class defines the interface for the creation and manipulation of
// NX line objects.
class OPENPPEXPORT UgLine : public UgCurveObject,
                            public Line
{

    UG_DECLARE_INTERNAL_CLASS ( UgLine )

    public:

        // Create a UgLine object by specifying two points.
        static UgLine *create 
        ( 
            const Point3    &start_point,   // <I>
                                            // The start point in Absolute Coordinate
                                            // System coordinates of the line
            const Point3    &end_point,     // <I>
                                            // The end point in Absolute Coordinate
                                            // System coordinates of the line
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

        // Edit the start point of the invoking object
        void setStartPoint
        (
            const Point3    &start_point    // <I>
                                            // The new start point in Absolute Coordinate
                                            // System coordinates of the line
        );

        // Edit the end point of the invoking object
        void setEndPoint
        (
            const Point3    &end_point      // <I>
                                            // The new end point in Absolute Coordinate
                                            // System coordinates of the line
        );

        // Return the prototype object of the invoking object if the invoking object
        // is an occurrence.  Return the invoking object if the invoking object is 
        // not an occurrence
        // 
        UgLine *askPrototype ( ) const;

        // Return the occurrence object that corresponds to the invoking prototype
        // object and is owned by the given UgAssemblyNode object. Return 0 if the
        // invoking object is not a prototype object, or if the occurrence object can
        // not be found.
        // 
        UgLine *askOccurrence 
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
        const std::vector < UgLine * > askAllOccurrences ( ) const;

    protected:

        // Initialize a UgLine object by actually creating an NX database line
        // by specifying two points.
        void initialize
        ( 
            const Point3    &start_point,   // <I>
                                            // The start point in Absolute Coordinate
                                            // System coordinates of the line
            const Point3    &end_point,     // <I>
                                            // The end point in Absolute Coordinate
                                            // System coordinates of the line
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
        
        // Construct a UgLine object
        UgLine
        (
            tag_t tag = NULL_TAG            // The tag of the NX database line that the
                                            // UgLine object corresponds to.
        );

        // Destroy a UgLine object
        virtual ~UgLine ( );

    public:

        // Return the Curve object that represents the invoking object.
        // 
        const Curve *askCurve ( ) const;

    protected:

        // Return the UgEvaluatableObject object that represents the invoking object.
        // 
        const UgEvaluatableObject *askEvaluatableObject ( ) const;

    private:

        // Edit all of the line data of the invoking object via an Open API struct.
        void setLineDefinition
        (
            const UF_EVAL_line_t &line      // <I>
                                            // The Open API struct that specifies
                                            // all of the line data.
        );

};

#undef EXPORTLIBRARY

#endif  // UG_LINE_INCLUDED
