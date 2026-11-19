/*
===========================================================================

          Copyright (c) 1998-2000 Unigraphics Solutions Inc.
                    Unpublished - All rights reserved

===========================================================================
  File description:

    Interface for the Point2 class.

===========================================================================

*/

#ifndef POINT2_INCLUDED
#define POINT2_INCLUDED

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

//
// This class defines the data and interface of a 2D position
class VMATHPPEXPORT Point2
{

    public:

        // Construct a point at ( 0.0, 0.0 )
        Point2 ( );
        
        // Construct a point at ( x, y )
        Point2
        (
            double x,           // The x coordinate of the point
            double y            // The y coordinate of the point
        );
        
        // Construct a point at ( array [ 0 ], array [ 1 ] )
        Point2
        (
            const double array [ 2 ]    // The x and y coordinates of the point
        );

        // Destruct a point
        virtual ~Point2 ( );
        
        // Return the coordinates of the point.  This is the operator used when the
        // invoking object is on the left side of the '=' in an assignment statement.
        // This operator allows the invoking object to be changed.
        double &operator[]
        (
            VectorMathCoordType index   // The specific point coordinate to
                                        // return.  Valid values are: X or Y.
        );
        
        // Return the coordinates of the point.  This is the operator used when the
        // invoking object is on the right side of the '=' in an assignment statement,
        // or when passing a const argument to a method or function.  This operator
        // does not allow the invoking object to be changed.
        const double &operator[]
        (
            VectorMathCoordType index   // The specific point coordinate to
                                        // return.  Valid values are: X or Y.
        ) const;
        
        // Return the Vector2 difference of ( Point2 - Point2 ).  This operation 
        // determines the vector that points from the first point to the 
        // second point and returns it.
        const Vector2 operator-
        (
            const Point2 &point         // The second point in the operation.
                                        // This point plus the returned vector
                                        // equals the first point.
        ) const;
        
        // Return the Point2 sum of ( Point2 + Vector2 ).  This operation 
        // offsets the point by adding the coordinates of the vector 
        // to the coordinates of the point and returns the new point.
        const Point2 operator+
        (
            const Vector2 &vector       // The vector whose coordinates are 
                                        // added to those of the point.
        ) const;
        
        // Return a reference to the invoking Point2 object after it has been
        // changed to be the sum of ( Point2 + Vector2 ).  This operation 
        // offsets the point by adding the coordinates of the vector 
        // to the coordinates of the point, and modifies the invoking Point2
        // object to be that point.
        Point2 &operator+=
        (
            const Vector2 &vector       // The vector whose coordinates are 
                                        // added to those of the point.
        );
        
        // Return the Point2 difference of ( Point2 - Vector2 ).  This operation 
        // offsets the point by subtracting the coordinates of the vector 
        // from the coordinates of the point and returns the new point.
        const Point2 operator-
        (
            const Vector2 &vector       // The vector whose coordinates are 
                                        // subtracted from those of the point.
        ) const;
        
        // Return a reference to the invoking Point2 object after it has been
        // changed to be the difference of ( Point2 - Vector2 ).  This operation 
        // offsets the point by subtracting the coordinates of the vector 
        // from the coordinates of the point, and modifies the invoking Point2
        // object to be that point.
        Point2 &operator-=
        (
            const Vector2 &vector       // The vector whose coordinates are 
                                        // subtracted from those of the point.
        );
        
        // Return the Point2 product of ( Point2 * double ).  This operation 
        // multiplies each coordinate of the point by the scale and returns
        // the new point.
        const Point2 operator*
        (
            double scale                // The scale factor.
        ) const;
             
        // Return a reference to the invoking Point2 object after it has been
        // changed to be the product of ( Point2 * double ).  This operation 
        // multiplies each coordinate of the invoking Point2 object by the
        // scale.
        Point2 &operator*=
        (
            double scale                // The scale factor.
        );
        
        // Return the Point2 quotient of ( Point2 / double ).  This operation 
        // divides each coordinate of the point by the scale and returns
        // the new point.
        const Point2 operator/
        (
            double scale                // The scale factor.
        ) const;
        
        // Return a reference to the invoking Point2 object after it has been
        // changed to be the quotient of ( Point2 / double ).  This operation 
        // divides each coordinate of the invoking Point2 object by the scale.
        Point2 &operator/=
        (
            double scale                // The scale factor.
        );
        
        // Return the distance of the invoking Point2 object from the given point.
        double askDistance
        (
            const Point2 &point = Point2 ( )
                                        // <I>
                                        // The point whose distance is to be
                                        // measured from the invoking Point2
                                        // object
        ) const;
        
        // Determine the equality of two points with a user-defined tolerance.
        // Two points are considered equal if the distance between the two points
        // is less than or equal to the specified tolerance.
        bool isEqual
        ( 
            const Point2  &point,       // <I>
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
            const Point2  &point        // The point to test for equality against
                                        // the invoking object.
        ) const;
        
        // Determine the inequality of two points with the system tolerance.
        // Two points are considered unequal if the distance between the two
        // points is greater than the system tolerance.
        bool operator!=
        ( 
            const Point2  &point        // The point to test for inequality against
                                        // the invoking object.
        ) const;
        
        // Convert the invoking Point2 object into a Vector2 object and return
        // the vector.  The x coordinate of the vector is the x coordinate of
        // the point, and the y coordinate of the vector is the y coordinate of
        // the point.
        const Vector2 asVector2 ( ) const;
        
        // Convert the invoking Point2 object into a Point3 object and return
        // the 3D point.  The x coordinate of the 3D point is the x coordinate of
        // the 2D point, the y coordinate of the 3D point is the y coordinate
        // of the 2D point, and the z coordinate of the 3D point is ( 0.0 ).
        const Point3 asPoint3 ( ) const;
        
        // Convert the invoking Point2 object into a double array.  The element
        // array [ 0 ] is the x coordinate of the point, and the element array [ 1 ]
        // is the y coordinate of the point.
        void asArray
        (
            double array [ 2 ]          // <O>
                                        // The x and y coordinates of the point
        ) const;
        
    private:
        
        // The x coordinate of the Point2 object
        double          m_x;
        
        // The y coordinate of the Point2 object
        double          m_y;
};

// Return the Point2 product of ( double * Point2 ).  This operation multiplies
// each coordinate of the point by the scale and returns the new point.
VMATHPPEXPORT const Point2 operator*
(
    double         scale,            // The scale factor
    const Point2  &point             // The point to scale
);

#undef EXPORTLIBRARY

#endif  // POINT2_INCLUDED
