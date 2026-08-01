/*
================================================================================

          Copyright (c) 1998-2000 Unigraphics Solutions Inc.
                    Unpublished - All rights reserved

================================================================================
  File description:

    Header file for NX object C++ class definitions

================================================================================

*/

#ifndef UG_OBJECT_INCLUDED
#define UG_OBJECT_INCLUDED

// ****************************************************************************
// Include files for base classes and other needed types
// ****************************************************************************

#include <ug_openpp.hxx>

#include <uf.h>
#include <libopenpp_exports.hxx>

// ****************************************************************************
// Forward declarations for classes
// ****************************************************************************

class UgPart;

// This class defines the interface for manipulation of all tag-based NX objects.
// Every Open++ class that represents an NX database object with a tag is 
// derived from this class.
class OPENPPEXPORT UgObject
{
   
    public:

        // Determine if the tag of the invoking object is NULL_TAG.
        bool isNull ( ) const;

        // Return the NX part object that owns the invoking object.
        // This method must be implemented in a derived class so that all instantiable
        // classes derived from this class have access to the implementation of this
        // method.
        virtual UgPart *askOwningPart ( ) const = 0;

        // Return the tag of the NX database object that corresponds to the invoking object.
        tag_t getTag ( ) const;

        // Find the Open++ object that corresponds to the specified tag.  If an Open++
        // object cannot be found, and an Open++ object cannot be created that corresponds
        // to the specified tag, then this method will return 0.
        static UgObject *find
        (
            tag_t tag                       // <I>
                                            // The tag of the corresponding NX database object
        );        
         
    protected:

        // Edit the tag of the NX database object that corresponds to the invoking object.
        void setTag
        (
            tag_t tag                       // <I>
                                            // The new tag of the NX database object that
                                            // the invoking object will corresponds to.
        );
   
        // Construct a UgObject object
        explicit UgObject
        (
            tag_t tag = NULL_TAG            // The tag of the NX database object that
                                            // the UgObject object corresponds to.
        );

        // Destroy a UgObject object
        virtual ~UgObject ( );

    private:

        // Construct a UgObject object by copying an existing UgObject object.
        // This is provided as a private method to disallow copy construction and
        // ensure a one-to-one mapping between Open++ objects and their NX 
        // database objects.
        UgObject
        (
            const UgObject &ug_object       // The UgObject object to copy
        );

        // Assign a UgObject object by copying an existing UgObject object.
        // This is provided as a private method to disallow assignment and
        // ensure a one-to-one mapping between Open++ objects and their NX 
        // database objects.
        UgObject &operator= 
        ( 
            const UgObject &ug_object       // The UgObject object to assign
        );

        // Clear the tag of the NX database object that corresponds to the invoking object.
        void clearTag ( );

        // Restore the tag of the NX database object that corresponds to the invoking object.
        void restoreTag
        ( 
            tag_t tag                       // <I>
                                            // The tag of the NX database object that
                                            // the invoking object will corresponds to.
        );

        // The tag of the NX database object that the Open++ object corresponds to.
        tag_t m_tag;

        // has the tag been cleared
        bool m_cleared;

    // allow UgDerivedClassManager to invoke setTag ( )
    friend class UgDerivedClassManager;

    // The global function UgTagManagerCallback is a friend to allow access to UgObject
    // internals, enabling the management of Open++ objects via NX callbacks.
    friend void UgTagManagerCallback ( UF_TAG_event_t reason, tag_t tag, void *client_data );

    // The global function UgTagManagerAtExit is a friend to allow access to UgObject
    // internals, enabling the management of Open++ objects via NX callbacks.
    friend void UgTagManagerAtExit ( void );
        
};

// ****************************************************************************
// Declare macros for methods for Unigraphics classes
// ****************************************************************************

#include <ug_class_manager.hxx>

// this macro is ONLY FOR USE within Unigraphics classes
// DO NOT USE within derived classes

#define UG_DECLARE_INTERNAL_CLASS( class_name ) \
    public: \
        static UgObject *createLeafInstance ( tag_t tag ); \
        static int askObjectType ( );
 
// ****************************************************************************
// Implement macros for methods for Unigraphics classes
// ****************************************************************************

// this macro is ONLY FOR USE within Unigraphics classes
// DO NOT USE within derived classes

#define UG_IMPLEMENT_INTERNAL_CLASS( class_name, type ) \
    UgObject                        *class_name::createLeafInstance ( tag_t tag ) { return new class_name ( tag ); } \
    int                              class_name::askObjectType ( ) { return type; } \
    static const UgLeafClassManager  class_name ## _Class ( type, &class_name::createLeafInstance );

#undef EXPORTLIBRARY

#endif  // UG_OBJECT_INCLUDED
