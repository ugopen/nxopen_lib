/*==================================================================================================

            Copyright (c) 2012 Siemens Product Lifecycle Management Software Inc.
                            Unpublished - All rights reserved


====================================================================================================*/

#ifndef UF_SF_CURVE_INCLUDED
#define UF_SF_CURVE_INCLUDED

#include <uf_defs.h>
#include <uf_curve.h>
#include <libufun_cae_exports.h>

#ifdef __cplusplus
extern "C" {
#endif

/******************************************************************************
Create a smart/dumb line/arc in fem/sim part. You input a UF_CURVE_line_arc_t data structure,
which specified the data needed for the line/arc to be created. Output is the
object identifier of the smart/dumb line/arc. An error is returned if
line/arc cannot be created with the specified data.

Return: error code

Environment: Internal  and  External

History:
******************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_CURVE_create_line_arc
(
    UF_CURVE_line_arc_t  *line_arc_data, /* <I> Pointer to line/arc data structure */
    tag_t * curve_id  /* <O> Object identifier of new associative line/arc in fem/sim.
                             if is_asso == TRUE - smart line/arc.
                             if is_asso == FALSE - dumb line/arc  */
);

/******************************************************************************
Create a smart/dumb line through two points in fem/sim part.

Return: error code

Environment: Internal  and  External

History:
******************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_CURVE_create_line_point_point
(
    tag_t point1, /* <I> tag of start point */
    tag_t point2, /* <I> tag of end point */
    UF_CURVE_limit_p_t limit_p[2], /* <I> extension limits */
    tag_t support_plane, /* <I> tag of support plane of the line */
    logical is_asso, /* <I> true - if associative, false - if not associative */
    tag_p_t line_feature_id /* <O> if is_asso == TRUE - object identifier of new smart line
                                   if is_asso == FALSE - object identifier of new dumb line */
);
/******************************************************************************
Create a smart/dumb arc through three points in fem/sim part.

Return: error code

Environment: Internal  and  External

History:
******************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_CURVE_create_arc_3point
(
    tag_t point1, /* <I> tag of start point */
    tag_t point2, /* <I> tag of end point */
    tag_t point3, /* <I> tag of middle point */
    UF_CURVE_limit_p_t limit_p[2], /* <I> extension limits */
    tag_t support_plane, /* <I> tag of support plane of the arc */
    logical is_asso, /* <I> true - if associative, false - if not associative */
    tag_p_t arc_id /* <O> if is_asso == TRUE - smart arc
                          if is_asso == FALSE - dumb arc arc */
);
/******************************************************************************
Create a smart/dumb arc through two points and of specific radius in fem/sim part.

Return: error code

Environment: Internal  and  External

History:
******************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_CURVE_create_arc_point_point_radius
(
    tag_t point1, /* <I> tag of start point */
    tag_t point2, /* <I> tag of end point */
    double radius, /* <I> value of radius */
    UF_CURVE_limit_p_t limit_p[2], /* <I> extension limits */
    tag_t support_plane, /* <I> tag of support plane of the arc */
    logical is_asso, /* <I> true - if associative, false - if not associative */
    tag_p_t arc_feature_id/* <O> if is_asso == TRUE - object identifier of new smart arc feature
                                 if is_asso == FALSE - object identifier of new dumb arc */
);
/******************************************************************************
Create a smart/dumb arc through a start point and specific center in fem/sim part.

Return: error code

Environment: Internal  and  External
History:
******************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_CURVE_create_arc_point_center
(
    tag_t point, /* <I> tag of start point */
    tag_t center, /* <I> tag of center */
    UF_CURVE_limit_p_t limit_p[2], /* <I> extension limits */
    tag_t support_plane, /* <I> tag of support plane of the arc */
    logical is_asso, /* <I> true - if associative, false - if not associative */
    tag_p_t arc_id /* <O> if is_asso == TRUE - object identifier of new smart arc
                          if is_asso == FALSE - object identifier of new dumb arc */
);
/******************************************************************************
Create a smart/dumb arc of given radius and specific center in fem/sim part.

Return: error code

Environment: Internal  and  External

History:
******************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_CURVE_create_arc_center_radius
(
    tag_t center, /* <I> tag of center */
    double radius, /* <I> value of radius */
    tag_t help_point, /* <I> point to define the start orientation */
    UF_CURVE_limit_p_t limit_p[2], /* <I> extension limits */
    tag_t support_plane, /* <I> tag of support plane of the arc */
    logical is_asso, /* <I> true - if associative, false - if not associative */
    tag_p_t arc_id /* <O> if is_asso == TRUE - object identifier of new smart arc
                          if is_asso == FALSE - object identifier of new dumb arc */
);

#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#include <uf_sf_retiring.h>

#endif    /*  END UF_CURVE_INCLUDED  */
