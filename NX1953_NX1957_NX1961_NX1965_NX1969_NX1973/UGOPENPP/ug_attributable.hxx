/*
================================================================================

          Copyright (c) 1998-2000 Unigraphics Solutions Inc.
                    Unpublished - All rights reserved

================================================================================
  File description:

    Header file for NX Attributable object C++ class definitions.

================================================================================

*/

#ifndef UG_ATTRIBUTABLE_INCLUDED
#define UG_ATTRIBUTABLE_INCLUDED

// ****************************************************************************
// Include files for base classes and other needed types
// ****************************************************************************

#include <ug_object.hxx>

#include <ug_string.hxx>
#include <ug_vector.hxx>
#include <libopenpp_exports.hxx>

// ****************************************************************************
// Forward declarations for classes
// ****************************************************************************

extern "C"
{
// 
typedef struct UF_ATTR_value_s UF_ATTR_value_t;
}

// This class defines the interface for the creation and manipulation of
// NX Attributes.
class OPENPPEXPORT UgAttributableObject : public virtual UgObject {

    public:

        // Return true if an int attribute with the  
        // given title is attached to the invoking object.
        bool isIntAttribute
        ( 
            const std::string &title            // <I>
                                                // The attribute title
        ) const;

        // Return true if a double attribute with the  
        // given title is attached to the invoking object.
        bool isDoubleAttribute
        ( 
            const std::string &title            // <I>
                                                // The attribute title
        ) const;
        
        // Return true if a string attribute with the  
        // given title is attached to the invoking object.
        bool isStringAttribute
        ( 
            const std::string &title            // <I>
                                                // The attribute title
        ) const;

        // Return true if a null attribute with the  
        // given title is attached to the invoking object.
        bool isNullAttribute
        ( 
            const std::string &title            // <I>
                                                // The attribute title
        ) const;

        // Create a new int attribute with the given
        // title and attach it to the invoking object.
        void addIntAttribute
        (
            const std::string &title,           // <I>
                                                // The attribute title
            int                int_value        // <I>
                                                // The attribute value
        );

        // Create a new double attribute with the given
        // title and attach it to the invoking object.
        void addDoubleAttribute
        (
            const std::string &title,           // <I>
                                                // The attribute title
            double             double_value     // <I>
                                                // The attribute value
        );

        // Create a new string attribute with the given
        // title and attach it to the invoking object.
        void addStringAttribute
        (
            const std::string &title,           // <I>
                                                // The attribute title
            const std::string &string_value     // <I>
                                                // The attribute value
        );

        // Create a new null attribute with the given
        // title and attach it to the invoking object.
        void addNullAttribute
        (
            const std::string &title            // <I>
                                                // The attribute title
        );

        // Return the value of the int attribute with
        // the given title that is attached to the invoking object.
        int getIntAttributeValue 
        ( 
            const std::string &title            // <I>
                                                // The attribute title
        ) const;

        // Return the value of the double attribute with
        // the given title that is attached to the invoking object.
        double getDoubleAttributeValue 
        ( 
            const std::string &title            // <I>
                                                // The attribute title
        ) const;

        // Return the value of the string attribute with
        // the given title that is attached to the invoking object.
        const std::string getStringAttributeValue 
        ( 
            const std::string &title            // <I>
                                                // The attribute title
        ) const;
 
        // Edit the value of the int attribute with
        // the given title that is attached to the invoking object.
        void setIntAttributeValue
        (
            const std::string &title,           // <I>
                                                // The attribute title
            int                int_value        // <I>
                                                // The new attribute value
        ); 

        // Edit the value of the double attribute with
        // the given title that is attached to the invoking object.
        void setDoubleAttributeValue
        (
            const std::string &title,           // <I>
                                                // The attribute title
            double             double_value     // <I>
                                                // The new attribute value
        ); 

        // Edit the value of the string attribute with
        // the given title that is attached to the invoking object.
        void setStringAttributeValue
        (
            const std::string &title,           // <I>
                                                // The attribute title
            const std::string &string_value     // <I>
                                                // The new attribute value
        ); 

        // Delete the int attribute with
        // the given title that is attached to the invoking object.
        void deleteIntAttribute
        (                                              
            const std::string &title            // <I>
                                                // The attribute title
        );

        // Delete the double attribute with
        // the given title that is attached to the invoking object.
        void deleteDoubleAttribute
        (                                              
            const std::string &title            // <I>
                                                // The attribute title
        );        
        
        // Delete the string attribute with
        // the given title that is attached to the invoking object.
        void deleteStringAttribute
        (                                              
            const std::string &title            // <I>
                                                // The attribute title
        );

        // Delete the null attribute with
        // the given title that is attached to the invoking object.
        void deleteNullAttribute
        (                                              
            const std::string &title            // <I>
                                                // The attribute title
        );

        // Return the titles of all of the int attributes attached to the invoking object.
        const std::vector < std::string > askIntAttributeTitles ( ) const;

        // Return the titles of all of the double attributes attached to the invoking object.
        const std::vector < std::string > askDoubleAttributeTitles ( ) const;

        // Return the titles of all of the string attributes attached to the invoking object.
        const std::vector < std::string > askStringAttributeTitles ( ) const;

        // Return the titles of all of the null attributes attached to the invoking object.
        const std::vector < std::string > askNullAttributeTitles ( ) const;

        // Delete all of the int attributes attached to the invoking object.
        void deleteAllIntAttributes ( );

        // Delete all of the double attributes attached to the invoking object.
        void deleteAllDoubleAttributes ( );

        // Delete all of the string attributes attached to the invoking object.
        void deleteAllStringAttributes ( );
        
        // Delete all of the null attributes attached to the invoking object.
        void deleteAllNullAttributes ( );
  
    protected:

        // Construct a UgAttributableObject object
        explicit UgAttributableObject
        (
            tag_t tag = NULL_TAG                // The tag of the NX database attribute that 
                                                // the UgAttributableObject object corresponds to.
        );

        // Destroy a UgAttributableObject object
        virtual ~UgAttributableObject ( );

    private:

        // Does an attribute of the given title and type exist ?
        bool isAttribute
        ( 
            const std::string &title,           // <I>
                                                // The attribute title 
            int                type             // <I>
                                                // The attribute type
        ) const;

        // Count the attributes of the given type
        int countAttributes 
        ( 
            int type                            // <I>
                                                // The attribute type
        ) const;

        // Return the attribute titles of the given type attached to the invoking object..
        const std::vector < std::string > askAttributeTitles 
        ( 
            int type                            // <I>
                                                // The attribute type
        ) const;

        // Return the attribute of the given title and type attached to the invoking object.        
        const UF_ATTR_value_t getAttribute 
        ( 
            const std::string &title,           // <I>
                                                // The attribute title 
            int                type             // <I>
                                                // The attribute type 
        ) const;        
        
        // Edit the attribute of the given title and type attached to the invoking object.
        void setAttribute 
        ( 
            const std::string      &title,      // <I>
                                                // The attribute title 
            const UF_ATTR_value_t  *value       // <I>
                                                // The attribute type/value
        ) const;

        // Add an attribute of the given title and type to the invoking object.
        void addAttribute 
        ( 
            const std::string      &title,      // <I>
                                                // The attribute title 
            const UF_ATTR_value_t  *value       // <I>
                                                // The attribute type/value
        ) const;

        // Delete the attribute of the given title and type attached to the invoking object.
        void deleteAttribute 
        ( 
            const std::string &title,           // <I>
                                                // The attribute title 
            int                type             // <I>
                                                // The attribute type 
        ) const;
    
        // Delete all attributes of the given type attached to the invoking object.
        void deleteAllAttributes 
        ( 
            int type                            // <I>
                                                // The attribute type
        ) const;

        // For parts we have to use the part attribute tag.
        tag_t askTag ( ) const;

};

#undef EXPORTLIBRARY

#endif  // UG_ATTRIBUTE_INCLUDED
