/*
================================================================================

          Copyright (c) 1998-2000 Unigraphics Solutions Inc.
                    Unpublished - All rights reserved

================================================================================
  File description:

    Header file for Class Manager C++ class definitions

================================================================================

*/

#ifndef UG_CLASS_MANAGER_INCLUDED
#define UG_CLASS_MANAGER_INCLUDED

// ****************************************************************************
// Include files for base classes and other needed types
// ****************************************************************************

#include <ug_openpp.hxx>
#include <ug_string.hxx>
#include <uf_udobj.h>
#include <libopenpp_exports.hxx>

// ****************************************************************************
// Forward declarations for classes
// ****************************************************************************

class UgTypedObject;
class UgObject;

// @<EXCLUDE>@
// This class defines the interface for the creation and manipulation of
// objects whose purpose is to manage the classes that define the Open++
// leaf classes.  This class is a support class.  Objects from this class
// are created via machinery within Open++ and should *_NEVER_* be
// created outside of that machinery.
class UgLeafClassManager
{

    public:

        // The signature of a function for the creation of objects of leaf Open++ classes.
        typedef UgObject *( *CreateLeafFunction ) ( tag_t tag );

        // Construct a UgLeafClassManager object for use by leaf Open++ classes
        // to register the creation functions of objects of that class.
        UgLeafClassManager
        (
            int                    object_type,         // The object type (from the header
                                                        // file 'uf_object_types.h') of the
                                                        // leaf class whose creation function
                                                        // is being registered.
            CreateLeafFunction     create_function      // The function that creates instances
                                                        // of the leaf class.
        );

        // Copy constructor
        UgLeafClassManager ( const UgLeafClassManager & src );

        // Destroy a UgLeafClassManager object
        virtual ~UgLeafClassManager ( );

    private:

        // Default constructor that is not implemented
        UgLeafClassManager ( );

        // Assignment operator this not implemented
        UgLeafClassManager & operator= ( const UgLeafClassManager & rhs );

        // Create an instance of a leaf Open++ class.
        static UgObject *createLeafInstance
        (
            int   type,                                 // <I>
                                                        // The NX type for the object
            tag_t tag                                   // <I>
                                                        // The NX tag for the object
        );

        // The function that creates a new instance of a class that is derived from a leaf 
        // Open++ class.
        const CreateLeafFunction m_create_function;

    // The UgObject class is a friend to make use of the private methods of this class.
    friend class UgObject;

};

// @<EXCLUDE>@
// This class defines the interface for the creation and manipulation of
// objects whose purpose is to manage the classes that are user-derived 
// from the Open++ leaf classes.  This class is a support class.  
// Objects from this class are created via machinery within Open++ 
// and should *_NEVER_* be created outside of that machinery.
class OPENPPEXPORT UgDerivedClassManager
{

    public:

        // The signature of a function for the creation of objects of classes derived
        // from leaf Open++ classes.
        typedef UgTypedObject *( *CreateDerivedFunction ) ( );
        
        // Construct a UgDerivedClassManager object for use by classes derived from
        // the leaf Open++ classes to register the creation functions of
        // objects of that class.
        UgDerivedClassManager
        (
            const std::string     &class_name,          // The name of the UDO class to create
                                                        // for the objects of the derived class.
            CreateDerivedFunction  create_function,     // The function that creates instances
                                                        // of the derived class.
            bool                   has_udo_feature      // If true, the UDO class which supports 
                                                        // the derived class is feature based.
                                                        // If false, the UDO class is not feature
                                                        // based.
        );

        // Copy constructor
        UgDerivedClassManager ( const UgDerivedClassManager & src );

        // Destroy a UgDerivedClassManager object
        virtual ~UgDerivedClassManager ( );

    private:

        // Default constructor that is not implemented
        UgDerivedClassManager ( );

        // Assignment operator that is not implemented
        UgDerivedClassManager & operator= ( const UgDerivedClassManager & rhs );

        // Create an instance of a class that is derived from a leaf Open++ class.
        static UgTypedObject *createDerivedInstance
        (
            UF_UDOBJ_class_t class_id,                  // <I>
                                                        // The id of the UDO class that supports
                                                        // the derived class.
            tag_t            tag,                       // <I>
                                                        // The NX tag for the object
            tag_t            udo_tag                    // <I>
                                                        // The NX tag for the udo object
        );

        // Return the id of the UDO class that supports a class that is derived from a leaf
        // Open++ class.
        UF_UDOBJ_class_t askClassId ( ) const;

        // The function that creates a new instance of a class that is derived from a leaf 
        // Open++ class.
        const CreateDerivedFunction m_create_function;

        // The id of the UDO class that supports a class that is derived from a leaf 
        // Open++ class. 
        UF_UDOBJ_class_t            m_class_id;

        // Determines if a class that is derived from a leaf Open++ classes is feature based.
        // If true, the UDO class that supports the derived class is feature based.  If false,
        // the UDO class is not.
        const bool                  m_has_udo_feature;
 
    // The UgObject class is a friend to make use of the private methods of this class.
    friend class UgObject;

    // The UgExtensionObject class is a friend to make use of the private methods of this class.
    friend class UgExtensionObject;

};

#undef EXPORTLIBRARY

#endif  // UG_CLASS_MANAGER_INCLUDED
