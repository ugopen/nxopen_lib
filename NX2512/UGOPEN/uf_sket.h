/*******************************************************************************

          Copyright (c) 1995-2006 UGS Corp.
                   All rights reserved




File description:

Open C API interface to the sketcher.  These functions are primarily for old sketches
that are created before UG v13.  A few functions work for more modern sketches, as documented.

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

For the functions listed under "for all sketches", many have a modern equivalent in the
NX Open API.  It is strongly suggested to use the NX Open API instead of these functions
for sketches created after UG v13, where possible.

Public Routines
===================
  -- for all sketches
    UF_SKET_ask_dim_status
    UF_SKET_ask_sketch_info             (supports extracted sketches)
    UF_SKET_ask_sketch_of_geom
    UF_SKET_add_objects
    UF_SKET_ask_exps_of_sketch
    UF_SKET_ask_dimensions_of_sketch
    UF_SKET_ask_geoms_of_sketch         (supports extracted sketches)
    UF_SKET_create_sketch
    UF_SKET_delete_dimensions
    UF_SKET_initialize_sketch
    UF_SKET_terminate_sketch
    UF_SKET_ask_reference_status
    UF_SKET_set_reference_status
    UF_SKET_ask_sket_frec_eid

  -- for V13.0+ sketches only
    UF_SKET_is_out_of_date

  -- for pre-V13.0 sketches only
    UF_SKET_ask_face_sketches
    UF_SKET_ask_feature_sketches
    UF_SKET_ask_sketch_features
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
#include <uf_sket_types.h>

#include <libufun_exports.h>

#ifdef __cplusplus
extern "C" {
#endif


/******************************************************************************
Adds geometric objects to the current sketch.

The following restrictions applies:
1) UF_SKET_initialize_sketch must have been previously called.
2) The construction coordinate system of the arcs you wish to add must be
parallel to the sketch plane.
3) The geometry must already be non-associative, meaning not output of another 
feature.  For new sketches, the geometry must lie on the sketch plane.

Environment: Internal and External

See Also: UF_SKET_initialize_sketch

For v13+ sketches, use <ja_method>NXOpen.Sketch.AddGeometry</ja_method>

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
Returns status of a sketch dimension as well as its expression.

Environment: Internal  and  External

See Also:

For v13+ sketches, use <ja_class>NXOpen.SketchDimensionalConstraint</ja_class>.

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

For v13+ sketches, use <ja_method>NXOpen.Sketch.GetAllConstraintsOfType</ja_method>

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

For v13+ sketches, use <ja_method>NXOpen.Sketch.GetAllExpressions</ja_method>

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
Returns all sketches associated with a face or datum plane.  Only works
for sketches before version UG v13.

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
Returns all sketches associated with a feature.  Only works for sketches before
version UG v9.

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

For v13+ sketches, use <ja_method>NXOpen.Sketch.GetAllGeometry</ja_method>

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

For v13+ sketches, use <ja_method>NXOpen.Sketch.GetOwningSketch</ja_method>

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

See Also: 

For v13+ sketches, use <ja_class>NXOpen.Preferences.PartSketch</ja_class> or 
                       <ja_class>NXOpen.Preferences.SessionSketch</ja_class>

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
Returns all features associated with a sketch. Only works for sketches before
version UG v9.

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

/******************************************************************************
Attaches a non-feature sketch to a planar face or datum plane and returns the
resulting sketch feature tag. For reattaching sketch features from before UG v9
to a different face or datum plane, please use UF_MODL_reattach_target_face.

Environment: Internal  and  External

See Also: UF_MODL_reattach_target_face

For v13+ sketches, use <ja_method>NXOpen.SketchCollection.CreateSketchInPlaceBuilder2</ja_method>

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


/******************************************************************************
Creates an empty sketch.

The following restrictions applies:
UF_SKET_initialize_sketch must have been previously called.

Environment: Internal  and  External

See Also: UF_SKET_initialize_sketch


For v13+ sketches, use <ja_method>NXOpen.SketchCollection.CreateSketchInPlaceBuilder2</ja_method>

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
 tag_t  *sketch_id    /* <O>   Tag of the sketch created    */
);

/******************************************************************************
This routine deletes dimensions given their tags. The dimension tags could
belong to different sketches.

Environment: Internal  and  External

See Also: UF_SKET_create_dimension

For v13+ sketches, use <ja_method>NXOpen.Update.AddObjectsToDeleteList</ja_method>

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

For v13+ sketches, use <ja_method>NXOpen.Update.AddObjectsToDeleteList</ja_method>

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

/*******************************************************************************
This function sets the dimension/sketch curve to reference/active.

The following restrictions applies:
UF_SKET_initialize_sketch must have been previously called.

Environment: Internal  and  External

See Also: UF_SKET_ask_reference_status

For v13+ sketches, use <ja_method>NXOpen.SketchCollection.CreateConvertToFromReferenceBuilder</ja_method>

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

For v13+ sketches, use <ja_method>NXOpen.Sketch.Deactivate</ja_method>

History:
******************************************************************************/
extern UFUNEXPORT int UF_SKET_terminate_sketch ( void );

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
