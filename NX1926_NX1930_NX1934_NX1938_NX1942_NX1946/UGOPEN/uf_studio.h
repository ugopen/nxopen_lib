/*===========================================================================

           Copyright (c) 1998-2005 Unigraphics Solutions Inc.
                         Unpublished - All rights reserved

=============================================================================

 

File description:

    User Function declaration (Open C API) for Shape Studio Freeform.
    Including:
        Styled Blend

===========================================================================*/

#ifndef UF_STUDIO_INCLUDED
#define UF_STUDIO_INCLUDED

/*  */

#include <uf_defs.h>
#include <uf_modl_types.h>
#include <libufun_exports.h>

#ifdef __cplusplus
extern "C" {
#endif

/***************************************************************************

    Styled Blend

***************************************************************************/


/*
  The following are enum and struct types used for UF_STUDIO_styled_blend.
  All types and all enum entries are prefixed by UF_STUDIO_stybld.
*/

/* Method choices for tangent holding curve creation.

*/
enum UF_STUDIO_stybld_method_e
{
   UF_STUDIO_stybld_method_curves = 0,
   UF_STUDIO_stybld_method_law,
   UF_STUDIO_stybld_method_profile
};
typedef enum UF_STUDIO_stybld_method_e UF_STUDIO_stybld_method_t;

/* Transition choices for law-controlled tangent holding curves, and
   for depth and skew of the blend surface.

*/
enum UF_STUDIO_stybld_trans_e
{
   UF_STUDIO_stybld_trans_constant = 0,
   UF_STUDIO_stybld_trans_linear,
   UF_STUDIO_stybld_trans_non_inflecting,
   UF_STUDIO_stybld_trans_s_shaped
};
typedef enum UF_STUDIO_stybld_trans_e UF_STUDIO_stybld_trans_t;

/* Continuity choices for smoothness between walls and blend surface.

*/
enum UF_STUDIO_stybld_cont_e
{
   UF_STUDIO_stybld_cont_tangent = 0,
   UF_STUDIO_stybld_cont_curvature,
   UF_STUDIO_stybld_cont_g3,
   UF_STUDIO_stybld_cont_position
};
typedef enum UF_STUDIO_stybld_cont_e UF_STUDIO_stybld_cont_t;

/* Direction choices for flow direction.

*/
enum  UF_STUDIO_stybld_direct_e
{
   UF_STUDIO_stybld_direct_no_specific = 0,
   UF_STUDIO_stybld_direct_perpendicular,
   UF_STUDIO_stybld_direct_iso_u,
   UF_STUDIO_stybld_direct_iso_v
};
typedef enum  UF_STUDIO_stybld_direct_e UF_STUDIO_stybld_direct_t;

/* Stiffness choices for blend surface.

*/
enum UF_STUDIO_stybld_stiff_e
{
   UF_STUDIO_stybld_stiff_auto = 0,
   UF_STUDIO_stybld_stiff_low
};
typedef enum UF_STUDIO_stybld_stiff_e UF_STUDIO_stybld_stiff_t;

/* Trim choices.

*/
enum UF_STUDIO_stybld_trim_e
{
   UF_STUDIO_stybld_trim_attach_all = 0,
   UF_STUDIO_stybld_trim_no,
   UF_STUDIO_stybld_trim_input_walls,
   UF_STUDIO_stybld_trim_input_blends
};
typedef enum UF_STUDIO_stybld_trim_e UF_STUDIO_stybld_trim_t;

/* Minimum radius choices.

*/
enum UF_STUDIO_stybld_minrad_e
{
   UF_STUDIO_stybld_minrad_none = 0,
   UF_STUDIO_stybld_minrad_bound,
   UF_STUDIO_stybld_minrad_peak
};
typedef enum UF_STUDIO_stybld_minrad_e UF_STUDIO_stybld_minrad_t;

/* Lofting degree choices (degree in v-direction).

*/
enum UF_STUDIO_stybld_v_degree_e
{
   UF_STUDIO_stybld_v_degree_cubic = 3,
   UF_STUDIO_stybld_v_degree_quintic = 5
};
typedef enum UF_STUDIO_stybld_v_degree_e UF_STUDIO_stybld_v_degree_t;

/* Data structure of shape transition for depth and skew */
struct UF_STUDIO_stybld_shape_trans_s
{
    UF_STUDIO_stybld_trans_t  trans_type; /* Transition type. */
    double start; /* Start value = 0...100. Used for all transition types. */
    double end; /* End value = 0...100. Used for all transition types except constant. */
    double peak; /* Peak value = 0...100. Only used for non_inflecting transition type. */
    double slope; /* Slope value = 0...100. Only used for s-shaped transition type. */
    double position; /* Position of middle value = 10...90. Only used for non_inflecting and
                        s_shaped transition type. */
};
typedef struct UF_STUDIO_stybld_shape_trans_s UF_STUDIO_stybld_shape_trans_t, *UF_STUDIO_stybld_shape_trans_p_t;

/* Data structure of curve transition controlling the shape of tangent holding
   curves.
*/
struct UF_STUDIO_stybld_curve_trans_s
{
    UF_STUDIO_stybld_trans_t  trans_type; /* Transition type.

       Note, depending on the transition, trans_type, only some of the three
       expressions, start, end and peak, are used. All used expresions must
       evaluate to non-negative values, and at least one used expression must
       evaluate to a positive value. */
    char *start; /* Expression string for start value. Used for for all transition types. */
    char *end; /* Expression tag for end value. Used for all transition types except
       constant. */
    char *peak; /* Expression tag for peak value. Only used for non_inflecting transition
       type. */
    double slope; /* Slope value = 0...100. Only used for s-shaped transition type. */
    double position; /* Position of middle value = 10...90. Only used for non_inflecting and
       s_shaped transition type. */
};
typedef struct UF_STUDIO_stybld_curve_trans_s UF_STUDIO_stybld_curve_trans_t, *UF_STUDIO_stybld_curve_trans_p_t;

/* Data structure for styled blend creation and editing. */
struct UF_STUDIO_stybld_data_s
{
    UF_STUDIO_stybld_method_t method; /* Method choice for tangent holding curve creation. */
    int   num_faces1; /* Number of faces for wall 1. */
    tag_t *faces1; /* Array of num_faces1 face tags for wall 1. You may use a single
       face collection as the defintion of the wall.  If you do want to use
       a collection then it must be the only object in the array
       i.e.  num_faces1 == 1 */
    logical reverse_normal1; /* Reverse normal on wall 1. If TRUE, the face normal direction of
       wall 1 will be reversed. In case that method is set to
       UF_STUDIO_stybld_method_law and center_curve is set to NULL
       (automatically generated center curve), the face normal is used to
       determine to which quadrant the blend will be applied. */
    int   num_faces2; /* Number of faces for wall 2. */
    tag_t *faces2; /* Array of num_faces2 face tags for wall 2.
       You may use a single face collection as the defintion of the wall.
       If you do want to use a collection then it must be the only object
       in the array i.e.  num_faces2 == 1.
       If num_faces2 = 1 and faces2[0] is tag of a datum plane, then
       Symmetric Modeling mode is active. */
    logical reverse_normal2; /* Reverse normal on wall 2. If TRUE, the face normal direction of
       wall 2 will be reversed. In case that method is set to
       UF_STUDIO_stybld_method_law and center_curve is set to NULL
       (automatically generated center curve), the face normal is used to
       determine to which quadrant the blend will be applied. */
    logical floating_mode; /* Only used for Symmetric Modeling (see comments for faces2).
       If floating_mode is set to true, no tangent holding line on the datum plane
       needs to be selected (method = UF_STUDIO_stybld_method_curves), or no
       tangent holding line on the datum plane will be created
       (method = UF_STUDIO_stybld_method_law).
       If floating_mode is set to false, a tangent holding line on the datum plane
       must be selected (method = UF_STUDIO_stybld_method_curves), or
       tangent holding line on the datum plane will be created
       (method = UF_STUDIO_stybld_method_law).
    */
    tag_t  edge_1; /* connecting edge of 1st adjacent blend */
    tag_t  edge_2; /* connecting edge of 2nd adjacent blend */
    double trim_1; /* trimming back factor of 1st adjacent blend */
    double trim_2; /* trimming back factor of 2nd adjacent blend */
    UF_STUDIO_stybld_cont_t continuity_blend_1; /* continuity zu 1st blend */
    UF_STUDIO_stybld_cont_t continuity_blend_2; /* continuity zu 2nd blend */
    UF_STRING_p_t spine; /* Pointer to spine string (optional). If set to NULL, no spine is used. */
    UF_STRING_p_t profile_curve; /* Pointer to profile curve string */
    UF_STUDIO_stybld_shape_trans_t depth; /* Depth transition. */
    UF_STUDIO_stybld_shape_trans_t skew; /* Skew transition. */
    double distance_tol; /* Distance tolerance */
    double angle_tol; /* Angle tolerance */
    logical reverse_direction1; /* Reverse direction flag at wall 1. If TRUE, the tangent direction of
       the blend surface at wall 1 will be reversed. */
    logical reverse_direction2; /* Reverse direction flag at wall 2. If TRUE, the tangent direction of
       the blend surface at wall 2 will be reversed. */
    UF_STUDIO_stybld_cont_t continuity1; /* Continuity between blend surface and  wall 1. */
    UF_STUDIO_stybld_cont_t continuity2; /* Continuity between blend surface and  wall 2.
       Not used for Symmetric Modeling (see comments for faces2). */
    UF_STUDIO_stybld_direct_t direction1; /* Flow direction of blend surface at wall 1. */
    UF_STUDIO_stybld_direct_t direction2; /* Flow direction of blend surface at wall 2.
       Not used for Symmetric Modeling (see comments for faces2). */
    UF_STUDIO_stybld_stiff_t stiffness; /* Stiffness choice for blend surface. Only used if continuity1 and
       continuity2 are set to UF_STUDIO_stybld_cont_curvature, or, in case
       of Symmetric Modeling (see comments for faces2), if continuity1 is
       set to UF_STUDIO_stybld_cont_curvature . */
    UF_STUDIO_stybld_trim_t trim; /* Trim choice.
       Not used for Symmetric Modeling (see comments for faces2). */
    UF_STRING_p_t curve1; /* Pointer to string for tangent holding curve 1.
       Only used if method is set to UF_STUDIO_stybld_method_curves. */
    UF_STRING_p_t curve2; /* Pointer to string for tangent holding curve 2.
       Only used if method is set to UF_STUDIO_stybld_method_curves.
       Not used for Symmetric Modeling (see comments for faces2) with
       floating_mode set to true. */
    UF_STUDIO_stybld_curve_trans_t curve_trans1; /* Transition controlling the shape of tangent holding curve 1.
       Only used if method is set to UF_STUDIO_stybld_method_law. */
   UF_STUDIO_stybld_curve_trans_t curve_trans2; /* Transition controlling the shape of tangent holding curve 2.
       Only used if method is set to UF_STUDIO_stybld_method_law.
       Not used for Symmetric Modeling (see comments for faces2) with
       floating_mode set to true. */
    UF_STRING_p_t center_curve; /* Pointer to string for center curve (optional). Only used if method is
       set to UF_STUDIO_stybld_method_curves. In this case, if pointer is set
       to NULL, the intersection curve between wall 1 and wall 2 is used as
       center curve, if feasible. */
    logical reverse_center_curve; /* Reverse center curve flag is only used if method is set to
       UF_STUDIO_stybld_method_law and if the center_curve is set to NULL,
       i.e., the center curve is automatically generated. If TRUE, the
       direction of the intersection curve between wall 1 and wall 2 will be
       reversed. */
    int center_as_spine;
    double start_extension; /* Extension at start point of center curve is only used if method is set
       to UF_STUDIO_stybld_method_law. start_extension = -50...50. If the
       value is positive, the center curve will be extended linearly by
       start_extension/100 * arclength of the center curve. If the value is
       negative, the center curve will be shortened by start_extension/100 *
       length of parameter range of the center curve. */
    double end_extension; /* Extension at end point of center curve is only used if method is set
       to UF_STUDIO_stybld_method_law. end_extension = -50...50. If the
       value is positive, the center curve will be extended linearly by
       end_extension/100 * arclength of the center curve. If the value is
       negative, the center curve will be shortened by end_extension/100 *
       length of parameter range of the center curve. */
    UF_STUDIO_stybld_minrad_t min_radius_mode; /* Minimum Radius mode.
       UF_STUDIO_stybld_minrad_none:  No minimum radius constraint,
       UF_STUDIO_stybld_minrad_bound: Sections of blend should not exceed
                                      min_radius value,
       UF_STUDIO_stybld_minrad_peak:  Midpoint of sections assumes min_radius
                                      value. */
    char *min_radius; /* Minimum radius value >= 0. */
    UF_STUDIO_stybld_v_degree_t v_degree; /* Lofting degree choice. Degree of blend surface in v-direction can be
       cubic or quintic. */

};
typedef struct UF_STUDIO_stybld_data_s UF_STUDIO_stybld_data_t, *UF_STUDIO_stybld_data_p_t;

/* Functions for styled blend feature.*/

/******************************************************************************
Allocates and initializes the styled blend data structure. It is to
be used in conjunction with UF_STUDIO_create_styled_blend,
UF_STUDIO_edit_styled_blend and UF_STUDIO_ask_styled_bend.

Environment: Internal  and  External
See Also: UF_STUDIO_create_styled_blend
          UF_STUDIO_edit_styled_blend
          UF_STUDIO_ask_styled_bend
          UF_STUDIO_free_styled_bend
History: Original release in V18.0.
******************************************************************************/

extern UFUNEXPORT int UF_STUDIO_init_styled_blend(
UF_STUDIO_stybld_data_p_t *styled_blend_data /* <O> Styled blend data structure. */
);

/******************************************************************************
Frees memory of the styled blend data structure that was previously
allocated with UF_STUDIO_init_styled_blend.

Environment: Internal  and  External
See Also: UF_STUDIO_init_styled_blend
History: Original release in V18.0.
******************************************************************************/

extern UFUNEXPORT int UF_STUDIO_free_styled_blend(
UF_STUDIO_stybld_data_p_t *styled_blend_data /* <I/O> Styled blend data structure. */
);

/******************************************************************************
Creates a styled blend feature from the styled blend data
structure.

Environment: Internal  and  External
See Also: UF_STUDIO_init_styled_blend
          UF_STUDIO_edit_styled_blend
          UF_STUDIO_ask_styled_bend
History: Original release in V18.0.
******************************************************************************/

extern UFUNEXPORT int UF_STUDIO_create_styled_blend(
UF_STUDIO_stybld_data_p_t styled_blend_data, /* <I> Styled blend data structure. */
tag_p_t styled_blend  /* <O> Styled blend feature object identifier. */
);

/******************************************************************************
Edits an existing styled blend feature based on a styled blend data structure.

Environment: Internal  and  External
See Also: UF_STUDIO_init_styled_blend
          UF_STUDIO_create_styled_blend
          UF_STUDIO_ask_styled_bend
History: Original release in V18.0.
******************************************************************************/

extern UFUNEXPORT int UF_STUDIO_edit_styled_blend(
UF_STUDIO_stybld_data_p_t styled_blend_data, /* <I> Styled blend data structure. */
tag_t styled_blend  /* <I/O> Styled blend feature object identifier. */
);


/******************************************************************************
Populates a styled blend data structure of a styled blend feature.

Environment: Internal  and  External
See Also: UF_STUDIO_init_styled_blend
          UF_STUDIO_create_styled_blend
          UF_STUDIO_edit_styled_bend

History: Original release in V18.0.
******************************************************************************/

extern UFUNEXPORT int UF_STUDIO_ask_styled_blend(
tag_t styled_blend,  /* <I> Styled blend feature object identifier. */
UF_STUDIO_stybld_data_p_t styled_blend_data /* <O> Styled blend data structure. */
);


/******************************************************************************
Populates a collector enabled styled blend data structure of a
styled blend feature.

Environment: Internal  and  External
See Also: UF_STUDIO_init_styled_blend
          UF_STUDIO_create_styled_blend
          UF_STUDIO_edit_styled_bend

History: Original release in NX2.0
******************************************************************************/

extern UFUNEXPORT int UF_STUDIO_ask_styled_blend1(
tag_t styled_blend,  /* <I> Styled blend feature object identifier. */
UF_STUDIO_stybld_data_p_t styled_blend_data /* <O> Styled blend data structure. */
);

/* end Styled Blend */

#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif /* UF_STUDIO_H_INCLUDED */
