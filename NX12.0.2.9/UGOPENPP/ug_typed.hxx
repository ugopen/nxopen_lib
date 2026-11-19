/*
================================================================================

          Copyright (c) 1998-2000 Unigraphics Solutions Inc.
                    Unpublished - All rights reserved

================================================================================
  File description:

    Header file for Typed NX object C++ class definitions

================================================================================

*/

#ifndef UG_TYPED_INCLUDED
#define UG_TYPED_INCLUDED

// ****************************************************************************
// Include files for base classes and other needed types
// ****************************************************************************

#include <ug_attributable.hxx>
#include <ug_in_part.hxx>
#include <ug_string.hxx>
#include <libopenpp_exports.hxx>

class UgUDO;

// This class defines the interface for the manipulation of NX objects that are
// typed.  This is the base class for every Open++ class that represents an NX
// object that has a type associated with it.
class OPENPPEXPORT UgTypedObject : public UgInPartObject,
                                        public UgAttributableObject
{

    public:

        // Determine if the invoking object is alive.
        bool isAlive ( ) const;

        // Determine if the invoking object is condemned.
        bool isCondemned ( ) const;
 
        // Determine if the invoking object is extended by a UDO.
        bool isExtended ( ) const;

        // Return the Open type ( as defined in uf_object_types.h ) of the invoking object.
        int askType ( ) const;

        // Return the Open subtype ( as defined in uf_object_types.h ) of the invoking object.
        int askSubtype ( ) const;

        // Return the extending UDO of the invoking object.
        // Return 0 if the invoking object is not extended by a UDO.
        UgUDO *askExtendingUDO ( ) const;

        // Return the name of the invoking object.
        virtual const std::string getName ( ) const;

        // Edit the name of the invoking object.
        void setName
        (
            const std::string &name     // <I>
                                        // The new name to give the invoking object
        );

        // Delete the NX database object that corresponds to the invoking object.
        // This method is provided to satisfy the pure virtual method defined in
        // the class UgInPartObject.
        void destroy ( );

    protected:

        // Construct a UgTypedObject object
        UgTypedObject
        (
            tag_t tag = NULL_TAG            // The tag of the NX database object that
                                            // the UgTypedObject object corresponds to.
        );

        // Destroy a UgTypedObject object
        virtual ~UgTypedObject ( );

    // The UgObject class is a friend to make use of the constructor of this class.
    friend class UgObject;

};

#undef EXPORTLIBRARY

#endif  // UG_TYPED_INCLUDED
