/*
================================================================================

          Copyright (c) 1998-2000 Unigraphics Solutions Inc.
                    Unpublished - All rights reserved

================================================================================
  File description:

    Header file for Body C++ class definitions.

================================================================================

*/

#ifndef UG_BODY_INCLUDED
#define UG_BODY_INCLUDED

// ****************************************************************************
// Include files for base classes and other needed types
// ****************************************************************************

#include <ug_displayable.hxx>
#include <ug_vector.hxx>

#include <uf_modl.h>
#include <libopenpp_exports.hxx>

// ****************************************************************************
// Forward declarations for classes
// ****************************************************************************

class UgBodyFeatureObject;
class UgFace;
class UgEdge;
class UgAssemblyNode;

// This class defines the interface for the manipulation of
// NX body objects.
class OPENPPEXPORT UgBody : public UgDisplayableObject
{

    UG_DECLARE_INTERNAL_CLASS ( UgBody )

    public:

        // This enum defines the units of density that are available for a body.
        enum DensityUnits
        {   
            PoundsInches     = UF_MODL_pounds_inches,       // The density is defined as
                                                            // pounds per cubic inch.
            PoundsFeet       = UF_MODL_pounds_feet,         // The density is defined as
                                                            // pounds per cubic foot.
            GramsCentimeters = UF_MODL_grams_centimeters,   // The density is defined as
                                                            // grams per cubic centimeter.
            KilogramsMeters  = UF_MODL_kilograms_meters     // The density is defined as
                                                            // kilograms per cubic meter.
        };
      
        // Determine if the invoking object is a sheet body.
        bool isSheet ( ) const;
      
        // Determine if the invoking object is a solid body.
        bool isSolid ( ) const;
        
        // Return the density of the invoking object in the requested units.
        double getDensity 
        (
            DensityUnits    units           // <I>
                                            // The units to return the density in
        ) const;
        
        // Return all of the features of the invoking object sorted by order of update.
        const std::vector < UgBodyFeatureObject * > askFeatures ( ) const;

        // Return all of the faces of the invoking object.
        const std::vector < UgFace * > askFaces ( ) const;

        // Return all of the edges of the invoking object.
        const std::vector < UgEdge * > askEdges ( ) const;

        // Edit the density of the body
        // Return the density of the invoking object.
        void setDensity
        (
            DensityUnits    units,          // <I>
                                            // The units that the new density is specified in.
            double          density         // <I>
                                            // The new density
        );

        // Return the prototype object of the invoking object if the invoking object
        // is an occurrence.  Return the invoking object if the invoking object is 
        // not an occurrence
        UgBody *askPrototype ( ) const;

        // Return the occurrence object that corresponds to the invoking prototype
        // object and is owned by the given UgAssemblyNode object. Return 0 if the
        // invoking object is not a prototype object, or if the occurrence object can
        // not be found.
        UgBody *askOccurrence 
        (
             const UgAssemblyNode *node  // <I> 
                                         // The owning object of the returned occurrence
                                         // object.
        ) const;

        // Return a std::vector object that contains all of the occurrences of the
        // invoking prototype object in all of the UgAssemblyNode objects in the
        // session.  Return a zero-length std::vector if the invoking object is not a
        // prototype object, or if the invoking object has no occurrences.
        const std::vector < UgBody * > askAllOccurrences ( ) const;

   protected:

        // Construct a UgBody object
        UgBody
        (
            tag_t tag = NULL_TAG            // The tag of the NX database body that the
                                            // UgBody object corresponds to.
        );

        // Destroy a UgBody object
        virtual ~UgBody ( );

};

#undef EXPORTLIBRARY

#endif  // UG_BODY_INCLUDED
