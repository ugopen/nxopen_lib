/*
===========================================================================

          Copyright (c) 1998-2000 Unigraphics Solutions Inc.
                    Unpublished - All rights reserved

===========================================================================
  File description:

    Interface for the Vector3 class.

===========================================================================

*/

#ifndef VECTOR3_INCLUDED
#define VECTOR3_INCLUDED

// ****************************************************************************
// Include files for base classes and other needed types
// ****************************************************************************

#include <vector_constants.hxx>
#include <libvmathpp_exports.hxx>

// ****************************************************************************
// Forward declarations for classes
// ****************************************************************************

class Vector2;
class Point3;
class Matrix3;

//
// This class defines the data and interface of a 3D vector
class VMATHPPEXPORT Vector3
{

    public:

        // Construct a vector with coordinates ( 0.0, 0.0, 0.0 )
        Vector3 ( );
        
        // Construct a vector with coordinates ( x, y, z )
        Vector3
        (
            double x,           // The x coordinate of the vector
            double y,           // The y coordinate of the vector
            double z            // The z coordinate of the vector
        );
        
        // Construct a vector with coordinates ( array [ 0 ], array [ 1 ], array [ 2 ] )
        Vector3
        (
            const double array [ 3 ]    // The x, y, and z coordinates of the vector
        );

        // Destruct a vector
        virtual ~Vector3 ( );
        
        // Return the coordinates of the vector.  This is the operator used when the
        // invoking object is on the left side of the '=' in an assignment statement.
        // This operator allows the invoking object to be changed.
        double &operator[]
        (
            VectorMathCoordType index   // The specific vector coordinate to
                                        // return.  Valid values are: X, Y, or Z.
        );
        
        // Return the coordinates of the vector.  This is the operator used when the
        // invoking object is on the right side of the '=' in an assignment statement,
        // or when passing a const argument to a method or function.  This operator
        // does not allow the invoking object to be changed.
        const double &operator[]
        (
            VectorMathCoordType index   // The specific vector coordinate to
                                        // return.  Valid values are: X, Y, or Z.
        ) const;
        
        // Return the Vector3 sum of ( Vector3 + Vector3 ).  This operation 
        // adds two vectors and returns the new vector.
        const Vector3 operator+
        (
            const Vector3 &vec3         // The second vector in the operation
                                        // ( Vector3 + Vector3 ).
        ) const;
        
        // Return a reference to the invoking Vector3 object after it has been
        // changed to be the sum of ( Vector3 + Vector3 ).  This operation 
        // adds two vectors and modifies the invoking Vector3 object to be that
        // vector.
        Vector3 &operator+=
        (
            const Vector3 &vec3         // The second vector in the operation
                                        // ( Vector3 += Vector3 ).
        );
        
        // Return the Point3 sum of ( Vector3 + Point3 ).  This operation 
        // offsets the point by the vector and returns the new point.
        const Point3 operator+
        (
            const Point3 &pnt3          // The point to offset in the operation
                                        // ( Vector3 + Point3 ).
        ) const;
        
        // Return the Vector3 difference of ( Vector3 - Vector3 ).  This operation 
        // subtracts one vector from another and returns the new vector.
        const Vector3 operator-
        (
            const Vector3 &vec3         // The second vector in the operation
                                        // ( Vector3 - Vector3 ).
        ) const;
        
        // Return a reference to the invoking Vector3 object after it has been
        // changed to be the difference of ( Vector3 - Vector3 ).  This operation 
        // subtracts a vector from the invoking Vector3 object and modifies that
        // object to be that vector.
        Vector3 &operator-=
        (
            const Vector3 &vec3         // The second vector in the operation
                                        // ( Vector3 -= Vector3 ).
        );
        
        // Return the Vector3 product of ( Vector3 * double ).  This operation 
        // multiplies each coordinate of the vector by the scale and returns
        // the new vector.
        const Vector3 operator*
        (
            double scale                // The scale factor.
        ) const;
        
        // Return a reference to the invoking Vector3 object after it has been
        // changed to be the product of ( Vector3 * double ).  This operation 
        // multiplies each coordinate of the invoking Vector3 object by the
        // scale.
        Vector3 &operator*=
        (
            double scale                // The scale factor.
        );
        
        // Return the Vector3 product of ( Vector3 * Matrix3 ).  This operation
        // rotates the vector to the orientation defined by the matrix.
        const Vector3 operator*
        (
            const Matrix3 &matrix       // The matrix used to rotate the vector
        ) const;
        
        // Return a reference to the invoking Vector3 object after it has been
        // changed to be the product of ( Vector3 * Matrix3 ).  This operation 
        // rotates the vector to the orientation defined by the matrix.
        Vector3 &operator*=
        (
            const Matrix3 &matrix       // The matrix used to rotate the vector
        );
        
        // Return the Vector3 quotient of ( Vector3 / double ).  This operation 
        // divides each coordinate of the vector by the scale and returns
        // the new vector.
        const Vector3 operator/
        (
            double scale                // The scale factor.
        ) const;
        
        // Return a reference to the invoking Vector3 object after it has been
        // changed to be the quotient of ( Vector3 / double ).  This operation 
        // divides each coordinate of the invoking Vector3 object by the
        // scale.
        Vector3 &operator/=
        (
            double scale                // The scale factor.
        );
        
        // Return the Vector3 result of ( -Vector3 ).  This operation 
        // multiplies each coordinate of the vector by ( -1.0 ) and returns
        // the new vector.
        const Vector3 operator- ( ) const;
        
        // Return the dot product of two vectors.
        double dot
        (
            const Vector3 &vec3         // <I>
                                        // The vector to dot against the invoking
                                        // Vector3 object.
        ) const;
        
        // Return the Vector3 object that is the cross product of two vectors.
        const Vector3 cross
        (
            const Vector3 &vec3         // <I>
                                        // The vector to cross against the invoking
                                        // Vector3 object.
        ) const;
        
        // Return the magnitude of the invoking Vector3 object.
        double askMagnitude ( ) const;
        
        // Determine the equality of two vectors with a user-defined tolerance.
        // Two vectors are considered equal if the magnitude of the vector difference
        // between the two vectors is less than or equal to the specified tolerance.
        bool isEqual
        ( 
            const Vector3  &vec3,       // <I>
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
            const Vector3  &vec3        // The vector to test for equality against
                                        // the invoking object.
        ) const;
        
        // Determine the inequality of two vectors with the system tolerance.
        // Two vectors are considered unequal if the magnitude of the vector difference
        // between the two vectors is greater than the system tolerance.
        bool operator!=
        ( 
            const Vector3  &vec3        // The vector to test for inequality against
                                        // the invoking object.
        ) const;
        
        // Return a Vector3 object that is parallel to the invoking Vector3
        // object and has a magnitude of ( 1.0 ).  This method will throw the 
        // exception VectorMathZeroVector if the invoking Vector3 object has
        // a magnitude of ( 0.0 ).
        const Vector3 askUnit
        (
            double tolerance = VectorMathZeroTolerance
                                        // <I>
                                        // The tolerance value used in the test
                                        // for the magnitude of the invoking object
                                        // being ( 0.0 ).
        ) const;
        
        // Convert the invoking Vector3 object into a Point3 object and return
        // the point.  The x coordinate of the point is the x coordinate of
        // the vector, the y coordinate of the point is the y coordinate of
        // the vector, and the z coordinate of the point is the z coordinate of
        // the vector.
        const Point3 asPoint3 ( ) const;
        
        // Convert the invoking Vector3 object into a Vector2 object and return
        // the 2D vector.  The x coordinate of the 2D vector is the x coordinate of
        // the 3D vector, and the y coordinate of the 2D vector is the y coordinate
        // of the 3D vector.
        const Vector2 asVector2 ( ) const;
        
        // Convert the invoking Vector3 object into a double array.  The element
        // array [ 0 ] is the x coordinate of the vector, the element array [ 1 ]
        // is the y coordinate of the vector, and the element array [ 2 ] is the z 
        // coordinate of the vector.
        void asArray
        (
            double array [ 3 ]          // <O>
                                        // The x, y, and z coordinates of the vector
        ) const;
        
        // Determine the angle between the invoking Vector3 object and the given vector.
        // The returned angle ( in radians ) will range between greater than or equal to 
        // ( 0.0 ) and less than TwoPi.  The positive orientation for the angle is
        // determined by the vector cross product of the invoking Vector3 object 
        // with the input vector.
        double askAngle
        (
            const Vector3 &vec3,        // <I>
                                        // The vector whose angular spread from the 
                                        // invoking Vector3 object is to be determined.
            double         tolerance = VectorMathZeroTolerance
                                        // <I>
                                        // A tolerance value used to test the vectors
                                        // for zero vectors and to test for ( 0.0 )
                                        // return angle.
        ) const;
        
        // Determine the angle between the invoking Vector3 object and the given vector.
        // The returned angle ( in radians ) will range between greater than or equal to 
        // ( 0.0 ) and less than TwoPi.  The positive orientation for the angle is
        // determined by comparing the input orientation vector with the vector cross
        // product of the invoking Vector3 object with the input vector.  If the dot
        // product is positive, the vector cross product determines the orientation;
        // if the dot product is negative, the negative of the vector cross product
        // determines the orientation.
        double askAngle
        (
            const Vector3 &vec3,        // <I>
                                        // The vector whose angular spread from the 
                                        // invoking Vector3 object is to be determined.
            const Vector3 &orient,      // <I>
                                        // Vector used to determine the positive orientation
                                        // for the returned angle.
            double         tolerance = VectorMathZeroTolerance
                                        // <I>
                                        // A tolerance value used to test the vectors
                                        // for zero vectors and to test for ( 0.0 )
                                        // return angle.
        ) const;
        
        // Determine if the invoking Vector3 object is parallel to a given vector.
        // Two vectors are considerd parallel if the sine of the angle between the
        // two vectors is ( 0.0 ), or if the magnitude of either vector is equal to
        // ( 0.0 ).
        bool isParallel
        (
            const Vector3 &vec3,        // <I>
                                        // The vector to test parallelism with the 
                                        // invoking Vector3 object.
            double         tolerance = VectorMathZeroTolerance
                                        // <I>
                                        // A tolerance value used to test for ( 0.0 )
                                        // values.
        ) const;
        
        // Determine if the invoking Vector3 object is perpendicular to a given vector.
        // Two vectors are considerd perpendicular if the cosine of the angle between
        // the two vectors is ( 0.0 ), or if the magnitude of either vector is equal to
        // ( 0.0 ).
        bool isPerpendicular
        (
            const Vector3 &vec3,        // <I>
                                        // The vector to test perpendicularity with the 
                                        // invoking Vector3 object.
            double         tolerance = VectorMathZeroTolerance
                                        // <I>
                                        // A tolerance value used to test for ( 0.0 )
                                        // values.
        ) const;
        
        // Determine a vector that is perpendicular to the invoking Vector3 object and
        // return that Vector3 object.  This method does not guarantee any other 
        // relationship between the returned object and the invoking object.
        const Vector3 askPerpendicular ( ) const;
        
    private:
        
        // The x coordinate of the Vector3 object
        double         m_x;
        
        // The y coordinate of the Vector3 object
        double         m_y;
        
        // The z coordinate of the Vector3 object
        double         m_z;
    
    // The Matrix3 class is a friend to make use of vector coordinates
    // without requiring the Vector3::operator[] method.
    friend class Matrix3;

    // The Point3 class is a friend to make use of vector coordinates
    // without requiring the Vector3::operator[] method.
    friend class Point3;

};

// Return the Vector3 product of ( double * Vector3 ).  This operation multiplies
// each coordinate of the vector by the scale and returns the new vector.
VMATHPPEXPORT const Vector3 operator*
(
    double          scale,           // The scale factor
    const Vector3  &vec3             // The vector to scale
);

#undef EXPORTLIBRARY

#endif  // VECTOR3_INCLUDED
