/*******************************************************************************

             Copyright (c) 1998-2001 Unigraphics Solutions Inc.
                       Unpublished - All Rights Reserved                       




File Description:
This is the Open C API interface to transformations.  Using these subroutines you 
can:
.    change coordinates
.    map positions
.    perform compound transformations
.    perform translation, scaling, and rotation
.    mirror through a line or plane
.    perform transformation
***************************************************************************/

#ifndef UF_TRNS_INCLUDED 
#define UF_TRNS_INCLUDED 


/***************************************************************************

  ***************************************************************************/


#include <uf_defs.h>
#include <libufun_exports.h>


#ifdef __cplusplus
extern "C" {
#endif

/*******************************************************************************
 Returns a matrix to map coordinates from one coordinate system to another.
 NOTE: rp1 and rp2 are invalid when they contain a zero direction vector, or 
 the X and Y vectors are parallel.         
 Return: 
        void.
 Environment: Internal & External
 See Also:
 History:
*******************************************************************************/
extern UFUNEXPORT void FTN(uf5940)(
double ref_csys[9], /* <I>
                Real Data For Reference Coordinate System
                rp1[0-2] is the origin in absolute coordinates.  
                rp1[3-8] are the X and Y vectors in absolute coordinates.
                */
double dest_csys[9],  /* <I>
               Real Data For Destination Coordinate System
                rp2[0-2] is the origin in absolute coordinates.  
                rp2[3-8] are the X and Y vectors in absolute coordinates.
               */
double matrix[12],   /* <O>
                  Resulting Matrix.  This must be declared to hold 12 doubles.
               */
int *status   /* <O>
                  Status Code
                     0 = Success 
                     1 = rp1 Is Invalid
                     2 = rp2 Is Invalid
              */  
); /* <WRAPAS:UF_TRNS_create_csys_mapping_matrix> */
/*******************************************************************************
Returns the transformation of a position. No new objects are created here.

When rp2 is the "Change Coordinate" matrix (from UF5940), ra1 should be a 
position with respect to the reference coordinate system in the input in order 
to get back ra1 as a position with respect to the destination coordinate system
in the output. When rp2 is any other type of transformation matrix, ra1 should 
be a position in the absolute coordinates. The output in ra1 is then a
transformed position in absolute coordinates as well.

Return: void.
Environment: Internal & External
See Also:
History:
*******************************************************************************/
extern UFUNEXPORT void FTN(uf5941)(
double ra1[3],            /* <I/O>
                             Position/ Transformed Position
                          */
double rp2[12]            /* <I>
                          Defined Transformation Matrix.  This must be declared
                          to hold 12 doubles.
                          */
); /* <WRAPAS:UF_TRNS_map_position> */
/*******************************************************************************
Returns a product of two previously defined transformation matrices.

This is not a math routine to multiply any 2 matrices. The input matrices are 
transformation matrices only, and the product is the compound transformation 
matrix.

Return: void.
Environment: Internal & External
See Also:
History:
*******************************************************************************/
extern UFUNEXPORT void FTN(uf5942)(
double matrix1[16],               /* <I>
                                  Matrix Number 1.  This must be a 16 element
                                  array.
                                  */
double matrix2[16],               /* <I>
                                  Matrix Number 2.  This must be a 16 element
                                  array.
                                  */
double product[16]                /* <O>
                                  Product Matrix.  This must be a 16 element
                                  array.
                                  */
); /* <WRAPAS:UF_TRNS_multiply_matrices> */
/*******************************************************************************
Returns a matrix to perform a linear transformation a delta distance along the 
X-, Y-, and Z- axes of the absolute coordinate system.

Return: void.
Environment: Internal & External
See Also:
History:
*******************************************************************************/
extern UFUNEXPORT void FTN(uf5943)(
double translation[3],             /* <I>
                         Distance To Translate
                         rp1[0-2] contains Dx, Dy and Dz respectively.
                         */
double matrix[16]              /* <O>
                         Translation Matrix.  This must be a 16 element
                         array.
                         */
); /* <WRAPAS:UF_TRNS_create_translation_matrix> */
/*******************************************************************************
Returns a matrix to perform a scaling, uniform or non-uniform,  about an 
arbitrary origin.

Return: void.
Environment: Internal & External
See Also:
History:
*******************************************************************************/
extern UFUNEXPORT void FTN(uf5944)(
int *type,                   /* <I>
                             Type
                                1 - Uniform
                                2 - Non-Uniform
                             */
double scales[3],            /* <I>
                             Scaling Factors.   
                                rp2[0] is Sx (or factor s when ip1=1) 
                                rp2[1] is Sy (not used when ip1=1)
                                rp2[2] is Sz (not used when ip1=1).
                             */
double origin[3],            /* <I>
                             Scaling Origin (Absolute Coordinates)
                             */
double matrix[16],           /* <O>
                             Scaling Matrix.  This must be declared to hold
                             16 doubles.
                             */
int *status                  /* <O>
                             Status Code
                                    0 - Success
                                    1 - Scaling Factor Is Not Greater Than Zero
                                    2 - Invalid Option
                             */
); /* <WRAPAS:UF_TRNS_create_scaling_matrix> */
       
 
/*******************************************************************************
Returns a matrix to perform a rotation around an arbitrary axis.

Return: void
Environment: Internal & External
See Also:
History:
*******************************************************************************/
extern UFUNEXPORT void FTN(uf5945)(
double origin[3],            /* <I>
                             Origin Of The Axis - Absolute Coordinates
                             */
double direction[3],         /* <I>
                             Direction Vector - Absolute Coordinates
                             */
double *degrees_rotation,    /* <I>
                             Rotation Angle In Degrees
                             */
double matrix[16],           /* <O>
                             Rotation Matrix.  This must be declared to hold
                             16 doubles.
                             */
int *status                  /* <O>
                             Status Code
                                    0 - Success
                                    1 - Direction Vector Is A Zero Vector
                             */
); /* <WRAPAS:UF_TRNS_create_rotation_matrix> */
/*******************************************************************************
Returns a matrix to perform a reflection through a line or a plane.

When the line is perpendicular to the XY plane there is an infinite number of 
planes that pass through the line and are perpendicular to the XY plane;  
therefore, error code = 2.

Return: void
Environment: Internal & External
See Also:
History:
*******************************************************************************/
extern UFUNEXPORT void FTN(uf5946)(
tag_t *object,              /* <I>
                            Line Or Plane Object Identifier
                            */
double matrix[16],        /* <O>
                          Mirror matrix.  This must be declared to hold 16
                          doubles.
                          */
int *status               /* <O>
                          Status Code
                                 0 - Success
                                 1 - Invalid Line Or Plane Object Identifier
                                 2 - Unique Plane Through Line Cannot Be Defined
                          */
); /* <WRAPAS:UF_TRNS_create_reflection_matrix> */
/*******************************************************************************
Transform objects according to a previously defined matrix.  The matrix should
be defined by calls to uf5942-uf5946.

The upper limit on the number of objects to transform is 32767. The object 
types supported for non-uniform scaling are the same as those supported by 
non-uniform scaling in interactive NX.

Return: void
Environment: Internal & External
See Also:
History:
*******************************************************************************/
extern UFUNEXPORT void FTN(uf5947)(
const double rp1[16],         /* <I>
                              Defined Transformation Matrix.  This must be
                              a 16 element array.  This array should be 
                              initialized using the functions uf5942-uf5946
                              to produce the required transformation.
                              */
const tag_t objects[],       /* <I>
                             Array of object identifiers.
                             */
const int *n_objects,         /* <I>
                              Number of objects in np2 array.
                              */
const int *move_or_copy,      /* <I>
                              Move/Copy Status 
                                  1 - Move 
                                  2 - copy.
                              */
const int *dest_layer,        /* <I>
                              Destination Layer, 
                                  0       - the original layer,
                                  -1      - the work layer 
                                  1 - 256 - the specified layer
                              */    
const int *trace_curves,      /* <I>
                              Trace Curve Status, 1 means on, 2 means off.
                              */
tag_t *copies,            /* <O,len:n_objects>
                           List of copied object identifiers.  This is 
                           not used when ip4 = 1.  When ip4 is 2, this must
                           be dimensioned by the caller as large enough to
                           contain the same number of objects that are in np2.
                           */
tag_t *trace_curve_group,  /* <O>
                           Group of trace curves.  This is not used when 
                           ip6 is set to 2.
                           */
int *status                /* <O>
                           Status Code
                             0 - Success
                             1 - Too Many Or Too Few Entities To 
                                 Transform
                             2 - Invalid Parameter
                             3 - Invalid Object (Not Alive Or Not
                                 Transformable)
                             4 - Shear Matrix With Non-shearable
                                 Objects In The List
                             5 - Modeling update error
                             6 - Error adding modeling data to copied solid
                             7 - Cannot scale parametric solid
                             8 - Transformation is unsuitable for the object
                             9 - Cannot scale developed curve
                            10 - Cannot mirror solid
                            11 - Cannot transform occurrence
                            12 - Cannot transform sketches or sketch curves
                           */
); /* <WRAPAS:UF_TRNS_transform_objects> */

#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif    /*  END UF_TRNS_INCLUDED  */
