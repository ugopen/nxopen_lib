/*
================================================================================

          Copyright (c) 1998-2000 Unigraphics Solutions Inc.
                    Unpublished - All rights reserved

================================================================================
  File description:

    Header file for Orientable Object C++ class definitions.

================================================================================

*/

#ifndef UG_ORIENTABLE_INCLUDED
#define UG_ORIENTABLE_INCLUDED

// ****************************************************************************
// Include files for base classes and other needed types
// ****************************************************************************

#include <ug_object.hxx>
#include <libopenpp_exports.hxx>

// ****************************************************************************
// Forward declarations for classes
// ****************************************************************************

class Matrix3;

// This class defines the interface for the accessing and editing of the
// orientation matrix that is attached to an NX object.  Each NX object
// Open++ class that represents an object that references an 
// orientation matrix is derived from this class.
class OPENPPEXPORT UgOrientableObject : public virtual UgObject
{

    public:

        // Return the orientation matrix in Absolute Coordinate System coordinates
        // of the invoking object.
        virtual const Matrix3 getMatrix ( ) const;

        // Edit the orientation matrix of the invoking object.
        virtual void setMatrix
        (
            const Matrix3 &matrix   // <I>
                                    // The matrix in Absolute Coordinate System
                                    // coordinates that re-defines the orientation
                                    // of the invoking object.
        );

    protected:

        // Construct a UgOrientableObject object
        UgOrientableObject
        (
            tag_t tag = NULL_TAG            // The tag of the NX database object that
                                            // the UgOrientableObject object corresponds to.
        );

        // Destroy a UgOrientableObject object
        virtual ~UgOrientableObject ( );

};

#undef EXPORTLIBRARY

#endif  // UG_ORIENTABLE_INCLUDED
