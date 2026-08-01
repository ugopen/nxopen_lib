/*
================================================================================

          Copyright (c) 1998-2000 Unigraphics Solutions Inc.
                    Unpublished - All rights reserved

================================================================================
  File description:

    Header file for Geometric NX Point C++ class definitions.

================================================================================

*/

#ifndef UG_POINT_INCLUDED
#define UG_POINT_INCLUDED

// ****************************************************************************
// Include files for base classes and other needed types
// ****************************************************************************

#include <ug_displayable.hxx>
#include <ug_session.hxx>
#include <ug_smart.hxx>
#include <ug_part.hxx>
#include <ug_vector.hxx>
#include <libopenpp_exports.hxx>

// ****************************************************************************
// Forward declarations for classes
// ****************************************************************************

class Point3;
class UgAssemblyNode;

// This class defines the interface for the creation and manipulation of
// NX point objects.
class OPENPPEXPORT UgPoint : public UgDisplayableObject,
                                  public UgDisplayableSmartObject
{

    UG_DECLARE_INTERNAL_CLASS ( UgPoint )

    public:

        // Create a UgPoint object at the specified point location.
        static UgPoint *create 
        ( 
            const Point3    &point,         // <I>
                                            // The point location in Absolute
                                            // Coordinate System coordinates of the point
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

        // Return the point location in Absolute Coordinate System coordinates of the
        // invoking object.
        const Point3 getPoint ( ) const;

        // Edit the point location of the invoking object
        void setPoint
        (
            const Point3    &point          // <I>
                                            // The new point location in Absolute
                                            // Coordinate System coordinates of the point
        );

        // Return the prototype object of the invoking object if the invoking object
        // is an occurrence.  Return the invoking object if the invoking object is 
        // not an occurrence
        // 
        UgPoint *askPrototype ( ) const;

        // Return the occurrence object that corresponds to the invoking prototype
        // object and is owned by the given UgAssemblyNode object. Return 0 if the
        // invoking object is not a prototype object, or if the occurrence object can
        // not be found.
        // 
        UgPoint *askOccurrence 
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
        const std::vector < UgPoint * > askAllOccurrences ( ) const;

    protected:

        // Initialize a UgPoint object by actually creating an NX database point
        // at the specified point location.
        void initialize
        ( 
            const Point3    &point,         // <I>
                                            // The point location in Absolute
                                            // Coordinate System coordinates of the point
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

        // Construct a UgPoint object
        UgPoint
        (
            tag_t tag = NULL_TAG            // The tag of the NX database point that the
                                            // UgPoint object corresponds to.
        );

        // Destroy a UgPoint object
        virtual ~UgPoint ( );

};

#undef EXPORTLIBRARY

#endif  // UG_POINT_INCLUDED
