/*
================================================================================

          Copyright (c) 1998-2000 Unigraphics Solutions Inc.
                    Unpublished - All rights reserved

================================================================================
  File description:

    Header file for Geometric NX Parabola C++ class definitions.

================================================================================

*/

#ifndef UG_PARABOLA_INCLUDED
#define UG_PARABOLA_INCLUDED

// ****************************************************************************
// Include files for base classes and other needed types
// ****************************************************************************

#include <ug_session.hxx>
#include <ug_conic.hxx>
#include <ug_part.hxx>
#include <ug_vector.hxx>

#include <parabola.hxx>
#include <libopenpp_exports.hxx>

// ****************************************************************************
// Forward declarations for classes
// ****************************************************************************

class CoordSys;
class Matrix3;
class Point3;
class UgAssemblyNode;

// This class defines the interface for the creation and manipulation of
// NX parabola objects.
class OPENPPEXPORT UgParabola : public UgConicObject,
                                     public Parabola
{

    UG_DECLARE_INTERNAL_CLASS ( UgParabola )

    public:
        
        // Create a UgParabola object by specifying the minimum y value, maximum y value,
        // center, focal length, and matrix.
        static UgParabola *create
        ( 
            double           focal_length,  // <I>
                                            // The focal length of the parabola
            double           minimum_y,     // <I>
                                            // The minimum y value of the parabola
            double           maximum_y,     // <I>
                                            // The maximum y value of the parabola
            const CoordSys  &csys,          // <I>
                                            // The coordinate system of the parabola.  The
                                            // origin of the coordinate system defines
                                            // the center of the parabola in Absolute
                                            // Coordinate System coordinates, and the matrix
                                            // of the coordinate system defines the
                                            // orientation of the parabola in Absolute
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

        // Edit the focal length of the invoking object.
        void setFocalLength
        (
            double           focal_length   // <I>
                                            // The new focal length of the parabola
        );

        // Edit the minimum y value of the invoking object
        void setMinimumY
        (
            double           minimum_y      // <I>
                                            // The new minimum y value of the parabola
        );

        // Edit the maximum y value of the invoking object
        void setMaximumY
        (
            double           maximum_y      // <I>
                                            // The new maximum y value of the parabola
        );

        // Edit the center point of the invoking object
        void setCenterPoint
        (
            const Point3    &center_point   // <I>
                                            // The new center point ( in Absolute
                                            // Coordinate System coordinates )
                                            // of the parabola
        );

        // Return the prototype object of the invoking object if the invoking object
        // is an occurrence.  Return the invoking object if the invoking object is 
        // not an occurrence
        UgParabola *askPrototype ( ) const;

        // Return the occurrence object that corresponds to the invoking prototype
        // object and is owned by the given UgAssemblyNode object. Return 0 if the
        // invoking object is not a prototype object, or if the occurrence object can
        // not be found.
        UgParabola *askOccurrence 
        (
             const UgAssemblyNode *node  // <I> 
                                         // The owning object of the returned occurrence
                                         // object.
        ) const;

        // Return a std::vector object that contains all of the occurrences of the
        // invoking prototype object in all of the UgAssemblyNode objects in the
        // session.  Return a zero-length std::vector if the invoking object is not a
        // prototype object, or if the invoking object has no occurrences.
        const std::vector < UgParabola * > askAllOccurrences ( ) const;
         
    protected:

        // Initialize a UgParabola object by actually creating an NX database parabola
        // by specifying the minimum y value, maximum y value, center, focal length,
        // and matrix.
        void initialize 
        ( 
            double           focal_length,  // <I>
                                            // The focal length of the parabola
            double           minimum_y,     // <I>
                                            // The minimum y value of the parabola
            double           maximum_y,     // <I>
                                            // The maximum y value of the parabola
            const CoordSys  &csys,          // <I>
                                            // The coordinate system of the parabola.  The
                                            // origin of the coordinate system defines
                                            // the center of the parabola in Absolute
                                            // Coordinate System coordinates, and the matrix
                                            // of the coordinate system defines the
                                            // orientation of the parabola in Absolute
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

        // Construct a UgParabola object
        UgParabola
        (
            tag_t tag = NULL_TAG            // The tag of the NX database parabola that the
                                            // UgParabola object corresponds to.
        );

        // Destroy a UgParabola object
        virtual ~UgParabola ( );

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

        // Edit all of the parabola data of the invoking object via an Open API struct.
        void setParabolaDefinition
        (
            const UF_EVAL_parabola_t &parabola  // <I>
                                                // The Open API struct that specifies
                                                // all of the parabola data.
        );

};

#undef EXPORTLIBRARY

#endif  // UG_PARABOLA_INCLUDED
