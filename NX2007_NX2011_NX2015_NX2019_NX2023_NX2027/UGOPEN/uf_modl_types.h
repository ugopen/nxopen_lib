/*******************************************************************************
             Copyright (c) 1998-2004 Unigraphics Solutions Inc.
                       Unpublished - All Rights Reserved



File description:
    Contains Open API typedefs for modeling.

*****************************************************************************/

#ifndef UF_MODL_TYPES_H_INCLUDED
#define UF_MODL_TYPES_H_INCLUDED

#ifdef USE_PRAGMA_ONCE
#pragma once
#endif

/***************************************************************************

  ***************************************************************************/


#include <uf_defs.h>

#ifdef __cplusplus
extern "C" {
#endif

/***************************************************************************
 *         Limit definitions
 *
 *  UF_MAX_EXP_LENGTH is being deprecated because NX is moving to support
 *  multibyte characters.  User written programs should start using the
 *  new definitions for expressions:
 *    UF_MAX_EXP_BUFSIZE should be used for buffer allocations and memory
 *                      allocations, e.g. char my_exp[UF_MAX_EXP_BUFSIZE];
 *    UF_MAX_EXP_NCHARS  should be used to limit the number of characters in
 *                      a buffer.  NX code will enforce these limits.
 *  New routines have been added which will help in this transition:
 *     UF_TEXT_count_characters() will count the number of characters in a
 *     buffer.
 *     UF_TEXT_terminate_chars() will terminate a C string after the given
 *     number of characters.  
 */

#define UF_MAX_EXP_NCHARS    1024
#define UF_MAX_EXP_BUFSIZE   NX_BUFSIZE(UF_MAX_EXP_NCHARS)
#define UF_MAX_EXP_LENGTH    (UF_MAX_EXP_BUFSIZE-1)

#define UF_MODL_FLAT_TOPOLOGY           1   /* UF_MODL_ask_face_topology */
#define UF_MODL_CYLINDRICAL_TOPOLOGY    2   /* UF_MODL_ask_face_topology */
#define UF_MODL_CONICAL_TOPOLOGY        3   /* UF_MODL_ask_face_topology */
#define UF_MODL_SPHERICAL_TOPOLOGY      4   /* UF_MODL_ask_face_topology */
#define UF_MODL_TOROIDAL_TOPOLOGY       5   /* UF_MODL_ask_face_topology */

/*
   A Surface Parameter (space) curve, or SP-curve represents a 3-space
       curve as a curve in the parameter space of the surface.
*/
#define UF_MODL_LINEAR_EDGE             3001    /* UF_MODL_ask_edge_type */
#define UF_MODL_CIRCULAR_EDGE           3002    /* UF_MODL_ask_edge_type */
#define UF_MODL_ELLIPTICAL_EDGE         3003    /* UF_MODL_ask_edge_type */
#define UF_MODL_INTERSECTION_EDGE       3004    /* UF_MODL_ask_edge_type */
#define UF_MODL_SPLINE_EDGE             3005    /* UF_MODL_ask_edge_type */
#define UF_MODL_SP_CURVE_EDGE           3006    /* UF_MODL_ask_edge_type */
#define UF_MODL_FOREIGN_EDGE            3007    /* UF_MODL_ask_edge_type */
#define UF_MODL_CONST_PARAMETER_EDGE    3008    /* UF_MODL_ask_edge_type */
#define UF_MODL_TRIMMED_CURVE_EDGE      3009    /* UF_MODL_ask_edge_type */
#define UF_MODL_CONVERGENT_EDGE        100007    /* UF_MODL_ask_edge_type */

#define UF_MODL_SOLID_BODY              5601    /* UF_MODL_ask_body_type */
#define UF_MODL_SHEET_BODY              5602    /* UF_MODL_ask_body_type */

#define UF_MODL_NON_PERIODIC             0   /* UF_MODL_ask_face_periodic */
#define UF_MODL_PERIODIC                 1   /* UF_MODL_ask_face_periodic */
#define UF_MODL_BOTH_X_PERIODIC         -2   /* UF_MODL_ask_face_periodic */
#define UF_MODL_MIN_X_PERIODIC          -3   /* UF_MODL_ask_face_periodic */
#define UF_MODL_MAX_X_PERIODIC          -4   /* UF_MODL_ask_face_periodic */

#define UF_MODL_OPEN_CURVE               0  /* UF_MODL_ask_curve_periodicity*/
#define UF_MODL_CLOSED_PERIODIC_CURVE    1  /* UF_MODL_ask_curve_periodicity*/
#define UF_MODL_CLOSED_NON_PERIODIC_CURVE  2  /* UF_MODL_ask_curve_periodicity*/

#define UF_MODL_LOC                      0   /* UF_MODL_evaluate_curve */
#define UF_MODL_LOC_1STDERV              1   /* UF_MODL_evaluate_curve */
#define UF_MODL_LOC_1STDERV_2NDDERV      2   /* UF_MODL_evaluate_curve */

#define UF_MODL_EVAL                     0   /* UF_MODL_evaluate_face */
#define UF_MODL_EVAL_DERIV1              1   /* UF_MODL_evaluate_face */
#define UF_MODL_EVAL_DERIV2              2   /* UF_MODL_evaluate_face */
#define UF_MODL_EVAL_DERIV3              3   /* UF_MODL_evaluate_face */
#define UF_MODL_EVAL_UNIT_NORMAL         10  /* UF_MODL_evaluate_face */
#define UF_MODL_EVAL_NORMAL              11  /* UF_MODL_evaluate_face */
#define UF_MODL_EVAL_ALL                 33  /* UF_MODL_evaluate_face */

#define UF_MODL_POINT                   0  /* UF_MODL_ask_obj_dimensionality */
#define UF_MODL_LINEAR                  1  /* UF_MODL_ask_obj_dimensionality */
#define UF_MODL_PLANAR                  2  /* UF_MODL_ask_obj_dimensionality */
#define UF_MODL_THREE_DIMENSIONAL       3  /* UF_MODL_ask_obj_dimensionality */

#define UF_MODL_EDGE                     0   /* UF_MODL_cr_rel_dplane/daxis */
#define UF_MODL_MID_POINT                1   /* UF_MODL_cr_rel_dplane/daxis */
#define UF_MODL_END_POINT                2   /* UF_MODL_cr_rel_dplane/daxis */
#define UF_MODL_RIGHT_END_POINT          3   /* UF_MODL_cr_rel_dplane/daxis */
#define UF_MODL_LEFT_END_POINT           4   /* UF_MODL_cr_rel_dplane/daxis */

#define       UF_MODL_BLEND_NO_OVERFLOW       0  /* <YS> */
#define       UF_MODL_BLEND_SMOOTH_OVERFLOW   1
#define       UF_MODL_BLEND_CLIFF_OVERFLOW    1
#define       UF_MODL_BLEND_NOTCH_OVERFLOW    1

#define UF_MODL_ALONG_NORMAL 0
#define UF_MODL_OPPOSITE_NORMAL 1
#define UF_MODL_PATCH_HOLE 2
#define UF_MODL_TORUS_TYPE            4005   /* UF_MODL_ask_face_torus_type */
#define UF_MODL_NOT_A_TORUS             -1   /* UF_MODL_ask_face_torus_type */
#define UF_MODL_DOUGHNUT_TORUS           1   /* UF_MODL_ask_face_torus_type */
#define UF_MODL_APPLE_TORUS              2   /* UF_MODL_ask_face_torus_type */
#define UF_MODL_LEMON_TORUS              3   /* UF_MODL_ask_face_torus_type */
#define UF_MODL_OSCULATING_APPLE_TORUS   4   /* UF_MODL_ask_face_torus_type */

#define UF_MODL_CYLINDRICAL_FACE        16   /* UF_MODL_ask_face_type */
#define UF_MODL_CONICAL_FACE            17   /* UF_MODL_ask_face_type */
#define UF_MODL_SPHERICAL_FACE          18   /* UF_MODL_ask_face_type */
#define UF_MODL_TOROIDAL_FACE           19   /* UF_MODL_ask_face_type */
#define UF_MODL_SWEPT_FACE              20   /* UF_MODL_ask_face_type */
#define UF_MODL_PLANAR_FACE             22   /* UF_MODL_ask_face_type */
#define UF_MODL_BLENDING_FACE           23   /* UF_MODL_ask_face_type */
#define UF_MODL_PARAMETRIC_FACE         43   /* UF_MODL_ask_face_type */
#define UF_MODL_OFFSET_FACE             65   /* UF_MODL_ask_face_type */
#define UF_MODL_FOREIGN_FACE            66   /* UF_MODL_ask_face_type */
#define UF_MODL_CONVERGENT_FACE          67   /* UF_MODL_ask_face_type */

#define UF_MODL_ALONG_FIXED_VECTOR       0   /* UF_MODL_***_quilt */
#define UF_MODL_ALONG_DRIVER_NORMALS     1   /* UF_MODL_***_quilt */

#define UF_MODL_MESH_OF_CURVES_DRIVER    0   /* UF_MODL_***_quilt */
#define UF_MODL_B_SURFACE_DRIVER         1   /* UF_MODL_***_quilt */
#define UF_MODL_SELF_REFIT_DRIVER        2   /* UF_MODL_***_quilt */

#define CSYS_TO_CSYS   2

#define UF_MODL_FIXED_LENGTH            0
#define UF_MODL_FULL_THREAD             1
#define UF_MODL_RIGHT_HAND              1
#define UF_MODL_LEFT_HAND               2
#define UF_MODL_NO_INSTANCES            0
#define UF_MODL_INCL_INSTANCES          1
#define UF_MODL_TAPERED                 1
#define UF_MODL_NON_TAPERED             0

/* Qualifier flags for UF_MODL_create_rpo_constraints */
#define UF_MODL_ARC_CENTER             (0)
#define UF_MODL_ARC_TANGENT            (1)
#define UF_MODL_ENDPOINT_1             (2)
#define UF_MODL_ENDPOINT_2             (3)
#define UF_MODL_HORZ_CENTERLINE_PNT_1  (4)
#define UF_MODL_HORZ_CENTERLINE_PNT_2  (5)
#define UF_MODL_VERT_CENTERLINE_PNT_1  (6)
#define UF_MODL_VERT_CENTERLINE_PNT_2  (7)

/* Qualifier flags for UF_MODL_replace_feat_strings */
#define UF_MODL_STRING_ADD             (0)
#define UF_MODL_STRING_REMOVE          (1)
#define UF_MODL_STRING_REPLACE         (2)

/* Constants returned by UF_MODL_compare_topology */

#define COMPARE_COMPLETED            0
#define COMPARE_UNSUITABLE_OBJECTS   1
#define COMPARE_OBJECT_NOT_ALIVE     2
#define COMPARE_UNABLE_TO_FACET      3

#define COMPARE_NOMATCH              0
#define COMPARE_FACES_IDENTICAL      1
#define COMPARE_FACES_EQUIVALENT     2
#define COMPARE_SURFACES_IDENTICAL   3
#define COMPARE_SURFACES_EQUIVALENT  4
#define COMPARE_EDGES_IDENTICAL      5
#define COMPARE_EDGES_EQUIVALENT     6
#define COMPARE_CURVES_IDENTICAL     7
#define COMPARE_CURVES_EQUIVALENT    8


enum UF_MODL_hole_type_e
{
     UF_SIMPLE_HOLE,
     UF_COUNTER_BORE_HOLE,
     UF_COUNTER_SUNK_HOLE
} ;

typedef enum UF_MODL_hole_type_e UF_MODL_hole_type_e_t;

enum UF_MODL_slot_type_e
{
     UF_RECTANGULAR_SLOT,
     UF_BALL_END_SLOT,
     UF_U_SLOT,
     UF_T_SLOT,
     UF_DOVE_TAIL_SLOT
} ;

typedef enum UF_MODL_slot_type_e UF_MODL_slot_type_e_t;

struct UF_MODL_features_s
{
    int         feat_count;
    tag_t       *feat_tags; /* <len:feat_count> */
    char        feat_type[ MAX_LINE_BUFSIZE ];
} ;

typedef struct UF_MODL_features_s UF_MODL_features_t,
*UF_MODL_features_p_t;

struct UF_MODL_SRF_VALUE_s
{
        double    srf_pos[3];         /* Position */


        double    srf_du[3];         /* partial d/du */
        double    srf_dv[3];         /* partial d/dv  */

        double    srf_unormal[3];    /* unit normal */


        double    srf_d2u[3];        /* Second order partials */
        double    srf_dudv[3];       /* Second order partials */
        double    srf_d2v[3];        /* Second order partials */

        double    srf_d3u[3];        /* Third order partials */
        double    srf_d2udv[3];      /* Third order partials */
        double    srf_dud2v[3];      /* Third order partials */
        double    srf_d3v[3];        /* Third order partials */

        double    srf_normal[3];     /* normal, this is not unitized */

} ;

typedef struct UF_MODL_SRF_VALUE_s UF_MODL_SRF_VALUE_t,
*UF_MODL_SRF_VALUE_p_t;

/*
The following codes always appear fixed:
    UF_MODL_STATE_CLOSED
    UF_MODL_STATE_PERIODIC
    UF_MODL_STATE_UNNORMALIZED
    UF_MODL_STATE_CLAMPED
*/

/*

 */
#define UF_MODL_STATE_RANGE_START       0
#define UF_MODL_STATE_CLOSED            0
#define UF_MODL_STATE_PERIODIC          1
#define UF_MODL_STATE_UNNORMALIZED      2
#define UF_MODL_STATE_CLAMPED           3
#define UF_MODL_STATE_DEGENERACY        5
#define UF_MODL_STATE_G1_DISCONTINUITY  6
#define UF_MODL_STATE_SMOOTHED_TO_CN    7
#define UF_MODL_STATE_KNOT_NONC0        8
#define UF_MODL_STATE_KNOT_MULT         9
#define UF_MODL_STATE_KNOT_DECREASING  10
#define UF_MODL_STATE_KNOT_TOOCLOSE    11
#define UF_MODL_STATE_DEGEN_EDGE       13
#define UF_MODL_STATE_SELF_INTERSECT   14
#define UF_MODL_STATE_RANGE_END        49

#define UF_MODL_STATE_IS_FIXED(x) ((x)&1)
#define UF_MODL_STATE_IS_V(x) ((x)&2)

struct UF_MODL_bsurface_s
{
    int num_poles_u;
    int num_poles_v;
    int order_u;
    int order_v;
    int is_rational;
    double *knots_u;
    double *knots_v;
    double (*poles)[4]; /* <len:num_poles_u*num_poles_v> */
} ;

typedef struct UF_MODL_bsurface_s UF_MODL_bsurface_t, *UF_MODL_bsurface_p_t;

#ifndef RATIONAL_UNKNOWN
#define RATIONAL_UNKNOWN        -1
#define RATIONAL_YES            TRUE
#define RATIONAL_NO             FALSE
#endif

/*
    Density units.
*/
enum UF_MODL_density_units_e
{
    UF_MODL_pounds_inches     = 1,
    UF_MODL_pounds_feet       = 2,
    UF_MODL_grams_centimeters = 3,
    UF_MODL_kilograms_meters  = 4
} ;

typedef enum UF_MODL_density_units_e UF_MODL_density_units_t,
*UF_MODL_density_units_p_t;

struct UF_MODL_bsurf_row_info_s
{
    int         num_points;
    double      *points; /* <len:num_points> */
    double      *weight; /* <len:num_points> */
} ;

typedef struct UF_MODL_bsurf_row_info_s UF_MODL_bsurf_row_info_t,
*UF_MODL_bsurf_row_info_p_t;

struct UF_MODL_ray_hit_point_info_s
{
    double      hit_point[3];  /* Point coord where ray hit the target */
    double      hit_normal[3]; /* Normal of the target at the hit point */
    tag_t       hit_face;      /* Face tag at the hit point (tag of prototype) */
    tag_t       hit_body;      /* Body tag at the hit point (tag of original input occurrence ) */
} ;

typedef struct UF_MODL_ray_hit_point_info_s UF_MODL_ray_hit_point_info_t,
*UF_MODL_ray_hit_point_info_p_t;

/* Define the scale types which should correspond to the types
   defined in scale.h */
enum UF_SCALE_TYPE_e{
   UF_SCALE_TYPE_UNIFORM      = 0, /*SCALE_METHOD_UNIFORM,*/
   UF_SCALE_TYPE_AXISYMMETRIC,     /* = SCALE_METHOD_AXISYMMETRIC,*/
   UF_SCALE_TYPE_GENERAL           /*= SCALE_METHOD_GENERAL*/
} ;

typedef enum UF_SCALE_TYPE_e UF_SCALE_TYPE_t;

/* WRAP_GEOMETRY feature
 */
#define UF_WRAP_GEOM_CLOSE_SHARP    (0)
#define UF_WRAP_GEOM_CLOSE_BEVELED  (1)
#define UF_WRAP_GEOM_CLOSE_NONE     (2)

/* Dynamic update */
#define UF_MODL_NO_DYNAMIC_UPDATE          (0)
#define UF_MODL_DYNAMIC_UPDATE_INCREMENTAL (1)
#define UF_MODL_DYNAMIC_UPDATE_CONTINUOUS  (2)
#define UF_MODL_UPDATE_FIRST_LEVEL         (0)
#define UF_MODL_UPDATE_ALL                 (1)

/* Define the data for a wrap geometry feature. */
struct UF_MODL_wrap_geom_s
{
       int     close_gap;         /* Method used to close gaps between
                                     faces after offsetting them.
                                     May be one of:
                                       UF_WRAP_GEOM_CLOSE_SHARP
                                       UF_WRAP_GEOM_CLOSE_BEVELED
                                       UF_WRAP_GEOM_CLOSE_NONE
                                  */
       double  dist_tol;          /* Tolerance used to generate vertices from
                                     geometry. This is also the primary face
                                     offset.
                                  */
       char    *add_offset;       /* Additional offset applied to faces. */
       char    *split_offset;     /* Offset applied to each side of the
                                     splitting plane so that the resulting
                                     bodies overlap and can be united.
                                  */
       int     num_geoms;         /* Number of tags in the geometry array. */
       tag_t   *geometry;         /* <len:num_geoms>Array of geometry tags.  May be solid
                                     bodies, sheet bodies, curves or points.
                                  */
       int     num_splits;        /* Number of tags in the splits array. This
                                     can be zero if no splitting planes are
                                     used.
                                  */
       tag_t   *splits;           /* <len:num_splits>Array of smart planes (xforms) and/or
                                     datum planes to be used to split the
                                     geometry.  This can be NULL if num_splits
                                     is zero.
                                  */
} ;

typedef struct UF_MODL_wrap_geom_s UF_MODL_wrap_geom_t,
                                  *UF_MODL_wrap_geom_p_t;

/* WRAP_ASSEMBLY feature
 */

/* Define the data for a wrap assembly feature. */
struct UF_MODL_wrap_assem_s
{
       int     close_gap;         /* Method used to close gaps between
                                     faces after offsetting them.
                                     May be one of:
                                       UF_WRAP_GEOM_CLOSE_SHARP
                                       UF_WRAP_GEOM_CLOSE_BEVELED
                                       UF_WRAP_GEOM_CLOSE_NONE
                                  */
       double  dist_tol;          /* Tolerance used to generate vertices from
                                     geometry. This is also the primary face
                                     offset.
                                  */
       char    *add_offset;       /* Additional offset applied to faces. */
       char    *split_offset;     /* Offset applied to each side of the
                                     splitting plane so that the resulting
                                     bodies overlap and can be united.
                                  */
       int     num_geoms;         /* Number of tags in the geometry array. */
       tag_t   *geometry;         /* <len:num_geoms> Array of geometry tags.  May be solid
                                     bodies, sheet bodies, curves or points.
                                  */
       tag_t   *geom_xforms;      /* <len:num_geoms>Array of xforms to position each geometry
                                     tag. The transform determines the
                                     position of the linked feature relative to
                                     its source geometry.  Must be NULL_TAG
                                     (apply no transformation) or an
                                     assy_ctxt_xform in the work part.
                                  */
       int     num_splits;        /* Number of tags in the splits array. This
                                     can be zero if no splitting planes are
                                     used.
                                  */
       tag_t   *splits;           /* <len:num_splits>Array of smart planes (xforms) and/or
                                     datum planes to be used to split the
                                     geometry.  This can be NULL if num_splits
                                     is zero.
                                  */
       tag_t   *split_xforms;     /* <len:num_splits>Array of xforms to position each split
                                     (datums only, interpart smart planes are
                                     not allowed). The transform determines the
                                     position of the linked feature relative to
                                     its source geometry.  Must be NULL_TAG
                                     (apply no transformation) or an
                                     assy_ctxt_xform in the work part.
                                     Must be NULL_TAG for each smart plane.
                                  */
} ;

typedef struct UF_MODL_wrap_assem_s UF_MODL_wrap_assem_t,
                                   *UF_MODL_wrap_assem_p_t;

/* Define the data for a linked exterior feature. */
#define UF_LINKED_EXT_GROUP_NONE         (0)
#define UF_LINKED_EXT_GROUP_SINGLE       (1)
#define UF_LINKED_EXT_GROUP_BY_COMPONENT (2)

#define UF_LINKED_HL_RES_COARSE          (0)
#define UF_LINKED_HL_RES_NORMAL          (1)
#define UF_LINKED_HL_RES_FINE            (2)
#define UF_LINKED_HL_RES_VERY_FINE       (3)

#define UF_LINKED_RAY_ALONG_NORMS        (0)
#define UF_LINKED_RAY_ABOVE_NORMS        (1)
#define UF_LINKED_RAY_FROM_POINT         (2)

/* Define the data structure for an Linked Exterior feature. */
struct UF_MODL_linked_ext_s
{
       int     num_bodies;        /* Number of candidate bodies.       */
       tag_t   *bodies;           /* <len:num_bodies> Candidate bodies.                 */
       tag_t   *xforms;           /* <len:num_bodies> Array of xforms. One for each body,
                                     determines the position of the body
                                     relative to its source geometry.
                                     Must be NULL_TAG (apply no transformation) or
                                     an assy_ctxt_xform in the work part.
                                  */
       int     num_faces;         /* Number of tags in the faces array.  */
       tag_t   *faces;            /* <len:num_faces> Array of face tags.                 */
       int     *xform_index;      /* <len:num_faces> Array of indices into xforms array, one index
                                     for each face. Determines the position
                                     of the linked feature relative to its
                                     source geometry.
                                  */
       int group_results;        /* Method used to group resulting sheet bodies.
                                    One of:
                                       UF_LINKED_EXT_GROUP_NONE
                                       UF_LINKED_EXT_GROUP_SINGLE
                                       UF_LINKED_EXT_GROUP_COMPONENT
                                  */
       logical mass_props;       /* If true, calculate mass properties of
                                    all candidate solid bodies.
                                  */
       logical delete_openings;  /* If true, any holes in the resulting sheet are
                                    closed up; if false they are left. Note: A hole
                                    is any interior edge loop without an adjacent
                                    face.
                                  */
       logical at_timestamp;     /* If true, each linked region updates at
                                    a time determined by its creation timestamp.
                                    If false, the linked regions update after their
                                    source faces body is completely generated.
                                    Note: this only applies to the linked regions.
                                    Mass properties are always calcualted after the
                                    body is completely generated
                                  */
};
typedef struct UF_MODL_linked_ext_s UF_MODL_linked_ext_t,
                                    *UF_MODL_linked_ext_p_t;




struct UF_MODL_parent_disp_info_s
{
    tag_t    eid;             /* Parent curve's entity ID */
    int      layer_number;    /* Parent curve's original layer number */
    int      blank_status;    /* Parent curve's original blank status */
    logical  change_status;   /* Change in any display status of parent curve */
};
typedef struct UF_MODL_parent_disp_info_s UF_MODL_disp_info_t,
                                         *UF_MODL_disp_info_p_t;

struct loop_list
{
   int                     type;        /* Peripheral=1, Hole=2, Other=3 */
   uf_list_t               *edge_list;  /* Pointer to the next list of
                                           edge EIDs */
   struct loop_list        *next;       /* Pointer to the next loop */
};
typedef struct loop_list uf_loop_t, *uf_loop_p_t;

enum UF_MODL_SWEEP_TRIM_OPTS
{
    DO_NOT_EXTEND_TRIM_FACE            = 0,
    DO_NOT_EXTEND_AND_EXTEND_TRIM_FACE = 1,
    EXTEND_FIRST_TRIM_FACE             = 2,
    EXTEND_SECOND_TRIM_FACE            = 4,
    EXTEND_BOTH_TRIM_FACES             = 6
};
typedef enum UF_MODL_SWEEP_TRIM_OPTS UF_MODL_SWEEP_TRIM_OPTS;

enum UF_MODL_SWEEP_TRIM_SIGNS
{
    UF_MODL_SWEEP_TRIM_NONE = 0,          /* No trimming */
    UF_MODL_SWEEP_TRIM_TO_FACE = 1,       /* Trim to one Face */
    UF_MODL_SWEEP_TRIM_BETW_TWO_FACES = 2, /* Trim between Faces */
    UF_MODL_SWEEP_TRIM_TO_ALL = 3          /* Trim to All */
};
typedef enum UF_MODL_SWEEP_TRIM_SIGNS UF_MODL_SWEEP_TRIM_SIGN;

enum UF_MODL_boolean_body
{
    UF_MODL_TARGET_BODY = 0,
    UF_MODL_TOOL_BODY   = 1
} ;
typedef enum UF_MODL_boolean_body UF_MODL_boolean_body_e_t;

enum UF_FEATURE_SIGNS
{
     UF_NULLSIGN = 0,    /* create new target solid */
     UF_POSITIVE = 1,    /* add to target solid */
     UF_NEGATIVE = 2,     /* subtract from target solid */
     UF_UNSIGNED = 3,    /* intersect with target solid */

/* the following are new settings introduced for the function
   UF_MODL_ask_feature_boolean
   and are intended to eventually replace the previous settings. */

     UF_NO_BOOLEAN = 4,  /* feature has not been booleaned */
     UF_TOP_TARGET = 5,  /* feature is the "top target" feature, it has no
                            "parent" features but does have tool features */
     UF_UNITE = 6,       /* feature has been united to target solid */
     UF_SUBTRACT = 7,    /* feature has been subtracted from target solid */
     UF_INTERSECT = 8,   /* feature has been intersected with target solid */
     UF_DEFORM_POSITIVE = 9, /* feature used to deform the positive side
                                of the target sheet */
     UF_DEFORM_NEGATIVE = 10 /* feature used to deform the negative side
                                of the target sheet */
} ;
typedef enum UF_FEATURE_SIGNS UF_FEATURE_SIGN;

/* defines used for Extrude, revolve, sweep along path trim options */
struct UF_MODL_SWEEP_TRIM_object_s
{
    tag_t *trim_objects;          /* <len:trim_count> Array of objects defining the trim. */
    int trim_count;               /* number of objects in the trim_objects
                                     array. */
    UF_MODL_SWEEP_TRIM_SIGN sign; /* Type of trim. */
    tag_t *thru_bodies;           /* <len:num_thru_bodies> No longer used. */
    int num_thru_bodies;          /* No longer used. */
};
typedef struct UF_MODL_SWEEP_TRIM_object_s UF_MODL_SWEEP_TRIM_object_t,
*UF_MODL_SWEEP_TRIM_object_p_t;

/* Define the data structure used by UF_MODL_create_fitted_spline().
   For "By Tolerance" method, you need to at least specify 'degree', 'num_of_points',
   'points', 'tolerance' and 'num_of_segments'(must be zero).
   For "By Segments" method, you need to at least specify 'degree', 'num_of_points',
   'points', and 'num_of_segments'.
   The "By Template" method is not supported at this moment.
 */
struct  SPLINE_FIT_s
{
  double  *points;           /* coordinates for the points to be fitted.
                                points[0~2] = (x, y, z) for the 1st point,
                                points[3~5] = (x, y, z) for the 2nd point,
                                ...
                             */
  double  *slopes;           /* The slope values.
                                slopes[0~2] = start slope when slope_flag = 1 or 3
                                              end slope when slope_flag = 2,
                                slopes[3~5] = end slope when slope_flag = 3.
                             */
  double  *weights;          /* values for user-defined weights. Only positive values are allowed */
  double  tolerance;         /* Tolerance value for the "By Tolerance" method.
                                This value will be ignored when the 'num_of_segments' is
                                positive  */

  int     num_of_points;     /* Number of points to be fitted */
  int     slope_flag;        /* 0=no slopes, 1=only start slope exists,
                                2=only end slope exists, 3=both end slopes exist */
  int     num_of_weights;    /* Number of user-defined weights */
  int     *weight_positions; /* The index of points (from 1 ~ num_of_points) for the user-defined
                                weights to apply to */
  int     num_of_segments;   /* Number of segments for the "By Segments" method.
                                Must be set to 0 for "By Tolerance" method. */
  int     degree;            /* The desired degree for the fitted spline        */
};
typedef struct  SPLINE_FIT_s SPLINE_FIT_t, *SPLINE_FIT_p_t;

enum UF_MODL_trim_blend_options
{
    UF_TRIM_AND_ATTACH = 0,       /* Trim blend and faces and attach blend */
    UF_TRIM_LONG_AND_ATTACH,      /* Trim blend and faces long and attach blend */
    UF_NO_TRIM_AND_ATTACH,        /* Not trim blend and faces and attach blend */
    UF_TRIM_ALL,                  /* Trim blend and faces */
    UF_TRIM_BLEND,                /* Trim blend */
    UF_NO_TRIM,                   /* Do not trim blend */
    UF_TRIM_BLEND_LONG,           /* Trim blend long */
    UF_TRIM_BLEND_SHORT           /* Trim blend short */
};
typedef enum UF_MODL_trim_blend_options UF_MODL_trim_blend_option;

enum UF_MODL_blend_radius_types
{
    UF_CONSTANT = 0,         /* Constant radius blend */
    UF_LAW_CONTROLLED,       /* Law controlled radius blend */
    UF_TANGENCY_CONTROLLED,  /* Tangency controlled radius blend */
    UF_CONIC,                /* Conic cross section blend */
    UF_CONIC_AUTO_RHO,       /* Conic cross section blend with rho defined by
                                the system*/
    UF_DISC,                 /* Circular disc blend */
    UF_ISOPARAMETER,         /* Circular isoparameter blend */
    UF_MATCH_TANGENTS,       /* Soft blend with matching tangent hold lines */
    UF_MATCH_CURVATURE       /* Soft blend with matching curvature */
};
typedef enum UF_MODL_blend_radius_types UF_MODL_blend_radius_type;

/* This union is only used internally to test face blend using law parms.
   The last void pointer "law_parameters" in UF_MODL_blend_faces_create_data_t
   is pointing to this union internally when blend type is UF_LAW_CONTROLLED.
   In future, when we have UF for law-parms, this will be available to user.
*/
union UF_MODL_blend_law_parms_union
{
    void     *circular_law_parms;
    void     *conic_law_parms[3];
};
typedef union UF_MODL_blend_law_parms_union UF_MODL_blend_law_parms_u,
*UF_MODL_blend_law_parms_p_u;

struct UF_MODL_blend_faces_create_data_s
{
    tag_t           *first_set;          /* <len:first_set_size> Array of tags of faces and/or bodies
                                            which make up the first set of
                                            faces. */
    int              first_set_size;     /* Number of objects in the first_set
                                            array. */
    logical          flip_first_normal;  /* Determine which side of the first
                                            face from the first set of faces
                                            the blend lies.  If TRUE, the
                                            blend lies in the direction of the
                                            face normal. */
    tag_t           *second_set;         /* <len:second_set_size> Array of tags of faces and/or bodies
                                            which make up the second set of
                                            faces. */
    int              second_set_size;    /* Number of objects in the second_set
                                            array. */
    logical          flip_second_normal; /* Determine which side of the first
                                            face from the second set of faces
                                            the blend lies.  If TRUE, the
                                            blend lies in the direction of the
                                            face normal. */
    logical          propagate;          /* If TRUE, the blend is allowed to
                                            propagate past smooth edges beyond
                                            the provided sets of faces. */
    tag_t           *cliff_edges;        /* <len:n_cliff_edges> Array of edge tags.  The blend is
                                            constrained to be a cliffedge blend
                                            in the region of the given edges. */
    int              n_cliff_edges;      /* Number of tags in the cliff_edges
                                            array. */
    tag_t           *thls;               /* <len:n_thls> Array of edges or curves.  The blend
                                            is constrained to be a tangent hold
                                            line blend in the region of the
                                            given edges or curves. */
    int              n_thls;             /* Number of tages in the thls array.*/
    logical          proj_on_first_set;  /* If TRUE, project thls curves on the
                                            first face set.  If FALSE, project
                                            thls curves on the second face set.
                                            This is only used when thls curves
                                            are provided. */
    logical          end_overflow;       /* If TRUE, allow end tangent and notch
                                            overflow. */
    char            *blend_tolerance;    /* Tolerance associated with the
                                            blend. */
    UF_MODL_trim_blend_option
                     trim_option;        /* Blend trimming option. */
    UF_MODL_blend_radius_type
                     radius_type;        /* Blend radius type. */
    char            *default_radius;     /* Radius for the constant radius
                                            blend. */
    void            *law_parameters;     /* Law parameters for a law controlled
                                            blend. */
};
typedef struct UF_MODL_blend_faces_create_data_s
UF_MODL_blend_faces_create_data_t,
*UF_MODL_blend_faces_create_data_p_t;

/*
  The following enum is used in the UF_MODL_parm structure to
  specify how the parameter is being defined.
*/
enum UF_MODL_parm_method_e
{
  UF_MODL_PARM_CONSTANT,
  UF_MODL_PARM_LAW_SPINE,
  UF_MODL_PARM_LAW_NO_SPINE
};
typedef enum UF_MODL_parm_method_e UF_MODL_parm_method_t;


struct UF_MODL_blend_faces_limit_data_s
{
    logical          use_start_limit; /* If TRUE, the blend is trimmed to start
                                         in a constant parameter line determined
                                         by a start limiting plane.  The blend
                                         lies on the positive side of the
                                         plane. */
    double           start_limit[6];  /* Definition of the start limit plane
                                         (point and a normal vector). */
    logical          use_end_limit;   /* If TRUE, the blend is trimmed to end in
                                         a constant parameter line determined
                                         by a start limiting plane.  The blend
                                         lies on the positive side of the
                                         plane. */
    double           end_limit[6];    /* Definition of the end limit plane
                                         (point and a normal vector). */
    logical          use_help_point;  /* If TRUE, use a help point to
                                         differentiate between multiple
                                         alternative possible blends between
                                         the faces.  If there is a blend which
                                         passes close to the help point, it is
                                         the one created. */
    double           help_point[3];   /* Coordinates of the help point. */

};
typedef struct UF_MODL_blend_faces_limit_data_s
UF_MODL_blend_faces_limit_data_t,
*UF_MODL_blend_faces_limit_data_p_t;

/*  Structure used to define bounding objects for
    Trim sheet to bounding objects. */
struct UF_MODL_trim_object {
    tag_t    object_tag;               /* tag of bounding object */
    int      curve_project_method;     /* projection method for curves
                                          1 = along surface normals
                                          2 = along a vector */
};
typedef struct UF_MODL_trim_object UF_MODL_trim_object_t,
*UF_MODL_trim_object_p_t;

/*
*   Typedef for a rpo routine function pointer.
*/
typedef int (*UF_MODL_rpo_f_p_t)(tag_t /* <I> */);

/* Various functions use this structure to define a single profile shape or
   multiple profile shapes. The profile shape can usually consist of
   curves, all edges of a face, and edges.  When this structure is returned
   from a query function, the caller is responsible for calling
   UF_MODL_free_string_list to deallocate memory.
*/
struct string_list
{
    int        num;      /* Number of items in the string array and the
                            dir array. (Min = 1, Max = 150)*/
    int        *string;  /* <len:num> Number of items in the ID array for each string.
                            (Min = 1, Max = 402) */
    int        *dir;     /* <len:num> Indication of whether the string defined in id
                            should start from the beginning of the first curve
                            or the end of the first curve.  This should be set
                            to either UF_MODL_CURVE_START_FROM_BEGIN or
                            UF_MODL_CURVE_START_FROM_END. */
    tag_t      *id;      /* <len:num> The array of items defining the string.  This array
                            should be as long as the total of the number of
                            items indicated in string.  Although not all
                            functions allow all the data types, this array can
                            typically include curves, faces and edges. */
};
typedef struct string_list UF_STRING_t, *UF_STRING_p_t;

struct method_list
{
    int            method;
    int            inter;
    tag_t          id;
    double         value[3];
    UF_STRING_p_t  s_curve;
};
typedef struct method_list UF_METHOD_t, *UF_METHOD_p_t;

enum UF_MODL_overlap_check_e
{
    UF_MODL_OVERLAP_CHECK_OFF,
    UF_MODL_OVERLAP_CHECK_ON
};
typedef enum UF_MODL_overlap_check_e UF_MODL_overlap_check_t,
*UF_MODL_overlap_check_p_t;

enum UF_MODL_quilt_type_e
{
    UF_MODL_CURVE_MESH_ALONG_FIXED_VECTOR   = 1,
    UF_MODL_CURVE_MESH_ALONG_DRIVER_NORMALS,
    UF_MODL_B_SURFACE_ALONG_FIXED_VECTOR,
    UF_MODL_B_SURFACE_ALONG_DRIVER_NORMALS,
    UF_MODL_SELF_REFIT
};
typedef enum UF_MODL_quilt_type_e UF_MODL_quilt_type_t,
*UF_MODL_quilt_type_p_t;

struct UF_MODL_quilt_data_s
{
    UF_MODL_overlap_check_t
                  check_overlap;        /* flag for controlling overlap checking
                                           = UF_MODL_OVERLAP_CHECK_OFF
                                           = UF_MODL_OVERLAP_CHECK_ON */
    int           num_target_faces;     /* number of tags in target_faces
                                           array */
    tag_t         *target_faces;        /* array of target faces tags */
    char          *inside_distance;     /* interior distance tolernace */
    char          *inside_angle;        /* interior angular tolerance in
                                           degrees */
    char          *edge_distance;       /* edge distance tolerance */
    char          *edge_angle;          /* edge angular tolerance in degrees */

};
typedef struct UF_MODL_quilt_data_s UF_MODL_quilt_data_t,
*UF_MODL_quilt_data_p_t;

/* The following structure holds data that is specific to the
   UF_MODL_curve_mesh_along_fixed_vector type of quilt surface.
   This structure completely defines all creation parameters of this type
   of surface.
*/
struct UF_MODL_curve_mesh_along_fixed_vector_data_s
{
    UF_MODL_quilt_data_t   quilt_data;           /* Structure of common
                                                    elements of the quilt
                                                    feature. */
    double                 projection_vector[3]; /* projection vector */
    UF_STRING_p_t          primary_curves;       /* string of primary curves */
    UF_STRING_p_t          cross_curves;         /* string of cross curves */
};
typedef struct UF_MODL_curve_mesh_along_fixed_vector_data_s
UF_MODL_curve_mesh_along_fixed_vector_data_t,
*UF_MODLcurve_mesh_along_fixed_vector_data__p_t;

/* The following structure holds data that is specific to the
   UF_MODL_curve_mesh_along_driver_normals type of quilt surface.
   This structure completely defines all creation parameters of this type
   of surface.
*/
struct UF_MODL_curve_mesh_along_driver_normals_data_s
{
    UF_MODL_quilt_data_t   quilt_data;           /* Structure of common
                                                    elements of the quilt
                                                    feature. */
    char                   *projection_limit;    /* projection distance limit
                                                    (= 0 if no limit) */
    UF_STRING_p_t          primary_curves;       /* string of primary curves */
    UF_STRING_p_t          cross_curves;         /* string of cross curves */
};
typedef struct UF_MODL_curve_mesh_along_driver_normals_data_s
UF_MODL_curve_mesh_along_driver_normals_data_t,
*UF_MODL_curve_mesh_along_driver_normals_data_p_t;

/* The following structure holds data that is specific to the
   UF_MODL_b_surface_along_fixed_vector type of quilt surface. This
   structure completely defines all creation parameters of this type of
   surface.
*/
struct UF_MODL_b_surface_along_fixed_vector_data_s
{
    UF_MODL_quilt_data_t   quilt_data;           /* Structure of common
                                                    elements of the quilt
                                                    feature. */
    double                 projection_vector[3]; /* projection vector */
    tag_t                  driver_surface;       /* driver b-surface */
};
typedef struct UF_MODL_b_surface_along_fixed_vector_data_s
UF_MODL_b_surface_along_fixed_vector_data_t,
*UF_MODL_b_surface_along_fixed_vector_data_p_t;

/* The following structure holds data that is specific to the
   UF_MODL_b_surface_along_driver_normals type of quilt surface.
   This structure completely defines all creation parameters of this type
   of surface.
*/
struct UF_MODL_b_surface_along_driver_normals_data_s
{
    UF_MODL_quilt_data_t   quilt_data;           /* Structure of common
                                                    elements of the quilt
                                                    feature. */
    char                   *projection_limit;    /* projection distance limit
                                                    (= 0 if no limit) */
    tag_t                  driver_surface;       /* driver b-surface */
};
typedef struct UF_MODL_b_surface_along_driver_normals_data_s
UF_MODL_b_surface_along_driver_normals_data_t,
*UF_MODL_b_surface_along_driver_normals_data_p_t;

/* The following structure holds data that is specific to the
   UF_MODL_self_refit type of quilt surface.  This structure completely
   defines all creation parameters of this type of surface.
*/
struct UF_MODL_self_refit_data_s
{
    tag_t         driver_surface;       /* driver b-surface */
    char          *inside_distance;     /* interior distance tolernace */
    char          *inside_angle;        /* interior angular tolerance in
                                           degrees */
    char          *edge_distance;       /* edge distance tolerance */
    char          *edge_angle;          /* edge angular tolerance in degrees */

};
typedef struct UF_MODL_self_refit_data_s UF_MODL_self_refit_data_t,
*UF_MODL_self_refit_data_p_t;

/* This union is used to hold a pointer to one of the previous 5 structures
   depending on the type of quilt surface.
*/
union UF_MODL_quilt_data_structures_union
{
    UF_MODL_curve_mesh_along_fixed_vector_data_t   *quilt_type1;
    UF_MODL_curve_mesh_along_driver_normals_data_t *quilt_type2;
    UF_MODL_b_surface_along_fixed_vector_data_t    *quilt_type3;
    UF_MODL_b_surface_along_driver_normals_data_t  *quilt_type4;
    UF_MODL_self_refit_data_t                      *quilt_type5;
};
typedef union UF_MODL_quilt_data_structures_union
UF_MODL_quilt_data_structures_u,
*UF_MODL_quilt_data_structures_p_u;

/*
  The following enum is used to define the direction of a curve
  or set of curves.
 */
enum UF_MODL_curve_direction_e
{
    UF_MODL_CURVE_START_FROM_END = -1,
    UF_MODL_CURVE_START_UNUSED,
    UF_MODL_CURVE_START_FROM_BEGIN
};
typedef enum UF_MODL_curve_direction_e UF_MODL_curve_direction_t;

/*
  The following are the enum's and structures needed to define
  the UF_MODL_parm information and UF_MODL_law information.
*/

/*
  The following enum is used in the UF_MODL_law structure to
  specify how the parameter is being defined.
*/
enum UF_MODL_law_method_e
{
  UF_MODL_LAW_CONSTANT,
  UF_MODL_LAW_LINEAR,
  UF_MODL_LAW_CUBIC,
  UF_MODL_LAW_SPINE_PTS_LINEAR,
  UF_MODL_LAW_SPINE_PTS_CUBIC,
  UF_MODL_LAW_EQUATION,
  UF_MODL_LAW_CURVE
};
typedef enum UF_MODL_law_method_e UF_MODL_law_method_t;

/* This structure is used in conjunction with the law spine structure to
   define points and associated values on a spine.
*/
struct UF_MODL_law_spine_pt_val_s
{
    double pt[3];                  /* Point coordinates at which to associate
                                      the corresponding value. The closest
                                      point on the spine to this point is used.
                                      If the spine is closed and the end point
                                      is put in the array twice, the beginning
                                      of the spine is used for the first point
                                      and the ending for the second point. */
    char   value[ MAX_LINE_BUFSIZE ]; /* The value assigned to the law at the
                                      given point. */
};
typedef struct UF_MODL_law_spine_pt_val_s UF_MODL_law_spine_pt_val_t,
*UF_MODL_law_spine_pt_val_p_t;



/* method_type == UF_MODL_LAW_CONSTANT */
struct UF_MODL_law_constant_s
{
    char        value[ MAX_LINE_BUFSIZE ]; /* The law evaluates to this constant
                                           value along the entire parameter
                                           range of the law. */
};
typedef struct UF_MODL_law_constant_s UF_MODL_law_constant_t;

/* method_type == UF_MODL_LAW_LINEAR or UF_MODL_LAW_CUBIC.  The law evaluates
   in a linear progression, or cubic progression along the parameter range of
   the law.
*/
struct UF_MODL_law_linear_cubic_s
{
    char        start_value[ MAX_LINE_BUFSIZE ]; /* The starting value. */
    char        end_value[ MAX_LINE_BUFSIZE ];   /* The ending value. */
};
typedef  struct UF_MODL_law_linear_cubic_s UF_MODL_law_linear_cubic_t;

/* method_type == UF_MODL_LAW_SPINE_PTS_LINEAR or UF_MODL_LAW_SPINE_PTS_CUBIC
   The law evaluates to the values supplied at the corresponding spine points,
   and varies linearly or cubically in between these values.
*/
struct UF_MODL_law_spine_pts_linear_cubic_s
{
    int                        number_of_pts_vals; /* Number of elements in the
                                                      pts_vals array. */
    UF_MODL_law_spine_pt_val_t *pts_vals;          /* <len:number_of_pts_vals>
                                                      Array of points on spine
                                                      curves at which values
                                                      are defined and the
                                                      corresponding values. */
};
typedef struct UF_MODL_law_spine_pts_linear_cubic_s
UF_MODL_law_spine_pts_linear_cubic_t;

/* method_type == UF_MODL_LAW_EQUATION.  The law evaluates to the result of
   solving the equation, while varying the variable specified from 0 to 1. */
struct UF_MODL_law_equation_s
{
    char        parm[ MAX_LINE_BUFSIZE ];    /* A character string containing the
                                             dependent variable of the equation
                                             which varies from 0 to 1 during
                                             evaluation of the law. */
    char        function[ MAX_LINE_BUFSIZE ]; /* A character string containing
                                              the equation that should be solved
                                              to determine the value of the law.
                                              Note that this equation must have
                                              the variable defined in "parm"
                                              in it. */
};
typedef struct UF_MODL_law_equation_s UF_MODL_law_equation_t;

/* method_type == UF_MODL_LAW_CURVE.  The law evaluates to the "Y" distance
between the given profile and the base curve, the profile should be in the
X-Y plane. If a base curve is not supplied, then the X axis is used as a base.*/
struct UF_MODL_law_curve_s
{
    UF_STRING_t   law_profile; /* Profile defining the law. */
    tag_t         base;        /* Base curve of the law.  If a base is not
                                  desired, set this to NULL_TAG. */
    UF_MODL_curve_direction_t direction; /* Indication if the base curve should
                                            start from the beginning or end
                                            of the curve.  This is unused if no
                                            base curve is defined. */
};
typedef struct UF_MODL_law_curve_s UF_MODL_law_curve_t;

/* Union of the different ways to define the law. */
union UF_MODL_law_defined_by_u
{
    UF_MODL_law_constant_t               constant;
    UF_MODL_law_linear_cubic_t           linear_cubic;
    UF_MODL_law_spine_pts_linear_cubic_t spine_pts_linear_cubic;
    UF_MODL_law_equation_t               equation;
    UF_MODL_law_curve_t                  curve;
};
typedef union UF_MODL_law_defined_by_u UF_MODL_law_defined_by_t;

/* This structure defines a law, with a spine, in conjunction with the
   UF_MODL_parm structure.

   Note for all character string values in the structure, if the character
   string is in expression format (e.g., p5=25,  p5+p7), and the
   expression does not exist, an expression is created and the law is
   associated to that expression. If the expression does exist, then the
   existing expression is edited, and the law is associated to that
   expression. If the character string contains an expression name
   (e.g., p5) and the expression exists, the law is associated to that
   expression, if the expression does not exist an error occurs. If
   the character string is a numeric value (e.g., 25), the law is not
   associated to an expression.
*/
struct UF_MODL_law_spine_s
{
    UF_STRING_t               spine_profile; /* A profile used to define the
                                                spine of the law. */
    UF_MODL_law_method_t      method_type;   /* Indication of how the law is
                                                being defined.  */
    UF_MODL_law_defined_by_t  defined_by;    /* The definition of the law */
};
typedef struct UF_MODL_law_spine_s UF_MODL_law_spine_t,
*UF_MODL_law_spine_p_t;

/* method_type == UF_MODL_LAW_CONSTANT.  The law evaluates to this constant
   value along the entire parameter range of the law. */
struct UF_MODL_law_no_spine_constant_s
{
    char        value[ MAX_LINE_BUFSIZE ]; /* A character string containing the
                                           constant value desired. */
};
typedef struct UF_MODL_law_no_spine_constant_s UF_MODL_law_no_spine_constant_t;

/* method_type == UF_MODL_LAW_LINEAR or UF_MODL_LAW_CUBIC.  The law evaluates
   in a linear progression or cubic progression along the parameter range
   of the law. */
struct UF_MODL_law_no_spine_linear_cubic_s
{
    char        start_value[ MAX_LINE_BUFSIZE ]; /* A character string containing
                                                 the starting value desired. */
    char        end_value[ MAX_LINE_BUFSIZE ]; /* A character string containing
                                                 the ending value desired. */
};
typedef struct UF_MODL_law_no_spine_linear_cubic_s
UF_MODL_law_no_spine_linear_cubic_t;

/* method_type == UF_MODL_LAW_EQUATION.  The law evaluates to the result of
   solving the equation while varying the variable specified from 0 to 1. */
struct UF_MODL_law_no_spine_equation_s
{
    char        parm[ MAX_LINE_BUFSIZE ];     /* A character string containing the
                                              dependent variable of the
                                              equation, this variable varies
                                              from 0 to 1 during evaluation of
                                              the law. */
    char        function[ MAX_LINE_BUFSIZE ]; /* A character string containing
                                              the equation that should be solved
                                              to determine the value of the law.
                                              Note that this equation must have
                                              the variable defined by "parm"
                                              in it. */
};
typedef struct UF_MODL_law_no_spine_equation_s
UF_MODL_law_no_spine_equation_t;

/* method_type == UF_MODL_LAW_CURVE.  The law evaluates to the "Y" distance
between the given profile and the base curve, the profile should be in the
X-Y plane. If a base curve is not supplied, then the X axis is used as a base.*/
struct UF_MODL_law_no_spine_curve_s
{
    UF_STRING_t   law_profile; /* Profile defining the law. */
    tag_t         base;        /* Base curve of the law.  If the base curve is
                                  not desired, set this to NULL_TAG. */
    UF_MODL_curve_direction_t direction; /* Indication if the base curve should
                                            start from the beginning or end of
                                            the curve. */
};
typedef struct UF_MODL_law_no_spine_curve_s UF_MODL_law_no_spine_curve_t;


/* Union of the different ways to define the law. */
union UF_MODL_law_no_spine_defined_by_union
{
    UF_MODL_law_no_spine_constant_t     constant;
    UF_MODL_law_no_spine_linear_cubic_t linear_cubic;
    UF_MODL_law_no_spine_equation_t     equation;
    UF_MODL_law_no_spine_curve_t        curve;
};
typedef union UF_MODL_law_no_spine_defined_by_union
UF_MODL_law_no_spine_defined_by_union_t;

/*
The following structure is used to define a law without a spine.

Note for all character string values in the structure, if the character
string is in expression format (e.g., p5=25,  p5+p7), and the
expression does not exist, an expression is created and the law is
associated to that expression. If the expression does exist, then the
existing expression is edited, and the law is associated to that
expression. If the character string contains an expression name (e.g.,
p5) and the expression exists, the law is associated to that expression,
if the expression does not exist an error occurs. If the character string
is a numeric value (e.g., 25) the law is not associated to an expression.

When a function is returning the law structure for a particular
parameter, all character string values are fully defined expressions
(i.e., p5=25), if they had an associated expression
*/
struct UF_MODL_law_no_spine_s
{
    UF_MODL_law_method_t                     method_type; /* Indication of how
                                                             the law is being
                                                             defined. */
    UF_MODL_law_no_spine_defined_by_union_t  defined_by;  /* Definition of the
                                                             law. */
};
typedef struct UF_MODL_law_no_spine_s UF_MODL_law_no_spine_t,
*UF_MODL_law_no_spine_p_t;

/* method_type == UF_MODL_PARM_CONSTANT */
struct UF_MODL_parm_constant_s
{
  char    value[ MAX_LINE_BUFSIZE ]; /* A character string containing the constant
                                     value desired, note that this string can be
                                     a numeric value (e.g., "25"), a fully
                                     defined expression (e.g., "p5=25"), an
                                     existing expression name (e.g., "p5"),  or
                                     an expression string  (i.e.,"p5+p7"). If
                                     the fully defined expression exists then
                                     the expression will be edited. If the
                                     expression name does not exist then an
                                     error occurs. Otherwise an expression
                                     is created. */
};
typedef struct UF_MODL_parm_constant_s UF_MODL_parm_constant_t;

/* method_type == UF_MODL_PARM_LAW_SPINE */
struct UF_MODL_parm_law_spine_s
{
    UF_MODL_law_spine_p_t     law; /* Definition of the law. */
};
typedef struct UF_MODL_parm_law_spine_s UF_MODL_parm_law_spine_t;

/* method_type == UF_MODL_PARM_LAW_NO_SPINE */
struct UF_MODL_parm_law_no_spine_s
{
    UF_MODL_law_no_spine_p_t  law; /* Definition of the law. */
};
typedef struct UF_MODL_parm_law_no_spine_s UF_MODL_parm_law_no_spine_t;

union UF_MODL_parm_defined_by_union
{
     UF_MODL_parm_constant_t     constant;     /* Information used to define
                                                  a constant parameter. */
     UF_MODL_parm_law_spine_t    law_spine;    /* Information to define a
                                                  law_spine parameter. */
     UF_MODL_parm_law_no_spine_t law_no_spine; /* Information to define a
                                                  law_no_spine parameter. */
};
typedef union UF_MODL_parm_defined_by_union UF_MODL_parm_defined_by_union_t;

/*
  The following structure is used to define input parameters
  when there is an option between using a constant value or
  a law.
*/
struct UF_MODL_parm_s
{
  UF_MODL_parm_method_t            method_type; /* Indication of how the
                                                   parameter is being defined,
                                                   either through a constant
                                                   value, of which an expression
                                                   is made, or by a law. */
  UF_MODL_parm_defined_by_union_t  defined_by;  /* Definition of the parameter*/
};
typedef struct UF_MODL_parm_s UF_MODL_parm_t, *UF_MODL_parm_p_t;

/* This new create face blend data structure is intended to replace the old
   one in the feature.
*/
struct UF_MODL_face_blend_create_data_s
{
    tag_t                     *first_set;   /* <len:first_set_size> You can input individual faces or a
                                               face collector.*/
    int                        first_set_size;
    logical                    flip_first_normal;
    tag_t                     *second_set;  /* <len:second_set_size> You can input individual faces or a
                                               face collector.*/
    int                        second_set_size;
    logical                    flip_second_normal;
    logical                    propagate;
    tag_t                     *cliff_edges; /* <len:n_cliff_edges> */
    int                        n_cliff_edges;
    tag_t                     *thls;      /* <len:n_thls> You can input individual edges or curves or
                                             you can input an edge or curve collector.*/
    int                        n_thls;
    logical                    proj_on_first_set; /* this only takes effect if
                                                    the thls are curves and the
                                                    first and second face sets
                                                    are on different bodies. */
    logical                    end_overflow;
    char                      *blend_tolerance;
    UF_MODL_trim_blend_option  trim_option;
    UF_MODL_blend_radius_type  radius_type;
    char                      *default_radius;
    tag_t                     *thls_1;    /* <len:n_thls_1> This is used for soft blend to
                                             specify the tangent control lines
                                             on the second face set. thls are
                                             used as the tangent control lines
                                             on the first face set. You can input
                                             individual edges or curves or you
                                             can input an edge or curve collector.*/
    int                        n_thls_1;
    UF_MODL_parm_p_t          *law_parameters;

/* law_parameters should be an array of UF_MODL_parm_p_t whose length is
   determined by the UF_MODL_blend_radius_type being used

    UF_MODL_blend_radius_type        law_parameters

         UF_CONSTANT
      or UF_TANGENCY_CONTROLLED      NULL (we will ignore it anyway)

         UF_LAW_CONTROLLED
      or UF_DISC
      or UF_ISOPARAMETER             One element array. Must have
                                     method_type == UF_MODL_PARM_LAW_SPINE,
                                     to specify the radius data and the spine.

         UF_CONIC                    Three-element array.  First element must
                                     have method_type == UF_MODL_PARM_LAW_SPINE
                                     and will specify first offset1 and spine.
                                     Second element will specify offset2.
                                     Third element will specify rho values.

         UF_CONIC_AUTO_RHO           Two-element array.  First element must have
                                     method_type == UF_MODL_PARM_LAW_SPINE
                                     and will specify first offset1 and spine.
                                     Second element will specify offset2.

         UF_MATCH_TANGENTS           One-element array.  Must have
                                     method_type == UF_MODL_PARM_LAW_SPINE,
                                     Only the spine information will be used,
                                     the other data should be NULL.

         UF_MATCH_CURVATURE          Two-element array.  First element must have
                                     method_type == UF_MODL_PARM_LAW_SPINE
                                     and will specify skew and spine.
                                     Second element will specify rho values.
 */

  logical          remove_self_int;    /* New Option added in NX3,Remove Surface Self-Intersections
                                          Will work only for Constant radius rolling ball blends,
                                          Will not work with cliff edges,tangency control, DISC,
                                          Law controlled, ISOPARAM blends*/

};
typedef struct UF_MODL_face_blend_create_data_s
               UF_MODL_face_blend_create_data_t,
              *UF_MODL_face_blend_create_data_p_t;

/*
  The following are the enum's and structures needed to define
  the UF_MODL_secsrf information.
*/

/* Create methods */
enum UF_MODL_secsrf_cre_method
{
    UF_MODL_secsrf_init_create_method,
    UF_MODL_secsrf_five_points,
    UF_MODL_secsrf_four_points_slope,
    UF_MODL_secsrf_ends_slopes_shoulder,
    UF_MODL_secsrf_ends_apex_shoulder,
    UF_MODL_secsrf_ends_apex_rho,
    UF_MODL_secsrf_ends_slopes_rho,
    UF_MODL_secsrf_ends_slope_arc,
    UF_MODL_secsrf_three_points_arc,
    UF_MODL_secsrf_fillet_shoulder,
    UF_MODL_secsrf_fillet_rho,
    UF_MODL_secsrf_ends_slopes_hilite,
    UF_MODL_secsrf_ends_apex_hilite,
    UF_MODL_secsrf_fillet_hilite,
    UF_MODL_secsrf_two_points_radius,
    UF_MODL_secsrf_ends_slopes_cubic,
    UF_MODL_secsrf_fillet_cubic,
    UF_MODL_secsrf_point_radius_angle_arc,
    UF_MODL_secsrf_not_used1,    /* Not implemented */
    UF_MODL_secsrf_not_used2,    /* Not implemented */
    UF_MODL_secsrf_full_circle
} ;
typedef enum UF_MODL_secsrf_cre_method UF_MODL_secsrf_cre_method_t;

/* Generic parameter methods */
enum UF_MODL_secsrf_param_method
{
    UF_MODL_secsrf_no_data,  /* No Data, (Rho, radius, law, etc.) */
    UF_MODL_secsrf_constant, /* data_constant */
    UF_MODL_secsrf_linear,   /* data_value[2]  */
    UF_MODL_secsrf_cubic,    /* data_value[2]  */
    UF_MODL_secsrf_tension,  /* NULL */
    UF_MODL_secsrf_general   /* general_law (UF_MODL_parm general law) */
};
typedef enum UF_MODL_secsrf_param_method UF_MODL_secsrf_param_method_t;

struct UF_MODL_secsrf_param_data_values_s
{
    double data_constant;   /* Constant Law value */
    tag_t  data_exp[2];     /* Cubic/linear expression tags */
    double data_value[2];   /* Cubic/linear law values */
    UF_MODL_parm_t *general_law;     /* general law structure */
};
typedef struct UF_MODL_secsrf_param_data_values_s
UF_MODL_secsrf_param_data_values_t;

/* Section Surface Generic data Stucture for laws, rho, etc.
   You can define any type of law (not just constant, linear, and
   cubic), by using the UF_MODL_parm_t structure.

   For the UF_MODL_ask_section_surface function, if the section
   surface queried uses a constant, linear, or cubic law, then those
   types still return as constant, linear, or cubic.  However, if you use
   any other type of law, it is noted as "UF_MODL_secsrf_general".
   The data for that law appears in the data_values.general_law field of the
   UF_MODL_secsrf_param structure.
*/
struct UF_MODL_secsrf_param_s
{
    UF_MODL_secsrf_param_method_t data_method; /* method type value */
    UF_MODL_secsrf_param_data_values_t data_values;
};
typedef struct UF_MODL_secsrf_param_s UF_MODL_secsrf_param_t,
*UF_MODL_secsrf_param_p_t;

/* Section Surface data Structure

Currently there are 18 different Section surface construction techniques. Each
requiring a different combination of construction geometry and data. Below is
the common data used for all of the section surfaces.

Given:
UF_MODL_secsrf_data_t section_surface;
section_surface.polynomial_status = 0; Conic - since rational B-spline curves
                                       can represent conic curves exactly, this
                                       option produces a true, exact conic shape
                                       with no reversals in curvature. It accepts
                                       rho values between 0.0001 and 0.9999.
                                       Parameterization may be highly nonuniform.
                                       The Conic option does not work for fillet-cubic,
                                       ends-slopes-rho, and ends-slopes-cubic section
                                       features. If you choose Conic when creating one
                                       of these section types, the system ignores your
                                       choice and uses Cubic instead.
section_surface.polynomial_status = 1; Cubic - these curves have roughly the same shape
                                       as their rational counterparts (used in the Conic
                                       option) but produce a surface with a better
                                       parameterization. This option distributes the flow
                                       lines along the entire curve, but does not produce
                                       exact conic shapes. For example, rho values greater
                                       than 0.75 create section curves which are not shaped
                                       like a conic. For this reason, the maximum rho allowed
                                       when creating polynomial cubic sections is 0.75.
section_surface.polynomial_status = 2; Quintic - the surfaces are degree 5, and are C2
                                       (curvature continuous) between patches.
section_surface.tolerance = any valid NX tolerance value;
section_surface.direction_indicator = 1; create surface in the direction of the
                                         face normal
section_surface.direction_indicator = -1; create surface opposite the face normal
                                    (UF_MODL_secsrf_point_radius_angle_arc only)

The following shows the options for section surface that contain rho
data: UF_MODL_secsrf_ends_apex_rho, UF_MODL_secsrf_ends_slopes_rho and
UF_MODL_secsrf_fillet_rho section surfaces. Valid rho values are described in
the "Section" section of the "Free Form Features" chapter of the Modeling User
Manual.

If a section surface has no rho data the rho method should be set to
the following.

section_surface.rho_data.data_method = UF_MODL_secsrf_no_data;

If the rho method is set to a constant rho then a valid rho value must
be placed in data_values structure.

section_surface.rho_data.data_method =    UF_MODL_secsrf_constant;
section_surface.rho_data.data_values.data_constant = valid rho value;

If the rho method is set to a linear or cubic rho then a valid rho value
must be placed in data_values structure.  The expression tag will take
precedence over the a real value. Both rho values need to be populated.

section_surface.rho_data.data_method = UF_MODL_secsrf_linear or
                                       UF_MODL_secsrf_cubic;
section_surface.rho_data.data_values.data_value[0]=valid rho value;
or section_surface.rho_data.data_values.data_exp[0]=expression tag;
and
section_surface.rho_data.data_values.data_value[1]=valid rho value;
or section_surface.rho_data.data_values.data_exp[1]=expression tag;

If the rho method is set to least tension then the rho_values must be
set to NULL.
section_surface.rho_data.data_method = UF_MODL_secsrf_tension;
section_surface.rho_data.data_values.general_law = NULL;

If the rho value is set to general the user is required NOT to change
the data_values.
section_surface.rho_data.data_method = UF_MODL_secsrf_general;
section_surface.rho_data.data_values.general_law = pointer data to
                                                   a law function;

The following shows the options for section surface that contain
radius data: UF_MODL_secsrf_two_points_radius and
UF_MODL_secsrf_point_radius_angle_arc section surfaces. Valid
radius values are described in the Section Surface documentation.

If a section surface has no radius data the data method should be set
to the following.
section_surface.radius_data.data_method = UF_MODL_secsrf_no_data;

If the radius method is set to a constant radius then a valid radius
value must be placed in data_values structure.
section_surface.radius_data.data_method = UF_MODL_secsrf_constant;
section_surface.radius_data.data_values.data_constant = valid radius value;

If the radius method is set to a linear or cubic then a valid radius
value must be placed in data_values structure.  The expression tag will
take precedence over the a real value. Both radius values need to be populated.
section_surface.radius_data.data_method = UF_MODL_secsrf_linear or
                                          UF_MODL_secsrf_cubic;
section_surface.radius_data.data_values.data_value[0]=valid radius value; or
section_surface.radius_data.data_values.data_exp[0]=expression tag;
and
section_surface.radius_data.data_values.data_value[1]=valid radius value; or
section_surface.radius_data.data_values.data_exp[1]=expression tag;

If the radius value is set to general the user is required NOT to
change the data_values.
section_surface.radius_data.data_method = UF_MODL_secsrf_general;
section_surface.radius_data.data_values.general_law = pointer data
                                                      to a law function;

The following shows the options for a section surface that contain
angle data:  UF_MODL_secsrf_point_radius_angle_arc section
surface. Valid angle values are described in the Section Surface
documentation.

If a section surface has no angle data the data method should be set to
the following.
section_surface.angle_data.data_method = UF_MODL_secsrf_no_data;

If the angle method is set to a constant angle then a valid angle value
must be placed in data_values structure.
section_surface.angle_data.data_method = UF_MODL_secsrf_constant;
section_surface.angle_data.data_values.data_constant = valid angle value;

If the angle method is set to a linear or cubic angle then a valid angle
value must be placed in data_values structure.  The expression tag will
take precedence over the a real value. Both angle values need to be populated.
section_surface.angle_data.data_method = UF_MODL_secsrf_linear or
                                         UF_MODL_secsrf_cubic;
section_surface.angle_data.data_values.data_value[0]=valid angle value; or
section_surface.angle_data.data_values.data_exp[0]=expression tag;
and
section_surface.angle_data.data_values.data_value[1]=valid angle value; or
section_surface.angle_data.data_values.data_exp[1]=expression tag;

If the angle value is set to general the user is required NOT to change
the data_values.
section_surface.angle_data.data_method = UF_MODL_secsrf_general;
section_surface.angle_data.data_values.general_law = pointer data
                                                     to a law function;

Note: The UF_MODL_secsrf_general data method can not be used
directly. It is a place holder for any section surface which contains a
law value that is populated during an UF_MODL_ask_section_surface call.  Do
not modify this data.

The following is a list of each type and their required geometry tags and data.

section_surface.create_method = UF_MODL_secsrf_five_points;
section_surface.control_strings[0] = Start curve tag;
section_surface.control_strings[1] = First interior curve tag;
section_surface.control_strings[2] = Second interior curve tag;
section_surface.control_strings[3] = Third interior curve tag;
section_surface.control_strings[4] = End curve tag;
section_surface.control_strings[5] = NULL;
section_surface.spine_string = Spine curve tag;
section_surface.rho_data = NULL;
section_surface.tangent_faces[0] = NULL;
section_surface.tangent_faces[1] = NULL;
section_surface.radius_data = NULL;
section_surface.angle_data = NULL;

section_surface.create_method = UF_MODL_secsrf_four_points_slope;
section_surface.control_strings[0] = Start curve tag;
section_surface.control_strings[1] = Start slope curve tag;
section_surface.control_strings[2] = First interior curve tag;
section_surface.control_strings[3] = Second interior curve tag;
section_surface.control_strings[4] = End curve tag;
section_surface.control_strings[5] = NULL;
section_surface.spine_string = Spine curve tag;
section_surface.rho_data = NULL;
section_surface.tangent_faces[0] = NULL;
section_surface.tangent_faces[1] = NULL;
section_surface.radius_data = NULL;
section_surface.angle_data = NULL;

section_surface.create_method = UF_MODL_secsrf_ends_slopes_shoulder;
section_surface.control_strings[0] = Start curve tag;
section_surface.control_strings[1] = Start slope curve tag;
section_surface.control_strings[2] = End curve tag;
section_surface.control_strings[3] = End slope curve tag;
section_surface.control_strings[4] = Shoulder curve tag;
section_surface.control_strings[5] = NULL;
section_surface.spine_string = Spine curve tag;
section_surface.rho_data = NULL;
section_surface.tangent_faces[0] = NULL;
section_surface.tangent_faces[1] = NULL;
section_surface.radius_data = NULL;
section_surface.angle_data = NULL;

section_surface.create_method = UF_MODL_secsrf_ends_apex_shoulder;
section_surface.control_strings[0] = Start curve tag;
section_surface.control_strings[1] = Apex curve tag;
section_surface.control_strings[2] = End curve tag;
section_surface.control_strings[3] = Shoulder curve tag;
section_surface.control_strings[4] = NULL;
section_surface.control_strings[5] = NULL;
section_surface.spine_string = Spine curve tag;
section_surface.rho_data = NULL;
section_surface.tangent_faces[0] = NULL;
section_surface.tangent_faces[1] = NULL;
section_surface.radius_data = NULL;
section_surface.angle_data = NULL;

section_surface.create_method = UF_MODL_secsrf_ends_apex_rho;
section_surface.control_strings[0] = Start curve tag;
section_surface.control_strings[1] = Apex curve tag;
section_surface.control_strings[2] = End curve tag;
section_surface.control_strings[3] = NULL;
section_surface.control_strings[4] = NULL;
section_surface.control_strings[5] = NULL;
section_surface.spine_string = Spine curve tag;
section_surface.rho_data = must be populated
section_surface.tangent_faces[0] = NULL;
section_surface.tangent_faces[1] = NULL;
section_surface.radius_data = NULL;
section_surface.angle_data = NULL;

section_surface.create_method = UF_MODL_secsrf_ends_slopes_rho;
section_surface.control_strings[0] = Start curve tag;
section_surface.control_strings[1] = Start Slope curve tag;
section_surface.control_strings[2] = End curve tag;
section_surface.control_strings[3] = End Slope curve tag;
section_surface.control_strings[4] = NULL;
section_surface.control_strings[5] = NULL;
section_surface.spine_string = Spine curve tag;
section_surface.rho_data = must be populated
section_surface.tangent_faces[0] = NULL;
section_surface.tangent_faces[1] = NULL;
section_surface.radius_data = NULL;
section_surface.angle_data = NULL;

section_surface.create_method = UF_MODL_secsrf_ends_slope_arc;
section_surface.control_strings[0] = Start curve tag;
section_surface.control_strings[1] = Start Slope curve tag;
section_surface.control_strings[2] = End curve tag;
section_surface.control_strings[3] = NULL;
section_surface.control_strings[4] = NULL;
section_surface.control_strings[5] = NULL;
section_surface.spine_string = Spine curve tag;
section_surface.rho_data = NULL;
section_surface.tangent_faces[0] = NULL;
section_surface.tangent_faces[1] = NULL;
section_surface.radius_data = NULL;
section_surface.angle_data = NULL;

section_surface.create_method = UF_MODL_secsrf_three_points_arc;
section_surface.control_strings[0] = Start curve tag;
section_surface.control_strings[1] = First Interior curve tag;
section_surface.control_strings[2] = End curve tag;
section_surface.control_strings[3] = NULL;
section_surface.control_strings[4] = NULL;
section_surface.control_strings[5] = NULL;
section_surface.spine_string = Spine curve tag;
section_surface.rho_data = NULL;
section_surface.tangent_faces[0] = NULL;
section_surface.tangent_faces[1] = NULL;
section_surface.radius_data = NULL;
section_surface.angle_data = NULL;

section_surface.create_method = UF_MODL_secsrf_fillet_shoulder;
section_surface.control_strings[0] = Curve tag on first face;
section_surface.control_strings[1] = Curve tag on second face;
section_surface.control_strings[2] = Shoulder curve tag;
section_surface.control_strings[3] = NULL;
section_surface.control_strings[4] = NULL;
section_surface.control_strings[5] = NULL;
section_surface.spine_string = Spine curve tag;
section_surface.rho_data = NULL;
section_surface.tangent_faces[0] = First face tag;
section_surface.tangent_faces[1] = Second face tag;
section_surface.radius_data = NULL;
section_surface.angle_data = NULL;

section_surface.create_method = UF_MODL_secsrf_fillet_rho;
section_surface.control_strings[0] = Curve tag on first face;
section_surface.control_strings[1] = Curve tag on second face;
section_surface.control_strings[2] = NULL;
section_surface.control_strings[3] = NULL;
section_surface.control_strings[4] = NULL;
section_surface.control_strings[5] = NULL;
section_surface.spine_string = Spine curve tag;
section_surface.rho_data = must be populated with rho data
section_surface.tangent_faces[0] = First face tag;
section_surface.tangent_faces[1] = Second face tag;
section_surface.radius_data = NULL;
section_surface.angle_data = NULL;

section_surface.create_method = UF_MODL_secsrf_ends_slopes_hilite;
section_surface.control_strings[0] = Start curve tag;
section_surface.control_strings[1] = Start Slope curve tag;
section_surface.control_strings[2] = End curve tag;
section_surface.control_strings[3] = End Slope curve tag;
section_surface.control_strings[4] = Start highlight curve tag;
section_surface.control_strings[5] = End highlight curve tag;
section_surface.spine_string = Spine curve tag;
section_surface.rho_data = NULL;
section_surface.tangent_faces[0] = NULL;
section_surface.tangent_faces[1] = NULL;
section_surface.radius_data = NULL;
section_surface.angle_data = NULL;

section_surface.create_method = UF_MODL_secsrf_ends_apex_hilite;
section_surface.control_strings[0] = Start curve tag;
section_surface.control_strings[1] = Apex curve tag;
section_surface.control_strings[2] = End curve tag;
section_surface.control_strings[3] = Start highlight curve tag;
section_surface.control_strings[4] = End highlight curve tag;
section_surface.control_strings[5] = NULL;
section_surface.spine_string = Spine curve tag;
section_surface.rho_data = NULL;
section_surface.tangent_faces[0] = NULL;
section_surface.tangent_faces[1] = NULL;
section_surface.radius_data = NULL;
section_surface.angle_data = NULL;

section_surface.create_method = UF_MODL_secsrf_fillet_hilite;
section_surface.control_strings[0] = Curve tag on first face;
section_surface.control_strings[1] = Curve tag on second face;
section_surface.control_strings[3] = Start highlight curve tag;
section_surface.control_strings[4] = End highlight curve tag;
section_surface.control_strings[5] = NULL;
section_surface.spine_string = Spine curve tag;
section_surface.rho_data = must be populated with rho data
section_surface.tangent_faces[0] = Face tag one;
section_surface.tangent_faces[1] = Face tag two;
section_surface.radius_data = NULL;
section_surface.angle_data = NULL;

section_surface.create_method = UF_MODL_secsrf_two_points_radius;
section_surface.control_strings[0] = Start curve tag;
section_surface.control_strings[1] = End curve tag;
section_surface.control_strings[2] = NULL;
section_surface.control_strings[3] = NULL;
section_surface.control_strings[4] = NULL;
section_surface.control_strings[5] = NULL;
section_surface.spine_string = Spine curve tag;
section_surface.rho_data = NULL;
section_surface.tangent_faces[0] = NULL;
section_surface.tangent_faces[1] = NULL;
section_surface.radius_data = must be populated with radius data
section_surface.angle_data = NULL;

section_surface.create_method = UF_MODL_secsrf_ends_slopes_cubic;
section_surface.control_strings[0] = Start curve tag;
section_surface.control_strings[1] = Start Slope  curve tag;
section_surface.control_strings[2] = End curve tag;
section_surface.control_strings[3] = End Slope curve tag;
section_surface.control_strings[4] = NULL;
section_surface.control_strings[5] = NULL;
section_surface.spine_string = Spine curve tag;
section_surface.rho_data = NULL;
section_surface.tangent_faces[0] = NULL;
section_surface.tangent_faces[1] = NULL;
section_surface.radius_data = NULL;
section_surface.angle_data = NULL;

section_surface.create_method = UF_MODL_secsrf_fillet_cubic;
section_surface.control_strings[0] = Curve tag on first face;
section_surface.control_strings[1] = Curve tag on second face;
section_surface.control_strings[2] = NULL;
section_surface.control_strings[3] = NULL;
section_surface.control_strings[4] = NULL;
section_surface.control_strings[5] = NULL;
section_surface.spine_string = Spine curve tag;
section_surface.rho_data = NULL;
section_surface.tangent_faces[0] = First face tag;
section_surface.tangent_faces[1] = Second face tag;
section_surface.radius_data = NULL;
section_surface.angle_data = NULL;

section_surface.create_method = UF_MODL_secsrf_point_radius_angle_arc;
section_surface.control_strings[0] = Start curve tag;
section_surface.control_strings[1] = NULL;
section_surface.control_strings[2] = NULL;
section_surface.control_strings[3] = NULL;
section_surface.control_strings[4] = NULL;
section_surface.control_strings[5] = NULL;
section_surface.spine_string = Spine curve tag;
section_surface.rho_data = NULL;
section_surface.tangent_faces[0] = First face tag;
section_surface.tangent_faces[1] = NULL;
section_surface.radius_data = must be populated with radius data
section_surface.angle_data = must be populated with angle data;
section_surface.direction_indicator = must be 1 or -1;

section_surface.create_method = UF_MODL_secsrf_full_circle;
section_surface.control_strings[0] = Guide edge curve tag;
section_surface.control_strings[1] = Orientation edge curve tag;
section_surface.control_strings[2] = NULL;
section_surface.control_strings[3] = NULL;
section_surface.control_strings[4] = NULL;
section_surface.control_strings[5] = NULL;
section_surface.spine_string = Spine curve tag;
section_surface.rho_data = NULL;
section_surface.tangent_faces[0] = NULL;
section_surface.tangent_faces[1] = NULL;
section_surface.radius_data = must be populated with radius data
section_surface.angle_data = NULL;
*/
struct UF_MODL_secsrf_data_s
{
    UF_MODL_secsrf_cre_method_t create_method; /* Creation Method */
    int polynomial_status;                     /* Polynomial status */
    UF_MODL_secsrf_param_t rho_data;           /* Rho data */
    double tolerance;                          /* Tolerance used to
                                                  create surface */
    tag_t tangent_faces[2];                    /* Face tags of tanget faces */
    UF_STRING_p_t control_strings[6];          /* Control string Array */
    UF_STRING_p_t spine_string;                /* Spine curve string */
    UF_MODL_secsrf_param_t radius_data;        /* Radius law  data */
    UF_MODL_secsrf_param_t angle_data;         /* Angle law data */
    int direction_indicator;                   /* Surface direction */
};
typedef struct UF_MODL_secsrf_data_s UF_MODL_secsrf_data_t,
*UF_MODL_secsrf_data_p_t;

/*
  The following are the enum's and structures needed to define
  the UF_MODL_vector information.
*/

/*
  The following enum is used in the UF_MODL_vector structure
  to specify how the vector is being defined.
*/
enum UF_MODL_vector_type_e
{
  UF_MODL_VECTOR_DIRECTION,
  UF_MODL_VECTOR_AXIS,
  UF_MODL_VECTOR_FACE_NORMAL,
  UF_MODL_VECTOR_TWO_POINTS,
  UF_MODL_VECTOR_PLANE_OF_CURVES,
  UF_MODL_VECTOR_FACE_NORMALS,
  UF_MODL_VECTOR_DIRECTION_EXACT_GEOMETRY,
  UF_MODL_VECTOR_AXIS_EXACT_GEOMETRY,
  UF_MODL_VECTOR_FACE_NORMALS_EXACT_GEOMETRY
};
typedef enum UF_MODL_vector_type_e UF_MODL_vector_type_t;

/* vector_type == UF_MODL_VECTOR_DIRECTION */
struct UF_MODL_vector_direction_s
{
   double   xyz[3];   /* 3D direction vector. */
};
typedef struct UF_MODL_vector_direction_s UF_MODL_vector_direction_t;

/* vector_type == UF_MODL_VECTOR_AXIS */
struct UF_MODL_vector_axis_s
{
   tag_t    identifier; /* Tag of the datum plane or plane whose normal is to
                           be used to define the vector, or the tag of a datum
                           axis. */
};
typedef struct UF_MODL_vector_axis_s UF_MODL_vector_axis_t;

/* vector_type == UF_MODL_VECTOR_FACE_NORMAL */
struct UF_MODL_vector_face_normal_s
{
  tag_t      face;     /* tag of the face whose normal or reverse normal is to
                          be used to define the vector. */
  double     point[3]; /* Point coordinates on the face to determine the
                          normal or reverse normal at.  The closest point on
                          the face to this point is used. */
};
typedef struct UF_MODL_vector_face_normal_s UF_MODL_vector_face_normal_t;

/* vector_type == UF_MODL_VECTOR_TWO_POINTS */
struct UF_MODL_vector_two_points_s
{
  double     from_point[3]; /* Point coordinates from which the vector is to
                               start. */
  double     to_point[3]; /* Point coordinates at which the vector is to
                               end. */
} ;
typedef struct UF_MODL_vector_two_points_s UF_MODL_vector_two_points_t;

/* vector_type == UF_MODL_VECTOR_PLANE_OF_CURVES */
struct UF_MODL_vector_plane_of_curves_s
{
  int        number_of_curves; /* Number of curves in the following array. */
  tag_t      *curves;          /* Array of curves whose plane normal is to
                                  be found.  The normal will be the vector. */
};
typedef struct UF_MODL_vector_plane_of_curves_s
UF_MODL_vector_plane_of_curves_t;

/* Union of the various methods of defining a vector. */
union UF_MODL_vector_defined_by_union
{
    UF_MODL_vector_direction_t        direction;
    UF_MODL_vector_axis_t             axis;
    UF_MODL_vector_face_normal_t      face_normal;
    UF_MODL_vector_two_points_t       two_points;
    UF_MODL_vector_plane_of_curves_t  plane_of_curves;
};
typedef union UF_MODL_vector_defined_by_union
UF_MODL_vector_defined_by_union_t;

/*
  The following structure allows definition of a vector
  with a variety of options. Note that associativity to
  any data is not maintained unless otherwise specified.
*/
struct UF_MODL_vector_s
{
  int                                reverse_vector; /* Indicates if the vector
                                                        calculated should then
                                                        be reversed before being
                                                        used.  If zero, the
                                                        vector is not reversed.
                                                        Any other value will
                                                        reverse the vector. */
  UF_MODL_vector_type_t              vector_type;    /* Indication of which
                                                        structure is being used
                                                        to define the vector.*/
  UF_MODL_vector_defined_by_union_t  defined_by;     /* The definition of the
                                                        vector. */
};
typedef struct UF_MODL_vector_s UF_MODL_vector_t, *UF_MODL_vector_p_t;

/*
  The following are some generic enum's and structures that
  are used in various user function interfaces.
*/

/*
  The following enum is used in the UF_MODL_faces structure to
  specify the type of extension desired.
*/
enum UF_MODL_face_extension_e
{
  UF_MODL_FACE_EXTENSION_NONE,
  UF_MODL_FACE_EXTENSION_LINEAR,
  UF_MODL_FACE_EXTENSION_NATURAL,
  UF_MODL_FACE_EXTENSION_CURV,
  UF_MODL_FACE_EXTENSION_CIRC
};
typedef enum UF_MODL_face_extension_e UF_MODL_face_extension_t;

/*
  The following structure allows definition of an array of
  faces along with an extension option.
*/
struct UF_MODL_faces_s
{
   int                      number_of_faces; /* Number of faces supplied in the
                                                following array. */
   tag_t                    *faces;          /* <len:number_of_faces>Array of faces to be used in the
                                                function.  Note that some
                                                functions may allow planes and
                                                datum planes in this array. */
   UF_MODL_face_extension_t face_extension;  /* Indication of how the faces
                                                should be extended if the
                                                function allows for face
                                                extension.  */
};
typedef struct UF_MODL_faces_s UF_MODL_faces_t, *UF_MODL_faces_p_t;

enum UF_MODL_offset_trans_type_e
{
  UF_MODL_OFFSET_OF_FACES,
  UF_MODL_TRANSLATION_OF_FACES
};
typedef enum UF_MODL_offset_trans_type_e UF_MODL_offset_trans_type_t;

struct UF_MODL_offset_trans_faces_s
{
  UF_MODL_faces_p_t           faces;       /* The faces to be offset or
                                              translated. */
  UF_MODL_offset_trans_type_t method_type; /* Indication of whether the faces
                                              are to be offset or translated. */

  char          distance[ MAX_LINE_BUFSIZE ]; /* <len:MAX_LINE_BUFSIZE>
                                              A character string containing the
                                              constant value to offset or
                                              translate the given faces. */
  UF_MODL_vector_p_t          direction;   /* A vector defining the direction
                                              of translation, only used if
                                              method_type is
                                              UF_MODL_TRANSLATION_OF_FACES.  It
                                              can be NULL otherwise. */
};
typedef struct UF_MODL_offset_trans_faces_s
UF_MODL_offset_trans_faces_t,
*UF_MODL_offset_trans_faces_p_t;

enum UF_MODL_proj_type_e
{
  UF_MODL_PROJ_NORMAL_TO_CURVES,
  UF_MODL_PROJ_ALONG_VECTOR
};
typedef enum UF_MODL_proj_type_e UF_MODL_proj_type_t;

/* This structure is used in various functions to define a set of curves that
   is then subsequently projected along the specified vector. The
   function also requires the input of faces/planes/datum_planes to
   define the target of the projection.
*/
struct UF_MODL_project_curves_s
{
  int                 number_of_curves;       /* The number of curves in the
                                                 following array. */
  tag_t               *curves;                /* <len:number_of_curves>
                                                 The array of curves. */
  UF_MODL_proj_type_t curve_projection_type;  /* Indication of whether the
                                                 curves should be projected
                                                 along their plane normal or
                                                 along the following vector. */
  UF_MODL_vector_p_t  curve_projection_vector;/* The vector along which to
                                                 project the curves, if
                                                 curve_projection_type is
                                                 UF_MODL_PROJ_ALONG_VECTOR. */

};
typedef struct UF_MODL_project_curves_s UF_MODL_project_curves_t,
*UF_MODL_project_curves_p_t;

/*
  The following are valid parameters to UF_MODL_set_update_fail_option ().
 */

enum UF_MODL_update_option_e
{
    UF_MODL_UPDATE_NO_OPTION = 0,   /*No option defined yet                             */
    UF_MODL_UPDATE_UNDO,            /*Undo entire Update operation.                     */
    UF_MODL_UPDATE_SUPPRESS,        /*Suppress previous failed object                   */
    UF_MODL_UPDATE_SUPPRESS_ALL,    /*Suppress previous failed object and rest of list  */
    UF_MODL_UPDATE_ACCEPT,          /*Accept warning of previous object                 */
    UF_MODL_UPDATE_ACCEPT_ALL,      /*Accept previous warning and future of same type   */
    UF_MODL_UPDATE_INTERRUPT        /*Interrupt update                                  */
};
typedef enum UF_MODL_update_option_e UF_MODL_update_option_t;

/*
  The following enum's and structures are used in the pocket/pad
  Open API interfaces.
*/

enum UF_MODL_curves_represent_e
{
  UF_MODL_THEORETICAL_INTERSECT,
  UF_MODL_TANGENT_AT_END_OF_BLEND
};
typedef enum UF_MODL_curves_represent_e UF_MODL_curves_represent_t;

enum UF_MODL_pocketpad_type_e
{
  UF_MODL_SINGLE_OUTLINE,
  UF_MODL_DOUBLE_OUTLINE,
  UF_MODL_SINGLE_OUTLINE_CORNER,
  UF_MODL_DOUBLE_OUTLINE_CORNER,
  UF_MODL_SINGLE_OUTLINE_NO_ATTACH,
  UF_MODL_DOUBLE_OUTLINE_NO_ATTACH
};
typedef enum UF_MODL_pocketpad_type_e UF_MODL_pocketpad_type_t;

enum UF_MODL_taper_relative_to_e
{
  UF_MODL_TAPER_FACE_NORMALS,
  UF_MODL_TAPER_FIXED_VECTOR,
  UF_MODL_TAPER_BY_OUTLINE_FACE_NORMALS,
  UF_MODL_TAPER_BY_OUTLINE_FIXED_VECTOR
};
typedef enum UF_MODL_taper_relative_to_e UF_MODL_taper_relative_to_t;

enum UF_MODL_outline_represents_e
{
  UF_MODL_SHAPE_AT_PLACEMENT,
  UF_MODL_SHAPE_AT_FLOOR,
  UF_MODL_SHAPE_AT_TOP
};
typedef enum UF_MODL_outline_represents_e UF_MODL_outline_represents_t;

/***************************************************************************

 ****************************************************************************/

/* outline_type == UF_MODL_SINGLE_OUTLINE */
struct UF_MODL_single_outline_s
{
  UF_MODL_project_curves_p_t      outline_curves;    /* The curves making up the
                                                        outline. */
  UF_MODL_curves_represent_t      curves_represent;  /* Indication of whether
                                                        the curves represent
                                                        theoreticals or tangents
                                                     */
  UF_MODL_outline_represents_t    outline_represents;/* Indication of whether
                                                        this outline is defining
                                                        the shape of the
                                                        pocket/pad at the
                                                        placement face of the
                                                        pocket/pad, at the
                                                        floor face o the pocket,
                                                        or at the top face
                                                        of the pad. */
  UF_MODL_parm_p_t                taper_angle;       /* The parameter containing
                                                        the angle value for the
                                                        taper, if the
                                                        taper_relative_to setting
                                                        is
                                                        UF_MODL_TAPER_BY_OUTLINE_FACE_NORMALS
                                                        or
                                                        UF_MODL_TAPER_BY_OUTLINE_FIXED_VECTOR
                                                        then this should be an array
                                                        of UF_MODL_parm_t where each
                                                        is a law using the outline
                                                        curve/edge as the spine
                                                        */
  UF_MODL_taper_relative_to_t     taper_relative_to; /* Indication of how the
                                                        taper angle is measured,
                                                        either relative to the
                                                        face normals or to a
                                                        fixed vector. */
  UF_MODL_vector_p_t              taper_vector;      /* The vector from which
                                                        the taper angle is
                                                        measured, if the taper
                                                        is relative to a fixed
                                                        vector. */
};
typedef struct UF_MODL_single_outline_s UF_MODL_single_outline_t;

/* outline_type == UF_MODL_DOUBLE_OUTLINE */
struct UF_MODL_pocketpad_outline_double_outline_s
{
  UF_MODL_project_curves_p_t    placement_curves; /* The curves making up the
                                                     outline for the placement
                                                     faces. */
  UF_MODL_curves_represent_t    placement_curves_represent; /* Indication of
                                                     whether the curves
                                                     represent theoreticals or
                                                     tangents. */
  UF_MODL_project_curves_p_t    floor_top_curves; /* The curves making up the
                                                     outline for the floor/top
                                                     faces. */
  UF_MODL_curves_represent_t    floor_top_curves_represent; /* Indication of
                                                     whether the curves
                                                     represent theoreticals or
                                                     tangents. */
};
typedef struct UF_MODL_pocketpad_outline_double_outline_s
UF_MODL_pocketpad_outline_double_outline_t;

/* outline_type == UF_MODL_SINGLE_OUTLINE_CORNER  or
   outline_type == UF_MODL_SINGLE_OUTLINE_NO_ATTACH */
struct UF_MODL_pocketpad_outline_single_outline_corner_s
{
  UF_MODL_project_curves_p_t      outline_curves;    /* The curves making up the
                                                        outline. */
  UF_MODL_curves_represent_t      curves_represent;  /* Indication of whether
                                                        the curves represent
                                                        theoreticals or tangents
                                                     */
  UF_MODL_outline_represents_t    outline_represents;/* Indication of whether
                                                        this outline is defining
                                                        the shape of the
                                                        pocket/pad at the
                                                        placement face of the
                                                        pocket/pad, at the
                                                        floor face o the pocket,
                                                        or at the top face
                                                        of the pad. */
  UF_MODL_parm_p_t                taper_angle;       /* The parameter containing
                                                        the angle value for the
                                                        taper. */
  UF_MODL_taper_relative_to_t     taper_relative_to; /* Indication of how the
                                                        taper angle is measured,
                                                        either relative to the
                                                        face normals or to a
                                                        fixed vector. */
  UF_MODL_vector_p_t              taper_vector;      /* The vector from which
                                                        the taper angle is
                                                        measured, if the taper
                                                        is relative to a fixed
                                                        vector. */
  UF_MODL_parm_p_t                corner_radius;     /* The parameter containing
                                                        the radius value desired
                                                        for "corner" of
                                                        non-smooth outlines.
                                                        Non-smooth outlines are
                                                        outlines whose curve
                                                        tangents are not within
                                                        angle tolerance across
                                                        their end points. This
                                                        radius is applied on
                                                        the side of the
                                                        pocket/pad at these
                                                        points. */
};
typedef struct UF_MODL_pocketpad_outline_single_outline_corner_s
UF_MODL_pocketpad_outline_single_outline_corner_t;

/* outline_type == UF_MODL_DOUBLE_OUTLINE_CORNER or
   outline_type == UF_MODL_DOUBLE_OUTLINE_NO_ATTACH */
struct UF_MODL_pocketpad_outline_double_outline_corner_s
{
  UF_MODL_project_curves_p_t    placement_curves; /* The curves making up the
                                                     outline for the placement
                                                     faces. */
  UF_MODL_curves_represent_t    placement_curves_represent; /* Indication of
                                                     whether the curves
                                                     represent theoreticals or
                                                     tangents. */
  UF_MODL_project_curves_p_t    floor_top_curves; /* The curves making up the
                                                     outline for the floor/top
                                                     faces. */
  UF_MODL_curves_represent_t    floor_top_curves_represent; /* Indication of
                                                     whether the curves
                                                     represent theoreticals or
                                                     tangents. */
  UF_MODL_parm_p_t              corner_radius;     /* The parameter containing
                                                      the radius value desired
                                                      for "corner" of
                                                      non-smooth outlines.
                                                      Non-smooth outlines are
                                                      outlines whose curve
                                                      tangents are not within
                                                      angle tolerance across
                                                      their end points. This
                                                      radius is applied on
                                                      the side of the
                                                      pocket/pad at these
                                                      points. */
};
typedef struct UF_MODL_pocketpad_outline_double_outline_corner_s
UF_MODL_pocketpad_outline_double_outline_corner_t;

/* Union of the methods to define a pocket/pad. */
union UF_MODL_pocketpad_outline_defined_by_s
{
     UF_MODL_single_outline_t                          single_outline;
     UF_MODL_pocketpad_outline_double_outline_t        double_outline;
     UF_MODL_pocketpad_outline_single_outline_corner_t single_outline_corner;
     UF_MODL_pocketpad_outline_double_outline_corner_t double_outline_corner;
};
typedef union UF_MODL_pocketpad_outline_defined_by_s
UF_MODL_pocketpad_outline_defined_by_t;

/* The general pocket/pad functions use this structure to define the
   outline to specify the shape of the pocket/pad. This structure also
   defines whether the pocket/pad is created with a single outline at
   either the placement faces, or the floor/top faces of the pocket/pad, or
   with outlines at both the placement faces and the floor/top faces of
   the pocket/pad.
*/
struct UF_MODL_pocketpad_outline_s
{
  UF_MODL_pocketpad_type_t outline_type; /* Indication of whether the pocket/pad
                                            is being defined with a single
                                            outline at either the placement face
                                            or the floor/top face of the
                                            pocket/pad, or if the pocket/pad is
                                            being defined with outlines at both
                                            the placement face and the floor/top
                                            face of the pocket/pad.
                                            Also controls if the pocket/pad will
                                            be booleaned to a target solid or
                                            not */
  UF_MODL_pocketpad_outline_defined_by_t  defined_by;
                                         /* The definition of the pocket/pad. */
};
typedef struct UF_MODL_pocketpad_outline_s UF_MODL_pocketpad_outline_t,
*UF_MODL_pocketpad_outline_p_t;

/* This structure is used in creating and inquiring symbolic threads. */
struct UF_MODL_symb_thread_data_s
{
    tag_t            cyl_face;          /* Cylindrical face to be threaded. */
    tag_t            start_face;        /* Face at which the thread starts. */
    double           axis_direction[3]; /* Direction of the thread. */
    int              include_instances; /* Instancing flag, UF_MODL_NO_INSTANCES
                                           means no thread on instances of
                                           cylindrical face.
                                           UF_MODL_INCL_INSTANCES means threads
                                           on instances of the cylindrical face.
                                        */
    int              rotation;          /* Rotation, either UF_MODL_RIGHT_HAND
                                           or UF_MODL_LEFT_HAND. */
    int              length_flag;       /* Indicates the thread is a fixed
                                           length or a full thread.
                                           UF_MODL_FULL_THREAD or
                                           UF_MODL_FIXED_LENGTH. */
    int              tapered;           /* UF_MODL_TAPERED if this is a tapered
                                           thread, UF_MODL_NON_TAPERED if this
                                           is a non tapered thread. */
    int              num_starts;        /* Number of start. */
    char             *length;           /* Expression of the thread length. */
    char             *form;             /* Thread form. */
    char             *method;           /* Thread method. */
    char             *callout;         /* Thread callout.  In creation, if you
                                          specify a callout, the major diameter,
                                          minor diameter, pitch, tapped
                                          drill/shaft diameter, length, and
                                          tapered indicator are read from the
                                          thread table and the values of those
                                          parameters from the structure are
                                          ignored except for the length value.
                                          If the length value is specified in
                                          the structure, it will be used instead
                                          of the one read from the table. If no
                                          callout is specified, the values of
                                          those parameters are used in creating
                                          the thread.  Not specifying a callout
                                          means to pass a NULL pointer, passing
                                          an empty string ("") causes an error.
                                          In Inquiry, if a callout is specified
                                          in creating the thread, those
                                          parameters also return in the
                                          structure together with the callout.
                                       */
    char             *major_dia;       /* Major diameter expression of the
                                          thread. */
    char             *minor_dia;       /* Minor diameter expression of the
                                          thread. */
    char             *tapped_dia;      /* Tapped diameter expression of the
                                          thread. */
    char             *pitch;           /* Thread pitch expression. */
    char             *angle;           /* Thread angle expression. */
    logical          internal_thread;  /* Indicates type of thread.
                                          TRUE for internal thread type else, FALSE*/
};
typedef struct UF_MODL_symb_thread_data_s UF_MODL_symb_thread_data_t,
*UF_MODL_symb_thread_data_p_t;

enum UF_MODL_intersect_type_e
{
    UF_MODL_INTERSECT_POINT,
    UF_MODL_INTERSECT_COINCIDE,
    UF_MODL_INTERSECT_CURVE
};
typedef enum UF_MODL_intersect_type_e UF_MODL_intersect_type_t;


/*intersect_type == UF_MODL_INTERSECT_POINT*/
struct UF_MODL_intersect_info_point_s
{
  double  coords[3];
  double  object_1_u_parm;
  double  object_1_v_parm;
  double  object_2_u_parm;
  double  object_2_v_parm;
};
typedef struct UF_MODL_intersect_info_point_s UF_MODL_intersect_info_point_t;

/*intersect_type == UF_MODL_INTERSECT_COINCIDE*/
struct UF_MODL_intersect_info_coincide_s
{
  tag_t   identifier;
  double  object_1_first_parm;
  double  object_1_second_parm;
  double  object_2_first_parm;
  double  object_2_second_parm;
};
typedef struct UF_MODL_intersect_info_coincide_s
UF_MODL_intersect_info_coincide_t;

/*intersect_type == UF_MODL_INTERSECT_CURVE*/
struct UF_MODL_intersect_info_curve_s
{
  tag_t   identifier;
};
typedef struct UF_MODL_intersect_info_curve_s UF_MODL_intersect_info_curve_t;

union UF_MODL_intersect_info_intersect_s
{
     UF_MODL_intersect_info_point_t     point;
     UF_MODL_intersect_info_coincide_t  coincide;
     UF_MODL_intersect_info_curve_t     curve;
};
typedef union UF_MODL_intersect_info_intersect_s
UF_MODL_intersect_info_intersect_t;

struct UF_MODL_intersect_info_s
{
    UF_MODL_intersect_type_t   intersect_type;
    UF_MODL_intersect_info_intersect_t intersect;
};
typedef struct UF_MODL_intersect_info_s UF_MODL_intersect_info_t,
*UF_MODL_intersect_info_p_t;

/*
  The following structures and typedefs are used by the bead user functions.
*/
enum UF_MODL_bead_width_relative_e
{
    UF_MODL_RELATIVE_THEORETICAL,
    UF_MODL_RELATIVE_TANGENT
};
typedef enum UF_MODL_bead_width_relative_e UF_MODL_bead_width_relative_t;

enum UF_MODL_bead_angle_relative_e
{
    UF_MODL_RELATIVE_CENTERLINE,
    UF_MODL_RELATIVE_WALL
};
typedef enum UF_MODL_bead_angle_relative_e UF_MODL_bead_angle_relative_t;

enum UF_MODL_bead_shape_e
{
    UF_MODL_U_SHAPED,
    UF_MODL_V_SHAPED,
    UF_MODL_CIRCULAR_SHAPED
};
typedef enum UF_MODL_bead_shape_e UF_MODL_bead_shape_t;

enum UF_MODL_bead_plane_normal_e
{
    UF_MODL_TANGENT_ALONG_CENTERLINE,
    UF_MODL_FIXED_DIRECTION
};
typedef enum UF_MODL_bead_plane_normal_e UF_MODL_bead_plane_normal_t;

enum UF_MODL_bead_attach_e
{
    UF_MODL_BEAD_NOT_ATTACHED,
    UF_MODL_BEAD_ATTACHED
};
typedef enum UF_MODL_bead_attach_e UF_MODL_bead_attach_t;

enum UF_MODL_bead_hollow_e
{
    UF_MODL_BEAD_NOT_HOLLOW,
    UF_MODL_BEAD_HOLLOW
};
typedef enum UF_MODL_bead_hollow_e UF_MODL_bead_hollow_t;

enum UF_MODL_bead_ends
{
    UF_MODL_END_CAPS_NONE,
    UF_MODL_END_CAPS_START,
    UF_MODL_END_CAPS_END,
    UF_MODL_END_CAPS_BOTH
};
typedef enum UF_MODL_bead_ends UF_MODL_bead_ends_t;

/* plane_normal_type == UF_MODL_FIXED_DIRECTION */
struct UF_MODL_bead_plane_fixed_s
{
   UF_MODL_vector_p_t   normal_direction;  /* direction info to define
                                              the normal of the
                                              orientation plane of the
                                              bead sections */
};
typedef struct UF_MODL_bead_plane_fixed_s UF_MODL_bead_plane_fixed_t;

union UF_MODL_bead_plane_defined_by_s
{
    UF_MODL_bead_plane_fixed_t fixed;
};
typedef union UF_MODL_bead_plane_defined_by_s UF_MODL_bead_plane_defined_by_t;

/* This structure is used to define the normal of the orientation plane
   for the bead sections. */
struct UF_MODL_bead_section_plane_s
{
    UF_MODL_bead_plane_normal_t  plane_normal_type; /* Indication of how the
                                                       section plan normal is
                                                       being defined, either as
                                                       a tangent along the
                                                       centerline or a fixed
                                                       direction. */

    UF_MODL_bead_plane_defined_by_t defined_by;     /* Additional information
                                                       required if the
                                                       plane_normal_type is
                                                       UF_MODL_FIXED_DIRECTION.
                                                       In this case, this will
                                                       be a pointer to direction
                                                       information which defines
                                                       the fixed normal of the
                                                       orientation plane. */
};
typedef struct UF_MODL_bead_section_plane_s UF_MODL_bead_section_plane_t,
*UF_MODL_bead_section_plane_p_t;

struct UF_MODL_bead_section_parms_s
{
    UF_MODL_bead_shape_t          shape;            /* cross sectional shape
                                                       type of bead  */
    UF_MODL_parm_p_t              radius;           /* radius of the blend
                                                       between bead walls and
                                                       secondary face if one
                                                       is defined or just
                                                       between the bead walls
                                                       if there isn't one */
    UF_MODL_parm_p_t              placement_width;  /* width of the bead in
                                                       the placement face */
    UF_MODL_bead_width_relative_t placement_width_relative; /* Indication of
                                                       how placement width
                                                       is measured.*/
    UF_MODL_parm_p_t              secondary_width;  /* width of the bead in
                                                       the secondary face */
    UF_MODL_bead_width_relative_t secondary_width_relative; /* When a radius
                                                       is specified along with
                                                       a secondary width, this
                                                       defines how the
                                                       secondary width is
                                                       measured. */
    UF_MODL_parm_p_t              taper_angle;      /* angle between the bead
                                                       wall and the section
                                                       axis at the centerline */
    UF_MODL_bead_angle_relative_t taper_angle_relative; /* Indication of how
                                                       the taper angle is
                                                       measured. */
    UF_MODL_parm_p_t              height;           /* height of bead along
                                                       the section axis */
    UF_MODL_parm_p_t              blend_radius;   /* Radius of blend between
                                                     side walls and placement
                                                     faces */
    UF_MODL_parm_p_t              end_cap_radius;   /* Radius of the end caps on
                                                       a circular bead.  This is
                                                       measured tangent to the
                                                       end of the centerline.
                                                       It must be greater than
                                                       the height and the
                                                       radius. */
    UF_MODL_parm_p_t              end_cap_angle;    /* Angle of the end cap
                                                       taper on the v bead */
    UF_MODL_bead_ends_t           end_cap_option;   /* Indicates where end
                                                       caps should be placed
                                                       on the bead          */
    UF_MODL_bead_attach_t         attach;           /* If TRUE, boolean bead
                                                       to the target body.
                                                       If FALSE, a separate body
                                                       will be created.  */
    UF_MODL_bead_hollow_t         hollow;           /* If TRUE, create a hollow
                                                       bead which preserves the
                                                       thickness of the target
                                                       solid body.  Only
                                                       applicable when attach
                                                       is TRUE. */
};
typedef struct UF_MODL_bead_section_parms_s UF_MODL_bead_section_parms_t,
*UF_MODL_bead_section_parms_p_t;


/* The UF_MODL_simpl_data_s structure contains the parametric information used
 * to define a simplification feature.
 *
 * When the simplification feature is applied to a body, certain faces are
 * removed from the body, and the gaps are healed over (creating new faces if
 * necessary).  The faces to be removed are determined as follows:
 *
 * All faces in the array <retained_faces> are retained.
 * Any face that can be reached from another retained face without crossing a
 * boundary edge is retained.
 * All other faces are removed. NOTE: The interactive Simplify dialog
 * automatically adds any boundary face to the retained_faces array. This must
 * be done by the caller of UF_MODL_create_simplify to achieve the same results.
 *
 * The boundary edges are defined as follows:
 *
 * All edges in the array <boundary_edges> are boundary edges.
 * None of the edges in the array <non_boundary_edges> are boundary edges.
 * All edges of faces in the array <boundary_faces>, except those edges in the
 * array <non_boundary_edges>, are also boundary edges.
 * All edges created by imprint features in the array <imprint_features>, except
 * those edges in the array <non_boundary_edges>, are also boundary edges.
 * The edges of holes on the body whose diameter is less than the current value
 * of <max_hole_dia_expression>, except those edges in the array
 * <non_boundary_edges>, are also boundary edges.  (Effectively, such holes are
 * removed.)  A hole is defined to be an inward-pointing full cylindrical face
 * or an inward-pointing full conical face.  To suppress this option, simply
 * pass in an expression evaluating to 0.0 or less.
 *
 * The array <removed_faces> can be used to verify the simplification feature.
 * If any face in it would remain on the solid after the feature were created,
 * the feature is not actually created and the ifail
 * UF_MODL_SIMPL_FACE_NOT_REMOVED is returned.  This also applies if the feature
 * is previewed.
 *
 * The following restrictions apply to simplify parms:
 * A face may be both a retained face and a boundary face, hence the two arrays
 * may have elements in common.
 * A retained or boundary face may not be a removed face.
 * At least one retained face must be supplied.
 * All faces must be on the same body.
 * The <boundary_edges> and the <non_boundary_edges> arrays can have no elements
 * in common.
 *
 * In some cases, one or more faces cannot be removed at all, because the
 * surrounding faces cannot be healed across them, or because this would divide
 * the body into two or more disjoint pieces.  In this case, the ifail
 * UF_MODL_SIMPL_HEAL_FAILED is returned.  These cases cannot be detected by
 * previewing the simplification, only when it is actually applied.
 */
struct UF_MODL_simpl_data_s
{
    int             n_retained_faces;         /* Number of retained faces */
    tag_t          *retained_faces;           /* <len:n_retained_faces> Array of retained faces */
    int             n_boundary_faces;         /* Number of boundary faces */
    tag_t          *boundary_faces;           /* <len:n_boundary_faces> Array of boundary faces */
    int             n_removed_faces;          /* Number of removed faces */
    tag_t          *removed_faces;            /* <len:n_removed_faces> Array of removed faces */
    int             n_boundary_edges;         /* Number of boundary edges */
    tag_t          *boundary_edges;           /* <len:n_boundary_edges> Array of boundary edges */
    int             n_non_boundary_edges;     /* Number of non-boundary edges */
    tag_t          *non_boundary_edges;       /* <len:n_non_boundary_edges> Array of non-boundary edges */
    int             n_imprint_features;       /* Number of imprint features
                                                 to apply */
    tag_t          *imprint_features;         /* <len:n_imprint_features> Array of imprint features
                                                 whose edges are to be
                                                 boundaries */
    tag_t           max_hole_dia_expression;  /* Expression for maximum
                                                 diameter holes to remove */
} ;
typedef struct UF_MODL_simpl_data_s UF_MODL_simpl_data_t,
*UF_MODL_simpl_data_p_t;

/* This structure contains the parametric information used to define an
 * imprint feature which will imprint edges on all the faces connected to
 * <imprint_face> which intersect with <imprint_datum_plane>.  Hence it will
 * define a closed loop on the solid, even if the geometry of the solid is
 * later changed.  It is an error if the face does not intersect
 * <imprint_datum_plane>.
 */
struct UF_MODL_imprint_loop_data_s
{
    tag_t           imprint_face;         /* The face defining the starting
                                             point of the imprint */
    tag_t           imprint_datum_plane;  /* The datum plane of intersection */
};
typedef struct UF_MODL_imprint_loop_data_s UF_MODL_imprint_loop_data_t,
*UF_MODL_imprint_loop_data_p_t;

/* This structure contains the parametric information used to define an
 * imprint feature which will imprint an edge on every face in <imprint_faces>
 * where they intersect with <imprint_datum_plane>.  The faces must all be on
 * the same body.  It is an error if none of the faces intersect
 * <imprint_datum_plane>.
 */
struct UF_MODL_imprint_faces_data_s
{
    int             n_imprint_faces;      /* The number of faces */
    tag_t          *imprint_faces;        /* <len:n_imprint_faces> Array of faces to be imprinted */
    tag_t           imprint_datum_plane;  /* The datum plane of intersection */
};
typedef struct UF_MODL_imprint_faces_data_s UF_MODL_imprint_faces_data_t,
*UF_MODL_imprint_faces_data_p_t;

struct UF_MODL_devchk_ee_info_s
{
    int       dev_type;       /* 0 - no deviation
                               1 - step
                               2 - overlap
                               3 - gap
                              */
    tag_t     face_1_tag;     /* face tag on which edge_1_pnt lies
                              */
    double    edge_1_pnt[3];  /* point on an edge of face_pairs[0] used for
                               deviation checking
                              */
    double    norm_1[3];      /* face normal at edge_1_pnt
                              */
    tag_t     face_2_tag;     /* face tag on which edge_2_pnt lies
                              */
    double    edge_2_pnt[3];  /* point on an edge of face_pairs[1], where the
                               minimum deviation occured from edge_1_pnt
                              */
    double    norm_2[3];      /* face normal at edge_2_pnt
                              */
    double    edge_dist;      /* distance between edge_1_pnt and edge_2_pnt
                              */
    double    norm_angle;     /* Angle between the face normals
                              */
};
typedef struct UF_MODL_devchk_ee_info_s UF_MODL_devchk_ee_info_t,
*UF_MODL_devchk_ee_info_p_t;

/*
  Data for UDFS definition Expression Sets
*/
#define UF_UDFS_EXP         0
#define UF_UDFS_EXP_OPTION  1
#define UF_UDFS_EXP_RANGE   2
struct UF_MODL_udfs_exp_s
{
    int type;            /* UDF expression type:
                            UF_UDFS_EXP: UDF regular expression
                            UF_UDFS_EXP_RANGE: by number range
                            UF_UDFS_EXP_OPTION: by options
                         */
    char *exp;           /* Expression string */

    char exp_name[256];  /* Expression name */
    char **define_value; /* <len:num_def> Array of expression defining values */
    int num_def;         /* Number of expression defining values */
    char low_end[256];   /* Expression minimum value */
    char high_end[256];  /* Expression maximum value */
    int scale_type;      /* Expression value type:
                            scale_type = 0 -> integer
                            scale_type = 1 -> double
                         */
};
typedef struct UF_MODL_udfs_exp_s UF_MODL_udfs_exp_t, *UF_MODL_udfs_exp_p_t;

/*
  Data for UDFS definition.
*/
struct UF_MODL_udfs_def_data_s
{
    tag_t *frecs;                   /* <len:num_frecs> Array of UDF member features */
    int num_frecs;                  /* Number of UDF member features */
    UF_MODL_udfs_exp_p_t *exp_defs; /* <len:num_exp> Array of UDF expressions */
    int num_exp;                    /* Number of UDF expressions */
    tag_t *refs;                    /* <len:num_ref> Array of UDF parents */
    char **ref_prompts;             /* <len:num_ref> Array of UDF parent prompting strings */
    int num_ref;                    /* Number of UDF parents */
    char name_str_data[256];        /* UDF definition feature name */
    logical explosion_flag;         /* Flag of UDF explosion */
};
typedef struct UF_MODL_udfs_def_data_s UF_MODL_udfs_def_data_t,
*UF_MODL_udfs_def_data_p_t;

/********************************************************************
This structure contains UDF expression information:
old_exps: At the instantiation, they can be obtained from
          the UDF feature definition by calling the public API
          routine UF_MODL_init_udf_insert_data_from_def().

          At the editing, they can be obtained from the UDF
          instantiated feature by calling the public API routine
          UF_MODL_ask_instantiated_udf().

new_exp_values: They can be inputted by the user for both of
                instantiation and editing.
*********************************************************************/
struct UF_MODL_udf_exp_data_s
{
    int   num_exps;         /* Number of expressions */
    tag_t *old_exps;        /* <len:num_exps> Array of udf definition expression */
    char  **new_exp_values; /* <len:num_exps> Array of new expression new values
                               only the right hand side
                            */
};
typedef struct UF_MODL_udf_exp_data_s UF_MODL_udf_exp_data_t,
*UF_MODL_udf_exp_data_p_t;


/*********************************************************************
This structure contains UDF parent direction information:
Currently there are the following 2 ways to deal with the direction
for both of instantiation and editing:

(1) Keep the same UDF parent direction.
(2) Reverse the UDF parent direction.
*********************************************************************/
enum UF_MODL_udf_reverse_dir_e
{
   UF_MODL_UDF_KEEP_DIR = 0,  /* Keep the UDF parent direction */
   UF_MODL_UDF_REVERSE_DIR    /* Reverse the UDF parent direction */
};
typedef enum UF_MODL_udf_reverse_dir_e UF_MODL_udf_reverse_dir_t;


/*

    */

/* 
 */
/*********************************************************************
This structure contains UDF parent's mapping data information:

num_mapping_objs: At the instantiation, this number of mapping objects
                  can be obtained by calling the public API routine
                  UF_MODL_init_udf_insert_data_from_def(). At the editing,
                  it can be obtained by calling the public API routine
                  UF_MODL_ask_instantiated_udf().

reverse_objs_dir: must be inputted by the user for both of instantiation
                  and editing.

For the UDF parent's types: Edges, Curves, Points. There is no need to
prepare the mapping data.

For the UDF parent's types: Faces, Bodies, Sketches, Feature curves and
output objects of Smart Collectors. If there is a need to do the mapping
at the instantiation or editing, then use these 2 arrays: old_output_objs[]
and new_output_objs[] to store the objects that need to be mapped:

At the instantiation, the array old_output_objs[] can be obtained
(i.e. memory allocation and content) from the UDF feature definition by
calling the public API routine UF_MODL_init_udf_insert_data_from_def().
The memory of array new_output_objs[] must be allocated by the user and
its content must be also inputted by the user.

At the editing, the array old_output_objs[] can be obtained (i.e. memory
allocation and content) from the UF_MODL_ask_instantiated_udf(). The memory
of array new_output_objs[] must be allocated by the user and its content
must be also inputted by the user.

For the UDF parent's types: Output curves of Smart Sections. The user has to
prepare the mapping data. If there is a need to do the mapping at the
instantiation or editing, then use these 2 arrays: old_output_objs_index[]
and new_output_objs_index[] to store the Smart Section's output objects
that need to be mapped. Note that these output objects are condemned, which
are not displayed (i.e., invisible). They can't be used or destroyed for
further applications:

At the instantiation, the array old_output_objs_index[] can be obtained
(i.e. memory allocation and content) from the UDF feature definition by
calling the public API routine UF_MODL_init_udf_insert_data_from_def().
The memory of array new_output_objs_index[] must be allocated by the user
and its content must be also inputted by the user.

At the editing, the array old_output_objs_index[] can be obtained (i.e. memory
allocation and content) from the UF_MODL_ask_instantiated_udf(). The memory of
array new_output_objs_index[] must be allocated by the user and its content
must be also inputted by the user.
************************************************************************/
struct UF_MODL_udf_mapping_data_s
{
    /* This data is to specify how many objects that need to be mapped
       during the mapping process
    */

    int num_mapping_objs;                        /* Number of mapping objects */

    /* This data is only used for reversing the direction of
       mapping objects
    */

    UF_MODL_udf_reverse_dir_t *reverse_objs_dir; /*<len:num_mapping_objs> Rev. mapping obj. dir. flags */

    /* This data is only used for UDF parent's objects that need
       to be mapped
    */

    union
    {
       /* These data are only used for the following mapping objects:
          Faces, Bodies, Sketches, Feature Curves, ... and
          Ouput objects of Smart Collectors.
       */

       struct
       {
            tag_t *old_output_objs;
            /* Array of mapping objects of an old parent
               To fill out this array, please see the above comments.
            */

            tag_t *new_output_objs;
            /* Array of mapping objects of a new parent.
               To fill out this array, please see the above comments.
            */

       } output_objs_non_ss;

       /* These data are only used for the following mapping objects:
          Output objects of Smart Sections (these objects are condemned,
          which are not displayed (i.e. invisible)).

          Note that these output objects can't be used or destroyed
          for further applications.
       */

       struct  /* Only for Smart Sections */
       {
            int *old_output_objs_index;
            /* Array of index of Smart Section's output objects of an old parent.
               To fill out this array, please see the above comments.
            */

            int *new_output_objs_index;
            /* Array of index of Smart Section's output objects of a new parent.
               To fill out this array, please see the above comments.
            */

       } output_objs_ss;

    } defined_by;

};
/*

*/

typedef struct UF_MODL_udf_mapping_data_s
               UF_MODL_udf_mapping_data_t, *UF_MODL_udf_mapping_data_p_t;


/**************************************************************************
This structure contains UDF parents information:

This information consists of UDF parents, parent's direction data and
parent's mapping data.

Instantiation:

old_refs: can be obtained from the UDF feature definition.
new_refs: can be inputted by the user.
reverse_refs_dir: can be inputted by the user.
mapping_data: some of them must be inputted by the user (please see all the
comments about the data structure UF_MODL_udf_mapping_data_t).

Edit (from a UDF instantiated feature):

old_refs: can be obtained from the UDF instantiated feature.
new_refs: can be inputted by the user.
reverse_refs_dir: can be inputted by the user.
mapping_data: some of them must be inputted by the user (please see all the
comments about the data structure UF_MODL_udf_mapping_data_t).

Ask (from a UDF instantiated feature):

old_refs: can be obtained from the UDF instantiated feature.
new_refs: must be NULL.
reverse_refs_dir: can be obtained from the UDF instantiated feature.
mapping_data: can be obtained from the UDF instantiated feature.
**************************************************************************/
struct UF_MODL_udf_ref_data_s
{
    int   num_refs;                           /* Number of UDF parents */
    tag_t *old_refs;                          /* <len:num_refs> Array of old parents */
    tag_t *new_refs;                          /* <len:num_refs> Array of new parents */
    UF_MODL_udf_reverse_dir_t *reverse_refs_dir;/* <len:num_refs>Array of rev. parent. dir. flags */
    UF_MODL_udf_mapping_data_t *mapping_data; /* <len:num_refs>Mapping data */
};
typedef struct UF_MODL_udf_ref_data_s UF_MODL_udf_ref_data_t,
*UF_MODL_udf_ref_data_p_t;

/*
   Typedef for a UDF mapping routine function pointer.
 */

typedef int (*UF_MODL_udf_mapping_f_p_t) (tag_t, UF_MODL_udf_ref_data_p_t);

/* Define the data for a Rough Offset feature. */
typedef enum
{
    UF_RSO_SURF_METHOD_CLOUD = 0,
    UF_RSO_SURF_METHOD_THRU,
    UF_RSO_SURF_METHOD_ROUGH_FIT,
    UF_RSO_NUM_SURF_METHOD_OPTIONS
} UF_RSO_surf_method_t;

typedef enum
{
    UF_RSO_SURF_CTRL_BY_SYSTEM = 0,
    UF_RSO_SURF_CTRL_BY_USER,
    UF_RSO_NUM_SURF_CTRL_OPTIONS
} UF_RSO_surf_ctrl_option_t;

typedef enum
{
    UF_RSO_TRIM_OPT_NO = 0,
    UF_RSO_TRIM_OPT_YES,
    UF_RSO_TRIM_OPT_BND_CURVE,
    UF_RSO_NUM_TRIM_OPTS
} UF_RSO_trim_option_t;

struct UF_MODL_rough_offset_s
{
    tag_t                          *entities;
                                   /* <len:num_entities> Offset entities: face or sheet body */
    int                            num_entities;
                                   /* Number of offset entities */
    tag_t                          smart_csys;
                                   /* The tag for a coordinate system, of which
                                      Z axis indicates the offset direction,
                                      X axis the stepping direction, and Y axis
                                      the stepover direction.  WCS would be
                                      used if NULL_TAG */
    char                           offset_distance[ UF_MAX_EXP_BUFSIZE ];
                                   /* Offset distance */
    char                           offset_deviation[ UF_MAX_EXP_BUFSIZE ];
                                   /* Offset distance deviation */
    char                           stepover_distance[ UF_MAX_EXP_BUFSIZE ];
                                   /* Stepover distance */
    UF_RSO_surf_method_t           surf_method;
                                   /* Surface generation method:
                                      UF_RSO_SURF_METHOD_CLOUD: Cloud Points
                                      UF_RSO_SURF_METHOD_THRU: Through Curves
                                      UF_RSO_SURF_METHOD_ROUGH_FIT: Rough Fit
                                   */
    UF_RSO_surf_ctrl_option_t      surf_ctrl_type;
                                   /* Surface control type:
                                      UF_RSO_SURF_CTRL_BY_SYSTEM: System Defined
                                      UF_RSO_SURF_CTRL_BY_USER: User Defined
                                      It is used only when surf_method is
                                      UF_RSO_SURF_METHOD_CLOUD
                                   */
    int                            u_patches;
                                   /* Number of U patches when the surface
                                      control type UF_RSO_SURF_CTRL_BY_USER */
    UF_RSO_trim_option_t           boundary_trim;
                                   /* Boundary trimming option:
                                      UF_RSO_TRIM_OPT_NO: No Trimming
                                      UF_RSO_TRIM_OPT_YES: Trimming
                                      UF_RSO_TRIM_OPT_BND_CURVE: Boundary Curve
                                      only
                                   */
};
typedef struct UF_MODL_rough_offset_s
               UF_MODL_rough_offset_t, *UF_MODL_rough_offset_p_t;

/* Direction reference options used for creation of
the law extension surface. */
enum UF_MODL_lawext_dirref_e
{
   UF_MODL_lawext_dirref_face = 0, /* Existing face(s) or sheet(s)
                                   */
   UF_MODL_lawext_dirref_vector    /* Smart vector
                                   */
};
typedef enum UF_MODL_lawext_dirref_e UF_MODL_lawext_dirref_t;

/* Following is a structure definition for law extension feature data.
It includes all the input elements to create a law controlled extension
surface.

Minimum four parameters are required to be specified. The base curve, one
of the options in direction reference, length law and angle law are required
for creation of the feature. The law parameters, length_law_parms and
angle_law_parms may be defined using UF_MODL_create_law ( ).

The specification of spine is optional and can be specified at following
three places.
1. Feature spine
2. Length law spine
3. Angle law spine
It is necessary that spine should be unique where ever specified. Only feature
can have spine specified but only law(s) cannot have spine specified.*/
struct UF_MODL_lawext_data_s
{
   UF_MODL_lawext_dirref_t ref_type; /* Direction reference type
                                     */
   void *length_law_parms;           /* For the specification of
                                        length law parameters */
   void *angle_law_parms;            /* For the specification of
                                        angle law parameters */
   UF_STRING_p_t curve;              /* Pointer to string for base curve
                                        from which extension surface will
                                        be created */
   int n_faces;                      /* Number of faces used for direction
                                        reference.
                                        A face collection may be used as the
                                        one and only member of the array.
                                        Will be zero if direction
                                        reference type is not set to
                                        UF_MODL_lawext_dirref_face */
   tag_t *face_ids;                  /* <len:n_faces>
                                        Array of n_faces number of tags used
                                        for direction reference. Only used if
                                        direction reference type is set to
                                        UF_MODL_lawext_dirref_face */
   tag_t smart_dir;                  /* Smart direction vector tag. Only used
                                        if  direction reference type is set to
                                        UF_MODL_lawext_dirref_vector */
   UF_STRING_p_t spine;              /* Pointer to spine string (optional).
                                        If set to NULL, curve is used as spine */
   double distance_tol;              /* Distance tolerance
                                     */
   double angle_tol;                 /* Angle tolerance
                                     */
   int merge;                        /* Merge faces
                                     */
   int bisided;                      /* Extend on both sides or not
                                     */
};
typedef struct UF_MODL_lawext_data_s UF_MODL_lawext_data_t,
*UF_MODL_lawext_data_p_t;


/*  Data structure for matchedge
    all data members should be set except for the following:
    when match target_type is not 3, match_dir_vector_tag is not used.
    when flow_control[0]/flow_control[1] is not 4,
         adjacent_vec[0]/adjacent_vec[1] is not used.
    when limit_pole_move is not 2, move_direction_tag is not used.
*/
struct UF_MODL_matchedge_data_s
{
    tag_t          edit_edge_tag;                /* the edge to be edited */
    int            match_target_type;            /* 0:edge, 1:face, 2:curve, 3:datum*/
    int            match_continuity[4];          /* on/off for G0, G1, G2 and G3 */
    tag_t          match_dir_vector_tag;         /* direction tag if match with vector */
    int            count_of_targets;             /* number of target entity */
    tag_p_t        target_entity_tags;           /* <len:count_of_targets> edge, face, curve or datum tags */
    int            flow_control[2];              /* flow control: start and end edge
                                                    0-     no, 1-perpend, 2-IsoU, 3-IsoV , 4-adjacent*/
    double         adjacent_vec[2][3];           /* direction of adjacent direction*/
    int            side_lock[2];                 /* start or end side lock on/off */
    int            opposite_lock;                /* opposite lock: 0:no, 1:G0, 2:G1, 3:G2, 4:G3 */
    int            match_exact;                  /* exact on/off */
    int            match_end_to_end;             /* end to end on/off */
    int            limit_pole_move;              /* limit pole movement: 0-no limit, 1-project, 2-use vector,
                                                    3-fix begin, 4-fix end, 5-fix both */
    tag_t          move_direction_tag;           /* direction tag if limit pole move */
    int            match_edge_degree;            /* degree of the edit edge*/
    int            match_edge_patches;           /*number of Bezier patches along edit edge*/
    int            lateral_edge_degree;          /*degree of the lateral edges*/
    int            lateral_edge_patches;         /*number of Bezier patches along lateral edges*/

};
typedef struct UF_MODL_matchedge_data_s
               UF_MODL_matchedge_data_t, *UF_MODL_matchedge_data_p_t;

/** data structure for Refit Face **/

/* Refitting direction */
enum UF_MODL_refit_face_refit_direction_e
{
   UF_MODL_refit_face_refit_direction_UV = 0, /* Both U and V */
   UF_MODL_refit_face_refit_direction_U,      /* U */
   UF_MODL_refit_face_refit_direction_V       /* V */
};
typedef enum UF_MODL_refit_face_refit_direction_e UF_MODL_refit_face_refit_direction_t;

/* Refitting method (control refit by...) */
enum UF_MODL_refit_face_refit_method_e
{
   UF_MODL_refit_face_refit_method_deg_patch = 0, /* Specify degree and number of patches */
   UF_MODL_refit_face_refit_method_deg_tol,       /* Specify degree and tolerance */
   UF_MODL_refit_face_refit_method_patch_tol,     /* Specify number of patches and tolerance */
   UF_MODL_refit_face_refit_method_keep_parameterization      /* Keep parameterization */
};
typedef enum UF_MODL_refit_face_refit_method_e UF_MODL_refit_face_refit_method_t;

/* Fitting direction (only with target) */
enum UF_MODL_refit_face_fit_direction_e
{
   UF_MODL_refit_face_refit_direction_no_direction = 0,  /* No direction */
   UF_MODL_refit_face_refit_direction_x_direction,       /* x direction */
   UF_MODL_refit_face_refit_direction_y_direction,       /* y direction */
   UF_MODL_refit_face_refit_direction_z_direction,       /* z direction */
   UF_MODL_refit_face_refit_direction_view_direction     /* view direction */
};
typedef enum UF_MODL_refit_face_fit_direction_e UF_MODL_refit_face_fit_direction_t;

/* Boundary continuity */
enum UF_MODL_refit_face_continuity_e
{
   UF_MODL_refit_face_continuity_free = 0, /* No constraint */
   UF_MODL_refit_face_continuity_G0,       /* G0 continuity */
   UF_MODL_refit_face_continuity_G1,       /* G1 continuity */
   UF_MODL_refit_face_continuity_G2        /* G2 continuity */
};
typedef enum UF_MODL_refit_face_continuity_e UF_MODL_refit_face_continuity_t;

/*
Following is a structure definition for refit face target data.

Parameters are to be specified as follows:
1.Number of target objects
2.Target objects
3.Fit direction
4.Maximum checking distance (any positive number)
*/
struct UF_MODL_refit_face_target_data_s
{
   int            n_target_obj;            /* Number of target objects */
   tag_t          *target_obj;             /* <len:n_target_obj> Target objects */
   UF_MODL_refit_face_fit_direction_t fit_direction_data;      /* Fit direction */
   double         max_checking_data;  /* Maximum checking distance */
};
typedef struct UF_MODL_refit_face_target_data_s UF_MODL_refit_face_target_data_t,
*UF_MODL_refit_face_target_data_p_t;


/*
Following is a structure definition for refit face feature data.
It includes all the input elements to create a Refit Face feature.

Parameters are to be specified as follows:
1.Face
2.Target data
3.Refit direction
4.Refit method
5.Desired U degree (integer between 1 and 24)
6.Desired U number of patches (positive integer)
7.Desired V degree (integer between 1 and 24)
8.Desired V number of patches (positive integer)
9.umin edge continuity
10.umax edge continuity
11.vmin edge continuity
12.vmax edge continuity
13.Tolerance (any number larger than 0)
14.Smoothness (any number between 0 and 100)
15.Modification percentage (any number between 0 and 100)

*/
struct UF_MODL_refit_face_data_s
{
   tag_t                face;                /* NX eid of a face to be refit */
   UF_MODL_refit_face_target_data_p_t  target_data;  /* target data */

   int                  direction_data;      /* Surface refitting direction */
   int                  method_data;         /* Surface refitting method */
   int                  u_deg_int_data;      /* Degree in U */
   int                  u_patch_int_data;    /* Number of patches in U */
   int                  v_deg_int_data;      /* Degree in V */
   int                  v_patch_int_data;    /* Number of patches in V */
   UF_MODL_refit_face_continuity_t umin_cnstr_data;     /* umin edge continuity */
   UF_MODL_refit_face_continuity_t umax_cnstr_data;     /* umax edge continuity */
   UF_MODL_refit_face_continuity_t vmin_cnstr_data;     /* vmin edge continuity */
   UF_MODL_refit_face_continuity_t vmax_cnstr_data;     /* vmax edge continuity */
   double               tolerance_real_data; /* Tolerance */
   double               smoothness_real_data; /* Smoothness (only with target) */
   double               percentage_real_data; /* Modification percentage (only with target) */
};
typedef struct UF_MODL_refit_face_data_s UF_MODL_refit_face_data_t,
*UF_MODL_refit_face_data_p_t;



/* Enumarations and data structure for Snip Surface feature */

/* Bounding object types used for snipping a surface */
enum UF_MODL_snipsurf_boundary_type_e
{
    UF_MODL_snipsurf_boundary_type_curves = 0,      /* Curves or Edges*/
    UF_MODL_snipsurf_boundary_type_plane            /* Plane */
};
typedef enum UF_MODL_snipsurf_boundary_type_e
             UF_MODL_snipsurf_boundary_type_t;

/* Refitting method used to create new snipped surfaces.
   Quality of the resultant surface depends on the refit method used. */

enum UF_MODL_snipsurf_refit_method_e
{
    UF_MODL_snipsurf_refit_method_none = 0,    /* None, no surface refitting done. Resultant
                                                  surface has same number of degree and patches
                                                  as the original surface.*/
    UF_MODL_snipsurf_refit_method_deg_patch,   /* Specify degree and patches for the resultant
                                                  surface */
    UF_MODL_snipsurf_refit_method_deg_tol,     /* Specify degree and distance tolerance for
                                                  the resultant surface*/
    UF_MODL_snipsurf_refit_method_patch_tol    /* Specify patches and distance tolerance for
                                                  the resultant surface*/
};
typedef enum UF_MODL_snipsurf_refit_method_e
             UF_MODL_snipsurf_refit_method_t;

/**********************************************************************************
Structure definition for Snip Surface feature data. It includes all the input
elements to create a Snip Surface feature.

Minimum five parameters are required to be specified as follows:
1.Edit face
2.One of the types of bounding objects
3.Type of operation (snipping or divide)
4.Region point
5.Surface refitting method

In case of divide operation,two snip surface features are created. During
feature editing user cannot change operation type from snip to divide or viseversa.
***********************************************************************************/
struct UF_MODL_snipsrf_feature_data_s
{
    tag_t                              edit_face;          /* NX eid of a face to be snipped */
    UF_MODL_snipsurf_boundary_type_t   boundary_type;      /* Snipping bounding object type  */
    UF_STRING_t                        snip_cv_string;     /* Profile defining the snip curve */
    tag_t                              snipping_plane;     /* NX eid of plane used as snipping object,
                                                              Used only if boundary_type is,
                                                              UF_MODL_snipsurf_boundary_type_plane */
    double                          project_vector[3];     /* Projection vector,
                                                              Necessary only if boundary_type is,
                                                              UF_MODL_snipsurf_boundary_type_curves */
    int                                 snip_or_divide;    /* Flag indicating snipping or divide operation,
                                                              0: Divide, otherwise Snipping operation
                                                              Does not play any role during snip surface
                                                              feature editing */
    double                          region_point_uv[2];    /* Region point on the edit_face indicating the
                                                              retained side of the face divided by imprinted
                                                              snipping curve. uv[0]: U value, uv[1]: V value
                                                              on the surface corresponding to edit_face.
                                                              Does not play any role if snip_or_divide value
                                                              is zero i.e. divide operation. */

    int                                 project_method;    /* Project methods:
                                                               0- along surface normal,
                                                               1- along view direction,
                                                               2- along x direction,
                                                               3- along y direction,
                                                               4- along z direction,
                                                               5- along given vector */
    UF_MODL_snipsurf_refit_method_t    refit_method;       /* Surface refitting method */
    int                                refit_degree;       /* Refit direction degree,
                                                              Necessary if refit_type is,
                                                              UF_MODL_snipsurf_refit_method_deg_patch or
                                                              UF_MODL_snipsurf_refit_method_deg_tol */
    int                                refit_patches;      /* Refit direction patches,
                                                              Necessary if refit_type is,
                                                              UF_MODL_snipsurf_refit_method_deg_patch or
                                                              UF_MODL_snipsurf_refit_method_patch_tol */
    double                             tols[2];            /* Tolerance used for refitting,
                                                              Necessary if refit_type is,
                                                              UF_MODL_snipsurf_refit_method_deg_tol or
                                                              UF_MODL_snipsurf_refit_method_patch_tol */

};
typedef struct UF_MODL_snipsrf_feature_data_s
               UF_MODL_snipsrf_feature_data_t, *UF_MODL_snipsrf_feature_data_p_t;

/* The data structure for the Spherical Corner feature. To create a feature,
a face collector for each wall must be provided.  It can contain faces from
different bodies but the body being use to indicate the wall normal must be
specified through wall_x_ref_body and the reserve flag through is_wall_x_reversed.
When multiple solutions exist, a help point is required to determine the
nearest result.
*/
struct UF_MODL_spherical_corner_s
{
    double dist_tol;               /* The distance tolerance */
    double angle_tol;              /* The angle tolerance */
    char radius[ UF_MAX_EXP_BUFSIZE ];   /* The radius of the spherical corner */
    tag_t wall_1;                  /* The face collector of Wall 1 */
    tag_t wall_2;                  /* The face collector of Wall 2 */
    tag_t wall_3;                  /* The face collector of Wall 3 */
    tag_t wall_1_ref_body;         /* The reference body for determining the normal of Wall 1 */
    tag_t wall_2_ref_body;         /* The reference body for determining the normal of Wall 2 */
    tag_t wall_3_ref_body;         /* The reference body for determining the normal of Wall 3 */
    logical is_wall_1_reversed;    /* Reverse flag of Wall 1 based on the reference body */
    logical is_wall_2_reversed;    /* Reverse flag of Wall 2 based on the reference body */
    logical is_wall_3_reversed;    /* Reverse flag of Wall 3 based on the reference body */
    tag_t help_point;              /* Help point to determine the nearest result when multiple solutions exist */
};
typedef struct UF_MODL_spherical_corner_s
               UF_MODL_spherical_corner_t, *UF_MODL_spherical_corner_p_t;

/* Silhouette flange types */
enum UF_MODL_sflange_type_e
{
    UF_MODL_sflange_basic = 0,    /* Basic silhouette flange */
    UF_MODL_sflange_absolute_gap, /* Absolute gap silhouette flange */
    UF_MODL_sflange_visual_gap    /* Visual gap silhouette flange */
};
typedef enum UF_MODL_sflange_type_e
             UF_MODL_sflange_type_t;

/* Silhouette flange reference direction options */
enum UF_MODL_sflange_dir_e
{
    UF_MODL_sflange_dir_normal = 0, /* Use the normal of faces.
                                       This method is not for a visual gap
                                       silhouette flange. */
    UF_MODL_sflange_dir_vector,      /* Use a (smart) vector.
                                        A visual gap silhouette flange must use
                                        this method. */
    UF_MODL_sflange_dir_normal_draft, /* Use the normal of faces to define
                                         the dummy flange and create the final
                                         flange with draft method. */
    UF_MODL_sflange_dir_vector_draft  /* Use the vector to define the dummy
                                         flange and create the final flange
                                         with the draft method. */
};
typedef enum UF_MODL_sflange_dir_e UF_MODL_sflange_dir_t;

/* Silhouette flange trimming and attachment options */
enum UF_MODL_sflange_trim_e
{
    UF_MODL_sflange_no_trim_sew = 0, /* No trim and sew */
    UF_MODL_sflange_trim_sew,     /* Base faces and pipe are trimmed.
                                     Base faces, pipe and flange faces
                                     are sewed together. */
    UF_MODL_sflange_no_sew,       /* Base faces and pipe are trimmed, but
                                     only pipe and flange faces are sewed. */
    UF_MODL_sflange_no_trim       /* Base faces are not trimmed.
                                     The pipe and flange faces are trimmed
                                     and sewed. */
};
typedef enum UF_MODL_sflange_trim_e UF_MODL_sflange_trim_t;

/* Silhouette flange continuity options */
enum UF_MODL_sflange_continuity_e
{
    UF_MODL_sflange_continuity_g0 = 0, /* G0 */
    UF_MODL_sflange_continuity_g1,     /* G1 */
    UF_MODL_sflange_continuity_g2      /* G2 */
};
typedef enum UF_MODL_sflange_continuity_e UF_MODL_sflange_continuity_t;

/* Data structure for creating a silhouette flange feature. */
struct UF_MODL_sflange_data_s
{
    UF_MODL_sflange_type_t type;     /* Silhouette flange type */
    UF_MODL_sflange_dir_t  dir_opt;  /* Reference direction method.
                                        It's the view direction if creating
                                        a visual gap silhouette flange. */
    UF_MODL_sflange_trim_t trim_opt; /* Trimming and attachment option */
    UF_MODL_sflange_continuity_t base_cont;  /* Continuity between base faces
                                                and blend */
    UF_MODL_sflange_continuity_t flange_cont;/* Continuity between blend and
                                                flange */
    int base_scale;              /* transition scale to the flange */
    int flange_scale;            /* transition scale to the base faces */
    tag_t feature_tag;           /* An existing silhouette flange which is
                                    referenced by the gap based silhouette flange.
                                    NULL_TAG if creating a basic silhouette
                                    flange. */
    UF_STRING_p_t curve;         /* Pointer to the base curves if creating
                                    a basic silhouette flange.
                                    No curves are needed for a gap-based
                                    silhouette flange. Set #curve = 0. */
    int n_faces;                 /* Number of the base faces */
    tag_t *face_tags;            /* Tag array of the base faces */
    tag_t vec_tag;               /* Smart vector tag if the reference direction
                                    is a smart vector.
                                    NULL_TAG if the reference direction method
                                    is face normal. */
    double radius;               /* Radius of the constant radius pipe. */
    double gap;                  /* Gap of a gap-based silhouette flange. */
    tag_t  centerline_tag;       /* Centerline curve of the pipe of
                                    the silhouette flange. The length & angle
                                    laws will be created using this curve. */
    void *radius_law_parms;      /* Radius law parameters. */
    void *length_law_parms;      /* Length law parameters. */
    void *angle_law_parms;       /* Angle law parameters. */
    double distance_tol;         /* Distance tolerance */
    double angle_tol;            /* Angle tolerance */
    double vec_0[3];             /* Zero-degree vector at the middle point of
                                    the pipe's centerline of the referenced
                                    silhouette flange.
                                    It's parallel to the face normal or the
                                    smart vector dependent upon the reference
                                    direction method.
                                    This is needed only if creating a gap-based
                                    silhouette flange. */
    double vec_90[3];            /* 90-degree vector at the middle point of
                                    the pipe's centerline of the referenced
                                    silhouette flange.
                                    It's parallel to the cross-product of the
                                    curve tangent and the face normal or
                                    the smart vector dependent upon the
                                    reference direction method.
                                    This is needed only if creating a gap-based
                                    silhouette flange. */
    logical merge_faces;         /* If TRUE, merge faces whenever possible.
                                    If FALSE, don't merge faces. */
    logical create_pipe_only;    /* If TRUE, only create the pipe, i.e.
                                    no flange faces will be created.
                                    If FALSE, both the fillet and flange faces
                                    will be created. */
    logical flip_dir;            /* If TRUE, flip the side where the pipe
                                    and flanges to be created wrt base faces. */
    logical flip_side;           /* If TRUE, flip the side where the pipe
                                    and flanges to be created wrt to the edges
                                    or the pipe of the referenced silhouette
                                    flange. */
    logical extend_pipe;         /* If TRUE, extend the tube to the boundary
                                    edges of the base faces at both ends. */
};
typedef struct UF_MODL_sflange_data_s
               UF_MODL_sflange_data_t, *UF_MODL_sflange_data_p_t;



/******************************************************************
Data Structure definitions for Styled Corner Surface feature
*******************************************************************/

/******************************************************************
Structure to store the curve control option and corresponding
parameters for top curve, bottom curve, interior u-curve and
v-curve.
******************************************************************/
struct UF_MODL_stycorner_crv_opt_s
{
    int         shape_control;  /**********************************
                                0:  depth & skew,             *
                                1:  Tangent magnitude,        *
                                2:  Template                  *
                                If shape_control is 2 (template),
                                then there is no need to set
                                the rest of the data structure
                                *******************************/
    double      start_tagmag;   /* start tangent magnitude    *
                                   must be set if
                                   shape_control is 1 (tangent magnitude),
                                 ****************************************/
    double      end_tagmag;     /* end tangent magnitude                *
                                   must be set if
                                   shape_control is 1 (tangent magnitude),
                                 ****************************************/
    double      depth;          /* depth of curve                   *
                                   must be set if
                                   shape_control is 0 (depth & skew),
                                 ************************************/
    double      skew;           /* skew of curve                    *
                                   must be set if
                                   shape_control is 0 (depth & skew),
                                 ************************************/
};
typedef struct UF_MODL_stycorner_crv_opt_s
               UF_MODL_stycorner_crv_opt;


/******************************************************************

Data structure definition for Styled Corner Surface feature data.

This data structure includes all the input elements to create
a Styled Corner Surface feature.

The following 2 parameters are part specific and must be
specified as follows:

1.  blend_faces[3]  -- three face ug_tags
2.  base faces info -- a) number of base faces > 0 &
                       b) the corresponding  array of ug_tags.

The following parameters should also be set correctly, at least,
they should be set to the suggested default values:

*  interior curve control options  (value range: 0,1,2,3)
*
*  UF_MODL_stycorner_crv_opt   crv_opt[4]
*
*  boundary conditions/continuity (0=G0, 1=G1, 2=G2)
*  G0 tolerance
*  G1 tolerance
*  trim & attach  option   (either 0 or 1)
*  split vertex control parameters (percent)
*  type of face option:    3-sided surface or a 4-sided surface
*  2 trim curve creation options (value range: 0,1,2)
*  2 interior iso-u-curve end parameters (percent)
*  2 interior iso-v-curve end parameters (percent)

***************************************************************/
struct UF_MODL_stycorner_data_s
{

    tag_t   blend_faces[3]; /* three input faces bounding/defining
                            the corner (in any order):
                            0 - blend face 1,
                            1 - blend face 2,
                            2 - blend face 3          */

    int     num_base_faces;  /* number of base faces      */
    tag_t   *base_faces;     /* <len:num_base_faces> tags of base faces        */

    double  split_curve_params[2]; /* two normalized input parameters
                                   for the split vertex: [0.0, 1.0]:
                                   0 - vertex on face 1,
                                   1 - vertex on face 2 *************/

    int     interior_opt;   /*  use interior curve control options:
                            0 - none,
                            1 - iso-u curve,
                            2 - iso-v curve,
                            3 - iso-u  curve and iso-v  curve    */

    int     boundary_conds[4];  /* curves boundary conditions
                                value:
                                0 -- G0,
                                1 -- G1,
                                2 -- G2
                                index ==
                                0 -- trim curve1,
                                1 -- trim curve2,
                                2 -- bottom curve,
                                3 -- top curve               */
    int     trim_attach_opt;  /* trim & attach  option:
                              0 -- no trim,
                              1 -- trim all    *********/

    double  dist_tol;         /* G0 tolerance    */
    double  angle_tol;        /* G1 tolerance    */

    logical is_rectangular; /*  create a 3-sided surface
                            or a 4-sided surface:
                            0 -- 3-sided surface,
                            1 -- 4-sided surface              */

    UF_MODL_stycorner_crv_opt   crv_opt[4];
                                     /********************
                                     0 -- trim curve1,
                                     1 -- trim curve2,
                                     2 -- bottom curve,
                                     3 -- top curve      */

    int     trim_curve_opt[2]; /* 2 trim curve creation options
                               value = 0 -- Tangent Continuous,
                               value = 1 -- Line projection,
                               value = 2 -- Isoparametric    ****/

    double  interior_iso_u_crv_end_params[2];
                              /* interior u_curve end
                              params (percent):
                              index = 0 -- Start param, percent,
                              index = 1 -- End   param, percent  ****/

    double  interior_iso_v_crv_end_params[2];
                              /* interior v_curve end
                              params (percent):
                              index = 0 -- Start param, percent,
                              index = 1 -- End   param, percent  ****/

};
typedef struct UF_MODL_stycorner_data_s
               UF_MODL_stycorner_data_t,
              *UF_MODL_stycorner_data_p_t;



/*  Data structure for Styled Sweep
    "Move String" method: */
enum UF_MODL_styled_sweep_move_string_e
{
   UF_MODL_styled_sweep_move_string_move_none = 0, /* Move None */
   UF_MODL_styled_sweep_move_string_move_section,  /* Move Section */
   UF_MODL_styled_sweep_move_string_move_guide     /* Move Guide */
};
typedef enum UF_MODL_styled_sweep_move_string_e UF_MODL_styled_sweep_move_string_t;

/*
Following is a structure definition for Styled Sweep feature data.
It includes all the input elements to create a Styled Sweep feature.

Parameters are to be specified as follows:
1. Number of sections
2. Section string tag(s)
3. Guide string tag
4. Touch string tag (if any)
5. Spine string tag (if any)
6. Move String method
7. To auto init orient or not?
*/
struct UF_MODL_styled_sweep_data_s
{
    int            num_section;         /* Number of sections */
    UF_STRING_p_t  *section;            /* Section string(s) */
    UF_STRING_p_t  guide;               /* Guide string */
    UF_STRING_p_t  touch;               /* Touch string */
    UF_STRING_p_t  spine;               /* Spine string (if no spine_vector) */
    tag_t          spine_vector;        /* Spine vector (if no spine) */

    int            move_string_data;    /* Move String method */
    int            auto_init_orient;    /* To do auto-init-orient? */
};
typedef struct UF_MODL_styled_sweep_data_s UF_MODL_styled_sweep_data_t,
*UF_MODL_styled_sweep_data_p_t;

/*******************************************************************************
The following data structure will be used to define client data for
the ShapePattern user interface dialog, that allows users to choose a thumbnail picture from a list

Environment: Internal & External
See Also:
 UF_MODL_shape_pattern_create_dialog

History: Originally released in NX503
*******************************************************************************/
struct UF_MODL_shape_pattern_client_dialog_data_s
{
    char * PartName;             /* Part name */
    char * HoleName;             /* Hole name */
    int  iCountRecommendedShape; /* Number of recommended shapes */
    char **RecommendedShapeNames; /* <len:iCountRecommendedShape> Array of recommended shape names.*/
    char **RecommendedShapeThumbnailImageNames; /* <len:iCountRecommendedShape> Array of recommended shape thumbnail image names.*/
    char **RecommendedShapeLargeImageNames; /* <len:iCountRecommendedShape> Array of recommended shape large image names.*/

    int  iCountOtherShape;   /* Number of other shapes */
    char **OtherShapeNames; /* <len:iCountOtherShape> Array of other shape names.*/
    char **OtherShapeThumbnailImageNames; /* <len:iCountOtherShape> Array of other shape thumbnail image names.*/
    char **OtherShapeLargeImageNames; /* <len:iCountOtherShape> Array of other shape large image names.*/

    char *NoImageBmpName;   /* special image name when there is no image found */
    char *CurrentHoleShapePatternName; /* Current selected hole shape pattern name */
    char *CurrentLargeImageName; /* Current large image name */
    int   iSelectedHoleShapeIndex; /* Current selected hole shape index, zero based */
    logical  bSelFromRecommendedGroup; /* If true, shape is selected from recommended group */

};
typedef struct UF_MODL_shape_pattern_client_dialog_data_s
               UF_MODL_shape_pattern_client_dialog_data_t,
              *UF_MODL_shape_pattern_client_dialog_data_p_t;

/*****************************************************************
Following is a structure definition for deviation checking.
It holds the output data of deviation checking. 
******************************************************************/
struct UF_MODL_deviation_check_data_s
{
   int number_of_points_checked;             /* Number of points checked */
   double minimum_distance_error;            /* Minimum distance deviation */
   double maximum_distance_error;            /* Maximum distance deviation */
   double average_distance_error;            /* Average distance deviation */
   double minimum_angle_error;               /* Minimum angle deviation */
   double maximum_angle_error;               /* Maximum angle deviation */
   double average_angle_error;               /* Average angle deviation */
   double *distance_errors;                  /* <len:number_of_points_checked> Distance deviation at check points */
   double *angle_errors;                     /* <len:number_of_points_checked> Angle deviations at check points */
   double (*check_points)[3];                /* <len:number_of_points_checked> Points used in deviation checking */
};
typedef struct UF_MODL_deviation_check_data_s UF_MODL_deviation_check_data_t,
                                             *UF_MODL_deviation_check_data_p_t;

#ifdef __cplusplus
}
#endif


#endif     /* UF_MODL_TYPES_H_INCLUDED */
