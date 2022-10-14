/*
================================================================================

          Copyright (c) 1998-2000 Unigraphics Solutions Inc.
                    Unpublished - All rights reserved

================================================================================
  File description:

    Header file for Edge C++ class definitions.

================================================================================

*/

#ifndef UG_EDGE_INCLUDED
#define UG_EDGE_INCLUDED

// ****************************************************************************
// Include files for base classes and other needed types
// ****************************************************************************

#include <ug_evaluatable.hxx>
#include <ug_vector.hxx>
#include <libopenpp_exports.hxx>

// ****************************************************************************
// Forward declarations for classes
// ****************************************************************************

class UgBodyFeatureObject;
class UgBody;
class UgFace;
class UgAssemblyNode;

class Curve;

// This class defines the interface for the manipulation of NX edge objects.
class OPENPPEXPORT UgEdge : public UgEvaluatableObject
{

    UG_DECLARE_INTERNAL_CLASS ( UgEdge )

    public:

        // Return the body of the invoking object.
        UgBody *askBody ( ) const;

        // Return all of the features of the invoking object.
        const std::vector < UgBodyFeatureObject * > askFeatures ( ) const;

        // Return all of the faces of the invoking object.
        const std::vector < UgFace * > askFaces ( ) const;

        // Return all of the split edges of the invoking object.  All of the edges,
        // including the invoking edge, that were split from the invoking edge are
        // returned by this method.  An edge splits as a result of any number of
        // feature operations.  For example, if a slot is created on a block, the
        // edge that is broken to create the slot is split.
        const std::vector < UgEdge * > askSplitEdges ( ) const;

        // Return the Curve object that represents the invoking object.
        // This method is provided to satisfy the pure virtual method
        // defined in the class UgEvaluatableObject. This method returns
        // a Curve object that represents a snapshot of the edge at the
        // moment that the method is invoked.  A subsequent update
        // affecting the edge could make the snapshot invalid.  As a result,
        // the Curve objects returned by this method should never be cached.
        // In most uses of this method, the 'dynamic_cast' operator should
        // be used to convert the returned Curve pointer to a pointer of
        // a specific curve type to acquire the desired interface.  Currently
        // the valid pointer types that can represent the Curve returned by
        // this method are Line, Arc, Ellipse, and Spline.
        const Curve *askCurve ( ) const;

        // Return the prototype object of the invoking object if the invoking object
        // is an occurrence.  Return the invoking object if the invoking object is 
        // not an occurrence
        UgEdge *askPrototype ( ) const;

        // Return the occurrence object that corresponds to the invoking prototype
        // object and is owned by the given UgAssemblyNode object. Return 0 if the
        // invoking object is not a prototype object, or if the occurrence object can
        // not be found.
        UgEdge *askOccurrence 
        (
             const UgAssemblyNode *node  // <I> 
                                         // The owning object of the returned occurrence
                                         // object.
        ) const;

        // Return a std::vector object that contains all of the occurrences of the
        // invoking prototype object in all of the UgAssemblyNode objects in the
        // session.  Return a zero-length std::vector if the invoking object is not a
        // prototype object, or if the invoking object has no occurrences.
        const std::vector < UgEdge * > askAllOccurrences ( ) const;

    protected:

        // Construct a UgEdge object
        UgEdge
        (
            tag_t tag = NULL_TAG            // The tag of the NX database edge that the
                                            // UgEdge object corresponds to.
        );

        // Destroy a UgEdge object
        virtual ~UgEdge ( );

    private:

        // The Curve object that corresponds to the edge.
        Curve *m_edge_curve;

};

#undef EXPORTLIBRARY

#endif  // UG_EDGE_INCLUDED
