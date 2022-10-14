/*******************************************************************************
             Copyright (c) 1998-2000 Unigraphics Solutions, Inc.
                       Unpublished - All Rights Reserved

 

File Description:

These are vector functions that enable you to copy, add, perform scalar
multiplication, perform affine combinations, scale vectors and other
operations on 2D, 3D, and 4D vectors. The vector function names detail the
dimension of the vectors and provide a brief description of the operation
performed. For example, UF_VEC2_add performs a two dimensional vector addition.

*******************************************************************************/

#ifndef UF_VEC_H_INCLUDED
#define UF_VEC_H_INCLUDED


/***************************************************************************

  ***************************************************************************/

#include <libufun_exports.h>

#ifdef __cplusplus
extern "C" {
#endif

/******************************************************************************
Performs a two dimensional vector addition and returns the vector
sum in vec_sum[2].
Return:
       void

Environment: Internal  and  External

See Also:

History:
 *****************************************************************************/
extern UFUNEXPORT void  UF_VEC2_add(
const double vec1[2] ,/* <I>
                      Vector #1
                      */
const double vec2[2] ,/* <I>
                      Vector #2
                      */
double vec_sum[2]  /* <O>
                   The vector sum of vectors one and two
                   vec_sum = vec1 + vec2
                   */
);/* <NEC> */

/******************************************************************************
Performs a vector affine combination which consists of adding an
unscaled vector to a scaled vector. The first vector you input is vec[2],
which is unscaled. The second vector you input is the vec_to_scale[2],
which is scaled by the input argument scale. The resultant vector is
output to vec_comb[2].

Return:
      Void.

Environment: Internal  and  External

See Also:

History:
 ******************************************************************************/
extern UFUNEXPORT void  UF_VEC2_affine_comb(
const double vec[2] ,/* <I>
                     Unscaled vector
                     */
double scale ,/* <I>
              Scale to apply to vec_to_scale[2]
              */
const double vec_to_scale[2] ,/* <I>
                              The second two dimensional vector which is scaled.
                              */
double vec_comb[2]  /* <O>
                    Vector sum of unscaled vector and scaled vector
                    where vec_comb = vec + (scale * vec_to_scale)
                    */
);/* <NEC> */


/******************************************************************************
Calculates the scale factors of a linear combination of two vectors that
form a third vector. The vector combination is equal to the sum of the
two scaled vectors ( i.e., vec_comb = scale1 * vec1 + scale2 + vec2).

Return:
         0 = Scale factors can be calculated
         1 = Input vectors are parallel

Environment: Internal  and  External

See Also:

History:
 ******************************************************************************/
extern UFUNEXPORT int  UF_VEC2_components(
const double vec1[2] ,/* <I>
                      First vector of linear combination
                      */
const double vec2[2] ,/* <I>
                      Second vector of linear combination
                      */
const double vec_comb[2] ,/* <I>
                          Linear combination of vec1 and vec2
                          */
double tolerance ,/* <I>
                  Tolerance value to use for checking whether vec1
                  and vec2 are parallel
                  */
double * scale1 ,/* <O>
                 Scale factor of vec1 in linear combination
                 */
double * scale2  /* <O>
                 Scale factor of vec2 in linear combination
                 */
);

/******************************************************************************
Calculates the position of a point between the two end points of a line
segment. The point on the line segment is defined by:
pnt_on_seg = (parameter * pnt1) + ((1.0 - parameter) * pnt2).

Environment: Internal  and  External

Return:
      Void.

See Also:

History:
 ******************************************************************************/
extern UFUNEXPORT void  UF_VEC2_convex_comb(
double parameter ,/* <I>
                  Parameter of point to calculate
                  */
const double pnt1[2] ,/* <I>
                      First end point of line segment
                      */
const double pnt2[2] ,/* <I>
                      Second end point of line segment
                      */
double pnt_on_seg[2]  /* <O>
                      Point on line segment
                      */
);/* <NEC> */


/******************************************************************************
Copies the vector coordinates from a source vector to a destination
vector (vec_dst = vec_src).
Return:
       void.
Environment: Internal  and  External

See Also:

History:
 ******************************************************************************/
extern UFUNEXPORT void  UF_VEC2_copy(
const double vec_src[2] ,/* <I>
                         Source vector
                         */
double vec_dst[2]  /* <O>
                   Destination vector
                   */
);/* <NEC> */


/******************************************************************************
Calculates the cross product of two vectors.
Return:
      void.
Environment: Internal  and  External

See Also:

History:
 ******************************************************************************/
extern UFUNEXPORT void  UF_VEC2_cross(
const double vec1[2] ,/* <I>
                      Vector 1
                      */
const double vec2[2] ,/* <I>
                      Vector 2
                      */
double * cross_product  /* <O>
                        The cross product of vec1 and vec2
                        cross_product = vec1 x vec2
                        */
);/* <NEC> */

/*****************************************************************************
Calculates the distance between two points.
Return:
      void.
Environment: Internal  and  External

See Also:

History:
 ****************************************************************************/
extern UFUNEXPORT void  UF_VEC2_distance(
const double pnt1[2] ,/* <I>
                      Point 1
                      */
const double pnt2[2] ,/* <I>
                      Point 2
                      */
double * distance  /* <O>
                   The distance between pnt1 and pnt2
                   (distance = ||pnt1 - pnt2||)
                   */
);/* <NEC> */

/******************************************************************************
Calculates the dot product of vec1 and vec2.
Return:
       void.
Environment: Internal  and  External

See Also:

History:
 *****************************************************************************/
extern UFUNEXPORT void  UF_VEC2_dot(
const double vec1[2] ,/* <I>
                      Vector 1
                      */
const double vec2[2] ,/* <I>
                      Vector 2
                      */
double * dot_product  /* <O>
                      The dot product of vec1 and vec2
                      dot_product = vec1 (dot) vec2
                      */
);/* <NEC> */

/******************************************************************************
Determines if two vectors are equal within the specified tolerance.
Return:
      void.
Environment: Internal  and  External

See Also:

History:
 *****************************************************************************/
extern UFUNEXPORT void  UF_VEC2_is_equal(
const double vec1[2] ,/* <I>
                      Vector 1
                      */
const double vec2[2] ,/* <I>
                      Vector 2
                      */
double tolerance ,/* <I>
                  Tolerance value to use for checking
                  */
int * is_equal  /* <O>
                0 = Vectors are not equal
                1 = Vectors are equal
                */
);/* <NEC> */

/******************************************************************************
Determines if a vector is zero within the specified tolerance.
Return:
      void.
Environment: Internal  and  External

See Also:

History:
 *****************************************************************************/
extern UFUNEXPORT void  UF_VEC2_is_zero(
const double vec[2] ,/* <I>
                     Vector to test
                     */
double tolerance ,/* <I>
                  Tolerance value to use for checking
                  */
int * is_zero  /* <O>
               0 = Vectors is not zero
               1 = Vectors is zero
               */
);/* <NEC> */

/******************************************************************************
Calculates the vector linear combination of two vectors with the
specified scale values.
Return:
      void.
Environment: Internal  and  External

See Also:

History:
 *****************************************************************************/
extern UFUNEXPORT void  UF_VEC2_linear_comb(
double scale1 ,/* <I>
               Scale value for vector 1
               */
const double vec1[2] ,/* <I>
                      Vector 1
                      */
double scale2 ,/* <I>
               scale for vector 2
               */
const double vec2[2] ,/* <I>
                      Vector 2
                      */
double vec_comb[2]  /* <O>
                    Vector linear combination
                    vec_comb = (scale * vec1) + (scale2 * vec2)
                    */
);/* <NEC> */

/******************************************************************************
Calculates the magnitude of a vector.
Return:
      void.
Environment: Internal  and  External

See Also:

History:
 *****************************************************************************/
extern UFUNEXPORT void  UF_VEC2_mag(
const double vec[2] ,/* <I>
                     Vector whose magnitude is required
                     */
double * magnitude  /* <O>
                    Magnitude of vector
                    magnitude =  ||vec||
                    */
);/* <NEC> */

/*****************************************************************************
Calculates the coordinates of the mid-point on a line segment.
Return:
      void.
Environment: Internal  and  External

See Also:

History:
 *****************************************************************************/
extern UFUNEXPORT void  UF_VEC2_midpt(
const double pnt1[2] ,/* <I>
                      End Point #1 of line segment
                      */
const double pnt2[2] ,/* <I>
                      End Point #2 of line segment
                      */
double mid_pnt[2]  /* <O>
                   Mid-point of line segment
                   mid_pnt = (0.5 * pnt1) + (0.5 * pnt2)
                   */
);/* <NEC> */

/*****************************************************************************
Calculates the negative of a vector.
Return:
      void.
Environment: Internal  and  External

See Also:

History:
 ****************************************************************************/
extern UFUNEXPORT void  UF_VEC2_negate(
const double vec[2] ,/* <I>
                     Vector to negate
                     */
double negated_vec[2]  /* <O>
                       Negated vector
                       negated_vec = (-1.0) x vec
                       */
);/* <NEC> */

/*****************************************************************************
Rotates a 2D vector about a line perpendicular to the plane of the
vector through the vector origin.
Return:
      void.
Environment: Internal  and  External

See Also:

History:
 ****************************************************************************/
extern UFUNEXPORT void  UF_VEC2_rotate(
const double vec[2] ,/* <I>
                     Vector to rotate
                     */
double angle ,/* <I>
              Angle to rotate through (in radians)
              */
double rotated_vec[2]  /* <O>
                       Rotated vector
                       */
);/* <NEC> */

/*****************************************************************************
Scales the coordinates of a vector.
Return:
      void.
Environment: Internal  and  External

See Also:

History:
 ****************************************************************************/
extern UFUNEXPORT void  UF_VEC2_scale(
double scale ,/* <I>
              Scale factor
              */
const double vec[2] ,/* <I>
                     Vector to scale
                     */
double scaled_vec[2]  /* <O>
                      scaled vector
                      scaled_vec = (scale x vec)
                      */
);/* <NEC> */

/*****************************************************************************
Subtracts one 2D vector from another.
Return:
      void.
Environment: Internal  and  External

See Also:

History:
 ****************************************************************************/
extern UFUNEXPORT void  UF_VEC2_sub(
const double vec1[2] ,/* <I>
                      Vector to subtract from
                      */
const double vec2[2] ,/* <I>
                      Vector to subtract
                      */
double vec_diff[2]  /* <O>
                    Vector difference
                    vec_diff = vec1  -  vec2
                    */
);/* <NEC> */

/*****************************************************************************
Unitizes a 2D vector.

Return:
         0 = Success (unit vector can be calculated)
         1 = input vector is zero

Environment: Internal  and  External

See Also:

History:
 *****************************************************************************/
extern UFUNEXPORT int  UF_VEC2_unitize(
const double vec[2] ,/* <I>
                     Vector to unitize
                     */
double tolerance ,/* <I>
                  Tolerance value to use for checking
                  */
double * magnitude ,/* <O>
                    Vector magnitude = |vec|
                    */
double unit_vec[2]  /* <O>
                    Unitized vector = vec/|vec|
                    */
);

/******************************************************************************
Converts a 2D vector to a 3D vector. Sets the Z-coordinate to zero.
Return:
      void.
Environment: Internal  and  External

See Also:

History:
 *****************************************************************************/
extern UFUNEXPORT void  UF_VEC2_vec3(
const double vec_2D[2] ,/* <I>
                        2D vector to convert to 3D
                        */
double vec_3D[3]  /* <O>
                  3D vector
                  */
);/* <NEC> */

/*****************************************************************************
Returns a 2D vector that is perpendicular to the input vector
Return:
      void.
Environment: Internal  and  External
See Also:

History:
*****************************************************************************/
extern UFUNEXPORT void UF_VEC2_ask_perpendicular
(
    const double vec1[2],           /* <I>
                                       2D vector */
    double vec_perp[2]              /* <O>
                                       2D vector */
    );/* <NEC> */


/*****************************************************************************
Determine if vectors are parallel within an input tolerance.  If the sine of
the angle between vec1 and vec2 is 0 then TRUE is returned.  Otherwise FALSE
is returned.

Return:
      void.
Environment: Internal  and  External
See Also:

History:
*****************************************************************************/
extern UFUNEXPORT void UF_VEC2_is_parallel
(
    const double vec1[2],           /* <I>
                                       2D vector */
    const double vec2[2],           /* <I>
                                       2D vector */
    double tolerance,               /* <I>
                                       tolerance */
    int *is_parallel                /* <O>
                                       = 0 Vectors are not parallel
                                       = 1 Vectors are parallel */
    );/* <NEC> */


/******************************************************************************
Determine if vectors are perpendicular within an input tolerance.  If the cosine
of the angle between vec1 and vec2 is 0 then TRUE is returned.  Otherwise FALSE
is returned.

Return:
      void.
Environment: Internal  and  External
See Also:

History:
*****************************************************************************/
extern UFUNEXPORT void UF_VEC2_is_perpendicular
(
    const double vec1[2],           /* <I>
                                       2D vector */
    const double vec2[2],           /* <I>
                                       2D vector */
    double tolerance,               /* <I>
                                       tolerance */
    int *is_perp                    /* <O>
                                       = 0 Vectors are not perpendicular
                                       = 1 Vectors are perpendicular */
    );/* <NEC> */

/*
********************************************************************************
*
*   Prototypes of functions used to initialize, access, and manipulate
*   3D points and vectors.
*
********************************************************************************
*/


/******************************************************************************
Performs a three dimensional vector addition and returns the vector
sum in vec_sum[3].
Return:
      void.
Environment: Internal  and  External

See Also:

History:
 *****************************************************************************/
extern UFUNEXPORT void  UF_VEC3_add(
const double vec1[3] ,/* <I>
                      The first three dimensional vector
                      */
const double vec2[3] ,/* <I>
                      The second three dimensional vector
                      */
double vec_sum[3]  /* <O>
                   The vector sum of vectors one and two
                   vec_sum = vec1 + vec2
                   */
);/* <NEC> */

/******************************************************************************
Performs a vector affine combination which consists of adding an
unscaled vector to a scaled vector. The first vector you input is vec[3],
which is unscaled. The second vector you input is the vec_to_scale[3]
which is scaled by the input argument scale. The resultant vector is
output to vec_comb[3].
Return:
      void.
Environment: Internal  and  External

See Also:

History:
 ******************************************************************************/
extern UFUNEXPORT void  UF_VEC3_affine_comb(
const double vec[3] ,/* <I>
                     Unscaled vector
                     */
double scale ,/* <I>
              Scale to apply to vec_to_scale[3]
              */
const double vec_to_scale[3] ,/* <I>
                            The second three dimensional vector which is scaled.
                            */
double vec_comb[3]  /* <O>
                    Vector sum of unscaled vector and scaled vector
                    where vec_comb = vec + (scale * vec_to_scale)
                    */
);/* <NEC> */

/******************************************************************************
Calculates the angle between two vectors using a third vector to
determine the direction. The third vector is one that is perpendicular
to both the vec_from and vec_to vectors. For example, if the two
vectors lie in the x-y plane, then the third vector would be parallel to
the z-axis.
Return:
      void.
Environment: Internal  and  External

See Also:

History:
 ******************************************************************************/
extern UFUNEXPORT void  UF_VEC3_angle_between(
const double vec_from[3] ,/* <I>
                          Vector to calculate angle from
                          */
const double vec_to[3] ,/* <I>
                        Vector to calculate angle to
                        */
const double vec_ccw[3] ,/* <I>
                         Vector to define counter-clockwise orientation
                         */
double * angle  /* <O>
                Angle between vec_from and vec_to using vec_ccw
                to determine positive orientation. The angle is in
                radians and 0.0 <= (*angle) < 2 PI.
                */
);/* <NEC> */

/*****************************************************************************
Calculates the position of a point between the two end points of a line
segment. The point on the line segment is defined by:
pnt_on_seg = (parameter * pnt1) + ((1.0 - parameter) * pnt2).

Return:
      void.
Environment: Internal  and  External

See Also:

History:
 ****************************************************************************/
extern UFUNEXPORT void  UF_VEC3_convex_comb(
double parameter ,/* <I>
                  Parameter of point to calculate
                  */
const double pnt1[3] ,/* <I>
                      First end point of line segment
                      */
const double pnt2[3] ,/* <I>
                      Second end point of line segment
                      */
double pnt_on_seg[3]  /* <O>
                      Point on line segment
                      */
);/* <NEC> */

/*****************************************************************************
Copies the vector coordinates from a source vector to a destination
vector (vec_dst = vec_src).
Return:
      void.
Environment: Internal  and  External

See Also:

History:
 *****************************************************************************/
extern UFUNEXPORT void  UF_VEC3_copy(
const double vec_src[3] ,/* <I>
                         Source vector
                         */
double vec_dst[3]  /* <O>
                   Destination vector
                   */
);/* <NEC> */


/*****************************************************************************
Calculates the cross product of two vectors.
Return:
      void.
Environment: Internal  and  External

See Also:

History:
 ****************************************************************************/
extern UFUNEXPORT void  UF_VEC3_cross(
const double vec1[3] ,/* <I>
                      Vector 1
                      */
const double vec2[3] ,/* <I>
                      Vector 2
                      */
double cross_product[3]  /* <O>
                         The cross product of vec1 and vec2
                         cross_product = vec1 * vec2
                         */
);/* <NEC> */

/*****************************************************************************
Calculates the distance between two points.
Return:
      void.
Environment: Internal  and  External

See Also:

History:
 *****************************************************************************/
extern UFUNEXPORT void  UF_VEC3_distance(
const double pnt1[3] ,/* <I>
                      Point 1
                      */
const double pnt2[3] ,/* <I>
                      Point 2
                      */
double * distance  /* <O>
                   The distance between pnt1 and pnt2
                   (distance = ||pnt1 - pnt2||)
                   */
);

/*****************************************************************************
Calculates the normal distance from a point to a plane.

Return:
         0 = Success (distance can be calculated)
         1 = The plane normal is zero

Environment: Internal  and  External

See Also:

History:
 ****************************************************************************/
extern UFUNEXPORT int UF_VEC3_distance_to_plane(
const double pnt1[3] ,/* <I>
                      Point to calculate distance from
                      */
const double pnt_on_plane[3] ,/* <I>
                              Point located on the plane
                              */
const double plane_normal[3] ,/* <I>
                              Plane normal
                              */
double tolerance ,/* <I>
                  Tolerance value to use for checking
                  */
double * distance  /* <O>
                   The normal distance from the point to the plane
                   */
);

/******************************************************************************
Calculates the dot product of vec1 and vec2.
Return:
       void.
Environment: Internal  and  External

See Also:

History:
 *****************************************************************************/
extern UFUNEXPORT void  UF_VEC3_dot(
const double vec1[3] ,/* <I>
                      Vector 1
                      */
const double vec2[3] ,/* <I>
                      Vector 2
                      */
double * dot_product  /* <O>
                      The dot product of vec1 and vec2
                      dot_product = vec1 (dot) vec2
                      */
);/* <NEC> */

/*****************************************************************************
Determines if a vector is zero within the specified tolerance.
Return:
      void.
Environment: Internal  and  External

See Also:

History:
 ****************************************************************************/
extern UFUNEXPORT void  UF_VEC3_is_zero(
const double vec[3] ,/* <I>
                     Vector to test
                     */
double tolerance ,/* <I>
                  Tolerance value to use for checking
                  */
int * is_zero  /* <O>
               0 = Vectors is not zero
               1 = Vectors is zero
               */
);/* <NEC> */

/*****************************************************************************
Determines if two vectors are equal within the specified tolerance.
Return:
      void.
Environment: Internal  and  External

See Also:

History:
 ****************************************************************************/
extern UFUNEXPORT void  UF_VEC3_is_equal(
const double vec1[3] ,/* <I>
                      Vector 1
                      */
const double vec2[3] ,/* <I>
                      Vector 2
                      */
double tolerance ,/* <I>
                  Tolerance value to use for checking
                  */
int * is_equal  /* <O>
                0 = Vectors are not equal
                1 = Vectors are equal
                */
);/* <NEC> */

/*****************************************************************************
Calculates the vector linear combination of two vectors with the
specified scale values.
Return:
      void.
Environment: Internal  and  External

See Also:

History:
 ****************************************************************************/
extern UFUNEXPORT void  UF_VEC3_linear_comb(
double scale1 ,/* <I>
               Scale value for vector 1
               */
const double vec1[3] ,/* <I>
                      Vector 1
                      */
double scale2 ,/* <I>
               scale for vector 2
               */
const double vec2[3] ,/* <I>
                      Vector 2
                      */
double vec_comb[3]  /* <O>
                    Vector linear combination
                    vec_comb = (scale * vec1) + (scale2 * vec2)
                    */
);/* <NEC> */

/******************************************************************************
Calculates the magnitude of a vector.
Return:
      void.
Environment: Internal  and  External

See Also:

History:
 *****************************************************************************/
extern UFUNEXPORT void  UF_VEC3_mag(
const double vec[3] ,/* <I>
                     Vector whose magnitude is required
                     */
double * magnitude  /* <O>
                    Magnitude of vector
                    magnitude =  ||vec||
                    */
);/* <NEC> */

/*****************************************************************************
Calculates the coordinates of the mid-point on a line segment.
Return:
      void.
Environment: Internal  and  External

See Also:

History:
 ****************************************************************************/
extern UFUNEXPORT void  UF_VEC3_midpt(
const double pnt1[3] ,/* <I>
                      End Point #1 of line segment
                      */
const double pnt2[3] ,/* <I>
                      End Point #2 of line segment
                      */
double mid_pnt[3]  /* <O>
                   Mid-point of line segment
                   mid_pnt = (0.5 * pnt1) + (0.5 * pnt2)
                   */
);/* <NEC> */

/*****************************************************************************
Calculates the negative of a vector.
Return:
      void.
Environment: Internal  and  External

See Also:

History:
 ****************************************************************************/
extern UFUNEXPORT void  UF_VEC3_negate(
const double vec[3] ,/* <I>
                     Vector to negate
                     */
double negated_vec[3]  /* <O>
                       Negated vector
                       negated_vec = (-1.0) * vec
                       */
);/* <NEC> */

/*****************************************************************************
Scales the coordinates of a vector.
Return:
      void.
Environment: Internal  and  External

See Also:

History:
 ****************************************************************************/
extern UFUNEXPORT void  UF_VEC3_scale(
double scale ,/* <I>
              Scale factor
              */
const double vec[3] ,/* <I>
                     Vector to scale
                     */
double scaled_vec[3]  /* <O>
                      scaled vector
                      scaled_vec = (scale x vec)
                      */
);/* <NEC> */

/*****************************************************************************
Subtracts one vector from  another.
Return:
      void.
Environment: Internal  and  External

See Also:

History:
 *****************************************************************************/
extern UFUNEXPORT void  UF_VEC3_sub(
const double vec1[3] ,/* <I>
                      Vector to subtract from
                      */
const double vec2[3] ,/* <I>
                      Vector to subtract
                      */
double vec_diff[3]  /* <O>
                    Vector difference
                    vec_diff = vec1 - vec2
                    */
);/* <NEC> */

/******************************************************************************
Calculates the triple scalar product of three vectors.
Return:
      void.
Environment: Internal  and  External

See Also:

History:
 *****************************************************************************/
extern UFUNEXPORT void  UF_VEC3_triple(
const double vec1[3] ,/* <I>
                      Vector #1
                      */
const double vec2[3] ,/* <I>
                      Vector #2
                      */
const double vec3[3] ,/* <I>
                      Vector #3
                      */
double * triple_product  /* <O>
                         The triple scalar product
                         triple_product = vec1 (dot) (vec2 x vec3)
                         */
);/* <NEC> */

/******************************************************************************
Unitizes a vector.

Return:
         0 = Success (unit vector can be calculated)
         1 = input vector is zero

Environment: Internal  and  External

See Also:

History:
 *****************************************************************************/
extern UFUNEXPORT int  UF_VEC3_unitize(
const double vec[3] ,/* <I>
                     Vector to unitize
                     */
double tolerance ,/* <I>
                  Tolerance value to use for checking
                  */
double * magnitude ,/* <O>
                    Vector magnitude = ||vec||
                    */
double unit_vec[3]  /* <O>
                    Unitized vector = vec/||vec||
                    */
);

/******************************************************************************
Converts a 3D vector to a 2D vector. Strips the Z-coordinate of the
3D vector.
Return:
      void.
Environment: Internal  and  External

See Also:

History:
 *****************************************************************************/
extern UFUNEXPORT void  UF_VEC3_vec2(
const double vec_3D[3] ,/* <I>
                        3D vector to convert to 2D
                        */
double vec_2D[2]  /* <O>
                  2D vector
                  */
);/* <NEC> */

/*****************************************************************************
Converts a 3D vector to a 4D homogeneous vector with a weight of
1.0.
Return:
      void.
Environment: Internal  and  External

See Also:

History:
 ******************************************************************************/
extern UFUNEXPORT void  UF_VEC3_vec4(
const double vec_3D[3] ,/* <I>
                        3D vector to convert to 4D
                        */
double vec_4D[4]  /* <O>
                  4D vector
                  */
);/* <NEC> */

/******************************************************************************
Converts a 3D vector to a 4D homogeneous vector with the given
weight. The 3D coordinates are multiplied by the specified weight. If
the 3D coordinates are (x,y,z) and the weight = h, then the 4D
coordinates would be (hx,hy,hz,h).
Return:
      void.
Environment: Internal  and  External

See Also:

History:
 *****************************************************************************/
extern UFUNEXPORT void  UF_VEC3_vec4_homogen(
const double vec_3D[3] ,/* <I>
                        3D vector to convert
                        */
double weight ,/* <I>
               Weight to be used
               */
double vec_4D[4]  /* <O>
                  4D homogeneous vector
                  */
);/* <NEC> */

/******************************************************************************
Returns a 3D vector that is perpendicular to the input vector
Return:
      void.
Environment: Internal  and  External
See Also:

History:
******************************************************************************/
extern UFUNEXPORT void UF_VEC3_ask_perpendicular
(
    const double vec1[3],           /* <I>
                                       3D vector */
    double vec_perp[3]              /* <O>
                                       3D vector perpendicular to the first
                                       vector. */
    );/* <NEC> */


/*****************************************************************************
Determine if vectors are parallel within an input tolerance.  If the sine of 
the angle between the vec1 and vec2 is less than tolerance then
TRUE is returned.  Otherwise a FALSE will be returned.  To get an angle
tolerance of x degrees the expected tolerance would be sin(x*DEGRA).

Return:
      void.
Environment: Internal  and  External
See Also:

History:
******************************************************************************/
extern UFUNEXPORT void UF_VEC3_is_parallel
(
    const double vec1[3],           /* <I>
                                       3D vector */
    const double vec2[3],           /* <I>
                                       3D vector */
    double tolerance,               /* <I>
                                       tolerance */
    int *is_parallel                /* <O>
                                       = 0 Vectors are not parallel
                                       = 1 Vectors are parallel */
    );/* <NEC> */


/******************************************************************************
Determine if vectors are perpendicular an input tolerance.  If the cosine of the
angle between vec1 and vec2 is less than the tolerance, then a TRUE is returned.
Otherwise FALSE is returned.  To check perpendicularity with x degrees from 90, 
the expected tolerance would be cos( (90-x)*DEGRA).

Return:
      void.
Environment: Internal  and  External
See Also:

History:
******************************************************************************/
extern UFUNEXPORT void UF_VEC3_is_perpendicular
(
    const double vec1[3],           /* <I>
                                       3D vector */
    const double vec2[3],           /* <I>
                                       3D vector */
    double tolerance,               /* <I>
                                       tolerance */
    int *is_perp                    /* <O>
                                       = 0 Vectors are not perpendicular
                                       = 1 Vectors are perpendicular */
    );/* <NEC> */


/*
********************************************************************************
*
*   Prototypes of functions used to initialize, access, and manipulate
*   4D points and vectors.
*
********************************************************************************
*/


/******************************************************************************
Copies the vector coordinates from a source vector to a destination
vector (vec_dst = vec_src).
Return:
      void.
Environment: Internal  and  External

See Also:

History:
 *****************************************************************************/
extern UFUNEXPORT void  UF_VEC4_copy(
const double vec_src[4] ,/* <I>
                         Source vector
                         */
double vec_dst[4]  /* <O>
                   Destination vector
                   */
);/* <NEC> */


/*****************************************************************************
Determines if two vectors are equal within the specified tolerance.
Return:
      void.
Environment: Internal  and  External

See Also:

History:
 *****************************************************************************/
extern UFUNEXPORT void  UF_VEC4_is_equal(
const double vec1[4] ,/* <I>
                      Vector #1
                      */
const double vec2[4] ,/* <I>
                      Vector #2
                      */
double tolerance ,/* <I>
                  Tolerance value to use for checking
                  */
int * is_equal  /* <O>
                0 = Vectors are not equal
                1 = Vectors are equal
                */
);/* <NEC> */

/******************************************************************************
Determines if a vector is zero within the specified tolerance.
Return:
      void.
Environment: Internal  and  External

See Also:

History:
 ******************************************************************************/
extern UFUNEXPORT void  UF_VEC4_is_zero(
const double vec[4] ,/* <I>
                     Vector to test
                     */
double tolerance ,/* <I>
                  Tolerance value to use for checking
                  */
int * is_zero  /* <O>
               0 = Vector is not zero
               1 = Vector is zero
               */
);/* <NEC> */

/******************************************************************************
Scales the coordinates of a vector.
Return:
      void.
Environment: Internal  and  External

See Also:

History:
 *****************************************************************************/
extern UFUNEXPORT void  UF_VEC4_scale(
double scale ,/* <I>
              Scale factor
              */
const double vec[4] ,/* <I>
                     Vector to scale
                     */
double scaled_vec[4]  /* <O>
                      scaled vector
                      scaled_vec = (scale x vec)
                      */
);/* <NEC> */

/*****************************************************************************
Converts a 4D vector to a 3D vector by stripping the weight of the 4D
vector.
Return:
      void.
Environment: Internal  and  External

See Also:

History:
 ****************************************************************************/
extern UFUNEXPORT void  UF_VEC4_vec3(
const double vec_4D[4] ,/* <I>
                        4D vector to convert to 3D
                        */
double vec_3D[3]  /* <O>
                  3D vector
                  */
);/* <NEC> */


/*****************************************************************************
Converts a 4D homogeneous vector to a 3D vector by dividing the 4D
coordinates by the weight.
Return:
      void.
Environment: Internal  and  External

See Also:

History:
 ****************************************************************************/
extern UFUNEXPORT void  UF_VEC4_vec3_homogen(
const double vec_4D[4] ,/* <I>
                        4D vector to convert
                        */
double vec_3D[3]  /* <O>
                  3D vector
                  */
);/* <NEC> */

#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif /* UF_VEC_H_INCLUDED */
