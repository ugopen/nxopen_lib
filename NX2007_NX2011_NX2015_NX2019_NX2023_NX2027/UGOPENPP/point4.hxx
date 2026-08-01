/*
===========================================================================

          Copyright (c) 1998-2000 Unigraphics Solutions Inc.
                    Unpublished - All rights reserved

===========================================================================
  File description:

    Interface for the Point4 class.

===========================================================================

*/

#ifndef POINT4_INCLUDED
#define POINT4_INCLUDED

// ****************************************************************************
// Include files for base classes and other needed types
// ****************************************************************************

#include <vector_constants.hxx>
#include <libvmathpp_exports.hxx>

// ****************************************************************************
// Forward declarations for classes
// ****************************************************************************

class Point3;

//
// This class defines the data and interface of a 4D position,
// which is represented as homogenous coordinates.  The 3D 
// position that is represented by a Point4 object can be 
// determined by dividing the coordinates by the weight.
class VMATHPPEXPORT Point4
{

    public:

        // Construct a Point4 object at ( 0.0, 0.0, 0.0, 1.0 ).
        Point4 ( );
        
        // Construct a Point4 object at ( x, y, z, weight ).
        Point4
        (
            double x,           // The x coordinate of the point
            double y,           // The y coordinate of the point
            double z,           // The z coordinate of the point
            double weight       // The weight coordinate of the point
        );
        
        // Construct a Point4 object at ( array [ 0 ], array [ 1 ], array [ 2 ], array [ 3 ] ).
        // 
        Point4
        (
            const double array [ 4 ]    // The x, y, z, and weight coordinates of
                                        // the point
        );
        
        // Construct a Point4 object at ( point [ X ] * weight, point [ Y ] * weight,
        // point [ Z ] * weight, weight ).
        // 
        Point4
        (
            const Point3  &point,           // The point to provide the x, y,
                                            // and z coordinates of the new point.
            double         weight = 1.0     // The weight coordinate of the point.
        );

        // Destroy a Point4 object.
        virtual ~Point4 ( );
        
        // Return a coordinate of the invoking object.  This is the operator used when the
        // invoking object is on the left side of the '=' in an assignment statement.
        // This operator allows the invoking object to be changed.
        double &operator[]
        (
            VectorMathCoordType index   // The specific point coordinate to
                                        // return.  Valid values are: X, Y, Z,
                                        // or W.
        );
        
        // Return a coordinate of the invoking object.  This is the operator used when the
        // invoking object is on the right side of the '=' in an assignment statement,
        // or when passing a const argument to a method or function.  This operator
        // does not allow the invoking object to be changed.
        const double &operator[]
        (
            VectorMathCoordType index   // The specific point coordinate to
                                        // return.  Valid values are: X, Y, Z,
                                        // or W.
        ) const;
        
        // Determine the equality of two points with a user-defined tolerance.
        // Two points are considered equal if the magnitude of a 4D vector
        // between the two points is less than or equal to the specified
        // tolerance.
        bool isEqual
        ( 
            const Point4  &point,       // <I>
                                        // The point to test for equality against
                                        // the invoking object.
            double         tolerance    // <I>
                                        // The tolerance value used in the test
                                        // for equality of the points.
        ) const;
        
        // Determine the equality of two points with the system tolerance.
        // Two points are considered equal if the magnitude of a 4D vector
        // between the two points is less than or equal to the system
        // tolerance.
        bool operator==
        ( 
            const Point4  &point        // The point to test for equality against
                                        // the invoking object.
        ) const;
        
        // Determine the inequality of two points with the system tolerance.
        // Two points are considered unequal if the magnitude of a 4D vector
        // between the two points is greater than the system tolerance.
        bool operator!=
        ( 
            const Point4  &point        // The point to test for inequality
                                        // against the invoking object.
        ) const;
        
        // Convert the invoking Point4 object into a Point3 object and return
        // the 3D point.  The x coordinate of the 3D point is the x coordinate of
        // the 4D point divided by its weight coordinate, the y coordinate of the
        // 3D point is the y coordinate of the 4D point divided by its weight
        // coordinate, and the z coordinate of the 3D point is the z coordinate of
        // the 4D point divided by its weight coordinate
        const Point3 asPoint3 ( ) const;
        
        // Convert the invoking Point4 object into a double array.  The element
        // array [ 0 ] is the x coordinate of the point, the element array [ 1 ]
        // is the y coordinate of the point, the element array [ 2 ] is the z coordinate
        // of the point, and the element array [ 3 ] is the weight coordinate of the 
        // point.
        void asArray
        (
            double array [ 4 ]          // <O>
                                        // The x, y, z, and weight coordinates of the
                                        // point
        ) const;
        
    private:
        
        // The x coordinate of the Point4 object.  This coordinate is the
        // x coordinate of a 3D point multiplied by the weight coordinate
        // of the 4D point.
        double         m_weight_x;
        
        // The y coordinate of the Point4 object.  This coordinate is the
        // y coordinate of a 3D point multiplied by the weight coordinate
        // of the 4D point.
        double         m_weight_y;
        
        // The z coordinate of the Point4 object.  This coordinate is the
        // z coordinate of a 3D point multiplied by the weight coordinate
        // of the 4D point.
        double         m_weight_z;
        
        // The weight coordinate of the Point4 object.
        double         m_weight;
        
};

#undef EXPORTLIBRARY

#endif  // POINT4_INCLUDED
