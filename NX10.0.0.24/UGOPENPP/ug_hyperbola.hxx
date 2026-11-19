/*
================================================================================

          Copyright (c) 1998-2000 Unigraphics Solutions Inc.
                    Unpublished - All rights reserved

================================================================================
  File description:

    Header file for Geometric NX Hyperbola C++ class definitions.

================================================================================

*/

#ifndef UG_HYPERBOLA_INCLUDED
#define UG_HYPERBOLA_INCLUDED

// ****************************************************************************
// Include files for base classes and other needed types
// ****************************************************************************

#include <ug_session.hxx>
#include <ug_conic.hxx>
#include <ug_part.hxx>
#include <ug_vector.hxx>

#include <hyperbola.hxx>
#include <libopenpp_exports.hxx>


// ****************************************************************************
// Forward declarations for classes
// ****************************************************************************

class CoordSys;
class Matrix3;
class Point3;
class UgAssemblyNode;

// This class defines the interface for the creation and manipulation of
// NX hyperbola objects.
class OPENPPEXPORT UgHyperbola : public UgConicObject,
                                      public Hyperbola
{

    UG_DECLARE_INTERNAL_CLASS ( UgHyperbola )

    public:

        // Create a UgHyperbola object by specifying the minimum y value, maximum y value,
        // center, semi transverse length, semi conjugate length, and matrix.
        static UgHyperbola *create
        ( 
            double           transverse,    // <I>
                                            // The semi transverse length of the hyperbola
            double           conjugate,     // <I>
                                            // The semi conjugate length of the hyperbola
            double           minimum_y,     // <I>
                                            // The minimum y value of the hyperbola
            double           maximum_y,     // <I>
                                            // The maximum y value of the hyperbola
            const CoordSys  &csys,          // <I>
                                            // The coordinate system of the hyperbola.  The
                                            // origin of the coordinate system defines
                                            // the center of the hyperbola in Absolute
                                            // Coordinate System coordinates, and the matrix
                                            // of the coordinate system defines the
                                            // orientation of the hyperbola in Absolute
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
 
        // Edit the length along the semi transverse axis of the invoking object.
        void setSemiTransverseLength
        (
            double           transverse     // <I>
                                            // The new semi transverse length of the hyperbola
        );

        // Edit the length along the semi conjugate axis of the invoking object.
        void setSemiConjugateLength
        (
            double           conjugate      // <I>
                                            // The new semi conjugate length of the hyperbola
        );

        // Edit the minimum y value of the invoking object
        void setMinimumY
        (
            double           minimum_y      // <I>
                                            // The new minimum y value of the hyperbola
        );

        // Edit the maximum y value of the invoking object
        void setMaximumY
        (
            double           maximum_y      // <I>
                                            // The new maximum y value of the hyperbola
        );

        // Edit the center point of the invoking object
        void setCenterPoint
        (
            const Point3    &center_point   // <I>
                                            // The new center point ( in Absolute
                                            // Coordinate System coordinates )
                                            // of the hyperbola        
        );

        // Return the prototype object of the invoking object if the invoking object
        // is an occurrence.  Return the invoking object if the invoking object is 
        // not an occurrence
        // 
        UgHyperbola *askPrototype ( ) const;

        // Return the occurrence object that corresponds to the invoking prototype
        // object and is owned by the given UgAssemblyNode object. Return 0 if the
        // invoking object is not a prototype object, or if the occurrence object can
        // not be found.
        // 
        UgHyperbola *askOccurrence 
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
        const std::vector < UgHyperbola * > askAllOccurrences ( ) const;

    protected:

        // Initialize a UgHyperbola object by actually creating an NX database hyperbola
        // by specifying the minimum y value, maximum y value, center, semi transverse
        // length, semi conjugate length, and matrix.
        void initialize 
        ( 
            double           transverse,    // <I>
                                            // The semi transverse length of the hyperbola
            double           conjugate,     // <I>
                                            // The semi conjugate length of the hyperbola
            double           minimum_y,     // <I>
                                            // The minimum y value of the hyperbola
            double           maximum_y,     // <I>
                                            // The maximum y value of the hyperbola
            const CoordSys  &csys,          // <I>
                                            // The coordinate system of the hyperbola.  The
                                            // origin of the coordinate system defines
                                            // the center of the hyperbola in Absolute
                                            // Coordinate System coordinates, and the matrix
                                            // of the coordinate system defines the
                                            // orientation of the hyperbola in Absolute
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

        // Construct a UgHyperbola object
        UgHyperbola
        (
            tag_t tag = NULL_TAG            // The tag of the NX database hyperbola that the
                                            // UgHyperbola object corresponds to.
        );

        // Destroy a UgHyperbola object
        virtual ~UgHyperbola ( );

    public:

        // Return the Curve object that represents the invoking object.
        // 
        const Curve *askCurve ( ) const;

    protected:

        // Return the UgEvaluatableObject object that represents the invoking object.
        // 
        const UgEvaluatableObject *askEvaluatableObject ( ) const;

    private:

        // Edit all of the hyperbola data of the invoking object via an Open API struct.
        void setHyperbolaDefinition
        (
            const UF_EVAL_hyperbola_t &hyperbola// <I>
                                                // The Open API struct that specifies
                                                // all of the hyperbola data.
        );

};

#undef EXPORTLIBRARY

#endif  // UG_HYPERBOLA_INCLUDED
