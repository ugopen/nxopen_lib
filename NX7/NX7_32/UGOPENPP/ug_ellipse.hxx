/*
================================================================================

          Copyright (c) 1998-2000 Unigraphics Solutions Inc.
                    Unpublished - All rights reserved

================================================================================
  File description:

    Header file for Geometric NX Ellipse C++ class definitions.

================================================================================

*/

#ifndef UG_ELLIPSE_INCLUDED
#define UG_ELLIPSE_INCLUDED

// ****************************************************************************
// Include files for base classes and other needed types
// ****************************************************************************

#include <ug_session.hxx>
#include <ug_conic.hxx>
#include <ug_part.hxx>
#include <ug_vector.hxx>

#include <ellipse.hxx>
#include <libopenpp_exports.hxx>

// ****************************************************************************
// Forward declarations for classes
// ****************************************************************************

class CoordSys;
class Matrix3;
class Point3;
class UgAssemblyNode;

// This class defines the interface for the creation and manipulation of
// NX ellipse objects.
class OPENPPEXPORT UgEllipse : public UgConicObject,
                                    public Ellipse
{

    UG_DECLARE_INTERNAL_CLASS ( UgEllipse )

    public:

        // Create a UgEllipse object by specifying the start angle, end angle,
        // center, radii, and matrix.
        static UgEllipse *create 
        (
            double           major_radius,  // <I>
                                            // The major radius of the ellipse
            double           minor_radius,  // <I>
                                            // The minor radius of the ellipse
            double           start_angle,   // <I>
                                            // The start angle ( in radians )
                                            // of the ellipse
            double           end_angle,     // <I>
                                            // The end angle ( in radians )
                                            // of the ellipse
            const CoordSys  &csys,          // <I>
                                            // The coordinate system of the ellipse.  The
                                            // origin of the coordinate system defines
                                            // the center of the ellipse in Absolute
                                            // Coordinate System coordinates, and the matrix
                                            // of the coordinate system defines the
                                            // orientation of the ellipse in Absolute
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
                
        // Return the orientation matrix of the invoking object.
        const Matrix3 getMatrix ( ) const;

        // Edit the major radius of the invoking object.
        void setMajorRadius
        (
            double           major_radius   // <I>
                                            // The new major radius of the ellipse
        );

        // Edit the minor radius of the invoking object.
        void setMinorRadius
        (
            double           minor_radius   // <I>
                                            // The new minor radius of the ellipse
        );

        // Edit the start angle of the invoking object
        void setStartAngle
        (
            double           start_angle    // <I>
                                            // The new start angle ( in radians )
                                            // of the ellipse
        );

        // Edit the end angle of the invoking object.
        void setEndAngle
        (
            double           end_angle      // <I>
                                            // The new end angle ( in radians )
                                            // of the ellipse
        );

        // Edit the center point of the invoking object
        void setCenterPoint
        (
            const Point3    &center_point   // <I>
                                            // The new center point ( in Absolute
                                            // Coordinate System coordinates )
                                            // of the ellipse
        );

        // Return the prototype object of the invoking object if the invoking object
        // is an occurrence.  Return the invoking object if the invoking object is 
        // not an occurrence
        UgEllipse *askPrototype ( ) const;

        // Return the occurrence object that corresponds to the invoking prototype
        // object and is owned by the given UgAssemblyNode object. Return 0 if the
        // invoking object is not a prototype object, or if the occurrence object can
        // not be found.
        UgEllipse *askOccurrence 
        (
             const UgAssemblyNode *node  // <I> 
                                         // The owning object of the returned occurrence
                                         // object.
        ) const;

        // Return a std::vector object that contains all of the occurrences of the
        // invoking prototype object in all of the UgAssemblyNode objects in the
        // session.  Return a zero-length std::vector if the invoking object is not a
        // prototype object, or if the invoking object has no occurrences.
        const std::vector < UgEllipse * > askAllOccurrences ( ) const;
                
    protected:

        // Initialize a UgEllipse object by actually creating an NX database ellipse
        // by specifying the start angle, end angle, center, radii, and matrix.
        void initialize
        (
            double           major_radius,  // <I>
                                            // The major radius of the ellipse
            double           minor_radius,  // <I>
                                            // The minor radius of the ellipse
            double           start_angle,   // <I>
                                            // The start angle ( in radians )
                                            // of the ellipse
            double           end_angle,     // <I>
                                            // The end angle ( in radians )
                                            // of the ellipse
            const CoordSys  &csys,          // <I>
                                            // The coordinate system of the ellipse.  The
                                            // origin of the coordinate system defines
                                            // the center of the ellipse in Absolute
                                            // Coordinate System coordinates, and the matrix
                                            // of the coordinate system defines the
                                            // orientation of the ellipse in Absolute
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

        // Construct a UgEllipse object
        UgEllipse
        (
            tag_t tag = NULL_TAG            // The tag of the NX database ellipse that the
                                            // UgEllipse object corresponds to.
        );

        // Destroy a UgEllipse object
        virtual ~UgEllipse ( );

    private:

        // Return the Curve object that represents the invoking object.
        // This method is provided to satisfy the pure virtual method
        // defined in the class UgEvaluatableObject.  It isn't needed by
        // direct users of this class because all of the methods that class
        // Curve provides are directly accessible via the indirect inheritance of
        // this class from the Curve class.  Hence, the scope of this method
        // is private in this class.  This method does enable polymorphic access
        // to objects of this class in the event that a UgEvaluatableObject
        // array containing edges as well as curves is encountered.
        const Curve *askCurve ( ) const;

        // Return the UgEvaluatableObject object that represents the invoking
        // object.  This method is provided to satisfy the pure virtual method
        // defined in the class Curve.  It isn't needed by direct users of this
        // this class because all the methods that class UgEvaluatableObject
        // provides are directly accessible via the inheritance of this class
        // from the UgEvaluatableObject class.  Hence, the scope of this method
        // is private in this class.  This method does enable polymorphic access
        // to objects of this class in the event that a Curve array containing
        // edges as well as curves is encountered.
        const UgEvaluatableObject *askEvaluatableObject ( ) const;

        // Edit all of the ellipse data of the invoking object via an Open API struct.
        void setEllipseDefinition
        (
            const UF_EVAL_ellipse_t &ellipse    // <I>
                                                // The Open API struct that specifies
                                                // all of the ellipse data.
        );

};

#undef EXPORTLIBRARY

#endif  // UG_ELLIPSE_INCLUDED
