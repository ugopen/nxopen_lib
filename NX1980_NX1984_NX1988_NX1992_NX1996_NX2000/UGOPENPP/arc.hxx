/*
================================================================================

          Copyright (c) 1998-2000 Unigraphics Solutions Inc.
                    Unpublished - All rights reserved

================================================================================
  File description:

    Header file for Geometric Arc C++ class definitions.

================================================================================

*/

#ifndef ARC_INCLUDED
#define ARC_INCLUDED

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
typedef struct UF_EVAL_arc_s UF_EVAL_arc_t;
}

class CoordSys;

// This class defines the interface for accessing the data of a UG arc object
// or a UG edge object that is circular.  UG arc objects can be modified via
// the UgArc class, but UG edge objects with circular form cannot be modified.
class OPENPPEXPORT Arc : public Conic
{

    public:

        // Return the radius of the invoking object.
        double getRadius ( ) const;

        // Return the start angle ( in radians ) of the invoking object.
        double getStartAngle ( ) const;

        // Return the end angle ( in radians ) of the invoking object.
        double getEndAngle ( ) const;

    protected:
    
        // Return all of the arc data of the invoking object via a UG/Open struct.
        const UF_EVAL_arc_t getArcDefinition ( ) const;

        // Construct an Arc object
        Arc ( );

        // Destroy an Arc object
        virtual ~Arc ( );

    private:

        // Return the coordinate system of the invoking object.  The origin
        // of the coordinate system defines the center of the arc in Absolute
        // Coordinate System coordinates.  The matrix of the coordinate system
        // defines the orientation of the arc in Absolute Coordinate System
        // coordinates.
        const CoordSys askCoordSys ( ) const;

};

#undef EXPORTLIBRARY

#endif  // ARC_INCLUDED
