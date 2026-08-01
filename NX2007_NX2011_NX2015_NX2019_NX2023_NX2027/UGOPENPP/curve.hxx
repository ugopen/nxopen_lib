/*
================================================================================

          Copyright (c) 1998-2000 Unigraphics Solutions Inc.
                      Unpublished - All rights reserved

================================================================================
  File description:

    Header file for base Geometric Curve C++ class definitions.

================================================================================

*/

#ifndef CURVE_INCLUDED
#define CURVE_INCLUDED

// ****************************************************************************
// Include files for base classes and other needed types
// ****************************************************************************

#include <ug_openpp.hxx>
#include <libopenpp_exports.hxx>

// ****************************************************************************
// Forward declarations for classes
// ****************************************************************************

class UgEvaluatableObject;
class Point3;

// This class defines the interface for accessing the data of a UG curve
// object or a UG edge object.
class OPENPPEXPORT Curve
{ 

    public:

        // Determine the equality of two Curve objects.  The two objects are
        // considered equal if the evaluator object of one curve is equal to
        // the evaluator object of the other curve.
        bool isEqual
        (
            const Curve *curve          // <I>
                                        // The Curve object to test for equality
                                        // against the invoking object.
        ) const;

        // Determine if the invoking object is a closed curve.
        bool isClosed ( ) const;

        // Return the start point in Absolute Coordinate System coordinates
        // of the invoking object.
        const Point3 askStartPoint ( ) const;

        // Return the end point in Absolute Coordinate System coordinates
        // of the invoking object.
        const Point3 askEndPoint ( ) const;
   
    protected:

        // Return the UgEvaluatableObject object that represents the invoking
        // object.
        virtual const UgEvaluatableObject *askEvaluatableObject ( ) const = 0;

        // Construct a Curve object
        Curve ( );

        // Destroy a Curve object
        virtual ~Curve ( );

    // The UgEdge class is a friend to allow the creation of Curve objects although
    // UgEdge is not derived from this class
    friend class UgEdge;

};

#undef EXPORTLIBRARY

#endif  // CURVE_INCLUDED
