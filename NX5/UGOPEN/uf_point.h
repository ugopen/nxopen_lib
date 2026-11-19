/*==================================================================================================
                    Copyright 2005 UGS Corp.  
                      All Rights Reserved.
====================================================================================================


File Description:

User functions for associative point creation
This file provides routines that enable you to create associative point.
Using the subroutines in this file, you can:
 . Create an associative point on curve.
 . Create an associative point with offset.
 . Create an associative point at conic center.
 . Create an associative point on surface.
 . Create an associative point with 3 scalars.
 . Create an associative point on arc angle.
 . Create an associative point along curve.
 . Create an associative point surface curve intersection.
 . Ask the point tag from an associative point feature.
==================================================================================================*/

#ifndef UF_POINT_H_INCLUDED
#define UF_POINT_H_INCLUDED

#include <uf_defs.h>
#include <uf_disp.h>
#include <uf_so.h>
#include <libufun_exports.h>

#ifdef __cplusplus
extern "C" {
#endif

/******************************************************************************
Creates an associative point on curve at scalar value t.

Environment: Internal and External

See Also:  UF_POINT_ask_point_output

History:
******************************************************************************/
extern UFUNEXPORT int UF_POINT_create_on_curve(
    const tag_t curve, /* <I> object id of curve */
    const tag_t t, /* <I> object id of scalar */
    tag_p_t point_feature_id /* <O> object id of point feature */  
    );

/******************************************************************************
Creates an associative point with a offset to the point.

Environment: Internal  and  External

See Also:  UF_POINT_ask_point_output

History:
******************************************************************************/
extern UFUNEXPORT int UF_POINT_create_with_offset(
    const tag_t base_point, /* <I> object id of Base point to offset */
    const tag_t offset, /* <I> object id of offset */
    tag_p_t point_feature_id /* <O> object id of point feature */
    );

/******************************************************************************
Creates an associative point at the center of a conic.

Environment: Internal  and  External

See Also:  UF_POINT_ask_point_output

History:
******************************************************************************/
extern UFUNEXPORT int UF_POINT_create_at_conic_center(
    const tag_t conic, /* <I> object id of conic */
    tag_p_t point_feature_id /* <O> object id of point feature */                        
    );
/******************************************************************************
Creates an associative point at intersection of two curves.

Environment: Internal  and  External

See Also:  UF_POINT_ask_point_output

History:
******************************************************************************/
extern UFUNEXPORT int UF_POINT_create_at_intersection_of_two_curves(
    const tag_t curve1, /* <I> object id of first curve */
    const tag_t curve2, /* <I> object id of second curve */
    const tag_t help_point1, /* <I> object id of help point on first curve */
    const tag_t help_point2, /* <I> object id of help point on second curve */
    tag_p_t point_feature_id /* <O> object id of point feature */                          
    );

/******************************************************************************
Creates an associative point on a surface at uv scalars for the surface. 

Note the u,v parameters are normalized from 0 to 1, so if you have read
surface parameters with UF_MODL_ask_face_parms, or UF_MODL_ask_face_uv_minmax,
you will have to normalize the parameters to the range of 0 to 1 prior to 
creating an associative point on the surface.

Environment: Internal  and  External

See Also:  UF_POINT_ask_point_output

History:
******************************************************************************/
extern UFUNEXPORT int UF_POINT_create_on_surface(
    const tag_t surface, /* <I> object id of surface */
    const tag_t u, /* <I> object id of u scalar parameter */
    const tag_t v, /* <I> object id of v scalar parameter */
    tag_p_t point_feature_id /* <O> object id of point feature */                        
    );
/******************************************************************************
Creates an associative point with three scalars.
Return: error code

Environment: Internal  and  External

See Also:  UF_POINT_ask_point_output

History:
******************************************************************************/
extern UFUNEXPORT int UF_POINT_create_3_scalars(
    const tag_t xyz[3], /* <I> Array of object ids of x,y, and z scalars */
    tag_p_t point_feature_id /* <O> object id of point feature */                        
    );
/******************************************************************************
Creates an associative point on arc at an angle.

Environment: Internal  and  External

See Also:  UF_POINT_ask_point_output

History:
******************************************************************************/
extern UFUNEXPORT int UF_POINT_create_on_arc_angle(
    const tag_t arc, /* <I> object id of arc */
    const tag_t angle, /* <I> object id of angle in radians */
    const tag_t xform, /* <I> object id of optional transform */
    tag_p_t point_feature_id /* <O> object id of point feature */                        
    );
/******************************************************************************
Creates an associative point along curve using a curve with base point and t (scalar
offset along curve). This point is derived by finding the closest point
on the given curve to the given base point and then offsetting this point
along the given curve by the arc length defined by t at absolute
distance or relative percent.

Environment: Internal  and  External

See Also:  UF_POINT_ask_point_output

History:
******************************************************************************/
extern UFUNEXPORT int UF_POINT_create_along_curve(
    const tag_t curve, /* <I> object id of curve or edge */
    const tag_t base_point, /* <I> object id of base point */
    const tag_t t, /* <I> object id of scalar offset along curve */
    const UF_SO_point_along_curve_option_t option, /* <I> Absolute/Relative offset option.
                                                          Can be one of the following enumerated constants:
                                                   UF_SO_point_along_curve_distance
                                                   UF_SO_point_along_curve_percent
                                                   */
    const logical flip, /* <I> If flip is set to TRUE, then t = -t */
    tag_p_t point_feature_id /* <O> object id of point feature */                        
    );
/******************************************************************************
Creates an associative point with surface and curve intersection

Environment: Internal  and  External

See Also:  UF_POINT_ask_point_output

History:
******************************************************************************/
extern UFUNEXPORT int UF_POINT_create_surface_curve_intersection(
    const tag_t surface, /* <I> object id of surface */
    const tag_t curve, /* <I> object id of curve or edge */
    const tag_t help_point1, /* <I> object id of help point on surface */
    const tag_t help_point2, /* <I> object id of help point on curve */
    tag_p_t point_feature_id /* <O> object id of point feature */                        
    );

/******************************************************************************
Ask the point tag from an associative point feature.

Environment: Internal  and  External

See Also:

History:
******************************************************************************/
extern UFUNEXPORT int UF_POINT_ask_point_output
(
    tag_t  point_feature_id,  /* <I> Object id of associative point feature. */
    tag_t  *point_id          /* <O> Object id of the point created by the feature. */
);


#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif /* END UF_POINT_H_INCLUDED */
