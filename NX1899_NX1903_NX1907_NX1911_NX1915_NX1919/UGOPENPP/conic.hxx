/*
================================================================================

          Copyright (c) 1998-2000 Unigraphics Solutions Inc.
                      Unpublished - All rights reserved

================================================================================
  File description:

    Header file for base Geometric Conic C++ class definitions.

================================================================================

*/

#ifndef CONIC_INCLUDED
#define CONIC_INCLUDED

// ****************************************************************************
// Include files for base classes and other needed types
// ****************************************************************************

#include <curve.hxx>
#include <libopenpp_exports.hxx>

// ****************************************************************************
// Forward declarations for classes
// ****************************************************************************

class CoordSys;
class Matrix3;
class Point3;

// This class defines the interface for accessing the data of a UG conic curve
// object, a UG circular edge object, or a UG elliptical edge object.
class OPENPPEXPORT Conic : public virtual Curve
{ 

    public:

        // Return the center point in Absolute Coordinate System coordinates
        // of the invoking object.
        const Point3 getCenterPoint ( ) const;

        // Return the orientation matrix in Absolute Coordinate System coordinates
        // of the invoking object.
        virtual const Matrix3 getMatrix ( ) const;

    protected:

        // Construct a Conic object
        Conic ( );

        // Destroy a Conic object
        virtual ~Conic ( );

    private:

        // Return the coordinate system of the invoking object.  The origin
        // of the coordinate system defines the center of the conic in Absolute
        // Coordinate System coordinates.  The matrix of the coordinate system
        // defines the orientation of the conic in Absolute Coordinate System
        // coordinates.
        virtual const CoordSys askCoordSys ( ) const = 0;

};

#undef EXPORTLIBRARY

#endif  // CONIC_INCLUDED
