/************************************************************************************
 *                                                                                  *
 *         Copyright 1992 Siemens Product Lifecycle Management Software Inc.        *
 *                               All Rights Reserved.                               *
 *                                                                                  *
 ************************************************************************************



File description:

The functions in this and the other uf_modl_*.h files allow
you to perform various modeling operations which include functions for:

creation of primitives and features
querying modeling objects
creating, deleting, and editing expressions

Several inquire routines with the prefix UF_MODL_ask_xxxx, return
lists of items. Since identifiers exist for bodies, features, faces and
edges, be careful to use the correct identifiers as input into other
UF_MODL_xxxx routines. The routines that return bodies, faces and
edges contain identifiers that can be used throughout the Open
API. But the routines that return feature identifiers can be used only
within other Open API functions with the prefix UF_MODL_xxxx
that require a feature for input.

For example, calling UF_MODL_ask_body_feats() returns a list of
features that are connected to the input body identifier. The
identifiers contained in this list are valid in the following routines
only:

UF_MODL_ask_xxxx_parms()
UF_MODL_ask_feat_xxxx()
UF_MODL_move_feature()
UF_MODL_delete_feature()

A common mistake in using the UF_MODL_xxxx routines involves the
hierarchy of the solids created. The descending order is body, feature,
face, and then edge. When you create the first primitive, you may
think that the identifier returned is a body identifier, but it is not. To
get the body, you must first call UF_MODL_ask_feat_body() to get the
proper body identifier.

The "ask" routines that inquire about bodies, faces, edges, etc. do not
guarantee a consistent order with respect to location in a list. For
example, if you get the faces on the block, a specific face is not always
found at the same location in the list.

The "ask" routines will return information with respect to the owning
part of the object being inquired, unless specifically stated in the
function's documentation. This is important in mixed unit assemblies where
data is desired in the context of the assembly part. By using the occurrence
tag as input to the "ask" routines, data will be scaled and translated to,
or from, the assembly. By using the prototype tag, data will be returned
in the context of the prototype part units.

When you have more than one solid in a part and you wish to perform
an operation on a solid such as adding a feature or doing a boolean,
you must identify which solid is the target for the operation. Use the
function  UF_MODL_active_part to identify the target
solid. You do not need to identify a solid if it is the only solid or if it
was the last solid you worked on interactively.

Before a body/face/edge is promoted, its occurrence points to the prototype in
the component. After a body/face/edge is promoted, a new prototype is created
and the occurrence is changed so that it points to the new prototype (promoted
prototype). The promoted prototype and the promoted body are one and the same.
Therefore, if you query a promoted body for its prototype with
 UF_ASSEM_ask_prototype_of_occ, it returns the tag of the promoted body.

You can go from a base body/face/edge to the corresponding promoted
body/face/edge using  UF_MODL_prom_map_object_up
Similarly, you can go from a promoted body/face/edge to the corresponding base
body/face/edge using  UF_MODL_prom_map_object_down. Both routines
work with prototypes only.

Work Part Restrictions
For those functions/subroutines that perform an operation (create/edit) with an
object, the object must not be an occurrence and the object must be in
the same part as the work part. If either one of these requirements are
not met, then a NULL_TAG is returned for the object on which the
operation is performed.

*****************************************************************************/

#ifndef UF_MODL_H_INCLUDED
#define UF_MODL_H_INCLUDED


/***************************************************************************

  ***************************************************************************/

#include <uf_defs.h>
#include <uf_modl_types.h>
#include <uf_modl_bsurf.h>
#include <uf_modl_curves.h>
#include <uf_modl_freeform.h>
#include <uf_modl_datum_features.h>
#include <uf_modl_primitives.h>
#include <uf_modl_form_features.h>
#include <uf_modl_udf.h>
#include <uf_modl_sweep.h>
#include <uf_modl_promotions.h>
#include <uf_modl_sketch.h>
#include <uf_modl_taper.h>
#include <uf_modl_blends.h>
#include <uf_modl_hollow.h>
#include <uf_modl_isets.h>
#include <uf_modl_simplify.h>
#include <uf_modl_smd.h>
#include <uf_modl_expressions.h>
#include <uf_modl_utilities.h>
#include <uf_modl_legacy.h>
#include <uf_modl_dieeng.h>
#include <uf_modl_mswp.h>
#include <uf_modl_mswp_types.h>
#include <libufun_exports.h>

#ifdef __cplusplus
extern "C" {
#endif

#ifndef UF_MODL_FILE
#define UF_MODL_FILE
#define   SOLID   70              /* Solid Entity Type */
#define   BODY    0               /* Body EID Sub-type */
#define   FACE    2               /* Face Sub-type */
#define   EDGE    3               /* Edge Sub-type */
#endif

/***************************************************************************
   Prototypes for Modeling Operation
  ***************************************************************************/

/*******************************************************************************
Return the current feature.  Any newly created feature will be created right
after this feature.  When a new feature is created, it is made the current
feature.

Environment: Internal  and  External
See Also:
History: This function was originally released in NX2.
******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_current_feature(
    tag_t     part,         /* <I>
                            NX part tag.
                            */
    tag_t    *feature_id    /* <O> Feature which is the current
                            feature in the given part.
                            */
);

/*******************************************************************************
Define the current feature.  Any newly created feature will be created right
after this feature.  When a new feature is created, it is made the current
feature.

Environment: Internal  and  External
See Also:
History: This function was originally released in V16.0.
******************************************************************************/
extern UFUNEXPORT int UF_MODL_set_current_feature(
    tag_t     feature_id    /* <I> Feature which is to be made the current
                            feature.
                            */
);

/****************************************************************************
Suppresses a list of features. Note that the system adds all implied
features and performs an update.

Environment: Internal  and  External
See Also:
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_suppress_feature(
uf_list_p_t feature_list  /* <I>
                          List of features to suppress.
                          */
);

/****************************************************************************
Unsuppress a list of features. Note that the system  adds all depended
features and performs an update.

Environment: Internal  and  External
See Also:
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_unsuppress_feature(
uf_list_p_t feature_list  /* <I>
                          List of features to unsuppress.
                          */
);

/****************************************************************************
Deletes a list of features. The input is a list of feature identifiers to be
deleted. The only type of output from this routine is the normal error
return from the program call.

Environment: Internal  and  External
See Also:
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_delete_feature(
uf_list_p_t cmtags  /* <I>
                    Linked list of tags for features to be deleted.
                    */
);

/****************************************************************************
Moves a list of features. The input is a list of feature identifiers, the
mode in which you want to move them, and the coordinate system
describing the move. The only type of output from this routine is the
normal error return from the program call.

POINT_TO_POINT option
real_data[0][3] Holds 3 elements to the "from point".
real_data[1][3] Holds 3 elements to the "to point".

AXIS_TO_AXIS option
real_data[0][6] Holds 6 element the first 3 is a point the next 3 elements
                are the from vector
real_data[1][3] Holds 3 element to the to vector

CSYS_TO_CSYS option
The CSYS matrices in real_data are not rotation matrices,
but describe the orientation of the x, y, and z axes of the coordinate
system. In other words, if real_data[0] = {1,2,3, 1,0,0, 0,1,0, 0,0,1 },
the coordinate system has origin (1,2,3). Its X axis is the vector
(1,0,0); Y axis is (0,1,0); and Z axis is (0,0,1).

The last nine components are not a rotation matrix but are, in fact,
the inverse of the CSYS rotation matrix. Also, the data in
real_data[0]) (as with all CMOD arrays representing matrices) is
column oriented. That is, matrices look like:
(Element1       Element4
 Element2       Element5
 Element3       Element6)

Whenever most Modeling operations are performed in Open API, the
system usually takes care of updating the database. However when you
move a feature this is not true. As a result, we recommend that after
moving a feature using the routine UF_MODL_move_feature, you should
update the database by calling routine UF_MODL_update.

Environment: Internal  and  External
See Also: UF_MODL_update
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_move_feature(
uf_list_p_t cmtag ,/* <I>
                   Linked list of tags for features to be moved.
                   */
int mode ,/* <I>
          Option specifying how move is to be done.
          POINT_TO_POINT  ( 0 )
          AXIS_TO_AXIS    ( 1 )
          CSYS_TO_CSYS    ( 2 )
          */
double  real_data[2][12]  /* <I>
                          CSYS describing the move. real_data[0] holds 12
                          element reference coordinate system matrix (first
                          three elements translation, remainder is rotation).
                          real_data[1] holds 12 element destination
                          coordinate system matrix.
                          */
);

/****************************************************************************
Reorders features in the modeling application. Note that this routine
performs an update.  Routine UF_MODL_ask_body_feats returns features in the
current creation order.

Environment: Internal  and  External
See Also:
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_reorder_feature(
tag_t  reference_feature ,/* <I>
                          Pivot feature.
                          */
uf_list_p_t reposition_features ,/* <I>
                                 List of features to reorder.
                                 */
int    method  /* <I>
               Reorder method:
               1 = Before
               2 = After
               */
);

/******************************************************************************
Ask if a feature can be copied

Environment: Internal  and  External
See Also:
History:
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_feature_can_be_copied
(
    tag_t   feature_eid,              /* <I>
                                      Features identifier
                                      */
    logical *copy_flag                /* <O>
                                      flag TRUE/FALSE;
                                      */
);

/******************************************************************************
Returns the parent references of an array of features and the name
of each parent's reference.

Environment: Internal and External
See Also:
History: This function was originally released in V15.0.
******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_references_of_features
(
    tag_t   *feature_array,           /* <I,len:num_features>
                                             Array of features identifier
                                      */
    int     num_features,             /* <I>
                                      Number of features
                                      */
    tag_t   **parents,                /* <OF,len:num_parents>
                                      An array of all the parents. This array
                                      must be freed by calling UF_free.
                                      */
    char    ***parent_names,          /* <OF,len:num_parents>
                                      An array of names of each parent.  This
                                      array must be freed by calling
                                      UF_free_string_array.
                                      */
    int     *num_parents              /* <O>
                                      Number of parents.
                                      */
);

/******************************************************************************
Paste an array of features into the current work part.

Environment: Internal and External
See Also:
History: Introduced in V1604, NX1.0.3, NX2.0. Replaces UF_MODL_paste_features.
         Outputs new features.
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_copy_paste_features
(
    tag_t   *feature_array,            /* <I,len:num_features>
                                       Array of features identifier
                                       */
    int     num_features,              /* <I>
                                       Number of features
                                       */
    tag_t   *old_parents,              /* <I,len:num_parents>
                                       Array of old parents
                                       */
    tag_t   *new_parents,              /* <I,len:num_parents>
                                       Array of new parent
                                       */
    int     num_parents,               /* <I>
                                       Number of refrences
                                       */
    int     expression_transfer_mode,  /* <I>
                                       Type of expression copy -
                                       0 = New, 1 = link, 2 = instance
                                       */
    int     parent_transfer_mode,      /* <I>
                                       Type of reference copy -
                                       0 = New, 1 = link, 2 = instance
                                       */
    tag_p_t * new_feature_array        /* <OF,len:num_features>
                                       Array of new features
                                       */
);

/******************************************************************************
Paste an array of features into the current work part.

Environment: Internal and External
See Also: UF_MODL_copy_paste_features
History: This function is replaced by UF_MODL_copy_paste_features.
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_paste_features
(
    tag_t   *feature_array,            /* <I,len:num_features>
                                       Array of features identifier
                                       */
    int     num_features,              /* <I>
                                       Number of features
                                       */
    tag_t   *old_parents,              /* <I,len:num_parents>
                                       Array of old parents
                                       */
    tag_t   *new_parents,              /* <I,len:num_parents>
                                       Array of new parent
                                       */
    int     num_parents,               /* <I>
                                       Number of refrences
                                       */
    int     expression_transfer_mode,  /* <I>
                                       Type of expression copy -
                                       0 = New, 1 = link, 2 = instance
                                       */
    int     parent_transfer_mode       /* <I>
                                       Type of reference copy -
                                       0 = New, 1 = link, 2 = instance
                                       */
);

/****************************************************************************
The input to UF_MODL_active_part is a solid body (type 70, subtype 0).
A subtle difference between interactive and programmatic access
to NX can be seen in the area of selection. In Open API,
when you have more than one solid in a given part, you must specify
which solid is "active." This operation is done automatically in
interactive mode. For example, to add features to two solids
interactively, you select a face on one solid, add the feature, and then
select the next solid.

To simulate this in Open API, you need to know the body obj_id's
for each solid in order to move from one solid to the next. So before
you can add a feature to a particular solid, you need to call
UF_MODL_active_part with the appropriate solid body. If you have
only one solid in the part, then it is always the "active" solid, and
calling UF_MODL_active_part is unnecessary.

Environment: Internal  and  External
See Also:
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_active_part(
tag_t body_obj_id ,/* <I>
                   Body obj_id.
                   */
int flag  /* <I>
          Display flag:
           TRUE for change display color,
           FALSE for do not change display color.
          */
);

/****************************************************************************
Sets the global solid density to the input value. The density units can be
any one of the following:

     UF_MODL_pounds_inches
     UF_MODL_pounds_feet
     UF_MODL_grams_centimeters
     UF_MODL_kilograms_meters

Environment: Internal  and  External
See Also: 
          UF_MODL_ask_default_density
History: Originally released in V16.0
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_set_default_density
(
    double                  density, /* <I>
                                     default density
                                     */
    UF_MODL_density_units_t units    /* <I>
                                     units of 'density'
                                     */
);
/******************************************************************************
Set the density of a body.
The input must be a body tag.
If the body is in the context of an assembly, it is the caller function's
responsibility to retrieve the body tag before this function can be called, i.e.,
if body is an occurrence, then the body tag must be retrieved first.

Environment:Internal and External
See Also:
History:
*******************************************************************************/
extern UFUNEXPORT int UF_MODL_set_body_density
(
    tag_t                   body,   /* <I>
                                    solid/sheet body
                                    */
    UF_MODL_density_units_t units,  /* <I>
                                    the unit of 'density'
                                    */
    double                  density /* <I>
                                    density of body
                                    */
);

/******************************************************************************
Sets the distance tolerance found in the Modeling Preferences dialog box.
Return:
      Void.
Environment: Internal  and  External
See Also:
History:
 ******************************************************************************/
extern UFUNEXPORT void UF_MODL_set_distance_tolerance(
double * tolerance ,/* <I>
                    Distance tolerance. Value must be greater than
                    metric 1e-5 or English 3e-7.
                    */
int * err_flag  /* <EC>
                Error code:
                0 = No error
                1 = Invalid value, tolerance not changed
                */
);

/******************************************************************************
Sets the angle tolerance found in the Modeling Preferences dialog box.
Return:
       Void.
Environment: Internal  and  External
See Also:
History:
 *****************************************************************************/
extern UFUNEXPORT void UF_MODL_set_angle_tolerance(
double * tolerance ,/* <I>
                    Angle tolerance. Value must be greater than e-10
                    (greater than zero).
                    */
int * err_flag  /* <EC>
                Error code:
                0 = No error
                1 = Invalid value, tolerance not changed
                */
);

/******************************************************************************
Changes the current setting for the sheet/solid body type modeling
preference. This preference is used when creating bodies through
curves to allow you to control the type of body created. The body type
option is used in the Through Curve Mesh, Through Curves, Extruded
Body, Body of Revolution, Swept, Section Surface and Ruled Free
Form Feature creation options.

Environment: Internal  and  External
See Also: UF_MODL_ask_body_type_pref
History:
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_set_body_type_pref(
int body_type  /* <I>
               Desired setting of the body type preference:
               UF_MODL_SOLID_BODY
               UF_MODL_SHEET_BODY
               */
);

/****************************************************************************
Performs a Boolean operation between two bodies.
NOTE: UF_NULLSIGN, which usually indicates create, defaults to
UF_POSITIVE (add to target solid).

Environment: Internal  and  External
See Also:
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_operations(
tag_t target ,/* <I>
              Target solid.
              */
tag_t  tool ,/* <I>
             Tools solid.
             */
UF_FEATURE_SIGN sign  /* <I>
                      The sign of the operation to be performed.
                       UF_NULLSIGN = same as UF_POSITIVE
                       UF_POSITIVE = add to target solid
                       UF_NEGATIVE = subtract from target solid
                       UF_UNSIGNED = intersect with target solid
                      */
);

/****************************************************************************
Unite two bodies.

UF_MODL_unite_bodies_with_retained_options honors the setting of the
"Boolean Face Properties from" option of the Modeling Preferences dialog,
but UF_MODL_unite_bodies always applies the display properties of
the target body to new faces.

Environment: Internal  and  External
See Also: 
          UF_MODL_unite_bodies_with_retained_options
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_unite_bodies(
        tag_t  target,     /* <I>
                           Target and resultant body
                           */
        tag_t  tool        /* <I>
                           Tool body
                           */
);


/****************************************************************************
Subtract two bodies.

UF_MODL_subtract_bodies_with_retained_options honors the setting of the
"Boolean Face Properties from" option of the Modeling Preferences dialog,
but UF_MODL_subtract_bodies always applies the display properties of
the target body to new faces.

Environment: Internal  and  External
See Also: 
          UF_MODL_subtract_bodies_with_retained_options
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_subtract_bodies(
        tag_t  target,            /* <I>
                                  Target body
                                  */
        tag_t  tool,              /* <I>
                                  Tool body
                                  */
        int    *num_result,       /* <O>
                                  Number of resultant bodies
                                  */
        tag_t  **resulting_bodies /* <OF,len:num_result>
                                  Resultant bodies.  These must be free by
                                  calling UF_free.
                                  */
);


/****************************************************************************
Intersect two bodies.

UF_MODL_intersect_bodies_with_retained_options honors the setting of the
"Boolean Face Properties from" option of the Modeling Preferences dialog,
but UF_MODL_intersect_bodies always applies the display properties of
the target body to new faces.

Environment: Internal  and  External
See Also: 
          UF_MODL_intersect_bodies_with_retained_options
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_intersect_bodies(
        tag_t  target,            /* <I>
                                  Target body
                                  */
        tag_t  tool,              /* <I>
                                  Tool body
                                  */
        int    *num_result,       /* <O>
                                  Number of resultant bodies
                                  */
        tag_t  **resulting_bodies /* <OF,len:num_result>
                                  Resultant bodies.  This array must be freed
                                  by calling UF_free.
                                  */
);


/******************************************************************************
Trims a solid body.

Environment: Internal  and  External
See Also:
History:
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_trim_body(
tag_t target_body ,/* <I>
                   Target body to be trimmed.
                   */
tag_t tool_tag ,/* <I>
                Tag of face, datum plane, or plane to be used for trim.
                */
int direction_flag ,/* <I>
                    0 = Accept default direction
                    1 = Reverse direction
                    */
tag_t * trim_feature  /* <O>
                      Resultant trim_feature identifier tag
                      */
);

/******************************************************************************
Trims a sheet body to a collection of curves, faces, or planes. The
curves can be projected along surface normals or along a vector.
Points on the sheet body define which region(s) of the sheet are to be
kept or discarded by the trim. If it can be determined that a trim
failure has occurred because there were gaps between the trimming
geometry, then the system returns the positions of those gaps  with the
corresponding return code.

The UF_MODL_trim_object_t data structure defines the objects used to trim the
sheet body. If the object is a curve, then the projection method must be
defined.

Environment: Internal  and  External
See Also:

History:
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_trim_sheet(
tag_t  sheet_body_tag ,/* <I>
                       Tag of sheet body to trim.
                       */
int  count_bounding_objects ,/* <I>
                             Number of trimming objects.
                             */
UF_MODL_trim_object_t ** bounding_objects ,/* <I,len:count_bounding_objects>
                                            Array of pointers to structures
                                            holding trimming object data.
                                            */
double  projection_vector[3] ,/* <I>
                            Vector for curves projected along a vector.
                            */
int  point_key ,/* <I>
                Points define regions to:
                0 = discard
                1 = keep
                */
int point_count ,/* <I>
                 Number of points. (Number of regions.)
                 */
double point_coords[] ,/* <I,len:3*point_count>
                       Array of points on the sheet.
                       (3 * point_count values.)
                       */
double tolerance ,/* <I>
                  Distance tolerance for any approximations.
                  */
int *number_gap_points ,/* <O>
                       Number of points returned in gap_points.
                       */
double ** gap_points  /* <OF,len:3*number_gap_points,free:UF_free>
                      Array of points showing positions of gaps.
                      (3 * number_gap_points values.)  This array must be freed
                      by calling UF_free.
                      */
);

/*******************************************************************************
Split one or more bodies with a cutting plane or a body face.

Environment:Internal and External
See Also: 
History: Originally released in V16.0
*******************************************************************************/
extern UFUNEXPORT int UF_MODL_split_body
(
   int       num_bodies,        /* <I> Number of bodies to be split */
   tag_t     *bodies,           /* <I,len:num_bodies>
                                       Bodies to be split */
   tag_t     cutting_body,      /* <I> Cutting plane or a sheet body */
   int       *num_split_bodies, /* <O> Number of the split bodies */
   tag_t     **split_bodies     /* <OF,len:num_split_bodies>
                                Returned split bodies.  This array
                                must be freed by calling UF_free.
                                */
);

/*******************************************************************************
Split one or more bodies with a cutting plane or a body face and retain the tool body.

Environment:Internal and External
See Also: 
History: Originally released in NX304
*******************************************************************************/
extern UFUNEXPORT int UF_MODL_split_body_retain_tool
(
   int       num_bodies,        /* <I> Number of bodies to be split */
   tag_t     *bodies,           /* <I,len:num_bodies>
                                       Bodies to be split */
   tag_t     cutting_body,      /* <I> Cutting plane or a sheet body */
   int       *num_split_bodies, /* <O> Number of the split bodies */
   tag_t     **split_bodies     /* <OF,len:num_split_bodies>
                                Returned split bodies.  This array
                                must be freed by calling UF_free.
                                */
);

/******************************************************************************
Replaces a set of faces on a body by patching in the faces of a sheet
body. The outer edges of the sheet must lie on or near faces of the
target. The faces on the "reverse" side of the tool sheet are removed
and replaced by the sheet body.


Environment: Internal  and  External
See Also:
History:
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_patch_body(
tag_t target_body ,/* <I>
                   Object id of target body to be patched
                   */
tag_t tool_sheet ,/* <I>
                  Object id of sheet body to patch into target
                  */
int reverse ,/* <I>
             Patch direction flag:
             UF_MODL_ALONG_NORMAL - along surface normal of tool_sheet
             UF_MODL_OPPOSITE_NORMAL -  opposite surface normal of tool_sheet
             */
tag_t * feature_obj_id  /* <O>
                        Feature object identifier of created patch feature
                        */
);

/******************************************************************************
Mirrors the input body about the datum plane specified.

Environment: Internal  and  External
See Also: 
History:
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_create_mirror_body(
const tag_t body ,/* <I>
            Object identifier of the body to be mirrored.
            */
const tag_t datum_plane ,/* <I>
                   Object identifier of the datum plane
                   */
tag_t *mirrored_body  /* <O>
                        Object identifier for the mirror body feature.
                        */
);

/****************************************************************************
Allows you to delete all the parameters of the solid bodies in the input list.

Environment: Internal  and  External
See Also: 
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_delete_body_parms(
uf_list_p_t  body_list  /* <I>
                        List of solid bodies
                        */
);

/****************************************************************************
Each sheet body and solid body on the input list will be made into an
unparameterized feature.

Each curve or point on the input list which is an output of a feature
will have the associativity removed, and will become basic curves and points.

Sketch curves are not supported by this function.

Environment: Internal  and  External
See Also:
History: This function is provided in v17 initially.
****************************************************************************/
extern UFUNEXPORT int UF_MODL_delete_object_parms(
uf_list_p_t  object_list  /* <I>
                          List of bodies,curves and points
                          */
);

/******************************************************************************
Replaces the body of an unparameterized feature with a copy of
another body. Both bodies must be single face sheet bodies.

Environment: Internal  and  External
See Also:
History:
 *****************************************************************************/
extern UFUNEXPORT int UF_MODL_replace_body_data(
tag_t original_feature ,/* <I>
                        Feature Object Identifier of unparameterized
                        feature which is to have its body replaced. Must be
                        a single face sheet body.
                        */
tag_t new_body  /* <I>
                Object Identifier of the single face sheet body to
                copy.
                */
);

/******************************************************************************
Replaces the tool body and target body of a boolean feature.

Environment: Environment: Internal and External
See Also: 
History: This function was originally released in V15.0.
*******************************************************************************/
extern UFUNEXPORT int UF_MODL_replace_boolean_body
(
    tag_t boolean_feature_obj_id, /* <I>
                                  The object identifier of a boolean feature to
                                  be modified.
                                  */
    UF_MODL_boolean_body_e_t type, /* <I>
                                   The type of body:
                                       UF_MODL_TARGET_BODY
                                       UF_MODL_TOOL_BODY
                                   */
    tag_t new_body /* <I>
                   The body tag of the new body which will replace either the
                   target or the tool body.
                   */
);

/****************************************************************************
Edits the u and v grid counts of a face or a body.

Environment: Internal  and  External
See Also: 
          UF_MODL_ask_face_grid_count
History: Originally released in V16.0
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_edit_face_grid_count
(
   tag_t     object,           /* <I>
                               tag of face or body
                               */
   int       u_count,          /* <I>
                               u grid counts
                               */
   int       v_count           /* <I>
                               v grid counts
                               */
);

/******************************************************************************
Based on the specified input, either removes edges and vertices or
joins separate faces into a single b-surface for a body. For option = 1, this
function removes all of the unnecessary edges and vertices from the input body.
For option= 2, the function joins two separate faces into one b-surface (within
the same body).

Environment: Internal  and  External
See Also:
History:
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_edit_face_join(
int opt ,/* <I>
         Joining option:
         1 = On same surface
         2 = convert to B-surface
         */
tag_t body_tag ,/* <I>
                Tag of body containing faces to be joined
                */
tag_t face_tags[2] ,/* <I>
                  Tags of 2 faces to be joined (if opt=2)
                  */
tag_t *result_tag  /* <O>
                  Tag of resulting feature.
                  */
);

/******************************************************************************
Replaces the current set of input faces with the set of faces input
through the parameter faces.

Environment: Environment: Internal and External
See Also: 
History: This function was originally released in V15.0.
*******************************************************************************/
extern UFUNEXPORT int UF_MODL_redefine_replace_faces
(
    tag_t feature_eid,     /* <I>
                           OFFSET or HOLLOW feature
                           */
    int number_of_faces,   /* <I>
                           Number of faces in faces array
                           */
    tag_t face_eids[]      /* <I,len:number_of_faces>
                           Array of faces to replace the current input faces in
                           the feature.
                           */
);

/******************************************************************************
Edits the string structure of a feature. The following restrictions apply:
   1. The valid features for this function are:
         Curve Mesh
         Thru Curves
         Ruled
         Swept
         Bounded Plane
   2. Only the Replace option may be used with Ruled and Bounded Plane features.
   3. When adding a new string at the beginning of a surface, use index = 0.
   4. The string input must be the entire string being changed, even if
      only one curve within a multi-curve string is changing. If you
      wish to edit one curve in a multi-curve string, you must build the
      entire new string.
   5. This function does not perform an update of the feature. You
      should call UF_MODL_update after you have completed all your
      string edit operations.

Environment: Internal  and  External
See Also:
History:
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_replace_feat_strings(
tag_t  feature_obj_id ,/* <I>
                       Feature object identifier
                       */
int  option ,/* <I>
             Operation to be performed
             UF_MODL_STRING_ADD = Add a string
             UF_MODL_STRING_REMOVE = Remove a string
             UF_MODL_STRING_REPLACE = Replace a string
             */
UF_STRING_p_t string ,/* <I>
                      Pointer to the string structure of a single string to
                      add or replace.
                      */
int  string_set ,/* <I>
                 Set of strings on which to perform the operation,
                 especially when the feature has more than 1 set of
                 strings
                         If feature = Thru Curve Mesh:
                         1 = Primary Curves
                         2 = Cross Curves
                         If feature = Freeform Sweep
                         1 = Guide Curves
                         2 = Section Curves
                         All others: string_set = 1
                 */
int  index  /* <I>
            Index at which to perform the operation starting at index=1
            If UF__MODL_STRING_ADD, add the string after the index
            If UF_MODL_STRING_REMOVE or UF_MODL_STRING_REPLACE,
            remove or replace at the index
            */
);

/******************************************************************************
This routine redefines a target face.

Environment: Internal  and  External
See Also:
History:
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_reattach_target_face(
tag_t feature_eid ,/* <I>
                   the feature being reattached
                   */
tag_t face_eid ,/* <I>
                new target placement face
                */
double point[3],/* <I>
                 new feature position
                 */
int flip ,/* <I>
          1: if the datum plane is flipped, else 0
          */
logical delete_rpo  /* <I>
                    1 if the rpo dims are to be deleted
                    */
);

/*******************************************************************************
Reattaches the new tool placement face.

Environment: Internal  and  External
See Also:
History:
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_reattach_tool_face(
tag_t feature_eid ,/* <I>
                   the feature being reattached
                   */
tag_t face_eid ,/* <I>
                the new tool placement face
                */
logical delete_rpo  /* <I>
                    TRUE, if the rpo dims are to be deleted
                    */
);

/******************************************************************************
Redefines the first thru/trim face.

Environment: Internal  and  External
See Also:
History:
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_reattach_thru_faces(
tag_t feature_eid ,/* <I>
                   the feature being reattached
                   */
int number_of_faces ,/* <I>
                     the number of trim/thru faces to be redefined
                     */
tag_t face_eids[] ,/* <I,len:number_of_faces>
                    the new thru/trim faces
                    */
logical delete_rpo  /* <I>
                    1 if the rpo dims are to be deleted
                    */
);

/******************************************************************************
Removes the thru faces from a hole or slot feature.

Environment: Environment: Internal and External
See Also:
History: This function was originally released in V15.0.
*******************************************************************************/
extern UFUNEXPORT int UF_MODL_remove_thru_faces
(
    tag_t feature_eid      /* <I>
                           The object identifier of the feature from which
                           the thru faces will be removed.
                           */
);

/******************************************************************************
Adds thru faces to a hole or slot feature.  A hole uses one thru face and a
slot uses two.

Environment:Internal and External
See Also:
History: This function was originally released in V15.0.
*******************************************************************************/
extern UFUNEXPORT int UF_MODL_add_thru_faces
(
    tag_t feature_eid,     /* <I>
                           The object identifier of the feature to which the
                           thru faces will be added.
                           */
    int number_of_faces,   /* <I>
                           The number of thru faces to add.
                           */
    tag_t face_eids[]      /* <I,len:number_of_faces>
                           An array of thru faces that will be added to the
                           feature.
                           */
);

/******************************************************************************
This routine is used to redefine the directional reference.

Environment: Internal  and  External
See Also: UF_MODL_reattach_target_face
History:
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_reattach_dir_ref(
tag_t feature_eid ,/* <I>
                   the feature being reattached
                   */
tag_t ref_eid ,/* <I>
               new directional reference
               */
int ref_is_horizontal ,/* <I>
                       1: reference is horizontal; 0: reference is vertical
                       */
logical delete_rpo  /* <I>
                    1 if the rpo dims are to be deleted
                    */
);

/******************************************************************************
This routine gets the direction of the directional reference. Given the
placement face and directional reference, the direction returned may
be used to determine whether to reverse the direction or not; i.e., to
set the value of the "reverse" argument in UF_MODL_reverse_dir_ref.

Environment: Internal  and  External
See Also: UF_MODL_reverse_dir_ref
History:Originally released in V13.0.4.  In V15.0 the argument, face_eid, was
added.
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_calculate_ref_dir
(
    tag_t feature_eid,         /* <I> feature eid */
    tag_t face_eid,            /* <I> target placement face. */
    logical flip_face_normal,  /* <I> this flag is only used when the target
                                  placement face is a
                                  datum plane. 1 flip the datum plane.
                                */
    tag_t ref_eid,             /* <I> directional reference. */
    double ref_dir[3]          /* <O> vector representing the directional
                                  reference. */
);

/******************************************************************************
Redefines the directional reference of a feature.

Environment: Internal  and  External
See Also: UF_MODL_calculate_ref_dir
          UF_MODL_ask_link_faces
History:Originally released in V15.0
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_reverse_dir_ref
(
    tag_t feature_eid,     /* <I> the feature being reattached */
    tag_t ref_eid,         /* <I> the new directional reference */
    int ref_is_horizontal, /* <I> 1: reference is horizontal, 0: reference is
                                  vertical */
    logical delete_rpo,    /* <I> 1: delete rpo dims */
    logical reverse        /* <I> 1: to reverse directional reference */
);

/******************************************************************************
Sets the current fail option in case an update failure occurs. This
allows the user to specify the update behavior in advance, should an
error occur in the middle of a modeling update. It would be as if a
user in interactive NX had selected the UNDO, SUPPRESS,
SUPPRESS ALL, ACCEPT_ALL or INTERRUPT button in the Edit 
During Update dialog.

The user can also set a variable of UGII_UPDATE_FAIL_OPTION before running 
an NX Open API and set it to any of the values defined in UF_MODL_update_option_e.

Environment: Internal  and  External
See Also: 
History:Original release was in V14.0.
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_set_update_fail_option(
UF_MODL_update_option_t new_fail_option  /* <I>
                                         Sets the update fail option to the
                                         given value.
                                         */
);

/****************************************************************************
Updates a part. You call this routine after you use UF_MODL_import_exp,
UF_MODL_edit_exp, and UF_MODL_move_feature. Imported and edited expressions
do not take effect until you update the part. After you move a feature, please
update the database.

Environment: Internal  and  External
See Also:
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_update( void );

/****************************************************************************
This function will trigger model update similar to UF_MODL_update. However
it will achieve a smoother animation display when the feature editing is done
in a loop.
Environment: Internal  and  External
See Also:
History:This function was originally released in NX3
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_update_for_animation ( void );

/******************************************************************************
Logs all the features in the current work part to the NX update list,
then performs an update. You may use this function to check whether or not all
the features in a part can be updated without modifying the part.  This
function is different from UF_MODL_update, which updates modified objects and
dependent objects only.  UF_MODL_update_all_features returns a value of zero
if the update completes successfully. It returns the error code
UF_MODL_ERR_PENDING_UPDATE, if it detects that the model has been modified and
the corresponding update has not been performed yet. It also returns the error
code of the first encountered failure, should the update fail.

Environment: Internal  and  External
See Also: 
History:This function was originally released in V14.0.
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_update_all_features( void );

/****************************************************************************
Compares two solid edges, or two solid faces based on a relation.
Currently, only the `geometric equivalence' relation is supported. Two
objects are geometrically equivalent if their underlying geometries
occupy the same position(s) in space.

Environment: Internal  and  External
See Also:
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_compare(
tag_t object1 ,/* <I>
               Object identifier of first object (valid objects are
               faces and edges)
               */
tag_t object2 ,/* <I>
               Object identifier of second object (valid objects are
               faces and edges)
               */
int relation ,/* <I>
              Relation to be used for comparison.
              1 = Geometric Equivalence
              */
int * equivalent  /* <O>
                     1 = If the relation exists between two objects
                     0 = Otherwise
                  */
);

/******************************************************************************
Compares two solid edges, or two solid faces based on the input
tolerances. If a successful comparison occurs, then the result returns
in the status argument.

The following description explains how the tolerances work by
showing how the function compares two faces. To compare two faces
the system facets the first face using the input facet_tolerance. The
facet_tolerance means that the distance from any point on a facet to
the face it was derived from must be less than this tolerance. The
distance from each facet vertex is then measured to the second face
and if this distance is less than the input distance_tolerance then this
point is considered to be on the second face. If the first face is on the
second face then the process repeats, but this time testing that the
second face is on the first face. It is recommended that tolerances be
no tighter than .01 mm ( 0.00001 meters ) or 0.000254 inches.

Environment: Internal  and  External
See Also:

History:Original release was in V14.0.
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_compare_topology(
tag_t solid_object1 ,/* <I>
                     Object identifier of first object (valid objects are
                     faces and edges)
                     */
tag_t solid_object2 ,/* <I>
                     Object identifier of second object (valid objects are
                     faces and edges)
                     */
double facet_tolerance ,/* <I>
                        Specifies the maximum distance any point on a
                        facet can be from its parent surface. All vertices of
                        facets are on the surface.
                        */
double distance_tolerance ,/* <I>
                           Specifies the maximum distance a vertex of a facet
                           can be from the other surface.
                           */
int * status  /* <O>
              Status value:
              COMPARE_NOMATCH
              COMPARE_FACES_IDENTICAL
              COMPARE_FACES_EQUIVALENT
              COMPARE_SURFACES_IDENTICAL
              COMPARE_SURFACES_EQUIVALENT
              COMPARE_EDGES_IDENTICAL
              COMPARE_EDGES_EQUIVALENT
              COMPARE_CURVES_IDENTICAL
              COMPARE_CURVES_EQUIVALENT
              Descriptions for these values are given in a table
              which follows in the general function description.
              */
);

/*******************************************************************************
Validate all of the input bodies, and return a code for each body indicating
if it is valid or not.

Environment:Internal and External
See Also: 
History: Originally released in V16.0
*******************************************************************************/
extern UFUNEXPORT int UF_MODL_validate_body
(
   int       num_bodies,        /* <I> Number of bodies to be validated */
   tag_t     *bodies,           /* <I,len:num_bodies>
                                       Array of bodies to be validated */
   int       *valid_info        /* <O> Validity info for each body.  This array
                                must have been allocated by the caller as
                                int valid_info[num_bodies].  There will be one
                                status per body, 1 indicates that the body is
                                valid and 2 indicates that the body is invalid.
                                valid_info[0] is the code for bodies[0], and
                                so on up to valid_info[num_bodies-1] and
                                bodies[num_bodies-1].
                                */
);

/******************************************************************************
Computes the requested derivatives of a face at the given parameter
values.

Environment: Internal  and  External
See Also:
History:
 *****************************************************************************/
extern UFUNEXPORT int UF_MODL_evaluate_face (
tag_t face_tag ,/* <I>
                Face tag
                */
int deriv_request ,/* <I>
                   order of the derivative to be computed:
                   UF_MODL_EVAL  -  position
                   UF_MODL_EVAL_DERIV1 -  position and first partial
                   UF_MODL_EVAL_DERIV2 - position, first partial and second
                                         partial
                   UF_MODL_EVAL_DERIV3 -  position, first, second and third
                                          partials
                      Defaults to UF_MODL_EVAL_DERIV2 for Blend faces

                   UF_MODL_EVAL_UNIT_NORMAL - position, first partials and
                                              unitized normal.
                   UF_MODL_EVAL_NORMAL - position, first partials and the
                                         ununitized normal.
                   UF_MODL_EVAL_ALL - position, normals and all the partials up
                                      to the third order.
                      Defaults to UF_MODL_EVAL_DERIV2 for Blend faces
                   */
double parms[2] ,/* <I>
                 u,v values at which derivatives are to be computed.
                 */
UF_MODL_SRF_VALUE_p_t eval_result  /* <O>
                                   Pointer to the structure containing
                                   position and derivatives:
                                   srf_pos[3]       - position
                                   srf_du[3]         - d/du
                                   srf_dv[3]         - d/dv
                                   srf_unormal[3] - unit normal
                                   srf_d2u[3]       - d2/du2
                                   srf_dudv[3]     - d2/dudv
                                   srf_d2v[3]       - d2/dv2
                                   srf_d3u[3]       - d3/du3
                                   srf_d2udv[3]    - d3/du2dv
                                   srf_dud2v[3]    - d3/dud2v
                                   srf_d3v[3]         - d3/dv3
                                   srf_normal[3]     - d/du X d/dv
                                   */
);

/******************************************************************************
Evaluates the parm structure at the given parameter value.  If the parm method
type is UF_MODL_PARM_CONSTANT, the value returned is the same regardless of
the parameter value that is passed in.

Environment: Internal  and  External
See Also:
History:Original release was in V13.0.
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_evaluate_parm(
UF_MODL_parm_p_t  parm ,/* <I>
                        Pointer to parm structure to evaluate
                        */
double  parameter ,/* <I>
                   Parameter at which to evaluate.  Must be between 0 and 1.
                   */
double * value  /* <O>
                Value of parm at given parameter.
                */
);

/******************************************************************************
Determines the intersection between the two input objects and
outputs information describing the intersection.

Environment: Internal  and  External
See Also: 
History:
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_intersect_objects (
tag_t object_1 ,/* <I>
                First object to participate in the intersection.
                */
tag_t object_2 ,/* <I>
                Second object to participate in the intersection
                */
double tolerance ,/* <I>
                  Tolerance used to determine if the objects
                  intersect. Any time object 1 passes within this
                  distance of object 2, it is considered an
                  intersection. This tolerance is a distance
                  tolerance in the units of the current work
                  part.
                  This input variable will only be used when object_1 or
                  object_2 is a point.  All other cases will use the 
                  Parasolid tolerance.
                  */
int * num_intersections ,/* <O>
                         Number of intersections found
                         */
UF_MODL_intersect_info_p_t ** intersections  /* <OF,len:num_intersections>
                                             Array of intersection information
                                             found, the memory allocated for
                                             this array and each element of the
                                             array should be freed with UF_free.
                                             */
);

/****************************************************************************
Checks each specified tool body against the single target body for interference.
An interference status is returned for each tool body.

Objects may be created as part of the interference checking.  These objects are
tagged for deletion, but to make sure the memory is freed and avoid memory overflow,
UF_MODL_update should be called following the call to UF_MODL_check_interference.

Environment: Internal  and  External
See Also: 
History: Originally released in V16.0
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_check_interference
(
    tag_t  target,    /* <I>
                      Target body against which interference is checked
                      */
    int    num_tools, /* <I>
                      Number of tool bodies specified in tools array
                      */
    tag_t  *tools,    /* <I,len:num_tools>
                      Tool bodies whose interference with target is inquired.
                      Dimensioned to num_tools
                      */
    int    *results   /* <O,len:num_tools>
                      Interference status for each tool body. The caller is
                      responsible for allocating it with an array size of
                      num_tools.
                      = 1 -> there is interference
                      = 2 -> no interference
                      = 3 -> touching, that is coincident faces
                      */
);

/****************************************************************************
Fires a ray at a list of transformed (optionally) bodies and returns information
about each face that is hit.  A ray that is tangent to the interior of a
face, but does not cross through the face is not considered a hit.  The lists
containing returned information are in the order of its distance from the
origin of the ray, the closest first.

The caller is responsible for freeing hit_list with UF_free.

Environment: Internal  and  External
See Also: 
History: Originally released in V16.0
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_trace_a_ray
(
    int     num_bodies,     /* <I>
                            The number of bodies that are to be hit
                            */
    tag_t   *bodies,        /* <I,len:num_bodies>
                            Array of body tags that are to be hit.  This array
                            is dimensioned to num_bodies.
                           */
    double  origin[3],      /* <I>
                            Point from which the ray is fired.
                            */
    double  direction[3],   /* <I>
                            The direction the ray is fired.
                            */
    double  transform[16],  /* <I>
                            Transformation needed to convert bodies into the
                            same co-ordinate system as the ray. Initialize
                            with UF_MTX4_identity. Only rotation and
                            translation are allowed.
                            */
    int     num_desired,    /* <I>
                            Maximum number of hit points desired.  A value of
                            zero requests that all hit points be returned.
                            */
    int     *num_results,   /* <O>
                            number of hit points found
                            */
    UF_MODL_ray_hit_point_info_p_t  *hit_list  /* <OF,len:num_results>
                            A pointer to an array of structures where each array
                            element will contain information about each hit.
                            The first element in this array will contain hit
                            point information that is closest to the origin
                            of the ray and the rest of the elements will
                            contain points that continue in order of increasing
                            distance.  The caller must free this array by
                            calling UF_free.
                            */
);

/*******************************************************************************
 *    This routine checks deviations between common edges (edges with deviations
 *    less than the Common Edge Tolerance) of the input faces.
 *
 * Environment  : Internal and External
 * See Also:
 * History: Originally released in v16.0
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_devchk_adjacent_edges(
    int num_faces, /* <I>  Number of input faces for deviation checking */
    tag_t  *faces, /* <I,len:num_faces>
                          Array of face tags to be checked. */
    double *tolerances, /* <I> [0] - Common Edge Tolerance: Edges with maximum
                                     distance greater than this value are
                                     non-common edges
                               [1] - Chordal Deviation: Used for sampling the
                                     edges if num_chk_points is zero.
                        */
    int num_chk_points, /* <I> if non-zero, edges are sampled at equally
                               spaced parameter values. if zero, Chordal
                               Deviation is used for sampling.
                        */
    int *num_devs,     /* <O> Number of deviations returned.*/
    UF_MODL_devchk_ee_info_t **devs /* <OF> deviations information corresponding
                                           to each sample point.  The caller is
                                           responsible for calling
                                           UF_free to free this array.
                                   */
);

/***************************************************************************
   Prototypes for Inquiring Modeling Objects
  ***************************************************************************/

/*******************************************************************************
Returns the fail option that is set for update failures. You use this
routine to get the current fail option in case an update failure occurs.
This allows the user to remember the previous value before setting
the option to a new value via UF_MODL_set_update_fail_option.

Environment: Internal  and  External
See Also: 
History:Original release was in V14.0.
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_update_fail_option(
UF_MODL_update_option_t *current_option  /* <O>
                                        Returns the fail option currently set
                                        for update failures.
                                        */
);

/*******************************************************************************
Gets the update error message associated with a feature.

Environment: Internal  and  External
See Also:
History: This function was originally released in V16.0.
******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_update_error_message(
    tag_t     feature_id,     /* <I>
                              Feature to be checked.
                              */
    char      **error_message /* <OF>
                              Update error message for this feature.  A NULL is
                              returned if the feature updated successfully.
                              This must be freed by calling UF_free.
                              */
);

/*******************************************************************************
Query the number of features which are out of date.

Environment: Internal  and  External
See Also:
History: This function was originally released in V16.0.
******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_out_of_date_features(
    int       *num_feature, /* <O>
                            Number of out of date features.
                            */
    tag_t     **features   /* <OF,len:num_feature>
                           Array of features which are out of date.  This array
                           must be freed by calling UF_free.
                           */
);

/*****************************************************************************
Return the feature time stamp.  The time stamp is a number which represents the
order in which the model was built.

Environment:Internal and External
See Also:
History: Originally released in V16.0
******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_time_stamp_of_feature(
tag_t    feature,      /* <I> Feature to check */
int      *time_stamp   /* <O> Time stamp of this feature. */
);

/******************************************************************************
Gets the feature object identifier for a given object. This function can
handle input datum axis, datum plane, sketch, and derived curve
objects i.e., objects including, but not limited to, the following types:
 UF_datum_axis_type
 UF_datum_plane_type
 UF_sketch_type
 UF_line_type
 UF_circle_type
 UF_conic_type
 UF_spline_type
 UF_point_type (if the point passed in is related to a DATUM_CSYS or Point Feature
                then the tag of the related feature is returned)

These are objects which belong to one feature.  This function does not support
solid edges and faces because a single face or edge can belong to multiple
features.

Environment: Internal  and  External
See Also: UF_MODL_ask_edge_feats
          UF_MODL_ask_face_feats

History:
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_object_feat(
tag_t  object_tag ,/* <I>
                   Object identifier.
                   */
tag_t * feature_tag  /* <O>
                     Feature object identifier.  NULL_TAG will be returned if no feature is found.
                     */
);

/*******************************************************************************
Get the object identifiers from a feature.

This function will return the display object identifiers of the following
features:

   DATUM_PLANE - returns object identifiers of type UF_datum_plane_type
   DATUM_AXIS  - returns object identifiers of type UF_datum_axis_type
   SKETCH      - returns object identifiers of type UF_sketch_type
   CURVE feature (like projection curve, extract.. ) returns object
                 identifiers of the curves.

Environment:Internal and External

See Also:
History: Originally released in V16.0
*******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_feat_object(

   tag_t    feature,   /* <I>  Feature tag            */
   int      *n_eids,   /* <O>  Number of objects      */
   tag_t    **eids     /* <OF,len:n_eids> objects array.  Free this by calling UF_free. */
   );

/****************************************************************************
Returns a list of all the suppressed features in the part.

Environment: Internal  and  External
See Also:
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_suppress_list(
uf_list_p_t  * feature_list  /* <OF,free:UF_MODL_delete_list>
                             List of all the suppressed features in the part.
                             This list must be freed by calling
                             UF_MODL_delete_list.
                             */
);

/****************************************************************************
Returns whether a feature is suppressed or not.

Environment: Internal  and  External
See Also:
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_suppress_feature(
tag_t feature ,/* <I>
               Feature to check.
               */
int  * suppress  /* <O>
                 If TRUE - feature is suppressed.
                 FALSE - feature is not suppressed.
                 */
);

/****************************************************************************
The input to UF_MODL_ask_feat_body is a feature that can be
obtained from using the UF_MODL_ask_*_feats routines.   The
output is a solid body (type 70, subtype 0) that can be used in the
UF_MODL_ask_body_* routines.

Environment: Internal  and  External
See Also:
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_feat_body(
tag_t feature_obj_id ,/* <I>
                      Feature object identifier.
                      */
tag_t *body_obj_id  /* <O>
                    Body object identifier which the feature belongs to.
                    */
);

/******************************************************************************
Is feature a body feature?  That is does the feature create a body or is
it applied to a body.

Environment:Internal and External
See Also:
History:
*******************************************************************************/
extern UFUNEXPORT int UF_MODL_is_body_feature
(
    tag_t    feature,        /* <I> feature to check */
    logical *is_body_feature /* <O> TRUE if a body feature, else FALSE */

);

/****************************************************************************
The input to UF_MODL_ask_feat_edges is a feature that can be
obtained from using the UF_MODL_ask_*_feats routines.  The
output is a list of solid edges associated to that feature.

Environment: Internal  and  External
See Also:
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_feat_edges(
tag_t feature_obj_id ,/* <I>
                      Feature object identifier to perform the inquiry
                      function upon.
                      */
uf_list_p_t * object_list  /* <OF,free:UF_MODL_delete_list>
                           Address of pointer to List of edges on the given
                           feature. Use UF_MODL_delete_list to free space
                           allocated for this linked list.
                           */
);

/****************************************************************************
The input to UF_MODL_ask_feat_faces is a feature that can be
obtained from using the UF_MODL_ask_*_feats routines.  The
output is a list of solid faces associated to that feature.

Environment: Internal  and  External
See Also:
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_feat_faces(
tag_t feature_obj_id ,/* <I>
                      Feature object identifier to inquire upon.
                      */
uf_list_p_t * object_list  /* <OF,free:UF_MODL_delete_list>
                           Address of pointer to list of faces on the given
                           feature. Use UF_MODL_delete_list to free space
                           allocated for this linked list.
                           */
);

/******************************************************************************
Returns a list of all of the nested features of the given feature.

Environment: Internal  and  External
See Also:
History:
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_nested_frecs(
    tag_t feature,              /* <I>
                                   feature being inquired
                                */
    uf_list_p_t *feature_list   /* <OF,free:UF_MODL_delete_list>
                                list of nested features.  This must be
                                freed by calling UF_MODL_delete_list.
                                */
);

/******************************************************************************
Inquires about the target face, tool face, horizontal/ vertical reference
of a feature.

Environment: Internal  and  External
See Also: UF_MODL_reattach_target_face
History:
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_link_faces(
tag_t feature_eid ,/* <I>
                   the feature being inquired
                   */
tag_t * target_face_eid ,/* <O>
                         the target placement face
                         */
tag_t * tool_face_eid ,/* <O>
                       the tool placement face
                       */
tag_t * dir_ref ,/* <O>
                 the directional reference
                 */
logical * ref_is_horizontal  /* <O>
                             TRUE = horizontal reference
                             FALSE = vertical reference
                             */
);

/******************************************************************************
Gets the first and second thru/trim faces of a feature.

Environment: Internal  and  External
See Also: UF_MODL_reattach_target_face
History:
 *****************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_thru_faces(
tag_t feature_eid ,/* <I>
                   the feature being inquired
                   */
tag_t * face1 ,/* <O>
               the first thru/trim face
               */
tag_t * face2  /* <O>
               the second thru/trim face
               */
);

/****************************************************************************
Gets the type of the input feature.

Environment: Internal  and  External
See Also: UF_MODL_ask_feat_name
          feature_name_test.c
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_feat_type(
tag_t feature_obj_id ,/* <I>
                      Feature to inquire upon.
                      */
char ** feature_type  /* <OF>
                      String containing feature type. Use UF_free to
                      deallocate memory when done.
                      */
);

/****************************************************************************
Returns a character string containing the feature type and time stamp
of the feature passed into the function. The time stamp refers to the
order of creation. For example, if you created two blocks they would
be time stamped as BLOCK(0) and BLOCK(1).

Environment: Internal  and  External
See Also: 
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_feat_name(
tag_t feature_tag ,/* <I>
                   Object identifier of feature to inquire.
                   */
char ** feature_name  /* <OF>
                      String containing feature name (feature type and
                      time stamp). Use UF_free to deallocate memory
                      when done.
                      */
);

/****************************************************************************
Returns a character string containing the proper legacy name of the feature
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_proper_legacy_feat_name(
tag_t feature_tag ,/* <I>
                   Object identifier of feature to inquire.
                   */
char ** feature_name  /* <OF>
                      String containing feature name (feature type and
                      time stamp). Use UF_free to deallocate memory
                      when done.
                      */
);

/****************************************************************************
Get the relatives (parents and children) of a feature. This function
works on all features, including datums, sketches, and projected
curves.

Environment: Internal  and  External
See Also: 
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_feat_relatives(
tag_t feature_tag ,/* <I>
                   feature on which we are inquiring.
                   */
int * num_parents ,/* <O>
                   number of parents tags in parent array.
                   */
tag_t ** parent_array ,/* <OF,len:num_parents>
                       Pointer to an array holding the feature tags of the
                       parents.  This must be freed by calling UF_free.
                       */
int * num_children ,/* <O>
                    number of children tags in the children array.
                    */
tag_t ** children_array  /* <OF,len:num_children>
                         Pointer to an array holding the feature tags of the
                         children.  This must be freed by calling UF_free.
                         */
);

/********************************************************************
Gets the sign of a feature. You input the object identifier of the
feature and this routine retrieves the "sign". The "sign" is a
numerical value representing the type of Boolean operation performed.

Environment: Internal  and  External

See Also:

History:
********************************************************************/
extern UFUNEXPORT int UF_MODL_ask_feature_sign(
tag_t feature_obj_id ,/* <I>
                      Feature object identifier
                      */
UF_FEATURE_SIGN * sign  /* <O>
                         Sign of resultant feature.
                         The sign of the feature is:
                         UF_NULLSIGN = 0, create new target solid
                         UF_POSITIVE = 1,  add to target solid
                         UF_NEGATIVE = 2, subtract from target solid
                         UF_UNSIGNED = 3, intersect with target solid
                         UF_DEFORM_POSITIVE = 9, deform on the positive side
                                                 of target
                         UF_DEFORM_NEGATIVE = 10 deform on the negative side
                                                 of target
                         */
);

/********************************************************************
Returns information about the boolean status of a solid feature.

Environment: Internal  and  External

See Also:

History:
********************************************************************/
extern UFUNEXPORT int UF_MODL_ask_feature_boolean(
tag_t  feature_obj_id ,/* <I>
                       Feature object identifier to inquire.
                       */
UF_FEATURE_SIGN * boolean_status  /* <O>
                                  UF_NO_BOOLEAN - feature has not been
                                                  booleaned.
                                  UF_TOP_TARGET - feature is not booleaned into
                                                  any other features but has
                                                  at least one tool as a child.
                                  UF_UNITE - feature has been united to a
                                             target solid.
                                  UF_SUBTRACT - feature has been subtracted
                                                from a target solid.
                                  UF_INTERSECT - feature has been intersected
                                                 with a target solid.
                                  UF_DEFORM_POSITIVE - feature used to deform
                                                       the positive side of the
                                                       target sheet.
                                  UF_DEFORM_NEGATIVE - feature used to deform
                                                       the negative side of the
                                                       target sheet.
                                  */
);


/********************************************************************
Gets feature direction. The direction of the feature is dependent on
the feature type. Some features have either one or two directions and
some have none.

Environment: Internal  and  External
See Also:


History:
********************************************************************/
extern UFUNEXPORT int UF_MODL_ask_feat_direction(
tag_t feature_obj_id ,/* <I>
                      A feature object identifier
                      */
double  dir_x[3] ,/* <O>
                  X direction
                  */
double dir_y[3]  /* <O>
                 Y direction
                 */
);
/********************************************************************
Inquires a single feature object and retrieves the location
of the feature in the absolute coordinate system. The location of
the feature is dependent on the feature type.

AXIS_ANGLE_DATUM_PLANE - NO LOCATION
AXIS_NORMAL_DATUM_PLANE - NO LOCATION
BALL_GROOVE - Location at the center of the groove.
BALL_SLOT - Location at the center slot attach face.
BLEND - NO LOCATION.
BLOCK - Location at the block corner.
BOSS - Location at the center of the boss attach face.
CBORE_HOLE - Location at the center of the hole attach face.
CHAMFER - NO LOCATION.
CIRCULAR_ISET - Location at the center of the iset rotation point.
CONE - Location at the center of the lower face.
CSUNK_HOLE - Location at the center of the hole attach face.
CYL_DATUM_PLANE - NO LOCATION
CYL_NORMAL_DATUM_PLANE - NO LOCATION
CYL_PARALLEL_DATUM_PLANE - NO LOCATION
CYLINDER - Location at the center of the lower face.
CYL_POCKET - Location at the center of the pocket attach face.
DATUM_AXIS - NO LOCATION
DATUM_PLANE - NO LOCATION
DOVE_TAIL_SLOT - Location at the center slot attach face.
HOLLOW - NO LOCATION.
INSTANCE - x, y location
LINEAR_ISET - Location of the first instance.
META - NO LOCATION
OFFSET - NO LOCATION.
PRISM - Location at the prism center.
PROJ_DCURVE - NO LOCATION
RECT_GROOVE - Location at the center of the groove.
RECT_PAD - Location at the corner of the pad attach face.
RECT_POCKET - Location at the center of the pocket attach face.
RECT_SLOT - Location at the center slot attach face.
SKETCH - NO LOCATION
SIMPLE HOLE - Location at the center of the hole attach face.
SPHERE - Location at the center of the sphere.
SWP104 - NO LOCATION.
TANGENT_PARALLEL_DATUM_PLANE - NO LOCATION
TRANSFORM_ISET - NO LOCATION
TAPER - The location and the direction of the taper specifies a
plane, and the intersection between this plane and the taper face
specify the axis of rotation.
TORUS - Location at the center of the lower face.
T_SLOT - Location at the center slot attach face.
UDF -  Location of the first feature in the UDF.
U_GROOVE - Location at the center of the groove.
U_SLOT - Location at the center slot attach face.

Environment: Internal  and  External
See Also:
History:
********************************************************************/
extern UFUNEXPORT int UF_MODL_ask_feat_location(
tag_t  feature_obj_id ,/* <I>
                       A feature object identifier
                       */
double location[3]  /* <O>
                    Location of feature in absolute coordinate system.
                    */
);

/****************************************************************************
Returns the first object on the input body of the requested type with the
given name.

Environment: Internal  and  External
See Also:
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_named_body_object(
      tag_t  *body_tag,    /* <I>
                           body identifier
                           */
      int  *object_type,   /* <I>
                           UF_solid_face_subtype or UF_solid_edge_subtype
                           */
      char  *object_name,  /* <I>
                           case sensitive object name
                           */
      tag_t  *object       /* <O>
                           returned object identifier
                           */
);

/******************************************************************************
Determines if a body is a solid or sheet.

Environment: Internal  and  External
See Also:
History:
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_body_type(
tag_t body_id ,/* <I>
               Object identifier for the body
               */
int * body_type  /* <O>
                 Body type:
                 UF_MODL_SOLID_BODY
                 UF_MODL_SHEET_BODY
                 0 : None of the above
                 */
);
/****************************************************************************
Returns the global solid density in the desired unit. The density units can be
any one of the following:

     UF_MODL_pounds_inches
     UF_MODL_pounds_feet
     UF_MODL_grams_centimeters
     UF_MODL_kilograms_meters

Environment: Internal  and  External
See Also: 
          UF_MODL_set_default_density
History: Originally released in V16.0
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_default_density
(
    UF_MODL_density_units_t units,    /* <I>
                                      units of 'density'
                                      */
    double                  *density  /* <O>
                                      default density
                                      */
);

/******************************************************************************
Returns the density of a body (solid or sheet body).

Environment:Internal and External
See Also:
History: Originally released in V15.0.
*******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_body_density
(
    const tag_t              body,   /* <I>
                                     solid/sheet body
                                     */
    UF_MODL_density_units_t  units,  /* <I>
                                     units of 'density'
                                     */
    double                  *density /* <O>
                                     density of body
                                     */
);

/******************************************************************************
Returns the current setting for the sheet/solid body type modeling
preference. This preference is used when creating bodies through
curves to allow you to control the type of body created. The body type
option is used in the Through Curve Mesh, Through Curves, Extruded
Body, Body of Revolution, Swept, Section Surface and Ruled Free
Form Feature creation options.

Environment: Internal  and  External
See Also: UF_MODL_set_body_type_pref
History:
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_body_type_pref(
int * body_type  /* <O>
                 Current setting of the body type preference
                 UF_MODL_SOLID_BODY
                 UF_MODL_SHEET_BODY
                 */
);
/****************************************************************************
Calling UF_MODL_ask_body_edges, with a solid body (type 70,
subtype 0) as input, returns a list of edges associated to that body.
The handling of this list can be done by using the UF_MODL_*_list*
routines.  The appropriate input to this routine can be obtained by
calling UF_MODL_ask_object() and inputting the above type, and
subtype.

If body is an occurrence, then the return values are relative to the
occurrence, and not the prototype.

Environment: Internal  and  External
See Also:
History: Modified in V15.0 to work relative to the occurrence.
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_body_edges(
tag_t body ,/* <I>
            Body object identifier
            */
uf_list_p_t * edge_list  /* <OF,free:UF_MODL_delete_list>
                         Address of a Pointer to a list of Edge object
                         identifiers. Use UF_MODL_delete_list to free
                         space allocated for this linked list.
                         */
);

/****************************************************************************
Calling UF_MODL_ask_body_faces, with a solid body (type 70,
subtype 0) as input, returns a list of faces associated to that body.  The
handling of this list can be done by using the UF_MODL_*_list*
routines.  The appropriate input to this routine can be obtained by
calling UF_MODL_ask_object() and inputting the above type, and
subtype.

If body is an occurrence, then the return values are relative to the
occurrence, and not the prototype.

Environment: Internal  and  External
See Also:
History: Modified in V15.0 to work relative to the occurrence.
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_body_faces(
tag_t  body ,/* <I>
             Body object identifier
             */
uf_list_p_t * face_list  /* <OF,free:UF_MODL_delete_list>
                         Address of a Pointer to a list of Face object
                         identifiers. Null pointer is returned if an error
                         occurs (`error' > 0). Use UF_MODL_delete_list to
                         free space allocated for this linked list.
                         */
);

/****************************************************************************
Calling UF_MODL_ask_body_feats, with a solid body (type 70,
subtype 0) as input, returns a list of features associated to that body.
The handling of this list can be done by using the UF_MODL_*_list*
routines.  The appropriate input to this routine can be obtained by
calling UF_MODL_ask_object() and inputting the above type, and subtype.

The features are returned in the current creation order.

No longer returns information about sketches or datum planes.  Does not
include features of type symbolic thread on the list since the symbolic
thread feature is an annotation feature and does not have a body that
contributes to the solid body. Use UF_MODL_ask_feat_relatives to obtain
the symbolic thread feature.

Environment: Internal  and  External
See Also:
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_body_feats(
tag_t body ,/* <I>
            Body object identifier
            */
uf_list_p_t * feature_tag_list  /* <OF,free:UF_MODL_delete_list>
                                Address of a pointer to a list of Feature tags.
                                Null pointer is returned if an error occurs
                                (`error' > 0). Use UF_MODL_delete_list to free
                                space allocated for this linked list.
                                */
);

/******************************************************************************
Returns a tabulation of all features found organized by feature type
showing the number of each type found and a total number of
features in the body selected.

Environment: Internal  and  External
See Also: 
History:
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_body_features(
tag_t body_id ,/* <I>
               Body object id
               */
int* features_count ,/* <O>
                     Number of features
                     */
UF_MODL_features_p_t** features_node  /* <OF,len:features_count> features_count
                                      Features node
                                      */
);

/****************************************************************************
Finds the extreme point of a face or an edge. Three direction vectors
are used to find the point. If there is a unique extreme point in the
first direction, then the other directions are ignored. Otherwise,
second and third directions are used successively to reduce the
number of extreme points to one.

The object identifier of the subobject containing the extreme point is
also returned.

For faces, the subobject is an edge containing the extreme point. If the
point does not lie on an edge, then a null object identifier (zero) is
returned for the subobject. For edges, the object identifier of the
subobject is always null (zero).

If object is an occurrence, then the return values are relative to the
occurrence, and not the prototype.

The vectors you input should be based on the ACS (Absolute Coordinate System)
of the Display part, so if your work part is a component and the Display
part is the assembly, you would want to enter in vectors for the Assembly's
ACS.

The coordinates returned will also be based on the Absolute Coordinate System
of the Display Part.

Environment: Internal  and  External
See Also:
History: Modified in V15.0 to work relative to the occurrence.
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_extreme(
tag_t object ,/* <I>
              Object identifier of object (valid objects are faces
              and edges)
              */
double dir1[3] ,/* <I>
                First direction vector
                */
double dir2[3] ,/* <I>
                Second direction vector
                */
double dir3[3] ,/* <I>
                Third direction vector
                */
tag_t * subent ,/* <O>
                Object identifier of subobject containing the
                extreme point (Null object identifier (zero) is
                returned, if the point does not lie on a subobject).
                */
double point[3]  /* <O>
                 Coordinates of the extreme point.
                 */
);

/********************************************************************
Queries the data associated with a face. The data ouput depends on the type
of face receiving the query. The data can include the object type of
the face, center point, axis direction, etc.

Note that the normal vector and surface derivative vectors may be obtained
for all types of faces using UF_MODL_ask_face_props.

Environment: Internal  and  External

See Also:  UF_MODL_ask_face_props

History:
********************************************************************/
extern UFUNEXPORT int UF_MODL_ask_face_data(
tag_t face ,/* <I>
            Face obj_id
            */
int * type ,/* <O>
            Face type is NX surface type code
            16 = cylinder
            17 = cone
            18 = sphere
            19 = revolved (toroidal)
            20 = extruded
            22 = bounded plane
            23 = fillet (blend)
            43 = b-surface
            65 = offset surface
            66 = foreign surface
            67 = Convergent surface
            */
double point[3] ,/* <O>
                 Point information is returned according to the value
                 of type as follows.
                 Plane   =       Position in plane
                 Cylinder=       Position on axis
                 Cone    =       Position on axis
                 Sphere  =       Center position
                 Torus   =       Center position
                 Revolved =      Position on axis
                 */
double dir[3] ,/* <O>
               Direction information is returned according to the
               value of type as follows.
               Plane   =       Normal direction
               Cylinder=       Axis direction
               Cone    =       Axis direction
               Torus   =       Axis direction
               Revolved =      Axis direction
               */
double box[6] ,/* <O>
               Face boundary. The coordinates of the opposite
               corners of a rectangular box with sides parallel to X,
               Y, and Z axes (Absolute Coordinate System) are
               returned. The box contains the specified face and is
               usually close to the minimum possible size, but this
               is not guaranteed.
               box[0] = Xmin
               box[1] = Ymin
               box[2] = Zmin
               box[3] = Xmax
               box[4] = Ymax
               box[5] = Zmax
               */
double * radius ,/* <O>
                 Face major radius:
                 For a cone, the radius is taken at the point[3]
                 position on the axis.
                 For a torus, the radius is taken at the major axis.
                 */
double * rad_data ,/* <O>
                   Face minor radius: only a torus or cone has rad_data as
                   a minor radius.
                   For a cone, rad_data is the half angle in radians.
                   For a torus, rad_data is taken at the minor axis.
                   */
int * norm_dir  /* <O>
                Face normal direction:  +1 if the face normal is in the
                same direction as the surface normal (cross product of
                the U- and V-derivative vectors), -1 if reversed.
                */
);

/****************************************************************************
Returns the parameter and point on the surface of a face
given a reference point.

Note that the returned point will be on the underlying surface
but may not be on the portion which is bounded by the edges
of the face.

Note that in some cases, there is a potential risk that the returned point might
be adjusted incorrectly where the underlying surface has an extended UV range.
Please use UF_MODL_ask_face_parm_2 instead.

Environment: Internal  and  External
See Also:
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_face_parm(
tag_t face_id ,/* <I>
               Face identifier.
               */
double ref_pnt[3] ,/* <I>
                  Reference point in absolute space (ref_pnt[3]).
                  */
double parm[2] ,/* <O>
               Parameter (u,v) on face (parm[2]).
               */
double face_pnt[3]  /* <O>
                   Point on the surface of the given face (face_pnt[3])
                   */
);

/****************************************************************************
Returns the parameter and point on the surface of a face
given a reference point.

Note that the returned point will be on the underlying surface
but may not be on the portion which is bounded by the edges
of the face.

Environment: Internal  and  External
See Also:
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_face_parm_2(
tag_t face_id ,/* <I>
               Face identifier.
               */
double ref_pnt[3] ,/* <I>
                  Reference point in absolute space (ref_pnt[3]).
                  */
double parm[2] ,/* <O>
               Parameter (u,v) on face (parm[2]).
               */
double face_pnt[3]  /* <O>
                   Point on the surface of the given face (face_pnt[3])
                   */
);

/****************************************************************************
Returns the point, first derivative in U, first derivative in V, second
derivative in U, second derivative in V, unit face normal, and the principal
radii of curvature on a face at a given parameter. Face parameters are
not normalized and the input parameter (param[2]) must be between the
Umin, Umax, Vmin, and Vmax of the face.

The unit face normal may be the same as the surface normal (cross product
of the U- and V-derivative vectors) or may be reversed.  For a solid body
face, the face normal may have been reversed so as to point out of the solid
body(for a valid solid body, all the face normals will point out of the body).
For a sheet body face, the face normal may be reversed if a REVERSE_NORMAL
feature has been applied (see UF_MODL_create_reverse_normal).

The face normal direction can be obtained from UF_MODL_ask_face_data.

Environment: Internal  and  External

See Also:  UF_MODL_ask_face_data
           UF_MODL_create_reverse_normal

History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_face_props(
tag_t face_id ,/* <I>
               Face identifier.
               */
double param[2] ,/* <I>
                Parameter (u,v) on face (param[2]).
                */
double point[3] ,/* <O>
                Point at parameter (point[3]).
                */
double u1[3] ,/* <O>
             First derivative in U (u1[3]).
             */
double v1[3] ,/* <O>
             First derivative in V (v1[3]).
             */
double u2[3] ,/* <O>
             Second derivative in U (u2[3]).
             */
double v2[3] ,/* <O>
             Second derivative in V (v2[3]).
             */
double unit_norm[3] ,/* <O>
                    Unit face normal (unit_norm[3]).
                    */
double radii[2]  /* <O>
                Principal radii of curvature (radii[2]).
                */
);

/******************************************************************************
Returns the periodicity of the underlying surface of a face (opened or closed).

Environment: Internal  and  External
See Also:

History:
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_face_periodicity(
tag_t face_id ,/* <I>
               Object identifier for the face
               */
int * U_status ,/* <O>
                U status:
                UF_MODL_NON_PERIODIC - not periodic in the U direction
                UF_MODL_PERIODIC - periodic in U direction
                UF_MODL_BOTH_X_PERIODIC - cross-periodic (poles at both ends)
                UF_MODL_MIN_X_PERIODIC - cross-periodic (poles at U min)
                UF_MODL_MAX_X_PERIODIC - cross-periodic (poles at U max)
                */
double * U_period ,/* <O>
                   Period in U direction
                   */
int * V_status ,/* <O>
                V status-
                UF_MODL_NON_PERIODIC - not periodic in the V direction
                UF_MODL_PERIODIC - periodic in V direction
                UF_MODL_BOTH_X_PERIODIC - cross-periodic (poles at both ends)
                UF_MODL_MIN_X_PERIODIC - cross-periodic (poles at V min)
                UF_MODL_MAX_X_PERIODIC - cross-periodic (poles at V max)
                */
double * V_period  /* <O>
                   Period in V direction
                   */
);

/***********************************************************************
Computes the u,v parameter space min, max  of a face.

Environment: Internal  and  External

See Also:

History: Original release was in V14.0.
*********************************************************************/
extern UFUNEXPORT int UF_MODL_ask_face_uv_minmax (
tag_t face_tag ,/* <I>
                Face tag
                */
double uv_min_max[4]  /* <O>
                      [0] - umin
                      [1] - umax
                      [2] - vmin
                      [3] - vmax
                      */
);

/******************************************************************************
Calculates maximum curvature data for a curve

Environment: Internal  and  External
See Also:
History:
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_max_curvature(
tag_t eid ,/* <I>
           Entity id (currently curve only)
           */
double range[4] ,/* <I>
              Entity's percent parameter range to be searched.
                For curve: range[0] = start percent of curve range,
                           range[1] = end percent of curve range
                    (so to find the maximum curvature over the whole range
                     of the curve, use range[0]=0.0, range[1]=100.0)
                For surface: range[0-1]= start/end percentages for u-range
                             range[2-3]= start/end percentages for v-range
                */
int curva_type ,/* <I>
                Curvature type of the surface. Not used for curve
                */
double max_curva[5] ,/* <O>
                   Data for the point where curvature is a maximum (curve only)
                     max_curva[0] = parameter value (not percentage)
                                     between curve min and max parameters
                     max_curva[1-3] = point coordinates
                     max_curva[4]   = curvature value
                   */
int * status  /* <O>
              1 if the curve has constant curvature -
                  in this case, only the curvature value is returned
              0 a best (not necessarily unique) maximum
                  curvature point is returned
              */
);

/****************************************************************************
Returns the u and v grid counts of a face or a body. It returns -1 as the
count when the faces of the selected body differ in the grid count.

Environment: Internal  and  External
See Also: 
          UF_MODL_edit_face_grid_count
History: Originally released in V16.0
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_face_grid_count
(
   tag_t     object,            /* <I>
                                tag of face or body
                                */
   int       *u_count,          /* <O>
                                u grid counts
                                */
   int       *v_count           /* <O>
                                v grid counts
                                */
);

/******************************************************************************
Gets the minimum radius of curvature on each side of the given face
where one exists, and its position and u-v parameters.  The position
is returned in the same units as the current part.

A minimum radius of curvature is deemed not to exist on one side of
the surface if it is nowhere concave on that side.  So the function can
return 0 (in the case of a plane), 1 (in the case of a cylinder, for
example) or 2 minima.

The magnitude of the radius has a positive sign if the surface is
concave with respect to its normal and a negative sign if the surface is
convex with respect to its normal.

If face is an occurrence, then the return values are relative to the
occurrence, and not the prototype.

Environment: Internal  and  External
See Also: 
History: Modified in V15.0 to work relative to the occurrence.
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_face_min_radii(
tag_t face ,/* <I>
            input face
            */
int * num_radii ,/* <O>
                 number of radii found
                 */
double  radii[2] ,/* <O>
                minimum radii of curvature
                */
double  positions[6] ,/* <O>
                    point locations of minimum radii.
                    */
double  params[4]  /* <O>
                 u-v parameters of each radii
                 */
);
/********************************************************************
Gets the type of a face.

Environment: Internal  and  External
See Also:

History:
********************************************************************/
extern UFUNEXPORT int UF_MODL_ask_face_type(

tag_t face ,/* <I>
            tag of the face
            */
int * type  /* <O>
            Face type is NX surface type code
            = UF_MODL_CYLINDRICAL_FACE
            = UF_MODL_CONICAL_FACE
            = UF_MODL_SPHERICAL_FACE
            = UF_MODL_TOROIDAL_FACE
            = UF_MODL_SWEPT_FACE
            = UF_MODL_PLANAR_FACE
            = UF_MODL_BLENDING_FACE
            = UF_MODL_PARAMETRIC_FACE
            = UF_MODL_OFFSET_FACE
            = UF_MODL_FOREIGN_FACE
            = UF_MODL_CONVERGENT_FACE
            */
);

/********************************************************************
Returns the type of toroidal surface.


Environment: Internal  and  External
See Also:

History:
********************************************************************/
extern UFUNEXPORT int UF_MODL_ask_face_torus_type(
tag_t face ,/* <I>
            tag of the face
            */
int * torus_type  /* <O>
                  Type of torus. Returns a defined constant for
                  the type of torus. For example UF_MODL_DOUGHNUT_TORUS.
                  */
);

/****************************************************************************
Get faces adjacent to a face. Adjacency is the connection along edges
and not at vertices. This function returns faces immediately adjacent
to a face.

If face is an occurrence, then the return values are relative to the
occurrence, and not the prototype.

Environment: Internal  and  External
See Also:
History: Modified in V15.0 to work relative to the occurrence.
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_adjac_faces(
tag_t face ,/* <I>
            Face object identifier
            */
uf_list_p_t * adjacent_faces  /* <OF,free:UF_MODL_delete_list>
                              Address of a pointer to a List of features. Use
                              UF_MODL_delete_list to free space allocated for
                              this linked list.
                              */
);

/******************************************************************************
Inquires the topology of a face.

The topology is determined from the peripheral edge loops of the face.  The
topology is related to, but does not describe the type of surface used to
create the face.  For example, a truncated cone has two closed loops and will
return UF_MODL_CYLINDRICAL_TOPOLOGY, not UF_MODL_CONICAL_TOPOLOGY.

Environment: Internal  and  External
See Also:
History:
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_face_topology(
tag_t face_id ,/* <I>
               Object identifier for the face
               */
int * topo_type  /* <O>
                 Topological type of a face:
                 UF_MODL_FLAT_TOPOLOGY = 1 peripheral loop
                 UF_MODL_CYLINDRICAL_TOPOLOGY = 2 peripheral loops, no pole
                 UF_MODL_CONICAL_TOPOLOGY = 2 peripheral loops, 1 pole
                 UF_MODL_SPHERICAL_TOPOLOGY = 2 peripheral loops, 2 poles
                 UF_MODL_TOROIDAL_TOPOLOGY = no peripheral loops
                 0 =     if error, or if input was a body with multiple faces
                 */
);

/****************************************************************************
The input to UF_MODL_ask_face_body is a single solid face.  What
is returned is a solid body (type 70, subtype 0), which can be later
used in the UF_MODL_ask_body_* routines.

Environment: Internal  and  External
See Also:
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_face_body(
tag_t face ,/* <I>
            Face object identifier
            */
tag_t *body_obj_id  /* <O>
                    Object identifier of Body.
                    */
);

/****************************************************************************
The input to UF_MODL_ask_face_edges is a single solid face.  What
is returned is a list of solid edges associated to that face.  The
handling of this list can be done by using the UF_MODL_*_list* routines.

If the face is an occurrence, then the return values are relative to the
occurrence, and not the prototype.

Environment: Internal  and  External
See Also:
History: Modified in V15.0 to work relative to the occurrence.
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_face_edges(
tag_t face ,/* <I>
            Face object identifier
            */
uf_list_p_t * edge_list  /* <OF,free:UF_MODL_delete_list>
                         Address of a pointer to a list of Edge object
                         identifiers. Use UF_MODL_delete_list to free
                         space allocated for this linked list.
                         */
);

/****************************************************************************
The input to UF_MODL_ask_face_feats is a single solid face.  What
is returned is a list of features to which the input face belongs (usually
a single feature).  The handling of this list can be done by using the
UF_MODL_*_list* routines.  The features within the list may only be
used within other UF_MODL_* routines that require a feature as
input.

Environment: Internal  and  External
See Also:
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_face_feats(
tag_t face_obj_id ,/* <I>
                   Face object identifier
                   */
uf_list_p_t * feature_list  /* <OF,free:UF_MODL_delete_list>
                            Address of a pointer to a List of features to which
                            the face belongs. The feature is the parent of the
                            face (features cannot belong to a face). Use
                            UF_MODL_delete_list to free space allocated for this
                            linked list.
                            */
);

/****************************************************************************
The input to UF_MODL_ask_face_loops is a single solid face.   What
is returned is a list of type 'loop_list.'  This is a pointer to a list of loop
structures. Each loop structure contains a list of edges that makeup a
particular loop. This structure is detailed within the uf_modl.h include
file.

If the face is an occurrence, then the return values are relative to the
occurrence, and not the prototype.

Environment: Internal  and  External
See Also:
History: Modified in V15.0 to work relative to the occurrence.
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_face_loops(
tag_t face ,/* <I>
            Object identifier of face containing loops
            */
uf_loop_p_t * loop_list  /* <OF,free:UF_MODL_delete_loop_list>
                         Address of a Pointer to a loop_list structure. Null
                         pointer is returned if face has no loops, or if an
                         error occurs (`error' > 0). Use
                         UF_MODL_delete_loop_list to free space allocated
                         for this linked list.
                         */
);

/******************************************************************************
Returns all of the split faces of the given face.  For occurrences input from
the face argument, the faces returned from the faces argument are on the
occurrence.

Environment: Internal  and  External
See Also:
History:
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_split_faces(
tag_t face ,/* <I>
            Object identifier of face
            */
int * nfaces ,/* <O>
              Number of split faces
              */
tag_t ** faces  /* <OF,len:nfaces>
                Array of tags of split faces. Use UF_free to deallocate memory.
                */
);

/******************************************************************************
Returns all of the merged faces of the given face.  For occurrences input from
the face argument, the faces returned from the faces argument are on the
occurrence.

Environment: Internal  and  External
See Also: UF_MODL_ask_split_faces
History: Introduced in V1604, V1701, V18
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_merged_faces(
tag_t face ,/* <I>
            Object identifier of face
            */
int * nfaces ,/* <O>
              Number of merged faces
              */
tag_t ** faces  /* <OF,len:nfaces>
                Array of tags of merged faces. Use UF_free to deallocate memory.
                */
);

/******************************************************************************
When a face is merged with another face, this creates a new face that has two
different face labels. The program returns the alive face that the original
was merged into.

This function does not work when edges have been merged via a Sew operation.

Environment: Internal  and  External
See Also:
History:
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_alive_face
(
tag_t face,       /* <I>
                     Object identifier of a new face
                  */
tag_t *alive_face /* <O>
                     Object identifier of an alive face
                  */
);


/****************************************************************************
The input to UF_MODL_ask_shared_edges are the two faces,
between which the user wants to find the common edges. Those edges
are returned in a list that can be manipulated by the
UF_MODL_*_list* routines.

If face1 or face2 is an occurrence, then the return values are relative to the
occurrence, and not the prototype.

Environment: Internal  and  External
See Also:
History: Modified in V15.0 to work relative to the occurrence.
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_shared_edges(
tag_t face1 ,/* <I>
             Object identifier of first face
             */
tag_t face2 ,/* <I>
             Object identifier of second face
             */
uf_list_p_t * shared_edges  /* <OF,free:UF_MODL_delete_list>
                            Pointer to a list of edge object identifiers. Null
                            pointer is returned if faces do not share edges,
                            or if an error occurs (`error' > 0).  Use
                            UF_MODL_delete_list to free space allocated for this
                            linked list.
                            */
);

/******************************************************************************
Returns the edge type.  Inquire routines only return geometric data for linear,
circular, elliptical and spline edges.

Environment: Internal  and  External
See Also: uf_modl_types.h for edge_type information.
History:
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_edge_type(
tag_t edge_id ,/* <I>
               Object identifier for the edge
               */
int * edge_type  /* <O>
                 Edge type:
                 UF_MODL_LINEAR_EDGE
                 UF_MODL_CIRCULAR_EDGE
                 UF_MODL_ELLIPTICAL_EDGE
                 UF_MODL_INTERSECTION_EDGE
                 UF_MODL_SPLINE_EDGE
                 UF_MODL_SP_CURVE_EDGE
                 UF_MODL_FOREIGN_EDGE
                 UF_MODL_CONST_PARAMETER_EDGE
                 UF_MODL_TRIMMED_CURVE_EDGE
                 UF_MODL_CONVERGENT_EDGE
                 */
);

/****************************************************************************
Get two lists of edges connected at each endpoint of a given edge.
The first list belongs to the endpoint closer to a given 3D point.
An edge may have zero, one, or two vertices. Consequently, null
pointers may be returned for both or either of the two lists. If one of
the lists is null, then the first list always returns the list of edges and
the second list is null.

If edge is an occurrence, then the return values are relative to the
occurrence, and not the prototype.

Environment: Internal  and  External
See Also:
History: Modified in V15.0 to work relative to the occurrence.
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_cnnc_edges(
tag_t edge ,/* <I>
            Edge object identifier
            */
double reference[3] ,/* <I>
                     3D point to determine the first endpoint of`edge'
                     */
uf_list_p_t * edges1 ,/* <OF,free:UF_MODL_delete_list>
                      Address of list of object identifiers of edges
                      connected at the endpoint closer to `reference'. Use
                      UF_MODL_delete_list to free space allocated for this
                      linked list.
                      */
uf_list_p_t * edges2  /* <OF,free:UF_MODL_delete_list>
                      Address of list of object identifiers of edges
                      connected at the endpoint further from `reference'.
                      Use UF_MODL_delete_list to free space allocated
                      for this linked list.
                      */
);

/******************************************************************************
Returns all of the split edges of the given edge.  For occurrences input from
the edge argument, the edges returned from the edges argument are on the
occurrence.

Environment: Internal  and  External
See Also:
History:
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_split_edges(
tag_t edge ,/* <I>
            Object identifier of edge
            */
int * nedges ,/* <O>
              Number of split edges
              */
tag_t ** edges  /* <OF,len:nedges>
                Array of object identifiers of split edges. Use
                UF_free to deallocate memory.
                */
);

/******************************************************************************
When an edge is merged with another edge, this creates a new edge that has 2
different edge labels, the program returns the original edge.

Environment: Internal  and  External
See Also:
History:
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_alive_edge
(
tag_t edge,       /* <I>
                     Object identifier of a new edge
                  */
tag_t *alive_edge /* <O>
                     Object identifier of an alive edge
                  */
);


/****************************************************************************
When the user calls UF_MODL_ask_edge_body, and inputs a solid
edge, the program returns the solid body (type 70, subtype 0) it is
associated to.  This identifier can be used in the other
UF_MODL_ask_body_* routines.

Environment: Internal  and  External
See Also:
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_edge_body(
tag_t edge ,/* <I>
            Edge object identifier
            */
tag_t * body_obj_id  /* <O>
                     Object identifier of body.
                     */
);

/****************************************************************************
When the user calls UF_MODL_ask_edge_faces, and inputs a solid
edge, the program returns a list of solid faces associated to that edge.
The handling of this list can be done by using the UF_MODL_*_list*
routines.

If the edge is an occurrence, then the return values are relative to the
occurrence, and not the prototype.

Environment: Internal  and  External
See Also:
History: Modified in V15.0 to work relative to the occurrence.
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_edge_faces(
tag_t edge ,/* <I>
            Edge object identifier
            */
uf_list_p_t * face_list  /* <OF,free:UF_MODL_delete_list>
                         Address of Pointer to a list of Face object
                         identifiers. Null pointer is returned if an error
                         occurs (`error' > 0). Use UF_MODL_delete_list to
                         free space allocated for this linked list.
                         */
);

/****************************************************************************
Given a solid edge as input, returns the vertices (endpoints) of the
edge. An edge may have zero, one, or two vertices, based on the edge
given. For example, a circle is an edge with a zero vertex and a line is
an edge with two vertices. It is also possible to create a circular edge
with one vertex. An example is extruding a triangle into a cylinder and
then performing a union on the results to obtain a body as shown.



When the input edge is an occurrence, the coordinates for point1 and
point2 are relative to the occurrence.

Environment: Internal  and  External
See Also: 
History: Modified in V15.0 to work relative to the occurrence.
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_edge_verts(
tag_t edge ,/* <I>
            Object identifier of edge containing vertices
            */
double point1[3] ,/* <O>
                  first endpoint of edge.
                  */
double point2[3] ,/* <O>
                  second endpoint of edge.
                  */
int *vertex_count  /* <O>
                   Number of endpoints returned. If only one
                   endpoint is returned, it is contained in `point1'.
                   */
);

/****************************************************************************
When the user calls UF_MODL_ask_edge_feats, and inputs a solid
edge, the program returns a list of features associated to that edge.
The handling of this list can be done by using the UF_MODL_*_list*
routines.  The features within the list may only be used within other
UF_MODL_* routines that require a feature as input.

Environment: Internal  and  External
See Also:
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_edge_feats(
tag_t edge_obj_id ,/* <I>
                   Object identifier of the edge.
                   */
uf_list_p_t * feature_list  /* <OF,free:UF_MODL_delete_list>
                            Address of a pointer to a List of features. Use
                            UF_MODL_delete_list to free space allocated for this
                            linked list.
                            */
);

/******************************************************************************
Gets the dimensionality of a geometric object.

Environment: Internal  and  External
See Also:
History:
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_obj_dimensionality(
tag_t object_id ,/* <I>
                 Object ID
                 */
int * dimensionality ,/* <O>
                      Dimensionality of the object:
                      -1 = object is not valid
                      UF_MODL_POINT
                      UF_MODL_LINEAR
                      UF_MODL_PLANAR
                      UF_MODL_THREE_DIMENSIONAL
                      */
double data[6]  /* <O>
               If *dimensionality = UF_MODL_POINT
               data[0 - 2] = coordinates of the point
               If *dimensionality = UF_MODL_LINEAR
               data[0 - 2] = coordinates of a point on the line
               data[3 - 5] = unit direction vector of the line
               If *dimensionality = UF_MODL_PLANAR
               data[0 - 2] = coordinates of a point on the plane
               data[3 - 5] = unit normal of the plane
               If *dimensionality = UF_MODL_THREE_DIMENSIONAL
               data[0 - 5] = not used
               */
);

/********************************************************************

   UF_MODL_ask_minimum_dist_3 is a version of UF_MODL_ask_minimum_dist_2
     with an additional input argument - opt_level

   UF_MODL_ask_minimum_dist_3 ( opt_level , object1, object2, guess1_given, guess1,
            guess2_given, guess2, min_dist, pt_on_obj1, pt_on_obj2, accuracy)

********************************************************************/
extern UFUNEXPORT int UF_MODL_ask_minimum_dist_3 (
int  opt_level , /* <I>
               0, works the same as UF_MODL_ask_minimum_dist_2
               1, uses a newer algorithm but should give the same results
               2, should produce more accurate results in some cases, and just as
                     good in all cases
               */
tag_t object1 ,/* <I>
               First object (if NULL_TAG, the point coordinates
               in guess1 are used instead)
               */
tag_t object2 ,/* <I>
               Second object (if NULL_TAG, the point coordinates
               in guess2 are used instead)

               If object1 and object2 are both NULL_TAG the distance from
               guess1 to guess2 is computed.
               */
int guess1_given ,/* <I>
                  1 - if a guess point for object1 is specified
                  0 otherwise
                  Ignored if object1 is a body
                  */
double guess1[3] ,/* <I>
                  Guess for the nearest point on object1, or point
                  coordinates to use in the distance computation if
                  object1 is a NULL_TAG. Ignored if object1 is a body.
                  */
int guess2_given ,/* <I>
                  1 - if a guess point for object2 is specified
                  0 otherwise
                  Ignored if object2 is a body
                  */
double guess2[3] ,/* <I>
                  Guess for the nearest point on object2, or point
                  coordinates to use in the distance computation if
                  object2 is a NULL_TAG. Ignored if object2 is a body.
                  */
double  * min_dist ,/* <O>
                    Resultant minimum distance.
                    */
double pt_on_obj1[3] ,/* <O>
                      Minimum distance Point on object1.
                      */
double pt_on_obj2[3] ,/* <O>
                      Minimum distance Point on object2.
                      */
double *accuracy  /* <O>
                  Size of absolute error resulting from the
                  use of faceted rather than solid bodies.
                  0.0 is output if neither body is faceted.
                  */

);

/********************************************************************

     UF_MODL_ask_minimum_dist_2 finds the minimum distance between a pair of objects.

     The objects can be:
        1. any combination of points, curves, planes, edges, faces or bodies.
        2. a faceted body and another faceted body or a solid edge, face
           or body or a point

     For objects not listed in 1, the error INVALID_ENTITY_TYPE is returned.

     If an attempt is made to measure between a faceted body and an object
     not listed in 2, the error UNSUITABLE_OBJECT_TYPES is returned.

     The function returns a pair of points (one for each object)
     at which the minimum distance is attained.

     The user can optionally specify a point on or near each object that is
     considered to be a good guess for the nearest point.  The guess point
     is ignored if either object is a faceted or solid body.

     Or, the user can find the distance to specified point coordinates
     by setting the object tag to NULL_TAG and inputting the point coordinates
     as the "guess" point.

     If either of the objects has a tolerance associated with it, the distance
     value may only be acccurate to within that tolerance.

     When a faceted body is involved in the measurement, the result may
     not be as accurate as that obtained with the equivalent solid body.
     It is recommended that UF_MODL_ask_minimum_dist_2 be used in this
     case, as an extra argument is provided to output the accuracy of the
     measurement.

Environment: Internal  and  External
See Also:  UF_MODL_ask_minimum_dist

History: Originally released in V17.0.
         In NX2.0.3 this function was updated to allow measurement between
         faceted bodies and points of type UF_point_type.

Note:  To get the best possible results, call UF_MODL_ask_minimum_dist_3() with an opt_level parameter value of "2".

********************************************************************/
extern UFUNEXPORT int UF_MODL_ask_minimum_dist_2 (
tag_t object1 ,/* <I>
               First object (if NULL_TAG, the point coordinates
               in guess1 are used instead)
               */
tag_t object2 ,/* <I>
               Second object (if NULL_TAG, the point coordinates
               in guess2 are used instead)

               If object1 and object2 are both NULL_TAG the distance from
               guess1 to guess2 is computed.
               */
int guess1_given ,/* <I>
                  1 - if a guess point for object1 is specified
                  0 otherwise
                  Ignored if object1 is a body
                  */
double guess1[3] ,/* <I>
                  Guess for the nearest point on object1, or point
                  coordinates to use in the distance computation if
                  object1 is a NULL_TAG. Ignored if object1 is a body.
                  */
int guess2_given ,/* <I>
                  1 - if a guess point for object2 is specified
                  0 otherwise
                  Ignored if object2 is a body
                  */
double guess2[3] ,/* <I>
                  Guess for the nearest point on object2, or point
                  coordinates to use in the distance computation if
                  object2 is a NULL_TAG. Ignored if object2 is a body.
                  */
double  * min_dist ,/* <O>
                    Resultant minimum distance.
                    */
double pt_on_obj1[3] ,/* <O>
                      Minimum distance Point on object1.
                      */
double pt_on_obj2[3] ,/* <O>
                      Minimum distance Point on object2.
                      */
double *accuracy  /* <O>
                  Size of absolute error resulting from the
                  use of faceted rather than solid bodies.
                  0.0 is output if neither body is faceted.
                  */

);
/********************************************************************

     UF_MODL_ask_minimum_dist finds the minimum distance between a pair of objects.

     The objects can be:
        1. any combination of points, curves, planes, edges, faces or bodies.
        2. a faceted body and another faceted body or a solid edge, face
           or body or a point

     For objects not listed in 1, the error INVALID_ENTITY_TYPE is returned.

     If an attempt is made to measure between a faceted body and an object
     not listed in 2, the error UNSUITABLE_OBJECT_TYPES is returned.

     The function returns a pair of points (one for each object)
     at which the minimum distance is attained.

     The user can optionally specify a point on or near each object that is
     considered to be a good guess for the nearest point.  The guess point
     is ignored if either object is a faceted or solid body.

     Or, the user can find the distance to specified point coordinates
     by setting the object tag to NULL_TAG and inputting the point coordinates
     as the "guess" point.

     If either of the objects has a tolerance associated with it, the distance
     value may only be acccurate to within that tolerance.

     When a faceted body is involved in the measurement, the result may
     not be as accurate as that obtained with the equivalent solid body.
     It is recommended that UF_MODL_ask_minimum_dist_2 be used in this
     case, as an extra argument is provided to output the accuracy of the
     measurement.

Environment: Internal  and  External
See Also:  UF_MODL_ask_minimum_dist_2
History: In V15.0 this function was updated to ignore guess points if a
         body is passed to it. Prior to V15.0, if you used a guess point
         and passed a body, this function returned an error message. A
         pre-V15.0 work around was to set the guess flags to a value of
         zero when passing in a body and using a guess point.
         In V17.0 this function was updated to allow measurement between
         faceted bodies and other faceted bodies and solid edges, faces
         and bodies.  If an attempt is made to measure between a faceted
         body and an entity not listed above the error
         UNSUITABLE_OBJECT_TYPES is returned.
         In NX2.0.3 this function was updated to allow measurement between
         faceted bodies and points of type UF_point_type.

Note:  To get the best possible results, call UF_MODL_ask_minimum_dist_3() with an opt_level parameter value of "2".


********************************************************************/
extern UFUNEXPORT int UF_MODL_ask_minimum_dist (
tag_t object1 ,/* <I>
               First object (if NULL_TAG, the point coordinates
               in guess1 are used instead)
               */
tag_t object2 ,/* <I>
               Second object (if NULL_TAG, the point coordinates
               in guess2 are used instead)

               If object1 and object2 are both NULL_TAG the distance from
               guess1 to guess2 is computed.
               */
int guess1_given ,/* <I>
                  1 - if a guess point for object1 is specified
                  0 otherwise
                  Ignored if object1 is a body
                  */
double guess1[3] ,/* <I>
                  Guess for the nearest point on object1, or point
                  coordinates to use in the distance computation if
                  object1 is a NULL_TAG. Ignored if object1 is a body.
                  */
int guess2_given ,/* <I>
                  1 - if a guess point for object2 is specified
                  0 otherwise
                  Ignored if object2 is a body
                  */
double guess2[3] ,/* <I>
                  Guess for the nearest point on object2, or point
                  coordinates to use in the distance computation if
                  object2 is a NULL_TAG. Ignored if object2 is a body.
                  */
double  * min_dist ,/* <O>
                    Resultant minimum distance.
                    */
double pt_on_obj1[3] ,/* <O>
                      Minimum distance Point on object1.
                      */
double pt_on_obj2[3]  /* <O>
                      Minimum distance Point on object2.
                      */
);

/********************************************************************
The routine UF_MODL_ask_angle_edge returns the values
associated to the angle-edge constraint. All coordinates are with
respect to the dimension plane, therefore there are only two values
(x,y).

Using UF_MODL_ask_constraints and UF_MODL_ask_constraint_type, find the
feature's "LINK_FACE_PARMS" constraint.  Use this constraint tag as the
"link_face_parms" input argument to the function UF_MODL_ask_link_face_plane
to obtain the dimension plane coordinate system.

Environment: Internal  and  External
See Also:  UF_MODL_ask_constraints.
          UF_MODL_ask_constraint_type
History: In V13.0, the tool argument was modified to output a NULL_TAG
         for a centerline.
********************************************************************/
extern UFUNEXPORT int UF_MODL_ask_angle_edge(
tag_t feature_obj_id ,/* <I>
                      Identifier for the feature.
                      */
tag_t constraint ,/* <I>
                  Identifier for constraint
                  */
int edit ,/* <I>
          This is an unused flag. It used to determine whether
          to return the right-hand side or both sides of an
          expression. Currently, both sides of an expression
          are returned.
          */
double fixed1[2] ,/* <O>
                  Dimension attachment point on the part
                  */
double fixed2[2] ,/* <O>
                  Point on part that along with the fixed1 point,
                  defines the line on the part that the dimension is
                  parallel/at an angle to.
                  */
double feature1[2] ,/* <O>
                    Dimension attachment point on the feature
                    */
double feature2[2] ,/* <O>
                    Point on the feature that along with the feature1
                    point, defines the line on the feature that the
                    dimension is parallel/at an angle to.
                    */
char ** how_far ,/* <OF>
                 Expression distance.  This must be freed by calling
                 UF_free.
                 */
tag_t * tool ,/* <O>
              Edge on the tool or NULL_TAG for centerline
              */
tag_t * part  /* <O>
              Edge on the part
              */
);

/******************************************************************************
Returns the angles between two vectors in radians.

Environment: Internal  and  External
See Also:
History:
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_vector_angle(
double vector1[3] ,/* <I>
                   First vector
                   */
double vector2[3] ,/* <I>
                   Second vector
                   */
double * small_angle ,/* <O>
                      Small angle (in radians)
                      */
double * large_angle  /* <O>
                      Large angle (in radians)
                      */
);

/********************************************************************
The routine UF_MODL_ask_horz_dime returns the values associated
to the horizontal dimension constraint. All coordinates are with respect
to the dimension plane, therefore there are only two values (x,y).

Using UF_MODL_ask_constraints and UF_MODL_ask_constraint_type, find the
feature's "LINK_FACE_PARMS" constraint.  Use this constraint tag as the
"link_face_parms" input argument to the function UF_MODL_ask_link_face_plane
to obtain the dimension plane coordinate system.

Environment: Internal  and  External
See Also:
History: In V13.0, the tool argument was modified to output a NULL_TAG
         for a centerline.
********************************************************************/
extern UFUNEXPORT int UF_MODL_ask_horz_dime(
tag_t feature_obj_id ,/* <I>
                      Identifier for the feature.
                      */
tag_t constraint ,/* <I>
                  Identifier for constraint
                  */
int edit ,/* <I>
          This is an unused flag. It used to determine whether
          to return the right-hand side or both sides of an
          expression. Currently, both sides of an expression
          are returned.
          */
double fixed[2] ,/* <O>
                 Dimension attachment point on the part
                 */
double feature[2] ,/* <O>
                   Dimension attachment point on the feature
                   */
double fixc[2] ,/* <O>
                Center of arc if attachment point is tangent to arc
                edge on part, otherwise it is the same as the fixed
                point.
                */
double feac[2] ,/* <O>
                Center of arc if attachment point is tangent to arc
                edge on feature, otherwise it is the same as the
                feature point.
                */
char ** how_far ,/* <OF>
                 Expression distance.  This must be freed by calling UF_free.
                 */
tag_t * tool ,/* <O>
              Edge on the tool or NULL_TAG for centerline
              */
tag_t * part  /* <O>
              Edge on the part
              */
);

/********************************************************************
The routine UF_MODL_ask_link_face_plane returns the plane
defining the link face constraint.  To ask for a feature's
constraints see UF_MODL_ask_constraints. To make an inquiry
on the list of constraints see UF_MODL_ask_constraint_type.

Environment: Internal  and  External
See Also: UF_MODL_ask_constraint_type
          UF_MODL_ask_constraints
History:
********************************************************************/
extern UFUNEXPORT int UF_MODL_ask_link_face_plane(
tag_t feature_obj_id ,/* <I>
                      Feature to inquire upon.
                      */
tag_t link_face_parms ,/* <I>
                       Link face identifier.
                       */
double cplane_csys[12]  /* <O>
                        Plane system for the link face.
                        [0-2]  X direction
                        [3-5]  Y direction
                        [6-8]  Z direction
                        [9-11] Origin
                        */
);

/********************************************************************
The routine UF_MODL_ask_para_dist returns the values associated
to the parallel-at-a-distance constraint.  To ask for a feature's
constraints see UF_MODL_ask_constraints. To make an inquiry on the
list of constraints see UF_MODL_ask_constraint_type.

All coordinates returned are with respect to the dimension plane, 
therefore there are only two values (x,y).

Using UF_MODL_ask_constraints and UF_MODL_ask_constraint_type, find the
feature's "LINK_FACE_PARMS" constraint.  Use this constraint tag as the
"link_face_parms" input argument to the function UF_MODL_ask_link_face_plane
to obtain the dimension plane coordinate system.

Environment: Internal  and  External
See Also: UF_MODL_ask_constraints
          UF_MODL_ask_constraint_type
History: In V13.0, the tool argument was modified to return a NULL_TAG
         for a centerline.
********************************************************************/
extern UFUNEXPORT int UF_MODL_ask_para_dist(
tag_t feature_obj_id ,/* <I>
                      Identifier for the feature.
                      */
tag_t constraint ,/* <I>
                  Identifier for constraint
                  */
int edit ,/* <I>
          This is an unused flag. It used to determine whether
          to return the right-hand side or both sides of an
          expression. Currently, both sides of an expression
          are returned.
          */
double fixed[2] ,/* <O>
                 Dimension attachment point on the part
                 */
double feature[2] ,/* <O>
                   Dimension attachment point on the feature
                   */
double fixc[2] ,/* <O>
                Center of arc if attachment point is tangent to arc
                edge on part, otherwise it is the same as the fixed
                point.
                */
double feac[2] ,/* <O>
                Center of arc if attachment point is tangent to arc
                edge on feature, otherwise it is the same as the
                feature point.
                */
char ** how_far ,/* <OF>
                 Expression distance.  This must be freed by the
                 caller by calling UF_free.
                 */
tag_t * tool ,/* <O>
              Edge on the tool or NULL_TAG for a centerline
              */
tag_t * part  /* <O>
              Edge on the part
              */
);

/********************************************************************
The routine UF_MODL_ask_para_edge returns the values associated
to the parallel-edge constraint.  To ask for a feature's constraints
see UF_MODL_ask_constraints. To make an inquiry on the list of constraints
see UF_MODL_ask_constraint_type.

All coordinates returned are with respect to the dimension plane, 
therefore there are only two values (x,y).

Using UF_MODL_ask_constraints and UF_MODL_ask_constraint_type, find the
feature's "LINK_FACE_PARMS" constraint.  Use this constraint tag as the
"link_face_parms" input argument to the function UF_MODL_ask_link_face_plane
to obtain the dimension plane coordinate system.

Environment: Internal  and  External
See Also: UF_MODL_ask_constraints
          UF_MODL_ask_constraint_type
History: In V13.0, the tool argument was modified to return a NULL_TAG
         for a centerline.
********************************************************************/
extern UFUNEXPORT int UF_MODL_ask_para_edge(
tag_t feature_obj_id ,/* <I>
                      Identifier for the feature.
                      */
tag_t constraint ,/* <I>
                  Identifier for constraint
                  */
int edit ,/* <I>
          This is an unused flag. It used to determine whether
          to return the right-hand side or both sides of an
          expression. Currently, both sides of an expression
          are returned.
          */
double fixed1[2] ,/* <O>
                  Dimension attachment point on the part
                  */
double fixed2[2] ,/* <O>
                  Point on the part that along with the fixed1 point,
                  defines the line on the part that the dimension is
                  parallel to.
                  */
double feature1[2] ,/* <O>
                    Dimension attachment point on the feature.
                    */
double feature2[2] ,/* <O>
                    Point on the feature that along with the feature1
                    point, defines the line on the feature that the
                    dimension is parallel to.
                    */
int * parallel ,/* <O>
                Is this a parallel constraint or a perpendicular constraint?
                TRUE=Parallel, FALSE=perpendicular
                */
char ** how_far ,/* <OF>
                 Expression distance.  This must be freed by calling UF_free.
                 */
tag_t * tool ,/* <O>
              Edge on the tool or NULL_TAG for a centerline.
              */
tag_t * part  /* <O>
              Edge on the part
              */
);

/********************************************************************
The routine UF_MODL_ask_perp_dist returns the values associated
to the perpendicular distance constraint.  To ask for a feature's
constraints see UF_MODL_ask_constraints. To make an inquiry on the
list of constraints see UF_MODL_ask_constraint_type.

All coordinates returned are with respect to the dimension plane, 
therefore there are only two values (x,y).

Using UF_MODL_ask_constraints and UF_MODL_ask_constraint_type, find the
feature's "LINK_FACE_PARMS" constraint.  Use this constraint tag as the
"link_face_parms" input argument to the function UF_MODL_ask_link_face_plane
to obtain the dimension plane coordinate system.

Environment: Internal  and  External
See Also: UF_MODL_ask_constraints
          UF_MODL_ask_constraint_type
History:
********************************************************************/
extern UFUNEXPORT int UF_MODL_ask_perp_dist(
tag_t feature ,/* <I>
               Identifier for the feature.
               */
tag_t constraint ,/* <I>
                  Identifier for constraint
                  */
int edit ,/* <I>
          This is an unused flag. It used to determine whether
          to return the right-hand side or both sides of an
          expression. Currently, both sides of an expression
          are returned.
          */
double fixed1[2] ,/* <O>
                  Dimension attachment point on the part.
                  */
double fixed2[2] ,/* <O>
                  Point on the part that along with the fixed1 point,
                  defines the line that the dimension is perpendicular
                  to.
                  */
double feature1[2] ,/* <O>
                    Dimension attachment point on the part.
                    */
double feac[2] ,/* <O>
                Center of arc if the attachment point is tangent to
                arc edge of feature, otherwise it is the same as the
                feature point.
                */
char ** how_far ,/* <OF>
                 Expression distance.  This must be freed by calling UF_free.
                 */
tag_t * tool ,/* <O>
              Edge on the tool or NULL_TAG for a centerline
              */
tag_t * part  /* <O>
              Edge on the part
              */
);

/******************************************************************
The routine UF_MODL_ask_vert_dime returns the values associated
to the vertical dimension constraint.  To ask for a feature's
constraints see UF_MODL_ask_constraints.  To make an inquiry on
the list of constraints see UF_MODL_ask_constraint_type.

All coordinates returned are with respect to the dimension plane, 
therefore there are only two values (x,y).

Using UF_MODL_ask_constraints and UF_MODL_ask_constraint_type, find the
feature's "LINK_FACE_PARMS" constraint.  Use this constraint tag as the
"link_face_parms" input argument to the function UF_MODL_ask_link_face_plane
to obtain the dimension plane coordinate system.

Environment: Internal  and  External
See Also: UF_MODL_ask_constraints
          UF_MODL_ask_constraint_type
History:
********************************************************************/
extern UFUNEXPORT int UF_MODL_ask_vert_dime(
tag_t feature_obj_id ,/* <I>
                      Identifier for the feature.
                      */
tag_t constraint ,/* <I>
                  Identifier for constraint
                  */
int edit ,/* <I>
          This is an unused flag. It was used to determine
          whether to return the right-hand side or both sides
          of an expression. Currently, both sides of an
          expression are returned.
          */
double fixed[2] ,/* <O>
                 Dimension attachment point on the part
                 */
double feature[2] ,/* <O>
                   Dimension attachment point on the feature
                   */
double fixc[2] ,/* <O>
                Center of arc if attachment point is tangent to arc
                edge on part, otherwise it is the same as the fixed
                point.
                */
double feac[2] ,/* <O>
                Center of arc if attachment point is tangent to arc
                edge on feature, otherwise it is the same as the
                feature point.
                */
char ** how_far ,/* <OF>
                 Expression distance.  This must be freed by calling UF_free.
                 */
tag_t * tool ,/* <O>
              Edge on the tool or NULL_TAG for a centerline.
              */
tag_t * part  /* <O>
              Edge on the part
              */
);

/******************************************************************************
Gets the distance tolerance found in the Modeling Preferences dialog
box. This value is in the units of the part.

Return:
       Void.

Environment: Internal  and  External
See Also:
History:
 ******************************************************************************/
extern UFUNEXPORT void UF_MODL_ask_distance_tolerance(
double * tolerance  /* <O>
                    Distance tolerance
                    */
); /* <NEC> */

/******************************************************************************
Gets the angle tolerance found in the Modeling Preferences dialog
box. The angle tolerance is returned in degrees.
Return:
      Void.
Environment: Internal  and  External
See Also:
History:
 ******************************************************************************/
extern UFUNEXPORT void UF_MODL_ask_angle_tolerance(
double * tolerance  /* <O>
                    Angle tolerance (in degrees)
                    */
); /* <NEC> */

/*******************************************************************************
Determines if a given point lies inside, outside or on the boundary of a given
face, edge, solid or sheet body.  In the case of a sheet body, a point is considered
inside the body if it is on the face and on the body if it is on the boundary
edges of the sheet body.

Environment:Internal and External
See Also: 
History: Originally released in V16.0
*******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_point_containment
(
   double    point[3],          /* <I> Point coordinates of the inquiry point */
   tag_t     body,              /* <I> Face, edge, solid, or sheet body tag on
                                       which point is inquired
                                */
   int       *pt_status         /* <O>
                                Returned status of the point on the body
                                   1 = point is inside the body
                                   2 = point is outside the body
                                   3 = point is on the body
                                */
);

/*******************************************************************************
If UF_MODL_ask_uv_points_containment will be called multiple times for the same face
then this function, in conjunction with UF_MODL_unset_containment, will improve
the performance of the computations.

Call this function before to your calls to UF_MODL_ask_uv_points_containment

Environment:Internal and External
See Also: 
History: Originally released in NX8.0.2
*******************************************************************************/
extern UFUNEXPORT int UF_MODL_set_containment
(
    tag_t face_eid    /* <I> face which will be used in multiple UF_MODL_ask_uv_points_containment calls */
);

/*******************************************************************************
If UF_MODL_ask_uv_points_containment will be called multiple times for the same face
then this function, in conjunction with UF_MODL_set_containment, will improve
the performance of the computations.

Call this function after to your calls to UF_MODL_ask_uv_points_containment

Environment:Internal and External
See Also: 
History: Originally released in NX8.0.2
*******************************************************************************/
extern UFUNEXPORT int UF_MODL_unset_containment
(
    tag_t face_eid    /* <I> face which was used in multiple UF_MODL_ask_uv_points_containment calls */
);

/*******************************************************************************
Determines if a set of 2D points lie inside, outside or on the boundary (vertex/edge) 
of a face.

If this function will be called multiple times for the same face then performance can
be improved by using UF_MODL_set_containment and UF_MODL_unset_containment.

Environment:Internal and External
See Also: 
History: Originally released in NX6.0.2
*******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_uv_points_containment
(
    int       n_uvs,        /* <I> Number of 2D (u, v) points */
    double    *u_parms,     /* <I> Array of u parameters of 2D points */
    double    *v_parms,     /* <I> Array of v parameters of 2D points */
    tag_t     face_eid,     /* <I> Face on which the 2D points are inquired */
    int       *pts_status   /* <O,len:n_uvs> Array of the point containment status which have the following values:
                                   1 = point is inside the face
                                   2 = point is outside the face
                                   3 = point is on the boundary of the face
                             */
);

/******************************************************************************
A geometry check routine.
Returns whether the input object is tiny.

Environment: Internal  and  External
See Also:
History:
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_tiny_geometry(
tag_t obj_tag ,/* <I>
               Tag of solid body, face, edge, or curve
               */
double tolerance ,/* <I>
                  Tolerance value to check against, if = 0, then use
                  the current modeling distance tolerance
                  */
logical *is_tiny /* <O>
                 FALSE = object is not tiny
                 TRUE = object is tiny
                 */
);

/******************************************************************************
A geometry check routine.
Returns whether the input object is slightly out of alignment with the input matrix.

Environment: Internal  and  External
See Also:
History:
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_misalign_geometry(
tag_t obj_tag ,/* <I>
               Tag of solid face or curve
               */
double *matrix   ,/* <I>
                  Matrix against which to check for alignment
                  */
double tolerance ,/* <I>
                  Angle tolerance within which to check
                  */
logical *is_misaligned /* <O>
                       Alignment flag:
                       FALSE = object is not misaligned
                       TRUE  = object is misaligned
                       */
);

/******************************************************************************
A geometry check routine.
Determine whether the body provided by the caller passes the data structures
check.  This routine should be called before UF_MODL_ask_face_face_intersect.

Environment: Internal  and  External
See Also: UF_MODL_ask_face_face_intersect
History:
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_body_structures  (
       tag_t body_tag,                    /* <I> body tag */
       int   *num_tags,                   /* <O>
                                          Number of faces/edges in the input
                                          body which don't pass data structures
                                          check.
                                          */
       tag_t **fault_tags                 /* <OF,len:num_tags>
                                          array of tags of faces/edges which
                                          don't pass data structures check.
                                          This must be freed by calling UF_free.
                                          */
);

/******************************************************************************
A geometry check routine.
Determine whether the body provided by the caller passes the consistency
check.  This routine should be called before UF_MODL_ask_face_face_intersect.

Environment: Internal  and  External
See Also: UF_MODL_ask_face_face_intersect
          UF_MODL_ask_body_structures
History:
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_body_consistency (
       tag_t body_tag,                    /* <I> body tag */
       int   *num_tags,                   /* <O>
                                          The number of faces/edges in the input
                                          body which don't pass the consistency
                                          check. */
       int   **fault_tokens,              /* <OF,len:num_tags>
                                          Array of fault tokens.  Each token is
                                          a UF_MODL error code, which can be
                                          translated to a string by passing it
                                          to UF_get_fail_message.  This array
                                          must be freed by calling UF_free.
                                          */
       tag_t **fault_tags                 /* <OF,len:num_tags>
                                          Array of tags of faces/edges
                                          which don't pass the consistency check
                                          This array must be freed by calling
                                          UF_free.
                                          */
);

/******************************************************************************
A geometry check routine.
Determine whether the body provided by the caller passes the face-face
intersection check.  This routine should be called after
UF_MODL_ask_body_consistency has returned no errors.

Environment: Internal  and  External
See Also: UF_MODL_ask_body_consistency
          UF_MODL_ask_body_structures
History:
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_face_face_intersect (
       tag_t body_tag,               /* <I> body tag */
       int   *num_tags,              /* <O>
                                     Number of faces in the input body which
                                     have a face to face intersection */
       tag_t **fault_tags            /* <OF, len:num_tags>
                                     Array of face tags which have a face to
                                     face intersection. This must be freed by
                                     calling UF_free. */
);

/******************************************************************************
Returns the number of boundary edges of a sheet body, the number of
edges in each of these boundaries, and the tags for the edges in each
boundary. These edges bound only a single face found in the input
sheet body.

The array num_edges is dimensioned by the number of boundaries
found (e.g. includes boundaries of holes).  Each element in the array
contains the number of edges in the corresponding boundary. The
array edge_tags is dimensioned large enough to contain all the tags of
all the edges in all the boundaries.  The edges belonging to boundary
1 are listed first in the array, followed immediately by the edges for
boundary 2, etc.

If body_tag is an occurrence, then the return values are relative to the
occurrence, and not the prototype.

Environment: Internal  and  External
See Also:

History: Modified in V15.0 to work relative to the occurrence.
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_body_boundaries(
tag_t body_tag ,/* <I>
                Tag of sheet body to check for boundaries
                */
int * num_boundaries ,/* <O>
                      Number of boundaries found
                      */
int **num_edges ,/* <OF,len:num_boundaries>
                   Array of number of edges in each boundary found.  This
                   must be freed by calling UF_free.
                   */
tag_t **edge_tags  /* <OF,len:num_boundaries>
                     Array of edge tags in each boundary.  This must be freed
                     by calling UF_free.
                     */
);

/******************************************************************************
A geometry check routine.
The condition for smoothness is defined as being that the angle
between the normals of the two faces that meet at the edge does not
at any point along that edge exceed the angle supplied by the user. If
the tolerance entered = 0, the current modeling angle tolerance is
used. Edges with only one adjacent face are reported as smooth.

Environment: Internal  and  External
See Also:
History:
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_edge_smoothness(
tag_t edge_tag ,/* <I>
                Tag of edge to check
                */
double tolerance ,/* <I>
                  Angle tolerance against which to check (in degrees)
                  */
logical * is_smooth  /* <O>
                     FALSE = edge is not smooth;
                     TRUE = edge is smooth
                     */
);

/******************************************************************************
Returns the tolerance of the input edge.

Environment: Internal  and  External
See Also:
History:
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_edge_tolerance(
tag_t edge_tag ,/* <I>
                Tag of solid edge to check tolerance of
                */
double *tolerance  /* <O>
                  Tolerance of edge_tag
                  */
);

/******************************************************************************
A geometry check routine.
Determines whether the face provided is smooth (G1 continuous) or not.

Environment: Internal  and  External
See Also:
History:
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_face_smoothness
     (
        tag_t           face_tag,        /* <I> face tag to be queried.*/
        logical         *is_smooth       /* <O> logical result:
                                         If TRUE, the input face is smooth.
                                         If FALSE, the input face is not smooth.
                                         */
     );

/******************************************************************************
A geometry check routine.
Determines whether the face provided is self-intersecting.

Environment: Internal  and  External
See Also:
History:
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_face_self_intersect
     (
        tag_t          face_tag,         /* <I> face tag */
        int            *fault_token,     /* <O>
                                         Fault token.  If 0, then the face is
                                         not self-intersecting.  Otherwise
                                         it is a model error code that can be
                                         converted to a string by calling
                                         UF_get_fail_message.
                                         */
        double          point[3]         /* <O>
                                         Point of self-intersection in ABS
                                         coordinates */
     );

/******************************************************************************
A geometry check routine.
Returns whether the input solid face has a spike or cut. This function
uses the following method: The angle between each pair of adjoining
edges is checked.  If this angle is very small, the system checks several
points along the shorter edge; if the distance between each of those
points and the longer edge is less than the current Modeling Distance
Tolerance, then the face is determined to have a spike or cut.
You can find the current Modeling Distance Tolerance with
UF_MODL_ask_distance_tolerance. You can change this tolerance
with UF_MODL_set_distance_tolerance.

Environment: Internal  and  External
See Also: UF_MODL_ask_distance_toleranc
e
          UF_MODL_set_distance_toleranc
e
History:
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_face_spikes(
tag_t  face_tag ,/* <I>
                 Tag of face to check for spikes or cuts
                 */
logical *is_spike  /* <O>
                   FALSE = face has no spike/cut
                   TRUE = face has a spike/cut
                   */
);


/******************************************************************************
Returns the mass properties of the  specified collection of solid or sheet
bodies.

Specify units and a density value, and either an accuracy value
(set accuracy = 1) or relative tolerances (set accuracy = 2) for the mass
property computations.

For simple analytic solid or sheet bodies (e.g., planes, cylinders), an
accuracy value of 0.9 is sufficient. For more complicated solids or
B-Surface sheet body faces, accuracy values closer to 1.0 may be
necessary.

If Relative Tolerances are specified, the system iterates on accuracy
values until successive mass property values are within the specified
relative tolerances.

The relative tolerance values are defined by the test value (or estimated
relative tolerance) is where MP(n) is the mass property value for the n-th
iteration on the accuracy value.

If a relative tolerance of 0.0 is specified, no testing is done for the
corresponding mass property value, although all the mass property
values are computed using the same accuracy values.

Environment: Internal  and  External
See Also:

History:
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_mass_props_3d(
tag_t * objects ,/* <I,len:num_objs> num_objs
                        Array of solid or sheet body identifiers,
                        Solid bodies for analysis type 1,
                        Sheet bodies for analysis types 2 and 3
                 */
int num_objs ,/* <I>
              Number of objects
              */
int type ,/* <I>
          Type of 3D Analysis
          1 =  Solid Bodies
          2 =  Thin Shell - Sheet Bodies
          3  =  Bounded by Sheet Bodies
          */
int   units ,/* <I>
             Units of mass and length
             1 = Pounds and inches
             2 = Pounds and feet
             3 = Grams and centimeters
             4 = Kilograms and meters
             */
double  density ,/* <I>
                 Density - Mass per unit volume (Mass per unit area for thin
                 shell).  Not used for solid body analysis; for solid bodies
                 the densities of the solid bodies are used in the analysis
                 and the density of the combined set of bodies is output
                 in the mass properties array (mass_props[46]).
                 */
int accuracy ,/* <I>
              1 = Use Accuracy
              2 = Use Relative Tolerances
              */
double acc_value[11] ,/* <I>
                      [0]    =  Accuracy value between 0.0 and 1.0
                                if accuracy = 1
                      [1-10] not used if accuracy = 1
                      [0]   = Relative Tolerance for Area if accuracy = 2
                      [1]   = Relative Tolerance for Volume
                      [2-4] = Relative Tolerances for First Moments (centroidal)
                      [5-7] = Relative Tolerances for Moments of Inertia
                              (centroidal)
                      [8-10]= Relative Tolerances for Products of Inertia
                              (centroidal)

                      */
double  mass_props[47] ,/* <O>
                        Mass properties
                        [0]     = Surface Area
                        [1]     = Volume (0.0 For Thin Shell)
                        [2]     = Mass
                        [3-5]   = Center Of Mass (COFM), WCS
                        [6-8]   = First Moments (centroidal)
                        [9-11]  = Moments Of Inertia, WCS
                        [12-14] = Moments Of Inertia (centroidal)
                        [15]    = Spherical Moment Of Inertia
                        [16-18] = Inertia Products, WCS
                        [19-21] = Inertia Products (centroidal)
                        [22-30] = Principal Axes, WCS
                        [31-33] = Principal Moments (centroidal)
                        [34-36] = Radii Of Gyration, WCS
                        [37-39] = Radii Of Gyration (centroidal)
                        [40]    = Spherical Radius Of Gyration
                        [41-45] = Unused
                        [46]    = Density
                        */
double  statistics[13]  /* <O>
                        Errors are Estimates of the Relative Tolerances
                        achieved if accuracy = 2; otherwise
                         +/- range errors are given
                        [0]  = Error For Surface Area
                        [1]  = Error For Volume
                        [2]  = Error For Mass
                        [3]  = Radius Of Error Sphere
                        [4]  = Error For Moment XC
                        [5]  = Error For Moment YC
                        [6]  = Error For Moment ZC
                        [7]  = Error For Moment Of Inertia XC
                        [8]  = Error For Moment Of Inertia YC
                        [9]  = Error For Moment Of Inertia ZC
                        [10] = Error For Product Of Inertia XCYC
                        [11] = Error For Product Of Inertia YCZC
                        [12] = Error For Product Of Inertia XCZC
                        */
);

/***************************************************************************
   Prototypes for Feature Modeling
  ***************************************************************************/

/****************************************************************************
Creates an offset.

Environment: Internal  and  External
See Also:
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_create_feature_offset(
char * offset ,/* <I>
               Offset
               */
uf_list_p_t features ,/* <I>
                      Offset feature object list.
                      */
tag_t * feature_obj_id  /* <O>
                        Feature object identifier of created feature offset
                        */
);

/********************************************************************
Gets the offset parameters.

Environment: Internal  and  External
See Also:
History:
********************************************************************/
extern UFUNEXPORT int UF_MODL_ask_offset_parms(
tag_t feature_obj_id ,/* <I>
                      A feature object identifier
                      */
int edit ,/* <I>
          This is an unused flag. It used to determine whether
          to return the right-hand side or both sides of an
          expression. Currently, both sides of an expression
          are returned.
          */
char ** value  /* <OF>
               The offset value.  This must be freed by calling
               UF_free.
               */
);


/****************************************************************************
Create offset feature using the input offset and list of features or
faces. The output of this function is the object identifier associated to
the offset feature. This routine works on planar faces, cylindrical faces
and conical faces.

Environment: Internal  and  External
See Also:
History: NX2.0 added the functionality to allow inputing face collector
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_create_face_offset(
char * offset ,/* <I>
               Offset offset.  Value must be greater than 1e-6 otherwise it is
               regarded as zero which is an invalid input.  We do not support
               zero as input.
               */
uf_list_p_t faces ,/* <I>
                   Offset feature/face object list. You can input a face collector
                   tag in the list. If you input a face collector, the face collector
                   should be the only member in the list.
                   */
tag_t * feature_obj_id  /* <O>
                        Feature object identifier of created face offset
                        */
);

/******************************************************************************
Create a Points Feature

Environment: Internal  and  External
See Also: UF_MODL_ask_points_parms
          UF_MODL_edit_points_parms
History: Originally released in V16.0
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_create_points_feature(
    int    num_points,          /* <I> Number of points */
    tag_t *points,              /* <I,len:num_points>
                                       Array of point tags */
    tag_t *feature_tag          /* <O> Feature tag */
);

/******************************************************************************
Ask for the points in a Points Feature

Environment: Internal  and  External
See Also: UF_MODL_create_points_feature
          UF_MODL_edit_points_parms
History: Originally released in V16.0
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_points_parms(
    tag_t   feature_tag,         /* <I> Feature tag */
    int    *num_points,          /* <O> Number of points */
    tag_t **points               /* <OF,len:num_points> Array of point tags.  This array must
                                    be freed by calling UF_free.
                                 */
);
/******************************************************************************
Replace the points in a Points Feature

Environment: Internal  and  External
See Also: UF_MODL_ask_points_parms
          UF_MODL_edit_points_parms
History: Originally released in V16.0
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_edit_points_parms(
    tag_t  feature_tag,         /* <I> Feature tag */
    int    num_points,          /* <I> Number of points */
    tag_t *points               /* <I,len:num_points> Array of point tags */
);

/******************************************************************************
Creates a subdivided face feature. The output of this function is the
object identifier associated to the subdivide face.

Environment: Internal  and  External
See Also:
History:
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_create_subdiv_face(
const tag_t* curve_refs ,/* <I,len:count>
                         Array of curves to subdivide the face with
                         */
const int  count ,/* <I>
                  Number of curves in curve_refs
                  */
const tag_t  face ,/* <I>
                   Face object identifier
                   */
const int proj_type ,/* <I>
                     Projection type
                     1 = Along surface normal
                     2 = Along vector (Not implemented yet)
                     */
const double vector[3] ,/* <I>
                        Projection vector if projection type = 2 (Not used)
                        */
tag_t * feature_obj_id  /* <O>
                        Feature object identifier of created subdivide face
                        */
);


/*******************************************************************************
Replaces a curve in a subdivided face feature with another curve. At
the end of the edit for a subdivided face, a UF_MODL_update should
be called to perform an update.

Environment: Internal  and  External
See Also: UF_MODL_update
History:
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_edit_subdiv_face(
const int  edit_flag ,/* <I>
                      Edit flag
                      1 = replace curve
                      others for future use
                      */
const tag_t  feature_obj_id ,/* <I>
                             Feature object identifier of a subdivide face
                             */
const tag_t  remove_curve ,/* <I>
                           Curve to remove from the subdivide face feature
                           */
const tag_t  add_curve ,/* <I>
                        Curve to add to the subdivide face feature
                        */
const double vector[3]  /* <I>
                        Projection vector (Not used)
                        */
);


/******************************************************************************
Returns the parameters of a subdivided face feature.

Environment: Internal  and  External
See Also:
History:
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_subdiv_face_parms(
const tag_t feature_obj_id ,/* <I>
                      Feature object identifier of a subdivided face
                      */
tag_t * face ,/* <O>
              Face object identifier which the subdivided face is
              on
              */
tag_t ** curves ,/* <OF,len:count>
                 Pointer to array of curves associated with the
                 subdivide face feature
                 */
int * count ,/* <O>
             Number of curves in curve array
             */
int* proj_type ,/* <O>
                Projection type
                1 = Along surface normal
                2 = Along vector (Not implemented yet)
                */
double* vector  /* <O>
                Projection vector (Not used)
                */
);

/******************************************************************************
Creates a face pair feature by defining faces.  The midsurface of the
face pair is created in the middle of the defining faces.

NOTE: a midsurface feature must be created before a call to this function and
passed in as midsrf_feature_obj_id(see UF_MODL_create_midsrf_feature).

Environment: Internal  and  External
See Also:
History:
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_cre_def_facepair_feat(
tag_t midsrf_feature_obj_id ,/* <I>
                             Midsurface Feature tag
                             */
tag_t defining_face_1 ,/* <I>
                       Defining face for side 1
                       */
tag_t defining_face_2 ,/* <I>
                       Defining face for side 2
                       */
uf_list_p_t side_1 ,/* <I>
                    List of target solid faces for side 1
                    */
uf_list_p_t side_2 ,/* <I>
                    List of target solid faces for side 2
                    */
tag_p_t facepair_feature_obj_id  /* <O>
                                 Face Pair Feature tag
                                 */
);


/******************************************************************************
Creates a face pair feature by a user selected midsurface.

NOTE: a midsurface feature must be created before a call to this function and
passed in as midsrf_feature_obj_id(see UF_MODL_create_midsrf_feature).

Environment: Internal  and  External
See Also:
History:
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_cre_sel_facepair_feat(
tag_t midsrf_feature_obj_id ,/* <I>
                             Midsurface Feature tag
                             */
tag_t user_selected_midsurface ,/* <I>
                                A Face or a sheet solid used to represent the
                                midsurface of the Face Pair feature.
                                */
uf_list_p_t side_1 ,/* <I>
                    List of target solid faces for side 1
                    */
uf_list_p_t side_2 ,/* <I>
                    List of target solid faces for side 2
                    */
tag_p_t facepair_feature_obj_id  /* <O>
                                 Face Pair Feature tag
                                 */
);

/******************************************************************************
Returns parameter data from a face pair feature.

Environment: Internal  and  External
See Also:
History:
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_facepair_parms(
tag_t facepair_feature_obj_id ,/* <I>
                               Face Pair Feature tag
                               */
int * face_pair_type ,/* <O>
                      Face Pair Feature type
                      1 Defining face
                      2  User Selected
                      */
tag_p_t midsrf_feature_obj_id ,/* <O>
                               Midsurface Feature tag of the Face Pair
                               */
tag_p_t defining_face_1 ,/* <O>
                         Defining face for side 1
                         */
tag_p_t defining_face_2 ,/* <O>
                         Defining face for side 2
                         */
tag_p_t user_selected_midsurface ,/* <O>
                                  A Face or a sheet solid used to represent the
                                  midsurface of the Face Pair feature.
                                  */
uf_list_p_t * side_1 ,/* <OF,free:UF_MODL_delete_list>
                      List of target solid faces for side 1.  This must be
                      freed by calling UF_MODL_delete_list.
                      */
uf_list_p_t * side_2 ,/* <OF,free:UF_MODL_delete_list>
                      List of target solid faces for side 2.  This must be
                      freed by calling UF_MODL_delete_list.
                      */
tag_p_t midsurface_sheet_body  /* <O>
                               Midsurface of the Face Pair Feature
                               */
);
/******************************************************************************
Returns the children and parameters of a patch body feature.

Environment: Internal  and  External
See Also:  UF_MODL_patch_body
History:
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_patch_body_parms(
tag_t feature_obj_id ,/* <I>
                      Feature object identifier of patch body feature
                      */
tag_t * target_body ,/* <O>
                     Object id of target body
                     */
tag_t * tool_sheet ,/* <O>
                    Object id of sheet body tool
                    */
int * reverse  /* <O>
               Patch direction flag
               UF_MODL_ALONG_NORMAL along surface normal of tool_sheet
               UF_MODL_OPPOSITE_NORMAL opposite surface normal of tool_sheet
               */
);
/******************************************************************************
Edits a patch feature.

Environment:Internal and External
See Also: UF_MODL_patch_body
          UF_MODL_ask_patch_body_parms
History:
*******************************************************************************/
extern UFUNEXPORT int UF_MODL_edit_patch_body_parms(
tag_t feature,    /* <I>
                  Feature to edit
                  */
tag_t new_target, /* <I>
                  New target body to replace the old target body
                  */
tag_t new_tool,   /* <I>
                  New tool body to replace the old tool body
                  */
tag_t new_face,   /* <I>
                  New face to replace the old face
                  */
int   new_reverse /* <I>
                  New reverse direction:
                  1 = Reverse
                  0 = No Reverse
                  */
);
/*******************************************************************************
Create multiple sewn sheets from a set of sheets.  This routine returns a list
of sheet bodies.  If you want the sew features, they can be obtained by calling


Environment: Internal  and  External
See Also:  UF_MODL_create_sew
           UF_MODL_ask_sew_sheet_body
           UF_MODL_edit_sew_sheet_body
           UF_MODL_ask_sew_solid_body
           UF_MODL_edit_sew_solid_body
History: Modified in V15 to return a list of sheet bodies, not a list of SEW
features
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_create_multiple_sews(
tag_t target_sheet ,/* <I>
                    Target sheet
                    */
int num_tools ,/* <I>
               Number of tools sheet array.
               */
tag_t tools_sheet[] ,/* <I,len:num_tools>
                     Tools sheet array.
                     */
double tolerance ,/* <I>
                  tolerance value.
                  */
uf_list_p_t* disjoint_list ,/* <OF,free:UF_MODL_delete_list>
                            List of disjoint sheets.  This list must be freed
                            by calling UF_MODL_delete_list.
                            */
uf_list_p_t* sew_list  /* <OF>
                       List of sewn sheets.  These are sheet bodies.
                       If you want the sheet feature, then you must call
                       UF_MODL_ask_body_features and then search the list
                       for the latest SEW feature.  This list must be freed
                       by calling UF_MODL_delete_list.
                       */
);
/******************************************************************************
Sews sheet bodies or faces of solid bodies together.  When sewing solids, the 
arrays targets and tools contain the faces from the target and tool bodies.  The
faces from one body must match in geometry with the faces from the other body.
It is important to understand the interactive functionality in NX before trying
to use this function.


Environment: Internal  and  External
See Also:  UF_MODL_create_multiple_sews
           UF_MODL_ask_sew_sheet_body
           UF_MODL_edit_sew_sheet_body
           UF_MODL_ask_sew_solid_body
           UF_MODL_edit_sew_solid_body
History:
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_create_sew(
int option ,/* <I>
            Option flag:
            0 = Sew general
            1 = Sew all instances
            */
int num_targets ,/* <I>
                 Size of the targets array
                 */
tag_t targets[] ,/* <I,len:num_targets>
                 Array of target tags ( sheet body when type_body = 0 
                      or face(s) from a solid body when type_body = 1 ).
                 */
int num_tools ,/* <I>
                 Size of the tool array
                 */
tag_t tools[] ,/* <I,len:num_tools>
                 Array of tool tags ( sheet body when type_body = 0 
                    or face(s) from a solid body when type_body = 1 ).
               */
double tolerance ,/* <I>
                  Tolerance value
                  */
int type_body ,/* <I>
               Type of body:
               0 = Sheet (default)
               1 = Solid
               */
uf_list_p_t * disjoint_list ,/* <OF,free:UF_MODL_delete_list>
                             List contains disjoint sheets from the target.
                             This list must be freed by calling
                             UF_MODL_delete_list.
                             */
tag_t * sew_id  /* <O>
                The sew feature that was created.
                */
);

/******************************************************************************
Returns the information stored in the record of the input sew sheet body feature.

Environment: Internal  and  External
See Also:  UF_MODL_create_sew
           UF_MODL_create_multiple_sews
           UF_MODL_edit_sew_sheet_body
History: Original release was in V16.0.1.
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_sew_sheet_body
(
  tag_t   feature_obj_eid ,       /* <I> Feature object id of trimmed sheet.  */
  tag_t  *target_sheet_body ,     /* <O> Tag of the target sheet body */
  int    *tool_sheet_bodies_count,/* <O> Number of tool sheet bodies */
  tag_t **tool_sheet_bodies,      /* <OF,len:tool_sheet_bodies_count> Array of NX eids of sheet bodies.
                                          This array must be freed by calling UF_free.  */
  double *tolerance               /* <O> Distance tolerance for approximations.  */
);

/******************************************************************************
Returns the information stored in the record of the input sew solid body feature.

Environment: Internal  and  External
See Also:  UF_MODL_create_sew
           UF_MODL_edit_sew_solid_body
History: Original release was in V16.0.1.
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_sew_solid_body
(
  tag_t   feature_obj_eid,   /* <I> Feature object id of trimmed sheet.  */
  int    *target_faces_count,/* <O> Number of faces on the target body to be sewn */
  tag_t **target_faces,      /* <OF,len:target_faces_count> Array of NX eids of faces on the target body
                                     to be sewn. This array must be freed by
                                     calling UF_free.  */
  int    *tool_faces_count,  /* <O> Number of faces on the tool body to be sewn */
  tag_t **tool_faces,        /* <OF,len:tool_faces_count> Array of NX eids of faces on the tool body
                                     to be sewn. This array must be freed by
                                     calling UF_free.  */
  double *tolerance          /* <O> Distance tolerance for approximations.  */
);

/******************************************************************************
Modifies data of the input sew sheet bodies feature to the specified
tool bodies and tolerance conditions specified in the inputs.

Environment: Internal  and  External
See Also:  UF_MODL_create_sew
           UF_MODL_create_multiple_sews
           UF_MODL_ask_sew_sheet_body
History: Original release was in V16.0.1.

 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_edit_sew_sheet_body
(
  tag_t  feature_obj_eid ,/* <I> Feature object id of sew feature.  */
  tag_t  new_target_eid,  /* <I> The NX eid of the the new target sheet body.
                                 This option will be available in V17. */
  int    tool_body_count, /* <I> Number of tool sheet bodies */
  tag_t *tool_body_eids,  /* <I,len:tool_body_count>
                                 Array of NX eids of sheet bodies */
  double tolerance        /* <I> Distance tolerance for approximations */
);

/******************************************************************************
Modifies data of the input sew solid bodies feature to the specified
tool and target faces and tolerance conditions specified in the inputs.

Environment: Internal  and  External
See Also:  UF_MODL_create_sew
           UF_MODL_ask_sew_solid_body
History: Original release was in V16.0.1.

 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_edit_sew_solid_body
(
  tag_t     feature_obj_eid ,  /* <I> Feature object id of trimmed sheet.  */
  int       target_faces_count,/* <I> Number of faces on the target body to be sewn */
  tag_t    *target_faces,      /* <I,len:target_faces_count>
                                     Array of NX eids of faces on the target body
                                     to be sewn. This array must be freed by
                                     calling UF_free.  */
  int       tool_faces_count,  /* <I> Number of faces on the tool body to be sewn */
  tag_t    *tool_faces,        /* <I,len:tool_faces_count>
                                     Array of NX eids of faces on the tool body
                                     to be sewn. This array must be freed by
                                     calling UF_free.  */
  double    tolerance          /* <I> Distance tolerance for approximations.  */
);

/******************************************************************************
Creates a thread feature.  Specify the creation parameters in the
thread parameter structure.

For internal thread, argument "internal_thread" should be set as "TRUE" in parameters 
which is pointer to thread parameter structure UF_MODL_symb_thread_data_s.

Environment: Internal  and  External
See Also: 
  UF_MODL_symb_thread_data_p_t
History:
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_create_symb_thread(
UF_MODL_symb_thread_data_p_t parameters ,/* <I>
                                         Pointer to thread parameter structure
                                         UF_MODL_symb_thread_data_s
                                         */
tag_t * thread_obj_id  /* <O>
                       Thread object id
                       */
);

/******************************************************************************
Get parameters of a thread feature.

Environment: Internal  and  External
See Also:  UF_MODL_symb_thread_data_t
History:
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_symb_thread_parms(
tag_t thread_obj_id ,/* <I>
                     Thread object id
                     */
UF_MODL_symb_thread_data_t * parameters  /* <OF>
                                         Pointer to thread parameter structure
                                         UF_MODL_symb_thread_data_s
                                         Use routine UF_MODL_free_symb_thread_data
                                         to free this structure when needed.
                                         */
);


/******************************************************************************
This routine frees symbolic thread data structure UF_MODL_symb_thread_data_t filled by
UF_MODL_ask_symb_thread_parms.


Environment: Internal  and  External
See Also:  UF_MODL_symb_thread_data_t
History: NX10.0.0
 ******************************************************************************/
extern UFUNEXPORT void UF_MODL_free_symb_thread_data(
UF_MODL_symb_thread_data_p_t thread  /* <I>
                                         Pointer to thread parameter structure
                                         UF_MODL_symb_thread_data_s
                                         */
);

/******************************************************************************
Edits a thread feature. This function will need a data structure as input.
Before calling this function, you can call UF_MODL_ask_symb_thread_parms
to check the existing thread parameters.

Only if a thread is created by the option "manual input" instead of "choose from table",
you can edit pitch, angle, minor and major diameters. Manual defined thread
has an empty callout, so you can know whether a thread is created by "manual input"
by checking if the callout is NULL, but you can not simply set callout = NULL.

For internal thread, argument "internal_thread" should be set as "TRUE" in parameters
which is pointer to thread parameter structure UF_MODL_symb_thread_data_s.

As any other editing function, you may need to call UF_MODL_update to view
your feature changes for internal Open API applications.

Environment: Internal  and  External
See Also:
 UF_MODL_symb_thread_data_p_t
History: This function is new to V14.0.
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_edit_symb_thread(
tag_t thread_obj_id ,/* <I>
                     Thread object id
                     */
UF_MODL_symb_thread_data_p_t parameters  /* <I>
                                         Pointer to thread parameter
                                         structure UF_MODL_symb_thread_data_s
                                         */
);

/*******************************************************************************
Create a reverse normal feature.  This will flip the normal on a sheet body.

Environment:Internal and External
See Also:
History: Originally released in V16.0
*******************************************************************************/
extern UFUNEXPORT int UF_MODL_create_reverse_normal
(
       tag_t sheet_body_tag, /* <I>
                             sheet body to be reversed
                             */

       int   option_flag,    /* <I>
                             = 0 - do not allow multiple reverse normal
                             features on the sheet body
                             = 1 - allow multiple reverse normal features
                             on the sheet body */

       tag_t *reverse_normal_tag /* <O>
                                 identifier for reverse normal feature
                                 */
);

/*******************************************************************************
Create a plane.

Environment:Internal and External
See Also: UF_MODL_ask_plane
          UF_MODL_edit_plane

History: Originally released in V16.0
*******************************************************************************/
extern UFUNEXPORT int UF_MODL_create_plane
(
   double    origin_point[3],  /* <I> Origin point of the plane */
   double    plane_normal[3],  /* <I> Plane normal */
   tag_t     *plane_tag        /* <O> New plane */
);

/*******************************************************************************
Returns the data of a plane feature.

Environment:Internal and External
See Also: UF_MODL_edit_plane
          UF_MODL_create_plane

History: Originally released in V16.0
*******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_plane
(
   tag_t     plane_tag,        /* <I> Plane */
   double    origin_point[3],  /* <O> Origin point of the plane */
   double    plane_normal[3]   /* <O> Normal of the plane */
);

/*******************************************************************************
Edits the data of a plane.

Environment:Internal and External
See Also: UF_MODL_ask_plane
          UF_MODL_create_plane

History: Originally released in V16.0
*******************************************************************************/
extern UFUNEXPORT int UF_MODL_edit_plane
(
   tag_t     plane_tag,        /* <I> Plane */
   double    origin_point[3],  /* <I> New origin point of the plane */
   double    plane_normal[3]   /* <I> New Normal of the plane */
);

/*******************************************************************************
Returns the data of a datum plane object.

Environment:Internal and External
See Also: UF_MODL_edit_plane
          UF_MODL_create_plane

History: Originally released in N5.0
*******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_datum_plane
(
   tag_t  dplane_tag,        /* <I> Datum plane */
   double dplane_point[3],   /* <O> Origin point of the datum plane */
   double dplane_normal[3]   /* <O> Normal direction of the datum plane */
);

/****************************************************************************
Create a uniform scale feature.

Environment: Internal  and  External
See Also:
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_create_uniform_scale(
    tag_t body_eid,  /* <I>
                     EID of body to be scaled
                     */
    int csys_type, /* <I>
                   Currently only UF_CSYS_WORK_COORDS is accepted
                   */
    char *scale_factor,  /* <I> */
    tag_t *feature_eid /* <O>
                       EID of the scale feature
                       */
);

/****************************************************************************
Create a non-uniform scale feature.

Environment: Internal  and  External
See Also:
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_create_non_uni_scale(
    tag_t body_eid,  /* <I>
                     EID of body to be scaled
                     */
    int csys_type, /* <I>
                   Currently only UF_CSYS_WORK_COORDS is accepted
                   */
    char *scale_factors[3],       /* <I> */
    tag_t *feature_eid /* <O>
                       EID of the scale feature
                       */
);

/************************************************************************
 *  This function will create scale features.
 *
 * Environment : Internal  and  External
 * See Also: UF_MODL_edit_scale
 * History : Released in V16.0
 ************************************************************************/
extern UFUNEXPORT int UF_MODL_create_scale
(
UF_SCALE_TYPE_t type, /* <I> The type of scale feature to create:
                               UF_SCALE_TYPE_UNIFORM
                               UF_SCALE_TYPE_AXISYMMETRIC
                               UF_SCALE_TYPE_GENERAL
                      */
tag_t *body_tags,     /* <I,len:num_body_tags>
                      An array of tags which contains the bodies to be scaled
                      */
int   num_body_tags,  /* <I> The number of body tags */
tag_t so_point,      /* <I> This is the tag of a smart point to use as the
                            origin of the scale feature.  If a NULL_TAG is
                            passed, the default origin will be the origin of
                            the WCS.  This argument is ignored for
                            UF_SCALE_TYPE_GENERAL scale features.
                     */
tag_t so_dir,  /* <I> This is a tag of a smart point to be used as the direction
                      of the scale for a UF_SCALE_TYPE_AXISYMMETRIC scale
                      feature. It is ignored for all other scale features.  If
                      a NULL_TAG is passed for an axisymmetric scale feature,
                      then the default will be the Z-axis of the WCS.
               */
tag_t so_csys, /* <I> This is the tag of a smart CSYS to be used for a
                      UF_SCALE_TYPE_GENERAL scale feature.  This parameter is
                      ignored for all other scale features.  If a NULL_TAG is
                      passed for a general scale feature, then the default will
                      be the WCS.
                */
char  factors[3][ UF_MAX_EXP_BUFSIZE ], /* <I,len:UF_MAX_EXP_BUFSIZE> An array of strings that define the
                                            scale factors.  These scale factors
                                            may include expressions.  For a
                                            uniform scale feature, there is only
                                            one string to use as a scale factor.
                                            For an axisymmetric scale feature,
                                            two factor strings must
                                            be passed in, the first being the
                                            scale factor along the axis, and the
                                            second being the scale factor in the
                                            other direction.  For a general
                                            scale feature, there will be three
                                            strings passed in this array, the
                                            first being the scale in the x-axis,
                                            the second being the scale in the
                                            y-axis and the third being the scale
                                            in the z-axis.
                                     */
tag_t **tags     /* <OF,len:num_body_tags>
                         This is an array of tags for the scale features
                         created. There will be one scale feature for each body
                         passed in.This array must be freed by calling UF_free.
                 */

);

/************************************************************************
 *  This function will edit a scale feature.
 *
 * Environment : Internal  and  External
 * See Also: UF_MODL_create_scale
 * History : Released in V16.0
 ************************************************************************/
extern UFUNEXPORT int UF_MODL_edit_scale
(
UF_SCALE_TYPE_t type, /* <I> The new type of scale feature to be edited to:
                                UF_SCALE_TYPE_UNIFORM
                                UF_SCALE_TYPE_AXISYMMETRIC
                                UF_SCALE_TYPE_GENERAL
                      */
tag_t tag,       /* <I>The tag of an existing scale feature to be edited */
tag_t so_point,  /* <I> This is the tag of a smart point to use as the origin
                        of the scale feature. If a NULL_TAG is passed, the
                        default origin will be the origin of the WCS.  This
                        argument is ignored for UF_SCALE_TYPE_GENERAL scale
                        features.
                 */
tag_t so_dir,    /* <I> This is a tag of a smart point to be used as the
                        direction of the scale for a UF_SCALE_TYPE_AXISYMMETRIC
                        scale feature.  It is ignored for all other scale
                        features. If a NULL_TAG is passed for an axisymmetric
                        scale feature, then the default will be the Z-axis of
                        the WCS.
                 */
tag_t so_csys,   /* <I> This is the tag of a smart CSYS to be used for a
                        UF_SCALE_TYPE_GENERAL scale feature.  This parameter is
                        ignored for all other scale features.  If a NULL_TAG is
                        passed for a general scale feature, then the default
                        will be the WCS.
                 */
char  factors[3][ UF_MAX_EXP_BUFSIZE ] /* <I,len:UF_MAX_EXP_BUFSIZE> An array of strings that define the
                                           scale factors.These scale factors may
                                           include expressions.  For a uniform
                                           scale feature, there is only one
                                           string to use as a scale factor.  For
                                           an axisymmetric scale feature, two
                                           factor strings must be passed in, the
                                           first being the scale factor along
                                           the axis, and the second being the
                                           scale factor in the other direction.
                                           For a general scale feature, there
                                           will be three strings passed in this
                                           array, the first being the scale in
                                           the x-axis, the second being the
                                           scale in the y-axis and the third
                                           being the scale in the z-axis.
                                    */
);

/************************************************************************
  This function will inquire and return parameters of a scale feature.

  Environment : Internal  and  External
  See  Also:  UF_MODL_create_scale
              UF_MODL_edit_scale
  History : Released in V16.0
 *************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_scale (
tag_t feature_tag,      /* <I> The tag of an existing scale feature */
UF_SCALE_TYPE_t * type, /* <O> Scale type. It is one of the following:
                                      UF_SCALE_TYPE_UNIFORM
                                      UF_SCALE_TYPE_AXISYMMETRIC
                                      UF_SCALE_TYPE_GENERAL
                        */
tag_t *so_point,     /* <O> This is the tag of a smart point used as the origin
                       of the scale feature. A NULL_TAG is returned for a
                       UF_SCALE_TYPE_GENERAL scale feature.
                     */

tag_t *so_dir,       /* <O> This is the tag of a smart point used as the
                        direction of the scale for a UF_SCALE_TYPE_AXISYMMETRIC
                        scale feature.  A NULL_TAG is returned for all other
                        scale features.
                     */
tag_t *so_csys,      /* <O> This is the tag of a smart CSYS used for a
                        UF_SCALE_TYPE_GENERAL scale feature.  A NULL_TAG is
                        returned for all other scale features.
                     */
char  factor[3][ UF_MAX_EXP_BUFSIZE ]
                    /* <O>  An array of strings that define the scale factors.
                      These scale factors may include expressions.  For a
                      uniform scale feature, there is only one string to use as
                      a scale factor.  For an axisymmetric scale feature, two
                      factor strings will be returned, the first being the
                      scale factor along the axis, and the second being the
                      scale factor in the other direction.  For a general scale
                      feature, there will be three strings returned in this
                      array, the first being the scale in the x-axis, the second
                      being the scale in the y-axis and the third being the
                      scale in the z-axis. */
);

/************************************************************************
 *  This function creates a Wrap Geometry feature.  A wrap geometry feature
 *  can be used to simplify NX geometry data by creating a convex solid envelope
 *  which surrounds the data.  This feature will be parameterized feature, so
 *  if the underlying model is changed, the wrap feature will automatically
 *  be updated.  The wrap feature can be used to hide proprietary data, to
 *  study packaging, for space capturing studies, or as a starting point when
 *  converting wireframe geometry to a solid.
 *
 * 
 *  Some of the detail of the original geometry can be retained by defining
 *  one or more splitting planes.
 * 
 *
 * See Also: UF_MODL_ask_wrap_geometry
 *           UF_MODL_edit_wrap_geometry
 *           UF_MODL_create_wrap_assembly
 *
 * Environment : Internal  and  External
 *
 * History : Released in V16.0
 ************************************************************************/
extern UFUNEXPORT int UF_MODL_create_wrap_geometry (
   UF_MODL_wrap_geom_p_t    wrap_data,   /* <I> Feature data */
   tag_t                    *feature_tag /* <O> Feature tag  */
   );

/************************************************************************
 *  This function reads the data of a Wrap Geometry feature.
 *
 * See Also: UF_MODL_create_wrap_geometry
 *           UF_MODL_edit_wrap_geometry
 *
 * Environment : Internal  and  External
 *
 * History : Released in V16.0
 ************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_wrap_geometry (
   tag_t                    feature_tag, /* <I> Feature tag  */
   UF_MODL_wrap_geom_p_t    wrap_data    /* <OF>
                                         Feature data.  The caller should
                                         allocate a
                                         UF_MODL_wrap_geom_t structure,
                                         and pass in a pointer to it.  This
                                         routine will fill in the structure
                                         based on the feature tag.  The caller
                                         is responsible for freeing the data
                                         returned in the geometry
                                         and splits array by calling UF_free,
                                         e.g.
                                            UF_free(wrap_data.splits);
                                            UF_free(wrap_data.geometry);
                                         */
   );

/************************************************************************
 *  This function edits a Wrap Geometry feature.
 *
 * See Also: UF_MODL_create_wrap_geometry
 *           UF_MODL_ask_wrap_geometry
 *
 * Environment : Internal  and  External
 *
 * History : Released in V16.0
 ************************************************************************/
extern UFUNEXPORT int UF_MODL_edit_wrap_geometry (
   tag_t                    feature_tag, /* <I> Feature tag  */
   UF_MODL_wrap_geom_p_t    wrap_data    /* <I> Feature data */
   );

/************************************************************************
 *  This function creates a Wrap Assembly feature in the work part.
 *  A Wrap Assembly feature can be used to simplify NX geometry data
 *  in an assembly by creating a convex solid envelope which surrounds the
 *  data.  This feature will be a parameterized feature, so if the underlying
 *  model is changed, the wrap feature will automatically be updated.  The
 *  wrap feature can be used to hide proprietary data, to study packaging,
 *  for space capturing studies, or as a starting point when converting
 *  wireframe geometry to a solid.  Input data can be from components and
 *  will create interpart links.  Each input object can have a corresponding
 *  assembly context xform to position the data in the work part.
 *
 * See Also: UF_MODL_ask_wrap_assembly
 *           UF_MODL_edit_wrap_assembly
 *           UF_MODL_edit_wrap_geometry
 *
 * Environment : Internal  and  External
 *
 * History : Released in V17.0
 ************************************************************************/
extern UFUNEXPORT int UF_MODL_create_wrap_assembly (
   UF_MODL_wrap_assem_p_t   wrap_data,   /* <I> Feature data */
   tag_t                    *feature_tag /* <O> Feature tag  */
   );

/************************************************************************
 *  This function reads the data of a Wrap Assembly feature.
 *
 * See Also: UF_MODL_create_wrap_assembly
 *           UF_MODL_edit_wrap_assembly
 *
 * Environment : Internal  and  External
 *
 * History : Released in V17.0
 ************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_wrap_assembly (
   tag_t                    feature_tag, /* <I> Feature tag  */
   UF_MODL_wrap_assem_p_t   wrap_data    /* <OF>
                                         Feature data.  The caller should
                                         allocate a
                                         UF_MODL_wrap_geom_t structure,
                                         and pass in a pointer to it.  This
                                         routine will fill in the structure
                                         based on the feature tag.  The caller
                                         is responsible for freeing the data
                                         returned in the geometry
                                         and splits array by calling UF_free,
                                         e.g.
                                            UF_free(wrap_data.geometry);
                                            UF_free(wrap_data.splits);
                                            UF_free(wrap_data.geom_xforms);
                                            UF_free(wrap_data.split_xform);
                                         */
   );

/************************************************************************
 *  This function edits a Wrap Assembly feature.
 *
 * See Also: UF_MODL_create_wrap_assembly
 *           UF_MODL_ask_wrap_assembly
 *
 * Environment : Internal  and  External
 *
 * History : Released in V17.0
 ************************************************************************/
extern UFUNEXPORT int UF_MODL_edit_wrap_assembly (
   tag_t                     feature_tag, /* <I> Feature tag  */
   UF_MODL_wrap_assem_p_t    wrap_data    /* <I> Feature data */
   );

/********************************************************************
Creates a chamfer feature using the type of chamfer, first and second
offset, and angle and list of edges to operate on. The output of this
function is the object identifier associated to the chamfer.

Environment: Internal  and  External
See Also:
History:
********************************************************************/
extern UFUNEXPORT int UF_MODL_create_chamfer(
int subtype ,/* <I>
             Chamfer type:
              1 = Single Offset
              2 = Double Offset
              3 = Offset and Angle
              4 = Freeform Single Offset
              5 = Freeform Double Offset
             */
char * offset1 ,/* <I>
                Chamfer offset 1
                */
char * offset2 ,/* <I>
                Chamfer offset 2
                */
char * theta ,/* <I>
              Chamfer angle
              */
uf_list_p_t edges ,/* <I>
                   List of edges to chamfer
                   */
tag_t * feature_obj_id  /* <O>
                        Feature object identifier of created chamfer
                        */
);

/********************************************************************
Creates a chamfer feature using the type of chamfer, first and second
offset, and angle and list of edges to operate on. If the Flip_option flag
is set to TRUE, the order of the input offsets will be flipped. The output
of this function is the object identifier associated to the chamfer.

Environment: Internal  and  External
See Also:
History:
********************************************************************/
extern UFUNEXPORT int UF_MODL_cre_chamfer_with_flip_option(
int subtype ,/* <I>
             Chamfer type:
              1 = Single Offset
              2 = Double Offset
              3 = Offset and Angle
              4 = Freeform Single Offset
              5 = Freeform Double Offset
             */
char * offset1 ,/* <I>
                Chamfer offset 1
                */
char * offset2 ,/* <I>
                Chamfer offset 2
                */
char * theta ,/* <I>
              Chamfer angle
              */
uf_list_p_t edges ,/* <I>
                   List of edges to chamfer
                   */
logical flip_option,/* <I>
                    Chamfer flip option
                    */
tag_t * feature_obj_id  /* <O>
                        Feature object identifier of created chamfer
                        */
);

/********************************************************************
Creates a chamfer feature using the type of chamfer, first and second
offset, and angle and list of edges to operate on.
- If the instance_option flag is set to TRUE, "chamfer ALL instances"
is turned ON, and vice versa.
-If the Flip_option flag
is set to TRUE, the order of the input offsets will be flipped. The output
of this function is the object identifier associated to the chamfer.

Environment: Internal  and  External
See Also:
History:
********************************************************************/
extern UFUNEXPORT int UF_MODL_cre_chamfer_with_instance_and_flip_option(
int subtype ,/* <I>
             Chamfer type:
              1 = Single Offset
              2 = Double Offset
              3 = Offset and Angle
              4 = Freeform Single Offset
              5 = Freeform Double Offset
             */
char * offset1 ,/* <I>
                Chamfer offset 1
                */
char * offset2 ,/* <I>
                Chamfer offset 2
                */
char * theta ,/* <I>
              Chamfer angle
              */
uf_list_p_t edges ,/* <I>
                   List of edges to chamfer
                   */
logical instance_option, /* <I> Enable chamfer all instances ON/OFF */
logical flip_option,/* <I>
                    Chamfer flip option
                    */
tag_t * feature_obj_id  /* <O>
                        Feature object identifier of created chamfer
                        */
);

/********************************************************************
Gets chamfer parameters.

Environment: Internal  and  External
See Also:
History:
********************************************************************/
extern UFUNEXPORT int UF_MODL_ask_chamfer_parms(
tag_t  feature_obj_id ,/* <I>
                       A feature object identifier
                       */
int  edit ,/* <I>
           This is an unused flag. It used to determine whether
           to return the right-hand side or both sides of an
           expression. Currently, both sides of an expression
           are returned.
           */
int * subtype ,/* <O>
               Chamfer subtype
               1 = Single offset.
               2 = Double offsets.
               3 = Offset and angle.
               4 = Freeform Single Offset
               5 = Freeform Double Offset
               */
char ** radius1 ,/* <OF>
                 Chamfer offset.  This must be freed by calling
                 UF_free.
                 */
char ** radius2 ,/* <OF>
                 Chamfer offset not valid for subtype 1 and 3.
                 This must be freed by calling UF_free.
                 */
char ** theta  /* <OF>
               Chamfer angle not valid for subtype 1 and 2.
               This must be freed by calling UF_free.
               */
);

/************************************************************************
 *  This function creates a mirror set feature.
 *
 * Environment : Internal  and  External
 *
 * See Also:
 *
 * History : Released in V16.0
 ************************************************************************/
extern UFUNEXPORT int UF_MODL_create_mirror_set(
tag_t *features,        /* <I,len:number_of_feature>
                               Array of features to mirror */
int number_of_feature,  /* <I> Number of features in the array */
tag_t mirror_plane,     /* <I> The mirror plane.  This can be a face or
                               a datum plane.
                        */
tag_t *mirror_set       /* <O> The tag of the new mirror set */
);

/************************************************************************
 *  This function asks for the mirror plane of the mirror set feature
 *
 * Environment : Internal  and  External
 * See Also: UF_MODL_create_mirror_set
 * History : Released in V16.0
 ************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_plane_of_mirror_set(
tag_t mirror_set, /* <I> The tag of the mirror feature */
tag_t *plane      /* <O> The mirror plane */
);

/************************************************************************
 *  This function ask for all the features inside the mirror set.
 *  The routine will return only the input features, to ask for the
 *  output feature use UF_MODL_ask_all_members_of_set().
 *
 * See Also:  UF_MODL_ask_all_members_of_set
 *
 * Environment : Internal  and  External
 *
 * History : Released in V16.0
 ************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_features_of_mirror_set(
tag_t mirror_set,        /* <I>  The tag of the mirror feature */
tag_t **features,        /* <OF,len:number_of_features>
                                 An array of input features.  This array must
                                 be freed by calling UF_free.
                         */
int *number_of_features  /* <O>  Number of features in the array */
);

/************************************************************************
 *  This function edits the mirror set.  It will replace all the features
 *  and the mirror plane of the mirror set feature.
 *
 * See Also: UF_MODL_create_mirror_set
 *           UF_MODL_ask_features_of_mirror_set
 *
 * Environment : Internal  and  External
 *
 * History : Released in V16.0
 ************************************************************************/
extern UFUNEXPORT int UF_MODL_edit_mirror_set(
tag_t mirror_set,       /* <I>  The tag of the mirror feature */
tag_t *features,        /* <I,len:number_of_features>
                               Array of features to mirror */
int number_of_features, /* <I> Number of features in the array */
tag_t mirror_plane      /* <I> The mirror plane can be a face or a datum plane*/
);


/******************************************************************************
 *  Create a feature set. If some member features are non-brwoseable,  the non-browseable features
 *  will be filtered out.
 *
 * Environment: Internal  and  External
 *
 * See Also:
 *
 * History: Released in V16.0
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_create_set_of_feature
(
    char *name,            /* <I> Name of feature set */
    tag_t *features,       /* <I,len:number_of_feature>
                                  Array of feature tags representing the
                                  members of the feature set */
    int number_of_feature, /* <I> Number of features in array */
    int hide_state,        /* <I> Hide state of feature set TRUE/FALSE */
    tag_t *feature         /* <O> Tag of feature set */
);

/******************************************************************************
 *  Edit, or replace, the members of a feature set.
 *
 * Environment: Internal  and  External
 *
 * See Also:
 *
 * History: Released in V16.0
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_edit_set_members
(
    tag_t set,            /* <I> The tag of the feature set */
    tag_t *features,      /* <I,len:number_of_feature>
                                 An array of input features representing
                                 the set members */
    int number_of_feature /* <I> Number of features in the array */
);

/******************************************************************************
 *  Edit the hide state of a feature set.
 *
 * Environment: Internal  and  External
 *
 * See Also:
 *
 * History: Released in V16.0
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_edit_set_hide_state
(
    tag_t set,      /* <I>  The tag of the feature set */
    int *hide_state /* <I/O> Integer value for hide state: 1 is for hidden.
                             Returns the previous state of the feature set */
);

/******************************************************************************
 *  Is the feature a member of a feature set, or sets?
 *
 * Environment: Internal  and  External
 *
 * See Also:
 *
 * History: Released in V16.0
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_is_feature_a_set_member
(
    tag_t feature, /* <I> Tag of feature */
    int *flag      /* <O> Return 1 if the feature is a member of a set. Otherwise, return 0. */
);

/******************************************************************************
 *  Is the feature a hidden member of a feature set, or sets?
 *
 * Environment: Internal  and  External
 *
 * See Also:
 *
 * History: Released in NX6.0
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_is_feature_a_hidden_set_member
(
    tag_t feature, /* <I> Tag of feature */
    logical *hidden_member /* <O> Return TRUE if the feature is a hidden member of a set. Otherwise, return FALSE. */
);

/******************************************************************************
 *  Return an array of feature sets that the feature is a member of.
 *
 * Environment: Internal  and  External
 *
 * See Also:
 *
 * History: Released in V16.0
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_sets_of_member
(
    tag_t feature,      /* <I>  Tag of feature */
    tag_t **sets,       /* <OF,len:number_of_sets> Array of feature sets that the feature belongs
                                too. This array must be freed by calling
                                UF_free */
    int *number_of_sets /* <O>  Number of sets in array */
);

/******************************************************************************
 *  Return the set that matches the feature name.
 *
 * Environment: Internal  and  External
 *
 * See Also:
 *
 * History: Released in V16.0
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_set_from_name
(
    char *name, /* <I> Feature set name */
    tag_t *set  /* <O> Tag of feature set */
);

/******************************************************************************
 *  Return an array of features that the set has as members.
 *
 * Environment: Internal  and  External
 *
 * See Also:
 *
 * History: Released in V16.0
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_all_members_of_set
(
    tag_t set,              /* <I>  Tag of feature set */
    tag_t **features,       /* <OF,len:number_of_features> Array of member features. This array
                                    must be freed by calling UF_free */
    int *number_of_features /* <O>  Number of features in array */
);

typedef struct
{
    tag_t original_entity;     /* Edge or face created by an
                                  original_feature[] */
    tag_t replacement_entity;  /* Corresponding edge or face
                                  created by a replacement_feature[] */
} UF_MODL_replace_features_t, * UF_MODL_replace_features_p_t;

/************************************************************************
This function replaces the features in original_features[] by the
features in replacement_features[] or the copies of features in
replacement_features[] if original_features[] are features on bodies,
curve features and datum features. The children of the original_features[]
will be reparented to the replacement_features[] or copies.

The original features will be deleted.

original_features[] can contain: features on the same body, curve features,
datum plane and datum axis features.

replacement_features[] must contain: features on other bodies (if
original_features[] contains features on a body), other curve features
(if original_features[] contains curve features) and other datum plane
and other datum axis features (if original_features[] contains datum plane
or datum axis features).

Note that original_features[] and replacement_features[] must contain
features that are in the same part file. Also, for features on a body, the
parents of each of the features in replacement_features[] must be either
another feature in the replacement_features[] or must be a feature which
is before the earliest feature in the original_features[].

parent_map[] maps entities created by the original_features[] to the
corresponding entities on the replacement_features[]. In addition to the
original_features[] and replacement_features[] you will  have to provide a map
of edges and faces on the original_features[] to  the corresponding edges and
faces of the replacement_features[].

You will specify the map as a array of objects of type
UF_MODL_replace_features_t described below. The children of the
original_features[] will be reparented to  copies of the corresponding
entities on the replacement_features[] that are specified in the  parent_map[].

Calling this function with return_map as true does not perform the replacement
but returns a parent_map[] each of whose original_entity elements are edges
and faces created by original_features[]. Only those edges and faces that are
parents of downstream features are returned in the parent_map[]. The
replacement_entity  elements of all the structures in the parent_map[] are 0.
You will have to assign the appropriate replacement_entity for each of
the structures returned in the parent_map[] before calling this function with
return_map as false to perform the actual replace.

Environment : Internal and External

See also: 

History: New in v17.0

 ************************************************************************/
extern UFUNEXPORT int UF_MODL_replace_features  (
    tag_t * original_features,      /* <I,len:n_original_features>
                                           Array of features to replace    */
    int     n_original_features,    /* <I> number of original_features    */
    tag_t * replacement_features,   /* <I,len:n_replm_features>
                                           Array of replacement features  */
    int     n_replm_features,       /* <I> number of replacement_features */
    logical return_map,             /* <I> return_map = true - return in
                                       parent_map[] the edges and faces created
                                       by the original_features[] which have to
                                       be mapped to the corresponding edges and
                                       faces on the replacement_features[]
                                       return_map = false - perform the replace
                                    */
    logical use_copy_of_replacement, /*  <I> use_copy_of_replacement = false -
                                         Use the replacement features directly to
                                         replace the original features
                                        use_copy_of_replacement = true  - Copy
                                        the replacement features and use the copy
                                        of the replacement feature to replace the
                                        original features
                                    */
    UF_MODL_replace_features_t ** parent_map, /* <I/O,len:n_parent_map>
                                                 Map of edges and faces
                                                 created by the
                                                 original_features[] to
                                                 corresponding edges and faces
                                                 on the replacement_features[]
                                              */
    int * n_parent_map /* <I/O> number of elements in (*parent_map)[] */
);

/******************************************************************************
Changes the current setting for the  modeling dynamic update preference. This
preference is used when editing a curve or a bridge curve feature from which
we can derive visible sheet or solid bodies.

If UF_MODL_NO_DYNAMIC_UPDATE is used, NX will not update the children
features of the curve. If UF_MODL_DYNAMIC_UPDATE_INCREMENTAL or
UF_MODL_DYNAMIC_UPDATE_CONTINUOUS is used, NX will dynamically update
the children, depending on the immediate children preference, of the curve
each time the mouse stops moving or moves, respectively.

Environment: Internal  and  External
See Also:  UF_MODL_ask_dynamic_update
           UF_MODL_set_immediate_children
           UF_MODL_ask_immediate_children
History: V17.0
*******************************************************************************/
extern UFUNEXPORT int UF_MODL_set_dynamic_update
(
    int  update_type  /* <I> Desired setting for dynamic update:
                             UF_MODL_NO_DYNAMIC_UPDATE,
                             UF_MODL_DYNAMIC_UPDATE_INCREMENTAL,
                             UF_MODL_DYNAMIC_UPDATE_CONTINUOUS
                       */
);

/******************************************************************************
Returns the current setting for the  modeling dynamic update preference. This
preference is used when editing a curve or a bridge curve feature from which
we can derive visible sheet or solid bodies.  If UF_MODL_NO_DYNAMIC_UPDATE is
used, NX will not update the children features of the curve. If
UF_MODL_DYNAMIC_UPDATE_INCREMENTAL or UF_MODL_DYNAMIC_UPDATE_CONTINUOUS is used,
NX will dynamically update the children, depending on the immediate
children preference, of the curve each time the mouse stops moving or moves,
respectively.

Environment: Internal  and  External
See Also:  UF_MODL_set_dynamic_update
           UF_MODL_set_immediate_children
           UF_MODL_ask_immediate_children
History: V17.0
*******************************************************************************/
extern UFUNEXPORT int  UF_MODL_ask_dynamic_update
(
    int *update_type  /* <O> Current setting of dynamic update:
                             UF_MODL_NO_DYNAMIC_UPDATE,
                             UF_MODL_DYNAMIC_UPDATE_INCREMENTAL,
                             UF_MODL_DYNAMIC_UPDATE_CONTINUOUS
                       */
);

/******************************************************************************
Changes the current setting for the modeling immediate children preference.
This preference is used when editing curve whose is parent of features that
create sheet and/or solid bodies and the modeling dynamic update is either
UF_MODL_DYNAMIC_UPDATE_INCREMENTAL or UF_MODL_DYNAMIC_UPDATE_CONTINUOUS.

If the user edits a curve through edit feature or edit bridge curve feature,
this preference is not applicable.  If UF_MODL_UPDATE_FIRST_LEVEL is used,
NX will update the first visible sheet or solid bodies that can be
derived from the curve. If UF_MODL_UPDATE_ALL, NX will update all
features related to the editing curve.

Environment: Internal  and  External
See Also:  UF_MODL_ask_immediate_children
           UF_MODL_ask_dynamic_update
           UF_MODL_set_dynamic_update
History: V17.0
 ******************************************************************************/
extern UFUNEXPORT int  UF_MODL_set_immediate_children
(
    int update_level /* <I> Desired setting for immediate children:
                              UF_MODL_UPDATE_FIRST_LEVEL,
                              UF_MODL_UPDATE_ALL
                      */
);

/******************************************************************************
Returns the current setting for the modeling immediate children preference.
This preference is used when editing curve whose is parent of features that
create sheet and/or solid bodies and the modeling dynamic update is either
UF_MODL_DYNAMIC_UPDATE_INCREMENTAL or UF_MODL_DYNAMIC_UPDATE_CONTINUOUS.

If the user edits a curve through edit feature or edit bridge curve feature,
this preference is not applicable.  If UF_MODL_UPDATE_FIRST_LEVEL is used,
NX will update the first visible sheet or solid bodies that can be
derived from the curve. If UF_MODL_UPDATE_ALL, NX will update all
features related to editing curve.

Environment: Internal  and  External
See Also:  UF_MODL_set_immediate_children
           UF_MODL_ask_dynamic_update
           UF_MODL_set_dynamic_update
History: V17.0
 ******************************************************************************/
extern UFUNEXPORT int  UF_MODL_ask_immediate_children
(
    int *update_level/* <O> Current setting of immediate children:
                              UF_MODL_UPDATE_FIRST_LEVEL,
                              UF_MODL_UPDATE_ALL
                      */
);
/******************************************************************************
Unites two bodies with options to keep the original target body, tool body, or both bodies.

Environment: Internal  and  External
See Also: ,
          UF_MODL_unite_bodies.
History: Release version 19.
******************************************************************************/
extern UFUNEXPORT int UF_MODL_unite_bodies_with_retained_options
(
    tag_t      original_target  ,    /* <I> Original target  body */
    tag_t      original_tool  ,      /* <I>  Original tool body */
    logical    retain_target_body ,  /* <I> Indicate whether to retain the target body.
                                            If TRUE  - the resulting body is the new body and
                                                       target body is retained,
                                               FALSE - the resulting body is the modified target body. */
    logical    retain_tool_body ,    /* <I> Indicate whether to retain the tool body.
                                            If TRUE  - the tool body is not consumed.
                                               FALSE - the tool body is consumed */
    tag_t    * frec_eid              /* <O> The resulting feature record tag */
) ;

/******************************************************************************
Subtract two bodies with options to keep the original target body, tool body, or both bodies.

Note: This function does not use the Modeling tolerance. The default tolerance used in the
Boolean operation is 0.01mm (1.0e-5 m).

Environment: Internal  and  External
See Also: ,
          UF_MODL_subtract_bodies.
History: Release version 19.
******************************************************************************/
extern UFUNEXPORT int UF_MODL_subtract_bodies_with_retained_options
(
    tag_t      original_target  ,    /* <I> Original target  body */
    tag_t      original_tool  ,      /* <I>  Original tool body */
    logical    retain_target_body ,  /* <I> Indicate whether to retain the target body.
                                            If TRUE  - the resulting body is the new body and
                                                       target body is retained,
                                               FALSE - the resulting body is the modified target body. */
    logical    retain_tool_body ,    /* <I> Indicate whether to retain the tool body.
                                            If TRUE  - the tool body is not consumed.
                                               FALSE - the tool body is consumed */
    tag_t    * frec_eid              /* <O> The resulting feature record tag */
) ;

/******************************************************************************
Intersect two bodies with options to keep the original target body, tool body, or both bodies.

Environment: Internal  and  External
See Also: ,
          UF_MODL_intersect_bodies.
History: Release version 19.
******************************************************************************/
extern UFUNEXPORT int UF_MODL_intersect_bodies_with_retained_options
(
    tag_t      original_target  ,    /* <I> Original target  body */
    tag_t      original_tool  ,      /* <I>  Original tool body */
    logical    retain_target_body ,  /* <I> Indicate whether to retain the target body.
                                            If TRUE  - the resulting body is the new body and
                                                       target body is retained,
                                               FALSE - the resulting body is the modified target body. */
    logical    retain_tool_body ,    /* <I> Indicate whether to retain the tool body.
                                            If TRUE  - the tool body is not consumed.
                                               FALSE - the tool body is consumed */
     tag_t    * frec_eid             /* <O> The resulting feature record tag */
) ;

/******************************************************************************
Edit the boolean features with the option to
keep the original target body, tool body, or both bodies.

Environment: Internal  and  External
See Also: UF_MODL_unite_bodies_with_retained_options ,
          UF_MODL_subtract_bodies_with_retained_options ,
          UF_MODL_intersect_bodies_with_retained_options
          UF_MODL_replace_boolean_body
History: Release version 19.
******************************************************************************/
extern UFUNEXPORT int UF_MODL_edit_boolean_with_retained_options
(
    tag_t      feature_eid ,  /* <I> Boolean feature */
    tag_t      new_target  ,  /* <I> If 0 is passed in, the target body is not
                                     change. Otherwise, the new target body will
                                     be changed in the boolean feature */
    tag_t      new_tool       /* <I> If 0 is passed in, the tool body is not
                                     change. Otherwise, the new tool body will
                                     be changed in the boolean feature */
) ;

/******************************************************************************
Returns the information stored in the record of the input boolean feature.

Environment: Internal  and  External
See Also: UF_MODL_unite_bodies_with_retained_options ,
          UF_MODL_subtract_bodies_with_retained_options ,
          UF_MODL_intersect_bodies_with_retained_options
          UF_MODL_edit_boolean_with_retained_options
          UF_MODL_replace_boolean_body
History: Release version 19.
******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_boolean_with_retained_options
(
    tag_t               feature_eid ,         /* <I> Boolean feature */
    UF_FEATURE_SIGN   * sign ,                /* <O> Type of boolean:
                                               *       - UF_POSITIVE : unite
                                               *       - UF_NEGATIVE : subtract
                                               *       - UF_UNSIGNED : intersect */
    tag_t             * original_target  ,    /* <O> Original target  body */
    tag_t             * original_tool  ,      /* <O>  Original tool body */
    logical           * retain_target_body ,  /* <O> Indicate whether to retain the target body.
                                                     If TRUE  - the resulting body is the new body and
                                                                target body is retained,
                                                        FALSE - the resulting body is the modified target body. */
    logical           * retain_tool_body      /* <O> Indicate whether to retain the tool body.
                                                     If TRUE  - the tool body is not consumed.
                                                        FALSE - the tool body is consumed */
) ;

/******************************************************************************
Returns the feature and the corresponding error code if a feature failed
to update resulting in an undo of the update. This function can be used to
provide more information to the user about the feature that failed to update.

The tag of the feature and the error code will only be returned if the update fail
option is set to UF_MODL_UPDATE_UNDO or if the update fail option is
UF_MODL_UPDATE_NO_OPTION and the update was invoked by a user function program.

The tag of the feature and the error code returned by this function is guaranteed
to be valid and accurate only when this function is called immediately after a
call to UF_MODL_update()

Environment: Internal  and  External
See Also:  UF_MODL_update
           UF_MODL_ask_update_fail_option
           UF_MODL_set_update_fail_option
History: V18.0
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_update_undo_feat (
    tag_t * feat,        /* <O> Feature that failed to update resulting in an UNDO */
    int   * feat_ifail   /* <O> The corresponding error code                       */
);

/****************************************************************************
Gets the tolerance of the input feature.

Environment: Internal  and  External

History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_feat_tolerance(
    tag_t   feature_obj_id ,   /* <I> Feature to inquire upon */
    logical *tolerance_exists, /* <O> Returns TRUE if distance tolerance exists for the feature */
    double  *tolerance         /* <O> Distance tolerance of feature */
);

/****************************************************************************
Sets the given tolerance to the input feature.

Environment: Internal  and  External

History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_set_feat_tolerance(
    tag_t   feature_obj_id ,   /* <I> Feature to set */
    double  tolerance,         /* <I> Distance tolerance to set in the feature */
    logical update_part        /* <I> Indicate whether to update the part.
                                      If TRUE  - Part will get updated by calling UF_MODL_update,
                                         FALSE - Part will not get updated, User has to update the part.
                                         User can set the tolerance of multiple features and then update
                                         the part by calling UF_MODL_update at end or
                                         pass the update_part flag as true for last feature */
);

/****************************************************************************
Returns the face in a feature instance that corresponds to a face in the
master of the instance. The feature instance must be a feature created from a
"pattern" feature, i.e. a feature of type LINEAR_PATTERN, CIRCULAR_PATTERN, or
MIRROR_SET. If the corresponding face cannot be found, this routine will
return NULL_TAG

Environment: Internal  and  External
History: NX4.0.2
***************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_matching_face_in_instance
(
    tag_t face_tag,           /* <I> Tag of a face whose owning feature is an instance master */
    tag_t feat_instance,      /* <I> Tag of a patterned feature */
    tag_t *instanced_face     /* <O> Tag of the face in the patterned feature */
);

/****************************************************************************
Returns all instances of the given feature from "pattern" features, i.e. features
of type LINEAR_PATTERN, CIRCULAR_PATTER, or MIRROR_SET.

Environment: Internal  and  External
History: NX4.0.2
**************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_instances_of_feature
(
    tag_t feature_tag,            /* <I> Tag of a feature */
    tag_t **feature_patterns,     /* <OF,len:n_feature_patterns> Array of feature instances.
                                     This array must be freed using UF_free */
    int *n_feature_patterns       /* <O> Number of feature patterns */
);

/*****************************************************************************************************************
Calculates the deviation between two curves

Environment: Internal  and  External
History:
******************************************************************************************************************/
extern UFUNEXPORT int UF_MODL_devchk_curve_to_curve
(
   tag_t curve1_id,           /* <I> Tag of the first curve */
   tag_t curve2_id,           /* <I> Tag of the second curve */
   int num_of_check_points,   /* <I> The number of check points. It should not smaller than 2 */
   UF_MODL_deviation_check_data_p_t check_result    /* <O> Address of UF_MODL_deviation_check_data_s structure */
); /* <NEC> */

/*****************************************************************************************************************
Calculates the deviation between curve and face

Environment: Internal  and  External
History:
******************************************************************************************************************/
extern UFUNEXPORT int UF_MODL_devchk_curve_to_face
(
   tag_t curve_id,            /* <I> Tag of curve */
   tag_t face_id,             /* <I> Tag of face */
   int num_of_check_points,   /* <I> The number of check points. It should not smaller than 2 */
   UF_MODL_deviation_check_data_p_t check_result    /* <O> Address of UF_MODL_deviation_check_data_s structure */
); /* <NEC> */

/*****************************************************************************************************************
Calculates the deviation between edge and face

Environment: Internal  and  External
History:
******************************************************************************************************************/
extern UFUNEXPORT int UF_MODL_devchk_edge_to_face
(
   tag_t edge_id,             /* <I> Tag of edge */
   tag_t face_of_edge_id,     /* <I> Tag of face which is associated with the former edge */ 
   tag_t second_face_id,      /* <I> Tag of second face */
   int num_of_check_points,   /* <I> The number of check points. It should not smaller than 2 */
   UF_MODL_deviation_check_data_p_t check_result    /* <O> Address of UF_MODL_deviation_check_data_s structure */
); /* <NEC> */

/*****************************************************************************************************************
Calculates the deviation between two faces 

Environment: Internal  and  External
History:
******************************************************************************************************************/
extern UFUNEXPORT int UF_MODL_devchk_face_to_face
(
   tag_t face1_id,            /* <I> Tag of the first face */
   tag_t face2_id,            /* <I> Tag of the second face */
   int num_check_points_u,     /* <I> The number of points in U direction. It should not smaller than 2 */
   int num_check_points_v,     /* <I> The number of points in V direction. It should not smaller than 2 */
   UF_MODL_deviation_check_data_p_t check_result    /* <O> Address of UF_MODL_deviation_check_data_s structure */
); /* <NEC> */

/*****************************************************************************************************************
Calculates the deviation between two edges

Environment: Internal  and  External
History:
******************************************************************************************************************/
extern UFUNEXPORT int UF_MODL_devchk_edge_to_edge
(
   tag_t edge1_id,            /* <I> Tag of the first edge */
   tag_t face_of_edge1_id,    /* <I> Tag of the face which is associated with the first edge */
   tag_t edge2_id,            /* <I> Tag of the second edge */
   tag_t face_of_edge2_id,    /* <I> Tag of the face which is associated with the second edge */
   int num_of_check_points,   /* <I> The number of check points. It should not smaller than 2 */
   UF_MODL_deviation_check_data_p_t check_result    /* <O> Address of UF_MODL_deviation_check_data_s structure */
); /* <NEC> */

/*****************************************************************************************************************
Determines the intersection between the two input curves, and outputs information describing the intersection.

Environment: Internal  and  External
History:
******************************************************************************************************************/
extern UFUNEXPORT int UF_MODL_intersect_curve_to_curve
(
    tag_t curve1_id,            /* <I> first curve or edge to intersect */
    tag_t curve2_id,            /* <I> second curve or edge to intersect */
    int* num_intersections,     /* <O> number of intersections */
    double** data               /* <OF,len:5*num_intersections,free:UF_free>
                                    This array must be freed by calling UF_free.
                                       It is a one dimensional array whose size is num_intersections * 5
                                       data[5*i + 0], data[5*i + 1] and data[5*i + 2] holds the coordinates of the point
                                       data[5*i + 3] holds the parameter of first curve or edge
                                       data[5*i + 4] holds the parameter of second curve or edge */
); 

/*****************************************************************************************************************
Determines the intersection between the curve and plane and
outputs information describing the intersection.

Environment: Internal  and  External
History:
******************************************************************************************************************/
extern UFUNEXPORT int UF_MODL_intersect_curve_to_plane
(
    tag_t curve_id,             /* <I> curve or edge to intersect */
    tag_t plane_id,             /* <I> plane curve to intersect */
    int* num_intersections,     /* <O> number of intersections */
    double** data               /* <OF,len:4*num_intersections,free:UF_free>
                                       This array must be freed by calling UF_free.
                                       It is a one dimensional array whose size is num_intersections * 4
                                       data[4*i + 0], data[4*i + 1] and data[4*i + 2] holds the coordinates of the point
                                       data[4*i + 3] holds the parameter of first curve or edge */
); 

/*****************************************************************************************************************
Determines the intersection between the curve and face, then outputs information describing the intersection.

Environment: Internal  and  External
History:
******************************************************************************************************************/
extern UFUNEXPORT int UF_MODL_intersect_curve_to_face
(
    tag_t curve_id,             /* <I> curve or edge to intersect */
    tag_t face_id,              /* <I> face to intersect */
    int* num_intersections,     /* <O> number of intersections */
    double** data               /* <OF,len:6*num_intersections,free:UF_free>
                                This array must be freed by calling UF_free.
                                       It is a one dimensional array whose size is num_intersections * 6
                                       data[6*i + 0], data[6*i + 1] and data[6*i + 2] holds the coordinates of the point
                                       data[6*i + 3] holds the parameter of first curve or edge
                                       data[6*i + 4] holds the u parameter of face
                                       data[6*i + 5] holds the v parameter of face */
);

/******************************************************************************
Given a feature, ask if the feature is browseable feature.

Environment:Internal and External
See Also:
History: NX8.0.3
*******************************************************************************/
extern UFUNEXPORT int UF_MODL_is_browseable_feature
(
    tag_t   feature_tag,                            /* <I> The feature whose browseable status is to be checked. */
    logical report_inactive_feature,                /* <I> TRUE: Inactive feature is reported as browseable.
                                                           FALSE: Inactive feature is not reported as browseable. */
    logical report_feature_unable_to_make_current,  /* <I> TRUE: Feature that cannot be made current is reported as browseable.
                                                           FALSE: Feature that cannot be made current is not reported as browseable. */
    logical *is_browseable                          /* <O> True if the feature is browseable, false otherwise. */
);

/******************************************************************************
Given a feature, get all update fail messages of that feature.

Environment: Internal  and  External
See Also:
History: NX8.0.3
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_feat_error
(
tag_t   feature_tag, /* <I> The feature being inquired.*/
int    *errNum,      /* <O> Number of error messages.*/
char ***errMessage   /* <OF,len:errNum>
                     Array of error messages. 
                     The caller is responsible for calling UF_free to free this array.
                     */
);

/******************************************************************************
Get the display name of the given feature.

Environment: Internal  and  External
See Also:
History: NX8.0.3
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_feat_display_name
(
tag_t feature_tag,   /* <I> The feature being inquired.*/
char ** feature_name /* <OF>The display name of the feature.
                        The caller is responsible for calling UF_free to free this array.*/
);

/******************************************************************************
Return the show report reference option. The option determines whether feature 
failure and warning will be shown in the feature update report. 

Environment: Internal  and  External
See Also:
History: NX8.0.3
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_show_report_reference
(
logical *reportReference /* <O>TRUE if report reference is shown, FALSE otherwise.*/
);

/******************************************************************************
Set the show report reference option. The option determines whether feature 
failure and warning will be shown in the feature update report.

Environment: Internal  and  External
See Also:
History: NX8.0.3
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_set_show_report_reference
(
logical reportReference /* <I>TRUE indicates report reference will be shown, FALSE otherwise.*/
);

/******************************************************************************
Get all failed feature records after update. Including feature records with 
warning messages.

Environment: Internal  and  External
See Also:
History: NX8.5.1
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_feat_fail_list(
    uf_list_p_t *failure_frec_list /* <OF> Failed feature record list.
                                   The caller is responsible for calling UF_MODL_delete_list
                                   to delete this list.
                                   */
);

/******************************************************************************
Given a feature, get all update warning messages of that feature.

Environment: Internal  and  External
See Also:
History: NX8.5.1
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_feat_warning_messages
(
    tag_t   feature_eid, /* <I> The feature being inquired.*/
    int    *wanNum,      /* <O> Number of warning messages.*/
    char  ***wanMessage  /* <OF,len:wanNum>
                         Array of warning messages. 
                         The caller is responsible for calling UF_free to free this array.
                         */
);

/******************************************************************************
The option determines whether feature update warnings will be recorded in the feature update report.
User should set this value back to "false" after using it.

Environment: Internal  and  External
See Also:
History: NX8.5.1
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_record_feature_update_warnings(
    logical warning_option /* <I> TRUE indicates that feature update warnings will be recorded. */
);



/******************************************************************************
Given a body, function returns true if body is a convergent body

Environment:Internal and External
See Also:
History: NX11.0.0
*******************************************************************************/
extern UFUNEXPORT int UF_MODL_is_body_convergent
(
tag_t    body,        /* <I> body to check */
logical *is_convergent_body /* <O> TRUE if a body is convergent body, else FALSE */
);

#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif     /* UF_MODL_H_INCLUDED */
