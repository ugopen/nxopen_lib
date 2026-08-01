/*****************************************************************************
             Copyright (c) 1998-2001,2002-2000 Unigraphics Solutions Inc.
                       Unpublished - All Rights Reserved



File description:
    Open API modeling routines to create, edit and inquire about datum features
    such as datum plane and datum axis.
*****************************************************************************/

#ifndef UF_MODL_DATUM_FEATURES_H_INCLUDED
#define UF_MODL_DATUM_FEATURES_H_INCLUDED


/***************************************************************************

  ***************************************************************************/

#include <uf_defs.h>
#include <uf_modl_types.h>
#include <libufun_exports.h>

#ifdef __cplusplus
extern "C" {
#endif

/*******************************************************************************
Creates a fixed datum plane feature where the plane passes through
"point" with a normal of "direction".


Environment: Internal  and  External
See Also: UF_MODL_ask_object_feat
History:
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_create_fixed_dplane(
double point[3] ,/* <I>
                 center point of datum plane
                 */
double direction[3] ,/* <I>
                     normal vector of datum plane
                     */
tag_t * dplane_tag  /* <O>
                    The created fixed datum plane tag. This is not a feature
                    tag. To obtain the feature tag use UF_MODL_ask_object_feat.
                    */
);

/******************************************************************************
Allows you to create relative datum planes based on the input
constraints. Refer to the table of available constraint types shown
below for the allowable combination of constraint types. If any of the
constraint geometry is an edge, then you must specify whether you are
using the edge or a point on the edge via the point_select parameter.
The which_plane argument determines which datum plane solutions
are returned. You can get up to two datum planes depending on the
specified constraints. The reference point is used to specify which
plane is returned first in the dplane_tag array. If you do not specify
this value, then the datum planes are returned in an arbitrary order.

When editing the Datum Plane created by this function an old style datum plane
dialog will be presented.


NOTE: A "Through Point" constraint can only be specified by putting an edge in
the object_tags array and an appropriate mid/end modifier in the
point_select array.


Environment: Internal  and  External
See Also: UF_MODL_ask_object_feat
History:
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_create_relative_dplane(
int num_refs ,/* <I>
              Number of constraint objects (<=3).
              */
tag_t object_tags[3] ,/* <I>
                      Array of constraint object tags (<=3).  See the
                      table of "Available Constraint Types" for possible
                      constraint types.
                      */
int  point_select[3] ,/* <I>
                      Array indicating to use edge constraint or point on
                      edge constraint if edge tag is supplied in obj_tags:
                      UF_MODL_EDGE
                      UF_MODL_MID_POINT
                      UF_MODL_END_POINT
                      UF_MODL_RIGHT_END_POINT start point of the edge
                      UF_MODL_LEFT_END_POINT  end point of edge
                      */
int  which_plane ,/* <I>
                  Solution number if more than one datum plane can
                  be constructed for the set of input constraints.

                  For the case where the first input object is a
                  CYL/REV/CONE/SPHERE and the second input object is a PLANE:
                    1. Two planes parallel to plane and tangent to the
                       face.  The plane closest to the reference point is
                       returned first in the dplane_tag array.
                    2. Two planes perpendicular to plane and tangent
                       to the face.  The plane closest to the reference
                       point is returned first in the dplane_tag array.
                    3. Plane through the face axis and angle to plane.
                       No reference point needed for this case.

                  For the case where the first input object is a CYL/REV
                  and the second input object is a CYL/REV/SPHERE:
                  (see Figure for examples)
                    1. Two planes where the tangency is on the "same
                       sides" of the faces.  The plane closest to the
                       reference point is returned first in the
                       dplane_tag array.
                    2. Two planes where the tangency is on the
                       "opposite sides" of the faces.  The plane closest
                       to the reference point is returned first in the
                       dplane_tag array.
                    3. Plane through both the face axes.  No reference
                       point needed for this case.

                  For the case where the first input object is a CYL/REV/SPHERE
                  and the second input object is a POINT:
                    1. Two planes tangent to the face and through
                       point.  The plane closest to the reference point
                       is returned first in the dplane_tag array.
                  */
double reference_point[3] ,/* <I>
                           Reference points used with which_plane flag.  If
                           NULL, then the order of the datum planes in the
                           dplane_tag array is arbitrary.
                           */
char * angle_string ,/* <I>
                     Angle parameter string.
                     */
char * offset_string ,/* <I>
                      Offset parameter string.
                      */
int* num_dplanes ,/* <O>
                  Number of datum planes returned (<=2)
                  */
tag_t dplane_tag[2]  /* <O>
                     The created datum plane(s). These are feature tags.
                     */
);

/******************************************************************************
Creates a datum plane perpendicular to a given direction at a given point.

If smart objects are used to specify the point or direction,
their update option must be set to UF_SO_update_within_modeling.

Environment: Internal  and  External
See Also:  UF_MODL_ask_object_feat
           UF_MODL_ask_datum_point_and_direction
           UF_MODL_edit_datum_point
           UF_MODL_edit_datum_direction
History: Original release was in V16.0.
******************************************************************************/
extern UFUNEXPORT int UF_MODL_create_point_dirr_dplane(
tag_t point, /* <I>
                A point on the datum plane.
             */
tag_t direction, /* <I>
                    The normal to the datum plane.
                 */
tag_t *dplane_tag /* <O>
                    The created datum plane. This is a not a feature tag.
                    To obtain the feature tag use UF_MODL_ask_object_feat.
                 */
);

/******************************************************************************
Creates a fixed datum axis feature which lies on the line through
Point1 in the direction of Point2.


Environment: Internal  and  External
See Also: UF_MODL_ask_object_feat
History:Original release was in V13.0.
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_create_fixed_daxis(
double point1[3] ,/* <I>
                  first point of datum axis
                  */
double point2[3] ,/* <I>
                  second point of datum axis
                  */
tag_t * daxis_tag  /* <O>
                   the created fixed datum axis. This is a not a feature
                   tag. To obtain the feature tag use UF_MODL_ask_object_feat.
                   */
);

/*******************************************************************************
Allows you to create relative datum axes. When the geometric objects
of the constraints and/or point types (for point constraints)  are input,
the routine creates the appropriate datum axis.

Environment: Internal  and  External
See Also:  UF_MODL_ask_feat_object

History:
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_create_relative_daxis
(
 int num_refs,          /* <I> number of constraints  maximum number of three */

 tag_t obj_eids[3],     /* <I> eids of the constraint objects maximum number of
                               three
                        */

 int point_select[3],   /* <I> Array indicating to use edge constraint or point on
                      edge constraint if edge tag is supplied in obj_tags:
                      UF_MODL_EDGE
                      UF_MODL_MID_POINT
                      UF_MODL_END_POINT
                      UF_MODL_RIGHT_END_POINT start point of the edge
                      UF_MODL_LEFT_END_POINT  end point of edge
                     */

 tag_t *daxis_feid      /* <O> Feature tag for the created datum axis, or
                               NULL_TAG if the datum axis was not created. */
);

/******************************************************************************
Creates a datum axis at a given point with a given direction.
If smart objects are used to specify the start point or direction,
their update option must be set to UF_SO_update_within_modeling.

Environment: Internal  and  External
See Also:  UF_MODL_ask_object_feat
           UF_MODL_ask_datum_point_and_direction
           UF_MODL_edit_datum_point
           UF_MODL_edit_datum_direction
History: Original release was in V16.0.
******************************************************************************/
extern UFUNEXPORT int UF_MODL_create_point_dirr_daxis(
tag_t point, /* <I>
                The start point of the datum axis.
             */
tag_t direction, /* <I>
                    The direction of the datum axis.
                 */
tag_t *daxis_tag /* <O>
                    The created datum axis. This is a not a feature tag.
                    To obtain the feature tag use UF_MODL_ask_object_feat.
                 */
);


/******************************************************************************
Create a datum axis which is defined by a curve and a point on that curve.

Environment: Internal  and  External
See Also:
History:
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_create_frenet_daxis
(
 tag_t curve_tag,        /* <I> eid of the curve, it could be UF_line_type,
                                UF_circle_type, UF_conic_type,
                                UF_spline_type or UF_solid_edge_subtype.
                         */

 tag_t direction_tag,    /* <I> eid of the constraint object which defines the
                                direction of the projection curve,
                                NULL if not the case. it could be a face,
                                edge, line, datum plane or datum axis.
                         */

 char  *perc_string,     /* <I> the parameter of curve, range from 0 to 100 */

 int direction_type,     /* <I> the direction of frenet datum axis, 1 and 4
                                are tangent direction and its opposite,
                                2 and 5 are normal direction and its opposite,
                                3 and 6 are binormal and its opposite,
                                and 0 when projection curve is created
                         */

 tag_t *daxis_feid       /* <O> the created daxis eid */
);


/******************************************************************************
Gets datum plane parameters. Plane center and normal are given in
an array of three floating point numbers with X value in the first
element, Y in the second, and Z in the third. Parameters for offset
distance from plane and offset angle from plane are returned in
expression format which needs to be deallocated using UF_free. If
these two parameters are not applicable, the pointers are NULL.
acquires and prints out the parameters for the selected datum plane.

Environment: Internal  and  External
See Also:

History:
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_datum_plane_parms(
tag_t  feature_obj_id ,/* <I>
                       Feature object identifier of datum plane.
                       */
double  origin[3] ,/* <O>
                   Datum plane center.
                   */
double normal[3] ,/* <O>
                  Datum plane normal.
                  */
char ** offset ,/* <OF>
                Offset distance from plane.  This must be freed by calling
                UF_free.
                */
char ** angle  /* <OF>
               Offset angle from plane.  This must be freed by calling UF_free.
               */
);

/****************************************************************************
Get datum axis parameters.

Environment: Internal  and  External
See Also: 
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_datum_axis_parms(
        tag_t  feature_id,      /* <I>
                                Feature tag for datum axis
                                */
        double origin[3],       /* <O>
                                Datum axis base point
                                */
        double normal[3]        /* <O>
                                Datum axis direction
                                */
);

/******************************************************************************
Returns the point and direction of a datum feature.

If the datum does not have a point or direction tag, NULL_TAG is returned.

Environment: Internal  and  External
See Also:  UF_MODL_ask_object_feat
           UF_MODL_create_point_dirr_daxis
           UF_MODL_create_point_dirr_dplane
           UF_MODL_edit_datum_point
           UF_MODL_edit_datum_direction
History: Original release was in V16.0.
******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_datum_point_and_direction(
tag_t datum_feature_tag, /* <I>
                            The datum feature tag.
                         */
tag_p_t point, /* <O>
                  The point of the datum.
               */
tag_p_t direction /* <O>
                     The direction of a datum axis or, the normal to the datum
                     plane.
                  */
);

/******************************************************************************
Replaces the base point of a datum feature with new_point.

The feature should have been created using UF_MODL_create_point_dirr_daxis() or
UF_MODL_create_point_dirr_dplane().  If a smart object is used to specify the
new point, its update option should be UF_SO_update_within_modeling.

Environment: Internal  and  External
See Also:  UF_MODL_ask_object_feat
           UF_MODL_create_point_dirr_daxis
           UF_MODL_create_point_dirr_dplane
           UF_MODL_ask_datum_point_and_direction
           UF_MODL_edit_datum_direction
History: Original release was in V16.0.
******************************************************************************/
extern UFUNEXPORT int UF_MODL_edit_datum_point(
tag_t datum_feature_tag, /* <I>
                    The datum tag.
                 */
tag_t new_point /* <I>
                   The new point for the datum
                */
);

/******************************************************************************
Replaces the direction of a datum feature with new_direction.

The feature should have been created using UF_MODL_create_point_dirr_daxis or
UF_MODL_create_point_dirr_dplane().  If a smart object is used to specify the
new direction, its update option should be UF_SO_update_within_modeling.

Environment: Internal  and  External
See Also:  UF_MODL_ask_object_feat
           UF_MODL_create_point_dirr_daxis
           UF_MODL_create_point_dirr_dplane
           UF_MODL_ask_datum_point_and_direction
           UF_MODL_edit_datum_point
History: Original release was in V16.0.
******************************************************************************/
extern UFUNEXPORT int UF_MODL_edit_datum_direction(
tag_t datum_feature_tag, /* <I>
                    The datum tag.
                 */
tag_t new_direction /* <I>
                       The new direction of the datum axis.
                    */
);


/*******************************************************************************
Reverses the normal direction of a datum plane.  The function UF_MODL_update
must be called to actually apply the reversal.

Environment: Internal  and  External
See Also: UF_MODL_update
History:
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_reverse_datum_plane(
tag_t datum_plane_tag  /* <I>
                       Tag of the datum plane to reverse.
                       */
);

/******************************************************************************
Indicates if the datum plane is reversed in term of its normal
direction. Each datum plane has two normal directions: "regular" and
"opposite". Here, a "regular" datum plane direction would be the one
displayed during creation in an interactive session just before a user
selects the apply button. Similarly, an "opposite" datum plane
direction signifies the direction which is opposite to the regular one. If
the current datum plane direction is an opposite one, then the datum
plane is reversed.

Environment: Internal  and  External
See Also:
History:Original release was in V14.0.
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_is_datum_plane_reversed(
tag_t datum_plane_tag ,/* <I>
                       tag of the datum plane to reverse
                       */
logical * reversed  /* <O>
                    TRUE = Indicates the datum plane direction is
                            reversed.
                    FALSE = Indicates the datum plane direction is
                            not reversed.
                    */
);
/******************************************************************************
Reverses the direction of a datum axis.

Environment: Internal  and  External
See Also: UF_MODL_reverse_datum_plane
History:Original release was in V14.0.
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_reverse_datum_axis(
tag_t datum_axis_tag  /* <I>
                      Tag of the datum axis to reverse.
                      */
);

/******************************************************************************
Indicates if the datum axis is reversed in term of its direction. Each
datum axis has two directions: "regular" and "opposite". Here, a
"regular" datum axis direction would be the one displayed during
creation in an interactive session just before a user selects the apply
button. Similarly, an "opposite" datum axis direction signifies the
direction which is opposite to the regular one. If the current datum
axis direction is an opposite one, then the datum axis is reversed.

Environment: Internal  and  External
See Also: UF_MODL_is_datum_plane_reversed
History: Original release was in V14.0.
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_is_datum_axis_reversed(
tag_t datum_axis_tag ,/* <I>
                      tag of the datum axis to reverse
                      */
logical * reversed  /* <O>
                    TRUE = this means that the datum axis direction is
                    reversed.
                    FALSE =  this means that the datum axis direction
                    is not reversed.
                    */
);

/******************************************************************************
Converts the given datum feature into an absolute datum feature.

Environment: Internal  and  External

See Also:  UF_MODL_ask_object_feat

History: Original release was in V16.0.
******************************************************************************/
extern UFUNEXPORT int UF_MODL_convert_to_fixed_datum(
tag_t  datum_feature_tag  /* <I>
                             The datum tag.
                          */
);

/******************************************************************************
Returns the size of a datum axis

Environment: Internal  and  External

See Also:

History:
******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_daxis_size (
tag_t  daxis_tag,  /*  <I>
                       The datum tag
                   */
double *length     /*  <O>
                       Length of the datum axis
                   */
);

/***************************************************************************
   Prototypes for datum CSYS feature user functions
  ***************************************************************************/

/*******************************************************************************
Creates a datum CSYS given a transform defined by its tag.

The smart CSYS (visible object) and the  datum CSYS feature are created
with the update option always set to SO_update_within_modeling

Environment: Internal  and  External
See Also:


History:
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_create_datum_csys(
const tag_t object_in_part,  /* <I>
                                Object in part to define context.
                             */
tag_t xform_tag,             /* <I>
                                Tag of xform object:
                                Must be smart with update option set to
                                SO_update_within_modeling and must be created
                                using one of the construction methods:
                                . defined by three points
                                . defined by two directions and a point
                                . defined by three planes
                                . defined by offset from an existing CSYS
                              */
logical create_components,  /* <I>
                               Flag that if set will create all the components:
                               origin point,3 datum planes and 3 datum axes
                             */
 tag_t *datum_csys_feature   /* <O>
                                Tag of the datum CSYS feature - If successful
                             */
);

/*******************************************************************************
Returns the components of a datum CSYS and the parent smart CSYS.
There are the total of 7 components as follows:
   origin      -  origin point
   daxes[3]    -  datum axes coincident with the CSYS coordinate axes
   dplanes[3]  -  datum planes coincident with the CSYS coordinate planes

The application is responsible for allocating memory for the arrays

Environment: Internal  and  External
See Also:
History:
 ******************************************************************************/
extern UFUNEXPORT void UF_MODL_ask_datum_csys_components(
tag_t datum_csys_tag, /* <I>
                         Tag of the datum CSYS feature
                      */
tag_t *csys_tag,      /* <O>
                         Tag of the smart CSYS
                      */
tag_t *origin,        /* <O>
                         Tag of the origin point
                      */
tag_t daxes[3],        /* <O>
                         Tag of the three datum axes coincident
                          with the coordinate axes
                      */
tag_t dplanes[3]       /* <O>
                          Tag of the three datum planes coincident
                           with the coordinate planes
                      */
); /* <NEC> */

/*************************************************************************************************
This function returns the tag of the parent XFORM

If the feature record is not of a datum CSYS feature, NULL_TAG is returned.

Environment: Internal  and  External
See Also:
History:
*************************************************************************************************/
extern UFUNEXPORT tag_t  UF_MODL_ask_xform_tag_of_datum_csys  (
tag_t datum_csys_tag   /* <I>
                          Tag of the datum CSYS feature
                       */
); /* <NEC> */
/*************************************************************************************************
This function sets the tag of the XFORM into the csys of a datum_csys

If unsuccessful returns error code

Environment: Internal  and  External
See Also:
History:NX3
*************************************************************************************************/
extern UFUNEXPORT int UF_MODL_set_xform_tag_of_datum_csys  (
tag_t datum_csys_feature, /* <I> Tag of datum csys feature */
tag_t xform_tag       /* <I> xform tag to be set in datum_csys_tag*/
);

/*************************************************************************************************
This function creates the datum CSYS feature given the input of linear and
rotational(angular)offset values in distance and angle units respectively.
If unsuccessful returns error code

Environment: Internal  and  External
See Also:
History:NX3.0.1
*************************************************************************************************/
extern UFUNEXPORT int UF_MODL_create_datum_csys_offset(
const tag_t object_in_part, /*<I> Object in part to define context */
tag_t parent_datum_csys_tag, /*<I> Tag of CSYS component of the parent datum CSYS feature */
const double linear_offset[3], /*<I> Linear offset values in distance units */
const double angular_offset[3], /*<I> Angular (rotational) offset values in angle units */
logical create_components, /*<I> If TRUE, datum CSYS with components would be created */
tag_t *datum_csys_tag /*<O> Tag of created datum CSYS feature */
);
/*************************************************************************************************
This function sets the visibility of datum CSYS feature based on the logical value of
input argument "visibility"
If unsuccessful returns error code

Environment: Internal  and  External
See Also:
History:NX3.0.1
*************************************************************************************************/
extern UFUNEXPORT int UF_MODL_set_datum_csys_visibility(
const tag_t datum_csys_tag, /*<I> Tag of datum CSYS feature */
const logical visibility /*<I> If TRUE, datum CSYS with components would be visible */
);

/*************************************************************************************************
This function sets the "fixed size" display of datum CSYS feature. If "Fixed size component" toggle
in the CSYS constructor dialog is ON, then the datum CSYS will not be resized relative to the view.

If unsuccessful returns error code

Environment: Internal  and  External
See Also:
History:NX3.0.1
*************************************************************************************************/
extern UFUNEXPORT int UF_MODL_set_datum_csys_scaling(
const tag_t datum_csys_tag, /*<I> Tag of datum CSYS feature */
const logical scaling_on /*<I> If TRUE, datum CSYS with fixed size would be displayed */
);


#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif     /* UF_MODL_DATUM_FEATURES_H_INCLUDED */
