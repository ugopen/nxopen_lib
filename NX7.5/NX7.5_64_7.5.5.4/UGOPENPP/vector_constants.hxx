/*
===========================================================================

          Copyright (c) 1998-2000 Unigraphics Solutions Inc.
                    Unpublished - All rights reserved

===========================================================================
  File description:

    Header file for basic Vector Mathematical constants

===========================================================================

*/

#ifndef VECTOR_CONSTANTS_INCLUDED
#define VECTOR_CONSTANTS_INCLUDED

//  The constant that represents the value Pi
const double    Pi                      = 3.14159265358979324;

//  The constant that represents the value ( 2.0 * Pi )
const double    TwoPi                   = 2.0 * Pi;

//  The constant that represents the default zero tolerance
//  used by the Vector Math classes.  If two double values
//  differ by the tolerance value or less, then those two
//  double values are considered to be equal.  If a tolerance
//  value is not specified, or the default tolerance is
//  implied, this is the value that is used.
const double    VectorMathZeroTolerance = 1.0e-10;

//  This function converts a measure in radians and returns
//  the corresponding measure in degrees.
inline double convertRadiansToDegrees
(
    double radians          // <I>
                            // The radian measure
);

//  This function converts a measure in degrees and returns
//  the corresponding measure in radians.
inline double convertDegreesToRadians
(
    double degrees          // <I>
                            // The degree measure
);

//  Enum passed as an argument for the operator[] functions.
//  The value specifies just what is being asked of the object. 
enum VectorMathCoordType
{
    X,      //  Return the X coordinate of a point or vector,
            //  or the X direction vector of a matrix.
    Y,      //  Return the Y coordinate of a point or vector,
            //  or the Y direction vector of a matrix.
    Z,      //  Return the Z coordinate of a point or vector,
            //  or the Z direction vector of a matrix.
    W       //  Return the weight of a Point4 object.
};

// ****************************************************************************
// Implementation for global functions
// ****************************************************************************

// ****************************************************************************
// ****************************************************************************
// Do *_NOT_* rely on implementation details of the functions!  The function
// implementation may change in the future.  Confine yourself to the public
// declarations.
// ****************************************************************************
// ****************************************************************************

inline double convertRadiansToDegrees ( double radians )
{
    return ( ( radians * 180.0 ) / Pi );
}

inline double convertDegreesToRadians ( double degrees )
{
    return ( ( degrees * Pi ) / 180.0 );
}

#endif  // VECTOR_CONSTANTS_INCLUDED
