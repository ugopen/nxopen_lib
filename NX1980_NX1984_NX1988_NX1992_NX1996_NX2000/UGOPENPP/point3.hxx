/*
===========================================================================

          Copyright (c) 1998-2000 Unigraphics Solutions Inc.
                    Unpublished - All rights reserved

===========================================================================
  File description:

    Interface for the Point3 class.

===========================================================================

*/

#ifndef POINT3_INCLUDED
#define POINT3_INCLUDED

// ****************************************************************************
// Include files for base classes and other needed types
// ****************************************************************************

#include <vector_constants.hxx>
#include <libvmathpp_exports.hxx>

// ****************************************************************************
// Forward declarations for classes
// ****************************************************************************

class Vector3;
class Point2;
class Matrix3;

//
// This class defines the data and interface of a 3D position.
class VMATHPPEXPORT Point3
{

    public:

        // Construct a Point3 object at ( 0.0, 0.0, 0.0 ).
        Point3 ( );
        
        // Construct a Point3 object at ( x, y, z ).
        Point3
        (
            double x,           // The x coordinate of the point
            double y,           // The y coordinate of the point
            double z            // The z coordinate of the point
        );
        
        // Construct a Point3 object at ( array [ 0 ], array [ 1 ], array [ 2 ] ).
        // 
        Point3
        (
            const double array [ 3 ]    // The x, y, and z coordinates of the
                                        // point
        );

        // Destroy a Point3 object.
        virtual ~Point3 ( );
        
        // Return a coordinate of the invoking object.  This is the operator used when the
        // invoking object is on the left side of the '=' in an assignment statement.
        // This operator allows the invoking object to be changed.
        double &operator[]
        (
            VectorMathCoordType index   // The specific point coordinate to
                                        // return.  Valid values are: X, Y, or Z.
        );
        
        // Return a coordinate of the invoking object.  This is the operator used when the
        // invoking object is on the right side of the '=' in an assignment statement,
        // or when passing a const argument to a method or function.  This operator
        // does not allow the invoking object to be changed.
        const double &operator[]
        (
            VectorMathCoordType index   // The specific point coordinate to
                                        // return.  Valid values are: X, Y, or Z.
        ) const;
        
        // Return the Vector3 difference of ( Point3 - Point3 ).  This operation 
        // determines the vector that points from the first point to the 
        // second point and returns it.
        const Vector3 operator-
        (
            const Point3 &point         // The second point in the operation.
                                        // This point plus the returned vector
                                        // equals the first point.
        ) const;
        
        // Return the Point3 sum of ( Point3 + Vector3 ).  This operation 
        // offsets the point by adding the coordinates of the vector 
        // to the coordinates of the point and returns the new point.
        const Point3 operator+
        (
            const Vector3 &vector       // The vector whose coordinates are 
                                        // added to those of the point.
        ) const;
        
        // Return a reference to the invoking Point3 object after it has been
        // changed to be the sum of ( Point3 + Vector3 ).  This operation 
        // offsets the point by adding the coordinates of the vector 
        // to the coordinates of the point, and modifies the invoking Point3
        // object to be that point.
        Point3 &operator+=
        (
            const Vector3 &vector       // The vector whose coordinates are 
                                        // added to those of the point.
        );
        
        // Return the Point3 difference of ( Point3 - Vector3 ).  This operation 
        // offsets the point by subtracting the coordinates of the vector 
        // from the coordinates of the point and returns the new point.
        const Point3 operator-
        (
            const Vector3 &vector       // The vector whose coordinates are 
                                        // subtracted from those of the point.
        ) const;
        
        // Return a reference to the invoking Point3 object after it has been
        // changed to be the difference of ( Point3 - Vector3 ).  This operation 
        // offsets the point by subtracting the coordinates of the vector 
        // from the coordinates of the point, and modifies the invoking Point3
        // object to be that point.
        Point3 &operator-=
        (
            const Vector3 &vector       // The vector whose coordinates are 
                                        // subtracted from those of the point.
        );
        
        // Return the Point3 product of ( Point3 * double ).  This operation 
        // multiplies each coordinate of the point by the scale and returns
        // the new point.
        const Point3 operator*
        (
            double scale                // The scale factor.
        ) const;
        
        // Return a reference to the invoking Point3 object after it has been
        // changed to be the product of ( Point3 * double ).  This operation 
        // multiplies each coordinate of the invoking Point3 object by the
        // scale.
        Point3 &operator*=
        (
            double scale                // The scale factor.
        );
        
        // Return the Point3 product of ( Point3 * Matrix3 ).  This operation
        // rotates the point to the orientation defined by the matrix.
        const Point3 operator*
        (
            const Matrix3 &matrix       // The matrix used to rotate the point
        ) const;
        
        // Return a reference to the invoking Point3 object after it has been
        // changed to be the product of ( Point3 * Matrix3 ).  This operation 
        // rotates the point to the orientation defined by the matrix.
        Point3 &operator*=
        (
            const Matrix3 &matrix       // The matrix used to rotate the point
        );
        
        // Return the Point3 quotient of ( Point3 / double ).  This operation 
        // divides each coordinate of the point by the scale and returns
        // the new point.
        const Point3 operator/
        (
            double scale                // The scale factor.
        ) const;
        
        // Return a reference to the invoking Point3 object after it has been
        // changed to be the quotient of ( Point3 / double ).  This operation 
        // divides each coordinate of the invoking Point3 object by the scale.
        Point3 &operator/=
        (
            double scale                // The scale factor.
        );
        
        // Return the distance between the invoking Point3 object and the given
        // point.  The default argument provides the distance between the invoking
        // Point3 object and the origin.
        double askDistance
        (
            const Point3 &point = Point3 ( )
                                        // <I>
                                        // The point whose distance is to be
                                        // measured from the invoking Point3
                                        // object
        ) const;
        
        // Determine the equality of two points with a user-defined tolerance.
        // Two points are considered equal if the distance between the two points
        // is less than or equal to the specified tolerance.
        bool isEqual
        ( 
            const Point3  &point,       // <I>
                                        // The point to test for equality against
                                        // the invoking object.
            double         tolerance    // <I>
                                        // The tolerance value used in the test
                                        // for equality of the points.
        ) const;
        
        // Determine the equality of two points with the system tolerance.
        // Two points are considered equal if the distance between the two points
        // is less than or equal to the system tolerance.
        bool operator==
        ( 
            const Point3  &point        // The point to test for equality against
                                        // the invoking object.
        ) const;
        
        // Determine the inequality of two points with the system tolerance.
        // Two points are considered unequal if the distance between the two
        // points is greater than the system tolerance.
        bool operator!=
        ( 
            const Point3  &point        // The point to test for inequality
                                        // against the invoking object.
        ) const;
        
        // Convert the invoking Point3 object into a Vector3 object and return
        // the vector.  The x coordinate of the vector is the x coordinate of
        // the point, the y coordinate of the vector is the y coordinate of
        // the point, and the z coordinate of the vector is the z coordinate of
        // the point.
        const Vector3 asVector3 ( ) const;
        
        // Convert the invoking Point3 object into a Point2 object and return
        // the 2D point.  The x coordinate of the 2D point is the x coordinate of
        // the 3D point, and the y coordinate of the 2D point is the y coordinate
        // of the 3D point.
        const Point2 asPoint2 ( ) const;
        
        // Convert the invoking Point3 object into a double array.  The element
        // array [ 0 ] is the x coordinate of the point, the element array [ 1 ]
        // is the y coordinate of the point, and the element array [ 2 ] is the 
        // z coordinate of the point.
        void asArray
        (
            double array [ 3 ]          // <O>
                                        // The x, y, and z coordinates of the point
        ) const;
        
    private:
        
        // Determine the dot product between the invoking Point3 object and a
        // vector.  This method only makes sense in conjunction with the
        // multiplication of a point and a matrix which involves the dot product
        // of the point with the column vectors of the matrix.
        double dot
        (
            const Vector3 &vector           // <I>
                                            // The vector to dot with the point.
        ) const;    
        
        // The x coordinate of the Point3 object
        double         m_x;
        
        // The y coordinate of the Point3 object
        double         m_y;
        
        // The z-coordinate of the Point3 object
        double         m_z;

};

// Return the Point3 product of ( double * Point3 ).  This operation multiplies
// each coordinate of the point by the scale and returns the new point.
VMATHPPEXPORT const Point3 operator*
(
    double         scale,            // The scale factor
    const Point3  &point             // The point to scale
);

#undef EXPORTLIBRARY

#endif  // POINT3_INCLUDED
