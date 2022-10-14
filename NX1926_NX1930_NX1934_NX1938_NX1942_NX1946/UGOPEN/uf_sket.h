/*******************************************************************************

          Copyright (c) 1995-2006 UGS Corp.
                   All rights reserved




File description:

Open C API interface to the sketcher.

 The sketch functions in this file enable you to:
  . Create an empty sketch.
  . Initialize (activate) and terminate (deactivate) an existing sketch.
  . Add/Extract geometric objects to a sketch.
  . Mirror geometries.
  . Create, query and delete dimensions and geometric constraints.
  . Update a sketch.
  . Interrogate a sketch including its orientation, origin, solved status,...,etc.
  . Query constraint's type and constraints associated with a geometry.
  . Query the type and status of a sketch dimension.
  . Get all the geometries, expressions, dimensions, and geometric constraints
    for a sketch.
  . Get all sketches associated with a face or a feature.
  . Get all features associated with a sketch.
  . Query/Edit current sketch preference settings.


Each sketch routine either returns a zero (no error) or an error code.
Use UF_get_fail_message to obtain the error message string.  Currently,
the support for extracted sketches is limited to those that are noted
as "supports extracted sketches" below.



Public Routines
===================
  -- for all sketches
    UF_SKET_ask_dim_status
    UF_SKET_ask_face_sketches
    UF_SKET_ask_sketch_info             (supports extracted sketches)
    UF_SKET_ask_sketch_features
    UF_SKET_add_objects
    UF_SKET_ask_exps_of_sketch
    UF_SKET_ask_dimensions_of_sketch
    UF_SKET_ask_geoms_of_sketch         (supports extracted sketches)
    UF_SKET_ask_feature_sketches
    UF_SKET_create_sketch
    UF_SKET_delete_dimensions
    UF_SKET_initialize_sketch
    UF_SKET_terminate_sketch
    UF_SKET_ask_reference_status
    UF_SKET_set_reference_status

  -- for V13.0+ sketches only
    UF_SKET_add_extracted_object
    UF_SKET_add_conics
    UF_SKET_ask_constraint_class
    UF_SKET_ask_constraint_type
    UF_SKET_ask_constraints_of_geometry
    UF_SKET_ask_constraints_of_sketch
    UF_SKET_ask_geo_cons_of_geometry
    UF_SKET_ask_geo_cons_of_sketch
    UF_SKET_ask_preferences
    UF_SKET_ask_sketch_status
    UF_SKET_create_geometric_constraint
    UF_SKET_create_dimension
    UF_SKET_create_dimensional_constraint
    UF_SKET_delete_constraints
    UF_SKET_mirror_objects
    UF_SKET_read_geometric_constraint
    UF_SKET_read_dimension
    UF_SKET_read_dimensional_constraint
    UF_SKET_set_preferences
    UF_SKET_update_sketch

  -- for pre-V13.0 sketches only
    UF_SKET_attach_to_face
    UF_SKET_delete_legacy_constraint
    UF_SKET_ask_legacy_preferences
    UF_SKET_set_legacy_preferences


Release Highlights
===================
V17:
  o New functions:
       UF_SKET_add_conics
       UF_SKET_ask_constraint_class
       UF_SKET_create_dimensional_constraint
       UF_SKET_read_dimensional_constraint
       UF_SKET_ask_reference_status
       UF_SKET_set_reference_status.
  o Argument changes:
       UF_SKET_ask_constraints_of_geometry
       UF_SKET_ask_constraints_for_sketch
  o Rename:
       UF_SKET_create_constraint is renamed to UF_SKET_create_geometric_constraint.
       UF_SKET_read_constraint is renamed to UF_SKET_read_geometric_constraint.
  o Obsoleted:
       UF_SKET_ask_info
       UF_SKET_delete_dimension
*****************************************************************************/

#ifndef UF_SKET_H_INCLUDED
#define UF_SKET_H_INCLUDED


/***************************************************************************

  ***************************************************************************/

#include <uf_defs.h>
#include <uf_obj_types.h>
#include <uf_curve.h>
#include <uf_sket_types.h>
#include <uf_retiring.h>
#include <libufun_exports.h>

#ifdef __cplusplus
extern "C" {
#endif

/******************************************************************************
Adds conics to the current sketch.

The following restrictions applies:
1) UF_SKET_initialize_sketch must have been previously called.
2) The construction coordinate system of the conic you wish to add must be
parallel to the sketch plane.
3) Object has to be either a hyperbola, parabola, or a partial ellipse
   with angular span smaller than 180 degree.

Environment: Internal and External

See Also: UF_SKET_initialize_sketch

History: This function was originally released in V17.0
******************************************************************************/
extern UFUNEXPORT int UF_SKET_add_conics
(
 tag_t sketch_tag,    /* <I>  Sketch tag.                      */
 int count,           /* <I>  Number of conics to be added.   */
 tag_t *object        /* <I,len:count>
                              Array of conics to be added to the sketch */
);

/******************************************************************************
This routine adds extracted objects to a sketch. New objects, extracted
from the input objects and become associative with the input objects, will
be added to the sketch.

The following restrictions applies:
UF_SKET_initialize_sketch must have been previously called.

Environment: Internal and external.

See Also: UF_SKET_initialize_sketch

History: This function was originally released in V16.0.
******************************************************************************/
extern UFUNEXPORT int UF_SKET_add_extracted_objects
(
 tag_t  sketch_tag, /* <I> Sketch tag                            */
 int    count,      /* <I> Number of objects to be extracted     */
 tag_t  *objects,   /* <I,len:count>
                           Array of objects to be extracted      */
 int    output_mode,/* <I> Output mode
                           UF_SKET_EXTR_ORIG_TYPE
                           UF_SKET_EXTR_MULTI_SPLINES
                           UF_SKET_EXTR_SINGLE_SPLINE
                    */
 int    *num_extracted_objs, /* <O>  Number of extracted objects */
 tag_t  **extracted_objs     /* <OF,len:num_extracted_objs>
                             Array of extracted objects.
                                Use UF_free to deallocate memory when done.
                             */
);


/******************************************************************************
Adds geometric objects to the current sketch.

The following restrictions applies:
1) UF_SKET_initialize_sketch must have been previously called.
2) The construction coordinate system of the arcs you wish to add must be
parallel to the sketch plane.

Environment: Internal and External

See Also: UF_SKET_initialize_sketch

History:
******************************************************************************/
extern UFUNEXPORT int UF_SKET_add_objects
(
 tag_t sketch_tag,    /* <I>  Sketch tag.                      */
 int count ,          /* <I>  Number of objects to be added.   */
 tag_t *object        /* <I,len:count>
                              Array of objects to be added to the sketch */
);


/******************************************************************************
This function returns the constaint class of the given constraint tag.

Environment: Internal  and  External

See Also:

History: This function was originally released in V17.0.
******************************************************************************/
extern UFUNEXPORT int UF_SKET_ask_constraint_class
(
 tag_t                con_tag,    /* <I> Constraint tag */
 UF_SKET_con_class_t *con_class   /* <O>
                                     Constraint class:
                                     - UF_SKET_geo_cons
                                     - UF_SKET_dim_cons
                                  */
);


/******************************************************************************
This function finds the constaint type

Environment: Internal  and  External

See Also:

History: This function was originally released in V16.0.
******************************************************************************/
extern UFUNEXPORT int UF_SKET_ask_constraint_type
(
   tag_t con_tag,                /* <I>  Constraint tag          */
   UF_SKET_con_type_t  *con_type /* <O>  The type of constraint  */
);


/******************************************************************************
This function finds all the geometric constraints associated with a geometry.

Environment: Internal  and  External

See Also: UF_SKET_ask_constraints_of_geometry

History: V17 change: This function was renamed from UF_SKET_ask_constraints_of_geometry,
         which was originally released in V16.0.
******************************************************************************/
extern UFUNEXPORT int UF_SKET_ask_geo_cons_of_geometry
(
   tag_t sketch_tag, /* <I>  Sketch tag.             */
   tag_t geom_tag,   /* <I>  Tag of the geometry.    */
   int   *con_num,   /* <O>  Number of constraints.  */
   tag_t **con_tags  /* <OF,len:con_num>
                             Array of constraints.
                        Use UF_free to deallocate memory when done.
                     */
);

/******************************************************************************
This function finds all the constraints, with the specified class, associated
 with a geometry.

Environment: Internal  and  External

See Also: UF_SKET_ask_geo_cons_of_geometry

History: V17 change: This function is new for V17.0. Although the
         function's name is not new, the parameter list has changed.

        Past callers of the UF_SKET_ask_constraints_of_geometry function
        should replace their calls by UF_SKET_ask_geo_cons_of_geometry or
        may use this function with additional parameter 'con_class' set to
        SKET_geo_cons to get the same result as before.

******************************************************************************/
extern UFUNEXPORT int UF_SKET_ask_constraints_of_geometry
(
tag_t               sketch_tag, /* <I> Sketch tag */
tag_t               geom_tag,   /* <I>  Tag of the geometry.    */
UF_SKET_con_class_t con_class,  /* <I>
                                   Constraint class:
                                   - UF_SKET_all_cons
                                   - UF_SKET_geo_cons
                                   - UF_SKET_dim_cons
                                */
int                 *con_num,   /* <O> Number of output constraints */
tag_t              **con_tags   /* <OF,len:con_num>
                                   Array of constraints of the sketch.
                                    Use UF_free to deallocate memory when done.
                                */
);

/*******************************************************************************
Output geometric constraints of a given sketch.

Environment: Internal  and  External


See Also: UF_SKET_ask_constraints_of_sketch

History: V17 change: This function was renamed from UF_SKET_ask_constraints_of_sketch,
         which was originally released in V16.0.
*******************************************************************************/
extern UFUNEXPORT int UF_SKET_ask_geo_cons_of_sketch
(
 tag_t     sketch_tag,   /* <I> Sketch tag */
 int       *num_cons,    /* <O> Number of output constraints */
 tag_t     **con_tags    /* <OF,len:num_cons>
                                Array of constraints of the sketch.
                            Use UF_free to deallocate memory when done.
                         */
);

/*******************************************************************************
Output constraints, with the specified class, of a given sketch.


Environment: Internal  and  External

See Also: UF_SKET_ask_geo_cons_of_sketch

History: V17 change: This function is new for V17.0. Although the
         function's name is not new, the parameter list has changed.

        Past callers of the UF_SKET_ask_constraints_of_sketch function
        should replace their calls by UF_SKET_ask_geo_cons_of_sketch or
        may use this function with additional parameter 'con_class' set
        to SKET_geo_cons to get the same result as before.

*******************************************************************************/
extern UFUNEXPORT int UF_SKET_ask_constraints_of_sketch
(
tag_t               sketch_tag, /* <I> Sketch tag */
UF_SKET_con_class_t con_class,  /* <I>
                                   Constraint class:
                                   - UF_SKET_all_cons
                                   - UF_SKET_geo_cons
                                   - UF_SKET_dim_cons
                                */
int                 *num_cons,  /* <O> Number of output constraints */
tag_t              **con_tags   /* <OF,len:num_cons>
                                    Array of constraints of the sketch.
                                    Use UF_free to deallocate memory when done.
                                */
);

/******************************************************************************
Returns status of a sketch dimension as well as its expression.

Environment: Internal  and  External

See Also:

History:
*******************************************************************************/
extern UFUNEXPORT int UF_SKET_ask_dim_status
(
 tag_t dim_tag ,        /* <I>  Dimension tag.         */
 tag_t * exp_tag ,      /* <O>  Expression tag.        */
 char  exp_string[256] ,/* <O>  Expression string.     */
 double * value ,       /* <O>  Value of expression.   */
 int * status           /* <O>  Status:
                                1 = Reference
                                2 = Constrained(for pre-v13 sketches) or
                                Active(for v13+ sketches)
                                3 = Underconstrained(for pre-v13 sketches only)-
                                    some variables associated with the dimension
                                    are not constrained)   */
);

/*******************************************************************************
Output dimensions of a given sketch.

Environment: Internal  and  External

See Also:

History: This function was originally released in V16.0.
*******************************************************************************/
extern UFUNEXPORT int UF_SKET_ask_dimensions_of_sketch
(
 tag_t        sketch_tag,   /* <I>  Sketch tag */
 int          *num_dims,    /* <O>  Number of output dimensions */
 tag_t        **dim_tags    /* <OF,len:num_dims>
                                Array of dimensions of the sketch.
                                Use UF_free to deallocate memory when done.
                            */
);

/******************************************************************************
Returns the expressions for a sketch.

Environment: Internal  and  External

See Also:

History: Original release was in V14.0.
******************************************************************************/
extern UFUNEXPORT int UF_SKET_ask_exps_of_sketch
(
 tag_t  sketch_tag ,      /* <I>   Sketch tag                         */
 int    *num_exps ,       /* <O>   Number of expressions in sketch    */
 tag_t **expression_tags  /* <OF,len:num_exps>
                                Array of expressions from the sketch.
                                Use UF_free to deallocate memory when done.
                          */
);


/******************************************************************************
Returns all sketches associated with a face or datum plane.

Environment: Internal  and  External

See Also:

History:
******************************************************************************/
extern UFUNEXPORT int UF_SKET_ask_face_sketches
(
 tag_t object ,             /* <I>  Solid face / datum plane tag.         */
 uf_list_p_t * object_list  /* <OF,free:UF_MODL_delete_list>
                                    List of sketches or NULL if none found.
                                    This argument must be freed by calling
                                    UF_MODL_delete_list
                            */
);

/******************************************************************************
Returns all sketches associated with a feature.

Environment: Internal  and  External

See Also:

History:
*******************************************************************************/
extern UFUNEXPORT int UF_SKET_ask_feature_sketches
(
 tag_t feature ,            /* <I>  Feature tag.    */
 uf_list_p_t * object_list  /* <OF,free:UF_MODL_delete_list>
                                    List of sketches or NULL if none found.
                                    This argument must be freed by calling
                                    UF_MODL_delete_list
                            */
);

/*******************************************************************************
Output geometries of a given sketch.

Environment: Internal  and  External

See Also:

History: This function was originally released in V16.0.
*******************************************************************************/
extern UFUNEXPORT int UF_SKET_ask_geoms_of_sketch
(
 tag_t        sketch_tag,   /* <I>  Sketch tag */
 int          *num_geoms,   /* <O>  Number of output geometries */
 tag_t        **geom_tags   /* <OF,len:num_geoms>
                                Array of geometries of the sketch.
                                Use UF_free to deallocate memory when done.
                            */
);


/*******************************************************************************

Output sketch of a given geometric object

Environment: Internal  and  External

See Also:

History: This function was originally released in NX 4.
*******************************************************************************/
extern UFUNEXPORT int UF_SKET_ask_sketch_of_geom
(
 tag_t         geom_tag,      /* <I> Geometric object */
 tag_t        *sketch_tag     /* <O> Sketch tag of which object is member
                                     NULL_TAG: if none */
);


/******************************************************************************
Returns current sketch preference settings for sketches created prior to V13.0.

Environment: Internal  and  External

See Also:  UF_SKET_ask_preferences
to query preferences for sketches created in V13.0 and beyond.
          UF_SKET_set_legacy_preferences
          UF_SKET_set_preferences

History: V15.0 change: This function was renamed from
         UF_SKET_ask_preferences to UF_SKET_ask_legacy_preferences.
******************************************************************************/
extern UFUNEXPORT int UF_SKET_ask_legacy_preferences
(
 double *snap_angle , /* <O> Snap angle.                      */
 double *cap_dist ,   /* <O> Capture distance.                */
 char    pt_name[256] ,    /* <O> Point name variable.             */
 int    auto_flag[2], /* <O>
                         Auto inferencing/constraint flag (1 = Off, 2 = On):
                         [0] = Auto inferencing
                         [1] = Auto constraint
                      */
 int    show_flag[3], /* <O> Show csys / datum / arrows flag (1 = Off, 2 = On):
                             [0] = CSYS
                             [1] = Datum
                             [2] = Arrows
                      */
 double *char_size ,  /* <O>  Character size.                 */
 int    *dec_places , /* <O>  Decimal places.                 */
 int    *ext_lines ,  /* <O> Extension lines:
                             1 = Both
                             2 = Line1
                             3 = Line2
                             4 = None
                      */
 int    *dim_label    /* <O> Dimension label:
                             1 = Value
                             2 = Expression
                             3 = Name
                      */
);


/******************************************************************************
Returns the current values for each of the sketch preference
variables applicable for sketches created in V13.0 and beyond.
To determine if this function should be called instead of
UF_SKET_ask_legacy_preferences, use UF_OBJ_ask_type_and_subtype and check for
UF_v13_sketch_subtype.

Environment: Internal and External

See Also: UF_SKET_ask_legacy_preferences
          UF_SKET_set_preferences
          UF_SKET_set_legacy_preferences

History: V15.0 change: This function is new for V15.0. Although the
         function's name is not new, the parameter list has changed.

         NX6   change: Sketches no longer have a  'character size' and 'decimal places'
         preference. Each individual dimension will have these preferences.
         The parameter list for this function will not change, but the values returned
         for 'character size' and 'decimal places' will always be the global annotation 
         preferences.

*******************************************************************************/
extern UFUNEXPORT int UF_SKET_ask_preferences
(
 tag_t    sketch_tag,  /* <I> Tag of input sketch; May be set to
                          NULL_TAG if there is not a particular
                          sketch which the user wants to query.
                       */
 double   *snap_angle,                    /* <O> Snap angle preference */
 char     name_prefix[ UF_OBJ_NAME_BUFSIZE ],   /* <O> Prefix for new sketch names */
 char     vertex_prefix[ UF_OBJ_NAME_BUFSIZE ], /* <O> Prefix for vertex names */
 char     line_prefix[ UF_OBJ_NAME_BUFSIZE ],   /* <O> Prefix for line names */
 char     arc_prefix[ UF_OBJ_NAME_BUFSIZE ],    /* <O> Prefix for arc names */
 char     conic_prefix[ UF_OBJ_NAME_BUFSIZE ],  /* <O> Prefix for conic names */
 char     spline_prefix[ UF_OBJ_NAME_BUFSIZE ], /* <O> Prefix for spline names */
 double   *char_size,                     /* <O> Character size is no longer a sketch preference. This parameter
                                             will always return the global annotation preferences- dimension
                                             character size */
 int      *dec_places,                    /* <O> Decimal places are no longer a sketch preference. This parameter
                                             will always return the global annotation preferences- dimension
                                             decimal places */
 int      *dim_label                      /* <O> Dimension Label:
                                                 1 = value
                                                 2 = expression
                                                 3 =  name
                                          */
);


/*******************************************************************************
This function returns the reference status - reference/active status
of a sketch curve or a dimension

The following restrictions applies:
UF_SKET_initialize_sketch must have been previously called.

Environment: Internal  and  External

See Also: UF_SKET_set_reference_status

History: This function was originally released in V17.0.
*******************************************************************************/
extern UFUNEXPORT int UF_SKET_ask_reference_status
( tag_t skt_tag,                     /* <I> Tag of the sketch to which the dim/curve belongs */
  tag_t member,                      /* <I> Tag of the dim/curve whose state needs to be determined */
  UF_SKET_reference_status_t *status /* <O> UF_SKET_active or UF_SKET_reference */
);

/******************************************************************************
Returns all features associated with a sketch.

Environment: Internal  and  External

See Also:

History:
*******************************************************************************/
extern UFUNEXPORT int UF_SKET_ask_sketch_features
(
 tag_t sketch_tag ,         /* <I>  Sketch tag.                   */
 uf_list_p_t * object_list  /* <OF,free:UF_MODL_delete_list>
                                    List of sketches or NULL if none found.
                                    This argument must be freed by calling
                                    UF_MODL_delete_list
                            */
);


/*******************************************************************************
Output general information about a given sketch.

Environment: Internal  and  External

See Also:

History: This function was originally released in V16.0.
*******************************************************************************/
extern UFUNEXPORT int UF_SKET_ask_sketch_info
(
 tag_t          sketch_tag, /* <I> Sketch tag */
 UF_SKET_info_t *sket_info  /* <O> Sketch information data structure.
                                   (See type UF_SKET_info_t in uf_sket_types.h
                                   for the structure members).
                            */
) ;

/*******************************************************************************
This routine returns the given sketch's status and the degrees of freedom
needed to make the sketch full-constrained if it is currently
under-constrained.

The following restrictions applies:
UF_SKET_initialize_sketch must have been previously called.

Environment: Internal  and  External

See Also: UF_SKET_initialize_sketch

History: This function was originally released in V16.0.
*******************************************************************************/
extern UFUNEXPORT int UF_SKET_ask_sketch_status
(
 tag_t            sketch_tag,    /* <I> Sketch tag */
 UF_SKET_status_t *sket_status,  /* <O> Sketch's current status.
                                        (See type UF_SKET_status_t in
                                        uf_sket_types.h for valid values).
                                 */
 int              *dof_needed    /* <O> Degrees of freedom needed to make the
                                        sketch fully-constrained. This value
                                        is meaningful only when sketch's status
                                        is UF_SKET_under_constrained.
                                 */

);


/*******************************************************************************
This routine returns the active sketch, or NULL_TAG if none active

Environment: Internal  and  External

History: This function was originally released in NX5.0.
*******************************************************************************/
extern UFUNEXPORT int UF_SKET_ask_active_sketch
(
 tag_t          * sketch_tag    /* <O> Active sketch tag, NULL_TAG if none  */

);


/******************************************************************************
Attaches a non-feature sketch to a planar face or datum plane and returns the
resulting sketch feature tag. For reattaching sketch features to a different
face or datum plane, please use UF_MODL_reattach_target_face.

Environment: Internal  and  External

See Also: UF_MODL_reattach_target_face

History:
 *****************************************************************************/
extern UFUNEXPORT int UF_SKET_attach_to_face
(
 tag_t sketch_tag , /* <I> Tag of the sketch to attach                  */
 tag_t face_tag ,   /* <I> Face or datum plane to attach the sketch to  */
 tag_t ref_tag ,    /* <I>
                       This defines a line which is the horizontal or vertical
                       reference used for positioning the sketch on the face or
                       datum plane. This object can be a linear edge, a datum
                       axis, a planar face, or a datum plane. The direction of
                       the line is specified in ref_info. A face or datum plane
                       constructs the line by intersecting itself with face_tag.
                    */
 int ref_info[2] ,  /* <I>
                       Data required to fully define the reference.
                       ref_info[0] = reference orientation
                       use one of the following values:
                       UF_SKET_HORIZONTAL
                       UF_SKET_VERTICAL
                       ref_info[1] = direction along reference
                       use one of the following values:
                       UF_SKET_ALONG_CURVE (start to end)
                       UF_SKET_OPPOSITE_CURVE (end to start)
                    */
 int plane_dir ,    /* <I>
                       Which side of plane or face to attach sketch.
                       use one of the following values:
                       UF_SKET_WITH_NORMAL (outwards from parent body)
                       UF_SKET_OPPOSITE_NORMAL (inwards from parent body)
                    */
 tag_t * sketch_feature_tag  /* <O> Sketch feature tag created  */
);


/****************************************************************************
This routine creates sketch geometry constraints of the specified type.
Not all parameters are required based on the type of constraint being
created. Refer to the descriptions below to determine which parameters
are used for each type of sketch constraints.

The following restrictions applies:
UF_SKET_initialize_sketch must have been previously called.

Environment: Internal  and  External

See Also: UF_SKET_delete_constraints
          UF_SKET_initialize_sketch
          UF_SKET_read_geometric_constraint
          UF_SKET_update_sketch

History: V17 change: This function was renamed from UF_SKET_create_constraint, which
         was originally released in V16.0.
****************************************************************************/
extern UFUNEXPORT int UF_SKET_create_geometric_constraint
(
 tag_t                sketch_tag,     /* <I>  Sketch tag.               */
 UF_SKET_con_type_t   con_type,       /* <I>  Constraint type.
                                         Valid types are:
                                          UF_SKET_fixed
                                          UF_SKET_horizontal
                                          UF_SKET_vertical
                                          UF_SKET_constant_length
                                          UF_SKET_constant_angle
                                          UF_SKET_uniform_scaled
                                          UF_SKET_non_uniform_scaled
                                          UF_SKET_parallel
                                          UF_SKET_perpendicular
                                          UF_SKET_collinear
                                          UF_SKET_equal_length
                                          UF_SKET_equal_radius
                                          UF_SKET_coincident
                                          UF_SKET_concentric
                                          UF_SKET_midpoint
                                          UF_SKET_slope
                                          UF_SKET_tangent
                                          UF_SKET_point_on_curve
                                          UF_SKET_point_on_string
                                      */
 int                   num_con_geoms, /* <I> Number of constraint geometries */
 UF_SKET_con_geom_t   *con_geoms,     /* <I,len:num_con_geoms>
                                         Array of constraint geometries
                                         (See type UF_SKET_con_geom_t in
                                         file uf_sket_types.h for the
                                         structure members).
                                      */
 tag_t                 *con_tag       /* <O> The tag of the created
                                         geometric constraint.
                                      */
);

/***************************************************************************


Some background and terminology
********************************

   All geometris used in a sketch can be broadly categorized into
   "External Reference Geometry" and "Internal Geometry":

   * Internal Geometry
     These are the regular point and curves (lines/arcs/ellipse/splines)
     that were created when a sketch is activated or were created outside
     the sketch but added to the sketch later. Currently, parabola and
     hyperbola are not supported as internal geometris.

   * External Reference Geometry
     These geometries are mainly used as reference for internal geometries.
     They are considered as 'fixed' objects for the sketch in question.
     Currently, external reference geometries could be non-sketch point/curves,
     point/curves belonging to sketches other than the one in question,
     datum planes, datum axis, and solid edges. Parabola and hyperbola
     cannot be used as external reference geometry either.

     NOTES:
       To be able to use curves in other sketches, datum planes, datum axis
       and solid edges as external reference for a sketch, they must be
       created before the sketch in question is created.
       For using non-sketch point/curves as external reference, there is no
       such a restriction.


  The UF_SKET_con_geom_t structure could represent an object itself or
  a vertex of the object.

  * Vertex Geometry

    When UF_SKET_con_geom_t is used to represent a vertex of an object,
    you need to set the 'geom_tag' to the tag of the object and the
    'vertex_type' to an appropriate value (ref.: the enum type
    UF_SKET_geom_vertex_t in uf_sket_types.h). You will also need to provide
    the 'vertex_index' (starting from 1) for spline's defining points. We will
    refer UF_SKET_con_geom_t of this kind by "Vertex Geometry".

  * Line/Circle/Ellipse/Spline/DatumAxis/DatumPlane Geometry

    When using UF_SKET_con_geom_t to represent an object, simply set the
    'geom_tag' to the tag of the object and the 'vertex_type' to
    UF_SKET_no_vertex. Depending on the types of the objects, they are
    referred as "Line Geometry", "Circle Geometry", ...etc.
    Notes that solid edges with line/circle/ellipse/spline as its underlying
    geometry are also referred as "Line/Circle/Ellipse/Spline Geometry".

  * Help data

    Help data are used to indicate the whereabouts on the geometry a
    constraint should apply to. They are only needed when the constraints
    are of type UF_SKET_tangent, UF_SKET_point_on_curve, and
    UF_SKET_point_on_string unless the geometry involved is a line or a
    straight edge. Help data is specified by either specifing a help point
    or a help parameter in the UF_SKET_con_geom_t structure.



The valid constraint geometry input for each constraint type
****************************************************************

       ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Following constraint types require exactly one constraint geometry,
        which must be an internal geometry to the sketch specified.
       ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 con_type                      con_geoms[0]
---------------------------------------------------------------------------
 UF_SKET_fixed               Vertex_Geometry or a Line/Circle/Ellipse_Geometry
 UF_SKET_horizontal          Line_Geometry
 UF_SKET_vertical            Line_Geometry
 UF_SKET_constant_length     Line_Geometry
 UF_SKET_constant_angle      Line_Geometry
 UF_SKET_uniform_scaled      Spline_Geometry
 UF_SKET_non_uniform_scaled  Spline_Geometry


       ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
       Following constraint types require exactly two constraint geometries
       and at least one of them must be an internal geometry to the sketch
       specified. The order of input constraint geometries can be exchanged.
       ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 con_type                     con_geoms[0]  |  con_geoms[1]
---------------------------------------------------------------------------
 UF_SKET_parallel            Line_Geometry    | Line_Geometry
                             Line_Geometry    | Ellipse_Geometry
                             Ellipse_Geometry | Ellipse_Geometry
                             Line_Geometry    | DatumAxis_Geometry
                             Line_Geometry    | DatumPlane_Geometry

 UF_SKET_perpendicular       Line_Geometry    | Line_Geometry
                             Line_Geometry    | Ellipse_Geometry
                             Ellipse_Geometry | Ellipse_Geometry
                             Line_Geometry    | DatumAxis_Geometry
                             Line_Geometry    | DatumPlane_Geometry

 UF_SKET_collinear           Line_Geometry    | Line_Geometry
                             Line_Geometry    | DatumAxis_Geometry
                             Line_Geometry    | DatumPlane_Geometry

 UF_SKET_equal_length        Line_Geometry    | Line_Geometry

 UF_SKET_equal_radius        Circle_Geometry  | Circle_Geometry

 UF_SKET_concentric          Circle_Geometry  | Circle_Geometry
                             Circle_Geometry  | Ellipse_Geometry
                             Ellipse_Geometry | Ellipse_Geometry

 UF_SKET_coincident          Vertex_Geometry  | Vertex_Geometry

 UF_SKET_midpoint            Vertex_Geometry  | Line_Geometry
                             Vertex_Geometry  | Circle_Geometry

 UF_SKET_slope               Vertex_Geometry  | Line_Geometry
                             Vertex_Geometry  | Circle_Geometry
                             Vertex_Geometry  | Ellipse_Geometry
                             Vertex_Geometry  | Spline_Geometry
                             Vertex_Geometry  | DatumAxis_Geometry
                             Vertex_Geometry  | DatumPlane_Geometry
                            ( The Vertex Geometry must represent a spline's
                              defining point)

 UF_SKET_point_on_curve      Vertex_Geometry  | Line_Geometry
                             Vertex_Geometry  | Circle_Geometry
                             Vertex_Geometry  | Ellipse_Geometry
                             Vertex_Geometry  | Spline_Geometry
                             Vertex_Geometry  | DatumAxis_Geometry
                             Vertex_Geometry  | DatumPlane_Geometry

 UF_SKET_tangent            Only the following combinations are invalid:
                             Line_Geometry    | Line_Geometry
                             Line_Geometry    | DatumAxis_Geometry
                             Line_Geometry    | DatumPlane_Geometry
                             Spline_Geometry  | DatumAxis_Geometry
                             Spline_Geometry  | DatumPlane_Geometry

       ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
       This constraint type requires at least two constraint geometries.
       The first one must be a Vertex Geometry.
       ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 con_type                      con_geoms[0]     con_geoms[1,...]
---------------------------------------------------------------------------

 UF_SKET_point_on_string    Vertex_Geometry    extracted curves

    *The geometries specified in con_geoms[1] to con_geoms[num_con_geoms-1]
    must be extracted curves (see UF_SKET_add_extracted_objects) and one of
    them must have help data specified. If there are multiple help data
    specified, the first one will be used.


*****************************************************************************/


/******************************************************************************
This routine creates sketch dimensions of the specified type.
Not all parameters are required based on the type of dimension
being created.  Refer to the descriptions below to determine
which parameters are used for each type of sketch dimension.

The following restrictions applies:
UF_SKET_initialize_sketch must have been previously called.

Environment: Internal  and  External

See Also: UF_SKET_initialize_sketch
          UF_SKET_update_sketch
          UF_SKET_read_dimension

History: This function was originally released in V16.0.
******************************************************************************/
extern UFUNEXPORT int UF_SKET_create_dimension
(
tag_t sketch_tag,                       /* <I>
                                           Sketch tag
                                        */
UF_SKET_con_type_t dim_type,            /* <I>
                                           Type of dimensions:
                                                UF_SKET_horizontal_dim
                                                UF_SKET_vertical_dim
                                                UF_SKET_parallel_dim
                                                UF_SKET_perpendicular_dim
                                                UF_SKET_angular_dim
                                                UF_SKET_radius_dim
                                                UF_SKET_diameter_dim
                                        */
UF_SKET_dim_object_p_t dim_object1,     /* <I>
                                           Data of first object geometry tag.
                                        */
UF_SKET_dim_object_p_t dim_object2,     /* <I>
                                           Data of second object geometry tag.
                                           Not used for UF_SKET_radius_dim or
                                           UF_SKET_diameter_dim.
                                        */
double dim_origin[3],                   /* <I>
                                           Dimension origin (X, Y, Z)
                                           in model space
                                        */
tag_t *dim_tag                          /* <O>
                                           Tag of created dimension
                                        */
);


/******************************************************************************
This routine creates dimension constraint.  This function differs from
that of UF_SKET_create_dimension for it will output the constraint tag
as opposed to the dimension tag and also the perimeter dimension creation is
supported by this routine.


The following restrictions applies:
UF_SKET_initialize_sketch must have been previously called.

Environment: Internal  and  External

See Also: UF_SKET_initialize_sketch
          UF_SKET_update_sketch
          UF_SKET_create_dimension
          UF_SKET_create_dimensional_constraint

History: This function was originally released in V17.0.
******************************************************************************/
extern UFUNEXPORT int UF_SKET_create_dimensional_constraint
(
tag_t sketch_tag,                  /* <I>
                                      Sketch tag
                                   */
UF_SKET_con_type_t dim_type,       /* <I>
                                      Type of dimensions:
                                          UF_SKET_horizontal_dim
                                          UF_SKET_vertical_dim
                                          UF_SKET_parallel_dim
                                          UF_SKET_perpendicular_dim
                                          UF_SKET_angular_dim
                                          UF_SKET_radius_dim
                                          UF_SKET_diameter_dim
                                          UF_SKET_perimeter_dim
                                   */
int num_dim_obj,                   /* <I>
                                      Number of geometry tags in the
                                      geoms array
                                   */
UF_SKET_dim_object_p_t dim_objs,   /* <I,len:num_dim_obj>
                                      Array of num_geom geometry tags
                                   */
double dim_origin[3],              /* <I>
                                      Dimension origin (X, Y, Z)
                                      in model space
                                   */
tag_t *con_tag                     /* <O>
                                      Tag of created dimensional constraint
                                   */
);

/******************************************************************************
Creates an empty sketch.

The following restrictions applies:
UF_SKET_initialize_sketch must have been previously called.

Environment: Internal  and  External

See Also: UF_SKET_initialize_sketch


History:
*******************************************************************************/
extern UFUNEXPORT int UF_SKET_create_sketch
(
 char   name[ UF_OBJ_NAME_BUFSIZE ],     /* <I>  Sketch name                
                              It can be at most UF_OBJ_NAME_LEN bytes long
                      */
 int    option ,      /* <I>  Option.
                              1: Sketch on face/datum plane
                              2: Specify sketch CSYS
                      */
 double matrix[9],    /* <I>  Sketch CSYS (for option = 2):
                              [0-5]: X-AXIS and Y-AXIS of matrix
                              [6-8]: Origin of CSYS
                      */
 tag_t  object[2],    /* <I>  Objects (for option = 1):
                              [0]: Solid face/Datum plane object
                              [1]: Reference object
                              (edge, datum axis, solid face/datum
                      */
 int    reference[2], /* <I>  Reference and direction (for option = 1):
                              [0]: Reference edge
                                   1: Horizontal
                                   2: Vertical
                              [1]: Direction
                                   1: Start to end (from vertex1 to vertex2)
                                   -1: End to start (from vertex2 to vertex1)
                      */
 int    plane_dir,    /* <I>  Datum plane direction:
                              1: Outwards from parent body.
                              2: Inward.
                      */
 tag_t  *sketch_id    /* <O>   Tag of teh sketch created    */
);

/******************************************************************************
This routine deletes constaints given their tags. The constraint tags could
belong to different sketches.

Environment: Internal  and  External

See Also: UF_SKET_create_geometric_constraint
          UF_SKET_read_geometric_constraint

History: This function was originally released in V16.0.
******************************************************************************/
extern UFUNEXPORT int UF_SKET_delete_constraints
(
  int   num_cons,     /* <I> number of constraints to be deleted */
  tag_t *con_tags     /* <I,len:num_cons>
                             Array of constraint tag.            */
);


/******************************************************************************
This routine deletes dimensions given their tags. The dimension tags could
belong to different sketches.

Environment: Internal  and  External

See Also: UF_SKET_create_dimension

History: This function was originally released in V16.0.
*******************************************************************************/
extern UFUNEXPORT int UF_SKET_delete_dimensions
(
 int    num_dims,    /* <I> Number of dimension tags to be deleted */
 tag_t *dim_tags     /* <I,len:num_dims>
                            Array of dimension tags to be deleted  */
) ;


/******************************************************************************
Deletes the specified geometric constraint from an old sketch.

Environment: Internal  and  External

See Also:

History: V16.0 change: This function was renamed from
         UF_SKET_delete_constraint to UF_SKET_delete_legacy_constraint.
******************************************************************************/
extern UFUNEXPORT int UF_SKET_delete_legacy_constraint
(
 int type ,/* <I>  The type of geometric constraint, one of the
                   following values:
                  UF_SKET_DATUM
                  UF_SKET_CONSTANT_OFFSETS
                  UF_SKET_POINT_ON_CURVE
                  UF_SKET_MIDPOINT_OF_CURVE
                  UF_SKET_HORIZONTAL_LINES
                  UF_SKET_VERTICAL_LINES
                  UF_SKET_CONSTANT_ANGLES
                  UF_SKET_CONSTANT_LENGTH_LINES
                  UF_SKET_COLLINEAR
                  UF_SKET_PARALLEL
                  UF_SKET_PERPENDICULAR
                  UF_SKET_EQUAL_LENGTH
                  UF_SKET_EQUAL_RADIUS
                  UF_SKET_TANGENT_CURVES
           */
 tag_t  obj_list[2] ,/* <I>
                        When delete_all flag = 0, the tag of the object from
                        which the constraint is deleted.
                     */
 int  assoc_var_list[2] ,/* <I>
                            When delete_all flag = 0, the variable index
                            associated with the object if type =
                                UF_SKET_DATUM
                                UF_SKET_CONSTANT_OFFSET
                                UF_SKET_POINT_ON_CURVE
                                UF_SKET_MIDPOINT_OF_CURVE
                                UF_SKET_CONSTANT_ANGLES
                                UF_SKET_CONSTANT_LENGTH_LINES
                                UF_SKET_TANGENT_CURVES
                                UF_SKET_CONSTANT_OFFSET
                                UF_SKET_TANGENT_CURVES
                            NOT USED for type =
                                UF_SKET_HORIZONTAL_LINES
                                UF_SKET_VERTICAL_LINES
                                UF_SKET_COLLINEAR
                                UF_SKET_PARALLEL
                                UF_SKET_PERPENDICULAR
                                UF_SKET_EQUAL_LENGTH
                                UF_SKET_EQUAL_RADIUS
                         */
 int  delete_all  /* <I>
                     Delete all flag, where 1 = yes (delete all constraints
                     of specified type)
                  */
);

/******************************************************************************
Initializes the sketch environment.

Environment: Internal  and  External

See Also: 

History:
*******************************************************************************/
extern UFUNEXPORT int UF_SKET_initialize_sketch
(
 char   name[ UF_OBJ_NAME_BUFSIZE ], /* <I/O> Input sketch name, returns updated sketch name. 
                           It should hold UF_OBJ_NAME_LEN bytes plus the trailing null.
                  */
 tag_t  *object   /* <O>   Sketch tag, NULL_TAG means non-existent sketch. */
);


/******************************************************************************
This function mirrors the objects on a center line. New objects and "mirror"
 constraints between the original objects and the new objects will be created.
 Note that points on the center line and lines collinear to the center line
 will not be mirrored. Therefore, the output number of mirrored objects will
 not necessaily be the same as the input number of objects.

The following restrictions applies:
UF_SKET_initialize_sketch must have been previously called.

Environment: Internal  and  External

See Also: UF_SKET_initialize_sketch

History: This function was originally released in V16.0.
*******************************************************************************/
extern UFUNEXPORT int UF_SKET_mirror_objects
(
   tag_t sketch_tag,      /* <I>  Sketch tag.                          */
   tag_t center_line_tag, /* <I>  Tag of the center line for mirror    */
   int   num_objs,        /* <I>  Number of objects.                   */
   tag_t *obj_tags,       /* <I,len:num_objs>
                                  Array of objects to be mirrored      */
   int   *num_new_objs,   /* <O>  Number of mirrored objects or
                                  constraints created.
                          */
   tag_t **new_obj_tags,  /* <OF,len:num_new_objs>
                                  Array of mirrored objects.
                                  Use UF_free to deallocate memory when done.
                          */
   tag_t **con_tags       /* <OF,len:num_new_objs>
                                  Array of constraints.
                                  Use UF_free to deallocate memory when done.
                          */
);

/******************************************************************************
This function queries the constraint information

Environment: Internal  and  External

See also : UF_SKET_create_geometric_constraint

History: V17 change: This function was renamed from UF_SKET_read_constraint,
         which was originally released in V16.0.
******************************************************************************/
extern UFUNEXPORT int UF_SKET_read_geometric_constraint
(
 tag_t sketch_tag,                /* <I>  Sketch tag.              */
 tag_t con_tag,                   /* <I>  Constraint tag.          */
 UF_SKET_con_type_t *con_type,    /* <O>  Constraint type.         */
 int *geom_count,                 /* <O>  Number of geometries.   */
 UF_SKET_con_geom_p_t *con_geoms  /* <OF,len:geom_count>
                                     Array of constraint geometries.
                                     Use UF_free to deallocate memory when done.
                                  */
);


/******************************************************************************
This function queries the dimension information.

Environment: Internal  and  External

See also :  UF_SKET_create_dimension

History: This function was originally released in V16.0.
******************************************************************************/
extern UFUNEXPORT int UF_SKET_read_dimension
(
tag_t sketch_tag,                       /* <I>
                                           Sketch tag
                                        */
tag_t dim_tag,                          /* <I>
                                           Dimension tag
                                        */
UF_SKET_con_type_t *dim_type,           /* <O>
                                           Type of dimensions:
                                               UF_SKET_horizontal_dim
                                               UF_SKET_vertical_dim
                                               UF_SKET_parallel_dim
                                               UF_SKET_perpendicular_dim
                                               UF_SKET_angular_dim
                                               UF_SKET_radius_dim
                                               UF_SKET_diameter_dim
                                        */
UF_SKET_dim_object_p_t dim_object1,     /* <O>
                                           Data of first object geometry tag
                                        */
UF_SKET_dim_object_p_t dim_object2,     /* <O>
                                           Data of second object geometry tag.
                                           Not used for UF_SKET_radius_dim or
                                           UF_SKET_diameter_dim
                                        */
double dim_origin[3],                   /* <O>
                                           Dimension origin in model space
                                        */
tag_t *dim_exp                          /* <O>
                                           Dimension expression tag
                                           (NULL_TAG for Reference dimensions)
                                        */
);


/******************************************************************************
This routine reads dimension constraint given a constraint tag.  This routine
differs from that of UF_SKET_read_dimension as it takes in the constraint tag
as opposed to the dimension tag.


The following restrictions applies:
UF_SKET_initialize_sketch must have been previously called.

Environment: Internal  and  External

See Also: UF_SKET_initialize_sketch
          UF_SKET_update_sketch
          UF_SKET_read_dimension
          UF_SKET_read_dimensional_constraint

History: This function was originally released in V17.0.
******************************************************************************/
extern UFUNEXPORT int UF_SKET_read_dimensional_constraint
(
tag_t sketch_tag,                       /* <I>
                                           Sketch tag
                                        */
tag_t con_tag,                          /* <I>
                                           Tag of dimensional constraint to read.
                                        */
UF_SKET_con_type_t *dim_type,           /* <O>
                                           Dimension type
                                        */
int *num_dim_obj,                       /* <O>
                                           Number of geometry tags in the
                                           geoms array
                                        */
UF_SKET_dim_object_p_t *dim_objs,       /* <OF,len:num_dim_obj>
                                           Array of num_geom geometry tags
                                           Use UF_free to deallocate memory when done.
                                        */
double dim_origin[3],                   /* <O>
                                           Dimension origin (X, Y, Z)
                                           in model space
                                        */
tag_t *dim_tag,                         /* <O>
                                           Tag of associated dimension object.
                                           Could be a NULL_TAG for cases such as
                                           perimeter dimensions.
                                        */
tag_t *exp_tag                          /* <O>
                                           Tag of associated expression object
                                        */
);

/******************************************************************************
Modify the current sketch preference settings for sketches created
prior to V13.0.

Environment: Internal  and  External

See Also: UF_SKET_ask_preferences
          UF_SKET_ask_legacy_preferences
          UF_SKET_set_preferences

History: V15.0 change: This function was renamed from
         UF_SKET_set_preferences to UF_SKET_set_legacy_preferences.
******************************************************************************/
extern UFUNEXPORT int UF_SKET_set_legacy_preferences
(
 const int values[9], /* <I> Array of flags to indicate which settings should be
                         modified (0 = leave at current value, 1 = change to
                         new value):
                             [0] = Snap angle
                             [1] = Capture distance
                             [2] = Point name variable
                             [3] = Auto inferencing/constraint flag
                             [4] = Show csys/datum/arrows flag
                             [5] = Character size
                             [6] = Decimal places
                             [7] = Extension lines
                             [8] = Dimension label
                      */
 double snap_angle,   /* <I>  Snap angle.                    */
 double cap_dist,     /* <I>  Capture distance.              */
 const char *pt_name,     /* <I>  Point name variable.           */
 const int  auto_flag[2], /* <I> Auto inferencing/constraint flag (1= Off; 2= On):
                             [0] = Auto inferencing
                             [1] = Auto constraint
                      */
 const int  show_flag[3], /* <I>  Show csys / datum / arrows flag (1= Off; 2= On)
                             [0] = CSYS
                             [1] = Datum
                             [2] = Arrows
                      */
 double char_size,    /* <I> Character size.               */
 int    dec_places,   /* <I> Decimal places.               */
 int    ext_lines,    /* <I> Extension lines:
                             1 = Both
                             2 = Line1
                             3 = Line2
                             4 = None
                      */
 int    dim_label    /* <I>  Dimension label:
                             1 = Value
                             2 = Expression
                             3 = Name
                     */
);


/******************************************************************************
Sets the sketch preferences for sketches created in V13 and beyond.
To determine if this function should be used instead of
UF_SKET_set_legacy_preferences, use UF_OBJ_ask_type_and_subtype
and check for subtype UF_v13_sketch_subtype.

Environment: Internal and External.

See Also:  UF_SKET_ask_preferences
to set preferences for sketches created in V13.0 and beyond.
          UF_SKET_ask_legacy_preferences
          UF_SKET_set_legacy_preferences

History: This function is new for V15.0. Although the function
         name is not new, the parameter list has changed.

         NX6   change: Sketches no longer have a  'character size' and 'decimal places'
         preference. Each individual dimension will have these preferences.
         The parameter list for this function has not changed. Calling this function
         will result in the 'character size' and 'decimal places' being set on each
         individual dimension in the sketch. 
         
*******************************************************************************/
extern UFUNEXPORT int UF_SKET_set_preferences
(
 tag_t     sketch_tag,       /* <I> Sketch tag.
                                May be NULL_TAG if there is no existing
                                sketch to which the preferences are to be
                                associated. The preferences will then
                                be applied to the sketches created
                                thereafter, with the exception of character size
                                and decimal places. These two will always come from
                                annotation preferences.
                             */

 int       values[10],          /* <I>
                                Array flag to indicate what action to
                                perform for which sketch preference
                                variable.
                                0: Do nothing
                                1: Action

                                [0]: Snap angle
                                [1]: Sketch name prefix
                                [2]: Vertex name prefix
                                [3]: Line name prefix
                                [4]: Arc name prefix
                                [5]: Conic name prefix
                                [6]: Spline name prefix
                                [7]: Character size
                                [8]: Decimal places
                                [9]: Dimension label
                             */

 double     snap_angle,                       /* <I> Snap angle            */
 char       name_prefix[ UF_OBJ_NAME_BUFSIZE ],     /* <I,len:UF_OBJ_NAME_LEN>
                                                  Sketch name prefix   */

 char       vertex_prefix[ UF_OBJ_NAME_BUFSIZE ],   /* <I,len:UF_OBJ_NAME_LEN>
                                                  Vertex name prefix   */

 char       line_prefix[ UF_OBJ_NAME_BUFSIZE ],     /* <I,len:UF_OBJ_NAME_LEN>
                                                  Line Iname prefix    */

 char       arc_prefix[ UF_OBJ_NAME_BUFSIZE ],      /* <I,len:UF_OBJ_NAME_LEN>
                                                  Arc name prefix      */

 char       conic_prefix[ UF_OBJ_NAME_BUFSIZE ],    /* <I,len:UF_OBJ_NAME_LEN>
                                                  Conic name prefix    */

 char       spline_prefix[ UF_OBJ_NAME_BUFSIZE ],   /* <I,len:UF_OBJ_NAME_LEN>
                                                  Spline name prefix   */

 double     char_size,                        /* <I>  Character size is no longer a sketch preference. The 
                                                 character size will be set for each individual dimension in 
                                                 the sketch. If sketch_tag==NULL_TAG nothing will be done. */

 int        dec_places,                       /* <I>   Decimal places are no longer a sketch preference. The 
                                                 decimal places will be set for each individual dimension in 
                                                 the sketch. If sketch_tag==NULL_TAG nothing will be done. */

 int        dim_label                         /* <I>  Dimension label
                                                 1 : Value
                                                 2 : Expression
                                                 3 : Name
                                              */
);




/*******************************************************************************
This function sets the dimension/sketch curve to reference/active.

The following restrictions applies:
UF_SKET_initialize_sketch must have been previously called.

Environment: Internal  and  External

See Also: UF_SKET_ask_reference_status

History: This function was originally released in V17.0.
*******************************************************************************/
extern UFUNEXPORT int UF_SKET_set_reference_status
( tag_t skt_tag,                    /* <I> Tag of the sketch to which the dim/curve belongs */
  tag_t member,                     /* <I> Array of the dim/curve tags whose state has to be set */
  UF_SKET_reference_status_t status /* <I> UF_SKET_active or UF_SKET_reference */
);


/******************************************************************************
Terminate the current sketch.

The following restrictions applies:
UF_SKET_initialize_sketch must have been previously called.

Note:  When in Drafting it is not possible to terminate the sketch. 

Environment: Internal  and  External

See Also: UF_SKET_initialize_sketch
          UF_SKET_update_sketch

History:
******************************************************************************/
extern UFUNEXPORT int UF_SKET_terminate_sketch ( void );



/******************************************************************************
This function updates the current sketch. If you had call to
UF_SKET_create_geometric_constraint, UF_SKET_create_dimension or
UF_SKET_mirror_objects to create constraints or dimensions in a sketch,
it is highly recommended that this routine should be called before calling
UF_SKET_terminate_sketch.

The following restrictions applies:
UF_SKET_initialize_sketch must have been previously called.

Environment: Internal  and  External

See Also: UF_SKET_initialize_sketch
          UF_SKET_create_dimension
          UF_SKET_create_geometric_constraint
          UF_SKET_mirror_objects
          UF_SKET_terminate_sketch

History: This function was originally released in V16.0.
******************************************************************************/
extern UFUNEXPORT int UF_SKET_update_sketch
(
 tag_t sketch_tag       /* <I>    Sketch object tag.    */
);

/******************************************************************************
This function determines whether a given constraint is inferred or not.

Environment: Internal  and  External

See Also:

History: This function was originally released in V18.0.
******************************************************************************/
extern UFUNEXPORT int UF_SKET_ask_con_is_inferred
(
 tag_t    con_tag,          /* <I>  Constraint object tag. */
 logical *inferred_con_fl   /* <O>  A flag that determines
                                    whether a given con is
                                    inferred or not.       */
);


/******************************************************************************
This function returns all inferred constraints of the given sketch.

Environment: Internal  and  External

See Also:

History: This function was originally released in V18.0.
******************************************************************************/
extern UFUNEXPORT int UF_SKET_ask_inferred_cons_of_sketch
(
 tag_t sketch_tag,       /* <I>  Sketch object tag.      */
 int   *num_cons,        /* <O>  Number of inferred cons.*/
 tag_t **con_tags        /* <OF,len:num_cons>
                                 Array of inferred cons.
                                 Use UF_free to deallocate
                                 the memory when done.   */
);

/******************************************************************************
This function returns a sketch feature eid given a sketch curve eid.

Environment: Internal  and  External

See Also:

History: This function was originally released in V18.0.
******************************************************************************/
extern UFUNEXPORT int UF_SKET_ask_sket_frec_eid
(
   tag_t sket_eid,        /* <I> Sketch curve tag */
   tag_t *sket_frec_eid   /* <O> Sketch feature tag */
);

/******************************************************************************
This function returns TRUE if the given sketch has any out of date references.
This function is valid only for modeling sketches created in V13.0 and later
versions of NX.

Environment: Internal  and  External

History: This function was originally released in V4.0.3.
******************************************************************************/
extern UFUNEXPORT int UF_SKET_is_out_of_date
(
   tag_t   sket_eid,        /* <I> Sketch tag                                    */
   logical *out_of_date     /* <O> TRUE => The sketch has out-of-date references */
);

#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif     /* UF_SKET_H_INCLUDED */
