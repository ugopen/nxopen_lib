/*
================================================================================

          Copyright (c) 1998-2000 Unigraphics Solutions Inc.
                    Unpublished - All rights reserved

================================================================================
  File description:

    Header file for NX in part object C++ class definitions

================================================================================

*/

#ifndef UG_IN_PART_INCLUDED
#define UG_IN_PART_INCLUDED

// ****************************************************************************
// Include files for base classes and other needed types
// ****************************************************************************

#include <ug_object.hxx>
#include <libopenpp_exports.hxx>

// ****************************************************************************
// Forward declarations for classes
// ****************************************************************************

class UgPart;

// This class defines the interface for the manipulation of NX objects that are
// owned by part objects.
class OPENPPEXPORT UgInPartObject : public virtual UgObject
{

    public:
        
        // Return the NX part object that owns the invoking object.
        UgPart *askOwningPart ( ) const;

        // Delete the NX database object that corresponds to the invoking object.
        // This method must be implemented in a derived class so that all instantiable
        // classes derived from this class have access to the implementation of this
        // method.
        virtual void destroy ( ) = 0;

    protected:

        // Construct a UgInPartObject object
        UgInPartObject
        (
            tag_t tag = NULL_TAG            // The tag of the NX database object that
                                            // the UgInPartObject object corresponds to.
        );

        // Destroy a UgInPartObject object
        virtual ~UgInPartObject ( );

};

#undef EXPORTLIBRARY

#endif  // UG_IN_PART_INCLUDED
