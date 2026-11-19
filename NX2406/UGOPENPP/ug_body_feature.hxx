/*
================================================================================

          Copyright (c) 1999-2000 Unigraphics Solutions Inc.
                    Unpublished - All rights reserved

================================================================================
  File description:

    Header file for Body Feature C++ class definitions.

================================================================================

*/

#ifndef UG_BODY_FEATURE_INCLUDED
#define UG_BODY_FEATURE_INCLUDED

// ****************************************************************************
// Include files for base classes and other needed types
// ****************************************************************************

#include <ug_feature.hxx>

#include <ug_vector.hxx>

#include <uf_modl.h>
#include <libopenpp_exports.hxx>
#include <UGOpenCPP_NXDeprecation.hxx>

// ****************************************************************************
// Forward declarations for classes
// ****************************************************************************

class UgBody;
class UgFace;
class UgEdge;

// This class defines the interface for the manipulation of NX body feature objects.
class UGOPENCPP_DEPRECATED("Replacement functionality exists in NXOpen API. Consider replacing usage with NXOpen::Features::BodyFeature.") OPENPPEXPORT UgBodyFeatureObject : public UgFeatureObject {

    public:

        // This enum defines the apply options that are available to body features.
        UGOPENCPP_DEPRECATED("Replacement functionality exists in NXOpen API. Consider replacing usage with NXOpen::Features::BodyFeature.") enum ApplyOption
        {
            Unite     = UF_POSITIVE,        //
                                            // The feature is united to the body.
            Subtract  = UF_NEGATIVE,        //
                                            // The feature is subtracted from the body.       
            Intersect = UF_UNSIGNED
                                            // The feature is intersected with the body.
        };
        
        // Return the body of the invoking object.
        UGOPENCPP_DEPRECATED("Replacement functionality exists in NXOpen API. Consider replacing usage with NXOpen::Features::BodyFeature.") UgBody *askBody ( ) const;

        // Return all the faces of the invoking object.
        UGOPENCPP_DEPRECATED("Replacement functionality exists in NXOpen API. Consider replacing usage with NXOpen::Features::BodyFeature.") const std::vector < UgFace * > askFaces ( ) const;

        // Return all the edges of the invoking object.
        UGOPENCPP_DEPRECATED("Replacement functionality exists in NXOpen API. Consider replacing usage with NXOpen::Features::BodyFeature.") const std::vector < UgEdge * > askEdges ( ) const;

   protected:

        // Construct a UgBodyFeature object
        UgBodyFeatureObject 
        ( 
            tag_t tag = NULL_TAG            // The tag of the NX database body feature that
                                            // the UgBodyFeature object corresponds to.
        );

        // Destroy a UgBodyFeature object
        virtual ~UgBodyFeatureObject ( );

    // The UgObject class is a friend to make use of the constructor of this class.
    friend class UgObject;

};

#undef EXPORTLIBRARY

#endif  // UG_BODY_FEATURE_INCLUDED
