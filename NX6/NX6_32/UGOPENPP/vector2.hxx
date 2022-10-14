/*
===========================================================================

          Copyright (c) 1998-2000 Unigraphics Solutions Inc.
                    Unpublished - All rights reserved

===========================================================================
  File description:

    Interface for the Vector2 class.

===========================================================================

*/

#ifndef VECTOR2_INCLUDED
#define VECTOR2_INCLUDED

// ****************************************************************************
// Include files for base classes and other needed types
// ****************************************************************************

#include <vector_constants.hxx>
#include <libvmathpp_exports.hxx>

// ****************************************************************************
// Forward declarations for classes
// ****************************************************************************

class Point2;
class Vector3;

//
// This class defines the data and interface of a 2D vector.
class VMATHPPEXPORT Vector2
{

    public:

        // Construct a vector with coordinates ( 0.0, 0.0 )
        Vector2 ( );
        
        // Construct a vector with coordinates ( x, y )
        Vector2
        (
            double x,           // The x coordinate of the vector
            double y            // The y coordinate of the vector
        );
        
        // Construct a vector with coordinates ( array [ 0 ], array [ 1 ] )
        Vector2
        (
            const double array [ 2 ]    // The x and y coordinates of the vector
        );

        // Destruct a vector
        virtual ~Vector2 ( );
        
        // Return the coordinates of the vector.  This is the operator used when the
        // invoking object is on the left side of the '=' in an assignment statement.
        // This operator allows the invoking object to be changed.
        double &operator[]
        (
            VectorMathCoordType index   // The specific vector coordinate to
                                        // return.  Valid values are: X or Y.
        );
        
        // Return the coordinates of the vector.  This is the operator used when the
        // invoking object is on the right side of the '=' in an assignment statement,
        // or when passing a const argument to a method or function.  This operator
        // does not allow the invoking object to be changed.
        const double &operator[]
        (
            VectorMathCoordType index   // The specific vector coordinate to
                                        // return.  Valid values are: X or Y.
        ) const;
        
        // Return the Vector2 sum of ( Vector2 + Vector2 ).  This operation 
        // adds two vectors and returns the new vector.
        const Vector2 operator+
        (
            const Vector2 &vector       // The second vector in the operation
                                        // ( Vector2 + Vector2 ).
        ) const;
        
        // Return a reference to the invoking Vector2 object after it has been
        // changed to be the sum of ( Vector2 + Vector2 ).  This operation 
        // adds two vectors and modifies the invoking Vector2 object to be that
        // vector.
        Vector2 &operator+=
        (
            const Vector2 &vector       // The second vector in the operation
                                        // ( Vector2 += Vector2 ).
        );
        
        // Return the Point2 sum of ( Vector2 + Point2 ).  This operation 
        // offsets the point by the vector and returns the new point.
        const Point2 operator+
        (
            const Point2 &point         // The point to offset in the operation
                                        // ( Vector2 + Point2 ).
        ) const;
        
        // Return the Vector2 difference of ( Vector2 - Vector2 ).  This operation 
        // subtracts one vector from another and returns the new vector.
        const Vector2 operator-
        (
            const Vector2 &vector       // The second vector in the operation
                                        // ( Vector2 - Vector2 ).
        ) const;
        
        // Return a reference to the invoking Vector2 object after it has been
        // changed to be the difference of ( Vector2 - Vector2 ).  This operation 
        // subtracts a vector from the invoking Vector2 object and modifies that
        // object to be that vector.
        Vector2 &operator-=
        (
            const Vector2 &vector       // The second vector in the operation
                                        // ( Vector2 -= Vector2 ).
        );
        
        // Return the Vector2 product of ( Vector2 * double ).  This operation 
        // multiplies each coordinate of the vector by the scale and returns
        // the new vector.
        const Vector2 operator*
        (
            double scale                // The scale factor.
        ) const;
        
        // Return a reference to the invoking Vector2 object after it has been
        // changed to be the product of ( Vector2 * double ).  This operation 
        // multiplies each coordinate of the invoking Vector2 object by the
        // scale.
        Vector2 &operator*=
        (
            double scale                // The scale factor.
        );
        
        // Return the Vector2 quotient of ( Vector2 / double ).  This operation 
        // divides each coordinate of the vector by the scale and returns
        // the new vector.
        const Vector2 operator/
        (
            double scale                // The scale factor.
        ) const;
        
        // Return a reference to the invoking Vector2 object after it has been
        // changed to be the quotient of ( Vector2 / double ).  This operation 
        // divides each coordinate of the invoking Vector2 object by the
        // scale.
        Vector2 &operator/=
        (
            double scale                // The scale factor.
        );
        
        // Return the Vector2 result of ( -Vector2 ).  This operation 
        // multiplies each coordinate of the vector by ( -1.0 ) and returns
        // the new vector.
        const Vector2 operator- ( ) const;
        
        // Return the dot product of two vectors.
        double dot
        (
            const Vector2 &vector       // <I>
                                        // The vector to dot against the invoking
                                        // Vector2 object.
        ) const;
        
        // Return the cross product of two vectors.
        double cross
        (
            const Vector2 &vector       // <I>
                                        // The vector to cross against the invoking
                                        // Vector2 object.
        ) const;
        
        // Return the magnitude of the invoking Vector2 object.
        double askMagnitude ( ) const;
        
        // Determine the equality of two vectors with a user-defined tolerance.
        // Two vectors are considered equal if the magnitude of the vector difference
        // between the two vectors is less than or equal to the specified tolerance.
        bool isEqual
        ( 
            const Vector2  &vector,     // <I>
                                        // The vector to test for equality against
                                        // the invoking object.
            double           tolerance  // <I>
                                        // The tolerance value used in the test
                                        // for equality of the vectors.
        ) const;
        
        // Determine the equality of two vectors with the system tolerance.
        // Two vectors are considered equal if the magnitude of the vector difference
        // between the two vectors is less than or equal to the system tolerance.
        bool operator==
        ( 
            const Vector2  &vector      // The vector to test for equality against
                                        // the invoking object.
        ) const;
        
        // Determine the inequality of two vectors with the system tolerance.
        // Two vectors are considered unequal if the magnitude of the vector difference
        // between the two vectors is greater than the system tolerance.
        bool operator!=
        ( 
            const Vector2  &vector      // The vector to test for inequality against
                                        // the invoking object.
        ) const;
        
        // Return a Vector2 object that is parallel to the invoking Vector2
        // object and has a magnitude of ( 1.0 ).  This method will throw the 
        // exception VectorMathZeroVector if the invoking Vector2 object has
        // a magnitude of ( 0.0 ).
        const Vector2 askUnit
        (
            double tolerance = VectorMathZeroTolerance
                                        // <I>
                                        // The tolerance value used in the test
                                        // for the magnitude of the invoking object
                                        // being ( 0.0 ).
        ) const;
        
        // Convert the invoking Vector2 object into a Point2 object and return
        // the point.  The x coordinate of the point is the x coordinate of
        // the vector, and the y coordinate of the point is the y coordinate of
        // the vector.
        const Point2 asPoint2 ( ) const;
        
        // Convert the invoking Vector2 object into a Vector3 object and return
        // the 3D vector.  The x coordinate of the 3D vector is the x coordinate of
        // the 2D vector, the y coordinate of the 3D vector is the y coordinate
        // of the 2D vector, and the z coordinate of the 3D vector is ( 0.0 ).
        const Vector3 asVector3 ( ) const;
        
        // Convert the invoking Vector2 object into a double array.  The element
        // array [ 0 ] is the x coordinate of the vector, and the element array [ 1 ]
        // is the y coordinate of the vector.
        void asArray
        (
            double array [ 2 ]          // <O>
                                        // The x and y coordinates of the vector
        ) const;
        
        // Determine the angle between the invoking Vector2 object and the given vector.
        // The returned angle ( in radians ) will range between greater than or equal to 
        // ( 0.0 ) and less than TwoPi.  The positive orientation for the angle is
        // determined by the vector cross product of the invoking Vector2 object 
        // with the input vector.
        double askAngle
        (
            const Vector2 &vector,      // <I>
                                        // The vector whose angular spread from the 
                                        // invoking Vector2 object is to be determined.
            double         tolerance = VectorMathZeroTolerance
                                        // <I>
                                        // A tolerance value used to test the vectors
                                        // for zero vectors and to test for ( 0.0 )
                                        // return angle.
        ) const;
        
        // Determine if the invoking Vector2 object is parallel to a given vector.
        // Two vectors are considerd parallel if the sine of the angle between the
        // two vectors is ( 0.0 ), or if the magnitude of either vector is equal to
        // ( 0.0 ).
        bool isParallel
        (
            const Vector2 &vector,      // <I>
                                        // The vector to test parallelism with the 
                                        // invoking Vector2 object.
            double         tolerance = VectorMathZeroTolerance
                                        // <I>
                                        // A tolerance value used to test for ( 0.0 )
                                        // values.
        ) const;
        
        // Determine if the invoking Vector2 object is perpendicular to a given vector.
        // Two vectors are considerd perpendicular if the cosine of the angle between
        // the two vectors is ( 0.0 ), or if the magnitude of either vector is equal to
        // ( 0.0 ).
        bool isPerpendicular
        (
            const Vector2 &vector,      // <I>
                                        // The vector to test perpendicularity with the 
                                        // invoking Vector2 object.
            double         tolerance = VectorMathZeroTolerance
                                        // <I>
                                        // A tolerance value used to test for ( 0.0 )
                                        // values.
        ) const;
        
        // Determine a vector that is perpendicular to the invoking Vector2 object and
        // return that Vector2 object.
        const Vector2 askPerpendicular ( ) const;
        
        // Determine the values ( *scalar1 ) and ( *scalar2 ) such that the invoking
        // Vector2 object is equal to ( *scalar1 ) * vec1 + ( *scalar2 ) * vec2.
        // Return false if the two component vectors are parallel and the invoking
        // Vector2 object is not parallel to either.  Return true otherwise.
        bool askComponents 
        (
            const Vector2 &vec1,    // <I>
                                    // First component vector of invoking Vector2 object
            const Vector2 &vec2,    // <I>
                                    // Second component vector of invoking Vector2 object
            double        *scalar1, // <O>
                                    // Scalar value for first component vector
            double        *scalar2, // <O>
                                    // Scalar value for second component vector
            double         tol = VectorMathZeroTolerance
                                    // <I>
                                    // Tolerance value to determine parallel vectors
        ) const;
        
        // Return a Vector2 object that is equal to the invoking Vector2
        // object rotated through an angle.
        const Vector2 rotate 
        (
            double ang              // <I>
                                    // The angle of rotation ( in radians )
        ) const;
        
    private:
        
        // The x coordinate of the Vector2 object
        double          m_x;
        
        // The y coordinate of the Vector2 object
        double          m_y;

    // The Point2 class is a friend to make use of vector coordinates
    // without requiring the Vector2::operator[] method.
    friend class Point2;

};

// Return the Vector2 product of ( double * Vector2 ).  This operation multiplies
// each coordinate of the vector by the scale and returns the new vector.
VMATHPPEXPORT const Vector2 operator*
(
    double          scale,           // The scale factor
    const Vector2  &vector           // The vector to scale
);

#undef EXPORTLIBRARY

#endif  // VECTOR2_INCLUDED
