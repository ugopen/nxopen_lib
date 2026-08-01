/*
================================================================================

          Copyright (c) 1999-2000 Unigraphics Solutions Inc.
                    Unpublished - All rights reserved

================================================================================
  File description:

    Header file for Reference Set C++ class definitions

================================================================================

*/

#ifndef UG_REFERENCE_SET_INCLUDED
#define UG_REFERENCE_SET_INCLUDED

// ****************************************************************************
// Include files for base classes and other needed types
// ****************************************************************************

#include <ug_typed.hxx>

#include <ug_string.hxx>
#include <ug_vector.hxx>
#include <libopenpp_exports.hxx>

// ****************************************************************************
// Forward declarations for classes
// ****************************************************************************

class UgDisplayableObject;
class CoordSys;

// This class defines the interface for the creation and manipulation of
// NX reference sets.
class OPENPPEXPORT UgReferenceSet : public UgTypedObject
{

    UG_DECLARE_INTERNAL_CLASS ( UgReferenceSet )

    public:

        // Create a UgReferenceSet object by specifying its components.
        static UgReferenceSet *create
        (
            const std::string                           &set_name,    // <I>
                                                                      // The name of the reference set.
            const CoordSys                              &orientation, // <I>
                                                                      // The orientation of the reference set
            const std::vector < UgDisplayableObject * > &members      // <I>
                                                                      // The members of the reference set.
                                                                      // The part that owns the first member
                                                                      // is the owning part of the new object
        );

        // Add new members to the invoking UgReferenceSet object.
        void addMembers
        (
            const std::vector < UgDisplayableObject * > &members // <I>
                                                                 // The new members to add to the
                                                                 // reference set.
        );

        // Return a std::vector object that contains the displayable members of the invoking UgReferenceSet object.
        // If you want the non-displayable members too, please use the c-function UF_ASSEM_ask_ref_set_members.
        const std::vector < UgDisplayableObject * >  askMembers ( ) const;


        // Remove members from the invoking UgReferenceSet object.
        void removeMembers
        (
            const std::vector < UgDisplayableObject * > &members  // <I>
                                                                  // The existing members to remove
                                                                  // from the reference set.
        );

        // Return the orientation of the invoking UgReferenceSet object.
        const CoordSys getCoordSys ( ) const;

        // Edit the orientation of the invoking UgReferenceSet object.
        void setCoordSys
        (
            const CoordSys &orientation // <I>
                                        // The new orientation of the reference set.
        );

    protected :

        // Initialize a UgReferenceSet object by actually creating an NX database
        // reference set from its components.
        void initialize
        (
            const std::string                           &set_name,    // <I>
                                                                      // The name of the reference set.
            const CoordSys                              &orientation, // <I>
                                                                      // The orientation of the reference set.
            const std::vector < UgDisplayableObject * > &members      // <I>
                                                                      // The members of the reference set.
                                                                      // The part that owns the first member
                                                                      // is the owning part of the new object.
        );

        // Construct a UgRefernceSet object.
        UgReferenceSet
        (
            tag_t tag = NULL_TAG  // <I>
                                  // Tag of the NX database reference set that the UgReferenceSet
                                  // object corresponds to.
        );

        // Destroy a UgRefernceSet object.
        virtual ~UgReferenceSet ( );

};

#undef EXPORTLIBRARY

#endif  // UG_REFERENCE_SET_INCLUDED
