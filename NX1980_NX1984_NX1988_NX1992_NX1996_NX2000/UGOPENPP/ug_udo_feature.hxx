/*
================================================================================

          Copyright (c) 1999-2000 Unigraphics Solutions Inc.
                    Unpublished - All rights reserved

================================================================================
  File description:

    Header file for UDO Feature C++ class definitions.

================================================================================

*/

#ifndef UG_UDO_FEATURE_INCLUDED
#define UG_UDO_FEATURE_INCLUDED

// ****************************************************************************
// Include files for base classes and other needed types
// ****************************************************************************

#include <ug_feature.hxx>
#include <libopenpp_exports.hxx>

// ****************************************************************************
// Forward declarations for classes
// ****************************************************************************

// This class defines the interface for the manipulation of NX udo feature objects.
class OPENPPEXPORT UgUDOFeature : public UgFeatureObject {

    UG_DECLARE_INTERNAL_CLASS ( UgUDOFeature )

    public:

        // Explicitly log the invoking object for update.  
        // This may be called for edits that do not implicitly 
        // log the UDO feature.  'UgExtensionObject::setInt', 
        // for example, does not cause the UDO feature to be 
        // logged for update.  If you consider the UDO to be 
        // out of date after such an edit then you need to 
        // invoke this method and then 'UgSession::update'.
        void logForUpdate ( ) const;

    protected:

        // Construct a UgUDOFeature object
        UgUDOFeature 
        ( 
            tag_t tag = NULL_TAG            // The tag of the NX database udo feature that
                                            // the UgUDOFeature object corresponds to.
        );

        // Destroy a UgUDOFeature object
        virtual ~UgUDOFeature ( );

};

#undef EXPORTLIBRARY

#endif  // UG_UDO_FEATURE_INCLUDED
