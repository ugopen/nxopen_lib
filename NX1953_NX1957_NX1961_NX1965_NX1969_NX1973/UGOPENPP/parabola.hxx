/*
================================================================================

          Copyright (c) 1998-2000 Unigraphics Solutions Inc.
                    Unpublished - All rights reserved

================================================================================
  File description:

    Header file for Geometric Parabola C++ class definitions.

================================================================================

*/

#ifndef PARABOLA_INCLUDED
#define PARABOLA_INCLUDED

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
typedef struct UF_EVAL_parabola_s UF_EVAL_parabola_t;
}

class CoordSys;

// This class defines the interface for accessing the data of a UG parabola object
class OPENPPEXPORT Parabola : public Conic
{

    public:
       
        // Return the focal length of the invoking object.
        double getFocalLength ( ) const;

        // Return the minimum y value of the invoking object.
        double getMinimumY ( ) const;

        // Return the maximum y value of the invoking object.
        double getMaximumY ( ) const;
   
    protected:
    
        // Return all of the parabola data of the invoking object via a UG/Open struct.
        const UF_EVAL_parabola_t getParabolaDefinition ( ) const;

        // Construct a Parabola object
        Parabola ( );

        // Destroy a Parabola object
        virtual ~Parabola ( );

    private:

        // Return the coordinate system of the invoking object.  The origin
        // of the coordinate system defines the center of the parabola in Absolute
        // Coordinate System coordinates.  The matrix of the coordinate system
        // defines the orientation of the parabola in Absolute Coordinate System
        // coordinates.
        const CoordSys askCoordSys ( ) const;
        
};

#undef EXPORTLIBRARY

#endif  // PARABOLA_INCLUDED
