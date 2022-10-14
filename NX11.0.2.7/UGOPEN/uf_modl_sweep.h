/*****************************************************************************
             Copyright (c) 1998-2002 Unigraphics Solutions Inc.
                       Unpublished - All Rights Reserved



File description:
    Open API modeling routines to create, edit and inquire about sweeps.
*****************************************************************************/

#ifndef UF_MODL_SWEEP_H_INCLUDED
#define UF_MODL_SWEEP_H_INCLUDED


/***************************************************************************

  ***************************************************************************/

#include <uf_defs.h>
#include <uf_modl_types.h>
#include <libufun_exports.h>

#ifdef __cplusplus
extern "C" {
#endif

/****************************************************************************
Creates an extruded body. The taper angle and limit variables are
character strings so that expressions may be input if desired. You can
only use lines and arcs when using the taper option. Also, if you
extrude an open profile, you must set the taper angle to zero. In the
example code we opted not to use this option so we set the value
equal to zero (char *taper_angle = "0.0"). If you have a circle inside
the boundary of your closed generator curves, the taper angle for the
circle is opposite in sign. For example, if you specify a taper angle of 1
degree (char *taper_angle = "1.0"), the taper angle for the circle is
minus 1 degree. See the Modeling User manual for more details on
the taper angle.

The profile created by the object list must be contiguous.


Environment: Internal  and  External
See Also: 
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_create_extruded(
uf_list_p_t objects ,/* <I>
                     List of objects to be extruded.
                     */
char * taper_angle ,/* <I>
                    Taper angle (in degrees).
                    */
char * limit[2] ,/* <I>
               Limit of extrusion. This is declared as:
               char *limit[2]. The first value is the start value of
               the extrusion and the second value is the end of the
               extrusion (see the example program).
               */
double point[3] ,/* <I>
                 not used
                 */
double direction[3] ,/* <I>
                     Extrusion axis.
                     */
UF_FEATURE_SIGN sign ,/* <I>
                      The sign of the operation to be performed.
                       UF_NULLSIGN = create new target solid
                       UF_POSITIVE = add to target solid
                       UF_NEGATIVE = subtract from target solid
                       UF_UNSIGNED = intersect with target solid
                      */
uf_list_p_t * features  /* <OF,free:UF_MODL_delete_list>
                        List of feature identifiers created.  This list
                        must be freed by calling UF_MODL_delete_list.
                        */
);

/*************************************************************************
Creates an extruded body, and performs Boolean operation with given target
body.

Environment: Internal  and  External
See Also:   UF_MODL_create_extruded
History: Originally released in V16.0.
*************************************************************************/
extern UFUNEXPORT int UF_MODL_create_extruded1 (
uf_list_p_t objects ,/* <I>
                     List of objects to be extruded.
                     */
char * taper_angle ,/* <I>
                    Taper angle (in degrees).
                    */
char *limit[2] ,/* <I>
               Limit of extrusion. This is declared as:
               char *limit[2]. The first value is the start value of
               the extrusion and the second value is the end of the
               extrusion (see the example program).
               */
double point[3] ,/* <I>
                 not used
                 */
double direction[3],/* <I>
                     Extrusion axis.
                     */
UF_FEATURE_SIGN sign,/* <I>
                      The sign of the operation to be performed.
                       UF_NULLSIGN = create new target solid
                       UF_POSITIVE = add to target solid
                       UF_NEGATIVE = subtract from target solid
                       UF_UNSIGNED = intersect with target solid
                      */
tag_t target_body,     /* <I>  Target body to perform Boolean*/
uf_list_p_t * features  /* <OF,free:UF_MODL_delete_list>
                        List of feature identifiers created.  This list
                        must be freed by calling UF_MODL_delete_list.
                        */
);

/****************************************************************************
Creates an extruded body or bodies.

Multiple profiles may be used as input for the object list. Each
contiguous profile will create an extrusion feature. The modeling
distance tolerance will be used to define each profile.


Environment: Internal  and  External
See Also:   UF_MODL_create_extruded
History: Originally released in V18.0.
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_create_extruded2(
uf_list_p_t objects ,/* <I>
                     List of objects to be extruded.
                     */
char * taper_angle ,/* <I>
                    Taper angle (in degrees).
                    */
char *limit[2] ,/* <I>
               Limit of extrusion. This is declared as:
               char *limit[2]. The first value is the start value of
               the extrusion and the second value is the end of the
               extrusion (see the example program).
               */
double point[3] ,/* <I>
                 not used
                 */
double direction[3] ,/* <I>
                     Extrusion axis.
                     */
UF_FEATURE_SIGN sign ,/* <I>
                      The sign of the operation to be performed.
                       UF_NULLSIGN = create new target solid
                       UF_POSITIVE = add to target solid
                       UF_NEGATIVE = subtract from target solid
                       UF_UNSIGNED = intersect with target solid
                      */
uf_list_p_t * features  /* <OF,free:UF_MODL_delete_list>
                        List of feature identifiers created.  This list
                        must be freed by calling UF_MODL_delete_list.
                        */
);

/****************************************************************************
Creates an extruded solid body along a specified path.

Environment: Internal  and  External
See Also:
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_create_extruded_path(
uf_list_p_t objects ,/* <I>
                     List of objects or one section builder,
                     but not both, to be extruded.
                     */
uf_list_p_t path_objects ,/* <I>
                          List of objects or one section builder, but not
                          both, for providing a path for the extrusion.
                          */
double point[3] ,/* <I>
                 Point
                 */
double direction[3] ,/* <I>
                     Not used, can be set as (0,0,1)
                     */
UF_FEATURE_SIGN sign ,/* <I>
                      Sign of the operation to be performed:
                       0 = create a new target solid
                       1 = add to a target solid
                       2 = subtract from a target solid
                       3 = intersect with a target solid
                      */
uf_list_p_t * features  /* <OF,free:UF_MODL_delete_list>
                        List of feature identifiers created.  This list
                        must be freed by calling UF_MODL_delete_list.
                        */
);

/*********************************************************************
Creates an extruded solid body along a specified path, and performs Boolean
operation with given target body.

Environment: Internal  and  External
See Also:  UF_MODL_create_extruded_path
History: Originally released in V16.0.
******************************************************************/
extern UFUNEXPORT int UF_MODL_create_extruded_path1(
uf_list_p_t objects ,/* <I>
                     List of objects or one section builder,
                     but not both, to be extruded.
                     */
uf_list_p_t path_objects ,/* <I>
                          List of objects or one section builder, but not
                          both, for providing a path for the extrusion.
                          */
double point[3] ,/* <I>
                 Point
                 */
double direction[3] ,/* <I>
                     Not used, can be set as (0,0,1).
                     */
UF_FEATURE_SIGN sign ,/* <I>
                      Sign of the operation to be performed:
                       0 = create a new target solid
                       1 = add to a target solid
                       2 = subtract from a target solid
                       3 = intersect with a target solid
                      */
tag_t target_body,    /*<I>  The target body to perform Boolean operation */
uf_list_p_t * features  /* <OF,free:UF_MODL_delete_list>
                        List of feature identifiers created.  This list
                        must be freed by calling UF_MODL_delete_list.
                        */
);

/****************************************************************************
Creates a revolved feature.


Environment: Internal  and  External
See Also: UF_MODL_create_extrusion
          
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_create_revolution(
tag_t * objects ,/* <I,len:object>
                 Array of objects or one section builder object tag
                 but not both, to be revolved
                 */
int  object ,/* <I>
             Count of objects
             */
UF_MODL_SWEEP_TRIM_object_p_t trim_data ,/* <I>
                                             Pointer to structure for trimming
                                             data
                                             */
char * limit[2] ,/* <I>
               Limit of revolution.
               */
char * offsets[2] ,/* <I>
                   Offsets for open strings
                   */
double region_point[3] ,/* <I>
                        Point on region of object
                        */
logical  region_specified ,/* <I>
                           True or False for region desired
                           */
logical  solid_creation ,/* <I>
                         If the body_type preference set by
                         UF_MODL_set_body_type_pref is
                         UF_MODL_SOLID_BODY, and
                         solid_creation is set to TRUE, then
                         UF_MODL_create_revolution creates solid
                         bodies if the input string is closed.  Otherwise,
                         sheet bodies are the result.
                         */
double axis_point[3] ,/* <I>
                      Point of origin for axis direction vector
                      */
double direction[3] ,/* <I>
                     Revolution axis direction vector.
                     */
UF_FEATURE_SIGN sign ,/* <I>
                      The sign of the operation to be performed.
                      UF_NULLSIGN = create new target solid
                      UF_POSITIVE = add to target solid
                      UF_NEGATIVE = subtract from target solid
                      UF_UNSIGNED = intersect with target solid
                      */
tag_t ** features ,/* <OF,len:number_of_features>
                   Array of revolved feature tags.  This must
                   be freed by calling UF_free.
                   */
int* number_of_features  /* <O>
                         Number of features returned
                         */
);

/***************************************************************************
Creates a revolved feature, and performs Boolean operation with given target
body.

Environment: Internal  and  External
See Also:  UF_MODL_create_revolution
History: Originally released in V16.0.
*********************************************************************/
extern UFUNEXPORT int UF_MODL_create_revolution1(
tag_t * objects ,/* <I,len:object>
                    Array of objects or one section builder object tag
                    but not both, to be revolved
                 */
int  object ,/* <I>
             Count of objects
             */
UF_MODL_SWEEP_TRIM_object_p_t trim_data ,/* <I>
                                             Pointer to structure for trimming
                                             data
                                             */
char * limit[2] ,/* <I>
               Limit of revolution.
               */
char * offsets[2] ,/* <I>
                   Offsets for open strings
                   */
double region_point[3] ,/* <I>
                        Point on region of object
                        */
logical  region_specified ,/* <I>
                           True or False for region desired
                           */
logical  solid_creation ,/* <I>
                         If the body_type preference set by
                         UF_MODL_set_body_type_pref is
                         UF_MODL_SOLID_BODY, and
                         solid_creation is set to TRUE, then
                         UF_MODL_create_revolution creates solid
                         bodies if the input string is closed.  Otherwise,
                         sheet bodies are the result.
                         */
double axis_point[3] ,/* <I>
                      Point of origin for axis direction vector
                      */
double direction[3] ,/* <I>
                     Revolution axis direction vector.
                     */
UF_FEATURE_SIGN sign ,/* <I>
                      The sign of the operation to be performed.
                      UF_NULLSIGN = create new target solid
                      UF_POSITIVE = add to target solid
                      UF_NEGATIVE = subtract from target solid
                      UF_UNSIGNED = intersect with target solid
                      */
tag_t target_body,        /* <I> target body to perform Boolean operation*/
tag_t ** features ,/* <OF,len:number_of_features>
                   Array of revolved feature tags.  This must
                   be freed by calling UF_free.
                   */
int* number_of_features /* <O>
                         Number of features returned
                         */
);

/****************************************************************************
Creates an extruded feature.  The resulting body is a solid if the input
string is closed and the solid_creation option is TRUE.  Otherwise a sheet
body results.  A sheet can not be tapered and the taper_angle must be set to
0.0.  The UF_MODL_SWEEP_TRIM_object structure is used to define the trim
objects.  The limits of extrusion are valid only if the
UF_MODL_SWEEP_TRIM_object structure is not specified (NULL).  The region
point corresponds to the point chosen after selecting intersecting objects.
If the region_point_specified is false then the region point is ignored.

Note that the offset direction is determined by the cross product of the
direction vector of the first profile segment and the extrusion direction
vector.  The direction of a segment follows the direction of the profile
flow instead of the parametric or mathematical direction of the segment.

The profile created by the object list must be contiguous.


Environment: Internal  and  External
See Also: 
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_create_extrusion(
tag_t * objects ,/* <I,len:object_count>
                 List of objects to be extruded
                 */
int  object_count ,/* <I>
                   Number of objects
                   */
UF_MODL_SWEEP_TRIM_object_p_t trim_data ,/* <I>
                                         Pointer to structure for trimming data
                                         */
char * taper_angle ,/* <I>
                    Taper Angle.  The taper angle can be non-zero only if
                    the body being created is a sheet body.
                    */
char * limits[2] ,/* <I>
                  Limits of extrusion.  Only valid if trim_data = NULL
                  */
char * offsets[2] ,/* <I>
                   Offsets for open strings
                   */
double region_point[3] ,/* <I>
                        Point on region desired
                        */
logical  region_specified ,/* <I>
                           True or False for region desired
                           */
logical  solid_creation ,/* <I>
                         If TRUE, create solid bodies if input string is
                         closed.  Otherwise, sheet bodies are the result.
                         */
double direction[3] ,/* <I>
                     Extrusion direction
                     */
UF_FEATURE_SIGN sign ,/* <I>
                      The sign of the operation to be performed.
                      UF_NULLSIGN = create new target solid
                      UF_POSITIVE = add to target solid
                      UF_NEGATIVE = subtract from target solid
                      UF_UNSIGNED = intersect with target solid
                      */
tag_t ** features ,/* <OF,len:number_of_features>
                           Array of extruded feature tags.  This must
                           be freed by calling UF_free.
                   */
int* number_of_features  /* <O>
                         Number of features returned
                         */
);

/***************************************************************************
Creates an extruded feature, and perform Boolean operation with a target body.

Environment: Internal  and  External
See Also:  UF_MODL_create_extrusion
History: Originally released in V16.0.
*********************************************************************/
extern UFUNEXPORT int UF_MODL_create_extrusion1(
tag_t * objects ,/* <I,len:object_count>
                 List of objects to be extruded
                 */
int  object_count ,/* <I>
                   Number of objects
                   */
UF_MODL_SWEEP_TRIM_object_p_t trim_data ,/* <I>
                                         Pointer to structure for trimming data
                                         */
char * taper_angle ,/* <I>
                    Taper Angle.
                    */
char * limits[2] ,/* <I>
                  Limits of extrusion.  Only valid if trim_data = NULL
                  */
char * offsets[2] ,/* <I>
                   Offsets for open strings
                   */
double region_point[3] ,/* <I>
                        Point on region desired
                        */
logical  region_specified ,/* <I>
                           True or False for region desired
                           */
logical  solid_creation ,/* <I>
                         If TRUE, create solid bodies if input string
                         closed.  Otherwise, sheet bodies are the result.
                         */
double direction[3] ,/* <I>
                     Extrusion direction
                     */
UF_FEATURE_SIGN sign ,/* <I>
                      The sign of the operation to be performed.
                      UF_NULLSIGN = create new target solid
                      UF_POSITIVE = add to target solid
                      UF_NEGATIVE = subtract from target solid
                      UF_UNSIGNED = intersect with target solid
                      */
tag_t  target_body,  /* <I>  target body to perform Boolean operation */
tag_t ** features ,/* <OF,len:number_of_features>
                   Array of extruded feature tags.  This must
                   be freed by calling UF_free.
                   */
int* number_of_features  /* <O>
                         Number of features returned
                         */
);

/****************************************************************************
Creates an extruded feature or features.

Multiple profiles may be used as input for the object list. Each
contiguous profile will create an extrusion feature. The modeling
distance tolerance will be used to define each profile.


Environment: Internal  and  External
See Also:  UF_MODL_create_extrusion
History: Originally released in V18.0.
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_create_extrusion2(
tag_t * objects ,/* <I,len:object_count>
                 List of objects to be extruded
                 */
int  object_count ,/* <I>
                   Number of objects
                   */
UF_MODL_SWEEP_TRIM_object_p_t trim_data ,/* <I>
                                         Pointer to structure for trimming data
                                         */
char * taper_angle ,/* <I>
                    Taper Angle.  The taper angle can be non-zero only if
                    the body being created is a sheet body.
                    */
char * limits[2] ,/* <I>
                  Limits of extrusion.  Only valid if trim_data = NULL
                  */
char * offsets[2] ,/* <I>
                   Offsets for open strings
                   */
double region_point[3] ,/* <I>
                        Point on region desired
                        */
logical  region_specified ,/* <I>
                           True or False for region desired
                           */
logical  solid_creation ,/* <I>
                         If TRUE, create solid bodies if input string is
                         closed.  Otherwise, sheet bodies are the result.
                         */
double direction[3] ,/* <I>
                     Extrusion direction
                     */
UF_FEATURE_SIGN sign ,/* <I>
                      The sign of the operation to be performed.
                      UF_NULLSIGN = create new target solid
                      UF_POSITIVE = add to target solid
                      UF_NEGATIVE = subtract from target solid
                      UF_UNSIGNED = intersect with target solid
                      */
tag_t ** features ,/* <OF,len:number_of_features>
                   Array of extruded feature tags.  This must
                   be freed by calling UF_free.
                   */
int* number_of_features  /* <O>
                         Number of features returned
                         */
);

/****************************************************************************
Creates an extruded feature.  The resulting body is a solid if the input
string is closed and the solid_creation option is TRUE.  Otherwise a sheet
body results.  A sheet can not be tapered and the taper_angle must be set to
0.0.  The UF_MODL_SWEEP_TRIM_object structure is used to define the trim
objects.  The trim_options is used to define the trim options if the
UF_MODL_SWEEP_TRIM_object structure is specified.

The limits of extrusion are valid only if the UF_MODL_SWEEP_TRIM_object
structure is not specified (NULL). The region point corresponds to the point
chosen after selecting intersecting objects. If the region_point_specified is
false then the region point is ignored.

Environment: Internal  and  External
See Also: UF_MODL_create_extrusion
History: Originally released in V15.0
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_create_extrude_trim_opts
(
    tag_t  *extrude_array,  /* <I,len:extrude_count>
                                   List of objects to be extruded.
                            */
    int extrude_count,      /* <I>
                            Count of the objects to be extruded.
                            */
    UF_MODL_SWEEP_TRIM_object_p_t trim_ptr,/* <I>
                                           The structure that contains the
                                           trimming data.
                                           */
    UF_MODL_SWEEP_TRIM_OPTS trim_options, /* <I>
                 Trimming options:
                    DO_NOT_EXTEND_TRIM_FACE = do not extend the trimming face,
                    DO_NOT_EXTEND_AND_EXTEND_TRIM_FACE = first do not extend
                       the trimming face and perform boolean operation.
                       If fails, extend the trimming face and perform boolean.
                    EXTEND_FIRST_TRIM_FACE = extend the first trimming face,
                    EXTEND_SECOND_TRIM_FACE = extend the second trimming face,
                    EXTEND_BOTH_TRIM_FACES = extend both trimming faces */

    char *taper_angle, /*<I>
                       The taper angle for the extrusion.
                       */
    char *limits[2],     /* <I,len:2> extrude_count
                       The limits of the extrusion.  Only used if the
                       trim_ptr argument is NULL.
                       */
    char *offsets[2],    /* <I,len:2>
                       The offsets for open strings
                       */
    double  region_point[3], /* <I>
                            The point on the region desired.
                            */
    logical cut_specified,  /* <I>
                            TRUE or FALSE for region desired.
                            */
    logical solid_body_creation, /* <I>
                                 If TRUE, create solid bodies if the input
                                 string is closed.  Otherwise sheet bodies will
                                 be created.
                                 */
    double dir[3],            /* <I>
                             The extrusion direction.
                             */
    UF_FEATURE_SIGN sign,    /* <I>
                             The sign of the operation to be performed:
                                UF_POSITIVE = add to target solid
                                UF_NEGATIVE = subtract from target solid
                                UF_UNSIGNED = intersect with target solid
                             */
    tag_t **objects,   /* <OF,len:object_count>
                       An array of extruded feature tags.  This must be freed
                       by calling UF_free.
                       */
    int *object_count  /* <O>
                       The number of features returned in the objects array.
                       */
);

/***************************************************************************
Creates an extruded feature with trimming options, and perform Boolean
operation with given target body.

Environment: Internal  and  External
See Also:   UF_MODL_create_extrude_trim_opts
History: Originally released in V16.0.
***********************************************************************/
extern UFUNEXPORT int UF_MODL_create_extrude_trim_opts1
(
    tag_t  *extrude_array,  /* <I,len:extrude_count>
                            List of objects to be extruded.
                            */
    int extrude_count,      /* <I>
                            Count of the objects to be extruded.
                            */
    UF_MODL_SWEEP_TRIM_object_p_t trim_ptr,/* <I>
                                           The structure that contains the
                                           trimming data.
                                           */
    UF_MODL_SWEEP_TRIM_OPTS trim_options, /* <I>
                 Trimming options:
                    DO_NOT_EXTEND_TRIM_FACE = do not extend the trimming face,
                    DO_NOT_EXTEND_AND_EXTEND_TRIM_FACE = first do not extend
                       the trimming face and perform boolean operation.
                       If fails, extend the trimming face and perform boolean.
                    EXTEND_FIRST_TRIM_FACE = extend the first trimming face,
                    EXTEND_SECOND_TRIM_FACE = extend the second trimming face,
                    EXTEND_BOTH_TRIM_FACES = extend both trimming faces */

    char *taper_angle, /*<I>
                       The taper angle for the extrusion.
                       */
    char *limits[2],     /* <I,len:2> extrude_count
                       The limits of the extrusion.  Only used if the
                       trim_ptr argument is NULL.
                       */
    char *offsets[2],    /* <I,len:2>
                       The offsets for open strings
                       */
    double  region_point[3], /* <I>
                            The point on the region desired.
                            */
    logical cut_specified,  /* <I>
                            TRUE or FALSE for region desired.
                            */
    logical solid_body_creation, /* <I>
                                 If TRUE, create solid bodies if the input
                                 string is closed.  Otherwise sheet bodies will
                                 be created.
                                 */
    double dir[3],            /* <I>
                             The extrusion direction.
                             */
    UF_FEATURE_SIGN sign,    /* <I>
                             The sign of the operation to be performed:
                                UF_POSITIVE = add to target solid
                                UF_NEGATIVE = subtract from target solid
                                UF_UNSIGNED = intersect with target solid
                             */
   tag_t target_body,  /* <I> Target body to perform Boolean operation */
   tag_t **objects,   /* <OF,len:object_count>
                       An array of extruded feature tags.  This must be freed
                       by calling UF_free.
                       */
   int *object_count  /* <O>
                       The number of features returned in the objects array.
                       */
);

/****************************************************************************
Creates an extruded feature using sweep along a guide.


Environment: Internal  and  External
See Also: UF_MODL_create_extrusion
          
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_create_extrusion_path(
tag_t * objects ,/* <I,len:object_count>
                 Section Objects.
                 */
int  object_count ,/* <I>
                   Number of section objects
                   */
tag_t * path_objects ,/* <I,len:path>
                      Path objects
                      */
int path ,/* <I>
          Number of path objects
          */
UF_MODL_SWEEP_TRIM_object_p_t trim_data ,/* <I>
                                         Not used
                                         */
char * offsets[2] ,/* <I>
                   Offsets
                   */
double region_point[3] ,/* <I>
                        Point in desired region
                        */
logical  region_specified ,/* <I>
                           True or False for region desired
                           */
logical  solid_creation ,/* <I>
                         If TRUE, create solid bodies if input string
                         closed.  Otherwise, sheet bodies are the result.
                         */
UF_FEATURE_SIGN sign ,/* <I>
                      The sign of the operation to be performed.
                      UF_NULLSIGN = create new target solid
                      UF_POSITIVE = add to target solid
                      UF_NEGATIVE = subtract from target solid
                      UF_UNSIGNED = intersect with target solid
                      */
tag_t **features ,/* <OF,len:number_of_features>
                  Array of extrude feature tags. This must be freed
                  by calling UF_free.
                  */
int* number_of_features  /* <O>
                         Number of features returned
                         */
);


/****************************************************************************
Creates an extruded feature using sweep along a guide, and performs Boolean
operation with given target body.

Environment: Internal  and  External
See Also:  UF_MODL_create_extrusion_path
History: Originally released in V16.0.
*********************************************************************/
extern UFUNEXPORT int UF_MODL_create_extrusion_path1(
tag_t * objects ,/* <I,len:object_count>
                 Section Objects.
                 */
int  object_count ,/* <I>
                   Number of section objects
                   */
tag_t * path_objects ,/* <I,len:path>
                      Path objects
                      */
int path ,/* <I>
          Number of path objects
          */
UF_MODL_SWEEP_TRIM_object_p_t trim_data ,/* <I>
                                         Not used
                                         */
char * offsets[2] ,/* <I>
                   Offsets
                   */
double region_point[3] ,/* <I>
                        Point in desired region
                        */
logical  region_specified ,/* <I>
                           True or False for region desired
                           */
logical  solid_creation ,/* <I>
                         If TRUE, create solid bodies if input string
                         closed.  Otherwise, sheet bodies are the result.
                         */
UF_FEATURE_SIGN sign ,/* <I>
                      The sign of the operation to be performed.
                      UF_NULLSIGN = create new target solid
                      UF_POSITIVE = add to target solid
                      UF_NEGATIVE = subtract from target solid
                      UF_UNSIGNED = intersect with target solid
                      */
tag_t   target_body,     /* <I> Boolean target */
tag_t **features ,/* <OF,len:number_of_features>
                  Array of extrude feature tags. This must be freed
                  by calling UF_free.
                  */
int* number_of_features /* <O>
                         Number of features returned
                         */
);

/****************************************************************************
Creates an extruded feature.  This function behaves like
UF_MODL_create_extrusion, except that the extruded direction is determined by
the direction of the input datum.  The resulting body is a solid if the input
string is closed and the solid_creation option is TRUE.  Otherwise a sheet
body results.  A sheet can not be tapered and the taper_angle must be set to
0.0.  The UF_MODL_SWEEP_TRIM_object structure is used to define the trim
objects.  The trim_options is used to define the trim options if the
UF_MODL_SWEEP_TRIM_object structure is specified.

The limits of extrusion are valid only if the UF_MODL_SWEEP_TRIM_object
structure is not specified (NULL). The region point corresponds to the point
chosen after selecting intersecting objects. If the region_point_specified is
false then the region point is ignored.

Environment: Internal  and  External
See Also: UF_MODL_create_extrusion
History: Originally released in V15.0
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_create_extrusion_dir
(
    tag_t  *extrude_array,  /* <I,len:extrude_count>
                                   List of objects to be extruded.
                            */
    int extrude_count,      /* <I>
                            Count of the objects to be extruded.
                            */
    UF_MODL_SWEEP_TRIM_object_p_t trim_ptr,/* <I>
                                           The structure that contains the
                                           trimming data.
                                           */
    UF_MODL_SWEEP_TRIM_OPTS trim_options, /* <I>
                 Trimming options:
                    DO_NOT_EXTEND_TRIM_FACE = do not extend the trimming face,
                    DO_NOT_EXTEND_AND_EXTEND_TRIM_FACE = first do not extend
                       the trimming face and perform boolean operation.
                       If fails, extend the trimming face and perform boolean.
                    EXTEND_FIRST_TRIM_FACE = extend the first trimming face,
                    EXTEND_SECOND_TRIM_FACE = extend the second trimming face,
                    EXTEND_BOTH_TRIM_FACES = extend both trimming faces */
    char *taper_angle, /*<I>
                       The taper angle for the extrusion.
                       */
    char *limits[2],     /* <I> extrude_count
                       The limits of the extrusion.  Only used if the
                       trim_ptr argument is NULL.
                       */
    char *offsets[2],    /* <I>
                       The offsets for open strings
                       */
    double  region_point[3], /* <I>
                            The point on the region desired.
                            */
    logical cut_specified,  /* <I>
                            TRUE or FALSE for region desired.
                            */
    logical solid_body_creation, /* <I>
                                 If TRUE, create solid bodies if the input
                                 string is closed.  Otherwise sheet bodies will
                                 be created.
                                 */
    tag_t datum_eid, /* <I>
                     Object identifier of a datum which will provide the
                     direction of the extrusion.
                     */
    UF_FEATURE_SIGN sign,    /* <I>
                             The sign of the operation to be performed:
                                UF_POSITIVE = add to target solid
                                UF_NEGATIVE = subtract from target solid
                                UF_UNSIGNED = intersect with target solid
                             */
    tag_t **objects,   /* <OF,len:object_count>
                       An array of extruded feature tags.  This must be freed
                       by calling UF_free.
                       */
    int *object_count  /* <O>
                       The number of features returned in the objects array.
                       */
);

/****************************************************************************
Creates an extruded feature.  This function behaves like
UF_MODL_create_extrusion, except that the extruded direction is determined by
the flag reverse_default and the direction of the input sketch.  The resulting
body is a solid if the input string is closed and the solid_creation option is
TRUE.  Otherwise a sheet body results.  A sheet can not be tapered and the
taper_angle must be set to 0.0.  The UF_MODL_SWEEP_TRIM_object structure is
used to define the trim objects.  The trim_options is used to define the trim
options if the UF_MODL_SWEEP_TRIM_object structure is specified.

The limits of extrusion are valid only if the UF_MODL_SWEEP_TRIM_object
structure is not specified (NULL). The region point corresponds to the point
chosen after selecting intersecting objects. If the region_point_specified is
false then the region point is ignored.

Environment: Internal  and  External
See Also: UF_MODL_create_extrusion
History: Originally released in V15.0
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_create_extrusion_default
(
    tag_t  *extrude_array,  /* <I,len:extrude_count>
                                   List of objects to be extruded.
                            */
    int extrude_count,      /* <I>
                            Count of the objects to be extruded.
                            */
    UF_MODL_SWEEP_TRIM_object_p_t trim_ptr,/* <I>
                                           The structure that contains the
                                           trimming data.
                                           */
    UF_MODL_SWEEP_TRIM_OPTS trim_options, /* <I>
                 Trimming options:
                    DO_NOT_EXTEND_TRIM_FACE = do not extend the trimming face,
                    DO_NOT_EXTEND_AND_EXTEND_TRIM_FACE = first do not extend
                       the trimming face and perform boolean operation.
                       If fails, extend the trimming face and perform boolean.
                    EXTEND_FIRST_TRIM_FACE = extend the first trimming face,
                    EXTEND_SECOND_TRIM_FACE = extend the second trimming face,
                    EXTEND_BOTH_TRIM_FACES = extend both trimming faces */
    char *taper_angle, /*<I>
                       The taper angle for the extrusion.
                       */
    char *limits[2],     /* <I> extrude_count
                       The limits of the extrusion.  Only used if the
                       trim_ptr argument is NULL.
                       */
    char *offsets[2],    /* <I>
                       The offsets for open strings
                       */
    double  region_point[3], /* <I>
                            The point on the region desired.
                            */
    logical cut_specified,  /* <I>
                            TRUE or FALSE for region desired.
                            */
    logical solid_body_creation, /* <I>
                                 If TRUE, create solid bodies if the input
                                 string is closed.  Otherwise sheet bodies will
                                 be created.
                                 */
    tag_t sketch_eid,  /* <I>
                       The object identifier of a sketch which will be used to
                       determine the direction of the extrusion.
                       */
    logical reverse_default, /* <I>
                             If TRUE, then reverse the direction of the sketch.
                             If FALSE, then use the same direction as the
                             sketch.
                             */
    UF_FEATURE_SIGN sign,    /* <I>
                             The sign of the operation to be performed:
                                UF_POSITIVE = add to target solid
                                UF_NEGATIVE = subtract from target solid
                                UF_UNSIGNED = intersect with target solid
                             */
    tag_t **objects,   /* <OF,len:object_count>
                       An array of extruded feature tags.  This must be freed
                       by calling UF_free.
                       */
    int *object_count  /* <O>
                       The number of features returned in the objects array.
                       */
);

/****************************************************************************
Creates an extruded feature, and perform Boolean operation with a target body.

Environment: Internal  and  External
See Also: UF_MODL_create_extrusion_default
History: originally released in V.16.0.
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_create_extrusion_default1
(
    tag_t  *extrude_array,  /* <I,len:extrude_count>
                                   List of objects to be extruded.
                            */
    int extrude_count,      /* <I>
                            Count of the objects to be extruded.
                            */
    UF_MODL_SWEEP_TRIM_object_p_t trim_ptr,/* <I>
                                           The structure that contains the
                                           trimming data.
                                           */
    UF_MODL_SWEEP_TRIM_OPTS trim_options, /* <I>
                 Trimming options:
                    DO_NOT_EXTEND_TRIM_FACE = do not extend the trimming face,
                    DO_NOT_EXTEND_AND_EXTEND_TRIM_FACE = first do not extend
                       the trimming face and perform boolean operation.
                       If fails, extend the trimming face and perform boolean.
                    EXTEND_FIRST_TRIM_FACE = extend the first trimming face,
                    EXTEND_SECOND_TRIM_FACE = extend the second trimming face,
                    EXTEND_BOTH_TRIM_FACES = extend both trimming faces */
    char *taper_angle, /*<I>
                       The taper angle for the extrusion.
                       */
    char *limits[2],     /* <I>
                       The limits of the extrusion.  Only used if the
                       trim_ptr argument is NULL.
                       */
    char *offsets[2],    /* <I,len:2>
                       The offsets for open strings
                       */
    double  region_point[3], /* <I>
                            The point on the region desired.
                            */
    logical cut_specified,  /* <I>
                            TRUE or FALSE for region desired.
                            */
    logical solid_body_creation, /* <I>
                                 If TRUE, create solid bodies if the input
                                 string is closed.  Otherwise sheet bodies will
                                 be created.
                                 */
    tag_t sketch_eid,  /* <I>
                       The object identifier of a sketch which will be used to
                       determine the direction of the extrusion.
                       */
    logical reverse_default, /* <I>
                             If TRUE, then reverse the direction of the sketch.  If
                             FALSE, then use the same direction as the sketch.
                             */
    UF_FEATURE_SIGN sign,    /* <I>
                             The sign of the operation to be performed:
                                UF_POSITIVE = add to target solid
                                UF_NEGATIVE = subtract from target solid
                                UF_UNSIGNED = intersect with target solid
                             */
    tag_t   target_body,     /* <I> Boolean target */
    tag_t **objects,   /* <OF,len:object_count>
                       An array of extruded feature tags.  This must be freed
                       by calling UF_free.
                       */
    int *object_count  /* <O>
                       The number of features returned in the objects array.
                       */
);


/****************************************************************************
Creates a revolved feature.  This function behaves like
UF_MODL_create_revolution, except the revolved point and direction are
determined by the direction of the input datum.


Environment: Internal  and  External
See Also: UF_MODL_create_revolution
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_create_revolution_dir
(
tag_t * objects ,/* <I,len:object>
                    Array of objects or one section builder object tag
                    but not both, to be revolved
                 */
int  object ,/* <I>
             Count of objects
             */
UF_MODL_SWEEP_TRIM_object_p_t trim_data ,/* <I>
                                         Pointer to structure for trimming data
                                         */
char *limit[2] ,/* <I>
               Limit of the revolution.
               */
char *offsets[2] ,/* <I>
                Offsets for open strings
                */
double region_point[3] ,/* <I>
                       Point on region of object
                       */
logical  region_specified ,/* <I>
                           True or False for region desired
                           */
logical  solid_creation ,/* <I>
                         If the body_type preference set by
                         UF_MODL_set_body_type_pref is UF_MODL_SOLID_BODY, and
                         solid_creation is set to TRUE, then
                         UF_MODL_create_revolution creates solid bodies if the
                         input string is closed.  Otherwise, sheet bodies
                         are the result.
                         */
tag_t datum_tag, /* <I>
                 Object identifier of the datum which is to be used to determine
                 the direction of the revolve.
                 */
UF_FEATURE_SIGN sign ,/* <I>
                      The sign of the operation to be performed.
                      UF_NULLSIGN = create new target solid
                      UF_POSITIVE = add to target solid
                      UF_NEGATIVE = subtract from target solid
                      UF_UNSIGNED = intersect with target solid
                      */
tag_t ** features ,/* <OF,len:number_of_features>
                   Array of revolved feature tags.  This must
                   be freed by calling UF_free.
                   */
int* number_of_features  /* <O>
                         Number of features returned
                         */
);


/****************************************************************************
Creates a solid of revolution.

Environment: Internal  and  External
See Also:
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_create_revolved(
uf_list_p_t obj_id_list ,/* <I>
                           List of objects or one section builder object tag
                           but not both, to be revolved
                         */
char *limit[2] ,/* <I>
               Limits of revolution. The declaration should be
               *limit[2], where limit[0] = start angle and limit[1] =
               end angle. Angles are in degrees.
               */
double point[3] ,/* <I>
                 Point
                 */
double direction[3] ,/* <I>
                     Revolution axis.
                     */
UF_FEATURE_SIGN sign ,/* <I>
                      The sign of the operation to be performed.
                      UF_NULLSIGN = create new target solid
                      UF_POSITIVE = add to target solid
                      UF_NEGATIVE = subtract from target solid
                      UF_UNSIGNED = intersect with target solid
                      */
uf_list_p_t * feature_list  /* <OF,free:UF_MODL_delete_list>
                            List of feature identifiers created.  This
                            list must be freed by calling UF_MODL_delete_list.
                            */
);

/*************************************************************************
Creates a solid of revolution, and performs Boolean operation with given
target body.

Environment: Internal  and  External
See Also:  UF_MODL_create_revolved
History: Originally released in V16.0.
*********************************************************************/
extern UFUNEXPORT int UF_MODL_create_revolved1(
uf_list_p_t obj_id_list ,/* <I>
                            List of objects or one section builder object tag
                            but not both, to be revolved
                         */
char *limit[2] ,/* <I>
               Limits of revolution. The declaration should be
               *limit[2], where limit[0] = start angle and limit[1] =
               end angle. Angles are in degrees.
               */
double point[3] ,/* <I>
                 Point
                 */
double direction[3] ,/* <I>
                     Revolution axis.
                     */
UF_FEATURE_SIGN sign ,/* <I>
                      The sign of the operation to be performed.
                      UF_NULLSIGN = create new target solid
                      UF_POSITIVE = add to target solid
                      UF_NEGATIVE = subtract from target solid
                      UF_UNSIGNED = intersect with target solid
                      */
tag_t         target_body,   /* <I> Boolean target */
uf_list_p_t * feature_list  /* <OF,free:UF_MODL_delete_list>
                            List of feature identifiers created.  This
                            list must be freed by calling UF_MODL_delete_list.
                            */
);


/****************************************************************************
Creates a tube, or cable, depending on the inner and outer diameters
specified. A cable is produced if the inner diameter is set to zero. The
output of this function is a list of feature object identifiers. The limit
variable is of type character to allow for expressions.


Environment: Internal  and  External
See Also: 
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_create_tube(
uf_list_p_t  path_list ,/* <I>
                        List of objects or one section builder object tag,
                        but not both, for the path.
                        */
char *limit[2] ,/* <I>
               Inner diameter and outer diameter of the tube. You
               can declare this as char *limit[2], where:
                       [0] =  outer diameter expression
                       [1] = inner diameter expression
               */
UF_FEATURE_SIGN sign ,/* <I>
                      The sign of the operation to be performed.
                      UF_NULLSIGN = create new target solid
                      UF_POSITIVE = add to target solid
                      UF_NEGATIVE = subtract from target solid
                      UF_UNSIGNED = intersect with target solid
                      */
uf_list_p_t * feature_list  /* <OF,free:UF_MODL_delete_list>
                            Feature object identifier list for tube created.
                            This list must be freed by calling
                            UF_MODL_delete_list.
                            */
);

/************************************************************************
Creates a tube, or cable, and performs Boolean operation with given target body.

Environment: Internal  and  External
See Also:  UF_MODL_create_tube
History: Originally released in V16.0.
************************************************************************/
extern UFUNEXPORT int UF_MODL_create_tube1(
uf_list_p_t  path_list ,/* <I>
                        List of objects or one section builder object tag,
                        but not both, for the path.
                        */
char *limit[2] ,/* <I>
               Inner diameter and outer diameter of the tube. You
               can declare this as char *limit[2], where:
                       [0] =  outer diameter expression
                       [1] = inner diameter expression
               */
UF_FEATURE_SIGN sign ,/* <I>
                      The sign of the operation to be performed.
                      UF_NULLSIGN = create new target solid
                      UF_POSITIVE = add to target solid
                      UF_NEGATIVE = subtract from target solid
                      UF_UNSIGNED = intersect with target solid
                      */
tag_t         target_body,   /* <I> Boolean target */
uf_list_p_t * feature_list  /* <OF,free:UF_MODL_delete_list>
                            Feature object identifier list for tube created.
                            This list must be freed by calling
                            UF_MODL_delete_list.
                            */
);

/****************************************************************************
Creates a tube feature.


Environment: Internal  and  External
See Also: 
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_create_trimmed_tube(
tag_t * objects ,/* <I,len:object_count>
                 Array of objects or one section builder object tag,
                 but not both, for the tube path
                 */
int  object_count ,/* <I>
                   Number of objects
                   */
UF_MODL_SWEEP_TRIM_object_p_t trim_data ,/* <I>
                                         Not used
                                         */
char * diameters[2] ,/* <I>
                     [0] = Outer Diameter
                     [1] = Inner diameter
                     */
UF_FEATURE_SIGN sign ,/* <I>
                      The sign of the operation to be performed.
                      UF_NULLSIGN = create new target solid
                      UF_POSITIVE = add to target solid
                      UF_NEGATIVE = subtract from target solid
                      UF_UNSIGNED = intersect with target solid
                      */
tag_t ** features ,/* <OF,len:number_of_features>
                   Array of tube feature tags
                   */
int* number_of_features  /* <O>
                         Number of features returned
                         */
);
/***************************************************************************
Creates a tube feature, and perform Boolean operation with given target body.

Environment: Internal  and  External
See Also:   UF_MODL_create_trimmed_tube
History: Originally released in V16.0.
*****************************************************************/
extern UFUNEXPORT int UF_MODL_create_trimmed_tube1(
tag_t * objects ,/* <I,len:object_count>
                 Array of objects or one section builder object tag,
                 but not both, for the tube path
                 */
int  object_count ,/* <I>
                   Number of objects
                   */
UF_MODL_SWEEP_TRIM_object_p_t trim_data ,/* <I>
                                         Not used
                                         */
char * diameters[2] ,/* <I>
                     [0] = Outer Diameter
                     [1] = Inner diameter
                     */
UF_FEATURE_SIGN sign ,/* <I>
                      The sign of the operation to be performed.
                      UF_NULLSIGN = create new target solid
                      UF_POSITIVE = add to target solid
                      UF_NEGATIVE = subtract from target solid
                      UF_UNSIGNED = intersect with target solid
                      */
tag_t         target_body,   /* <I> Boolean target */
tag_t ** features ,/* <OF,len:number_of_features>
                   Array of tube feature tags
                   */
int* number_of_features  /* <O>
                         Number of features returned
                         */
);

/****************************************************************************
Given an extrude feature, this function returns the extruded direction in
the parameter dir.  Given a revolve feature, this function returns the axis
point in the parameter pos and the axis direction in the parameter dir.

Environment: Internal  and  External
See Also:
History: Originally released in V15.0
****************************************************************************/
extern UFUNEXPORT int  UF_MODL_ask_sweep_direction(
tag_t  feature_id,   /* <I>
                     The feature ID
                     */
double pos[3],         /* <O>
                     The axis point for a revolve feature.  Not used for an
                     extrude feature.  This must be declared as double pos[3].
                     */
double dir[3]          /* <O>
                     The axis direction for a revolve feature.  For an extrude
                     feature the extruded direction.  This must be declared as
                     double dir[3].
                     */
);

/************************************************************************
 *  This function will replace the profile and/or guide curves/edges of
 *  a sweep feature that can be one of the following types, Extruded,
 *  Revolved, Sweep (Along a Guide), Cable/Tube.
 *
 *  The original and replacement curves/edges in the arrays original_profile/
 *  guide_objs and new_profile/guide_objs have to be contiguous.  The
 *  original strings will be replaced in the order of the original_profile/
 *  guide_objs array by the corresponding strings in the new_profile/guide_objs
 *  array.  If n_original_profile/guide_objs > n_new_profile/guide_objs,
 *  the last (n_original_profile/guide_objs - n_new_profile/guide_objs)
 *  strings in the original_profile/guide_objs array will be removed from
 *  the sweep featur's profile/guide.  If
 *  n_original_profile/guide_objs < n_new_profile/guide_objs, the last
 *  (n_new_profile/guide_objs - n_original_profile/guide_objs) strings in the
 *  new profile/guide array will be added to the feature.
 *
 *  It is suggested to use this function instead of UF_MODL_edit_sweep_curves
 *  if possible as UF_MODL_replace_sweep_strings has the edge/face tracking
 *  information retained when possible.
 *
 * Environment : Internal  and  External
 * See Also:  UF_MODL_edit_sweep_curves
 * History : Released in V15.0
 ************************************************************************/
extern UFUNEXPORT int UF_MODL_replace_sweep_strings
(
    tag_t             sweep_feature_id,
                      /* <I> Feature object identifier of sweep */
    int                   n_original_profile_objs,
                      /* <I> Number of contiguous original curves/edges in
                          the profile of the sweep feature to be replaced */
    tag_t            *original_profile_objs,
                      /* <I,len:n_original_profile_objs>
                          An array of contiguous original curves/edges in
                          the profile of the sweep feature to be replaced */
    int                   n_new_profile_objs,
                      /* <I> Number of contiguous curves/edges to replace
                          the curves/edges in the original_profile_objs. */
    tag_t            *new_profile_objs,
                      /* <I,len:n_new_profile_objs>
                          An array of contiguous curves/edges to replace
                          the curves/edges in the original_profile_objs. */
    int               n_original_guide_objs,
                      /* <I> Number of contiguous original curves/edges
                          in the guide of the sweep feature to be replaced. */
    tag_t            *original_guide_objs,
                      /* <I,len:n_original_guide_objs>
                          An array of contiguous original curves/edges
                          in the guide of the sweep feature to be replaced. */
    int               n_new_guide_objs,
                      /* <I> Number of contiguous curves/edges to replace
                          the curves/edges in the original_guide_objs. */
    tag_t            *new_guide_objs
                      /* <I,len:n_new_guide_objs>
                          An array of contiguous curves/edges to replace
                          the curves/edges in the original_guide_objs. */
);

/******************************************************************************
Removes and adds profile and guide curves of a sweep that can be one of the
following types, Extruded, Revolved, Sweep (along a Guide) and Cable/Tube.


Environment: Internal  and  External
See Also:
 UF_MODL_ask_sweep_curves
 UF_MODL_ask_sweep_of_udf
History:
 ******************************************************************************/
extern UFUNEXPORT int  UF_MODL_edit_sweep_curves(
tag_t sweep_id ,/* <I>
                sweep object identifier
                */
int n_profile_curves_removed ,/* <I>
                              number of the curves to be removed from the sweep
                              profile, 0 if no curve.
                              */
tag_t * profile_curves_removed ,/* <I,len:n_profile_curves_removed>
                                curves to be removed from the sweep profile,
                                NULL if no curve.
                                */
int n_profile_curves_added ,/* <I>
                            number of the curves to be added to the sweep
                            profile, 0 if no curve.
                            */
tag_t * profile_curves_added ,/* <I,len:n_profile_curves_added>
                              curves to be added to the sweep profile, NULL if
                              no curve.
                              */
int n_guide_curves_removed ,/* <I>
                            number of the curves to be removed from the sweep
                            guide, 0 if no curve.
                            */
tag_t * guide_curves_removed ,/* <I,len:n_guide_curves_removed>
                              curves to be removed from the sweep guide, NULL
                              if no curve.
                              */
int n_guide_curves_added ,/* <I>
                          number of the curves to be added to the sweep
                          guide, 0 if no curve.
                          */
tag_t * guide_curves_added  /* <I,len:n_guide_curves_added>
                            curves to be added to the sweep guide, NULL if no
                            curve.
                            */
);

/********************************************************************
Gets sweep parameters.

Environment: Internal  and  External
See Also:
History:
********************************************************************/
extern UFUNEXPORT int UF_MODL_ask_sweep_parms(
tag_t feature_obj_id ,/* <I>
                      A feature object identifier
                      */
int edit ,/* <I>
          This is an unused flag. It was used to determine
          whether to return the right-hand side or both sides
          of an expression. Currently, both sides of an
          expression are returned.
          */
char ** taper_angle ,/* <OF>
                     Taper angle.  This must be freed by
                     calling UF_free.
                     */
char ** limit1 ,/* <OF>
                Start angle (degrees) for revolved features or start
                offset distance for extruded features.  This must be
                freed by calling UF_free.
                */
char ** limit2  /* <OF>
                End angle (degrees) for revolved features or end
                offset distance for extruded features.  This must
                be freed by calling UF_free.
                */
);

/******************************************************************************
Retrieves the parameters used to create an extrusion.

Environment: Internal  and  External
See Also: UF_MODL_create_extrusion
History:Original release was in V13.0.
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_extrusion(
tag_t feature_obj_id ,/* <I>
                      Object tag for the extruded feature
                      */
int* num_objects ,/* <O>
                  Number of curves
                  */
tag_t** objects ,/* <OF,len:num_objects>
                 Pointer to an array containing the tags of the extruded curves.
                 This array must be freed by calling UF_free.
                 */
UF_MODL_SWEEP_TRIM_object_p_t* trim_ptr ,/* <OF,free:UF_MODL_SWEEP_free_trim_data>
                                         Pointer to structure for trimming data.
                                         This pointer may be returned as NULL,
                                         if trimming objects are not used.
                                         Use function UF_MODL_SWEEP_free_trim_data to free the trimming data.
                                         */
char** taper_angle ,/* <OF>
                    Taper angle.  This must be freed by calling UF_free.
                    */
char* limits[2] ,/* <OF>
                 Limits of extrusion.  Each element of this array must be
                 freed by calling UF_free.
                 */
char* offsets[2] ,/* <OF>
                  Offsets for open strings.  Each element of this array must be
                 freed by calling UF_free.
                  */
double region_point[3] ,/* <O>
                        Point on region desired.
                        */
logical* region_specified ,/* <O>
                           True or False for region desired.
                           */
logical* solid_creation ,/* <O>
                         TRUE = a solid body.
                         */
double direction[3]  /* <O>
                     Extrusion direction
                     */
);


/*******************************************************************************
Gets the profile curves and guide curves of a given sweep.  This will also
work for extrusion features as well.


Environment: Internal  and  External
See Also:
 UF_MODL_ask_sweep_of_udf
 UF_MODL_edit_sweep_curves
History:
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_sweep_curves(
tag_t sweep_id ,/* <I>
                sweep or extrusion object identifier
                */
int * n_profile_curves ,/* <O>
                        number of profile curves
                        */
tag_t ** profile_curves ,/* <OF,len:n_profile_curves>
                         An array of profile curves.  This is must be freed by
                         calling UF_free.
                         */
int * n_guide_curves ,/* <O>
                      number of guide curves
                      */
tag_t ** guide_curves  /* <OF,len:n_guide_curves>
                       An array of guide curves.  This must be freed by calling
                       UF_free.
                       */
);

/****************************************************************************
Given an extrude or revolve feature, this function sets the direction

Environment: Internal  and  External
See Also:
History: Originally released in V15.0
****************************************************************************/
extern UFUNEXPORT int  UF_MODL_set_sweep_axis(
tag_t  feature_id,   /* <I>
                     The feature ID.
                     */
double dir[3]          /* <I>
                     The new direction of the extrude or revolve feature.
                     */
);

/****************************************************************************
Given an extrude or revolve feature, this function sets the new tolerances.

Environment: Internal  and  External
See Also:
History: Originally released in V15.0
****************************************************************************/
extern UFUNEXPORT int  UF_MODL_set_sweep_tolerances(
tag_t  feature_id,   /* <I>
                     The feature ID.
                     */
double *tolerance    /* <O>
                     The new chaining and distance tolerance.
                     */
);

/******************************************************************************
Retrieves the parameters used to create a revolution.

Environment: Internal  and  External
See Also: UF_MODL_create_revolution
History:Original release was in V19.0 (NX1.0).
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_revolution
(
tag_t feature_obj_id,      /* <I> Object tag for the revolved feature
                           */
int* num_objects,          /* <O> Number of revolved curves
                           */
tag_t** objects,           /* <OF,len:num_objects> Pointer to an array containing the tags of the
                              revolved curves. This array must be freed by calling UF_free.
                           */
UF_MODL_SWEEP_TRIM_object_p_t* trim_ptr, /* <OF,free:UF_MODL_SWEEP_free_trim_data>
                                         Pointer to structure for trimming data.
                                         This pointer may be returned as NULL,
                                         if trimming objects are not used.
                                         Use function UF_MODL_SWEEP_free_trim_data to free the trimming data
                                         */
char* limits[2],           /* <OF> Limits of revolution. Each element of this array must be
                              freed by calling UF_free.
                           */
char* offsets[2],          /* <OF> Offsets for open strings. Each element of this
                              array must be freed by calling UF_free.
                           */
double region_point[3],    /* <O> Point on region desired.
                           */
logical* region_specified, /* <O> True or False for region desired.
                           */
logical* solid_creation,   /* <O> TRUE = a solid body.
                           */
double direction[3]        /* <O> Revolution direction
                           */
);

/******************************************************************************
Free the sweep trimming data.

Environment: Internal  and  External
See Also: UF_MODL_SWEEP_free_trim_data
History:Original release was in NX6.0
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_SWEEP_free_trim_data (UF_MODL_SWEEP_TRIM_object_p_t trim_object);


/****************************************************************************
Retrieves the offset direction for an extruded feature.

The offset point is defined as the middle point of the first profile curve of
an extruded feature.

The offset direction is defined by the cross product of the first profile curve
direction and the extruded direction. This direction starts from the offset point.

Environment: Internal  and  External
See Also: UF_MODL_ask_sweep_direction()
History: Originally released in V19.0 (NX1.0)
****************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_extrude_offset_dir
(
tag_t feature_id,   /* <I> Object tag for an extruded feature.
                    */
double point[3],      /* <O> The middle point of the first profile curve.
                       This must be declared as double point[3].
                    */
double direction[3]   /* <O> The offset direction for an extruded feature.
                       This must be declared as double direction[3].
                    */
);

#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif     /* UF_MODL_SWEEP_H_INCLUDED */
