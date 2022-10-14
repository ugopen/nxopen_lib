/*
================================================================================

          Copyright (c) 1998-2000 Unigraphics Solutions Inc.
                    Unpublished - All rights reserved

================================================================================
  File description:

    Header file for Geometric Hyperbola C++ class definitions.

================================================================================

*/

#ifndef HYPERBOLA_INCLUDED
#define HYPERBOLA_INCLUDED

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
typedef struct UF_EVAL_hyperbola_s UF_EVAL_hyperbola_t;
}

class CoordSys;

// This class defines the interface for accessing the data of a UG hyperbola object
class OPENPPEXPORT Hyperbola : public Conic
{

    public:

        // Return the length along the semi transverse axis of the invoking object.
        double getSemiTransverseLength ( ) const;

        // Return the length along the semi conjugate axis of the invoking object.
        double getSemiConjugateLength ( ) const;

        // Return the minimum y value of the invoking object.
        double getMinimumY ( ) const;

        // Return the maximum y value of the invoking object.
        double getMaximumY ( ) const;

    protected:
    
        // Return all of the hyperbola data of the invoking object via a UG/Open struct.
        const UF_EVAL_hyperbola_t getHyperbolaDefinition ( ) const;

        // Construct a Hyperbola object
        Hyperbola ( );

        // Destroy a Hyperbola object
        virtual ~Hyperbola ( );

    private:

        // Return the coordinate system of the invoking object.  The origin
        // of the coordinate system defines the center of the hyperbola in Absolute
        // Coordinate System coordinates.  The matrix of the coordinate system
        // defines the orientation of the hyperbola in Absolute Coordinate System
        // coordinates.
        const CoordSys askCoordSys ( ) const;

};

#undef EXPORTLIBRARY

#endif  // HYPERBOLA_INCLUDED
