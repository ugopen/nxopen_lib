/*
================================================================================

          Copyright (c) 1998-2000 Unigraphics Solutions Inc.
                    Unpublished - All rights reserved

================================================================================
  File description:

    Header file for Geometric Ellipse C++ class definitions.

================================================================================

*/

#ifndef ELLIPSE_INCLUDED
#define ELLIPSE_INCLUDED

// ****************************************************************************
// Include files for base classes and other needed types
// ****************************************************************************

#include <conic.hxx>
#include <libopenpp_exports.hxx>

// ****************************************************************************
// Forward declarations for classes
// ****************************************************************************
extern "C"
{
// 
typedef struct UF_EVAL_ellipse_s UF_EVAL_ellipse_t;
}

class CoordSys;

// This class defines the interface for accessing the data of a UG ellipse object
// or a UG edge object that is ellipical.  UG ellipse objects can be modified via
// the UgEllipse class, but UG edge objects with elliptical form cannot be modified.
class OPENPPEXPORT Ellipse : public Conic
{

    public:

        // Return the major radius of the invoking object.
        double getMajorRadius ( ) const;

        // Return the minor radius of the invoking object.
        double getMinorRadius ( ) const;

        // Return the start angle ( in radians ) of the invoking object.
        double getStartAngle ( ) const;

        // Return the end angle ( in radians ) of the invoking object.
        double getEndAngle ( ) const;

    protected:
    
        // Return all of the ellipse data of the invoking object via a UG/Open struct.
        const UF_EVAL_ellipse_t getEllipseDefinition ( ) const;

        // Construct an Ellipse object
        Ellipse ( );

        // Destroy an Ellipse object
        virtual ~Ellipse ( );

    private:

        // Return the coordinate system of the invoking object.  The origin
        // of the coordinate system defines the center of the ellipse in Absolute
        // Coordinate System coordinates.  The matrix of the coordinate system
        // defines the orientation of the ellipse in Absolute Coordinate System
        // coordinates.
        const CoordSys askCoordSys ( ) const;

};

#undef EXPORTLIBRARY

#endif  // ELLIPSE_INCLUDED
