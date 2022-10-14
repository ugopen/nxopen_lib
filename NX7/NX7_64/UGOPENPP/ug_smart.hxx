/*
================================================================================

          Copyright (c) 1998-2000 Unigraphics Solutions Inc.
                    Unpublished - All rights reserved

================================================================================
  File description:

    Header file for Smart Object C++ class definitions.

================================================================================

*/

#ifndef UG_SMART_INCLUDED
#define UG_SMART_INCLUDED

// ****************************************************************************
// Include files for base classes and other needed types
// ****************************************************************************

#include <ug_object.hxx>

#include <uf_so.h>
#include <libopenpp_exports.hxx>

// ****************************************************************************
// Forward declarations for classes
// ****************************************************************************

class UgFeatureObject;

// This class defines the interface for the accessing and editing of the
// parameters that constitute a smart NX object.  All NX object Open++
// classes that represent an object that can be smart are derived from
// this class.
class OPENPPEXPORT UgSmartObject : public virtual UgObject
{

    public:

        // This enum defines the update behaviors that are available to smart objects.
        enum UpdateOption
        {
            NoUpdate                    = UF_SO_dont_update,     //
                                                    // The smart object does not update.
                                                    // Smart objects that do not have 
                                                    // parameters do not update.  This option
                                                    // is intended for future use.
            UpdateWithinModeling        = UF_SO_update_within_modeling,      //
                                                    // The smart object updates within modeling,
                                                    // just like a feature does.  This option
                                                    // is intended for future use.
            UpdateAfterModeling         = UF_SO_update_after_modeling
                                                    // The smart object updates after modeling,
                                                    // just like a dimension does.
        };

        // This enum defines the visibility behaviors that are available to smart objects.
        enum VisibilityOption
        {
            Invisible                   = UF_SO_invisible,      //
                                                    // The smart object is not visible.
            Visible                     = UF_SO_visible,        //
                                                    // The smart object is visible.
            VisibleIfParentInvisible    = UF_SO_visible_if_parent_invisible
                                                    // The smart object is visible only if one
                                                    // or more of the smart object's parents 
                                                    // not loaded.  This option is used 
                                                    // mainly for extracted smart objects.
        };

        // Determine if the invoking object has parameters.
        bool hasParameters ( ) const;

        // Determine if the invoking object has a parent that has been deleted.
        bool isParentDeleted ( ) const;

        // Determine if the invoking object has a parent that is asleep.
        bool isParentAsleep ( ) const;

        // Determine if the invoking object has a parent that is not loaded.
        bool isParentNotLoaded ( ) const;

        // Determine if the invoking object has a parent that is out of date.
        bool isParentOutOfDate ( ) const;

        // Determine if the invoking object is out of date.
        bool isOutOfDate ( ) const;

        // Determine if the invoking object has become non associative.
        bool hasBecomeNonAssociative ( ) const;

        // Determine if the invoking object has a parent that has become non associative.
        bool hasParentBecomeNonAssociative ( ) const;

        // Determine if the invoking object has a parent that has failed to update.
        bool hasParentUpdateError ( ) const;

        // Return the visibility option of the invoking object. 
        VisibilityOption getVisibilityOption ( ) const;
        
        // Return the update error code of invoking object.
        int askUpdateErrorCode ( ) const;

        // Return the feature of the invoking object.
        // Return 0 if the invoking object does not belong to a feature.
        UgFeatureObject *askFeature ( ) const;

        // Delete the parameters of invoking object.
        void deleteParameters ( );

    protected:

        // Construct a UgSmartObject object
        UgSmartObject
        (
            tag_t tag = NULL_TAG            // The tag of the NX database object that
                                            // the UgSmartObject object corresponds to.
        );

        // Destroy a UgSmartObject object
        virtual ~UgSmartObject ( );

    private:

        // Return true if the invoking object is a prototype object.  Return false
        // otherwise.  This method is needed for UgSmartObject because occurrences cannot
        // be smart objects and this class does not derive from the UgDisplayableObject
        // class so as to be able to use UgDisplayableObject::isOccurrence().
        bool isPrototype ( ) const;

};


// This class defines the interface for the accessing and editing of the
// parameters that constitute a smart, displayable NX object.  All NX
// object Open++ classes that are derived from the class
// UgDisplayableObject and that represent an object that can be smart
// are derived from this class.
class OPENPPEXPORT UgDisplayableSmartObject : public UgSmartObject
{

    public:

        // Edit the visibility option of the invoking object. 
        void setVisibilityOption
        (
            VisibilityOption visibility_option      // <I>
                                                    // The new visibility option
        );
 
    protected:

        // Construct a UgDisplayableSmartObject object
        UgDisplayableSmartObject
        (
            tag_t tag = NULL_TAG            // The tag of the NX database object that
                                            // the UgDisplayableSmartObject object
                                            // corresponds to.
        );

        // Destroy a UgDisplayableSmartObject object
        virtual ~UgDisplayableSmartObject ( );

};

#undef EXPORTLIBRARY

#endif  // UG_SMART_INCLUDED
