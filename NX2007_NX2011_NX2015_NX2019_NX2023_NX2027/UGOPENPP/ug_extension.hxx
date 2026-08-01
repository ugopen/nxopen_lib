/*
================================================================================

          Copyright (c) 1998-2000 Unigraphics Solutions Inc.
                    Unpublished - All rights reserved

================================================================================
  File description:

    Header file for Extensions of NX object C++ class definitions

================================================================================

*/

#ifndef UG_EXTENSION_INCLUDED
#define UG_EXTENSION_INCLUDED

// ****************************************************************************
// Include files for base classes and other needed types
// ****************************************************************************

#include <ug_object.hxx>

#include <ug_string.hxx>
#include <libopenpp_exports.hxx>

// ****************************************************************************
// Forward declarations for classes
// ****************************************************************************

class UgUDO;

// ****************************************************************************
// Declare macros for data members and methods for derived classes
// ****************************************************************************

// this macro is ONLY FOR USE within derived classes
// DO NOT USE within Unigraphics classes

#define UG_DECLARE_CLASS( class_name ) \
    public: \
        static UgTypedObject *createDerivedInstance ( ); \
    protected: \
        const UgDerivedClassManager askClassManager ( ) const; \
    private: \
        static const UgDerivedClassManager m_class_manager;

#define UG_DECLARE_FEATURE_CLASS( class_name ) \
    UG_DECLARE_CLASS ( class_name )
    
// ****************************************************************************
// Implement macros for data members and methods for derived classes
// ****************************************************************************

// this macro is ONLY FOR USE within derived classes
// DO NOT USE within Unigraphics classes

#define UG_IMPLEMENT_CLASS( class_name ) \
    UgTypedObject               *class_name::createDerivedInstance ( ) { return new class_name; } \
    const UgDerivedClassManager  class_name::askClassManager ( ) const { return m_class_manager; } \
    const UgDerivedClassManager  class_name::m_class_manager ( #class_name, &class_name::createDerivedInstance, false );

#define UG_IMPLEMENT_FEATURE_CLASS( class_name ) \
    UgTypedObject               *class_name::createDerivedInstance ( ) { return new class_name; } \
    const UgDerivedClassManager  class_name::askClassManager ( ) const { return m_class_manager; } \
    const UgDerivedClassManager  class_name::m_class_manager ( #class_name, &class_name::createDerivedInstance, true );

// ****************************************************************************
// Macros to query and assign attributes to extended objects
// ****************************************************************************

#define UG_INT_PROPERTY( attribute, offset ) \
    int get ## attribute ( ) const \
    { \
        return getInt ( offset ); \
    } \
    void set ## attribute ( int value ) \
    { \
        setInt ( offset, value ); \
    }

#define UG_DOUBLE_PROPERTY( attribute, offset ) \
    double get ## attribute ( ) const \
    { \
        return getDouble ( offset ); \
    } \
    void set ## attribute ( double value ) \
    { \
        setDouble ( offset, value ); \
    }

#define UG_STRING_PROPERTY( attribute, offset ) \
    const std::string get ## attribute ( ) const \
    { \
        return getString ( offset ); \
    } \
    void set ## attribute ( const std::string &value ) \
    { \
        setString ( offset, value ); \
    }

#define UG_LENGTH_PROPERTY( attribute, offset ) \
    double get ## attribute ( ) const \
    { \
        return getLength ( offset ); \
    } \
    void set ## attribute ( double value ) \
    { \
        setLength ( offset, value ); \
    }

#define UG_AREA_PROPERTY( attribute, offset ) \
    double get ## attribute ( ) const \
    { \
        return getArea ( offset ); \
    } \
    void set ## attribute ( double value ) \
    { \
        setArea ( offset, value ); \
    }

#define UG_VOLUME_PROPERTY( attribute, offset ) \
    double get ## attribute ( ) const \
    { \
        return getVolume ( offset ); \
    } \
    void set ## attribute ( double value ) \
    { \
        setVolume ( offset, value ); \
    }

#define UG_LINK1_PROPERTY( class_name, attribute, offset ) \
    class_name *get ## attribute ( ) const \
    { \
        return dynamic_cast < class_name * > ( getLink ( 1, offset ) ); \
    } \
    void set ## attribute ( const class_name *link ) \
    { \
        setLink ( 1, offset, link ); \
    }

#define UG_LINK2_PROPERTY( class_name, attribute, offset ) \
    class_name *get ## attribute ( ) const \
    { \
        return dynamic_cast < class_name * > ( getLink ( 2, offset ) ); \
    } \
    void set ## attribute ( const class_name *link ) \
    { \
        setLink ( 2, offset, link ); \
    }

#define UG_LINK3_PROPERTY( class_name, attribute, offset ) \
    class_name *get ## attribute ( ) const \
    { \
        return dynamic_cast < class_name * > ( getLink ( 3, offset ) ); \
    } \
    void set ## attribute ( const class_name *link ) \
    { \
        setLink ( 3, offset, link ); \
    }

#define UG_LINK4_PROPERTY( class_name, attribute, offset ) \
    class_name *get ## attribute ( ) const \
    { \
        return dynamic_cast < class_name * > ( getLink ( 4, offset ) ); \
    } \
    void set ## attribute ( const class_name *link ) \
    { \
        setLink ( 4, offset, link ); \
    }

// This class defines the interface for accessing the persistent data that belongs to
// a class that has been derived from a leaf Open++ class.  A User Defined Object
// ( UDO ) is used to store the persistent data.  All data of the same type or significance
// is stored in the same block of data; e.g., all integers are stored in the integer
// block, and all lengths are stored in the length block.  A particular piece of data
// is distinguished by its data type or significance ( int, double, length, etc...)
// and an offset value ( beginning with the offset value of 0 ) that defines its position
// within its particular data block.
class OPENPPEXPORT UgExtensionObject : public virtual UgObject
{
 
    public:

        // Return a persistent integer from the extending UDO of the invoking object.
        int getInt
        (
            unsigned int offset         // <I>
                                        // The offset of the requested value.
        ) const;
        
        // Return a persistent double from the extending UDO of the invoking object.
        double getDouble
        (
            unsigned int offset         // <I>
                                        // The offset of the requested value.
        ) const;
        
        // Return a persistent string from the extending UDO of the invoking object.
        const std::string getString
        (
            unsigned int offset         // <I>
                                        // The offset of the requested value.
        ) const;

        // Return a persistent length from the extending UDO of the invoking object.
        double getLength
        (
            unsigned int offset         // <I>
                                        // The offset of the requested value.
        ) const;

        // Return a persistent area from the extending UDO of the invoking object.
        double getArea
        (
            unsigned int offset         // <I>
                                        // The offset of the requested value.
        ) const;

        // Return a persistent volume from the extending UDO of the invoking object.
        double getVolume
        (
            unsigned int offset         // <I>
                                        // The offset of the requested value.
        ) const;

        // Return a linked Open++ object from the extending UDO of the invoking object.
        UgTypedObject *getLink
        (
            unsigned int link_type,     // <I>
                                        // The link type for the requested object
            unsigned int offset         // <I>
                                        // The offset of the requested object
        ) const;

        // Add or edit a persistent integer in the extending UDO of the invoking object.
        void setInt
        (
            unsigned int offset,        // <I>
                                        // The offset of the new value.  If the offset
                                        // is less than or equal to the number of
                                        // existing values of this type, an existing
                                        // value will be edited.  If the offset is
                                        // greater than the number of existing values,
                                        // a new value will be added.
            int          value          // <I>
                                        // The new value to add or edit
        );
        
        // Add or edit a persistent double in the extending UDO of the invoking object.
        void setDouble
        (
            unsigned int offset,        // <I>
                                        // The offset of the new value.  If the offset
                                        // is less than or equal to the number of
                                        // existing values of this type, an existing
                                        // value will be edited.  If the offset is
                                        // greater than the number of existing values,
                                        // a new value will be added.
            double       value          // <I>
                                        // The new value to add or edit
        );
        
        // Add or edit a persistent string in the extending UDO of the invoking object.
        void setString
        (
            unsigned int       offset,  // <I>
                                        // The offset of the new value.  If the offset
                                        // is less than or equal to the number of
                                        // existing values of this type, an existing
                                        // value will be edited.  If the offset is
                                        // greater than the number of existing values,
                                        // a new value will be added.
            const std::string &value    // <I>
                                        // The new value to add or edit
        );       
        
        // Add or edit a persistent length in the extending UDO of the invoking object.
        void setLength
        (
            unsigned int     offset,    // <I>
                                        // The offset of the new value.  If the offset
                                        // is less than or equal to the number of
                                        // existing values of this type, an existing
                                        // value will be edited.  If the offset is
                                        // greater than the number of existing values,
                                        // a new value will be added.
            double           value      // <I>
                                        // The new value to add or edit
        );
        
        // Add or edit a persistent area in the extending UDO of the invoking object.
        void setArea
        (
            unsigned int     offset,    // <I>
                                        // The offset of the new value.  If the offset
                                        // is less than or equal to the number of
                                        // existing values of this type, an existing
                                        // value will be edited.  If the offset is
                                        // greater than the number of existing values,
                                        // a new value will be added.
            double           value      // <I>
                                        // The new value to add or edit
        );
        
        // Add or edit a persistent volume in the extending UDO of the invoking object.
        void setVolume
        (
            unsigned int     offset,    // <I>
                                        // The offset of the new value.  If the offset
                                        // is less than or equal to the number of
                                        // existing values of this type, an existing
                                        // value will be edited.  If the offset is
                                        // greater than the number of existing values,
                                        // a new value will be added.
            double           value      // <I>
                                        // The new value to add or edit
        );
        
        // Add or edit a linked Open++ object to the extending UDO of the invoking
        // object.
        void setLink
        (
            unsigned int          link_type,    // <I>
                                                // The link type to add or edit
            unsigned int          offset,       // <I>
                                                // The offset of the link.  If the offset
                                                // is less than or equal to the number of
                                                // existing links of this type, an existing
                                                // link will be edited.  If the offset is
                                                // greater than the number of existing links,
                                                // a new link will be added.
            const UgTypedObject  *object        // <I>
                                                // The object to add or edit
        );

        // This virtual method allows the derived class to define a method that
        // can provide information when a request is made of information of an
        // instance of the derived class.  The default behavior defined by this
        // method is to provide no information.
        virtual void infoObject ( );

        // This virtual method allows the derived class to define a method that
        // can provide notification when a linked object in the extending UDO of
        // an instance of the derived class is being deleted from an NX part.  This
        // allows the instance to perform any necessary update.  The default
        // behavior defined by this method is to do nothing.
        virtual void memberDeletion
        (
            UgTypedObject *deleted_object       // <I>
                                                // The linked object that is
                                                // being deleted
        );

        // This virtual method allows the derived class to define a method that
        // can provide notification when a linked object in the extending UDO of
        // an instance of the derived class has been changed.  This allows the
        // instance to perform any necessary update.  The default behavior
        // defined by this method is to do nothing.
        virtual void update
        (
            UgTypedObject *updated_object       // <I>
                                                // The linked object that has
                                                // been changed
        );
        
    protected:

        // Return the class manager for the invoking object.  The implementation
        // of this method as a pure virtual method within this class ensures that
        // the UG_DECLARE_CLASS and the UG_IMPLEMENT_CLASS macros have been used
        // in classes deriving from this class.
        virtual const UgDerivedClassManager askClassManager ( ) const = 0;

        // Construct a UgExtensionObject object
        UgExtensionObject
        (
            tag_t tag = NULL_TAG            // The tag of the NX database object that the
                                            // UgExtensionObject object corresponds to.
        );

        // Destroy a UgExtensionObject object
        virtual ~UgExtensionObject ( );

        UgExtensionObject(const UgExtensionObject&) = delete;
        UgExtensionObject& operator=(const UgExtensionObject&) = delete;

    
    private:
 
        // Create the UDO that extends the invoking object.
        void createUDO ( );

        // The member deletion callback function to register with NX for objects of
        // this class.
        static void delete_method
        (
            tag_t             udo_tag,          // <I>
                                                // The tag of the UDO that has a
                                                // linked object being deleted
            UF_UDOBJ_link_t  *delete_cause      // <I>
                                                // The object causing the delete
        );

        // The info object callback function to register with NX for objects of
        // this class.
        static void info_obj_method
        (
            tag_t             udo_tag           // <I>
                                                // The tag of the UDO that is to have
                                                // its information displayed
        );
        
        // The update callback function to register with NX for objects of
        // this class.
        static void update_method
        (
            tag_t             udo_tag,          // <I>
                                                // The tag of the UDO that needs to
                                                // be updated
            UF_UDOBJ_link_t  *update_cause      // <I>
                                                // The object causing the update
        );

        // The tag of the underlying NX UDO that extends the object.
        tag_t   m_udo_tag;

    // The UgDerivedClassManager class is a friend to allow access to the NX
    // callback functions although it is not derived from UgExtensionObject.
    friend class UgDerivedClassManager;

};

#undef EXPORTLIBRARY
 
#endif  // UG_EXTENSION_INCLUDED
