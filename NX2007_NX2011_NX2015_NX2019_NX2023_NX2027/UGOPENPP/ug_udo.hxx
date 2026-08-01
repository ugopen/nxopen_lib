/*
================================================================================

          Copyright (c) 1998-2000 Unigraphics Solutions Inc.
                    Unpublished - All rights reserved

================================================================================
  File description:

    Header file for User Defined Object ( UDO ) C++ class definitions.

================================================================================

*/

#ifndef UG_UDO_INCLUDED
#define UG_UDO_INCLUDED

// ****************************************************************************
// Include files for base classes and other needed types
// ****************************************************************************

#include <ug_displayable.hxx>

#include <ug_string.hxx>
#include <ug_vector.hxx>

#include <uf_udobj.h>
#include <libopenpp_exports.hxx>

// ****************************************************************************
// Forward declarations for classes
// ****************************************************************************

class UgUDOFeature;

// This class defines the interface for the creation and manipulation of
// NX User Defined Objects ( UDO ) objects.
class OPENPPEXPORT UgUDO : public UgDisplayableObject {

    UG_DECLARE_INTERNAL_CLASS ( UgUDO )
    
    public:

        // Return the Class ID of the invoking object.
        UF_UDOBJ_class_t askClassId ( ) const;

        // Return the UDO feature of the invoking object.
        UgUDOFeature *askUDOFeature ( ) const;
        
        // Return all of the objects that are owned by the invoking object.
        const std::vector < UgTypedObject * > getOwnedObjects ( ) const;

        // Return all of the int values attached to the invoking object.
        const std::vector < int > getInts ( ) const;

        // Return all of the double values attached to the invoking object.
        const std::vector < double > getDoubles ( ) const;

        // Return all of the strings attached to the invoking object.
        const std::vector < std::string > getStrings ( ) const;

        // Return all of the length values attached to the invoking object.
        const std::vector < double > getLengths ( ) const;

        // Return all of the area values attached to the invoking object.
        const std::vector < double > getAreas   ( ) const;

        // Return all of the volume values attached to the invoking object.
        const std::vector < double > getVolumes ( ) const;

        // Return all of the 'link_type' links attached to the invoking object.
        const std::vector < UgTypedObject * > getLinks 
        ( 
            unsigned int link_type                      // <I>
                                                        // The type of link
        ) const;

        // Edit all of the int values attached to the invoking object.
        void setInts
        (
            const std::vector < int > &ints             // <I>
                                                        // The new int values
        );
        
        // Edit all of the double values attached to the invoking object.
        void setDoubles
        (
            const std::vector < double > &doubles       // <I>    
                                                        // The new double values
        );
        
        // Edit all of the strings attached to the invoking object.
        void setStrings
        (
            const std::vector < std::string > &strings  // <I>
                                                        // The new strings
        );
        
        // Edit all of the length values attached to the invoking object.
        void setLengths
        (
            const std::vector < double > &lengths       // <I>
                                                        // The new length values
        );
        
        // Edit all of the area values attached to the invoking object.
        void setAreas
        (
            const std::vector < double > &areas         // <I>
                                                        // The new area values
        );
        
        // Edit all of the volume values attached to the invoking object.
        void setVolumes
        (
            const std::vector < double > &volumes       // <I>
                                                        // The new volume values
        );

        // Edit all of the 'link_type' links attached to the invoking object.
        void setLinks
        (
            unsigned int                           link_type,  // <I>
                                                               // The type of link
            const std::vector < UgTypedObject * > &links       // <I>
                                                               // The new 'link_type' links
        );

        // Add new int values to the invoking object
        void addInts
        (
            const std::vector < int > &ints             // <I>
                                                        // The int values to add
        );

        // Add new double values to the invoking object
        void addDoubles
        (
            const std::vector < double > &doubles       // <I>    
                                                        // The double values to add
        );

        // Add new string to the invoking object
        void addStrings
        (
            const std::vector < std::string > &strings  // <I>
                                                        // The strings to add
        );

        // Add new length values to the invoking object
        void addLengths
        (
            const std::vector < double > &lengths       // <I>
                                                        // The length values to add
        );

        // Add new area values to the invoking object
        void addAreas
        (
            const std::vector < double > &areas         // <I>
                                                        // The area values to add
        );

        // Add new volume values to the invoking object
        void addVolumes
        (
            const std::vector < double > &volumes       // <I>
                                                        // The volume values to add
        );

        // Add new 'link_type' links to the invoking object.
        void addLinks
        (
            unsigned int                           link_type, // <I>
                                                              // The type of link
            const std::vector < UgTypedObject * > &links      // <I>
                                                              // The 'link_type' links to add
        );

        // Delete the specified int values from the invoking object.
        void deleteInts
        (
            unsigned int offset,                        // <I>
                                                        // The offset in the list of
                                                        // ints to start deleting from.
            unsigned int number_to_delete               // <I>
                                                        // The number of ints to delete.
        );

        // Delete the specified doubles values from the invoking object.
        void deleteDoubles
        (
            unsigned int offset,                        // <I>
                                                        // The offset in the list of
                                                        // doubles to start deleting from.
            unsigned int number_to_delete               // <I>
                                                        // The number of doubles to delete.
        );

        // Delete the specified strings from the invoking object.
        void deleteStrings
        (
            unsigned int offset,                        // <I>
                                                        // The offset in the list of
                                                        // strings to start deleting from.
            unsigned int number_to_delete               // <I>
                                                        // The number of strings to delete.
        );

        // Delete the specified length values from the invoking object.
        void deleteLengths
        (
            unsigned int offset,                        // <I>
                                                        // The offset in the list of
                                                        // lengths to start deleting from.
            unsigned int number_to_delete               // <I>
                                                        // The number of lengths to delete.
        );

        // Delete the specified area values from the invoking object.
        void deleteAreas
        (
            unsigned int offset,                        // <I>
                                                        // The offset in the list of
                                                        // areas to start deleting from.
            unsigned int number_to_delete               // <I>
                                                        // The number of areas to delete.
        );

        // Delete the specified volumes values from the invoking object.
        void deleteVolumes
        (
            unsigned int offset,                        // <I>
                                                        // The offset in the list of
                                                        // volumes to start deleting from.
            unsigned int number_to_delete               // <I>
                                                        // The number of volumes to delete.
        );

    protected:

        // Construct a UgUDO object
        UgUDO
        (
            tag_t tag = NULL_TAG                        // The tag of the NX database UDO that the
                                                        // UgUDO object corresponds to.
        );

        // Destroy a UgUDO object
        virtual ~UgUDO ( );

};

#undef EXPORTLIBRARY

#endif  // UG_UDO_INCLUDED
