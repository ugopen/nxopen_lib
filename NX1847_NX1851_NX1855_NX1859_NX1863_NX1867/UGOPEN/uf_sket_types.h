/*******************************************************************************
             Copyright 1998-2007 UGS Corp.
                  All Rights Reserved

 


File Description:

Open C API typedefs for the sketch module.

*******************************************************************************/

#ifndef UF_SKET_TYPES_INCLUDED
#define UF_SKET_TYPES_INCLUDED

#include <uf_defs.h>
#include <uf_obj_types.h>

#ifdef __cplusplus
extern "C" {
#endif


    /* output_mode used by UF_SKET_add_extracted_objects */
#define UF_SKET_EXTR_ORIG_TYPE         (0)
#define UF_SKET_EXTR_MULTI_SPLINES     (1)
#define UF_SKET_EXTR_SINGLE_SPLINE     (2)

    /* ref_info used by UF_SKET_attach_to_face  */
#define UF_SKET_HORIZONTAL        (1)
#define UF_SKET_VERTICAL          (2)
#define UF_SKET_WITH_NORMAL       (1)
#define UF_SKET_OPPOSITE_NORMAL   (2)
#define UF_SKET_ALONG_CURVE       (1)
#define UF_SKET_OPPOSITE_CURVE    (-1)

    /* geometric constraint type used by UF_SKET_delete_legacy_constraint */
#define UF_SKET_DATUM                   (10)
#define UF_SKET_CONSTANT_OFFSETS        (11)
#define UF_SKET_POINT_ON_CURVE          (12)
#define UF_SKET_MIDPOINT_OF_CURVE       (13)
#define UF_SKET_HORIZONTAL_LINES        (14)
#define UF_SKET_VERTICAL_LINES          (15)
#define UF_SKET_CONSTANT_ANGLES         (16)
#define UF_SKET_CONSTANT_LENGTH_LINES   (17)
#define UF_SKET_COLLINEAR               (18)
#define UF_SKET_PARALLEL                (19)
#define UF_SKET_PERPENDICULAR           (20)
#define UF_SKET_EQUAL_LENGTH            (21)
#define UF_SKET_EQUAL_RADIUS            (22)
#define UF_SKET_TANGENT_CURVES          (23)



/*
  Sketch Status definitions
*/

/*
    As of V17, the values of these UF_SKET_status_e will be recorded in
    the part file.  Hence, their values cannot be arbitrarily changed.
*/

enum UF_SKET_status_e
{
    UF_SKET_unknown_status,
    UF_SKET_not_evaluated,
    UF_SKET_under_constrained,
    UF_SKET_well_constrained,
    UF_SKET_over_constrained,
    UF_SKET_inconsistently_constrained
} ;
typedef enum UF_SKET_status_e UF_SKET_status_t, *UF_SKET_status_p_t;

enum UF_SKET_reference_status_e
{
    UF_SKET_reference,
    UF_SKET_active
};
typedef enum UF_SKET_reference_status_e UF_SKET_reference_status_t;

enum UF_SKET_con_type_e
{
    UF_SKET_no_con,
    UF_SKET_fixed,
    UF_SKET_horizontal,
    UF_SKET_vertical,
    UF_SKET_parallel,
    UF_SKET_perpendicular,
    UF_SKET_collinear,
    UF_SKET_equal_length,
    UF_SKET_equal_radius,
    UF_SKET_constant_length,
    UF_SKET_constant_angle,
    UF_SKET_coincident,
    UF_SKET_concentric,
    UF_SKET_mirror,
    UF_SKET_point_on_curve,
    UF_SKET_midpoint,
    UF_SKET_tangent,
    UF_SKET_radius_dim,
    UF_SKET_diameter_dim,
    UF_SKET_horizontal_dim,
    UF_SKET_vertical_dim,
    UF_SKET_parallel_dim,
    UF_SKET_perpendicular_dim,
    UF_SKET_angular_dim,
    UF_SKET_reserved_con_1,             /* Do not use */
    UF_SKET_reserved_con_2,             /* Do not use */
    UF_SKET_reserved_con_3,             /* Do not use */
    UF_SKET_reserved_con_4,             /* Do not use */
    UF_SKET_reserved_con_5,             /* Do not use */
    UF_SKET_reserved_con_6,             /* Do not use */
    UF_SKET_point_on_string,
    UF_SKET_slope,
    UF_SKET_uniform_scaled,
    UF_SKET_non_uniform_scaled ,
    UF_SKET_assoc_trim,                 /* Limited support */
    UF_SKET_assoc_offset,               /* Limited support */
    UF_SKET_perimeter_dim,
    UF_SKET_pgm_offset,
    UF_SKET_normal,
    UF_SKET_point_on_loop,
    UF_SKET_recipe_trim,
    UF_SKET_pattern,
    UF_SKET_rigid_set,
    UF_SKET_g1,
    UF_SKET_g2,
    UF_SKET_align,
    UF_SKET_tangent_to_string,
    UF_SKET_perpendicular_to_string,
    UF_SKET_scalable_set,
    UF_SKET_last_con_type /* The last constraint type indicator; NOT to be used. */
};

typedef enum UF_SKET_con_type_e UF_SKET_con_type_t, *UF_SKET_con_type_p_t;

#define UF_SKET_MAX_CON_TYPES 51

#define UF_SKET_MAX_GEOMETRY_PER_CON 4

enum UF_SKET_con_class_e
{
    UF_SKET_no_cons,
    UF_SKET_all_cons,
    UF_SKET_geo_cons,
    UF_SKET_dim_cons

};
typedef enum UF_SKET_con_class_e UF_SKET_con_class_t, *UF_SKET_con_class_p_t;


struct UF_SKET_info_s
{
int    subtype;          /* UF_v9_sketch_subtype, UF_v13_sketch_subtype or
                            UF_extracted_sketch_subtype
                         */
char   name[ UF_OBJ_NAME_BUFSIZE ];    /* sketch's name  */
tag_t  csys_tag;         /* sketch's CSYS tag          */
double csys[12];         /* sketch's CSYS :
                            sketch_csys[0-8] : the orientation,
                            sketch_csys[9-11]: the origin
                         */
char   view_name[16];    /* sketch's view name (for pre-V13 sketches only) */
tag_t  datum_tag;        /* sketch's datum tag (for pre-V13 sketches only) */
double datum[3];         /* sketch's datum (for pre-V13 sketches only)     */

} ;

typedef struct UF_SKET_info_s UF_SKET_info_t, *UF_SKET_info_p_t;
/******************************************************************************
  enum and structures for creating dimensions
******************************************************************************/

/*
 
*/

/*
   Associativity types for sketch dimension.
*/
enum UF_SKET_assoc_type_e{
    UF_SKET_assoc_type_none,
        UF_SKET_end_point,
        UF_SKET_arc_center,
        UF_SKET_tangency,
        UF_SKET_curve_point,
    UF_SKET_anchor_point
} ;

typedef enum UF_SKET_assoc_type_e UF_SKET_assoc_type_t;

enum UF_SKET_assoc_mod_e{
        UF_SKET_first_end_point,
        UF_SKET_last_end_point
} ;

typedef enum UF_SKET_assoc_mod_e UF_SKET_assoc_mod_t;

struct UF_SKET_dim_object_s
{
tag_t object_tag;            /* Tag of the object - sketch curves, edge,
                                datum plane, datum axis, NX curves */

UF_SKET_assoc_type_t object_assoc_type;    /* Object associativity type:
                                              UF_SKET_end_point;
                                              UF_SKET_arc_center -
                                                 object must be an arc;
                                              UF_SKET_tangency -
                                                 object must be an arc;
                          UF_SKET_curve_point -
                         object must be a spline
                          UF_SKET_anchor_point -
                         object must be a sketch conic */

int object_assoc_mod_value;   /* Object associativity modifier:
                                UF_SKET_first_end_point or UF_SKET_last_end_point
                    if object_assoc_type = UF_SKET_end_point;
                Not Used
                    if object_assoc_type = UF_SKET_arc_center or
                    UF_SKET_anchor_point;
                parameter percentage (0 - 100) (used to find approx tgt pt)
                    if object_assoc_type = UF_SKET_tangency;
                the index number of the defining point of the spline(starting from 1)
                    if object_assoc_type = UF_SKET_curve_point;
                  */

} ;

typedef struct UF_SKET_dim_object_s UF_SKET_dim_object_t, *UF_SKET_dim_object_p_t;

/******************************************************************************
  enum and structures for createing geometric constraints
******************************************************************************/

enum UF_SKET_geom_vertex_e
{
    UF_SKET_no_vertex,
    UF_SKET_start_vertex,
    UF_SKET_end_vertex,
    UF_SKET_center_vertex,          /* used only for Arcs/Ellipses */
    UF_SKET_spline_defining_point,  /* used only for splines       */
    UF_SKET_anchor_vertex,          /* used only by general conics */
    UF_SKET_spline_pole,            /* used only for splineByPoles */
    UF_SKET_mid_vertex              /* used only for Arcs/Lines    */
} ;

typedef enum UF_SKET_geom_vertex_e UF_SKET_geom_vertex_t;

enum UF_SKET_help_type_e
{
    UF_SKET_no_help_data,
    UF_SKET_use_help_pt,
    UF_SKET_use_help_param
};

typedef enum UF_SKET_help_type_e UF_SKET_help_type_t;

struct UF_SKET_con_geom_s
{
tag_t                  geom_tag;       /* The geomtry's tag */
UF_SKET_geom_vertex_t  vertex_type;    /* Vertex type if it is the vertex
                                          of the geometry that will be
                                          constrained.
                                          Valid types are specified in
                                          UF_SKET_geom_vertex_t.
                                       */
int                    vertex_index;   /* Starting from 1. Used to
                                          indicate which defining point
                                          of the spline will be constrained.
                                          Only used when vertex_type is
                                          UF_SKET_spline_defining_point.
                                       */
UF_SKET_help_type_t    use_help;       /* Whether to use help data (either
                                          help points or help parameter.)
                                          Valid types as specified in
                                          UF_SKET_help_type_t.  Help
                                          points/parameters are used to
                                          indicate whereabouts on the geometry
                                          a constraint should apply to. They
                                          are only needed when the constraints
                                          are of type UF_SKET_tangent,
                                          UF_SKET_point_on_curve, or
                                          UF_SKET_point_on_string.
                                        */
double                 help_point[3];  /* Help point */

double                 help_parameter; /* Help parameter */

};

typedef struct UF_SKET_con_geom_s UF_SKET_con_geom_t, *UF_SKET_con_geom_p_t;

#ifdef __cplusplus
}
#endif

#endif  /* UF_SKET_TYPES_INCLUDED */
