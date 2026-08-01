/*******************************************************************************

                    Copyright (c) 1998-2003 Unigraphics Solutions Inc. 
                             Unpublished - All rights reserved



File description:

The Geometric Expressions routines allow you to reference certain
geometric properties as constraints for defining parameters of
features. For example, you can use the minimum distance between
two objects as a driving expression for the length of a block.
The routines enable you to create the following new types of
expressions:
  . Length expression - an expression based upon the length of a curve 
    or an edge.
  . Distance expression - an expression based upon the minimum distance between
    two objects, or between a point and an object, or between two points.
  . Angle expression - an expression based upon the angle between two objects.

These expressions are created using scalar smart objects (see uf_so.h),
are created as features, and participate in the modeling update.

Many of these routines have an input which is a transformation
(xform). To create this transform and get its tag use the function
UF_SO_create_xform_assy_ctxt which provides the
transform for interpart geometric expressions (or one part occurrence
to another in an assembly tree). If both objects are in the same part,
then the tag of this transform is NULL_TAG.

All input objects to the routines must not be occurrence tags.

************************************************************************/

#ifndef UF_GEXP_H_INCLUDED
#define UF_GEXP_H_INCLUDED

/***************************************************************************

***************************************************************************/


#include <uf_gexp_types.h>
#include <libufun_exports.h>

#ifdef __cplusplus
extern "C" {
#endif

/**********************************************************************
Create a distance geometric expression feature.
This function computes and stores the minimum distance between
from_object and to_object in an expression. If object1_xform is not
NULL_TAG, then this transform is used to compute the
transformation for from_object.  If object2_xform is not NULL_TAG,
then this transform is used to compute the transformation for
to_object.  The created feature and the expression are stored in the 
current work part. The distance is in terms of the units of the work part, 
and is converted during ug_part_convert.

NOTE: The output expression's value may not be edited as you
would normal expressions.  It may only be used as a reference, and
only of features created after the geometric expression feature.

See Also: 
 UF_GEXP_edit_distance 
 UF_GEXP_ask_distance_parms


Environment: Internal  and  External
History: This function was originally released in V15.0.
 ************************************************************************/
extern UFUNEXPORT int UF_GEXP_create_distance(
    tag_t from_object,             /* <I>
                                   Tag of object to create the distance from.
                                   Valid object types are:
                                     UF_point_type,
                                     UF_line_type,
                                     UF_circle_type,
                                     UF_spline_type,
                                     UF_conic_type,
                                     UF_solid_type, and
                                     UF_datum_plane_type. 
                                     
                                   Occurrence tags are not allowed. Use the 
                                   prototype tag instead.
                                   */
    tag_t object1_xform,           /* <I>
                                   Tag of transformation for first object. 
                                   This tag is NULL_TAG if the object is in the
                                   same part in which the feature is created.
                                   */
    tag_t to_object,               /* <I>
                                   Tag of object to create distance to.  Valid 
                                   object types are:
                                      UF_point_type,
                                      UF_line_type,
                                      UF_circle_type,
                                      UF_spline_type,
                                      UF_conic_type,
                                      UF_solid_type, and
                                      UF_datum_plane_type. 

                                    Occurrence tags are not allowed. Use the 
                                    prototype tag instead.
                                   */
    tag_t object2_xform,           /* <I> 
                                   Tag of transformation for second object. 
                                   This tag is NULL_TAG if the object is in the
                                   same part in which the feature is created.
                                   */
    tag_t *feature_tag,            /* <O> 
                                   Tag of the created feature
                                   */
    tag_t *exp_tag                 /* <O>
                                   Tag of the created expression
                                   */
);

/******************************************************************
Creates an angle geometric expression feature. An angle between
from_object and to_object is computed and stored in an expression.
In the event that from_object is a line or a solid edge, qualifier1 is
used to determine which endpoint to use for computation. The same
is true for qualifier2 and to_object.  If object1_xform is not
NULL_TAG, then this is used to get the correct part occurrence tag
for from_object. The same is true for object2_xform and to_object.
The feature and the expression are created in the work part.  The
measured angle is in degrees.

NOTE The output expression's value may not be edited as you
would normal expressions.  It may only be used as a reference, and
only of features created after the geometric expression feature.

See Also: 
 UF_GEXP_edit_angle
 UF_GEXP_ask_angle_parms


Environment: Internal  and  External
History: This function was originally released in V15.0.
 ************************************************************************/
extern UFUNEXPORT int UF_GEXP_create_angle (
    tag_t from_object,              /* <I>
                                    Tag of object to create the angle from.
                                    Valid object types are:
                                     UF_line_type,
                                     UF_datum_plane_type,
                                     UF_datum_axis_type,
                                     UF_solid_type.
                                    A solid edge should be linear and a solid 
                                    face should be planar.

                                    Occurrence tags are not allowed. Use the 
                                    prototype tag instead.
                                    */
    UF_GEXP_qualifier_t qualifier1, /* <I>
                                    Qualifier for object1, only applicable to 
                                    lines and edges.  
                                    */
    tag_t object1_xform,            /* <I> 
                                    Tag of transformation for first object. 
                                    The tag is NULL_TAG if the object is in 
                                    the same part in which the feature is 
                                    created.       
                                    */
    tag_t to_object,                /* <I> 
                                    Tag of object to create angle from. 
                                    Valid object types are:
                                      UF_line_type,
                                      UF_datum_plane_type,
                                      UF_datum_axis_type,
                                      UF_solid_type.
                                    A solid edge should be linear and a solid 
                                    face should be planar.

                                    Occurrence tags are not allowed. Use the 
                                    prototype tag instead.
                                    */
    UF_GEXP_qualifier_t qualifier2, /* <I>
                                    Qualifier for object2,only applicable to 
                                    lines and edges. 
                                    */
    tag_t object2_xform,            /* <I> 
                                    Tag of transformation for second object. 
                                    The tag is NULL_TAG if the object is in the
                                    same part in which the feature is created.
                                    */
    tag_t *feature_tag,             /* <O> 
                                    Tag of the created feature
                                    */
    tag_t *exp_tag                  /* <O> 
                                    Tag of the created expression
                                    */
);


/******************************************************************
Creates a length expression feature. This function computes and
stores the length of object in an expression. If object_xform is not
NULL_TAG, then this transform is used to compute any scale factors
and units conversion for the object's length.
The resulting feature and expression are created in the work part.
The length is in terms of the units of the work part and is converted
during ug_part_convert.

NOTE The output expression's value may not be edited as you
would normal expressions.  It may only be used as a reference, and
only of features created after the geometric expression feature.

See Also: 
 UF_GEXP_edit_length
 UF_GEXP_ask_length_parms


Environment: Internal  and  External
History: This function was originally released in V15.0.
 **********************************************************************/
extern UFUNEXPORT int UF_GEXP_create_length (
    tag_t object,                  /* <I>
                                   Tag of object for which to create the length.
                                   Valid object types are:
                                      UF_line_type
                                      UF_circle_type
                                      UF_spline_type
                                      UF_conic_type
                                      UF_solid_type

                                    Occurrence tags are not allowed. Use the 
                                    prototype tag instead.
                                   */
    tag_t xform,                   /* <I>
                                    Tag of transformation for the object. 
                                    The tag is NULL_TAG if the object is in the
                                    same part in which the feature is created.
                                   */
    tag_t *feature_tag,            /* <O>
                                   Tag of the created feature
                                   */
    tag_t *exp_tag                 /* <O>
                                   Tag of the created expression
                                   */
);


/******************************************************************
Edits the distance expression feature by passing in new referenced
objects.  The newly calculated distance is stored in the expression
and all objects which reference the expression's value are then
updated to reflect the new value.  The calling routine must
call UF_MODL_update() to have the edit take effect.

See Also: 
 UF_GEXP_create_distance
 UF_GEXP_ask_distance_parms


Environment: Internal  and  External
History: This function was originally released in V15.0.
 ******************************************************************/
extern UFUNEXPORT int UF_GEXP_edit_distance (
    tag_t feature_tag,             /* <I>
                                   Tag of distance expression feature to edit.
                                   */
    tag_t new_from_object,         /* <I>
                                   Tag of object to use for newly edited 
                                   distance.

                                   Occurrence tags are not allowed. Use the 
                                   prototype tag instead.
                                   */
    tag_t new_xform1,              /* <I>
                                   Tag of transformation for first object. 
                                   This tag is NULL_TAG if the object is in the
                                   same part in which the feature is created.
                                   */
    tag_t new_to_object,           /* <I>
                                   Tag of object to use for newly edited 
                                   distance.

                                   Occurrence tags are not allowed. Use the 
                                   prototype tag instead.
                                   */
    tag_t new_xform2               /* <I>
                                   Tag of transformation for second object. 
                                   This tag is NULL_TAG if the object is in the
                                   same part in which the feature is created.
                                   */
);


/******************************************************************
Edits the length expression feature by passing in a new referenced
object and a new xform, if needed. The recomputed length
propagates into the expression, and all objects which reference its
value are updated to the correct value.  The calling routine must
call UF_MODL_update() to have the edit take effect.

See Also: 
 UF_GEXP_create_length
 UF_GEXP_ask_length_parms


Environment: Internal  and  External
History: This function was originally released in V15.0.
 *****************************************************************/
extern UFUNEXPORT int UF_GEXP_edit_length (
    tag_t feature_tag,             /* <I>
                                   Tag of length expression feature to edit.
                                   */
    tag_t new_object,              /* <I>
                                   Tag of object to use for newly edited length.
                                   Valid object types are:
                                     UF_line_type
                                     UF_circle_type
                                     UF_spline_type
                                     UF_conic_type
                                     UF_solid_type

                                   Occurrence tags are not allowed. Use the 
                                   prototype tag instead.
                                   */
    tag_t new_xform                /* <I>
                                   Tag of transformation for object. This 
                                   tag is NULL_TAG if the object is in the 
                                   same part in which the feature is created.
                                   */  
);


/******************************************************************
Edits the angle expression feature by passing in new referenced
objects, qualifiers, and transforms.  The recomputed angle then
propagates to the expression which updates all objects which
reference its value.  The calling routine must
call UF_MODL_update() to have the edit take effect.

See Also: 
 UF_GEXP_create_angle
 UF_GEXP_ask_angle_parms


Environment: Internal  and  External
History: This function was originally released in V15.0.
 ******************************************************************/
extern UFUNEXPORT int UF_GEXP_edit_angle(
    tag_t feature_tag,              /* <I>
                                    Tag of angle expression feature to edit.
                                    */
    tag_t new_from_object,          /* <I>
                                    Tag of object to use for newly edited angle.
                                    Valid object types are:
                                     UF_line_type
                                     UF_datum_plane_type
                                     UF_datum_axis_type
                                     UF_solid_type
                                    Solid edge should be linear and solid 
                                    face should be planar.

                                    Occurrence tags are not allowed. Use the 
                                    prototype tag instead.
                                    */
    UF_GEXP_qualifier_t qualifier1, /* <I>
                                    Qualifier for object1, only applicable to 
                                    lines and edges.
                                    */
    tag_t new_xform1,               /* <I>
                                    Tag of transformation for first object. 
                                    This is NULL_TAG if the object is in the 
                                    same part in which the feature is created.
                                    */
    tag_t new_to_object,            /* <I>
                                    Tag of object to use for newly edited angle.
                                    Valid object types are:
                                       UF_line_type
                                       UF_datum_plane_type
                                       UF_datum_axis_type
                                       UF_solid_type
                                    Solid edge should be linear and solid face 
                                    should be planar.

                                    Occurrence tags are not allowed. Use the 
                                    prototype tag instead.
                                    */
    UF_GEXP_qualifier_t qualifier2, /* <I>
                                    Qualifier for object2,only applicable to 
                                    lines and edges.
                                    */
    tag_t new_xform2                /* <I>
                                    Tag of transformation for second object. 
                                    This is NULL_TAG if the object is in the 
                                    same part in which the feature is created.
                                    */
);

/******************************************************************
Queries the given length expression feature and returns its
referenced object and transform.

See Also: 
 UF_GEXP_create_length
 UF_GEXP_edit_length

Environment: Internal  and  External
History: This function was originally released in V15.0.
 *****************************************************************/
extern UFUNEXPORT int UF_GEXP_ask_length_parms(
    tag_t feature_tag,            /* <I> 
                                  Tag of length expression feature to edit.
                                  */
    tag_t *ref_object,            /* <O> 
                                  Tag of referenced object
                                  */
    tag_t *xform                  /* <O> 
                                  Tag of transformation for the referenced 
                                  object.  The transformation is NULL_TAG for 
                                  an object in the same part in which the 
                                  feature was created.
                                  */
);


/******************************************************************
Queries the given distance expression feature and returns its object
references and transforms

See Also: 
 UF_GEXP_create_distance
 UF_GEXP_edit_distance

Environment: Internal  and  External
History: This function was originally released in V15.0.
 ******************************************************************/
extern UFUNEXPORT int UF_GEXP_ask_distance_parms (
    tag_t feature_tag,              /* <I>
                                    Tag of distance expression feature to query.
                                    */
    tag_t *ref1,                    /* <O>
                                    Tag of first referenced object
                                    */
    tag_t *xform1,                  /* <O>
                                    Tag of transformation for first object. 
                                    The transformation is NULL_TAG for objects 
                                    in the same part in which the feature was 
                                    created.
                                    */
    tag_t *ref2,                    /* <O>
                                    Tag of second referenced object
                                    */
    tag_t *xform2                   /* <O>
                                    Tag of transformation for second object. 
                                    The transformation is NULL_TAG for objects 
                                    in the same part in which the feature was 
                                    created.
                                    */
);


/******************************************************************
Queries the given angle geometric expression feature and returns the
referenced objects, transforms and qualifiers.

See Also: 
 UF_GEXP_edit_angle
 UF_GEXP_create_angle
 UF_GEXP_qualifier_t

Environment: Internal  and  External
History: This function was originally released in V15.0.
 ******************************************************************/
extern UFUNEXPORT int UF_GEXP_ask_angle_parms (
    tag_t feature_tag,                 /* <I>
                                       Tag of angle expression feature to query.
                                       */ 
    tag_t *object1,                    /* <O> 
                                       Tag of referenced object 1 the angle was
                                       created from
                                       */
    UF_GEXP_qualifier_t *qualifier1,   /* <O>
                                       Qualifier for object1, only applicable 
                                       to lines and edges.
                                       */
    tag_t *xform1,                     /* <O>
                                       Tag of transformation for first object; 
                                       if the object is in the same part the 
                                       feature was created in, this would be 
                                       NULL_TAG.
                                       */
    tag_t *object2,                    /* <O>
                                       Tag of referenced object 2 the angle 
                                       was created from.
                                       */  
    UF_GEXP_qualifier_t *qualifier2,   /* <O>
                                       Qualifier for object2, only applicable 
                                       to lines and edges.
                                       */
    tag_t *xform2                      /* <O>
                                       Tag of transformation for second object.
                                       This tag is NULL_TAG if the object is 
                                       in the same part in which the feature 
                                       was created.
                                       */
);

#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif /* UF_GEXP_H_INCLUDED */
