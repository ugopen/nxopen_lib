/*
================================================================================

          Copyright (c) 1998-2000 Unigraphics Solutions Inc.
                    Unpublished - All rights reserved

================================================================================
  File description:

    Header file for NX Displayable object C++ class definitions

================================================================================

*/

#ifndef UG_DISPLAYABLE_INCLUDED
#define UG_DISPLAYABLE_INCLUDED

// ****************************************************************************
// Include files for base classes and other needed types
// ****************************************************************************

#include <ug_constants.hxx> // Cannot define enum's as incomplete types on hp/sun <JBT>
#include <ug_typed.hxx>
#include <ug_vector.hxx>
#include <libopenpp_exports.hxx>
#include <UGOpenCPP_NXDeprecation.hxx>

// ****************************************************************************
// Forward declarations for classes
// ****************************************************************************

class UgReferenceSet;
class UgAssemblyNode;
class CoordSys;

// This class defines the interface for the manipulation of NX displayable objects.
class UGOPENCPP_DEPRECATED("Replacement functionality exists in NXOpen API. Consider replacing usage with NXOpen::DisplayableObject.") OPENPPEXPORT UgDisplayableObject : public UgTypedObject
{

    public:

        // Determine if the invoking object is blanked.
        UGOPENCPP_DEPRECATED("Replacement functionality exists in NXOpen API. Consider replacing usage with NXOpen::DisplayableObject.") bool isBlanked ( ) const;

        // Determine if the invoking object is highlighted.
        UGOPENCPP_DEPRECATED("Replacement functionality exists in NXOpen API. Consider replacing usage with NXOpen::DisplayableObject.") bool isHighlighted ( ) const;

        // Return the layer of the invoking object.
        UGOPENCPP_DEPRECATED("Replacement functionality exists in NXOpen API. Consider replacing usage with NXOpen::DisplayableObject.") int getLayer ( ) const;
 
        // Return the color of the invoking object.
        UGOPENCPP_DEPRECATED("Replacement functionality exists in NXOpen API. Consider replacing usage with NXOpen::DisplayableObject.") UgColor getColor ( ) const;

        // Return the line width of the invoking object.
        UGOPENCPP_DEPRECATED("Replacement functionality exists in NXOpen API. Consider replacing usage with NXOpen::DisplayableObject.") UgLineWidth getLineWidth ( ) const;

        // Return the line font of the invoking object.
        UGOPENCPP_DEPRECATED("Replacement functionality exists in NXOpen API. Consider replacing usage with NXOpen::DisplayableObject.") UgLineFont getLineFont ( ) const;

        // Edit the layer of the invoking object.
        UGOPENCPP_DEPRECATED("Replacement functionality exists in NXOpen API. Consider replacing usage with NXOpen::DisplayableObject.") void setLayer
        (
            int          layer  // <I>
                                // The new layer to place the invoking object on.
        );
 
        // Edit the color of the invoking object.
        UGOPENCPP_DEPRECATED("Replacement functionality exists in NXOpen API. Consider replacing usage with NXOpen::DisplayableObject.") void setColor
        (
            UgColor      color  // <I>
                                // The new color to assign to the invoking object
        );
 
        // Edit the line width of the invoking object
        UGOPENCPP_DEPRECATED("Replacement functionality exists in NXOpen API. Consider replacing usage with NXOpen::DisplayableObject.") void setLineWidth
        (
            UgLineWidth  width  // <I>
                                // The new line width to assign to the invoking object
        );
 
        // Edit the line font of the invoking object
        UGOPENCPP_DEPRECATED("Replacement functionality exists in NXOpen API. Consider replacing usage with NXOpen::DisplayableObject.") void setLineFont
        (
            UgLineFont   font   // <I>
                                // The new line font to assign to the invoking object
        );

        // Blank the invoking object.
        UGOPENCPP_DEPRECATED("Replacement functionality exists in NXOpen API. Consider replacing usage with NXOpen::DisplayableObject.") void blank ( );

        // Unblank the invoking object.
        UGOPENCPP_DEPRECATED("Replacement functionality exists in NXOpen API. Consider replacing usage with NXOpen::DisplayableObject.") void unblank ( );
  
        // Highlight the invoking object.
        UGOPENCPP_DEPRECATED("Replacement functionality exists in NXOpen API. Consider replacing usage with NXOpen::DisplayableObject.") void highlight ( );

        // Unhighlight the invoking object.
        UGOPENCPP_DEPRECATED("Replacement functionality exists in NXOpen API. Consider replacing usage with NXOpen::DisplayableObject.") void unhighlight ( );

        // Return a std::vector object that contains all of the reference sets that the
        // invoking object belongs to.  Return a zero-length std::vector if the invoking
        // object does not belong to any reference sets.
        UGOPENCPP_DEPRECATED("Replacement functionality exists in NXOpen API. Consider replacing usage with NXOpen::DisplayableObject.") const std::vector < UgReferenceSet * > askReferenceSets ( ) const;

        // Return true if the invoking object belongs to a reference set.  Return false
        // otherwise.
        UGOPENCPP_DEPRECATED("Replacement functionality exists in NXOpen API. Consider replacing usage with NXOpen::DisplayableObject.") bool isReferenceSetMember ( ) const;

        // Return true if the invoking object is an occurrence.  Return false otherwise.
        UGOPENCPP_DEPRECATED("Replacement functionality exists in NXOpen API. Consider replacing usage with NXOpen::DisplayableObject.") bool isOccurrence ( ) const;

        // Return the prototype object of the invoking object if the invoking object
        // is an occurrence. Return the invoking object if the invoking object is 
        // not an occurrence
        UGOPENCPP_DEPRECATED("Replacement functionality exists in NXOpen API. Consider replacing usage with NXOpen::DisplayableObject.") UgDisplayableObject *askPrototype ( ) const;

        // Return the occurrence object that corresponds to the invoking prototype
        // object and is owned by the given UgAssemblyNode object. Return 0 if the
        // invoking object is not a prototype object, or if the occurrence object can
        // not be found.
        UGOPENCPP_DEPRECATED("Replacement functionality exists in NXOpen API. Consider replacing usage with NXOpen::DisplayableObject.") UgDisplayableObject *askOccurrence
        (
             const UgAssemblyNode *node  // <I> 
                                         // The owning object of the returned occurrence
                                         // object.
        ) const;

        // Return a std::vector object that contains all of the occurrences of the
        // invoking prototype object in all of the UgAssemblyNode objects in the
        // session.  Return a zero-length std::vector if the invoking object is not a
        // prototype object, or if the invoking object has no occurrences.
        UGOPENCPP_DEPRECATED("Replacement functionality exists in NXOpen API. Consider replacing usage with NXOpen::DisplayableObject.") const std::vector < UgDisplayableObject * > askAllOccurrences ( ) const;

        // Return the UgAssemblyNode object that owns the invoking occurrence object.
        // Return 0 if the invoking object is a prototype object.
        UGOPENCPP_DEPRECATED("Replacement functionality exists in NXOpen API. Consider replacing usage with NXOpen::DisplayableObject.") UgAssemblyNode *askAssemblyNode ( ) const;

       
        // Return the transform data of the invoking object if the invoking object 
        // is an occurrence.  Return the Identity Coordinate System and a scale of
        // 1.0 if the invoking object is not an occurrence.
        UGOPENCPP_DEPRECATED("Replacement functionality exists in NXOpen API. Consider replacing usage with NXOpen::DisplayableObject.") void askTransformData
        (
             CoordSys *orientation, // <O>
                                    // The position and orientation in Absolute 
                                    // Coordinate System coordinates that maps from the
                                    // Absolute Coordinate System to the coordinate
                                    // system of the occurrence.
             double   *scale        // <O>
                                    // The scale factor. 
                                    // This value will be non-unity if there is a 
                                    // unit mix (inches/millimeters) between the
                                    // UgAssemblyNode object that owns the occurrence
                                    // and the UgPart object that owns the prototype.
        );

    protected:

        // Construct a UgDisplayableObject object
        UgDisplayableObject
        (
            tag_t tag = NULL_TAG            // The tag of the NX database displayable object
                                            // that the UgDisplayableObject object corresponds to.
        );

        // Destroy a UgDisplayableObject object
        virtual ~UgDisplayableObject ( );

    // The UgObject class is a friend to make use of the constructor of this class.
    friend class UgObject;

};

#undef EXPORTLIBRARY

#endif  // UG_DISPLAYABLE_INCLUDED
