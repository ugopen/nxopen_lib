/*
===========================================================================

          Copyright (c) 1998-2000 Unigraphics Solutions Inc.
                    Unpublished - All rights reserved

===========================================================================
  File description:

    Interface for the Matrix3 class.

===========================================================================

*/

#ifndef MATRIX3_INCLUDED
#define MATRIX3_INCLUDED

// ****************************************************************************
// Include files for base classes and other needed types
// ****************************************************************************

#include <vector_constants.hxx>
#include <vector3.hxx>
#include <libvmathpp_exports.hxx>

// ****************************************************************************
// Forward declarations for classes
// ****************************************************************************

class Point3;


// This class defines the data and interface of a 3X3 matrix.
// Each instance of this class represents a right-hand matrix that consists
// of 3 column vectors representing the x, y, and z direction, respectively,
// of an orientation in space.  Every matrix is guaranteed to be ortho-normal,
// which means that the direction vectors of the matrix are all unit vectors,
// and that each direction vector is perpendicular to every other direction
// vector.  If an object of this class has a x direction vector of 
// ( 1.0, 0.0, 0.0 ), a y direction vector of ( 0.0, 1.0, 0.0 ) and a z
// direction vector of ( 0.0, 0.0, 1.0 ), that object is referred to as
// the Identity Matrix.
class VMATHPPEXPORT Matrix3 {

    public:

        // Determines the direction vector that is being passed to the 
        // Matrix3 constructor that accepts a single direction vector.
        enum OneVectorInput 
        {
            X_Input,    // Create matrix specifying the x direction vector
            Y_Input,    // Create matrix specifying the y direction vector
            Z_Input     // Create matrix specifying the z direction vector
        };

        // Determines which two direction vectors are being passed to the
        // Matrix3 constructor that accepts two direction vectors.
        enum TwoVectorInput
        {
            XY_Input,   // Create matrix specifying the x & y direction vectors
            YZ_Input,   // Create matrix specifying the y & z direction vectors
            ZX_Input    // Create matrix specifying the z & x direction vectors
        };

        // Construct a Matrix3 object that is the Identity Matrix.
        Matrix3 ( );
        
        // Construct a Matrix3 object from an array.
        explicit Matrix3
        (
            const double array [ 9 ]    // An array that is compatible to
                                        // the matrix arrays that Open API functions
                                        // use.
        );
        
        // Construct a Matrix3 object that is the rotation matrix that revolves through
        // an angle about a vector.
        Matrix3
        (
            double         angle,       // Angle ( in radians ) that defines the
                                        // amount of revolution in the matrix.
            const Vector3 &vector       // Vector defining the axis of revolution.
                                        // The argument need not be a unit vector,
                                        // but if it is a zero vector, then the
                                        // Identity Matrix is constructed.
        );
        
        // Construct a Matrix3 object from the roll, pitch, and yaw angles
        Matrix3
        (
            double roll,                // Roll angle ( in radians )
            double pitch,               // Pitch angle ( in radians )
            double yaw                  // Yaw angle ( in radians )
        );
        
        // Construct a Matrix3 object from a single vector.  This constructor does
        // not uniquely define the matrix, as there is a degree of freedom
        // that is not specified.
        Matrix3 
        (
            OneVectorInput   input,     // Specifies the significance of the vector
                                        // used to create the matrix.
            const Vector3   &vector     // Single vector used to define the matrix.
                                        // The argument need not be a unit vector,
                                        // but if it is a zero vector, then the
                                        // exception VectorMathZeroVector will be
                                        // thrown.
        );
        
        // Construct a Matrix3 object from two orthogonal vectors.  This constructor
        // uniquely defines the matrix.
        Matrix3
        (
            TwoVectorInput   input,     // Specifies the significance of the two
                                        // vectors used to create the matrix.  The
                                        // exception VectorMathNonOrthogonal will
                                        // be thrown if the two vectors are not
                                        // orthogonal.
            const Vector3    &vector1,  // First vector used to define the matrix.
                                        // The argument need not be a unit vector,
                                        // but if it is a zero vector, then the
                                        // exception VectorMathZeroVector will be
                                        // thrown.
            const Vector3    &vector2   // Second vector used to define the matrix.
                                        // The argument need not be a unit vector,
                                        // but if it is a zero vector, then the
                                        // exception VectorMathZeroVector will be
                                        // thrown.
        );

        // Destroy a Matrix3 object.
        virtual ~Matrix3 ( );
        
        // Return a direction vector of the invoking object.
        const Vector3 operator[]
        (
            VectorMathCoordType index   // The specific direction vector to 
                                        // return.  Valid values are: X, Y,
                                        // or Z.
        ) const;
        
        // Return the Matrix3 product of ( Matrix3 * Matrix3 ).  This operation
        // concatenates two rotations into a single matrix.
        const Matrix3 operator*
        (
            const Matrix3 &matrix       // The second matrix in the operation
                                        // ( Matrix3 * Matrix3 ).
        ) const;
        
        // Return a reference to the invoking Matrix3 object after it has
        // been changed to be the product of ( Matrix3 * Matrix3 ).  This operation
        // concatenates two rotations into a single matrix, and modifies
        // the invoking Matrix3 object to be that matrix.
        Matrix3& operator*=
        (
            const Matrix3 &matrix       // The second matrix in the operation
                                        // ( Matrix3 =* Matrix3 ).
        );
        
        // Determine the equality of two matrices with a user-defined
        // tolerance.  Two matrices are considered equal if all of the column
        // vectors of one matrix are equal to the corresponding column vectors
        // of the other matrix within the specified tolerance.
        bool isEqual
        (
            const Matrix3  &matrix,     // <I>
                                        // The matrix to test for equality
                                        // against the invoking object.
            double          tolerance   // <I>
                                        // The tolerance value used in the test
                                        // for equality of the matrices.
        ) const;
        
        // Determine the equality of two matrices with the system
        // tolerance.  Two matrices are considered equal if all of the column
        // vectors of one matrix are equal to the corresponding column vectors
        // of the other matrix within the system tolerance.
        bool operator==
        (
            const Matrix3  &matrix      // The matrix to test for equality
                                        // against the invoking object.
        ) const;
        
        // Determine the inequality of two matrices with the system
        // tolerance.  Two matrices are considered unequal if any of the column
        // vectors of one matrix is unequal to the corresponding column vector
        // of the other matrix within the system tolerance.
        bool operator!=
        (
            const Matrix3  &matrix      // The matrix to test for inequality
                                        // against the invoking object.
        ) const;
        
        // Return the roll, pitch, yaw angles of the invoking matrix.
        void askRollPitchYaw
        (
            double *roll,               // <O>
                                        // The roll angle ( in radians )
            double *pitch,              // <O>
                                        // The pitch angle ( in radians )
            double *yaw                 // <O>
                                        // The yaw angle ( in radians )
        ) const;
        
        // Return the transpose of the invoking matrix.  The transpose matrix
        // has a x direction vector equal to the top row vector of the invoking
        // matrix, AND a y direction vector equal to the middle row vector of
        // the invoking matrix, AND a z direction vector equal to the bottom
        // row vector of the invoking matrix.
        const Matrix3 transpose ( ) const;
        
        // Convert the matrix to a 9 element double array
        void asArray
        (
            double array [ 9 ]          // <O>
                                        // An array that is compatible to
                                        // the matrix arrays that Open API functions
                                        // use.
        ) const;
        
        // Return the determinant of the invoking matrix.
        double askDeterminant ( ) const;
        
    private:
        
        // The X direction vector of the matrix
        Vector3         m_x_vector;
        
        // The Y direction vector of the matrix
        Vector3         m_y_vector;
        
        // The Z direction vector of the matrix
        Vector3         m_z_vector;

        // Return the top row vector of the matrix.
        const Vector3 askTopVector ( ) const;

        // Return the middle row vector of the matrix.
        const Vector3 askMiddleVector ( ) const;

        // Return the bottom row vector of the matrix.
        const Vector3 askBottomVector ( ) const;

        // A private constructor never meant to be used.  It is defined
        // to avoid the situation where the contructor
        // Matrix3 ( TwoVectorsInput, const Vector3 &vector ) is attempted.  This
        // private constuctor prevents the input argument in the above instance
        // from being converted to a double and having the constructor 
        // Matrix3 ( double, const Vector3 &vector ) invoked.
        Matrix3 
        (
            int            input,       // An integer value
            const Vector3 &vector       // A vector
        );
        
        // Return true if the matrix passes the ortho-normal criteria, false
        // otherwise.
        bool isOrthoNormal ( ) const;
        
        // Return true if the matrix is not ortho-normal, false otherwise.
        // The invoking matrix is guaranteed to be ortho-normal when this
        // method returns.
        bool orthoNormalize ( );
        
        // Method used in the ortho-normal processing.  This method
        // reconstructs a matrix that is not ortho-normal, and makes it ortho-
        // normal.
        void reconstructMatrix
        (
            bool massage_axes       // <I>
                                    // Invoke adjustAxes method if true before
                                    // ortho-normalizing the matrix
        );
        
        // Method used in the ortho-normal processing.  This method examines
        // the individual direction vectors of the matrix and sets small vector
        // coordinates ( to within zero tolerance ) to 0.0
        bool adjustAxes ( );
        
        // Initialize matrix from 3 orthogonal unit direction vectors
        void initialize
        (
            const Vector3 &x_vector,    // <I>
                                        // x direction vector
            const Vector3 &y_vector,    // <I>
                                        // y direction vector
            const Vector3 &z_vector     // <I>
                                        // z direction vector
        );
        
        // Initialize a matrix from two orthogonal vectors, using the cross
        // product of the input vectors to form the third.
        void initialize
        (
            TwoVectorInput   input,     // <I>
                                        // Specifies the significance of the two
                                        // vectors used to create the matrix.  The
                                        // exception VectorMathNonOrthogonal will
                                        // be thrown if the two vectors are not
                                        // orthogonal.
            const Vector3    &vector1,  // <I>
                                        // First vector used to define the matrix.
                                        // The argument need not be a unit vector,
                                        // but if it is a zero vector, then the
                                        // exception VectorMathZeroVector will be
                                        // thrown.
            const Vector3    &vector2   // <I>
                                        // Second vector used to define the matrix.
                                        // The argument need not be a unit vector,
                                        // but if it is a zero vector, then the
                                        // exception VectorMathZeroVector will be
                                        // thrown.
        );

        
        // A helper class for Matrix3.  An instance of this class contains
        // the sign/cosine pair for one of the direction angles ( roll, pitch,
        // yaw ) used to construct a matrix.
        class TrigValues {
            
            public:
            
                // Construct a TrigValues object from an angle.
                explicit TrigValues
                (
                    double angle = 0.0      // The constructing angle ( in radians )
                );
                
                // Construct a TrigValues object from the given sine and cosine.
                // If the input values do not obey the trigonometric equality,
                // they will be adjusted to correspond to a valid sine/cosine
                // pair.
                TrigValues
                (
                    double cosine,          // The cosine value
                    double sine             // The sine value
                );

                // Destroy a TrigValues object.
                virtual ~TrigValues ( );
                
                // Edit the sine and cosine values of the invoking object.
                // If the input values do not obey the trigonometric equality,
                // they will be adjusted to correspond to a valid sine/cosine
                // pair.
                void set
                (
                    double cosine,          // <I>
                                            // The cosine value
                    double sine             // <I>
                                            // The sine value
                );
                
                // Return the cosine of the invoking object.
                double askCosine ( ) const;
                
                // Return the sine of the invoking object.
                double askSine ( ) const;
                
                // Return the angle that corresponds to the sine and cosine of the 
                // invoking object.
                double askAngle ( ) const;
                
            private:
                
                // The cosine of the TrigValues object.
                double      m_cosine;
                
                // The sine of the TrigValues object.
                double      m_sine;
                
                // Insure that the invoking object contains valid values to
                // within the specified tolerance.  If the sine and cosine
                // values do not obey the trigonometric equality, they will be
                // adjusted to correspond to a valid sine/cosine pair.
                void validate
                (
                    double tolerance = VectorMathZeroTolerance
                                        // <I>
                                        // The tolerance value used in the test
                                        // for the trigonometric equality of 
                                        // sine/cosine pair.
                );
                
        };
        
        // Return the sine/cosine pairs for the roll, pitch, and yaw angles of
        // the matrix.
        void askAngleCosines
        (
            TrigValues   *roll,     // <O>
                                    // Sine/cosine pair of roll angle
            TrigValues   *pitch,    // <O>
                                    // Sine/cosine pair of pitch angle
            TrigValues   *yaw       // <O>
                                    // Sine/cosine pair of yaw angle
        ) const;
        
        // Initialize matrix from the sine/cosine pairs for the roll, pitch,
        // and yaw angles.
        void initialize
        (
            const TrigValues   &roll,   // <I>
                                        // Sine/cosine pair of roll angle
            const TrigValues   &pitch,  // <I>
                                        // Sine/cosine pair of pitch angle
            const TrigValues   &yaw     // <I>
                                        // Sine/cosine pair of yaw angle
        );

};

#undef EXPORTLIBRARY

#endif  // MATRIX3_INCLUDED
