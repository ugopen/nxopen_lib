/*****************************************************************************
             Copyright (c) 1998-2000 Unigraphics Solutions Inc.
                       Unpublished - All Rights Reserved                       



File description: 
    Open API modeling routines to create/inquire solid primitive features
    like block, cone, cylinder and sphere.

*****************************************************************************/

#ifndef UF_MODL_PRIMITIVES_H_INCLUDED
#define UF_MODL_PRIMITIVES_H_INCLUDED


/***************************************************************************

  ***************************************************************************/

#include <uf_defs.h>
#include <uf_modl_types.h>
#include <libufun_exports.h>

#ifdef __cplusplus
extern "C" {
#endif

/****************************************************************************
Create a solid block.

Environment: Internal  and  External
See Also:
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_create_block (
   UF_FEATURE_SIGN   sign,               /* <I>
                                         Sign of primitive
                                         */
   tag_t             targ_tag,           /* <I>
                                         Target body (if needed)
                                         */
   double            corner_pt[3],       /* <I>
                                         Corner point
                                         */
   char *            edge_len[3],        /* <I>
                                         Edge lengths
                                         */
   tag_t             *blk_tag            /* <O>
                                         Block feature tag
                                         */
);

/****************************************************************************
Create a solid cone.

Environment: Internal  and  External
See Also:
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_create_cone (
   UF_FEATURE_SIGN   sign,               /* <I>
                                         Sign of primitive
                                         */
   tag_t             targ_tag,           /* <I>
                                         Target body (if needed)
                                         */
   double            origin[3],          /* <I>
                                         Cone base origin
                                         */
   char              *height,            /* <I>
                                         Cone height
                                         */
   char              *diam[2],           /* <I>
                                         Cone diameters
                                         */
   double            direction[3],       /* <I>
                                         Cone direction vector
                                         */
   tag_t             *cone_tag           /* <O>
                                         Cone feature tag
                                         */
   );
/****************************************************************************
Create a solid cylinder.

Environment: Internal  and  External
See Also:
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_create_cylinder (
   UF_FEATURE_SIGN   sign,               /* <I>
                                         Sign of primitive
                                         */
   tag_t             targ_tag,           /* <I>
                                         Target body (if needed)
                                         */
   double            origin[3],          /* <I>
                                         Cylinder base origin
                                         */
   char              *height,            /* <I>
                                         Cylinder height
                                         */
   char              *diam,              /* <I>
                                         Cylinder diameter
                                         */
   double            direction[3],       /* <I>
                                         Cylinder dir vector
                                         */
   tag_t             *cyl_tag            /* <O>
                                         Cylinder feature tag
                                         */
   );
/****************************************************************************
Create a solid sphere.

Environment: Internal  and  External
See Also:
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_create_sphere (
   UF_FEATURE_SIGN   sign,               /* <I>
                                         Sign of primitive
                                         */
   tag_t             targ_tag,           /* <I>
                                         Target body (if needed)
                                         */
   double            center[3],          /* <I>
                                         Sphere center
                                         */
   char *            diam,               /* <I>
                                         Sphere diameter
                                         */
   tag_t             *sphere_tag         /* <O>
                                         Sphere feature tag
                                         */
   );
/****************************************************************************
Creates a block. The Corner Point indicates the origin of  the block to
be created. The X, Y and Z lengths control the size of the edge
lengths. The sign parameter controls the boolean operation
performed. The output of this function is the object identifier
associated to the block.

The origin point is with respect to the Absolute CSYS.  However, the
direction of the edge lengths are with respect to the WCS.


Environment: Internal  and  External
See Also: 
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_create_block1(
UF_FEATURE_SIGN sign ,/* <I>
                      The sign of the operation to be performed.
                      UF_NULLSIGN = create new target solid
                      UF_POSITIVE  = add to target solid
                      UF_NEGATIVE = subtract from target solid
                      UF_UNSIGNED = intersect with target solid
                      */
double corner_pt[3] ,/* <I>
                     Corner point (origin) of block
                     */
char * edge_len[3] ,/* <I>
                    Three edge lengths of block
                    */
tag_t * blk_obj_id  /* <O>
                    Feature object identifier of created block.
                    */
);

/****************************************************************************
Creates a cone. The origin indicates where the center of the bottom
face is located for the cone. The direction vector controls which axis
the cone is created on. The base and top diameters (diam) and height
control the size of the cone. The sign parameter controls the boolean
operation performed. The output of this function is the object
identifier associated to that cone.


Environment: Internal  and  External
See Also:
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_create_cone1(
UF_FEATURE_SIGN sign ,/* <I>
                      The sign of the operation to be performed.
                      UF_NULLSIGN = create new target solid
                      UF_POSITIVE = add to target solid
                      UF_NEGATIVE = subtract from target solid
                      UF_UNSIGNED = intersect with target solid
                      */
double origin[3] ,/* <I>
                  Origin for cone to be created.
                  */
char * height ,/* <I>
               Height for cone to be created.
               */
char * diam[2] ,/* <I>
                Diameters for cone to be created.
                [0] = base diameter
                [1] = top diameter
                */
double direction[3] ,/* <I>
                     Direction vector for cone to be created.
                     */
tag_t * cone_obj_id  /* <O>
                     Feature object identifier tag of created cone.
                     */
);

/****************************************************************************
Creates a cylinder. The origin indicates where the center of the
bottom face is located for the cylinder. The direction vector controls
the axis on which the cylinder is created. The diameter and height
control the size of the cylinder. The sign parameter controls the
boolean operation performed. The output of this function is the object
identifier associated to the cylinder.


Environment: Internal  and  External
See Also:
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_create_cyl1(
UF_FEATURE_SIGN sign ,/* <I>
                      The sign of the operation to be performed.
                      UF_NULLSIGN = create new target solid
                      UF_POSITIVE = add to target solid
                      UF_NEGATIVE = subtract from target solid
                      UF_UNSIGNED = intersect with target solid
                      */
double origin[3] ,/* <I>
                  Origin of cylinder to be created.
                  */
char * height ,/* <I>
               Height of cylinder to be created.
               */
char * diam ,/* <I>
             Diameter of cylinder to be created.
             */
double direction[3] ,/* <I>
                     Direction vector for cylinder to be created.
                     */
tag_t * cyl_obj_id  /* <O>
                    Feature object identifier of created cylinder
                    */
);

/****************************************************************************
Creates a sphere.  The Origin indicates the center of the sphere.  The
Diameter controls the size, and the sign parameter controls the
boolean operation performed. The output of this function is the feature
tag associated to the sphere.


Environment: Internal  and  External
See Also:
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_create_sphere1(
UF_FEATURE_SIGN sign ,/* <I>
                      The sign of the operation to be performed.
                      UF_NULLSIGN = create new target solid
                      UF_POSITIVE = add to target solid
                      UF_NEGATIVE = subtract from target solid
                      UF_UNSIGNED = intersect with target solid
                      */
double center[3] ,/* <I>
                  Center of sphere to be created.
                  */
char * diam ,/* <I>
             Diameter of sphere to be created.
             */
tag_t * sphere_obj_id  /* <O>
                       Feature tag of created sphere.
                       */
);

/********************************************************************
Gets block parameters.

Environment: Internal  and  External

See Also:

History:
********************************************************************/
extern UFUNEXPORT int UF_MODL_ask_block_parms(
tag_t feature_obj_id ,/* <I>
                      A feature object identifier
                      */
int edit ,/* <I>
          This is an unused flag. It used to determine whether
          to return the right-hand side or both sides of an
          expression. Currently, both sides of an expression
          are returned.
          */
char * size[3]  /* <OF>
                Block dimension (length , width , height)
                The string space allocated for the three elements
                should be freed via UF_free when they are not used.
                */
);

/********************************************************************
Gets cone parameters.

Environment: Internal  and  External
See Also:
History:
********************************************************************/
extern UFUNEXPORT int UF_MODL_ask_cone_parms(
tag_t feature_obj_id ,/* <I>
                      A feature object identifier
                      */
int edit ,/* <I>
          This is an unused flag. It used to determine whether
          to return the right-hand side or both sides of an
          expression. Currently, both sides of an expression
          are returned.
          */
char ** base_diameter ,/* <OF>
                       Base diameter.  This must be freed by calling UF_free.
                       */
char ** top_diameter ,/* <OF>
                      Top diameter.  This must be freed by calling UF_free.
                      */
char ** height ,/* <OF>
                Cone height.  This must be freed by calling UF_free.
                */
char ** half_angle  /* <OF>
                    Cone angle.  This must be freed by calling UF_free.
                    */
);

/********************************************************************
Gets cylinder parameters.

Environment: Internal  and  External
See Also:
History:
********************************************************************/
extern UFUNEXPORT int UF_MODL_ask_cylinder_parms(
tag_t feature_obj_id ,/* <I>
                      A feature object identifier
                      */
int edit ,/* <I>
          This is an unused flag. It used to determine whether
          to return the right-hand side or both sides of an
          expression. Currently, both sides of an expression
          are returned.
          */
char ** diameter ,/* <OF>
                  Cylinder diameter.  This must be freed by calling UF_free.
                  */
char ** height  /* <OF>
                Cylinder height.  This must be freed by calling UF_free.
                */
);

/********************************************************************
Gets sphere parameters.

Environment: Internal  and  External
See Also:
History:
********************************************************************/
extern UFUNEXPORT int UF_MODL_ask_sphere_parms(
tag_t feature_obj_id ,/* <I>
                      A feature object identifier
                      */
int edit ,/* <I>
          This is an unused flag. It was used to determine
          whether to return the right-hand side or both sides
          of an expression. Currently, both sides of an
          expression are returned.
          */
char ** diameter  /* <OF>
                  Sphere diameter.  This must be freed by
                  calling UF_free.
                  */
);


#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif     /* UF_MODL_PRIMITIVES_H_INCLUDED */
