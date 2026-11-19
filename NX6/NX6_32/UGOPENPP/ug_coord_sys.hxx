/*
================================================================================

          Copyright (c) 1998-2002 Unigraphics Solutions Inc.
                    Unpublished - All rights reserved

================================================================================
  File description:

    Header file for Coordinate System C++ class definitions.

================================================================================

*/

#ifndef UG_COORD_SYS_INCLUDED
#define UG_COORD_SYS_INCLUDED

// ****************************************************************************
// Include files for base classes and other needed types
// ****************************************************************************

#include <ug_displayable.hxx>
#include <ug_orientable.hxx>
#include <ug_session.hxx>
#include <ug_part.hxx>
#include <ug_vector.hxx>
#include <libopenpp_exports.hxx>

// ****************************************************************************
// Forward declarations for classes
// ****************************************************************************

class CoordSys;
class Point3;
class UgAssemblyNode;

// This class defines the interface for the creation and manipulation of
// NX coordinate system objects.
class OPENPPEXPORT UgCoordSys : public UgDisplayableObject, 
                                     public UgOrientableObject
{

    UG_DECLARE_INTERNAL_CLASS ( UgCoordSys )
    
    public:

        // Create a UgCoordSys object at the specified coordinate system.
        static UgCoordSys *create
        ( 
            const CoordSys  &csys,          // <I>
                                            // The defining coordinate system in Absolute
                                            // Coordinate System coordinates of the 
                                            // coordinate system.
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

        // Return the origin in Absolute Coordinate System coordinates of the
        // invoking object.
        const Point3 getOrigin ( ) const;

        // Return the defining coordinate system in Absolute Coordinate System coordinates
        // of the invoking object.
        const CoordSys getCoordSys ( ) const;

        // Edit the origin of the invoking object
        void setOrigin
        (
            const Point3 &origin            // <I>
                                            // The new origin in Absolute Coordinate
                                            // System coordinates of the coordinate 
                                            // system.
        );

        // Return the prototype object of the invoking object if the invoking object
        // is an occurrence.  Return the invoking object if the invoking object is 
        // not an occurrence
        UgCoordSys *askPrototype ( ) const;

        // Return the occurrence object that corresponds to the invoking prototype
        // object and is owned by the given UgAssemblyNode object. Return 0 if the
        // invoking object is not a prototype object, or if the occurrence object can
        // not be found.
        UgCoordSys *askOccurrence 
        (
             const UgAssemblyNode *node  // <I> 
                                         // The owning object of the returned occurrence
                                         // object.
        ) const;

        // Return a std::vector object that contains all of the occurrences of the
        // invoking prototype object in all of the UgAssemblyNode objects in the
        // session.  Return a zero-length std::vector if the invoking object is not a
        // prototype object, or if the invoking object has no occurrences.
        const std::vector < UgCoordSys * > askAllOccurrences ( ) const;

    protected:

        // Initialize a UgCoordSys object by actually creating an NX database coordinate
        // system at the specified coordinate system.
        void initialize 
        ( 
            const CoordSys  &csys,          // <I>
                                            // The defining coordinate system in Absolute
                                            // Coordinate System coordinates of the 
                                            // coordinate system.
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

        // Construct a UgCoordSys object
        UgCoordSys
        (
            tag_t tag = NULL_TAG            // The tag of the NX database coordinate system
                                            // that the UgCoordSys object corresponds to.
        );

        // Destroy a UgCoordSys object
        virtual ~UgCoordSys ( );

};

#undef EXPORTLIBRARY

#endif  // UG_COORD_SYS_INCLUDED
