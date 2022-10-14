/****************************************************************************
             Copyright (c) 1995-2000 Unigraphics Solutions, Inc.
                       Unpublished - All Rights Reserved                       

* 


 
   File Description:
     The routines in this chapter enable you to perform matrix operations
     such as copy, add, multiply matrices, calculate determinants, obtain
     an identity matrix, obtain the transpose of a matrix, etc. Matrix
     operations can be performed on 2 x 2, 3 x 3, and 4 x 4 matrices.
     The names of the matrix functions describe the dimension of the matrix.
     For example, functions of the form UF_MTX2_<name> apply to 2 x 2 matrices.

     Having a strong math background before using these functions is encouraged.  
     An example of call sequences can be found in the ugopen kits under 
        SampleNXOpenApplications->C++->BlockStyler->MatrixOperations.

     More examples can be found in these Solutions Center articles:
        Sample Open C API program : rotate copy selected csys about a specified axis  
        Sample Open C API program : rotate copy selected csys about one of its own axes  

     
     See Also: 

****************************************************************************/

#ifndef UF_MTX_H_INCLUDED
#define UF_MTX_H_INCLUDED


/***************************************************************************

****************************************************************************/


#include <uf_defs.h>
#include <libufun_exports.h>

#ifdef __cplusplus
extern "C" {
#endif

/***************************************************************************
Copies the 2x2 matrix elements from the source matrix to the
destination matrix

Return: void

Environment: Internal  and  External
See Also:
History:
****************************************************************************/
extern UFUNEXPORT void UF_MTX2_copy(
    const double   mtx_src[4],      /* <I>
                                    Source matrix 
                                    */
          double   mtx_dst[4]       /* <O>
                                    Destination matrix mtx_dst = mtx_src 
                                    */
);/* <NEC> */ 

/***************************************************************************
Calculates the determinant of a 2 x 2 matrix.

Return: void
Environment: Internal  and  External
See Also:
History:
****************************************************************************/
extern UFUNEXPORT void  UF_MTX2_determinant(
const double mtx[4] ,/* <I>
                     Matrix whose determinant in required
                     */
double * determinant  /* <O>
                      Matrix determinant
                      */
);/* <NEC> */ 

/***************************************************************************
Returns a 2 x 2 identity matrix.

Return: void

Environment: Internal  and  External
See Also:
History:
****************************************************************************/
extern UFUNEXPORT void  UF_MTX2_identity(
double identity_mtx[4]  /* <O>
                        Identity matrix
                        */
);/* <NEC> */ 

/***************************************************************************
Returns a matrix formed from two input vectors.

Return:
         Return value:
        0 = Success (vectors define a valid matrix)
        1 = Matrix cannot be defined

Environment: Internal  and  External
See Also:
History:
****************************************************************************/
extern UFUNEXPORT int UF_MTX2_initialize(
const double x_vec[2] ,/* <I>
                       Vector for the X-direction of matrix
                       */
const double y_vec[2] ,/* <I>
                       Vector for the Y-direction of matrix
                       */
double mtx[4]  /* <O>
               Matrix
               */
);

/***************************************************************************
Returns a 2x2 matrix product from two input matrices.

Return: void
Environment: Internal  and  External
See Also:
History:
****************************************************************************/
extern UFUNEXPORT void UF_MTX2_multiply(
const double mtx1[4] ,/* <I>
                      Matrix #1
                      */
const double mtx2[4] ,/* <I>
                      Matrix #2
                      */
double mtx_product[4]  /* <O>
                       Matrix product
                         mtx_product = mtx1 X mtx2
                       */
);/* <NEC> */ 

/***************************************************************************
Returns a 2x2 matrix product by transposing matrix #1 before
performing the multiplication.
Return: void
Environment: Internal  and  External
See Also:
History:
****************************************************************************/
extern UFUNEXPORT void UF_MTX2_multiply_t(
const double mtx1[4] ,/* <I>
                      Matrix #1 gets transposed before the
                      multiplication.
                      */
const double mtx2[4] ,/* <I>
                      Matrix #2
                      */
double mtx_product[4]  /* <O>
                       Matrix product
                       mtx_product = Transpose of mtx1 X mtx2
                       */
);/* <NEC> */ 

/***************************************************************************
Returns the transpose of a 2x2 matrix.
Return: void
Environment: Internal  and  External
See Also:
History:
****************************************************************************/
extern UFUNEXPORT void UF_MTX2_transpose(
const double mtx[4] ,/* <I>
                     Matrix to transpose
                     */
double transpose_mtx[4]  /* <O>
                         Transpose of the input matrix
                         */
);/* <NEC> */ 

/***************************************************************************
Returns a 2D vector which is the product of a 2D vector and a 2x2
matrix.

Return: void
Environment: Internal  and  External
See Also:
History:
****************************************************************************/
extern UFUNEXPORT void UF_MTX2_vec_multiply(
const double vec[2] ,/* <I>
                     Vector to multiply
                     */
const double mtx[4] ,/* <I>
                     Matrix to multiply
                     */
double vec_product[2]  /* <O>
                       Product (a vector)
                       vec_product = vec X mtx
                       */
);/* <NEC> */ 

/***************************************************************************
Returns a 2D vector which is the product of a 2D vector and a
transposed 2x2 matrix.

Return: void
Environment: Internal  and  External
See Also:
History:
****************************************************************************/
extern UFUNEXPORT void UF_MTX2_vec_multiply_t(
const double vec[2] ,/* <I>
                     Vector to multiply
                     */
const double mtx[4] ,/* <I>
                     Matrix to transpose and multiply
                     */
double vec_product[2]  /* <O>
                       Product (a vector)
                        vec_product = vec X transpose of mtx
                       */
);/* <NEC> */ 

/***************************************************************************
Returns the X-direction vector of a 2x2 matrix.

Return: void
Environment: Internal  and  External
See Also:
History:
****************************************************************************/
extern UFUNEXPORT void UF_MTX2_x_vec(
const double mtx[4] ,/* <I>
                     Matrix whose X-direction is required
                     */
double x_vec[2]  /* <O>
                 X-direction vector of the matrix
                 */
);/* <NEC> */ 

/***************************************************************************
Returns the Y-direction vector of a 2x2 matrix.

Return: void
Environment: Internal  and  External
See Also:
History:
****************************************************************************/
extern UFUNEXPORT void UF_MTX2_y_vec(
const double mtx[4] ,/* <I>
                     Matrix whose Y-direction is required
                     */
double y_vec[2]  /* <O>
                 Y-direction vector of the matrix
                 */
);/* <NEC> */ 

/****************************************************************************
*
*   Prototypes of functions used to initialize, access, and manipulate
*   3D matrices.
*
*****************************************************************************/


/***************************************************************************
Copies the matrix elements from a source 3x3 matrix to a destination 3x3
matrix.

Return: void
Environment: Internal  and  External
See Also:
History:
****************************************************************************/
extern UFUNEXPORT void  UF_MTX3_copy(
const double mtx_src[9] ,/* <I>
                         Source matrix
                         */
double mtx_dst[9]  /* <O>
                   Destination matrix
                   */
);/* <NEC> */ 

/***************************************************************************
Calculates the determinant of a  3 x 3 matrix.

Return: void
Environment: Internal  and  External
See Also:
History:
****************************************************************************/
extern UFUNEXPORT void  UF_MTX3_determinant(
const double mtx[9] ,/* <I>
                     Matrix whose determinant in required
                     */
double * determinant  /* <O>
                      Matrix determinant
                      */
);/* <NEC> */ 

/***************************************************************************
Returns a 3 x 3 identity matrix.

Return: void
Environment: Internal  and  External
See Also:
History:
****************************************************************************/
extern UFUNEXPORT void  UF_MTX3_identity(
double identity_mtx[9]  /* <O>
                        Identity Matrix
                        */
);/* <NEC> */ 

/***************************************************************************
Returns a 3x3 matrix formed from two input 3D vectors. The two
input vectors are normalized and the y-direction vector is made
orthogonal to the x-direction vector before taking the cross product
(x_vec X  y_vec) to generate the z-direction vector.

Return:
         Return value:
        0 = Success (vectors define a valid matrix)
        1 = Matrix cannot be defined

Environment: Internal  and  External
See Also:
History:
****************************************************************************/
extern UFUNEXPORT int UF_MTX3_initialize(
const double x_vec[3] ,/* <I>
                       Vector for the X-direction of matrix
                       */
const double y_vec[3] ,/* <I>
                       Vector for the Y-direction of matrix
                       */
double mtx[9]  /* <O>
               Matrix
               */
);

/***************************************************************************
Returns a 3x3 matrix with the given X-direction vector and having
arbitrary Y- and Z-direction vectors.

Return:
         Returns 0 if the input vector is nonzero; returns 1
         otherwise.

Environment: Internal  and  External
See Also:
History:
****************************************************************************/
extern UFUNEXPORT int UF_MTX3_initialize_x(
const double x_vec[3] ,/* <I>
                       Vector for the X-direction of matrix
                       */
double mtx[9]  /* <O>
               Matrix (3x3)
               */
);

/***************************************************************************
Returns a 3x3 matrix with the given Z-direction vector and having
arbitrary X- and Y-direction vectors.

Return:
         Returns 0 if the input vector is nonzero; 
         returns 1 otherwise.

Environment: Internal  and  External
See Also:
History:
****************************************************************************/
extern UFUNEXPORT int UF_MTX3_initialize_z(
const double z_vec[3] ,/* <I>
                       Vector for the Z-direction of matrix
                       */
double mtx[9]  /* <O>
               Matrix (3x3)
               */
);

/***************************************************************************
Converts a 3D matrix to a 4D matrix with a scale of 1.0 and a zero
translation vector.

Return: void
Environment: Internal  and  External
See Also:
History:
****************************************************************************/
extern UFUNEXPORT void UF_MTX3_mtx4(
const double mtx_3D[9] ,/* <I>
                        3D matrix
                        */
double mtx_4D[16]  /* <O>
                   4D matrix
                   */
);

/***************************************************************************
Returns a 3x3 matrix product from two input matrices.

Return: void
Environment: Internal  and  External
See Also:
History:
****************************************************************************/
extern UFUNEXPORT void UF_MTX3_multiply(
const double mtx1[9] ,/* <I>
                      Matrix #1
                      */
const double mtx2[9] ,/* <I>
                      Matrix #2
                      */
double mtx_product[9]  /* <O>
                       Matrix product
                       mtx_product = mtx1 X mtx2
                       */
);/* <NEC> */ 

/***************************************************************************
Returns a 3x3 matrix product by transposing the first matrix before
performing the multiplication.

Return: void
Environment: Internal  and  External
See Also:
History:
****************************************************************************/
extern UFUNEXPORT void UF_MTX3_multiply_t(
const double mtx1[9] ,/* <I>
                      Matrix #1 gets transposed before the multiplication.
                      */
const double mtx2[9] ,/* <I>
                      Matrix #2
                      */
double mtx_product[9]  /* <O>
                       Matrix product
                       mtx_product = trns(mtx1) X  mtx2
                       */
);/* <NEC> */ 

/***************************************************************************
Returns a 3x3 matrix whose direction vectors are orthogonal and of
unit length.

Return: void
Environment: Internal  and  External
See Also:
History:
****************************************************************************/
extern UFUNEXPORT void UF_MTX3_ortho_normalize(
double mtx[9] /* <I/O>
               Matrix to be ortho-normalized. (Input)
               Ortho-normalized matrix. (Output)
               */
);/* <NEC> */ 

/***************************************************************************
Returns a 3x3 rotation matrix about an axis and through a specified
angle of rotation.

Return: void
Environment: Internal  and  External
See Also:
History:
****************************************************************************/
extern UFUNEXPORT void UF_MTX3_rotate_about_axis(
const double rotation_axis[3] ,/* <I>
                               Vector of the rotation axis
                               */
double rotation_angle ,/* <I>
                       Angle of the rotation (in radians)
                       */
double mtx[9]  /* <O>
               Rotation Matrix
               */
);/* <NEC> */ 

/***************************************************************************
Returns the transpose of a  3x3 matrix.

Return: void
Environment: Internal  and  External
See Also:
History:
****************************************************************************/
extern UFUNEXPORT void UF_MTX3_transpose(
const double mtx[9] ,/* <I>
                     Matrix to transpose
                     */
double transpose_mtx[9]  /* <O>
                         Transposed matrix
                         transpose_mtx = trns(mtx) 
                         */
);/* <NEC> */ 

/***************************************************************************
Returns a vector which is the product of a 3D vector and a 3x3 matrix.

Return: void
Environment: Internal  and  External
See Also:
History:
****************************************************************************/
extern UFUNEXPORT void UF_MTX3_vec_multiply(
const double vec[3] ,/* <I>
                     Vector to multiply
                     */
const double mtx[9] ,/* <I>
                     Matrix to multiply
                     */
double vec_product[3]  /* <O>
                       Product (a vector)
                       vec_product = vec X mtx
                       */
);/* <NEC> */ 

/***************************************************************************
Returns a vector which is the product of a 3D vector and a transposed
3x3 matrix.

Return: void
Environment: Internal  and  External
See Also:
History:
****************************************************************************/
extern UFUNEXPORT void UF_MTX3_vec_multiply_t(
const double vec[3] ,/* <I>
                     Vector to multiply
                     */
const double mtx[9] ,/* <I>
                     Matrix to transpose and multiply
                     */
double vec_product[3]  /* <O>
                       Product (a vector)
                       vec_product = vec X trns(mtx)
                       */
);/* <NEC> */ 

/***************************************************************************
Returns the X-direction vector of a matrix.

Return: void
Environment: Internal  and  External
See Also:
History:
****************************************************************************/
extern UFUNEXPORT void UF_MTX3_x_vec(
const double mtx[9] ,/* <I>
                     3x3 Matrix whose X-direction is required
                     */
double x_vec[3]  /* <O>
                 X-direction vector of the matrix
                 */
);/* <NEC> */ 

/***************************************************************************
Returns the Y-direction vector of a 3x3 matrix.

Return: void
Environment: Internal  and  External
See Also:
History:
****************************************************************************/
extern UFUNEXPORT void UF_MTX3_y_vec(
const double mtx[9] ,/* <I>
                     Matrix whose Y-direction is required
                     */
double y_vec[3]  /* <O>
                 Y-direction vector of the matrix
                 */
);/* <NEC> */ 

/***************************************************************************
Returns the Z-direction vector of a 3x3 matrix.

Return: void
Environment: Internal  and  External
See Also:
History:
****************************************************************************/
extern UFUNEXPORT void UF_MTX3_z_vec(
const double mtx[9] ,/* <I>
                     Matrix whose Z-direction is required
                     */
double z_vec[3]  /* <O>
                 Z-direction vector of the matrix
                 */
);/* <NEC> */ 

/*****************************************************************************
*
*   Prototypes of functions used to initialize, access, and manipulate
*   4D matrices.
*
 ******************************************************************************/

/*****************************************************************************
Returns the 3x3 rotation matrix of a 4x4 matrix.

Return: void
Environment: Internal  and  External
See Also:
History:
*****************************************************************************/
extern UFUNEXPORT void UF_MTX4_ask_rotation(
const double mtx_4D[16] ,/* <I>
                         4x4 matrix whose rotation is required
                         */
double mtx_3D[9]  /* <O>
                  3x3 rotation matrix of the 4x4 matrix
                  */
);/* <NEC> */ 

/*****************************************************************************
Returns the scale factor of a 4x4 matrix.

Return: void
Environment: Internal  and  External
See Also:
History:
*****************************************************************************/
extern UFUNEXPORT void UF_MTX4_ask_scale(
const double mtx[16] ,/* <I>
                      Matrix whose scale is required.
                      */
double * scale  /* <O>
                Scale factor of the matrix
                */
);/* <NEC> */ 

/*****************************************************************************
Returns the translation vector of a 4x4 matrix.

Return: void
Environment: Internal  and  External
See Also:
History:
******************************************************************************/
extern UFUNEXPORT void UF_MTX4_ask_translation(
const double mtx[16] ,/* <I>
                      Matrix whose translation is required.
                      */
double translate_vec[3]  /* <O>
                         Translation vector of the matrix
                         */
);/* <NEC> */ 

/*****************************************************************************
Copies 4x4 matrix elements from the source matrix to the destination
matrix.

Return: void
Environment: Internal  and  External
See Also:
History:
******************************************************************************/
extern UFUNEXPORT void  UF_MTX4_copy(
const double mtx_src[16] ,/* <I>
                          Source matrix
                          */
double mtx_dst[16]  /* <O>
                    Destination matrix
                    mtx_dst = mtx_src
                    */
);/* <NEC> */ 

/*****************************************************************************
Edits the 3x3 rotation matrix of a 4 x 4 matrix.

Return: void
Environment: Internal  and  External
See Also:
History:
******************************************************************************/
extern UFUNEXPORT void  UF_MTX4_edit_rotation(
double mtx_4D[16] ,/* <I/O>
                   4x4 matrix whose rotation is to be edited. (Input)
                   4x4 with an edited 3x3 rotation matrix. (Output)
                   */
const double mtx_3D[9]  /* <I>
                        3x3 rotation matrix to use as replacement in 4x4
                        matrix.
                        */
);/* <NEC> */ 

/*****************************************************************************
Edits the scale factor of a 4 x 4 matrix.

Return: void
Environment: Internal  and  External
See Also:
History:
******************************************************************************/
extern UFUNEXPORT void  UF_MTX4_edit_scale(
double mtx[16] ,/* <I/O>
                4x4 matrix whose scale is to be edited. (Input)
                4x4 with an edited scale factor. (Output)
                */
double scale  /* <I>
              Scale factor to use as replacement in 4x4 matrix.
              */
);/* <NEC> */ 

/*****************************************************************************
Edits the translation vector of a 4 x 4 matrix.

Return: void
Environment: Internal  and  External
See Also:
History:
******************************************************************************/
extern UFUNEXPORT void  UF_MTX4_edit_translation(
double mtx[16] ,/* <I/O>
                4x4 matrix whose translation is to be edited. (Input)
                4x4 with an edited translation vector. (Output)
                */
const double translate_vec[3]  /* <I>
                               Translation vector to use as replacement in 4x4
                               matrix.
                               */
);/* <NEC> */ 

/*****************************************************************************
Returns a 4 x 4 identity matrix.

Return: void
Environment: Internal  and  External
See Also:
History:
******************************************************************************/
extern UFUNEXPORT void  UF_MTX4_identity(
double identity_mtx[16]  /* <O>
                         Identity Matrix
                         */
);/* <NEC> */ 

/*****************************************************************************
Returns the 4x4 matrix formed from a 3x3 rotation matrix, a 3D
translation vector, and a scale factor.

Return: void
Environment: Internal  and  External
See Also:
History:
******************************************************************************/
extern UFUNEXPORT void UF_MTX4_initialize(
double scale ,/* <I>
              Scale factor
              */
const double translation_vec[3] ,/* <I>
                                 Translation vector
                                 */
const double mtx_3D[9] ,/* <I>
                        3x3 rotation matrix
                        */
double mtx_4D[16]  /* <O>
                   4x4 matrix
                   */
);/* <NEC> */ 

/*****************************************************************************
Returns a 4x4 matrix product from two input matrices.

Return: void
Environment: Internal  and  External
See Also:
History:
******************************************************************************/
extern UFUNEXPORT void UF_MTX4_multiply(
const double mtx1[16] ,/* <I>
                       Matrix #1
                       */
const double mtx2[16] ,/* <I>
                       Matrix #2
                       */
double mtx_product[16]  /* <O>
                        Matrix product
                         mtx_product = mtx1 X  mtx2
                        */
);/* <NEC> */ 

/*****************************************************************************
Returns a 4x4 matrix product by transposing the first matrix before
performing the multiplication.

Return: void
Environment: Internal  and  External
See Also:
History:
******************************************************************************/
extern UFUNEXPORT void UF_MTX4_multiply_t(
const double mtx1[16] ,/* <I>
                       Matrix #1 gets transposed before the
                       multiplication.
                       */
const double mtx2[16] ,/* <I>
                       Matrix #2
                       */
double mtx_product[16]  /* <O>
                        Matrix product
                         mtx_product = trns(mtx1) X  mtx2
                        */
);/* <NEC> */ 

/*****************************************************************************
Returns a 4x4 matrix whose direction vectors are orthogonal and of
unit length.

Return: void
Environment: Internal  and  External
See Also:
History:
******************************************************************************/
extern UFUNEXPORT void UF_MTX4_ortho_normalize(
double mtx[16] /* <I/O>
                Matrix to be ortho-normalized. (Input)
                Ortho-normalized matrix. (Output)
                */
);/* <NEC> */ 

/*****************************************************************************
Returns the transpose of a 4x4 matrix.

Return: void
Environment: Internal  and  External
See Also:
History:
******************************************************************************/
extern UFUNEXPORT void UF_MTX4_transpose(
const double mtx[16] ,/* <I>
                      Matrix to transpose
                      */
double transpose_mtx[16]  /* <O>
                          Transposed matrix
                          transpose_mtx = trns(mtx)
                          */
);/* <NEC> */ 

/*****************************************************************************
Returns a 4D vector which is the product of a 4D vector and a 4x4
matrix.

Return: void
Environment: Internal  and  External
See Also:
History:
******************************************************************************/
extern UFUNEXPORT void UF_MTX4_vec_multiply(
const double vec[4] ,/* <I>
                     Vector to multiply
                     */
const double mtx[16] ,/* <I>
                      Matrix to multiply
                      */
double vec_product[4]  /* <O>
                       Product (a vector)
                        vec_product = vec X mtx
                       */
);/* <NEC> */ 

/*****************************************************************************
Returns a vector which is the product of a 4D vector and a transposed
matrix.

Return: void
Environment: Internal  and  External
See Also:
History:
******************************************************************************/
extern UFUNEXPORT void UF_MTX4_vec_multiply_t(
const double vec[4] ,/* <I>
                     Vector to multiply
                     */
const double mtx[16] ,/* <I>
                      Matrix to transpose and multiply
                      */
double vec_product[4]  /* <O>
                       Product (a vector)
                       vec_product = vec X trns(mtx)
                       */
);/* <NEC> */ 

/*****************************************************************************
Returns a 3D vector which is the product of a 3D vector and a 4x4
matrix. The 3D vector is treated as a 4D vector with a weight of 1.0.

Return: void
Environment: Internal  and  External
See Also:
History:
******************************************************************************/
extern UFUNEXPORT void UF_MTX4_vec3_multiply(
const double vec[3] ,/* <I>
                     Vector to multiply
                     */
const double mtx[16] ,/* <I>
                      Matrix to multiply
                      */
double vec_product[3]  /* <O>
                       Product (a vector)
                       vec_product = vec X mtx
                       */
);/* <NEC> */ 

/*****************************************************************************
Returns a 3D vector which is the product of a 3D vector and the
transpose of a 4x4 matrix. During the multiplication, the 3D vector is
treated as a 4D vector with a weight of 1.0.

Return: void
Environment: Internal  and  External
See Also:
History:
******************************************************************************/
extern UFUNEXPORT void UF_MTX4_vec3_multiply_t(
const double vec[3] ,/* <I>
                     Vector to multiply
                     */
const double mtx[16] ,/* <I>
                      Matrix to multiply
                      */
double vec_product[3]  /* <O>
                       Product (a vector)
                       vec_product = vec X trns(mtx)
                       */
);/* <NEC> */ 

/*****************************************************************************
Returns the X-direction vector of the 3x3 rotation of a 4x4 matrix.

Return: void
Environment: Internal  and  External
See Also:
History:
******************************************************************************/
extern UFUNEXPORT void UF_MTX4_x_vec(
const double mtx[16] ,/* <I>
                      4x4 Matrix whose X-direction is required
                      */
double x_vec[3]  /* <O>
                 X-direction vector of the matrix
                 */
);/* <NEC> */ 

/*****************************************************************************
Returns the Y-direction vector of the 3x3 rotation of a 4x4 matrix.

Return: void
Environment: Internal  and  External
See Also:
History:
******************************************************************************/
extern UFUNEXPORT void UF_MTX4_y_vec(
const double mtx[16] ,/* <I>
                      4x4 matrix whose Y-direction is required
                      */
double y_vec[3]  /* <O>
                 Y-direction vector of the matrix
                 */
);/* <NEC> */ 

/*****************************************************************************
Returns the Z-direction vector of the 3x3 rotation of a 4x4 matrix.

Return: void
Environment: Internal  and  External
See Also:
History:
******************************************************************************/
extern UFUNEXPORT void UF_MTX4_z_vec(
const double mtx[16] ,/* <I>
                      Matrix whose Z-direction is required
                      */
double z_vec[3]  /* <O>
                 Z-direction vector of the matrix
                 */
);/* <NEC> */ 

/*****************************************************************************
Returns the matrix using scaling and invariant point information.

Environment: Internal  and  External
See Also: 

History: Originally released in V16.0
******************************************************************************/
extern UFUNEXPORT int UF_MTX4_scaling (

    const double   invariant_point[3],  /* <I>
                                           Point which will be invariant to the
                                           scaling, in other words the center
                                           point of the scale operation. */  
    const double   scale[3],        /* <I>
                                       scaling in x, y, z directions 
                                    */
          double   mtx[16]          /* <O>
                                       returned matrix that can be used to
                                       tranform objects  */
);

    
/*****************************************************************************
Returns the matrix which can be used to rotate about a point

Environment: Internal  and  External
See Also: 

History: Originally released in V16.0
******************************************************************************/
extern UFUNEXPORT int UF_MTX4_rotation(

    const double   rotation_point[3],  /* <I>
                                          Point about which the rotation is to
                                          be performed.
                                       */ 
    const double   rotation_axis[3],   /* <I>
                                          Axis about which rotation to occur.
                                       */  
    const double   angle,              /* <I>
                                          rotation angle in degrees 
                                       */
          double   mtx[16]             /* <O>
                                       returned matrix that can be used to
                                       tranform objects  
                                       */
);

/*****************************************************************************
Returns the matrix which can be used to mirror about a plane

Environment: Internal  and  External
See Also: 

History: Originally released in V16.0
******************************************************************************/
extern UFUNEXPORT int UF_MTX4_mirror (
    const double   origin[3],      /* <I> 
                                   The origin of the plane.
                                   */
    const double   normal[3],      /* <I> 
                                   The plane normal 
                                   */
          double   mtx[16]         /* <O>
                                   Returned matrix that can be used to
                                   tranform objects  
                                   */
);

/*****************************************************************************
Returns the matrix which can be used to map from one csys to another.

Environment: Internal  and  External
See Also: 

History: Originally released in V16.0
******************************************************************************/
extern UFUNEXPORT int UF_MTX4_csys_to_csys (
    const double   from_origin[3],  /* <I> origin of csys to map from */
    const double   from_x_axis[3],  /* <I> x axis of csys to map from */
    const double   from_y_axis[3],  /* <I> y axis of csys to map from */
    const double   to_origin[3],    /* <I> origin of csys to map to */
    const double   to_x_axis[3],    /* <I> x axis of csys to map to */
    const double   to_y_axis[3],    /* <I> y axis of csys to map to */   
          double   mtx[16]          /* <O>
                                       Returned matrix that can be used to
                                       tranform objects  */
);

/*****************************************************************************
Returns the matrix which is the invert of the input one

Return:
         Return value:
        0 = Success (inverted matrix created)
        n = Matrix not defined

Environment: Internal  and  External

History: Originally released in V18.0
******************************************************************************/
extern UFUNEXPORT int UF_MTX4_invert (
    const double   mtx_in[16],     /* <I> 
                                   Input matrix
                                   */
          double   mtx_out[16]     /* <O>
                                   Returned inverted matrix
                                   */
);

#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif /* UF_MTX_H_INCLUDED */
