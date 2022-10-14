/*
===========================================================================

          Copyright (c) 1998-2000 Unigraphics Solutions Inc.
                    Unpublished - All rights reserved

===========================================================================
  File description:

    Header file for basic Vector Mathematical exceptions

===========================================================================

*/

#ifndef VECTOR_EXCEPTION_INCLUDED
#define VECTOR_EXCEPTION_INCLUDED

// ****************************************************************************
// Include files for base classes and other needed types
// ****************************************************************************

#include <vector_constants.hxx>
#include <libvmathpp_exports.hxx>

// This class defines the base class for all Vector Math exception classes.
// An object of this class will never be thrown directly, but this class may be used
// to catch any exception thrown by a Vector Math method.
class VMATHPPEXPORT VectorMathException
{

    public:

        // Destruct a VectorMathException object
        virtual ~VectorMathException ( );

    protected:

        // Construct a VectorMathException object
        VectorMathException ( );

};

// This class defines the object that will be thrown by any Vector Math operator[]
// method that is passed an invalid input for the invoking object.  E.g., passing
// the index 'W' to the Vector2::operator[] method will throw this exception.
class VMATHPPEXPORT VectorMathBadIndex : public VectorMathException
{

    public:

        // Construct a VectorMathBadIndex object
        VectorMathBadIndex
        (
            VectorMathCoordType index   // The index argument from the operator[]
                                        // method that caused the exception.
        );

        // Destruct a VectorMathBadIndex object
        virtual ~VectorMathBadIndex ( );

        // Return the index that caused the exception from an operator[] method
        VectorMathCoordType askIndex ( ) const;
        
    private:
        
        // The index value that caused the exception to be thrown from an
        // operator[] method.
        VectorMathCoordType     m_index;

};

// This class defines the object that will be thrown by any Vector Math vector
// method that cannot be invoked by a vector with a magnitude of ( 0.0 ) ( i.e.,
// Vector3::unit ), or by any Vector Math method that cannot accept as an input
// argument a vector with a magnitude of ( 0.0 ) ( i.e., certain Matrix3 contructors ).
class VMATHPPEXPORT VectorMathZeroVector : public VectorMathException
{

    public:

        // Construct a VectorMathZeroVector object
        VectorMathZeroVector ( );

        // Destruct a VectorMathZeroVector object
        virtual ~VectorMathZeroVector ( );

};

// This class defines the object that will be thrown by any Matrix3 constructor
// that is passed two vectors that are not perpendicular.
class VMATHPPEXPORT VectorMathNonOrthogonal : public VectorMathException
{
    
    public:

        // Construct a VectorMathNonOrthogonal object
        VectorMathNonOrthogonal ( );

        // Destruct a VectorMathNonOrthogonal object
        virtual ~VectorMathNonOrthogonal ( );

};

#undef EXPORTLIBRARY

#endif  // VECTOR_EXCEPTION_INCLUDED
