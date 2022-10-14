/*
================================================================================

          Copyright (c) 1998-2000 Unigraphics Solutions Inc.
                    Unpublished - All rights reserved

================================================================================
  File description:

    Header file for Geometric Line C++ class definitions.

================================================================================

*/

#ifndef LINE_INCLUDED
#define LINE_INCLUDED

// ****************************************************************************
// Include files for base classes and other needed types
// ****************************************************************************

#include <curve.hxx>
#include <libopenpp_exports.hxx>

// ****************************************************************************
// Forward declarations for classes
// ****************************************************************************
extern "C"
{
// 
typedef struct UF_EVAL_line_s UF_EVAL_line_t;
}

// This class defines the interface for accessing the data of a UG line object
// or a UG edge object that is linear.  UG line objects can be modified via
// the UgLine class, but UG edge objects with linear form cannot be modified.
class OPENPPEXPORT Line : public virtual Curve
{

    public:

        // Return the start point in Absolute Coordinate System coordinates
        // of the invoking object.
        const Point3 getStartPoint ( ) const;

        // Return the end point in Absolute Coordinate System coordinates
        // of the invoking object.
        const Point3 getEndPoint ( ) const;

    protected:
    
        // Return all of the line data of the invoking object via a UG/Open struct.
        const UF_EVAL_line_t getLineDefinition ( ) const;

        // Construct a Line object
        Line ( );

        // Destroy a Line object
        virtual ~Line ( );

};

#undef EXPORTLIBRARY

#endif  // LINE_INCLUDED
