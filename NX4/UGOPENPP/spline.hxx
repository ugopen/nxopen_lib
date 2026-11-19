/*
================================================================================

          Copyright (c) 1998-2000 Unigraphics Solutions Inc.
                    Unpublished - All rights reserved

================================================================================
  File description:

    Header file for Geometric Spline C++ class definitions.

================================================================================

*/

#ifndef SPLINE_INCLUDED
#define SPLINE_INCLUDED

// ****************************************************************************
// Include files for base classes and other needed types
// ****************************************************************************

#include <curve.hxx>
#include <ug_vector.hxx>
#include <point4.hxx>
#include <libopenpp_exports.hxx>

// ****************************************************************************
// Forward declarations for classes
// ****************************************************************************
extern "C"
{
// 
typedef struct UF_EVAL_spline_s UF_EVAL_spline_t;
}

// This class defines the interface for accessing the data of a UG spline object
// or a UG spline edge.  UG spline objects can be modified via the UgSpline class,
// but UG edge objects with spline form cannot be modified.
class OPENPPEXPORT Spline : public virtual Curve
{

    public:

        // Determine if the invoking object is a rational spline.
        bool isRational ( ) const;

        // Return the order of the invoking object.
        int getOrder ( ) const;

        // Return the knot sequence of the invoking object.
        const std::vector < double > getKnotSequence ( ) const;

        // Return the homogeneous control vertices of the invoking object.
        // The positions of the points are in Absolute Coordinate System coordinates.
        const std::vector < Point4 > getControlPoints ( ) const;

    protected:
    
        // Return all of the spline data of the invoking object via a UG/Open struct.
        const UF_EVAL_spline_t getSplineDefinition ( ) const;

        // Construct a Spline object
        Spline ( );

        // Destroy a Spline object
        virtual ~Spline ( );

};

#undef EXPORTLIBRARY

#endif  // SPLINE_INCLUDED
