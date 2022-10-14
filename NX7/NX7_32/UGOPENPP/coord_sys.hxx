/*
===========================================================================

          Copyright (c) 1998-2000 Unigraphics Solutions Inc.
                    Unpublished - All rights reserved

===========================================================================
  File description:

    Interface for the CoordSys class.

===========================================================================

*/

#ifndef COORD_SYS_INCLUDED
#define COORD_SYS_INCLUDED

// ****************************************************************************
// Include files for base classes and other needed types
// ****************************************************************************

#include <vector_constants.hxx>
#include <matrix3.hxx>
#include <point3.hxx>
#include <libvmathpp_exports.hxx>

//
// This class defines the data and interface of a Coordinate System
// that is composed of a 3D point that represents the origin of the
// coordinate system and a 3X3 matrix that represents the orientation
// of the coordinate system.  If an object of this class has an origin
// of ( 0.0, 0.0, 0.0 ) and an orientation of the Identity Matrix,
// that object is referred to as the Absolute Coordinate System.  ( For
// a definition of "Identity Matrix", see the overview for the Matrix3
// class. )
class VMATHPPEXPORT CoordSys
{

    public:

        // Construct a CoordSys object at ( 0.0, 0.0, 0.0 ) with the identity
        // matrix as the orientation.  The resulting Coordinate System is the
        // Absolute Coordinate System.
        CoordSys ( );
        
        // Construct a CoordSys object at the specified point with the identity
        // matrix as the orientation. 
        CoordSys
        (
            const Point3 &point     // The point in Absolute Coordinate System
                                    // coordinates that defines the origin of
                                    // the Coordinate System.
        );
        
        // Construct a CoordSys object at ( 0.0, 0.0, 0.0 ) with the specified
        // matrix as the orientation. 
        CoordSys
        (
            const Matrix3 &matrix   // The matrix in Absolute Coordinate System
                                    // coordinates that defines the orientation
                                    // of the Coordinate System.
        );
        
        // Construct a CoordSys object at the specified point with the specified
        // matrix as the orientation. 
        CoordSys
        (
            const Point3  &point,   // The point in Absolute Coordinate System
                                    // coordinates that defines the origin of
                                    // the Coordinate System.
            const Matrix3 &matrix   // The matrix in Absolute Coordinate System
                                    // coordinates that defines the orientation
                                    // of the Coordinate System.
        );

        // Destroy a CoordSys object.
        virtual ~CoordSys ( );
        
        // Return the point in Absolute Coordinate System coordinates that 
        // represents the origin of the Coordinate System
        const Point3 getOrigin ( ) const;
        
        // Edit the origin of the Coordinate System
        void setOrigin
        (
            const Point3 &point     // <I>
                                    // The point in Absolute Coordinate System
                                    // coordinates that re-defines the origin of
                                    // the Coordinate System.
        );
        
        // Return the matrix in Absolute Coordinate System coordinates that
        // represents the orientation of the Coordinate System
        const Matrix3 getMatrix ( ) const;
        
        // Edit the orientation matrix of the Coordinate System
        void setMatrix
        (
            const Matrix3 &matrix   // <I>
                                    // The matrix in Absolute Coordinate System
                                    // coordinates that re-defines the orientation
                                    // of the Coordinate System.
        );
        
        // Map a point in the coordinates of the Coordinate System represented
        // by the invoking object to the coordinates of another Coordinate System.
        const Point3 map
        (
            const Point3   &point,  // <I>
                                    // The point in Coordinate System coordinates
                                    // of the invoking object.
            const CoordSys &csys = CoordSys ( )   
                                    // <I>
                                    // The Coordinate System to map the point to.
                                    // Use of the default argument implies that the
                                    // point will be mapped to the Absolute 
                                    // Coordinate System.
        ) const;
        
        // Map a vector in the coordinates of the Coordinate System represented
        // by the invoking object to the coordinates of another Coordinate System.
        const Vector3 map
        (
            const Vector3  &vector, // <I>
                                    // The vector in Coordinate System coordinates
                                    // of the invoking object.
            const CoordSys &csys = CoordSys ( )   
                                    // <I>
                                    // The Coordinate System to map the vector to.
                                    // Use of the default argument implies that the
                                    // vector will be mapped to the Absolute 
                                    // Coordinate System.
        ) const;
        
        // Determine the equality of two Coordinate Systems with a user-defined
        // tolerance.  Two Coordinate Systems are considered equal if the origin
        // of one Coordinate System is equal to the origin of the other 
        // Coordinate System within the specified tolerance, AND the orientation
        // of one Coordinate System is equal to the orientation of the other
        // Coordinate System within the specified tolerance.
        bool isEqual
        (
            const CoordSys &csys,   // <I>
                                    // The Coordinate System to test for equality
                                    // against the invoking object.
            double          tolerance
                                    // <I>
                                    // The tolerance value used in the test for 
                                    // equality of the Coordinate Systems.
        ) const;
        
        // Determine the equality of two Coordinate Systems with the system
        // tolerance.  Two Coordinate Systems are considered equal if the origin
        // of one Coordinate System is equal to the origin of the other 
        // Coordinate System within the system tolerance, AND the orientation
        // of one Coordinate System is equal to the orientation of the other
        // Coordinate System within the system tolerance.
        bool operator==
        (
            const CoordSys &csys    // The Coordinate System to test for equality
                                    // against the invoking object.
        ) const;
        
        // Determine the inequality of two Coordinate Systems with the system
        // tolerance.  Two Coordinate Systems are considered unequal if the origin
        // of one Coordinate System is unequal to the origin of the other 
        // Coordinate System within the system tolerance, OR the orientation
        // of one Coordinate System is unequal to the orientation of the other
        // Coordinate System within the system tolerance.
        bool operator!=
        (
            const CoordSys &csys    // The Coordinate System to test for inequality
                                    // against the invoking object.
        ) const;
        
    private:
        
        // Point in Absolute Coordinate System coordinates that defines
        // the origin of the Coordinate System
        Point3          m_point;
        
        // Matrix in Absolute Coordinate System coordinates that defines
        // the orientation of the Coordinate System
        Matrix3         m_matrix;
        
        // Map a point in Absolute Coordinate System coordinates to 
        // the Coordinate System represented by the invoking object.
        const Point3 mapFromABS
        (
            const Point3 &point     // <I>
                                    // The point in Absolute Coordinate System
                                    // coordinates.
        ) const;
        
        // Map a vector in Absolute Coordinate System coordinates to 
        // the Coordinate System represented by the invoking object.
        const Vector3 mapFromABS
        (
            const Vector3 &vector   // <I>
                                    // The vector in Absolute Coordinate System
                                    // coordinates.
        ) const;
        
        // Map a point in the coordinates of the Coordinate System represented
        // by the invoking object to Absolute Coordinate System coordinates.
        const Point3 mapToABS
        (
            const Point3 &point     // <I>
                                    // The point in Coordinate System coordinates
                                    // of the invoking object.
        ) const;
        
        // Map a vector in the coordinates of the Coordinate System represented
        // by the invoking object to Absolute Coordinate System coordinates.
        const Vector3 mapToABS
        (
            const Vector3 &vector   // <I>
                                    // The vector in Coordinate System coordinates
                                    // of the invoking object.
        ) const;

};

#undef EXPORTLIBRARY

#endif  // COORD_SYS_INCLUDED
