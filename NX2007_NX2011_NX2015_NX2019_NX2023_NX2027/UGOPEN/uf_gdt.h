/******************************************************************************
             Copyright (c) 1998-2002,2003,2004,2005 Unigraphics Solutions, Inc.
                       Unpublished - All Rights Reserved



File description:

The Geometric Tolerancing Module manipulates actual design level manufacturing
data. Currently, this data is displayed as "old" notes or annotations on the
drawing of a part. The Geometric Tolerancing Module allows the designer to
include manufacturing information, in the form of Tolerance Features
(datums, datum targets, and tolerances), directly in the master model of the
part. These Tolerance Features are "smart," knowing when a change in the model
influences a change in a Tolerance Feature. The module does simple checking
automatically and comprehensive checking on user demand.

This API allows users of the Geometric Tolerancing Module to further enhance
their design environment and facilitate advanced design for manufacturing
on NX.



*******************************************************************************/

#ifndef UF_GDT_H_INCLUDED
#define UF_GDT_H_INCLUDED

#include <uf_defs.h>
#include <uf_drf_types.h>
#include <uf_pd_types.h>
#include <libufun_exports.h>

#ifdef __cplusplus
extern "C" {
#endif
/******************************************************************************

******************************************************************************/
#define ERROR_UF_GDT_base      1830000

#define UF_GDT_MAX_NAME_LEN 33

/******************************************************************************
                             Type Definition
*******************************************************************************/

/*ENUMERATED DATA TYPES*/

/* Defines the type of tolerances that can be part of a tolerance feature
   Tolerance features may include a number of these different types */
enum UF_GDT_tolerance_type_e
{
    UF_GDT_DATUM_TARGET_POINT_TYPE        = 0,  /* Datum target point tolerance type*/
    UF_GDT_DATUM_TARGET_LINE_TYPE         = 1,  /* Datum target line tolerance type */
    UF_GDT_DATUM_IDENTIFIER_TYPE          = 3,  /* Datum identifier type */
    UF_GDT_DATUM_MULTIPLE_TYPE            = 4,  /* Special Multiple datum type */
    UF_GDT_GEOMETRIC_TOLERANCE_TYPE       = 5,  /* Geometric tolerance type */
    UF_GDT_SIZE_TOLERANCE_TYPE            = 6,  /* Size Tolerance type */
    UF_GDT_DATUM_TARGET_DIA_TYPE          = 7,  /* Circular datum target areas */
    UF_GDT_DATUM_TARGET_RECT_TYPE         = 8,  /* Rectangular datum target areas */
    UF_GDT_DIRECTED_DIMENSION_TYPE        = 9,  /* Directed dimension type */
    UF_GDT_DATUM_TARGET_CYL_TYPE          = 10, /* Cylindrical datum target areas */
    UF_GDT_WALL_THICKNESS_TYPE            = 11, /* Wall thickness tolerance type */
    UF_GDT_DEPTH_TOLERANCE_TYPE           = 12, /* Depth Tolerance type */
    UF_GDT_LIMITS_AND_FITS_TOLERANCE_TYPE = 13, /* Limits and fits tolerance type */
    UF_GDT_THREAD_TOLERANCE_TYPE          = 14, /* Thread tolerance type */
    UF_GDT_DATUM_TARGET_USER_DEFINED_TYPE = 15  /* User defined datum target type */
};

typedef enum UF_GDT_tolerance_type_e UF_GDT_tolerance_type_t,
                                    *UF_GDT_tolerance_type_p_t;

/* Defines the valid set of feature types which can describe the geometry
   of a tolerance feature */
enum UF_GDT_feature_type_e
{
    UF_GDT_GENERAL_FEATURE,                    /* General feature type */
    UF_GDT_SLOT_FEATURE,                       /* Slot feature type */
    UF_GDT_TAB_FEATURE,                        /* Tab feature type */
    UF_GDT_HOLE_FEATURE,                       /* Hole feature type */
    UF_GDT_PIN_FEATURE,                        /* Pin feature type */
    UF_GDT_SOCKET_FEATURE,                     /* Socket feature type */
    UF_GDT_BALL_FEATURE,                       /* Ball feature type */
    UF_GDT_ELONGATED_HOLE_FEATURE,             /* Elongated hole feature type */
    UF_GDT_PLANE_FEATURE,                      /* Plane feature type */
    UF_GDT_BOUNDED_FEATURE,                    /* Bounded feature type */
    UF_GDT_TAPERED_HOLE_FEATURE,               /* Tapered hole feature type */
    UF_GDT_TAPERED_PIN_FEATURE,                /* Tapered pin feature type */
    UF_GDT_HOLLOW_TORUS_FEATURE,               /* Hollow torus feature type */
    UF_GDT_SOLID_TORUS_FEATURE,                /* Solid torus feature type */
    UF_GDT_HOLLOW_REVOLVED_FEATURE,            /* Hollow revolved feature type */
    UF_GDT_SOLID_REVOLVED_FEATURE,             /* Solid revolved feature type */
    UF_GDT_COUNTERBORE_HOLE_FEATURE,           /* Counterbore hole feature type */
    UF_GDT_COUNTERSINK_HOLE_FEATURE,           /* Countersink hole feature type */
    UF_GDT_EDGE_BLEND_FEATURE,                 /* Edge blend feature type */
    UF_GDT_THICKNESS_GAP_FEATURE,              /* Thickness/Gap feature type */
    UF_GDT_STEPPED_SHAFT_FEATURE,              /* Stepped shaft feature type */
    UF_GDT_STEPPED_HOLE_FEATURE,               /* Stepped hole feature type */
    UF_GDT_COMPLEX_ELONGATED_HOLE_FEATURE,     /* Complex elongated hole feature type */
    UF_GDT_OPPOSED_POINT_FEATURE,              /* Opposed point element feature type */
    UF_GDT_OPPOSED_LINE_FEATURE,               /* Opposed line element feature type */
    UF_GDT_THREAD_FEATURE,                     /* Thread Feature Type  */
    UF_GDT_MODEL_AXIS_FEATURE,                 /* Modeling Axis Feature Type */
    UF_GDT_MODEL_PLANE_FEATURE,                /* Modeling Plane Feature Type */
    UF_GDT_SPLINE_FEATURE,                     /* Spline feature type */
    UF_GDT_GEAR_FEATURE,                       /* Gear feature type */
    UF_GDT_CIRCULAR_TOOTH_THICKNESS_FEATURE,   /* Circular tooth thickness type */
    UF_GDT_CIRCULAR_SPACE_WIDTH_FEATURE,       /* Circular space width type */
    UF_GDT_PIN_MEASUREMENT_FEATURE             /* Pin measurement feature */
};

typedef enum UF_GDT_feature_type_e UF_GDT_feature_type_t,
                                  *UF_GDT_feature_type_p_t;
/* Defines the valid pattern types for a tolerance feature  */
enum UF_GDT_pattern_type_e
{
    UF_GDT_NO_PATTERN,
    UF_GDT_RADIAL_PATTERN,       /* Obsolete in V16 */
    UF_GDT_RECTANGULAR_PATTERN,  /* Obsolete in V16 */
    UF_GDT_ARBITRARY_PATTERN
};

typedef enum UF_GDT_pattern_type_e UF_GDT_pattern_type_t,
                                  *UF_GDT_pattern_type_p_t;

/* Defines the valid tolerance display formats for a size tolerance */
enum UF_GDT_tol_format_e
{
    UF_GDT_LIM_MINUS_BEFORE_PLUS,  /* Limits minus before plus */
    UF_GDT_LIM_PLUS_BEFORE_MINUS,  /* Limits plus before minus */
    UF_GDT_LIM_MINUS_OVER_PLUS,    /* Limits minus over plus */
    UF_GDT_LIM_PLUS_OVER_MINUS,    /* Limits plus over minus */
    UF_GDT_PLUS_OVER_MINUS,        /* Tolerance plus over minus */
    UF_GDT_MINUS_OVER_PLUS,        /* Tolerance minus over plus */
    UF_GDT_PLUS_MINUS,             /* Tolerance plus minus */
    UF_GDT_NO_TOLERANCE            /* No tolerance defined */
};
typedef enum UF_GDT_tol_format_e UF_GDT_tol_format_t, *UF_GDT_tol_format_p_t;


/* Defines the set of valid feature control frame characteristic GD&T types */
enum UF_GDT_characteristic_e
{
    UF_GDT_STRAIGHTNESS_TYPE,     /* GDT form type - straightness */
    UF_GDT_FLATNESS_TYPE,         /* GDT form type - flatness */
    UF_GDT_CIRCULAR_TYPE,         /* GDT form type - circular */
    UF_GDT_CYLINDRICAL_TYPE,      /* GDT form type _ cylindrical */
    UF_GDT_LINE_PROFILE_TYPE,     /* GDT profile type - line profile */
    UF_GDT_SURFACE_PROFILE_TYPE,  /* GDT profile type - surface profile */
    UF_GDT_ANGULAR_TYPE,          /* GDT orientation type - angular */
    UF_GDT_PERPENDICULAR_TYPE,    /* GDT orientation type - perpendicular */
    UF_GDT_PARALLEL_TYPE,         /* GDT orientation type - parallel */
    UF_GDT_POSITION_TYPE,         /* GDT position type - position */
    UF_GDT_CONCENTRIC_TYPE,       /* GDT position type - concentric */
    UF_GDT_SYMMETRIC_TYPE,        /* GDT position type - symmetric */
    UF_GDT_CIRCULAR_RUNOUT_TYPE,  /* GDT runout type - circular runout */
    UF_GDT_TOTAL_RUNOUT_TYPE      /* GDT runout type - total runout */
};

typedef enum UF_GDT_characteristic_e UF_GDT_characteristic_t,
                                    *UF_GDT_characteristic_p_t;

/* Defines the allowable material condition modifiers for feature control
   frame and datum specifications */
enum UF_GDT_material_modifier_e
{
    UF_GDT_MMC,                    /* Maximum material condition modifier */
    UF_GDT_LMC,                    /* Least material condition modifier */
    UF_GDT_RFS,                    /* Regardless of feature size modifier */

    UF_GDT_TANGENTIAL,             /* Tangential zone modifier NOTE: The
                                      tangential modifier may only be used
                                      to modify the tolerance zone of feature
                                      control frames. It may not be used to
                                      modify datum identifiers, targets, or
                                      references */

    UF_GDT_NO_MOD                  /* No material modifier. NOTE: The
                                      UF_GDT_NO_MOD type should be used in
                                      place of the RFS type for ASME 1994 and
                                      ISO applications */

};

typedef enum UF_GDT_material_modifier_e UF_GDT_material_modifier_t,
                                       *UF_GDT_material_modifier_p_t;

/* Defines the possible tolerance zone shapes for a feature control frame */
enum UF_GDT_zone_shape_e
{
    UF_GDT_SHAPE_PLANAR,           /* Planar tolerance zone - Planar zones
                                      define a tolerance zone which runs
                                      parallel to a flat or complex plane. */
    UF_GDT_SHAPE_CYLINDRICAL,      /* Cylindrical tolerance zone - Cylindri-
                                      cal zones define a tolerance zone which
                                      surrounds the AXIS of a cylindrical
                                      feature. */
    UF_GDT_SHAPE_SPHERICAL,        /* Spherical tolerance - Spherical zones
                                      define a tolerance zone surrounding
                                      the center of a spherical feature.*/
    UF_GDT_SHAPE_OFFSET            /* Profile zone - Offset zones define
                                      unilateral or bilateral tolerance zones
                                      used for profile tolerances. */
};

typedef enum UF_GDT_zone_shape_e UF_GDT_zone_shape_t, *UF_GDT_zone_shape_p_t;

/* Defines the allowable zone modifiers for a feature control frame */
enum UF_GDT_modifier_types_e
{
    UF_GDT_FREE_STATE,               /* Free state zone refinement (all) */
    UF_GDT_UNIT_BASIS_LENGTH,        /* Unit basis length refinement
                                        (straightness) */
    UF_GDT_UNIT_BASIS_AREA,          /* Unit basis area refinement (flatness) */
    UF_GDT_PROJECTED_ZONE,           /* Projected zone refinement (position) */
    UF_GDT_STATISTICAL,              /* Statistical refinement (many) */
    UF_GDT_NO_MODIFIERS,             /* No modifiers */
    UF_GDT_MAX_BONUS,                /* MAX bonus tolerance specification */
    UF_GDT_PATTERN_COUNT,            /* Obsolete in V16.0 */
    UF_GDT_INDIVIDUAL_COUNT,         /* Obsolete in V16.0 */
    UF_GDT_SEP_REQT,                 /* Obsolete in V16.0 */
    UF_GDT_SIM_REQT,                 /* Obsolete in V16.0 */
    UF_GDT_BOUNDARY,                 /* Obsolete in V16.0 */
    UF_GDT_ALL_OVER,                 /* Obsolete in V16.0 */
    UF_GDT_AVG_DIA,                  /* Obsolete in V16.0 */
    UF_GDT_COAX_HOLE_COUNT,          /* Obsolete in V16.0 */
    UF_GDT_NON_MANDATORY_MFG_DATA,   /* Obsolete in V16.0 */
    UF_GDT_NO_PERFECT_MMC_FORM,      /* Obsolete in V16.0 */
    UF_GDT_PERFECT_MMC_ORIENTATION,  /* Obsolete in V16.0 */
    UF_GDT_PERFECT_MMC_COAXIALITY,   /* Obsolete in V16.0 */
    UF_GDT_PERFECT_MMC_SYM_FEAT_LOC, /* Obsolete in V16.0 */
    UF_GDT_SURFACE_COUNT,            /* Obsolete in V16.0 */
    UF_GDT_THRU,                     /* Obsolete in V16.0 */
    UF_GDT_THRU_HOLE                 /* Obsolete in V16.0 */
};

typedef enum UF_GDT_modifier_types_e UF_GDT_modifier_types_t,
                                    *UF_GDT_modifier_types_p_t;

/* Defines the standard keyword ids */
enum UF_GDT_standard_keyword_id_e
{
    UF_GDT_PATTERN_COUNT_KEYWORD,            /* Pattern Count (3X, etc) */
    UF_GDT_INDIVIDUAL_COUNT_KEYWORD,         /* INDIVIDUALLY applied */
    UF_GDT_SEP_REQT_KEYWORD,                 /* SEP REQT applied */
    UF_GDT_SIM_REQT_KEYWORD,                 /* SIM REQT applied */
    UF_GDT_BOUNDARY_KEYWORD,                 /* BOUNDARY condition applied */
    UF_GDT_ALL_OVER_KEYWORD,                 /* ALL OVER applied to surfaces */
    UF_GDT_AVG_DIA_KEYWORD,                  /* AVG DIAM applied to size
                                                tolerances */
    UF_GDT_COAX_HOLE_COUNT_KEYWORD,          /* nX COAXIAL HOLES applied */
    UF_GDT_NON_MANDATORY_MFG_DATA_KEYWORD,   /* NON-MANDATORY MFG DATA applied */
    UF_GDT_NO_PERFECT_MMC_FORM_KEYWORD,      /* NON-PERFECT FORM AT MMC applied */
    UF_GDT_PERFECT_MMC_ORIENTATION_KEYWORD,
    UF_GDT_PERFECT_MMC_COAXIALITY_KEYWORD,
    UF_GDT_PERFECT_MMC_SYM_FEAT_LOC_KEYWORD,
    UF_GDT_SURFACE_COUNT_KEYWORD,            /* n SURFACES applied */
    UF_GDT_THRU_KEYWORD,                     /* THRU applied to feature */
    UF_GDT_THRU_HOLE_KEYWORD,                /* THRU HOLE applied to feature */
    UF_GDT_SIM_REQT_N_KEYWORD,               /* SIM REQT N applied to feature */
    UF_GDT_MAJOR_DIA_KEYWORD,                /* MAJOR DIA applied to thread feature */
    UF_GDT_MINOR_DIA_KEYWORD,                /* MINOR DIA applied to thread feature */
    UF_GDT_PITCH_DIA_KEYWORD,                /* PITCH DIA applied to thread feature */
    UF_GDT_INTERRUPTED_KEYWORD
};

typedef enum UF_GDT_standard_keyword_id_e UF_GDT_standard_keyword_id_t,
                                         *UF_GDT_standard_keyword_id_p_t;

/* Maximum and minimum keyword definitions */
#define UF_GDT__MIN_KEYWORD (UF_GDT_PATTERN_COUNT_KEYWORD)
#define UF_GDT__MAX_KEYWORD (UF_GDT_INTERRUPTED_KEYWORD)

/* Defines type to be used for both standard and user defined keyword ids */
typedef int UF_GDT_keyword_id_t, *UF_GDT_keyword_id_p_t;

/* Defines the standards that are supported by the Geometric Tolerancing
   module */
enum UF_GDT_standard_e
{
    UF_GDT_NO_STANDARD,            /* Standard not specified */
    UF_GDT_ANSI_1982,              /* ANSI Y14.5M - 1982 standard */
    UF_GDT_ASME_1994,              /* ASME Y14.5M - 1994 standard */
    UF_GDT_ISO_1983                /* ISO 1101 : 1983 standard */
};

typedef enum UF_GDT_standard_e UF_GDT_standard_t, *UF_GDT_standard_p_t;

/* Defines an enumerated type for each method of associating a datum
   display instance to the model. */
enum UF_GDT_datum_assoc_type_e
{
    UF_GDT_FEATURE_EDGE,      /* datum is attached to a feature edge */
    UF_GDT_DOTTED_DATUM,      /* datum is attached to stub of dotted leader */
    UF_GDT_ATTACHED_TO_FCF,   /* datum is attached to an fcf */
    UF_GDT_ATTACHED_TO_STUB,  /* datum is attached to a leader stub */
    UF_GDT_DIRECTED_DATUM,    /* datum is part of a directed datum instance */
    UF_GDT_EXTENSION_LINE     /* datum is attached to a dimension ext. line */
};

typedef enum UF_GDT_datum_assoc_type_e UF_GDT_datum_assoc_type_t,
                                      *UF_GDT_datum_assoc_type_p_t;

/* Defines an enumerated type for each data structure inside the GD&T module
   used in the UF_GDT_free routine */
enum UF_GDT_data_type_e
{
    UF_GDT_DATA_FRAME_TYPE,        /* UF_GDT_data_frame_t */
    UF_GDT_DATUM_IDENT_TYPE,       /* UF_GDT_datum_identifier_t */
    UF_GDT_DATUM_REF_TYPE,         /* UF_GDT_datum_reference_t */
    UF_GDT_DESCRIPT_TYPE,          /* UF_GDT_description_t */
    UF_GDT_DIRECTED_DIM_TYPE,      /* UF_GDT_directed_dimension_t */
    UF_GDT_FCF_TYPE,               /* UF_GDT_fcf_t */
    UF_GDT_MOD_DATA_TYPE,          /* UF_GDT_modifier_data_t */
    UF_GDT_MULTI_DATUM_TYPE,       /* UF_GDT_multiple_datum_t */
    UF_GDT_SIZE_TOL_TYPE,          /* UF_GDT_size_tolerance_t */
    UF_GDT_STATISTICAL_TYPE,       /* UF_GDT_statistical_info_t */
    UF_GDT_SURFACE_PARMS_TYPE,     /* UF_GDT_surface_parms_t */
    UF_GDT_TARGET_POINT_TYPE,      /* UF_GDT_datum_target_point_t */
    UF_GDT_TARGET_LINE_TYPE,       /* UF_GDT_datum_target_line_t */
    UF_GDT_TARGET_AREA_TYPE,       /* Obsolete in V15.0 */
    UF_GDT_TOL_VALUE_TYPE,         /* UF_GDT_tolerance_value_t */
    UF_GDT_TOL_ZONE_TYPE,          /* UF_GDT_tolerance_zone_t */
    UF_GDT_FEAT_PARMS_TYPE,        /* UF_GDT_feature_parms_t */
    UF_GDT_DIA_AREA_TYPE,          /* UF_GDT_target_dia_area_t */
    UF_GDT_RECT_AREA_TYPE,         /* UF_GDT_target_rect_area_t */
    UF_GDT_CYL_AREA_TYPE,          /* UF_GDT_target_cyl_area_t */
    UF_GDT_UDEF_AREA_TYPE,         /* UF_GDT_target_udef_area_t */
    UF_GDT_ANNOTATION_TAGS_TYPE,   /* UF_GDT_annotation_tags_t */
    UF_GDT_CALLOUT_STR_TYPE,        /* UF_GDT_callout_strings_t */
    UF_GDT_DEPTH_TOL_TYPE,          /* UF_GDT_depth_tolerance_t */
    UF_GDT_LIM_FITS_TOL_TYPE,       /* UF_GDT_limits_and_fits_tolerance_t */
    UF_GDT_DATUM_REF_FRAME_TYPE,    /* UF_GDT_drf_data_t */
    UF_GDT_THREAD_TYPE,             /* UF_GDT_thread_data_t */
    UF_GDT_MODL_DATA_TYPE,          /* UF_GDT_modl_data_t */
    UF_GDT_PRODUCT_ATT_TYPE         /* UF_GDT_product_attribute_t */
};

typedef enum UF_GDT_data_type_e UF_GDT_data_type_t, *UF_GDT_data_type_p_t;
/* Defines the allowable types of profile tolerances.
   Outside if defined to be the direction away from material and
   inside the direction into material.
*/
enum UF_GDT_profile_type_e
{
    UF_GDT_PROFILE_EQ_BILATERAL,   /* equally disposed bilateral   */
    UF_GDT_PROFILE_UNILATERAL_OUT, /* unilateral outside           */
    UF_GDT_PROFILE_UNILATERAL_IN,  /* unilateral inside            */
    UF_GDT_PROFILE_UNEQ_BILATERAL  /* unequally disposed bilateral */
};

typedef enum UF_GDT_profile_type_e UF_GDT_profile_type_t,
                                  *UF_GDT_profile_type_p_t;

/*  The following enumerated type is used to specify the type of master
 *  model link which is to be broken from the "break relationship" function.
 */
enum UF_GDT_relation_type_e
{
    UF_GDT_PULL_RELATION_TYPE   /* link between pulled feature and component */
};

typedef enum UF_GDT_relation_type_e UF_GDT_relation_type_t;

/* The following enumerated type defines the allowable types of appended text
 * locations.
 */
enum UF_GDT_text_location_e
{
    UF_GDT_ABOVE,                 /* above appended text */
    UF_GDT_BELOW,                 /* below appended text */
    UF_GDT_BEFORE,                /* before appended text */
    UF_GDT_AFTER                  /* after appended text */
};

typedef enum UF_GDT_text_location_e UF_GDT_text_location_t,
                                   *UF_GDT_text_location_p_t;

/*  The following enumerated type defines the directed dimension types
 *  available in the tolerancing module.
 */
enum UF_GDT_directed_dimension_type_e
{
    UF_GDT_LINEAR_DIRECTED_DIMENSION,   /* Linear directed dimension  */
    UF_GDT_ANGULAR_DIRECTED_DIMENSION   /* Angular directed dimension */
};

typedef enum UF_GDT_directed_dimension_type_e UF_GDT_directed_dimension_type_t,
                                          *UF_GDT_directed_dimension_type_p_t;

/* The following enumerated type defines the orientation and region types
 * available in the tolerancing module.
 */
enum UF_GDT_geometric_definition_type_e
{
    UF_GDT_ALL_GEOMETRY,                /* No Definition              */
    UF_GDT_PLANAR_ORIENTATION,          /* Planar Orientation         */
    UF_GDT_PLANAR_CROSS_SECTION,        /* Planar Cross Section       */
    UF_GDT_REGION,                      /* Region                     */
    UF_GDT_POINT,                       /* Point                      */
    UF_GDT_RECTANGULAR_REGION,          /* Rectangular Bounded Region */
    UF_GDT_CIRCULAR_REGION              /* Circular Bounded Region    */
};

typedef enum UF_GDT_geometric_definition_type_e
                                   UF_GDT_geometric_definition_type_t,
                                  *UF_GDT_geometric_definition_type_p_t;

/* The following enumerated type defines the size tolerance value
 * types available in the tolernacing module.
 */
enum UF_GDT_size_value_type_e
{
    UF_GDT_NO_SIZE,             /* No size tolerance value  */
    UF_GDT_LINEAR_SIZE,         /* Linear size tolerance    */
    UF_GDT_RADIAL_SIZE,         /* Radial size tolerance    */
    UF_GDT_DIAMETRAL_SIZE,      /* Diametral size tolerance */
    UF_GDT_ANGULAR_MAJOR_SIZE,  /* Angular major size tolerance */
    UF_GDT_ANGULAR_MINOR_SIZE   /* Angular minor size tolerance */
};

typedef enum UF_GDT_size_value_type_e UF_GDT_size_value_type_t,
                                     *UF_GDT_size_value_type_p_t;

/* The following enumerated type defines the leader terminator symbols */
enum UF_GDT_leader_type_e
{
    UF_GDT_LEADER_NON_TERMINATED = 0,
    UF_GDT_LEADER_DATUM,
    UF_GDT_LEADER_ARROWHEAD,
    UF_GDT_LEADER_DOT
};

typedef enum UF_GDT_leader_type_e UF_GDT_leader_type_t,
                                 *UF_GDT_leader_type_p_t;

/* The following enumerated type defines the leader stub direction */
enum UF_GDT_stub_direction_e
{
    UF_GDT_STUB_LEFT    = 1,
    UF_GDT_STUB_RIGHT,
    UF_GDT_STUB_UP,
    UF_GDT_STUB_DOWN
};

typedef enum UF_GDT_stub_direction_e UF_GDT_stub_direction_t,
                                    *UF_GDT_stub_direction_p_t;

/* The following enumerated type defines the valid index display
 * methods for GD&T,
 */
enum UF_GDT_index_display_type_e
{
    UF_GDT_UNIQUE = 0,
    UF_GDT_PART_BASED
};

typedef enum UF_GDT_index_display_type_e UF_GDT_index_display_type_t,
                                        *UF_GDT_index_display_type_p_t;

/* The following enumerated type defines the different feature edge
 * selection methods for GD&T,
 */
enum UF_GDT_edge_select_type_e
{
    UF_GDT_EDGE_SELECT_ON = 1,
    UF_GDT_EDGE_SELECT_OFF = 2,
    UF_GDT_EDGE_SELECT_ALWAYS = 3
};

typedef enum UF_GDT_edge_select_type_e UF_GDT_edge_select_type_t,
                                      *UF_GDT_edge_select_type_p_t;


enum UF_GDT_precedence_e
{
    UF_GDT_PRECEDENCE_NONE = 0,    /* No Precedence */
    UF_GDT_PRECEDENCE_PRIMARY,     /* Primary datum reference */
    UF_GDT_PRECEDENCE_SECONDARY,   /* Secondary datum reference */
   UF_GDT_PRECEDENCE_TERTIARY     /* Tertiary datum reference */
};

typedef enum UF_GDT_precedence_e UF_GDT_precedence_t,
                                *UF_GDT_precedence_p_t;

/* The following enumerated type defines the default part gaging
 * standards for GD&T
 */
enum UF_GDT_restrained_condition_e
{
    UF_GDT_FREE_STATE_CONDITION = 1,
    UF_GDT_RESTRAINED_CONDITION = 2
};

typedef enum UF_GDT_restrained_condition_e UF_GDT_restrained_condition_type_t,
                                          *UF_GDT_restrained_condition_type_p_t;
#define UF_GDT_SEPERATE_GAGE    UF_GDT_SEPARATE_GAGE
/* The following enumerated type defines the restrained condition
 * for a GD&T part
 */
enum UF_GDT_default_gage_type_e
{
    UF_GDT_SEPARATE_GAGE = 1,
    UF_GDT_SIMULTANEOUS_GAGE = 2
};

typedef enum UF_GDT_default_gage_type_e UF_GDT_default_gage_type_t,
                                       *UF_GDT_default_gage_type_p_t;

/* The following enumerated type defines the parameter used to map the
   faces of the modeling feature to the tolerance feature.
   Following describes each enum type, how it is related to the modeling
   feature parameter and how to use it to create tolerance features based
   on modeling features -

   UF_GDT_MODL_PARAM_INVALID:
   This enum type is resereved by the system for inernal use. It is not
   available for use.

   UF_GDT_MODL_PARAM_NONE:
   When this enum type is used, the system knows exactly how to map the
   faces of modeling feature to tolerance features.

   Use with following modeling features -
   1. Simple Hole
      Modeling Feature Parameter: Hole Diameter
      Tolerance feature will reference face defined by Hole Diameter parameter
   2. Extrude/Revolve
      Tolerance feature will reference cylindrical face in the modeling feature
      and create GDT pin/hole type tolerance features
   3. Cylindrical Pocket
      Modeling Feature Parameter: Pocket Diameter
      Tolerance feature will reference face defined by Pocket Diameter parameter
   4. Counterbore Hole
      System will create complex tolerance features/subfeatures -
      Complex feature - References hole and counterbore faces
      Complex subfeature 1 - References hole face
      Complex subfeature 2 - References counterbore face
   5. Countersink Hole
      System will create complex tolerance features/subfeatures -
      Complex feature - References countersink and hole faces
      Complex subfeature 1 - References hole face
      Complex subfeature 2 - References countersink face
      Cross-section definition subfeature for complex subfeature 2
   6. Symbolic Thread
      System will create complex tolerance features/subfeatures -
      Complex feature - References cylindrical face on which thread resides
      Complex subfeature - References modeling thread feature
   7. Boss
      Modeling Feature Parameter: Boss Diameter
      Tolerance feature will reference face defined by Boss Diameter
      parameter
   8. Edge Blend
      Modeling Feature Parameter: Radius
      Tolerance feature will reference faces defined by Radius parameter


   UF_GDT_MODL_PARAM_ALL:
   Use this enum type to create a GDT general type tolerance feature that
   references all the faces of the modeling feature. Currently, this is not
   enabled.


   UF_GDT_MODL_PARAM_HOLE:
   Use this enum type when creating tolerance feature that will reference
   cylindrical face of the modeling feature.

   Use with following modeling features -
   1. Counterbore Hole, Countersink Hole
      Modeling Feature Parameter: Hole Diameter
      Tolerance feature will reference faces defined by Hole Diameter parameter


   UF_GDT_MODL_PARAM_COUNTERBORE:
   Use this enum type when creating tolerance feature that will reference
   cylindrical face of the Counterbore Hole modeling feature.
   Modeling Feature Parameter: Counterbore Diameter
   Tolerance feature will reference faces defined by Counterbore Diameter
   parameter


   UF_GDT_MODL_PARAM_COUNTERSINK:
   Use this enum type when creating tolerance feature that will reference
   conical face of the Countersink Hole modeling feature.
   Tolerance feature will reference conical faces


   UF_GDT_MODL_PARAM_X_LENGTH:
   Use this enum type when creating tolerance feature that will reference
   faces of the modeling feature along the X-axis of the feature.

   Use with following modeling features -
   1. Rectangular Slot, Ball End Slot, U Slot, T Slot
      Modeling Feature Parameter: Length
      Tolerance feature will reference faces that are defined  by Length
      parameter
   2. Rectangular Pad, Rectangular Pocket
      Modeling Feature Parameter: X Length
      Tolerance feature will reference faces that are defined by X Length
      parameter


   UF_GDT_MODL_PARAM_Y_LENGTH:
   Use this enum type when creating tolerance feature that will reference
   faces of the modeling feature along the Y-axis of the feature.

   Use with following modeling features -
   1. Rectangular Slot, U Slot
      Modeling Feature Parameter: Width
      Tolerance feature will reference faces that are defined by Width
      parameter
   2. Ball End Slot
      Modeling Feature Parameter: Ball Diameter
      Tolerance feature will reference faces separated by distance equal to
      the ball diameter
   3. T Slot
      Modeling Feature Parameter: Bottom Width
      Tolerance feature will reference faces that are defined by Bottom Width
      parameter
   4. Rectangular Pad, Rectangular Pocket
      Modeling Feature Parameter: Y Length
      Tolerance feature will reference faces that are defined by Y Length
      parameter


   UF_GDT_MODL_PARAM_X_LENGTH_TOP:
   Use this enum type when creating tolerance feature that will reference
   top faces of the T Slot modeling feature along the X-axis of the feature.
   Modeling Feature Parameter: None


   UF_GDT_MODL_PARAM_Y_LENGTH_TOP:
   Use this enum type when creating tolerance feature that will reference
   top faces of the T Slot modeling feature along the Y-axis of the feature.
   Modeling Feature Parameter: Top Width
*/
enum UF_GDT_modl_parameter_e
{
    UF_GDT_MODL_PARAM_INVALID,
    UF_GDT_MODL_PARAM_NONE,
    UF_GDT_MODL_PARAM_ALL,
    UF_GDT_MODL_PARAM_HOLE,
    UF_GDT_MODL_PARAM_COUNTERBORE,
    UF_GDT_MODL_PARAM_COUNTERSINK,
    UF_GDT_MODL_PARAM_X_LENGTH,
    UF_GDT_MODL_PARAM_Y_LENGTH,
    UF_GDT_MODL_PARAM_X_LENGTH_TOP,
    UF_GDT_MODL_PARAM_Y_LENGTH_TOP
};

typedef enum UF_GDT_modl_parameter_e  UF_GDT_modl_parameter_t,
                                     *UF_GDT_modl_parameter_p_t;

/*******************************DATA STRUCTURES*****************************/

/* Defines the attributes required to describe a tolerance feature
   Alternatively the name and description of the tolerance feature may be
   manipulated directly using character strings and the UF_OBJ_read/write
   routines
*/
struct UF_GDT_description_s
{
    char *name;        /* Name of the tolerance feature/datum
                          NOTE :
                           . The name supplied may not be NULL.
                           . The name supplied must be unique within the
                             context of the tolerancing module.
                           . The name must be less than 31 characters in length.
                        */
    char *description; /* Description of the tolerance feature
                          NOTE : The description supplied is user defined and
                                 may be NULL.
                        */
};

typedef struct UF_GDT_description_s UF_GDT_description_t,
                                   *UF_GDT_description_p_t;


/*  Defines a tolerance for a feature control frame callout
    or zone refinement */
struct UF_GDT_tolerance_value_s
{
    tag_t  expression;     /* Tolerance value represented by an expression.
                            * NOTE: If set to "NULL_TAG", the "value" of the
                            * nominal will be used on input.  For output,
                            * the expression will contain the expressions
                            * reference and if created using an expression,
                            * the value will contain the value of that
                            * expression.
                            */
    double value;          /* Actual value of the tolerance */
    int    decimal_format; /* Number of digits to right of decimal point */
};

typedef struct UF_GDT_tolerance_value_s UF_GDT_tolerance_value_t,
                                       *UF_GDT_tolerance_value_p_t;

/* Defines the attributes of a datum identifier */
struct UF_GDT_datum_identifier_s
{
    char                      *datum_label;     /* Datum label of identifier */
    tag_t                     def_feat;         /* OBSOLETE: Unused by System */
    logical                   is_individual;    /* TRUE if datum is individual*/
};

typedef struct UF_GDT_datum_identifier_s UF_GDT_datum_identifier_t,
                                        *UF_GDT_datum_identifier_p_t;

/* Information used to apply statistical information to a tolerance
   specification (will evolve to accept additional statistical data) */
struct UF_GDT_statistical_info_s
{
    void *other_statistical_data;   /* Statistical data as needed */
};

typedef struct UF_GDT_statistical_info_s UF_GDT_statistical_info_t,
                                        *UF_GDT_statistical_info_p_t;

/* Information describing the shape of the zone being represented by a
   specific feature control frame */
struct UF_GDT_tolerance_zone_s
{
    UF_GDT_zone_shape_t         zone_shape;        /* Shape of the tolerance
                                                      zone */
    tag_t                       planar_ref;        /* Object that defines
                                                      zone when it is not
                                                      defined by the face set */
    tag_t                       expression;        /* Expression for the
                                                      tolerance value */
    double                      value;             /* Actual value of the
                                                      tolerance */
    int                         decimal_format;    /* Number of digits right
                                                      of decimal */
    UF_GDT_material_modifier_t  material_modifier; /* Material modifier */
};

typedef struct UF_GDT_tolerance_zone_s UF_GDT_tolerance_zone_t,
                                      *UF_GDT_tolerance_zone_p_t;

/* Defines information pertaining to a unit basis (length/area) refinement */
struct UF_GDT_unit_basis_s
{
    tag_t tolerance_expression; /* Expression defining tolerance value */
    tag_t length_expression;    /* Expression defining unit length */
    tag_t width_expression;     /* Expression defining unit width */
    int   decimal_format;       /* Decimal format of the expressions */
    int   ub_decimal_format;    /* Decimal format of the length/width
                                   expressions */
};

typedef struct UF_GDT_unit_basis_s UF_GDT_unit_basis_t,
                                  *UF_GDT_unit_basis_p_t;

/* Contains data concerning a datum reference located in a feature control
   frame. In the case of a multiple datum the first datum listed in the array
   is the multiple datum.
 */
struct UF_GDT_datum_reference_s
{
    tag_t                       datum_feature;      /* Tolerance feature for
                                                       this datum */
    UF_GDT_material_modifier_t *material_condition; /* <len:num_modifiers>
                                                       Array of the datum
                                                       reference's material
                                                       condition modifiers */
    int                         num_modifiers;      /* Number of modifiers
                                                       for datum */
};

typedef struct UF_GDT_datum_reference_s UF_GDT_datum_reference_t,
                                       *UF_GDT_datum_reference_p_t;

/* Contains data concerning a datum reference located in a feature control
   frame. In the case of a multiple datum the first datum listed in the array
   is the multiple datum.
 */
struct UF_GDT_drf_reference_s
{
    UF_GDT_datum_reference_t    datum_reference;
    tag_t                       definition;
};

typedef struct UF_GDT_drf_reference_s UF_GDT_drf_reference_t,
                                       *UF_GDT_drf_reference_p_t;


/* Represents a datum reference frame object
 */
struct UF_GDT_drf_data_s
{
    char                       *name;        /* Name of datum reference frame */
    char                       *description; /* Description of datum reference
                                              * frame */
    UF_GDT_drf_reference_p_t  primary;     /* Primary datum reference data */
    UF_GDT_drf_reference_p_t  secondary;   /* Secondary datum reference data */
    UF_GDT_drf_reference_p_t  tertiary;    /* Tertiary datum reference data */
};


typedef struct UF_GDT_drf_data_s UF_GDT_drf_data_t,
                                *UF_GDT_drf_data_p_t;


struct UF_GDT_proj_zone_s
{
    tag_t  expression;     /* Tolerance value represented by an expression */
    double value;          /* Actual value of the tolerance */
    int    decimal_format; /* Number of digits to right of decimal point */
    tag_t  direction;      /* The direction of the zone */
};

typedef struct UF_GDT_proj_zone_s UF_GDT_proj_zone_t, *UF_GDT_proj_zone_p_t;

/* Defines structure to return keyword data */
struct UF_GDT_keyword_s
{
    UF_GDT_keyword_id_t id;     /* Keyword id */
};

typedef struct UF_GDT_keyword_s UF_GDT_keyword_t,
                               *UF_GDT_keyword_p_t;

/* Defines information for the various modifications and refinements for a
   feature control frame

   The UF_GDT_MAX_BONUS frame modifier requires that the bonus_tol field be set.
 */
struct UF_GDT_modifier_data_s
{
    int               num_modifiers;   /* Number of modifiers */
    UF_GDT_modifier_types_t   *modifier_types; /* <len:num_modifiers> Array of modifier types */
    UF_GDT_proj_zone_t        *proj_zone;      /* Projected zone data */
    UF_GDT_unit_basis_t       *unit_length;    /* Unit basis length data */
    UF_GDT_unit_basis_t       *unit_area;      /* Unit basis area data */
    UF_GDT_statistical_info_t *statistics;     /* Statistical data */
    UF_GDT_tolerance_value_t  *bonus_tol;      /* Maximum bonus tolerance data*/
    int                       num_keywords;    /* Number of keywords */
    UF_GDT_keyword_p_t        keywords;        /* <len:num_keywords> Array of keywords */
};

typedef struct UF_GDT_modifier_data_s UF_GDT_modifier_data_t,
                                     *UF_GDT_modifier_data_p_t;

/* Defines the surfaces of a feature.  These are used by the ask, create, and
   set routines for tolerance feature. They are also used to define the
   origin surfaces for directed dimensions.

   Functions affected by the modification of this structure are:

 UF_GDT_ask_directed_dimension
 UF_GDT_ask_feature_parms
 UF_GDT_create_datum_identifier
 UF_GDT_create_fcf
 UF_GDT_create_instance
 UF_GDT_create_size_tolerance
 UF_GDT_set_directed_dimension
*/
struct UF_GDT_surface_parms_s
{
    int                             num_faces;  /* Number of faces that define
                                                 * the current surface */
    tag_p_t                         faces;      /* <len:num_faces> Set of face tags */
};

typedef struct UF_GDT_surface_parms_s UF_GDT_surface_parms_t,
                                     *UF_GDT_surface_parms_p_t;

/* Defines the attributes of a size tolerance . These are used by the size
   tolerance add, ask, create, and set routines. The values of the upper and
   lower tolerance values are both ADDED to the nominal value to obtain the
   overall tolerance for the feature.

   Functions affected by the modification of this structure are:
 UF_GDT_add_size_tolerance
 UF_GDT_create_size_tolerance
 UF_GDT_ask_size_tolerance_parms
 UF_GDT_ask_size_tolerance_tag
 UF_GDT_set_size_tolerance_parms
 */
struct UF_GDT_size_tolerance_s
{
    UF_GDT_size_value_type_t value_type; /* Type of size tolerance value */
    tag_t            dimension;      /* Tolerance value's dimension
                                              * identifier
                                              *
                                              * NOTE: This field is no longer
                                              * used and will always return
                                              * a NULL_TAG.
                                              */

    double           nominal_value;  /* Nominal value of tolerance */
    UF_GDT_tolerance_value_t upper_tol;      /* Upper tolerance value */
    UF_GDT_tolerance_value_t lower_tol;      /* Lower tolerance value */
    UF_GDT_tol_format_t      tol_format;     /* Displayed format of the
                                               size tol */
    UF_GDT_modifier_data_p_t modifier_data;  /* Modifier data */
    int                      decimal_format; /* Nominal Precision */
};

typedef struct UF_GDT_size_tolerance_s UF_GDT_size_tolerance_t,
                                      *UF_GDT_size_tolerance_p_t;

/* Defines the attributes of a depth tolerance . These are used by the depth
   tolerance ask and set routines. The values of the upper and
   lower tolerance values are both ADDED to the nominal value to obtain the
   overall tolerance for the feature.

   Functions affected by the modification of this structure are:
 UF_GDT_ask_depth_tolerance_parms
 UF_GDT_set_depth_tolerance_parms
*/
struct UF_GDT_depth_tolerance_s
{
    double                   nominal_value;  /* Nominal value of tolerance */
    UF_GDT_tolerance_value_t upper_tol;      /* Upper tolerance value */
    UF_GDT_tolerance_value_t lower_tol;      /* Lower tolerance value */
    UF_GDT_tol_format_t      tol_format;     /* Displayed format of the
                                                depth tol */
    int                      decimal_format; /* Nominal Precision */
};

typedef struct UF_GDT_depth_tolerance_s UF_GDT_depth_tolerance_t,
                                       *UF_GDT_depth_tolerance_p_t;

/* The following data structures are defined for limits and fits tolerance,
   These are used by the limits and fits tolerance ask, set routines.

   Functions affected by the modification of these structure are:
 UF_GDT_ask_depth_tolerance_parms
 UF_GDT_set_depth_tolerance_parms
 UF_GDT_set_depth_tolerance_parms
*/

enum UF_GDT_limits_and_fits_display_type_e
{
    UF_GDT_DEFAULT_DISPLAY_TYPE = 0,
    UF_GDT_LIMITS_DISPLAY_TYPE,
    UF_GDT_TOLERANCE_DISPLAY_TYPE,
    UF_GDT_NORMAL_DISPLAY_TYPE
};
typedef enum UF_GDT_limits_and_fits_display_type_e
             UF_GDT_limits_and_fits_display_type_t, *UF_GDT_limits_and_fits_display_type_p_t;

struct UF_GDT_limits_and_fits_data_s
{
    char *  deviation;      /* Fundamental deviation letter */
    char *  fit_type;       /* Type of fit system */
    int  fit_grade;         /* Fit grade */
    int  tol_grade;         /* Tolerance grade */
    int  dim_precision;     /* Nominal dimension precision */
    UF_GDT_limits_and_fits_display_type_t display_type;  /* Instance display type */
};

typedef struct UF_GDT_limits_and_fits_data_s  UF_GDT_limits_and_fits_data_t,
                                           *UF_GDT_limits_and_fits_data_p_t;
struct UF_GDT_limits_and_fits_tolerance_s
{
    UF_GDT_limits_and_fits_data_p_t limits_and_fits_data; /* Limits and fits data */
    UF_GDT_size_tolerance_p_t plus_minus_data;            /* Plus minus data */
};

typedef struct UF_GDT_limits_and_fits_tolerance_s UF_GDT_limits_and_fits_tolerance_t,
                                           *UF_GDT_limits_and_fits_tolerance_p_t;

struct UF_GDT_thread_data_s
{
    int pitch_dia_grade;               /* Tolerance grade based on pitch diameter */
    char* pitch_dia_deviation;         /* Deviation based on pitch diameter */
    int grade;                         /* Tolerance grade based on major/minor diameter */
    char* deviation;                   /* Deviation based on major/minor diameter */
    int thread_class;                  /* Thread class for ANSI non-metric threads */
};
typedef struct UF_GDT_thread_data_s  UF_GDT_thread_data_t,
                                   *UF_GDT_thread_data_p_t;

struct UF_GDT_thread_tolerance_s
{
    UF_GDT_thread_data_p_t thread_tol;            /* Thread data */
    UF_GDT_modifier_data_p_t modifier_data;       /* Modifier data */
};
typedef struct UF_GDT_thread_tolerance_s UF_GDT_thread_tolerance_t,
                                      *UF_GDT_thread_tolerance_p_t;


/* Defines information for feature definition data */
struct UF_GDT_geometric_definition_s
{
    UF_GDT_geometric_definition_type_t type; /* Type of definition */
    tag_t                            so_tag; /* Smart object of definition */
    double                           radius; /* UNUSED */
    tag_t                     trimmed_sheet; /* Trimmed sheet of region
                                                definition */
};

typedef struct UF_GDT_geometric_definition_s UF_GDT_geometric_definition_t,
                                            *UF_GDT_geometric_definition_p_t;

/* The following data structure contains modeling feature data. Currently,
 *  tolerance feature can reference following NX modeling features -
 *  1. Simple Hole
 *  2. Counterbore Hole
 *  3. Countersink Hole
 *  4. Extrusion/Revolution
 *  5. Boss
 *  6. Edge Blend
 *  7. Rectangular Pad
 *  8. Rectangular Slot
 *  9. Ball End Slot
 *  10. U Slot
 *  11. T Slot
 *  12. Cylindrical Pocket
 *  13. Rectangular Pocket
 *  14. Symbolic Thread
 *
 *  This data can be used in create/ask/set routines for modeling  based
 *  tolerance features.
 */
struct UF_GDT_modl_data_s
{
    int num_modl_features;               /* Number of modeling features */
    tag_p_t modl_feature_list;           /* <len:num_modl_features> Modeling feature list */
    UF_GDT_modl_parameter_t modl_param;  /* Modeling feature parameter to use for
                                          * face mapping between modeling feature and
                                          * tolerance feature */
    tag_t face_map;                      /* Object to use for inter part face mapping
                                          * face_map = NULL_TAG, for tolerance
                                          *            feature in piece part
                                          *          = Part occurrence tag, for
                                          *            tolerance feature in assembly part
                                          *          = Linked feature tag, for tolerance
                                          *            feature referencing wave linked
                                          *            geometry
                                          */
};

typedef struct UF_GDT_modl_data_s UF_GDT_modl_data_t, *UF_GDT_modl_data_p_t;

/* The following data structure contains the product attributes for the tolerance feature.
   Please refer <uf_pd_types.h> for detailed description of product attributes.

 */
struct UF_GDT_product_attribute_s
{
    int num_attributes;                     /* Number of product attributes. */
    UF_PD_product_attribute_p_t attributes; /* List of product attributes. */
};

typedef struct UF_GDT_product_attribute_s UF_GDT_product_attribute_t, *UF_GDT_product_attribute_p_t;


/* Defines the set of general properties for the tolerance feature. This data
   is common to all tolerance features.

   Functions affected by the modification of this structure are:
 UF_GDT_create_datum_identifier
 UF_GDT_create_datum_multiple
 UF_GDT_create_fcf
 UF_GDT_create_size_tolerance
 UF_GDT_ask_feature_parms
 */
struct UF_GDT_feature_parms_s
{
    int           num_faces;   /* Number of faces in the tolerance
                                        * feature specification.
                                        * NOTE: For wall thickness use
                                        * sets member below. */
    tag_t        *face_list;   /* <len:num_faces> Array of faces that describe the
                                        * tolerance feature.
                                        * NOTE: For wall thickness use
                                        * sets member below.
                                        * For spline/gear features, use sets member below. */
    UF_GDT_description_p_t descript;   /* The unique name and Description of
                                        * the tolerance feature */
    UF_GDT_feature_type_t   feature;   /* Geometric feature type of the
                                        * tolerance feature */
    UF_GDT_pattern_type_t   pattern;   /* Pattern type of the tolerance
                                        * feature */
    UF_GDT_modifier_data_p_t modifier_data; /* Tolerance feature Modifier
                                             * data */
    int                   num_sets;    /* Number of distinct sets of surfaces
                                        * for this feature
                                        * NOTE: To use face_list member
                                        * set this argument to 0. */
    UF_GDT_surface_parms_p_t  *sets;   /* <len:num_sets> Array of surface sets for this
                                        * feature */
    UF_GDT_geometric_definition_t def; /* Geometric Definition for this
                                        * feature */
    int num_modl_sets;                 /* Number of modeling features sets
                                        * NOTE: To use sets or face_list member,
                                        * set this argument to 0. */
    UF_GDT_modl_data_p_t *modl_sets;   /* <len:num_modl_sets> Modeling feature data sets for
                                        * tolerance feature creation */
};

typedef struct UF_GDT_feature_parms_s UF_GDT_feature_parms_t,
                                     *UF_GDT_feature_parms_p_t;

/* Contains the data concerning a single data frame for a feature control
   frame.
 */
struct UF_GDT_data_frame_s
{
    UF_GDT_tolerance_zone_p_t   tolerance_zone; /* Tolerance zone for frame */
    UF_GDT_datum_reference_p_t  primary;        /* Primary datum reference data */
    UF_GDT_datum_reference_p_t  secondary;      /* Secondary datum reference data */
    UF_GDT_datum_reference_p_t  tertiary;       /* Tertiary datum reference data */
    UF_GDT_modifier_data_p_t    modifier_data;  /* Frame modifiers */
};

typedef struct UF_GDT_data_frame_s UF_GDT_data_frame_t, *UF_GDT_data_frame_p_t;


/* Defines the information for a feature control frame (geometric tolerance)
   used by add, ask, create, and set routines.
 */
struct UF_GDT_fcf_s
{
    UF_GDT_characteristic_t   characteristic;  /* Type of geometric tolerance */
    int                       num_frames;      /* The number of frames in the
                                                  geometric tolerance call-out
                                                */
    UF_GDT_data_frame_p_t     data_frame;      /* <len:num_frames> Array of data frames for the
                                                  fcf */
};

typedef struct UF_GDT_fcf_s UF_GDT_fcf_t, *UF_GDT_fcf_p_t;

/* Contains information used by the multiple datum add, ask, create, and set
   routines.
 */
struct UF_GDT_multiple_datum_s
{
    int            num_datums;     /* Number of datum identifiers that
                                              define the multiple datum */
    tag_t         *datum_features; /* <len:num_datums> Array of datum features referenced
                                              by the geometric tolerance */
    tag_t          def_feat;       /* Where multiple feature types are
                                              possible a defining model feature
                                              for the multiple datum */
};

typedef struct UF_GDT_multiple_datum_s UF_GDT_multiple_datum_t,
                                      *UF_GDT_multiple_datum_p_t;

/*  Contains information pertaining to a datum target point. */
struct UF_GDT_datum_target_point_s
{
    tag_t   point_on_surface;  /* The identifier of the point which defines the
                                  target point */
    double  point_data[3];     /* The actual position of the target on their
                                  referencing plane */
    tag_t   datum_feature;     /* The identifier of the datum feature that the
                                  target constrains */
    int     target_index;      /* The identifier of the target point */
};

typedef struct UF_GDT_datum_target_point_s UF_GDT_datum_target_point_t,
                                          *UF_GDT_datum_target_point_p_t;

/*  Defines information pertaining to target line data */
struct UF_GDT_datum_target_line_s
{
    tag_t   start_point;       /* Identifier of line start point (smart pt) */
    tag_t   end_point;         /* Identifier of line end point (smart pt) */
    double  start_data[3];     /* Absolute position of start point (this is
                                * used for OUTPUT only) */
    double  end_data[3];       /* Absolute position of end point (this is used
                                * for OUTPUT only) */
    tag_t   datum_feature;     /* Identifier of parent datum */
    int     target_index;      /* Index of target */
};

typedef struct UF_GDT_datum_target_line_s UF_GDT_datum_target_line_t,
                                         *UF_GDT_datum_target_line_p_t;

/* Defines the parameters for constructing a circular or annular datum
   target area.
 */
struct UF_GDT_target_dia_area_s
{
    tag_t datum_feature;    /* The tag of the parent datum feature the target
                               is to be applied to.
                            */
    int target_index;       /* Datum target index to assign to new datum
                               targets.  On creation, the target index must be
                               unique in the context of the other datum targets
                               on the feature.
                            */
    tag_t point;            /* Identifier of smart point locating the center
                             * of the target. */
    UF_GDT_tolerance_value_t diameter;
                            /* Size of the outer datum target area diameter */
    UF_GDT_tolerance_value_t inner_dia;
                            /* Size of the inner diameter for annular areas */
    logical is_planar;      /* Is this a planar datum target area?
                             * Creation and Query routines only.
                             */
    tag_t orientation;      /* Orientation of area relative to surface.
                             * Should be XFORM tag (see uf_so.h).  A
                             * NULL_TAG will default to surface orientation.
                             */
    double location[3];     /* Absolute position of target (output only) */
};

typedef struct UF_GDT_target_dia_area_s UF_GDT_target_dia_area_t,
                                       *UF_GDT_target_dia_area_p_t;

/* Defines information for rectangular target area data */
struct UF_GDT_target_rect_area_s
{
    tag_t datum_feature;    /* This corresponds to the tag of the parent datum
                               feature the target is to be applied to.
                            */
    int target_index;       /* Datum target index to assign to new datum
                               targets.  On creation, the target index must be
                               unique in the context of the other datum targets
                               on the feature.
                            */
    tag_t point;            /* Identifier of smart point locating the center
                             * of the target. */
    logical is_planar;      /* Is this a planar datum target area?
                             * Creation and Query routines only.
                             */
    tag_t orientation;      /* Orientation of area relative to surface.
                             * Should be XFORM tag (see uf_so.h).  A
                             * NULL_TAG will default to surface orientation.
                             */
    UF_GDT_tolerance_value_t length;
                            /* Length of rectangular area */
    UF_GDT_tolerance_value_t height;
                            /* Height of rectangular area */
    double location[3];     /* Absolute position of target (output only) */
};

typedef struct UF_GDT_target_rect_area_s UF_GDT_target_rect_area_t,
                                        *UF_GDT_target_rect_area_p_t;

/* Defines information for non planar datum target area trim operations */
struct UF_GDT_target_non_planar_data_s
{
    logical project_normals;     /* Project along surface normals or use the
                                  * projection vector.
                                  */

    double projection_vector[3]; /* Vector for curves projected along a vector */

    int point_key;               /* Point defines region to:
                                  * 0 = discard or 1 = keep
                                  */

    double point_coords[3];      /* Location of the keep/discard point (ABS)   */
};

typedef struct UF_GDT_target_non_planar_data_s UF_GDT_target_non_planar_data_t,
                                              *UF_GDT_target_non_planar_data_p_t;

/* Defines information for user defined target area data */
struct UF_GDT_target_udef_area_s
{
    tag_t datum_feature;    /* This corresponds to the tag of the parent datum
                               feature the target is to be applied to.
                            */
    int target_index;       /* Datum target index to assign to new datum
                               targets.  On creation, the target index must be
                               unique in the context of the other datum targets
                               on the feature.
                            */
    tag_p_t curves;         /* <len:num_curves> Array of curves defining the user defined area.
                             * If planar, then the curves must for a closed
                             * planar loop.
                             * If not planar, then the curves will be used with
                             * np_data to create the area.
                             */
    int num_curves;         /* Number of curves in the array */
    logical is_planar;      /* Is this a planar datum target area?
                             * Creation and Query routines only.
                             */
    struct UF_GDT_target_non_planar_data_s np_data;
};

typedef struct UF_GDT_target_udef_area_s UF_GDT_target_udef_area_t,
                                        *UF_GDT_target_udef_area_p_t;


/* Defines information for cylindrical target area */
struct UF_GDT_target_cyl_area_s
{
    tag_t datum_feature;           /* Parent datum feature                */
    int target_index;              /* Unique index of datum target        */
    tag_t start_point;             /* Identifier of start point locating
                                    * the start point of the target       */
    tag_t end_point;               /* Identifier of end  point locating
                                    * the end point of the target         */
    double start_location[3];      /* Absolute position of start point
                                    * (output only)                       */
    double end_location[3];        /* Absolute position of end point
                                    * (output only)                       */
};

typedef struct UF_GDT_target_cyl_area_s UF_GDT_target_cyl_area_t,
                                       *UF_GDT_target_cyl_area_p_t;

/* Defines information for directed dimensions data */
struct UF_GDT_directed_dimension_s
{
    UF_GDT_directed_dimension_type_t type;      /* Type of directed
                                                 * dimension */
    UF_GDT_size_tolerance_t          size_data; /* Size data for the
                                                 * dimension */
    tag_t                            origin;       /* Tag of the origin
                                                    * tolerance feature.
                                                    * OBSOLETE IN V17.0 */
    UF_GDT_surface_parms_p_t         origin_surfs; /* Surface data for the
                                                    * origin feature. */
    UF_GDT_geometric_definition_t    origin_def;   /* Definition for the
                                                    * origin feature. */
};

typedef struct UF_GDT_directed_dimension_s UF_GDT_directed_dimension_t,
                                          *UF_GDT_directed_dimension_p_t;
struct UF_GDT_directed_dimension1_s
{
    UF_GDT_directed_dimension_type_t type;      /* Type of directed
                                                 * dimension */
    UF_GDT_size_tolerance_p_t          size_data; /* Size data for the
                                                 * dimension */
    tag_t                            origin;       /* Tag of the origin
                                                    * tolerance feature.
                                                    * OBSOLETE IN V17.0 */
    UF_GDT_surface_parms_p_t         origin_surfs; /* Surface data for the
                                                    * origin feature. */
    UF_GDT_geometric_definition_t    origin_def;   /* Definition for the
                                                    * origin feature. */
};

typedef struct UF_GDT_directed_dimension1_s UF_GDT_directed_dimension1_t,
                                          *UF_GDT_directed_dimension1_p_t;
/* Defines coordinates of a 3-D point */
struct UF_GDT_point_s
{
    double coords[3];
};

typedef struct UF_GDT_point_s UF_GDT_point_t,
                             *UF_GDT_point_p_t;

/* Defines information for leader data */
struct UF_GDT_leader_spec_s
{

    tag_t view;                        /* Tag of view the leader terminates in*/
    tag_t terminator;                  /* Tag of object leader is attached to */
    UF_GDT_point_t attach_point;       /* Point of the leader's terminator    */
    UF_GDT_point_t stub_points[2];     /* Stub start and end points.  Used only
                                        * in UF_GDT__ask_leader, not used for
                                        * leader creation.
                                        */
    int num_intermediates;             /* Number of intermediate points       */
    UF_GDT_point_p_t intermediates;    /* <len:num_intermediates> Array of intermediate leader points.
                                        * Stored from terminator to callout.
                                        * Does not include stub points or the
                                        * leader terminator point.
                                        */
    UF_GDT_leader_type_t type;         /* The type of leader's arrowhead      */
    logical is_profile_leader;         /* Is the leader a profile leader      */
    logical filled;                    /* Is the leader's arrowhead filled?   */
    logical all_around;                /* Is the leader an all_around leader? */
    double all_around_diameter;        /* Diameter of the all around symbol   */
    double dot_diameter;               /* Diameter of dot, if a dot terminator*/
    double arrowhead_length;           /* Length of the leader arrowhead      */
    double arrowhead_angle;            /* Angle of leader arrowhead (Degrees) */
    double stub_length;                /* Length of the leader's stub         */
    UF_GDT_stub_direction_t direction; /* Direction of the leader's stub      */
    tag_t profile_term2;               /* 2nd profile leader attachment object*/
    UF_GDT_point_t profile_attach;     /* 2nd profile leader attachment point */
    double profile_ldr_length;         /* Length of the 2nd profile leader    */
    int leader_color;                  /* Color of the leader                 */
    int leader_font;                   /* Font of the leader                  */
    int leader_width;                  /* (Line) Width of the leader
                                        * This width should be described
                                        * using the UF_OBJ_WIDTH definitions
                                        * in uf_obj.h
                                        */
    int arrowhead_color;               /* Color of the leader's arrowhead     */
    int arrowhead_font;                /* Font of the leader's arrowhead      */
    int arrowhead_width;               /* (Line) Width of leader's arrowhead
                                        * This width should be described
                                        * using the UF_OBJ_WIDTH definitions
                                        * in uf_obj.h
                                        */
    UF_DRF_arrow_info_t arrow_info;    /* Structure about the terminator.
                                        * Used only with UF_GDT__ask_leader, not
                                        * for leader creation.
                                        * Arrow_info includes:
                                        *     arrow sequence number
                                        *     arrowhead type
                                        *     arrowhead fill
                                        *     arrowhead origin
                                        *     arrowhead angle (Radians)
                                        *     arrowhead include angle (Radians)
                                        *     arrowhead height/length
                                        *     arrowhead width
                                        */
};

typedef struct UF_GDT_leader_spec_s UF_GDT_leader_spec_t,
                                   *UF_GDT_leader_spec_p_t;

/* Defines information for annotation data */
struct UF_GDT_annotation_tags_s
{
    tag_p_t dimension_tags; /* <len:num_dimension_tags> */
    int num_dimension_tags;

    tag_p_t feature_control_frame_tags;  /* <len:num_feature_control_frame_tags>
                                            created as notes */
    int num_feature_control_frame_tags;

    tag_p_t appended_text_tags;  /* <len:num_appended_text_tags> created as notes */
    int num_appended_text_tags;

    int num_non_dimensional_leaders;
};

typedef struct UF_GDT_annotation_tags_s UF_GDT_annotation_tags_t,
                                       *UF_GDT_annotation_tags_p_t;

/* Defines information for tolerance callout string */
struct UF_GDT_callout_string_s
{
    tag_t tolerance;              /* Tolerance feature or FCF tag */
    UF_GDT_tolerance_type_t type; /* Tolerance type               */
    char *string;                 /* Callout string for tolerance */
};

typedef struct UF_GDT_callout_string_s UF_GDT_callout_string_t,
                                      *UF_GDT_callout_string_p_t;

/*****************************************************************************
                               Error Defintions
*****************************************************************************/

#define UF_GDT_ERROR_BASE                       ERROR_UF_GDT_base
#define UF_GDT_ERROR_RANGE                      5000
#define UF_GDT_NO_ERRORS                        0
#define UF_GDT_ERR_DATUM_EXISTS                 ( ERROR_UF_GDT_base + 1 )

/* NOTE: The "UF_GDT_ERR_NOT_TOL_FEAT" error is returned when a passed tag
   is not a "UF_tolerance_feature_type" AND "UF_tolerance_feature_subtype".
   Passing the tag of a "UF_tolerance_model_subtype" will cause this error */

#define UF_GDT_ERR_NOT_TOL_FEAT                 ( ERROR_UF_GDT_base + 2 )
#define UF_GDT_ERR_SIZE_TOL_EXISTS              ( ERROR_UF_GDT_base + 3 )
#define UF_GDT_ERR_NOT_INSTANCE                 ( ERROR_UF_GDT_base + 4 )
#define UF_GDT_ERR_NOT_FCF                      ( ERROR_UF_GDT_base + 5 )
#define UF_GDT_ERR_BAD_FACE_IN_LIST             ( ERROR_UF_GDT_base + 6 )
#define UF_GDT_ERR_BAD_TOLERANCE_TYPE           ( ERROR_UF_GDT_base + 7 )
#define UF_GDT_ERR_BAD_FEATURE_TYPE             ( ERROR_UF_GDT_base + 8 )
#define UF_GDT_ERR_BAD_CHARACTERISTIC           ( ERROR_UF_GDT_base + 9 )
#define UF_GDT_ERR_BAD_MAT_MODIFIER             ( ERROR_UF_GDT_base + 10 )
#define UF_GDT_ERR_BAD_ZONE_SHAPE               ( ERROR_UF_GDT_base + 11 )
#define UF_GDT_ERR_BAD_FRAME_MOD                ( ERROR_UF_GDT_base + 12 )
#define UF_GDT_ERR_BAD_DATUM_PREC               ( ERROR_UF_GDT_base + 13 )
#define UF_GDT_ERR_BAD_STANDARD                 ( ERROR_UF_GDT_base + 14 )
#define UF_GDT_ERR_BAD_TOL_FORMAT               ( ERROR_UF_GDT_base + 15 )
#define UF_GDT_ERR_BAD_ENUM                     ( ERROR_UF_GDT_base + 16 )
#define UF_GDT_ERR_TOO_MANY_FRAMES              ( ERROR_UF_GDT_base + 17 )
#define UF_GDT_ERR_BAD_COUNT                    ( ERROR_UF_GDT_base + 18 )
#define UF_GDT_ERR_BAD_PATTERN_TYPE             ( ERROR_UF_GDT_base + 19 )
#define UF_GDT_ERR_BAD_ANNOTATION               ( ERROR_UF_GDT_base + 20 )
#define UF_GDT_ERR_TEST_FAILURE                 ( ERROR_UF_GDT_base + 21 )
#define UF_GDT_ERR_NULL_LABEL                   ( ERROR_UF_GDT_base + 22 )
#define UF_GDT_ERR_BAD_EDGE                     ( ERROR_UF_GDT_base + 23 )
#define UF_GDT_ERR_NOT_MULTIPLE_DATUM           ( ERROR_UF_GDT_base + 24 )
#define UF_GDT_ERR_UB_NOT_ALLOWED               ( ERROR_UF_GDT_base + 25 )
#define UF_GDT_ERR_UB_IS_NULL                   ( ERROR_UF_GDT_base + 26 )
#define UF_GDT_ERR_UB_INTERROGATE               ( ERROR_UF_GDT_base + 27 )
#define UF_GDT_ERR_NOT_PROFILE_FCF              ( ERROR_UF_GDT_base + 28 )
#define UF_GDT_ERR_INVALID_PROFILE_ZON          ( ERROR_UF_GDT_base + 29 )
#define UF_GDT_ERR_INVALID_INSTANCE             ( ERROR_UF_GDT_base + 30 )
#define UF_GDT_ERR_FEATURE_NOT_PULLED           ( ERROR_UF_GDT_base + 31 )
#define UF_GDT_ERR_DWG_DISPLAYED                ( ERROR_UF_GDT_base + 32 )
#define UF_GDT_ERR_INVALID_PROFILE_TOL          ( ERROR_UF_GDT_base + 33 )
#define UF_GDT_ERR_NO_SIZE_DATA_ON_FEATURE      ( ERROR_UF_GDT_base + 34 )
#define UF_GDT_ERR_NOT_SUBTOLERANCE_TYPE        ( ERROR_UF_GDT_base + 35 )
#define UF_GDT_ERR_NO_TOLERANCE_WITH_INDEX      ( ERROR_UF_GDT_base + 36 )
#define UF_GDT_ERR_NO_DIRECTED_DIM              ( ERROR_UF_GDT_base + 37 )
#define UF_GDT_ERR_BAD_SIZE_VALUE_TYPE          ( ERROR_UF_GDT_base + 38 )
#define UF_GDT_ERR_NON_POSITIVE_PARAMETERS      ( ERROR_UF_GDT_base + 39 )
#define UF_GDT_ERR_INVALID_REGION_BODIES        ( ERROR_UF_GDT_base + 40 )
#define UF_GDT_ERR_FEATURE_NOT_DATUM            ( ERROR_UF_GDT_base + 41 )
#define UF_GDT_ERR_NO_INDEXED_LEADER            ( ERROR_UF_GDT_base + 42 )
#define UF_GDT_ERR_NO_ADD_PROFILE_LDR           ( ERROR_UF_GDT_base + 43 )
#define UF_GDT_ERR_NO_ADD_TO_INSTANCE           ( ERROR_UF_GDT_base + 44 )
#define UF_GDT_ERR_NO_REMOVE_ONLY_LDR           ( ERROR_UF_GDT_base + 45 )
#define UF_GDT_ERR_NOT_FEATURE_INSTANCE         ( ERROR_UF_GDT_base + 46 )
#define UF_GDT_ERR_INVALID_VIEW                 ( ERROR_UF_GDT_base + 47 )
#define UF_GDT_ERR_NOT_DATUM_INSTANCE           ( ERROR_UF_GDT_base + 48 )
#define UF_GDT_ERR_INVALID_ASSOC_TYPE           ( ERROR_UF_GDT_base + 49 )
#define UF_GDT_ERR_TOL_VALIDATION_FAILED        ( ERROR_UF_GDT_base + 50 )
#define UF_GDT_ERR_NOT_PULLED_SUBTOLERANCE      ( ERROR_UF_GDT_base + 51 )
#define UF_GDT_ERR_INVALID_PATTERN_QUERIED      ( ERROR_UF_GDT_base + 52 )
#define UF_GDT_ERR_NOT_WALL_THICKNESS           ( ERROR_UF_GDT_base + 53 )
#define UF_GDT_ERR_NOT_COMPLEX_TOL_FEAT         ( ERROR_UF_GDT_base + 54 )
#define UF_GDT_ERR_NOT_COMPLEX_SUB_FEAT         ( ERROR_UF_GDT_base + 55 )
#define UF_GDT_ERR_NOT_VALID_FEAT_TYPE_FOR_LIM_FITS          ( ERROR_UF_GDT_base + 56 )
#define UF_GDT_ERR_NOT_VALID_FEAT_TYPE_FOR_LIM_FITS_ENGLISH  ( ERROR_UF_GDT_base + 57 )
#define UF_GDT_ERR_NOT_VALID_DATA_FOR_PART_UNIT              ( ERROR_UF_GDT_base + 58 )
#define UF_GDT_ERR_INVALID_LIM_FITS_DATA                     ( ERROR_UF_GDT_base + 59 )
#define UF_GDT_ERR_INCH_PART_WITH_ISO_STANDARD               ( ERROR_UF_GDT_base + 60 )
#define UF_GDT_ERR_UNVAILABLE_DATA_FOR_CURRENT_SETTING       ( ERROR_UF_GDT_base + 61 )
#define UF_GDT_ERR_NO_LIMITS_AND_FITS_TOLERANCE              ( ERROR_UF_GDT_base + 62 )
#define UF_GDT_ERR_BAD_PRECEDENCE_TYPE                       ( ERROR_UF_GDT_base + 63 )
#define UF_GDT_ERR_INVALID_FACES_FOR_EDIT                    ( ERROR_UF_GDT_base + 64 )
#define UF_GDT_ERR_UPDATE_PENDING               ( ERROR_UF_GDT_base + 65 )
#define UF_GDT_ERR_INVALID_KEYWORD              ( ERROR_UF_GDT_base + 66 )
#define UF_GDT_ERR_FEAT_NOT_VALID               ( ERROR_UF_GDT_base + 67 )
#define UF_GDT_ERR_NOT_DATUM                    ( ERROR_UF_GDT_base + 68 )
#define UF_GDT_ERR_NOT_BASE                     ( ERROR_UF_GDT_base + 69 )
#define UF_GDT_ERR_DELETED_DATUM                ( ERROR_UF_GDT_base + 70 )
#define UF_GDT_ERR_NOT_IDENT_DATUM              ( ERROR_UF_GDT_base + 71 )
#define UF_GDT_ERR_INVALID_THREAD_TOL           ( ERROR_UF_GDT_base + 72 )
#define UF_GDT_ERR_INVALID_FEAT_TYPE_FOR_THREAD_TOL          ( ERROR_UF_GDT_base + 73 )
#define UF_GDT_ERR_INVALID_MODL_DATA                         ( ERROR_UF_GDT_base + 74 )
#define UF_GDT_ERR_MODL_FEATURES_NOT_FULLY_LOADED            ( ERROR_UF_GDT_base + 75 )
#define UF_GDT_ERR_INVALID_FACE_MAP             ( ERROR_UF_GDT_base + 76 )
#define UF_GDT_ERR_FACE_MAP_MISMATCH            ( ERROR_UF_GDT_base + 77 )
#define UF_GDT_ERR_INVALID_MODL_FEATURE_TYPE    ( ERROR_UF_GDT_base + 78 )
#define UF_GDT_ERR_INVALID_MODL_PARAM           ( ERROR_UF_GDT_base + 79 )
#define UF_GDT_ERR_MODL_PARAM_MISMATCH          ( ERROR_UF_GDT_base + 80 )
#define UF_GDT_ERR_MODL_FEATURE_NULL_TAG        ( ERROR_UF_GDT_base + 81 )
#define UF_GDT_ERR_INVALID_PRODUCT_ATT_NUM_FOR_SPLINE_GEAR    ( ERROR_UF_GDT_base + 82 )
#define UF_GDT_END_OF_TABLE                     (0)

#define IS_UF_GDT_ERROR(error) \
          ((error >= UF_GDT_ERROR_BASE) && (error <= (UF_GDT_ERROR_BASE + 999)))
#define IS_UF_GDT_WARNING(error) \
      ((error >=UF_GDT_ERROR_BASE + 900) && (error <=(UF_GDT_ERROR_BASE + 999)))

/* errors 900 - 999 are reserved for warnings */
#define UF_GDT_WARNING                          (UF_GDT_ERROR_BASE + 900)

/*****************************************************************************
                              Function Prototypes
******************************************************************************/



/******************************************************************************
Add a datum identifier to an existent tolerance feature.

This function does not create a new tolerance feature. If an entirely
new tolerance feature is required use the UF_GDT_create_datum_identifier
routine.  The tolerance_feature parameter should be a UF_tolerance_feature_type.

Note: More than one datum identifier could be added to a tolerance feature one
at a tome.

Return Codes -
      UF_GDT_NO_ERRORS
      UF_GDT_ERR_NOT_TOL_FEAT
      UF_err_program_not_initialize
      UF_GDT_ERR_NULL_LABEL

Environment: Internal  and  External
See Also:
 UF_GDT_create_datum_identifier
History: Original release was in 14.0.
 *****************************************************************************/
extern UFUNEXPORT int UF_GDT_add_datum_identifier(
tag_t tolerance_feature ,/* <I>
                         Tolerance Feature to associate datum
                         identifier
                         */
UF_GDT_datum_identifier_t * datum_data  /* <I>
                                        Creation data for new datum
                                        identifier
                                        */
);


/******************************************************************************
This function adds a geometric tolerance to an existing tolerance feature.
This function does not create a new tolerance feature. If an entirely new
tolerance feature is required use the UF_GDT_create_fcf routine.

Environment: Internal  and  External
See Also:
 UF_GDT_create_fcf
History:Original release was in 14.0.
 ******************************************************************************/
extern UFUNEXPORT int UF_GDT_add_fcf(
tag_t tolerance_feature ,/* <I>
                         Tolerance Feature to associate datum identifier
                         */
UF_GDT_fcf_t * tolerance_data ,/* <I>
                               Creation data for new geometric tolerance
                               */
tag_t * fcf  /* <O>
             Identifier of the geometric tolerances feature control frame
             */
);

/******************************************************************************

This function adds a size tolerance to an existing tolerance feature.
This function does not create a new tolerance feature. If an entirely new
tolerance feature is required use the UF_GDT_create_size_tolerance routine.

Environment: Internal  and  External
See Also:
History: Original release was in 14.0.

 ******************************************************************************/
extern UFUNEXPORT int UF_GDT_add_size_tolerance(
tag_t tolerance_feature ,/* <I>
                         Tolerance Feature to associate size tolerance
                         */
UF_GDT_size_tolerance_t * size_data  /* <I>
                                     Creation data for new size tolerance
                                     */
);

/******************************************************************************
Returns the set of faces associated with the tolerance feature or
tolerance datum feature.  If the feature is in an out of date or retained
state, it is possible that no faces are returned to the caller.
Some valid datum features may not have any associated faces (for
example, datum target points, line, areas, centerplanes, etc.).

Environment: Internal  and  External
See Also:
History:Original release was in 14.0.
 ******************************************************************************/
extern UFUNEXPORT int UF_GDT_ask_faces(
tag_t tolerance_feature ,/* <I>
                         Tolerance Feature to inquire
                         */
int * num_faces ,/* <O>
                 Number of faces in face array
                 */
tag_p_t * faces  /* <OF,len:num_faces>
                 Array of faces associated with tolerance feature.
                 Use UF_free to deallocate memory when done.
                 */
);


/******************************************************************************
Queries the unique tolerance index for the given feature control
frame or tolerance feature.  A tolerance feature tag can only be passed into
this routine if the tolerance feature has a tolerance of size.

Environment: Internal  and  External
See Also:
History:This function was originally released in V15.0.
 ******************************************************************************/
extern UFUNEXPORT int UF_GDT_ask_tol_feat_tag(
tag_t tolerance ,/* <I>
                 Tolerance type to inquire
                 */
tag_t * tolerance_feature  /* <O>
                           Tolerance feature identifier of the queried
                           tolerance
                           */
);

/******************************************************************************
Returns the tag of the tolerance feature associated with a given
tolerance feature instance.

Environment: Internal  and  External
See Also:
History:Original release was in 14.0.
 ******************************************************************************/
extern UFUNEXPORT int UF_GDT_ask_tol_feat_of_instance(
tag_t feature_instance ,/* <I>
                        Tolerance Feature instance to inquire
                        */
tag_t * tolerance_feature  /* <O>
                           Identifier of the tolerance feature
                           referenced by the instance
                           */
);

/******************************************************************************
 Interrogates the unit basis data off of a tolerance feature

 Return:
 Return Codes -
        UF_GDT_NO_ERRORS
        UF_GDT_ERR_NOT_FCF
        UF_err_program_not_initialized

 Environment:Internal and External
 See Also:
 History:
 *****************************************************************************/
extern UFUNEXPORT int UF_GDT_ask_unit_basis(
    tag_t fcf,                          /* <I>
                                        Tag for FCF to interrogate    */
    UF_GDT_modifier_types_p_t modifier, /* <O>
                                        Characteristic type           */
    UF_GDT_unit_basis_p_t data          /* <OF>
                                        Unit basis data for fcf.  This must
                                        be freed by calling UF_free       */
);

/******************************************************************************
 Sets unit basis data for the given fcf

 Return:
 Return Codes -
        UF_GDT_NO_ERRORS
        UF_GDT_null_object
        UF_GDT_invalid_object
        UF_err_program_not_initialized

 Environment:Internal and External
 See also:
 History:
 *****************************************************************************/
extern UFUNEXPORT int UF_GDT_set_unit_basis(
    tag_t fcf,                          /* <I> Tag for FCF to set           */
    UF_GDT_modifier_types_t modifier,   /* <I> Characteristic type          */
    UF_GDT_unit_basis_p_t   data        /* <I> Unit basis data to set       */
);

/******************************************************************************
Allows the calling application to reassociate the set of faces associated
with the tolerance feature or datum feature.  Some tolerance features return
an error if the set of faces is modified (target points, target lines,
centerplanes, etc.)

Environment: Internal  and  External
See Also:
History:Original release was in 14.0.
 ******************************************************************************/
extern UFUNEXPORT int UF_GDT_set_faces(
tag_t tolerance_feature ,/* <I>
                         Tolerance Feature to set
                         */
int num_faces ,/* <I>
               Number of faces in face array
               */
tag_t * faces  /* <I,len:num_faces>
                      Array of faces to associate with the tolerance
                      feature
               */
);

/******************************************************************************
Allows the calling application to set the the type of profile tolerance
and the dimensions of the outer and inner portions of the tolerance
zone for unilateral and unequally disposed bilateral tolerances.
If the profile type is not UF_GDT_PROFILE_UNEQ_BILATERAL,
the outside parameter is ignored.

An error of UF_GDT_ERR_NOT_PROFILE_FCF is returned if the input feature
control frame is not a profile of line or profile of surface callout.

An error of UF_GDT_ERR_INVALID_PROFILE_TOL is returned if the input profile
type is UF_GDT_PROFILE_UNEQ_BILATERAL and outside is not in the
range (0, total_tolerance).

Environment: Internal  and  External
See Also:
History:This function was originally released in V15.0.
 ******************************************************************************/
extern UFUNEXPORT int UF_GDT_set_fcf(
tag_t fcf ,/* <I>
           Feature control frame to set
           */
UF_GDT_fcf_t * fcf_data  /* <I>
                         Feature control frame data to set the tolerance
                         feature with.
                         */
);


/******************************************************************************
Given a feature control frame, this function changes the tolerance
type to the specified characteristic.

Environment: Internal  and  External
See Also:
History:Original release was in 14.0.
 ******************************************************************************/
extern UFUNEXPORT int UF_GDT_set_characteristic(
tag_t fcf ,/* <I>
           Feature control frame to set
           */
UF_GDT_characteristic_t * characteristic  /* <I>
                                          Feature control frame type
                                          */
);

/******************************************************************************
Determines if the feature is a datum feature or a tolerance feature.
Datum features include: target points, target lines, target areas,
centerplanes, and all other datum identifiers. Tolerance features
include those tolerances with feature control frame callouts and
datum features defined with a tolerance.

Environment: Internal  and  External
See Also:
History:Original release was in 14.0.
 ****************************************************************************/
extern UFUNEXPORT int UF_GDT_is_datum(
tag_t tolerance_feature ,/* <I>
                         Tolerance Feature to inquire
                         */
logical * is_datum  /* <O>
                    Status of query
                    */
);

/******************************************************************************
Given a tolerance feature or datum feature, this function determines
if the feature describes a feature of size.

Environment: Internal  and  External
See Also:
History:Original release was in 14.0.
 ******************************************************************************/
extern UFUNEXPORT int UF_GDT_is_feature_of_size(
tag_t tolerance_feature ,/* <I>
                         Tolerance Feature to inquire
                         */
logical * feature_of_size  /* <O>
                           Flag indicating if the feature describes a
                           feature of size.
                           */
);


/******************************************************************************
This function allows the calling program to create a datum Identifier.

Environment: Internal  and  External
See Also:
History:Original release was in 14.0.
 ******************************************************************************/
extern UFUNEXPORT int UF_GDT_create_datum_identifier(
UF_GDT_feature_parms_p_t feat_parms ,/* <I>
                                     Number of identifiers in face list array
                                     */
UF_GDT_datum_identifier_p_t datum_data ,/* <I>
                                        Creation information of tolerance datum
                                        feature
                                        */
tag_p_t datum_feature  /* <O>
                       Identifier of created datum
                       */
);

/******************************************************************************
 This function creates a datum target point with the data specified.

 Return:
    Return Codes -
        UF_GDT_NO_ERRORS
        UF_err_bad_parameter_number_1
        UF_err_program_not_initialized

 Environment: Internal and External
 See Also:
 History:
 *****************************************************************************/
extern UFUNEXPORT int UF_GDT_create_target_point(
    UF_GDT_datum_target_point_p_t target_data,  /* <I>
                                                Target point data
                                                */
    tag_t *point                                /* <O>
                                                Tag of target point
                                                */
);


/******************************************************************************
 This function creates a datum target line with the line data specified.

 Return:
 Return Codes -
        UF_GDT_NO_ERRORS
        UF_err_bad_parameter_number_1
        UF_err_program_not_initialized

 Environment: Internal and External
 See also:
 History:
 *****************************************************************************/
extern UFUNEXPORT int UF_GDT_create_target_line(
    UF_GDT_datum_target_line_p_t target_data,   /* <I>
                                                Target line data
                                                */
    tag_t *target_line                          /* <O>
                                                Tag of target line
                                                */
);


/******************************************************************************
 This function creates a circular (or annular) datum target area with the
 area data specified.

 Return:
 Return Codes -
        UF_GDT_NO_ERRORS
        UF_err_bad_parameter_number_1
        UF_err_program_not_initialized

 Environment: Internal and External
 See also:
 History:
 *****************************************************************************/
extern UFUNEXPORT int UF_GDT_create_target_dia_area(
    UF_GDT_target_dia_area_p_t target_data,     /* <I>
                                                Target area data
                                                */
    tag_t *target_area                          /* <O>
                                                Tag of target area
                                                */
);


/******************************************************************************
 This function creates a rectangular datum target area with the area
 data specified.

 Return:
 Return Codes -
        UF_GDT_NO_ERRORS
        UF_err_bad_parameter_number_1
        UF_err_program_not_initialized

 Environment:Internal and External
 See also:
 History:
 *****************************************************************************/
extern UFUNEXPORT int UF_GDT_create_target_rect_area(
    UF_GDT_target_rect_area_p_t target_data,    /* <I>
                                                Target area data
                                                */
    tag_t *target_area                          /* <O>
                                                Tag of target area
                                                */
);

/******************************************************************************
 This function creates a user defined datum target area with the area
 data specified.

 Return:
 Return Codes -
        UF_GDT_NO_ERRORS
        UF_err_bad_parameter_number_1
        UF_err_program_not_initialized

 Environment:Internal and External
 See also:
 History:
 *****************************************************************************/
extern UFUNEXPORT int UF_GDT_create_target_udef_area(
    UF_GDT_target_udef_area_p_t target_data,    /* <I>
                                                Target area data
                                                */
    tag_t *target_area                          /* <O>
                                                Tag of target area
                                                */
);

/******************************************************************************
Allows the calling program to create a multiple datum.  The "num_faces"
and "face_list" fields in the UF_GDT_feature_parms_s structure should be
set to "0" and "NULL" respectively.

Environment: Internal  and  External
See Also:
History:Original release was in 14.0.
 ******************************************************************************/
extern UFUNEXPORT int UF_GDT_create_datum_multiple(
UF_GDT_feature_parms_p_t feat_parms ,/* <I>
                                     Creation information of tolerance datum
                                     feature
                                     */
UF_GDT_multiple_datum_p_t datum_data ,/* <I>
                                      Datum defining data
                                      */
tag_t * multiple_datum  /* <O>
                        Identifier of created datum
                        */
);

/******************************************************************************
Allows the calling program to create a feature control frame. This
does not create a displayed instance.

Environment: Internal  and  External
See Also:
History: Original release was in 14.0.
 ****************************************************************************/
extern UFUNEXPORT int UF_GDT_create_fcf(
UF_GDT_feature_parms_p_t  feat_parms ,/* <I>
                                      Tolerance feature creation data
                                      */
UF_GDT_fcf_t * tolerance_data ,/* <I>
                               Creation information for the feature
                               control frame
                               */
tag_t * tolerance_feature ,/* <O>
                           Identifier of created tolerance feature
                           */
tag_t * fcf  /* <O>
             Identifier of created FCF
             */
);

/******************************************************************************
Allows the calling program to create an instance of a tolerance
feature. The tolerance feature must be of a displayable type.

Environment: Internal  and  External
See Also:
History:Original release was in 14.0.
 ******************************************************************************/
extern UFUNEXPORT int UF_GDT_create_instance(
UF_GDT_tolerance_type_t type ,/* <I>
                              Type of tolerance feature to create
                              */
tag_t  tolerance_feature ,/* <I>
                          Referenced tolerance feature
                          */
tag_t view ,/* <I>
            Tag of the view where the instance is
            displayed
            */
tag_t edge ,/* <I>
            Solid edge where the leader is located
            */
double origin[3] ,/* <I>
                  Location of instance origin
                  */
double attach_point[3] ,/* <I>
                        Location of attachment point
                        */
tag_t * feature_instance  /* <O>
                          Identification tag of created feature
                          instance
                          */
);

/******************************************************************************
This function allows the calling program to create a size tolerance.
This does not create a displayed instance.

Environment: Internal  and  External
See Also:
History:
 ******************************************************************************/
extern UFUNEXPORT int UF_GDT_create_size_tolerance(
UF_GDT_feature_parms_p_t feat_parms ,/* <I>
                                     Tolerance feature creation data
                                     */
UF_GDT_size_tolerance_p_t size_data ,/* <I>
                                     Creation information for the size tolerance
                                     */
tag_t * size_tolerance  /* <O>
                        Identifier of created size tolerance
                        */
);

/******************************************************************************
Frees the memory allocated by the GDT module for its various data
structures.

Environment: Internal  and  External
See Also:
History:Original release was in 14.0.
 ******************************************************************************/
extern UFUNEXPORT int UF_GDT_free(
UF_GDT_data_type_t  type ,/* <I>
                          The type of data structure to free
                          */
void * data  /* <I>
             Pointer to a data structure
             */
);

/******************************************************************************
Returns the datum label associated with a tolerance datum feature.

The input tag object could be a tolerance feature or a datum object.
If it is a tolerance feature, it works the same way as before except
that if the tolerance feature refers to more than one datum, an error
called UF_GDT_ERR_FEAT_NOT_VALID will returned. If it is a datum object,
it will return the information about this datum.

Return Codes -
       UF_GDT_NO_ERRORS
       UF_GDT_ERR_NOT_BASE
       UF_GDT_ERR_FEAT_NOT_VALID
       UF_err_program_not_initialized

Environment: Internal  and  External
See Also:
History:Original release was in 14.0, modified in v18.0
 ******************************************************************************/
extern UFUNEXPORT int UF_GDT_ask_label_of_datum(
tag_t base ,/* <I>
                     Tolerance Datum Feature or datum object to inquire
                     */
char ** datum_label  /* <OF>
                     Label associated with tolerance datum/multiple
                     datum feature. Use UF_free to deallocate memory
                     when done.
                     */
);

/******************************************************************************
Edits the parameters of a datum identifier.  If the user specifies a "NULL"
for the datum data, the current datum information will be removed from the
tolerance feature.  In this case a size tolerance or a feature control frame
must still be part of the tolerance feature.

The input tag object could be a tolerance feature or a datum object.
If it is a tolerance feature, it works the same way as before except that if the
tolerance feature refers to more than one datum, an error called UF_GDT_ERR_FEAT_NOT_VALID
will returned. If it is a datum object, it will set the information about this datum.

Return Codes -
       UF_GDT_NO_ERRORS
       UF_err_program_not_initialized
       UF_GDT_ERR_FEAT_NOT_VALID
       UF_GDT_ERR_NULL_LABEL
       UF_GDT_ERR_NOT_BASE


Environment: Internal  and  External
See Also:
History:Original release was in 14.0. Modified in v18.0
 *****************************************************************************/
extern UFUNEXPORT int UF_GDT_set_datum_identifier(
tag_t base ,        /* <I> Either a tolerance feature or a datum object, if
                            it is a tolerance feature and the tolerance feature
                            refers to more than one datums, an error will returned.
                            */
UF_GDT_datum_identifier_t * datum_data  /* <I>
                                        Information to be edited
                                        */
);

/******************************************************************************
This function changes the label for a datum feature.  The label must be unique
in the context of the part file. Duplicate labels are not permitted.
The characters defining the label must be in the set of valid
characters as defined in the customer defaults file.

The input tag object could be a tolerance feature or a datum object.
If it is a tolerance feature, it works the same way as before except that if the
tolerance feature refers to more than one datum, an error called
UF_GDT_ERR_FEAT_NOT_VALID will returned. If it is a datum object,
it will set the information about this datum.

Return Codes -
       UF_GDT_NO_ERRORS
       UF_GDT_ERR_NOT_BASE
       UF_GDT_ERR_FEAT_NOT_VALID
       UF_err_program_not_initialized

Environment: Internal  and  External
See Also:
History:Original release was in 14.0, modified in release v18.0
 *****************************************************************************/
extern UFUNEXPORT int UF_GDT_set_datum_label(
tag_t           base,           /* <I>
                                    Tolerance datum feature or datum object to set
                                */
const char *    datum_label     /* <I>
                                    New label for datum feature
                                */
);

/******************************************************************************
This function edits the parameters of a multiple datum.

Note: The input tag could be a multiple datum feature or a multiple datum
      object.

Return Codes -
     UF_GDT_NO_ERRORS
     UF_GDT_ERR_NOT_BASE
    UF_err_program_not_initialized

Environment: Internal  and  External
See Also:
History: Original release was in 14.0, modified in release v18.0.
 ******************************************************************************/
extern UFUNEXPORT int UF_GDT_set_datum_multiple(
tag_t multiple_datum ,/* <I>
                      Multiple datum  to set
                      */
UF_GDT_multiple_datum_t * datum_data  /* <I>
                                      Information to be edited
                                      */
);

/******************************************************************************
Sets the datum references of a given frame for the specified feature
control frame.

Environment: Internal  and  External
See Also:
History: Original release was in 14.0.
 ******************************************************************************/
extern UFUNEXPORT int UF_GDT_set_datum_references(
tag_t fcf ,/* <I>
           Feature control frame to edit
           */
int nth_frame ,/* <I>
               FCF data frame to set
               */
int  num_frames ,/* <I>
                 Number of datum references in array
                 */
UF_GDT_datum_reference_t * datum_reference  /* <I>
                                            Primary datum reference of feature
                                            control frame
                                            */
);

/******************************************************************************
This function returns the tolerance feature description and name
information to the calling application.

Environment: Internal  and  External
See Also:
History:Original release was in 14.0.
 ******************************************************************************/
extern UFUNEXPORT int UF_GDT_ask_description(
tag_t tolerance_feature ,/* <I>
                         Tolerance Feature to inquire
                         */
UF_GDT_description_p_t * info  /* <OF,free:UF_GDT_free>
                               Description associated with tolerance feature or
                               tolerance datum feature.  This must be freed
                               by calling UF_GDT_free.
                               */
);

/******************************************************************************
Allows the user to change the name of a datum feature or tolerance
feature and assign a new description. If a field of the
UF_GDT_description_t structure is null that field is not updated.

Environment: Internal  and  External
See Also:
History: Original release was in 14.0.
 *****************************************************************************/
extern UFUNEXPORT int UF_GDT_set_description(
tag_t tolerance_feature ,/* <I>
                         Tolerance Feature to inquire
                         */
UF_GDT_description_t * info  /* <I>
                             Design information to associated with the
                             feature
                             */
);

/******************************************************************************
This function returns all displayed instances created from the
tolerance feature. 0..n instances may be returned.

Environment: Internal  and  External
See Also:
History:Original release was in 14.0
 ******************************************************************************/
extern UFUNEXPORT int UF_GDT_ask_tol_feat_instance(
tag_t tolerance_feature ,/* <I>
                         Tolerance Feature to inquire
                         */
int * num_instances ,/* <O>
                     Number of instances returned in above
                     array.
                     */
tag_p_t * feature_instances  /* <OF,len:num_instances>
                             Array of tags of all instances created from
                             the tolerance feature. Use UF_free to
                             deallocate memory when done.
                             */
);

/******************************************************************************
This routine returns the tolerance feature creation parameters, given
any tolerance feature.

Environment: Internal  and  External
See Also:
History:Original release was in 14.0.
 *****************************************************************************/
extern UFUNEXPORT int UF_GDT_ask_feature_parms(
tag_t tolerance_feature ,/* <I>
                         Tolerance Feature to inquire
                         */
UF_GDT_feature_parms_p_t * feat_parms  /* <OF,free:UF_GDT_free>
                                       Tolerance feature creation parameters.
                                       UF_GDT_free must be used to free the
                                       space allocated for this argument.
                                       */
);

/******************************************************************************
Allows the calling program to query the size tolerance information
(nominal value, +/- tolerance values, etc.) for a given tolerance
feature.

Environment: Internal  and  External
See Also:
History:Original release was in 14.0.
 ******************************************************************************/
extern UFUNEXPORT int UF_GDT_ask_size_tolerance_parms(
tag_t tolerance_feature ,/* <I>
                         Tolerance feature to inquire
                         */
UF_GDT_size_tolerance_p_t * size_data  /* <OF,free:UF_GDT_free>
                                       Information on the size tolerance.  The
                                       data allocated for this structure must
                                       be freed by calling UF_GDT_free.
                                       */
);


/******************************************************************************
This routine allows the calling program to query the limits and fits
tolerance information for a given tolerance feature.

Return Codes -
       UF_GDT_NO_ERRORS
       UF_GDT_ERR_NOT_TOL_FEAT
       UF_err_program_not_initialized
       UF_GDT_ERR_NO_LIMITS_AND_FITS_TOLERANCE

Environment: Internal  and  External
See Also:
History:Original release was in 18.0.
 *****************************************************************************/
extern UFUNEXPORT int UF_GDT_ask_limits_and_fits_tolerance_parms(
     tag_t tolerance_feature ,/* <I> Tolerance feature to inquire */
     UF_GDT_limits_and_fits_tolerance_p_t *data  /* <OF,free:UF_GDT_free>
                                                    Information on the limits
                                                   and fits tolerance.  The data
                                                   allocated for this structure must
                                                   be freed by calling UF_GDT_free.
                                                */
);

/******************************************************************************
Returns the identifier of the dimension which defines a size tolerance
for a given tolerance feature.  Any calls to this routine will only return
NULL_TAG.  To query size data please use UF_GDT_ask_size_tolerance_parms.
To query the appended text on a size tolerance please use
UF_GDT_ask_appended_text with the tolerance feature tag as parameter 1.

Environment: Internal  and  External
See Also:
History: Original release was in 14.0.
         Modified in V16 to always return a NULL_TAG
 ******************************************************************************/
extern UFUNEXPORT int UF_GDT_ask_size_tolerance_tag(
tag_t tolerance_feature ,/* <I>
                         Tolerance feature to inquire
                         */
tag_t * size_tolerance  /* <O>
                        Identifier of size tolerance
                        */
);

/******************************************************************************
Returns an array of tolerance attributes which compose the given
tolerance feature.

Environment: Internal  and  External
See Also:
History:Original release was in 14.0.
 ******************************************************************************/
extern UFUNEXPORT int UF_GDT_ask_tolerance_types(
tag_t tolerance_feature ,/* <I>
                         Tolerance feature to inquire
                         */
int * num_types ,/* <O>
                 Number of types in types array
                 */
UF_GDT_tolerance_type_p_t * types  /* <OF,len:num_types>
                                   Pointer to an array of tolerance types. Use
                                   UF_free to deallocate memory when done.
                                   */
);

/******************************************************************************
This routine returns the defining data for a given single feature
control frame. Characteristic, Tolerance Zone, and Datum Reference
information is returned for each frame in the array.

Environment: Internal  and  External
See Also:
History:Original release was in 14.0.
 ******************************************************************************/
extern UFUNEXPORT int UF_GDT_ask_fcf_parms(
tag_t fcf ,/* <I>
           Feature control frame to inquire
           */
UF_GDT_fcf_p_t * fcf_data  /* <OF,free:UF_GDT_free>
                           Feature control frame data.  This should be freed
                           by calling UF_GDT_free.
                           */
);

/******************************************************************************
This function returns the tags of the feature control frames that
reference a given tolerance feature. The feature control frames are
listed in the array in the order that they appear in their feature control
frame.

In the case of multiple feature control frames the the first
(topmost) frame is returned in the first element of the "fcfs" array.
The second in the second element etc.

Environment: Internal  and  External
See Also:
History:Original release was in 14.0.
 *****************************************************************************/
extern UFUNEXPORT int UF_GDT_ask_fcf_tags(
tag_t tolerance_feature ,/* <I>
                         Tolerance Feature to inquire
                         */
int * num_fcfs ,/* <O>
                Number of feature control frames in array
                */
tag_p_t * fcfs  /* <OF,len:num_fcfs>
                Array of tags of the feature control frame
                identifiers associated with tolerance feature. Use
                UF_free to deallocate memory when done.
                */
);

/******************************************************************************
Given a tolerance feature or datum feature, this function determines
the exact type of feature and return it to the caller.

Environment: Internal  and  External
See Also:
History:Original release was in 14.0.
 ******************************************************************************/
extern UFUNEXPORT int UF_GDT_ask_feature_type(
tag_t tolerance_feature ,/* <I>
                         Tolerance Feature to inquire
                         */
UF_GDT_feature_type_t * feature  /* <O>
                                 Feature type of tolerance feature.
                                 */
);

/******************************************************************************
Given a feature control frame, this function determines if the feature
control frame is a composite tolerance.  This function does not return a
true value for a non-composite tolerance composite feature control frame.

Environment: Internal  and  External
See Also:
History:Original release was in 14.0.
 ******************************************************************************/
extern UFUNEXPORT int UF_GDT_is_composite_tolerance(
tag_t fcf ,/* <I>
           Feature control frame to inquire
           */
logical * is_composite_tol  /* <O>
                            Result of query
                            */
);

/******************************************************************************
Given a feature control frame, this function returns the feature
control frame's tolerance characteristic.

Environment: Internal  and  External
See Also:
History:Original release was in 14.0.
 ******************************************************************************/
extern UFUNEXPORT int UF_GDT_ask_characteristic(
tag_t fcf ,/* <I>
           Feature control frame to inquire
           */
UF_GDT_characteristic_t * characteristic  /* <O>
                                          Result of query
                                          */
);

/******************************************************************************
Returns the standard that is in effect in the current drawing.

Environment: Internal  and  External
See Also:
History:Original release was in 14.0.
 ******************************************************************************/
extern UFUNEXPORT int UF_GDT_ask_tolerancing_standard(
UF_GDT_standard_t * standard  /* <O>
                              Current engineering standard used for
                              tolerancing
                              */
);

/******************************************************************************
Returns the information concerning the entire tolerance zone
associated with a feature control frame.

Environment: Internal  and  External
See Also:
History:Original release was in 14.0.
 ******************************************************************************/
extern UFUNEXPORT int UF_GDT_ask_tolerance_zone(
tag_t fcf ,/* <I>
           Feature control frame to inquire
           */
int  nth_zone ,/* <O>
               Tolerance zone frame to query
               */
UF_GDT_tolerance_zone_p_t * zone ,/* <OF,free:UF_GDT_free>
                                  Pointer to tolerance zone data. Use
                                  UF_GDT_free to deallocate memory
                                  when done.
                                  */
UF_GDT_modifier_data_p_t * frame_mod /* <OF,free:UF_GDT_free>
                                     Modifier information for the tolerance
                                     zone. UF_GDT_free to deallocate
                                     memory when done.
                                     */
);

/******************************************************************************
This function returns information on a specified datum identifier.

The input tag object could be a tolerance feature or a datum object.
If it is a tolerance feature, it works the same way as before except that if the
tolerance feature refers to more than one datum, an error called
UF_GDT_ERR_FEAT_NOT_VALID will returned. If it is a datum object, it will
return the information about this datum.

Return Codes -
       UF_GDT_NO_ERRORS
       UF_err_program_not_initialized
       UF_GDT_ERR_NOT_BASE
       UF_GDT_ERR_FEAT_NOT_VALID
       UF_GDT_ERR_NOT_IDENT_DATUM

Environment: Internal  and  External
See Also:
History:Original release was in 14.0, modified in release v18.0.
 ******************************************************************************/
extern UFUNEXPORT int UF_GDT_ask_datum_ident_parms(
tag_t  base ,/* <I>Datum feature or datm object */
UF_GDT_datum_identifier_p_t * datum_data  /* <OF,free:UF_GDT_free>
                                          Returned data concerning the datum
                                          identifier. Use UF_GDT_free to
                                          deallocate memory when done.
                                          */
);

/******************************************************************************
 This routine returns the information which defines a datum target point.

 Return:
  Return Codes -
        UF_GDT_NO_ERRORS
        UF_GDT_ERR_NOT_TOL_FEAT
        UF_err_program_not_initialized

 Environment: Internal and External
 See Also:
 History:
 *****************************************************************************/
extern UFUNEXPORT int UF_GDT_ask_target_point_parms(
    tag_t target,                         /* <I>
                                          Datum target tag */
    UF_GDT_datum_target_point_p_t *data   /* <OF,free:UF_GDT_free>
                                          Target point data.  Use UF_GDT_free
                                          to deallocate the memory allocated.
                                          */
);


/******************************************************************************
 This routine returns the information which defines a datum target line.

 Return:
  Return Codes -
        UF_GDT_NO_ERRORS
        UF_GDT_ERR_NOT_TOL_FEAT
        UF_err_program_not_initialized

 Environment:Internal and External
 See Also:
 History:
 *****************************************************************************/
extern UFUNEXPORT int UF_GDT_ask_target_line_parms(
    tag_t target,                         /* <I>
                                          Datum target tag
                                          */
    UF_GDT_datum_target_line_p_t *data    /* <OF,free:UF_GDT_free>
                                          Target line data.  Use UF_GDT_free
                                          to deallocated the memory when done.
                                          */
);


/******************************************************************************
 This routine returns the information which defines a circular datum
 target area.

 Return:
  Return Codes -
        UF_GDT_NO_ERRORS
        UF_GDT_ERR_NOT_TOL_FEAT
        UF_err_program_not_initialized

 Environment: Internal and External
 See Also:
 History:
 *****************************************************************************/
extern UFUNEXPORT int UF_GDT_ask_target_dia_parms(
    tag_t target,                         /* <I>
                                          Datum target tag
                                          */
    UF_GDT_target_dia_area_p_t *data      /* <OF,free:UF_GDT_free>
                                          Circular area data.  Use UF_GDT_free
                                          to deallocate the memory when done.
                                          */
);


/******************************************************************************
 This routine returns the information which defines a rectangular datum
 target area.
 Return:
  Return Codes -
        UF_GDT_NO_ERRORS
        UF_GDT_ERR_NOT_TOL_FEAT
        UF_err_program_not_initialized

 Environment : Internal and External
 See Also:
 History:
 *****************************************************************************/
extern UFUNEXPORT int UF_GDT_ask_target_rect_parms(
    tag_t target,                        /* <I>
                                         Datum target tag
                                         */
    UF_GDT_target_rect_area_p_t *data    /* <OF,free:UF_GDT_free>
                                         Rectangular area data.  Use UF_GDT_free
                                         to free the memory when done.
                                         */
);

/******************************************************************************
 This routine returns the information which defines a user defined datum
 target area.
 Return:
  Return Codes -
        UF_GDT_NO_ERRORS
        UF_GDT_ERR_NOT_TOL_FEAT
        UF_err_program_not_initialized

 Environment : Internal and External
 See Also:
 History:
 *****************************************************************************/
extern UFUNEXPORT int UF_GDT_ask_target_udef_parms(
    tag_t target,                         /* <I>
                                          Datum target tag
                                          */
    UF_GDT_target_udef_area_p_t *data     /* <OF,free:UF_GDT_free>
                                          User defined area data.  Use UF_GDT_free
                                          to free the memory when done
                                          */
);

/******************************************************************************
This function returns information on a specified multiple datum.

Environment: Internal  and  External
See Also:
History:Original release was in 14.0.
 *****************************************************************************/
extern UFUNEXPORT int UF_GDT_ask_datum_multiple_parms(
tag_t multiple_datum ,/* <I>
                      Identifier of multiple datum queried
                      */
UF_GDT_multiple_datum_p_t * datum_data  /* <OF,free:UF_GDT_free>
                                        Returned data concerning the multiple
                                        datum. Use UF_GDT_free to deallocate
                                        memory when done.
                                        */
);

/******************************************************************************
This function returns the identifier of the datum referred to by a
datum label.

Environment: Internal  and  External
See Also:
History:Original release was in 14.0.
*******************************************************************************/
extern UFUNEXPORT int UF_GDT_ask_datum_of_label(
const char *    datum_label,    /* <I>
                                    Datum label string to inquire
                                */
tag_t *         datum_feature   /* <O>
                                    Identifier of datum referenced by label
                                */
);

/******************************************************************************
The following function returns the datum references of the given data
frame in a given feature control frame.  The number frames is only greater
than one in the case of a composite tolerance. A non-composite tolerance
composite frame has only one frame.

Environment: Internal  and  External
See Also:
History:Original release was in 14.0.
*******************************************************************************/
extern UFUNEXPORT int UF_GDT_ask_datum_references(
tag_t fcf ,/* <I>
           Feature control frame to inquire
           */
int nth_frame ,/* <I>
               The frame in the feature control
               frame to query
               */
int * num_refs ,/* <O>
                Number of datum references
                returned
                */
UF_GDT_datum_reference_p_t ** datum_reference  /* <OF,len:num_refs>
                                               Function_to_free = UF_GDT_free
                                               Datum references for the feature
                                               control frame. Use UF_GDT_free
                                               to deallocate memory when done.
                                               */
);

/******************************************************************************
Get the feature control frames that reference the datum.

Note: The input could be a datum feature or a datum object.

Return Codes -
    UF_GDT_NO_ERRORS
    UF_GDT_ERR_NOT_TOL_FEAT
    UF_GDT_ERR_FEATURE_NOT_DATUM
    UF_err_program_not_initialized
    UF_GDT_ERR_NOT_BASE

Environment: Internal  and  External

See Also:

History:Original release was in V16.0
 *****************************************************************************/
extern UFUNEXPORT int UF_GDT_ask_datum_referencers(
    tag_t    base,             /* <I>  Datum feature or datum object to query  */
    int     *num_fcfs,          /* <O>  Number of feature control frames
                                        referencing the datum            */
    tag_p_t *fcfs               /* <OF,len:num_fcfs> List of feature control frames
                                        referencing the datum.  This should
                                        be freed with UF_free.           */
);

/******************************************************************************
Given a tolerance feature or datum feature, this function allows for
the resetting of the size tolerance parameters.

Environment: Internal  and  External
See Also:
History:Original release was in 14.0.
 *****************************************************************************/
extern UFUNEXPORT int UF_GDT_set_size_tolerance_parms(
tag_t tolerance_feature ,/* <I>
                         Tolerance Feature to set
                         */
UF_GDT_size_tolerance_t * size_data  /* <I>
                                     Data to be applied to tolerance feature.
                                     */
);

/******************************************************************************
Given a tolerance feature or datum feature, this function allows for
the resetting of the limits and fits tolerance parameters.

Return Codes -
       UF_GDT_NO_ERRORS
       UF_GDT_ERR_NOT_TOL_FEAT
       UF_err_program_not_initialized
       UF_GDT_ERR_NOT_VALID_FEAT_TYPE_FOR_LIM_FITS
       UF_GDT_ERR_NOT_VALID_FEAT_TYPE_FOR_LIM_FITS_ENGLISH
       UF_GDT_ERR_NOT_VALID_DATA_FOR_PART_UNIT
       UF_GDT_ERR_INVALID_LIM_FITS_DATA
       UF_GDT_ERR_INCH_PART_WITH_ISO_STANDARD
       UF_GDT_ERR_UNVAILABLE_DATA_FOR_CURRENT_SETTING

Environment: Internal  and  External
See Also:
History:Original release was in 18.0.
*****************************************************************************/
extern UFUNEXPORT int UF_GDT_set_limits_and_fits_tolerance_parms(
     tag_t tolerance_feature ,/* <I> Tolerance Feature to set */
     UF_GDT_limits_and_fits_data_p_t  data  /* <I> Data to be applied to
                                                       tolerance feature. */
);

/****************************************************************************
Queries if the given tolerance feature has a limits and fits tolerance.

Environment: Internal and External
See Also:
History: Originally released in V18.0
****************************************************************************/
extern UFUNEXPORT int UF_GDT_has_limits_and_fits_tolerance(
      tag_t tolerance_feature,          /* <I> Tolerance feature tag */
      logical *has_limits_and_fits_tolerance     /* <O>
                                             TRUE if the tolerance feature has a
                                             limits and fits tolerance.
                                             */
);


/******************************************************************************
 This function edits the tolerance zone of a given feature control
 frame.

 Return:
  Return Codes -
        UF_GDT_NO_ERRORS
        UF_GDT_ERR_NOT_FCF
        UF_err_program_not_initialized

 Environment: Internal  and  External
 See Also:
 History:
 *****************************************************************************/
extern UFUNEXPORT int UF_GDT_set_tolerance_zones(
    tag_t                  fcf, /* <I>
                                        FCF to set
                                        */
    int                  num_zones, /* <I>
                                        Number of zones to set
                                        */
    UF_GDT_tolerance_zone_p_t    zones, /* <I,len:num_zones>
                                        Tolerance zone data to set
                                        */
    UF_GDT_modifier_data_p_t  mod_data  /* <I>
                                        Modifier data to set
                                        */
);

/******************************************************************************
This function allows the user to change the value of the tolerancing standard
used by the GDT Module.  The standard can only be set if there are no
tolerance features created on the part.

Environment: Internal  and  External
See Also:
History:Original release was in 14.0.
 ******************************************************************************/
extern UFUNEXPORT int UF_GDT_set_tolerancing_standard(
UF_GDT_standard_t standard  /* <I>
                            Desired engineering standard used for
                            tolerancing
                            */
);

/******************************************************************************
Allows an "old" style Geometric Tolerancing symbol or feature to be upgraded
to be included in the new tolerancing module.  If the "old" symbol or feature
is inconsistent with the current model, the feature may be created in a
retained state.  Retained annotations cannot be upgraded.


Environment: Internal  and  External
See Also:
History:Original release was in 14.0.
 ******************************************************************************/
extern UFUNEXPORT int UF_GDT_upgrade_legacy_feature(
int num_annot ,/* <I>
               Number of annotations to be upgraded
               */
tag_t * annotation_features ,/* <I,len:num_annot>
                                    Identifier of the set of old dimensions and
                                    symbols that get converted
                             */
int  num_faces ,/* <I>
                Number of identifiers in face list array
                */
tag_t * face_list ,/* <I,len:num_faces>
                          Array of identifiers that define the face_list
                          of the tolerance feature
                   */
UF_GDT_feature_type_t feature ,/* <I>
                               Feature type of the tolerance feature
                               */
double origin[3] ,/* <I>
                  Origin of tolerance feature instance
                  */
UF_GDT_description_t *  descript ,/* <I>
                                  Description of the noew tolerance feature
                                  */
tag_t * tolerance_feature  /* <O>
                           Identifier of upgraded feature
                           */
);

/******************************************************************************
 Sets the profile type and outside zone for a profile of line or profile
 of surface tolerance.  The outside zone is only used when the profile type
 is set to UF_GDT_PROFILE_UNEQ_BILATERAL.

 Return:
  Return Codes -
        UF_GDT_NO_ERRORS
        UF_GDT_INVALID_OBJECT          (object is not an fcf)
        UF_GDT_NOT_PROFILE_FCF         (fcf does not contain a profile of
                                        surface or profile of line
                                        characteristic)
        UF_GDT_INVALID_PROFILE_ZON     (if profile type = UF_GDT_UNEQ_BILATERAL
                                        and outside does not follow the rule
                                        0.0 < outside < total_tolerance
                                                           - ASME Y14.5M 1994)
        UF_GDT_INVALID_PROFILE_TOL     (if profile type is not supported for
                                        current standard or feature)
        UF_err_program_not_initialized

 Environment: Internal and External
 See Also:
 History:
 *****************************************************************************/
extern UFUNEXPORT int UF_GDT_set_profile_tol_data(
    tag_t                      fcf,          /* <I>
                                             profile feature control frame to
                                             modify
                                             */
    UF_GDT_profile_type_t      profile_type, /* <I>
                                             profile type
                                             */
    UF_GDT_tolerance_value_p_t outside       /* <I>
                                            outside tolerance zone when type
                                                    is UF_GDT_UNEQ_BILATERAL
                                            */
);

/******************************************************************************
 Queries the profile type and outside zone for a profile of line or profile
 of surface tolerance.  The outside zone is only meaningful if the profile
 type returned is UF_GDT_PROFILE_UNEQ_BILATERAL.

 The outside value may indicate that the rule for the profile type
 UF_GDT_UNEQ_BILATERAL ( 0.0 < outside < total_tolerance) has
 been violated.  In this case the tolerance feature of the
 fcf will be retained.

 Return:
  Return Codes -
        UF_GDT_NO_ERRORS
        UF_GDT_INVALID_OBJECT          (object is not an fcf)
        UF_GDT_NOT_PROFILE_FCF         (fcf does not contain a profile of
                                        surface or profile of line
                                        characteristic)
        UF_err_program_not_initialized

 Environment: Internal and External
 See Also:
 History:
 *****************************************************************************/
extern UFUNEXPORT int UF_GDT_ask_profile_tol_data(
    tag_t                      fcf,          /* <I>
                                             profile feature control frame to
                                             modify
                                             */
    UF_GDT_profile_type_p_t    profile_type, /* <O>
                                             profile type
                                             */
    UF_GDT_tolerance_value_p_t outside       /* <O>
                                             outside tolerance zone when type
                                                    is UF_GDT_UNEQ_BILATERAL
                                             */
);


/****************************************************************************
 Return the component part from which a tolerance (fcf or size tolerance)
 was pulled.  If the tolerance feature input into this routine has no
 tolerance or size data, or the tolerance is not a pulled tolerance,
 an error will be returned.

 Return:
  Return Codes -
        UF_GDT_NO_ERRORS
        UF_GDT_ERR_NOT_SUBTOLERANCE
        UF_GDT_ERR_NOT_PULLED_SUBTOLERANCE
        UF_err_program_not_initialized

 Environment: Internal and External

 See Also:

 History: Originally released in V16.0
 ****************************************************************************/
extern UFUNEXPORT int UF_GDT_ask_pulled_tolerance_component(
    tag_t tolerance,      /* <I>
                       This can either be a tolerance feature or fcf tag that
                       is a pulled tolerance.
                       */
    tag_t *component_part_occ /* <O>
                       Part occurrence from which the given tolerance was
                       pulled.
                       */
);


/****************************************************************************
 Return the unique index number of a tolerance (fcf or size tolerance)
 in the component part file that it was pulled from.  If the tolerance
 feature input into this routine has no tolerance or size data, or the
 tolerance is not a pulled tolerance, an error will be returned.

 Return:
  Return Codes -
        UF_GDT_NO_ERRORS
        UF_GDT_ERR_NOT_TOLERANCE
        UF_GDT_ERR_NO_SIZE_DATA_ON_FEATURE
        UF_GDT_ERR_NOT_PULLED_SUBTOLERANCE
        UF_err_program_not_initialized

 Environment: Internal and External

 See Also:

 History: Originally released in V16.0
 ****************************************************************************/
extern UFUNEXPORT int UF_GDT_ask_component_tolerance_index(
    tag_t tolerance,   /* <I>
                       This can either be a tolerance feature or fcf tag that
                       is a pulled tolerance.
                       */
    int *index         /* <O>
                       Unique index for the tolerance that the given tag was
                       pulled from.
                       */
);


/****************************************************************************
 Determines if the tolerance feature being queried has been pulled from a
 component part.

 Return:
  Return Codes -
        UF_GDT_NO_ERRORS
        UF_GDT_INVALID_OBJECT          (object is not a tolerance feature)
        UF_err_program_not_initialized

 Environment: Internal and External
 See Also:
 History:
 ****************************************************************************/
extern UFUNEXPORT int UF_GDT_is_pulled_tolerance(
    tag_t tolerance_feature,      /* <I>
                                  Tolerance feature to query
                                  */
    logical *status               /* <O>
                                  Status of query
                                  */
);


/****************************************************************************
 Pull a tolerance feature up the assembly.  This function assumes the current
 work part is the part of the assembly and the tolerance feature specified
 resides in a component of that assembly.  A tolerance feature can only be
 pulled from a component of the current assembly.

 Return:
  Return Codes -
        UF_GDT_NO_ERRORS
        UF_GDT_ERR_DWG_DISPLAYED       (can't create instances on drawings)
        UF_GDT_INVALID_OBJECT          (object is not a tolerance feature)
        UF_GDT_ERR_INVALID_INSTANCE    (invalid instance specified)
        UF_err_program_not_initialized

 Environment: Internal and External
 See Also:
 History:
 ****************************************************************************/
extern UFUNEXPORT int UF_GDT_pull_tolerance(
    tag_t tolerance_feature, /* <I>
                             Tag of the tolerance feature in the component.
                             */
    tag_t instance,          /* <I>
                             Tag of the component where the tolerance feature
                             resides.
                             */
    tag_t *new_feature_tag,  /* <O>
                             Tag of the pulled feature created at the assembly
                             level.
                             */
    logical create_instance  /* <I>
                             If TRUE, an instance of the tolerance feature will
                             be created at the assembly level.
                             */
);


/****************************************************************************
 Break a master model relationship between an assembly part and a component
part.  The following relation types are currently supported:

 UF_GDT_PULL_RELATION_TYPE: If this type is specified, the tolerance
 feature at the assembly level must be supplied as input.  After
 the operation, the assembly level feature will no longer be
 dependent on the component tolerance.

 Return:
  Return Codes -
        UF_GDT_NO_ERRORS
        UF_GDT_INVALID_OBJECT          (object is not a tolerance feature)
        UF_GDT_FEATURE_NOT_PULLED      (attempt to break pull relation on a
                                        non-pulled feature)
        UF_err_program_not_initialized

 Environment: Internal and External
 See Also:
 History:
 ****************************************************************************/
extern UFUNEXPORT int UF_GDT_break_relationship(
    tag_t                  tolerance_feature, /* <I>
                                              Tolerance feature to convert
                                              from an assembly tolerance to a
                                              component level tolerance.
                                              */
    UF_GDT_relation_type_t relationship_type /* <I>
                                             Type of relationship to break.
                                             Possible values are:
                                                 UF_GDT_PULL_RELATION_TYPE
                                             */
);


/****************************************************************************
 Set the "auto load component" flag for the current NX work part.  This flag
 controls whether component parts should be automatically loaded when entering
 the tolerancing module.

 Return:
  Return Codes -
        UF_GDT_NO_ERRORS
        UF_err_program_not_initialized

 Environment: Internal and External
 See Also:
 History:
 ****************************************************************************/
extern UFUNEXPORT int UF_GDT_set_load_component_flag(
    logical flag /* <I>
                 If set to TRUE then component parts will be automatically
                 loaded when entering the tolerancing module.
                 */
);


/****************************************************************************
 Query the "auto load component" flag for the current
 NX work part.  This flag control whether component parts should be
 automatically loaded when entering the tolerancing module.

 Return:
  Return Codes -
        UF_GDT_NO_ERRORS
        UF_err_program_not_initialized

 Environment: Internal and External
 See Also:
 History:
 ****************************************************************************/
extern UFUNEXPORT int UF_GDT_ask_load_component_flag(
    logical *flag /* <O>
                  Current status of the load component flag.
                  TRUE = Load component flag is set.
                  */
);


/****************************************************************************
 Determines if the tolerance feature specified is currently retained.

 Return:
  Return Codes -
        UF_GDT_NO_ERRORS
        UF_err_program_not_initialized

 Environment: Internal and External
 See Also:
 History:
 ****************************************************************************/
extern UFUNEXPORT int UF_GDT_is_retained(
    tag_t tolerance_feature, /* <I>
                             Tag of the tolerance feature to query.
                             */
    logical *is_retained     /* <O>
                             Flag indicating whether the specified tolerance
                             feature is currently retained.
                             */
);

/****************************************************************************
 Check whether or not the keyword specified in the input part is a standard
 keyword.  If the keyword does not exist in the part then an error will
 be returned.

  Return Codes -
        UF_GDT_NO_ERRORS
        UF_err_program_not_initialized

 Environment: Internal and External

 See Also:

 History: Originally released in V16.0
 ****************************************************************************/
extern UFUNEXPORT int UF_GDT_is_user_defined_keyword(
    tag_t               part_tag,   /* <I>
                          Part to query
                          */
    UF_GDT_keyword_id_t keyword_id, /* <I>
                          Keyword to check if it is a user defined keyword
                          */
    logical            *status      /* <O>
                          TRUE if the keyword is user defined
                          FALSE if the keyword is a standard keyword
                          */
);

/****************************************************************************
 Return the name currently associated with the keyword specified in the input
 part.  If the keyword does not exist in the part then an error will
 be returned.

  Return Codes -
        UF_GDT_NO_ERRORS
        UF_err_bad_parameter_number_1
        UF_err_program_not_initialized

 Environment: Internal and External

 See Also:

 History: Originally released in V16.0
 ****************************************************************************/
extern UFUNEXPORT int UF_GDT_ask_keyword_name(
    tag_t               part_tag,     /* <I>
                          Part to query
                          */
    UF_GDT_keyword_id_t keyword_id,   /* <I>
                          Keyword whose name is requested
                          */
    char              **keyword_name  /* <OF>
                          Name corresponding to keyword.  This must be
                          freed by calling UF_free.
                          */
);

/****************************************************************************
 Return the text currently associated with the keyword specified in the input
 part.

 Return:
  Return Codes -
        UF_GDT_NO_ERRORS
        UF_err_program_not_initialized

 Environment: Internal and External
 See Also:
 History:
 ****************************************************************************/
extern UFUNEXPORT int UF_GDT_ask_keyword_text(
    tag_t           part_tag,       /* <I>
                                        Part to query
                                    */
    const char *    keyword_name,   /* <I>
                                        Keyword whose text is requested
                                    */
    char **         keyword_text    /* <OF>
                                        Text corresponding to keyword.  This must be
                                        freed by calling UF_free.
                                    */
);

/****************************************************************************
 Modify the text associated with the keyword specified in the input part.

 Return:
  Return Codes -
        UF_GDT_NO_ERRORS
        UF_err_program_not_initialized

 Environment: Internal and External
 See Also:
 History:
 ****************************************************************************/
extern UFUNEXPORT int UF_GDT_set_keyword_text(
    tag_t           part_tag,       /* <I>
                                        Part to query
                                    */
    const char *    keyword_name,   /* <I>
                                        Keyword whose text to modify
                                    */
    const char *    keyword_text    /* <I>
                                        New text for keyword
                                    */
);

/****************************************************************************
 Return the appended text at the specified location for the input feature
 control frame or dimension.  This routines functionality has been extended
 to include tolerance feature tags. Passing a tolerance feature tag
 in as parameter 1 will query the size tolerance appended text
 data for that tolerance feature.

 Return:
  Return Codes -
        UF_GDT_NO_ERRORS
        UF_err_program_not_initialized

 Environment: Internal and External
 See Also:
 History: Modified in V16 to include tolerance feature tags
 ****************************************************************************/
extern UFUNEXPORT int UF_GDT_ask_appended_text(
    tag_t                    object, /* <I>
                                     FCF, tolerance feature or dimension to
                                     query
                                     */
    UF_GDT_text_location_t location, /* <I>
                                     Appended text location to query
                                     */
    int                  *num_lines, /* <O>
                                     Number of appended text lines
                                     */
    char           ***appended_text  /* <OF,len:num_lines>
                                     Appended text at location requested.  This
                                     array of strings must be freed by calling
                                     UF_free_string_array.
                                     */
);

/****************************************************************************
 Modify the appended text at the specified location for the input feature
 control frame or dimension.

 Return:
  Return Codes -
        UF_GDT_NO_ERRORS
        UF_err_program_not_initialized

 Environment: Internal and External
 See Also:
 History:
 ****************************************************************************/
extern UFUNEXPORT int UF_GDT_set_appended_text(
    tag_t                fcf_or_dim, /* <I>
                                     FCF of dimension to query
                                     */
    UF_GDT_text_location_t location, /* <I>
                                     Appended text location to modify
                                     */
    int                   num_lines, /* <I>
                                     Number of appended text lines
                                     */
    char            **appended_text  /* <I,len:num_lines>
                                            Appended text at location requested
                                     */
);


/****************************************************************************
 Returns all of the tolerance features associated with the face specified.

 Return:
  Return Codes -
        UF_GDT_NO_ERRORS
        UF_err_program_not_initialized

 Environment: Internal and External
 See Also:
 History:
 ****************************************************************************/
extern UFUNEXPORT int UF_GDT_ask_features_of_face(
    tag_t face,                     /* <I>
                                    Face to query for associated tolerance
                                    features.
                                    */
    tag_t **tolerance_features,     /* <OF,len:num_tolerance_features>
                                    Array of tags of tolerance features
                                    associated with this face.  This array
                                    must be freed by calling UF_free.
                                    */
    int *num_tolerance_features     /* <O>
                                    Number of tolerance features in the array.
                                    */
);


/****************************************************************************
 Find the unique geometry index of a piece of geometry referenced by a
 tolerance feature or smart model attribute in the part file.

 Return:
  Return Codes -
        UF_GDT_NO_ERRORS
        UF_err_program_not_initialized

 Environment: Internal and External
 See Also:
 History:
   V18.0.  This function was enhanced to support smart model attributes.
 ****************************************************************************/
extern UFUNEXPORT int UF_GDT_ask_face_index(
    tag_t geometry,       /* <I>
                          Geometry tag to query index from
                          */
    int *geometry_index   /* <O>
                          Geometry index
                          */
);


/****************************************************************************
 Return the geometry tag that corresponds to the geometry index specified.

 Return:
  Return Codes -
        UF_GDT_NO_ERRORS
        UF_err_program_not_initialized

 Environment: Internal and External
 See Also:
 History:
   V18.0.  This function was enhanced to support smart model attributes.
 ****************************************************************************/
extern UFUNEXPORT int UF_GDT_ask_face_from_index(
    int geometry_index,   /* <I>
                          Index of geometry to lookup
                          */
    tag_t *geometry       /* <O>
                          Geometry tag with the index specified
                          */
);

/****************************************************************************
 Return the unique index, or requirement number of a tolerance (fcf or size
 tolerance) or smart model attribute in the part file.

 If the tag input is a tolerance feature and this feature contains no tolerance
 or or size data, an error will be returned.

 Return:
  Return Codes -
        UF_GDT_NO_ERRORS
        UF_GDT_ERR_NOT_TOLERANCE
        UF_GDT_ERR_NO_SIZE_DATA_ON_FEATURE
        UF_err_program_not_initialized

 Environment: Internal and External
 See Also:
 History:
   V18.0.  This function was enhanced to support smart model attributes.
 ****************************************************************************/
extern UFUNEXPORT int UF_GDT_ask_tolerance_index(
    tag_t requirement, /* <I>
                       This can either be a tolerance feature, fcf tag
                       or smart model attribute.
                       */
    int *index         /* <O>
                       Unique index for the given tag
                       */
);

/****************************************************************************
 Find the requirement tag for the index specified.

 If the "fcf" parameter is a NULL_TAG then the index is returned is
 either for size tolerance on a tolerance feature or a smart model
 attribute. If an fcf tag is returned then the index is for the fcf
 and the "requirement" is the parent feature of the fcf.

 Return:
  Return Codes -
        UF_GDT_NO_ERRORS
        UF_err_program_not_initialized

 Environment: Internal and External
 See Also:
 History:
   V18.0.  This function was enhanced to support smart model attributes.
 ****************************************************************************/
extern UFUNEXPORT int UF_GDT_ask_tolerance_from_index(
    int index,                /* <I>
                               Unique index number for the requirement
                               */
    tag_t *requirement,       /* <O>
                              Smart model attribute or tolerance feature for
                              the index.
                              */
    tag_t *fcf                /* <O>
                              Fcf for the index (if the requirement is a
                              tolerance feature and the index is for a
                              FCF.)
                              */
);

/****************************************************************************
 Finds information for a directed dimension tolerance on a tolerance feature.

 Environment: Internal and External
 See Also:
 History: Originally released in V16.0
 ****************************************************************************/
extern UFUNEXPORT int UF_GDT_ask_directed_dimension(
    tag_t tolerance_feature,            /* <I>
                                        Tolerance feature tag
                                        */
    UF_GDT_directed_dimension_p_t *data /* <OF>
                                        Data for the tolerance.  This must
                                        be freed by calling UF_free.
                                        */
);/* <NON_NXOPEN> */
extern UFUNEXPORT int UF_GDT_ask_directed_dimension1(
    tag_t tolerance_feature,            /* <I>
                                        Tolerance feature tag
                                        */
    UF_GDT_directed_dimension1_p_t *data /* <OF>
                                        Data for the tolerance.  This must
                                        be freed by calling UF_free.
                                        */
);
/****************************************************************************
 Put the information for a directed dimension tolerance on a tolerance feature.

 Environment: Internal and External
 See Also:
 History: Originally released in V16.0
 ****************************************************************************/
extern UFUNEXPORT int UF_GDT_set_directed_dimension(
    tag_t tolerance_feature,            /* <I>
                                        Tolerance feature tag
                                        */
    UF_GDT_directed_dimension_p_t data  /* <I>
                                        Data for the tolerance
                                        */
);

/****************************************************************************
 Queries if the given tolerance feature has a directed dimension.

 Environment: Internal and External
 See Also:
 History: Originally released in V16.0
 ****************************************************************************/
extern UFUNEXPORT int UF_GDT_has_directed_dimension(
    tag_t tolerance_feature,            /* <I>
                                        Tolerance feature tag
                                        */
    logical *has_directed_dimension     /* <O>
                                        TRUE if the tolerance feature has a
                                        directed dimension.
                                        */
);

/****************************************************************************
 Finds information about a geometric definition on a tolerance feature.

 Environment: Internal and External
 See Also:
 History: Originally released in V16.0
 ****************************************************************************/
extern UFUNEXPORT int UF_GDT_ask_geometric_definition(
    tag_t tolerance_feature,              /* <I>
                                          Tolerance feature tag
                                          */
    UF_GDT_geometric_definition_p_t *data /* <OF>
                                          Data for the definition.  This must
                                          be freed by calling UF_free.
                                          */
);

/****************************************************************************
 Create the information for a geometric definition on a tolerance feature.
 If the geometric definition is that of a region the input structure,
 data, contains a trimmed sheet and a thickened sheet.  The thickened
 sheet must be a thickening of the input trimmed sheet.  Creating
 associative trimmed sheets and thickened sheets for regions can be
 done by using the following routines:  UF_WAVE_create_linked_face,
 UF_MODL_create_sew, UF_MODL_create_trimmed_sheet, UF_MODL_ask_feat_body,
 and UF_MODL_create_thickened_sheet.

 Environment: Internal and External
 See Also:
 History: Originally released in V16.0
 ****************************************************************************/
extern UFUNEXPORT int UF_GDT_set_geometric_definition(
    tag_t tolerance_feature,              /* <I>
                                          Tolerance feature tag
                                          */
    UF_GDT_geometric_definition_p_t data  /* <I>
                                          Data for the definition
                                          */
);

/****************************************************************************
 Query if the given tolerance feature has a geometric definition.

 Environment: Internal and External
 See Also:
 History: Originally released in V16.0
 ****************************************************************************/
extern UFUNEXPORT int UF_GDT_has_geometric_definition(
    tag_t tolerance_feature,            /* <I>
                                        Tolerance feature tag
                                        */
    logical *has_geometric_definition   /* <O>
                                        TRUE if the tolerance feature has
                                        a geometric definition.
                                        */
);

/****************************************************************************
 For the given tolerance feature find the tolerance feature whose faces
 are a superset.  If no such feature exists, then a NULL_TAG will be
 returned.

 Environment: Internal and External
 See Also:
 History: Originally released in V16.0
 ****************************************************************************/
extern UFUNEXPORT int UF_GDT_ask_super_feature(
    tag_t tolerance_feature,     /* <I>
                                 Tolerance feature tag
                                 */
    tag_t *super_feature         /* <O>
                                 Tag of the super feature
                                 */
);

/****************************************************************************
 Given a tolerance feature, return an array of sub-features.  A sub-feature
 is a tolerance feature whose faces are a subset of the given tolerance
 feature.

 Environment: Internal and External
 See Also:
 History: Originally released in V16.0
 ****************************************************************************/
extern UFUNEXPORT int UF_GDT_ask_sub_features(
    tag_t   tolerance_feature,   /* <I>
                                 Tolerance feature tag
                                 */
    int     *num_sub_features,   /* <O>
                                 Number of subfeatures returned
                                 */
    tag_p_t *sub_features        /* <OF,len:num_sub_features>
                                 Array of subfeature tags.  This array must be
                                 freed by calling UF_free.
                                 */
);

/****************************************************************************
 Finds all targets for the given tolerance feature.

 Environment: Internal and External
 See Also:
 History: Originally released in V16.0
 ****************************************************************************/
extern UFUNEXPORT int UF_GDT_ask_targets_of_datum(
    tag_t datum,                /* <I>
                                Datum feature tag
                                */
    int *num_targets,           /* <O>
                                Number of targets returned
                                */
    tag_p_t *targets            /* <OF,len:num_targets>
                                Array of target tags.  This array must be freed
                                by calling UF_free.
                                */
);


/****************************************************************************
 Find the tag of the datum parent of a given target.

 Environment: Internal and External
 See Also:
 History: Originally released in V16.0
 ****************************************************************************/
extern UFUNEXPORT int UF_GDT_ask_datum_of_target(
    tag_t target,               /* <I>
                                Datum target to query
                                */
    tag_t *datum                /* <O>
                                Parent datum of the target
                                */
);

/****************************************************************************
 Determine if the tolerance feature specified is a linked feature.

 Environment: Internal and External
 See Also:
 UF_GDT_ask_linked_features
 History: Originally released in V16.0
 ****************************************************************************/
extern UFUNEXPORT int UF_GDT_is_linked_feature(
    tag_t tolerance_feature,    /* <I>
                                Tolerance feature to query
                                */
    logical *is_linked          /* <O>
                                TRUE if feature is linked
                                */
);

/****************************************************************************
 Return an array of features linked to the given tolerance feature.

 Environment: Internal and External
 See Also:
 UF_GDT_is_linked_feature
 History: Originally released in V16.0
 ****************************************************************************/
extern UFUNEXPORT int UF_GDT_ask_linked_features(
    tag_t   tolerance_feature,   /* <I>
                                 Tolerance feature tag
                                 */
    int     *num_linked,         /* <O>
                                 Number of linked features
                                 */
    tag_p_t *linked_features     /* <OF,len:num_linked>
                                 Array of linked feature tags.  This array must
                                 be freed by calling UF_free.
                                 */
);

/****************************************************************************
 Return two arrays of tags which correspond to the "displayed elements" of
 a display instance.  Note objects are created for feature control frames
 and feature control frame appended text.  This function is most useful for
 applications performing translation of display instance information to
 another data format.

 The input display instance could either be a tolerance feature instance or
 a product definition instance.

 NOTE: The application may use UF_OBJ_delete_object to delete each of the
 tags created and returned by this routine.

 NOTE ALSO: Users are responsible for deleting the output curves and annotations
 after calling this function and finish their operations.

 Environment: Internal and External
 See Also:
 History: Originally released in V16.0
 ****************************************************************************/
extern UFUNEXPORT int UF_GDT_ask_tags(
    tag_t display_instance,   /* <I>
                               Display instance in which to generate curve or
                               annotation tags.
                               */
    tag_t **curves,           /* <OF,len:num_curves>
                               Array of curves (either line or arc type curves)
                               used to describe the annotation display.  This
                               must be freed by calling UF_free.
                               */
    int *num_curves,          /* <O>
                               Number of curves in array
                               */
    tag_t **annotations,      /* <OF,len:num_annotations>
                               Array of annotations (either dimension, note,
                               or crosshatching) used to describe the
                               annotation display.  This array must be freed by
                               calling UF_free.
                               */
    int *num_annotations      /* <O>
                               Number of annotations in array
                               */
);

/****************************************************************************
 This function will set the following parameters for regions of tolerance
 features: region thickness, whether or not the region
 is to be crosshatched, the crosshatch angle, and the
 crosshatch distance

 Return Codes -
       UF_GDT_NO_ERRORS
       UF_GDT_ERR_NON_POSITIVE_PARAMETERS

 Environment: Internal and External
 See Also:
 History: Originally released in V16.0
 ****************************************************************************/
extern UFUNEXPORT int UF_GDT_set_region_parameters(
    double region_thickness,    /* <I>
                                 The region thickness which is to be used when
                                 regions for GDTs are created
                                 */
    logical crosshatch_on,      /* <I>
                                 TRUE if the region of a GDT is to be
                                 crosshatched.
                                 */
    double crosshatch_angle,    /* <I>
                                 The angle to be used when crosshatching a
                                 region
                                 */
    double crosshatch_distance  /* <I>
                                 The distance between hatch lines to be used
                                 when crosshatching a region
                                 */
);

/****************************************************************************
 The following function will add a leader to a given instance based
 on the given UF_GDT_leader_spec structure.

 Return Codes -
      UF_GDT_NO_ERRORS
      UF_GDT_ERR_INVALID_VIEW         (View to attach leader is invalid)
      UF_GDT_ERR_NO_ADD_PROFILE_LDR   (Cannot add a profile leader)
      UF_GDT_ERR_NO_ADD_TO_INSTANCE   (Cannot add leaders to the following:
                                       - instance with a tolerance of size
                                       - instances with a profile leader
                                       - datum targets
                                       - datums without dot terminated leader
                                      )
      UF_err_program_not_initialized

 Environment: Internal and External
 See Also:
 History: Originally released in V16.0
 ****************************************************************************/
extern UFUNEXPORT int UF_GDT_add_leader(
    tag_t instance,              /* <I>
                                  Tag of instance to add leader to
                                  */
    UF_GDT_leader_spec_p_t spec  /* <I>
                                  Spec structure of leader to create
                                  */
);


/****************************************************************************
 The following function will remove an instance's nth leader

 Return Codes -
      UF_GDT_NO_ERRORS
      UF_GDT_ERR_NO_INDEXED_LEADER    (Instance's nth leader non-existent)
      UF_GDT_ERR_NO_REMOVE_ONLY_LDR   (Can't remove instance's only leader)
      UF_err_program_not_initialized

 Environment: Internal and External
 See Also:
 History: Originally released in V16.0
 ****************************************************************************/
extern UFUNEXPORT int UF_GDT_remove_leader(
    tag_t instance,         /* <I>
                             Tag of instance to remove a leader from
                             */
    int nth                 /* <I>
                             Index of the leader to be removed
                             */
);

/****************************************************************************
 The following function will query a given instance for the nth
 leader object and return information about that leader

 Return Codes -
      UF_GDT_NO_ERRORS
      UF_GDT_ERR_NO_INDEXED_LEADER    (Instance's nth leader non-existent)
      UF_err_program_not_initialized

 Environment: Internal and External
 See Also:
 History: Originally released in V16.0
 ****************************************************************************/
extern UFUNEXPORT int UF_GDT_ask_leader(
    tag_t instance,             /* <I>
                                 Tag of instance to query
                                 */
    int nth,                    /* <I>
                                 Index of the leader to query
                                 */
    UF_GDT_leader_spec_p_t spec /* <O>
                                 Spec structure of the nth leader
                                 */
);

/****************************************************************************
 The following function will determine the number of leaders a given
 instance has.  This function will return a valid leader count for:
    Feature instances without a dimension
    Datum target instances
    Datum instances on dot terminated leaders
 For all other instances, a zero will return as the leader count.

 Return Codes -
      UF_GDT_NO_ERRORS
      UF_err_program_not_initialized

 Environment: Internal and External
 See Also:
 History: Originally released in V16.0
 ****************************************************************************/
extern UFUNEXPORT int UF_GDT_ask_num_leaders(
    tag_t instance,                /* <I>
                                    Tag of the instance to query
                                    */
    int *num_leaders               /* <O>
                                    Number of leaders on the instance
                                    */
);

/****************************************************************************
 The following function will query the given feature instance for:
      dimension tags
      feature control frame tags
      appended text tags (of the feature control frames only)
      number of non-dimensional leaders

 Return Codes -
      UF_GDT_NO_ERRORS
      UF_GDT_ERR_NOT_FEATURE_INSTANCE (Object is not a feature instance)
      UF_err_program_not_initialized

 Environment: Internal and External
 See Also:
 UF_GDT_free
 History: Originally released in V16.0
 ****************************************************************************/
extern UFUNEXPORT int UF_GDT_ask_annotation_tags(
    tag_t instance,                 /* <I>
                                     Tag of the instance to query
                                     */
    UF_GDT_annotation_tags_p_t tags /* <OF>
                                     Data queried off of the instance.  Use
                                     UF_GDT_free with
                                     UF_GDT_ANNOTATION_TAGS_TYPE to free this
                                     structure.
                                     */
);


/****************************************************************************
 The following function will return the datum identifiers associated with
 the tolerance feature callout or dimension instance.

 NOTE: The application is responsible for freeing the array of datums
 allocated by this function.

 Environment: Internal and External
 See Also:
 History: Originally released in V16.0
 ****************************************************************************/
extern UFUNEXPORT int UF_GDT_ask_associated_datums(
    tag_t feature_instance,     /* <I>
                                 Tolerance feature display instance
                                 */
    tag_t **associated_datums,  /* <OF,len:num_associated_datums>
                                 Associated datum features
                                 */
    int *num_associated_datums  /* <O>
                                 Number of datum attached to the instance
                                 */
);


/****************************************************************************
 Given a datum identifier, the following function will return the type of
 associative relationship for the datum.  This is especially useful when the
 caller needs to know how datum feature symbols are attached to other display
 instances.

 Environment: Internal and External
 See Also:
 History: Originally released in V16.0
 ****************************************************************************/
extern UFUNEXPORT int UF_GDT_ask_association_type(
    tag_t datum_instance,                  /* <I>
                                            Datum identifier instance
                                            */
    UF_GDT_datum_assoc_type_t *assoc_type  /* <I>
                                            Type of datum associativity
                                            */
);

/****************************************************************************
  Inherits the GD&T info from a model to drawing member view

  Environment: Internal and external
  See Also :
  History:     Originally released in V16.0
*******************************************************************************/
extern UFUNEXPORT int UF_GDT_inherit_model_gdt_to_drawing(
    tag_t member_view   /* <I> member view in which to inherit  */
);

/*******************************************************************************
  Sets the show feature info status for the work part to be true or false.

  Environment: Internal and external
  See Also :
  History:     Originally released in V16.0
*******************************************************************************/
extern UFUNEXPORT int UF_GDT_set_instance_display_information(
    logical preference  /* <I> Display preference setting  */
);

/*******************************************************************************
  Queries the show feature info status for the work part

  Environment: Internal and external
  See Also :
  History:     Originally released in V16.0
*******************************************************************************/
extern UFUNEXPORT int UF_GDT_ask_instance_display_information(
    logical *preference  /* <O> Current display preference setting  */
);

/*******************************************************************************
  Sets the selection of non-feature edges for the GD&T session to be true
  or false.

  Environment: Internal and external
  See Also :
  History:     Originally released in V16.0
*******************************************************************************/
extern UFUNEXPORT int UF_GDT_set_non_feature_edge_selection(
    UF_GDT_edge_select_type_t allow_non_feature_edges  /* <I> Should selection
                                                        *     of non-feature
                                                        *     edges be allowed
                                                        *     when creating
                                                        *     display instances?
                                                        */
);

/*******************************************************************************
  Queries the feature edges selection mode for the GD&T in the session.

  Environment: Internal and external
  See Also :
  History:     Originally released in V16.0
*******************************************************************************/
extern UFUNEXPORT int UF_GDT_ask_non_feature_edge_selection(
    UF_GDT_edge_select_type_t *allow_non_feature_edges  /* <O> Current selection
                                                         *     preference  */
);

/*******************************************************************************
  Reset the specified part's Geometric Tolerancing Callout Rules Table
  using the appropriate callout rules file.

  Environment: Internal and external
  See Also :
  History:     Originally released in V16.0
*******************************************************************************/
extern UFUNEXPORT int UF_GDT_reset_callout_rules(
    tag_t part /* <I> Part to update rules of */
);

/*******************************************************************************
  Return the callout strings corresponding to each of the tolerance feature's
  tolerance types.

  If the input tolerance tag is a tolerance feature tag then all of the
  tolerance feature's callout strings are returned including:
      its datum label (if any)
      its datum target label (if any)
      callout strings for each of its feature control frames (if any)
      callout string for its size tolerance  (if any)
      callout string for its directed dimension  (if any)

  If the input tolerance tag is a single feature control frame then only the
  its callout string is returned.

  If the input tolerance tag is a composite feature control frame then two
  callout strings are returned.  The first representing the upper tolerance
  and the second representing the lower tolerance.

  Return Codes -
      UF_GDT_NO_ERRORS
      UF_GDT_ERR_NOT_SUBTOLERANCE_TYPE
      UF_err_program_not_initialized

  Environment: Internal and external

  History:     Originally released in V16.0
 *****************************************************************************/
extern UFUNEXPORT int UF_GDT_ask_callout_strings(
    tag_t tolerance,            /* <I>
                                Tolerance to query may be either a tolerance
                                feature tag or a feature control frame tag
                                */
    int   *num_callout_strings, /* <O>
                                Number of callout strings
                                */
    UF_GDT_callout_string_p_t *callout_strings /* <OF,len:num_callout_strings,free:UF_GDT_free>
                                List of callout strings.
                                Use UF_GDT_free to free each element of this
                                array and then UF_free to free the array.
                                */
);

/*******************************************************************************
  Creates the a cylindrical datum target area on the part with the area data
  specified.

  Environment: Internal and external
  See Also :
  History:     Originally released in V16.0
*******************************************************************************/
extern UFUNEXPORT int UF_GDT_create_target_cyl_area(
    UF_GDT_target_cyl_area_p_t target_data,  /* <I> Target area data  */
    tag_t *target_area                       /* <O> Tag of target area */
);

/*******************************************************************************
  Returns the data associated with the cylindrical datum target area.

  Environment: Internal and external
  See Also :
  History:     Originally released in V16.0
*******************************************************************************/
extern UFUNEXPORT int UF_GDT_ask_target_cyl_parms(
    tag_t target,                     /* <I> Datum target tag */
    UF_GDT_target_cyl_area_p_t *data  /* <OF> Cylindrical area data */
);

/*******************************************************************************
  Returns the currently set index display method.

  Environment: Internal and external
  See Also :
  History:     Originally released in V16.0
********************************************************************************/
extern UFUNEXPORT int UF_GDT_ask_index_display(
    UF_GDT_index_display_type_t *index_display /* <O>
                                               Current index display method.
                                               */
);

/*******************************************************************************
  Sets the index display method.

  Environment: Internal and external
  See Also :
  History:     Originally released in V16.0
********************************************************************************/
extern UFUNEXPORT int UF_GDT_set_index_display(
    UF_GDT_index_display_type_t index_display /* <I>
                                              Desired index display method.
                                              */
);

/*******************************************************************************
  Returns the index of the given tolerance as a string.

  Environment: Internal and external
  See Also :
  History:     Originally released in V16.0
********************************************************************************/
extern UFUNEXPORT int UF_GDT_ask_tolerance_index_string(
    tag_t tolerance_tag, /* <I>
                         Tag of the tolerance to query. This should be either
                         the tag of an FCF object or a tolerance feature
                         object.
                         */
    char **index_string  /* <OF>
                         Tolerance index of the given tag. Use UF_free to
                         deallocate the memory when done.
                         */
);

/*******************************************************************************
  Returns the index of the given face as a string.

  Environment: Internal and external
  See Also :
  History:     Originally released in V16.0
********************************************************************************/
extern UFUNEXPORT int UF_GDT_ask_face_index_string(
    tag_t face_tag,      /* <I>
                         Tag of the face to query.
                         */
    char **index_string  /* <OF>
                         Face  index of the given tag. Use UF_free to
                         deallocate the memory when done.
                         */
);

/******************************************************************************
This function allows the calling program to create a wall thickness
tolerance feature.  This does not create a displayed instance.

 Environment:Internal and External
See Also:
 History:
 ******************************************************************************/
extern UFUNEXPORT int UF_GDT_create_wall_thickness(
UF_GDT_feature_parms_p_t feat_parms ,/* <I>
                                     Tolerance feature creation data
                                     */
UF_GDT_size_tolerance_p_t thickness_data ,/* <I>
                                          Creation information for the
                                          wall thickness tolerance
                                          */
tag_t * thickness_feature  /* <O>
                           Identifier of created tolerance feature
                           */
);

/******************************************************************************
Allows the calling program to query the wall thickness information
(nominal value, +/- tolerance values, etc.) for a given tolerance
feature.

Environment: Internal  and  External
See Also:
History:Original release was in 17.0.
 ******************************************************************************/
extern UFUNEXPORT int UF_GDT_ask_wall_thickness_parms(
tag_t tolerance_feature ,/* <I>
                         Tolerance feature to inquire
                         */
UF_GDT_size_tolerance_p_t * size_data  /* <OF,free:UF_GDT_free>
                                       Information on the wall thickness. The
                                       data allocated for this structure must
                                       be freed by calling UF_GDT_free.
                                       */
);

/******************************************************************************
Given a tolerance feature or datum feature, this function allows for
the resetting of the wall thickness tolerance parameters.

 Environment:Internal and External
See Also:
History:Original release was in 17.0.
*****************************************************************************/
extern UFUNEXPORT int UF_GDT_set_wall_thickness_parms(
tag_t tolerance_feature ,/* <I>
                         Tolerance Feature to set
                         */
UF_GDT_size_tolerance_t * thickness_data  /* <I>
                                          New wall thickness data.
                                          */
);

/****************************************************************************
 Queries if the given tolerance feature has a wall thickness tolerance.

 Environment: Internal and External
 See Also:
 History: Originally released in V17.0
 ****************************************************************************/
extern UFUNEXPORT int UF_GDT_has_wall_thickness(
    tag_t tolerance_feature,            /* <I>
                                        Tolerance feature tag
                                        */
    logical *has_wall_thickness         /* <O>
                                        TRUE if the tolerance feature has a
                                        directed dimension.
                                        */
);

/******************************************************************************
 This function queries the crosshatching distance and angle parameters for the
 given datum target area instance.

 Return:
 Return Codes -
 UF_GDT_NO_ERRORS
 UF_err_bad_parameter_number_1
 UF_err_program_not_initialized

 Environment:Internal and External
 See also:
 History:
*****************************************************************************/
extern UFUNEXPORT int UF_GDT_ask_target_area_xhatch(
    tag_t target_inst,                   /* <I> Tag of target instance      */
    double *distance,                    /* <O> Crosshatching distance      */
    double *angle                        /* <O> Crosshatching angle         */
);

/******************************************************************************
 This function sets the crosshatching distance and angle parameters for the
 given datum target area instance.

 Return:
 Return Codes -
 UF_GDT_NO_ERRORS
 UF_err_bad_parameter_number_1
 UF_err_bad_parameter_number_2
 UF_err_bad_parameter_number_3
 UF_err_program_not_initialized

 Environment:Internal and External
 See also:
 History:
*****************************************************************************/
extern UFUNEXPORT int UF_GDT_set_target_area_xhatch(
    tag_t target_inst,                   /* <I> Tag of target instance      */
    double distance,                     /* <I> Crosshatching distance      */
    double angle                         /* <I> Crosshatching angle         */
);

/*******************************************************************************
  Returns TRUE if the tolerance feature is a Complex Tolerance Feature.

  Return Codes -
  UF_GDT_NO_ERRORS
  UF_err_program_not_initialized
  UF_GDT_ERR_NOT_TOL_FEAT

  Environment: Internal and external

  See Also :

  History:     Originally released in V18.0
********************************************************************************/
extern UFUNEXPORT int UF_GDT_is_complex_feature(
    tag_t tolerance_tag,    /* <I>
                               Tag of the tolerance feature to query
                            */
    logical *status         /* <O>
                               Status of the query
                            */
);

/*******************************************************************************
  Returns TRUE if the tolerance feature is a Complex Tolerance Subfeature.

  Return Codes -
  UF_GDT_NO_ERRORS
  UF_err_program_not_initialized
  UF_GDT_ERR_NOT_TOL_FEAT

  Environment: Internal and external

  See Also :

  History:     Originally released in V18.0
********************************************************************************/
extern UFUNEXPORT int UF_GDT_is_complex_sub_feature(
    tag_t tolerance_tag,    /* <I>
                               Tag of the tolerance feature to query
                            */
    logical *status         /* <O>
                               Status of the query
                            */
);

/*******************************************************************************
  Given a complex tolerance subfeature, return its parent complex feature.
  A complex feature is a tolerance feature defined by a predefined set of
  subfeatures known as complex tolerance subfeatures.

  Return Codes -
  UF_GDT_NO_ERRORS
  UF_err_program_not_initialized
  UF_GDT_ERR_NOT_COMPLEX_SUB_FEAT

  Environment: Internal and external

  See Also :

      History:     Originally released in V18.0
********************************************************************************/
extern UFUNEXPORT int UF_GDT_ask_complex_feature(
    tag_t complex_sub_feature,     /* <I>
                                      Tag of the complex tolerance subfeature
                                      to query.
                                   */
    tag_p_t complex_feature        /* <O>
                                      Complex feature tags containing the
                                      complex tolerance subfeature specified.
                                   */
);

/*******************************************************************************
  Given a complex tolerance feature, return an array of complex sub-features.
  A complex sub-feature is a tolerance subfeature whose faces are a subset of
  the given complex tolerance feature.

  Return Codes -
  UF_GDT_NO_ERRORS
  UF_err_program_not_initialized
  UF_GDT_ERR_NOT_COMPLEX_TOL_FEAT

  Environment: Internal and external

  See Also :

  History:     Originally released in V18.0
********************************************************************************/
extern UFUNEXPORT int UF_GDT_ask_complex_sub_features(
    tag_t complex_feature,         /* <I>
                                      Tag of the complex tolerance feature to
                                      query.
                                   */
    int *num_complex_sub_features, /* <O>
                                      Number of complex subfeatures returned.

                                   */
    tag_p_t *complex_sub_features  /* <OF,len:num_complex_sub_features>
                                      Array of complex subfeature tags. This array
                                      must be freed by calling UF_free.
                                   */
);

/******************************************************************************
  Allows the calling program to query the depth tolerance information
  (nominal value, +/- tolerance values, etc.) for a given tolerance
  feature.

  Return Codes -
  UF_GDT_NO_ERRORS
  UF_GDT_ERR_NOT_TOL_FEAT
  UF_err_program_not_initialized x

  Environment: Internal  and  External
  See Also:
  History:     Original release was in 18.0.
******************************************************************************/
extern UFUNEXPORT int UF_GDT_ask_depth_tolerance_parms(
    tag_t tolerance_feature ,                /* <I>
                                                Tolerance feature to inquire
                                             */
    UF_GDT_depth_tolerance_p_t * depth_data  /* <OF,free:UF_GDT_free>
                                                Information on the depth tolerance.  The
                                                data allocated for this structure must
                                                be freed by calling UF_GDT_free.
                                             */
);

/******************************************************************************
  Given a tolerance feature or datum feature, this function allows for
  the resetting of the depth tolerance parameters.

  Return Codes -
  UF_GDT_NO_ERRORS
  UF_GDT_ERR_NOT_TOL_FEAT
  UF_GDT_ERR_TOL_VALIDATION_FAILED
  UF_err_program_not_initialized

  Environment: Internal  and  External
  See Also:
  History:     Original release was in 18.0.
*****************************************************************************/
extern UFUNEXPORT int UF_GDT_set_depth_tolerance_parms(
    tag_t tolerance_feature,               /* <I>
                                              Tolerance Feature to set
                                           */
    UF_GDT_depth_tolerance_t * depth_data  /* <I>
                                              Data to be applied to tolerance feature.
                                           */
);

/****************************************************************************
  Queries if the given tolerance feature has a depth tolerance.

  Return Codes -
  UF_GDT_NO_ERRORS
  UF_GDT_ERR_NOT_TOL_FEAT
  UF_err_program_not_initialized

  Environment: Internal and External
  See Also:
  History:     Originally released in V18.0
****************************************************************************/
extern UFUNEXPORT int UF_GDT_has_depth_tolerance(
    tag_t tolerance_feature,            /* <I>
                                           Tolerance feature tag
                                        */
    logical *has_depth_tolerance        /* <O>
                                           TRUE if the tolerance feature has a
                                           depth tolerance.
                                        */
);

/****************************************************************************
  Queries if the given tolerance feature has a size tolerance.

  Return Codes -
  UF_GDT_NO_ERRORS
  UF_GDT_ERR_NOT_TOL_FEAT
  UF_err_program_not_initialized

  Environment: Internal and External
  See Also:
  History:     Originally released in V18.0
****************************************************************************/
extern UFUNEXPORT int UF_GDT_has_size_tolerance(
    tag_t tolerance_feature,            /* <I>
                                           Tolerance feature tag
                                        */
    logical *has_size_tolerance         /* <O>
                                           TRUE if the tolerance feature has a
                                           size tolerance.
                                        */
);

/******************************************************************************
 This routine sets the size data based on the limits and fits information.

 Return Codes -
        UF_GDT_NO_ERRORS
        UF_GDT_ERR_NOT_TOL_FEAT
        UF_err_program_not_initialized

 Environment: Internal  and  External
 See Also:
 History:Original release was in 18.0.
 *****************************************************************************/
extern UFUNEXPORT int UF_GDT_set_size_data(
     tag_t tolerance_feature ,/* <I> Tolerance feature to inquire */
     UF_GDT_limits_and_fits_tolerance_p_t lim_fits  /* <IOF> Information on the limits
                                                   and fits tolerance.  The data
                                                   allocated for this structure must
                                                   be freed by calling UF_GDT_free.
                                                */
);

/******************************************************************************
 This routine creates a datum reference frame from the given data structure.

 Return Codes -
        UF_GDT_NO_ERRORS
        UF_err_program_not_initialized

 Environment: Internal  and  External
 See Also:
 History:Original release was in 18.0.
 *****************************************************************************/
extern UFUNEXPORT int UF_GDT_create_drf(
    UF_GDT_drf_data_p_t drf_data,  /* <I> Data of a datum reference frame    */
    tag_t *drf                     /* <O> Identifier of created frame        */
);

/******************************************************************************
 This routine sets the data of a datum reference frame from the given data
 structure.

 Return Codes -
        UF_GDT_NO_ERRORS
        UF_err_program_not_initialized

 Environment: Internal  and  External
 See Also:
 History:Original release was in 18.0.
 *****************************************************************************/
extern UFUNEXPORT int UF_GDT_set_drf(
    tag_t drf,                    /* <I> Datum reference frame identifier    */
    UF_GDT_drf_data_p_t drf_data  /* <I> Data of a datum reference frame     */
);

/******************************************************************************
 This function asks the data of the given datum reference frame.

 Return Codes -
        UF_GDT_NO_ERRORS
        UF_err_program_not_initialized

 Environment: Internal  and  External
 See Also:
 History:Original release was in 18.0.
 *****************************************************************************/
extern UFUNEXPORT int UF_GDT_ask_drf(
    tag_t drf,                    /* <I>  Datum reference frame identifier   */
    UF_GDT_drf_data_p_t *drf_data /* <OF> Data of a datum reference frame.
                                   *      This must be freed by calling UF_free
                                   */

);

/******************************************************************************
 This function sets the datum reference frame for a feature control frame.

 Return Codes -
        UF_GDT_NO_ERRORS
        UF_err_program_not_initialized

 Environment: Internal  and  External
 See Also:
 History:Original release was in 18.0.
 *****************************************************************************/
extern UFUNEXPORT int UF_GDT_set_fcf_drf(
    tag_t fcf,                 /* <I> Feature control frame identifier       */
    tag_t drf                  /* <I> Datum reference frame to use with FCF  */
);

/******************************************************************************
 This function sets the composite priority for a composite feature control
 frame.

 Return Codes -
        UF_GDT_NO_ERRORS
        UF_err_program_not_initialized

 Environment: Internal  and  External
 See Also:
 History:Original release was in 18.0.
 *****************************************************************************/
extern UFUNEXPORT int UF_GDT_set_composite_drf(
    tag_t fcf,                   /* <I> Feature control frame identifier    */
    UF_GDT_precedence_t priority /* <I> Precedence of lower datum frame     */
);

/******************************************************************************
 This function asks the datum reference frame of a feature control frame.

 Return Codes -
        UF_GDT_NO_ERRORS
        UF_err_program_not_initialized

 Environment: Internal  and  External
 See Also:
 History:Original release was in 18.0.
 *****************************************************************************/
extern UFUNEXPORT int UF_GDT_ask_fcf_drf(
    tag_t fcf,                 /* <I> Feature control frame identifier       */
    tag_t *drf                 /* <O> Datum reference frame to use with FCF  */
);

/******************************************************************************
 This function asks the composite priority for a composite feature control
 frame.

 Return Codes -
        UF_GDT_NO_ERRORS
        UF_err_program_not_initialized

 Environment: Internal  and  External
 See Also:
 History:Original release was in 18.0.
 *****************************************************************************/
extern UFUNEXPORT int UF_GDT_ask_composite_drf(
    tag_t fcf,                     /* <I> Feature control frame identifier   */
    UF_GDT_precedence_t *priority  /* <O> Precedence of lower datum frame    */
);

/******************************************************************************
 Given a datum reference frame, this function determines if the frame is a
 single datum reference frame.

 Return Codes -
        UF_GDT_NO_ERRORS
        UF_GDT_ERR_NOT_TOL_FEAT
        UF_err_program_not_initialized

 Environment: Internal  and  External
 See Also:
 History:Original release was in 18.0.
 *****************************************************************************/
extern UFUNEXPORT int UF_GDT_is_single_datum_reference_frame(
    tag_t    frame,        /* <I> Tag of the datum reference frame to query  */
    logical *is_single     /* <O> True if frame is a single datum ref frame  */
);

/************************************************************************
 *  This routine updates the given list of tolerance features.  If update
 *  is currently in progress, or any of the entites in the list are not
 *  tolerance features,  no update will be done.
 *
 *  Return:
 *       0  =  Success
 *       error code otherwise
 *
 *  See also:
 *  Environment : Internal  and  External
 *  History: Created in v16.0.4.2
 ***********************************************************************/
extern UFUNEXPORT int UF_GDT_update_features(
    int num_features,           /* <I>
                                Number of tolerance features to update
                                */
    tag_p_t features            /* <I,len:num_features>
                                       List of tolerance feature tags to update
                                */
);


/****************************************************************************
 This routine queries all the datums on the tolerance feature.

 Return Codes -
              UF_GDT_NO_ERRORS
              UF_err_program_not_initialized
              UF_GDT_ERR_NOT_TOL_FEAT

 Environment: Internal and External
 See Also:
 History: Originally released in V18.0
 ****************************************************************************/
extern UFUNEXPORT int UF_GDT_ask_datums_of_feature(
       tag_t datum_feature, /* <I>Tolerance feature to inquire */
       tag_p_t * datums,    /* <OF,len:num_datums> All the datums associated with the tolerance feature,
                                Use UF_free to deallocate memory when done. */
       int *num_datums      /* <O> Number of datums */
);


/******************************************************************************
This function returns the corresponding datum by a datum label.

Return Codes -
              UF_GDT_NO_ERRORS
              UF_err_program_not_initialized
              UF_GDT_ERR_NOT_TOL_FEAT

Environment: Internal  and  External
See Also:
History:Original release was in 18.0.
*******************************************************************************/
extern UFUNEXPORT int UF_GDT_ask_datum_by_label(
       const char * datum_label,    /* <I>Datum label string to inquire*/
       tag_t *      datum           /* <O>Tag of the corresponding datum*/
);


/******************************************************************************
This function allows the calling program to add a datum to tolerance feature.

Return Codes -
              UF_GDT_NO_ERRORS
              UF_err_program_not_initialized
              UF_GDT_ERR_NULL_LABEL
              UF_GDT_ERR_NOT_TOL_FEAT

Environment: Internal  and  External
See Also:
History:Original release was in 18.0.
 ******************************************************************************/
extern UFUNEXPORT int UF_GDT_add_datum_to_feature(
       tag_t feature, /* <I> Tolerance datum feature */
       tag_t datum    /* <I> Datum to be added       */
);


/******************************************************************************
This function allows the calling program to set keywords on datum objects.

Return Codes -
              UF_GDT_NO_ERRORS
              UF_err_program_not_initialized
              UF_GDT_ERR_INVALID_KEYWORD
              UF_GDT_ERR_NOT_DATUM

Environment: Internal  and  External
See Also:
History:Original release was in 18.0.
 ******************************************************************************/
extern UFUNEXPORT int UF_GDT_set_datum_keywords(
       tag_t datum,         /* <I> The datum object */
       int num_keywords,    /* <I> The number of keywords */
       UF_GDT_keyword_p_t keywords  /* <I,len:num_keywords> The keywords list */
);

/******************************************************************************
This function allows the calling program to query keywords on datum objects.

Return Codes -
              UF_GDT_NO_ERRORS
              UF_err_program_not_initialized
              UF_GDT_ERR_NOT_DATUM

Environment: Internal  and  External
See Also:
History:Original release was in 18.0.
 ******************************************************************************/
extern UFUNEXPORT int UF_GDT_ask_datum_keywords(
       tag_t datum,          /* <I> The datum object */
       int *num_keywords,    /* <O> The number of keywords */
       UF_GDT_keyword_p_t *keywords /* <OF,len:num_keywords>
                                            The keywords list */
);

/******************************************************************************
This function allows the calling program to query datum feature associated
with the given datum.

Return Codes -
              UF_GDT_NO_ERRORS
              UF_err_program_not_initialized
              UF_GDT_ERR_NOT_DATUM
              UF_GDT_ERR_DELETED_DATUM

Environment: Internal  and  External
See Also:
History:Original release was in 18.0.
 ******************************************************************************/
extern UFUNEXPORT int UF_GDT_ask_feature_of_datum(
       tag_t datum,          /* <I> The datum object */
       tag_t *feature        /* <O> The datum feature assoicated
                                with the datum object */
);

/******************************************************************************
This function allows the calling program to query a view to determine if it is
a GD&T view.

Return Codes -
              UF_GDT_NO_ERRORS
              UF_err_program_not_initialized

NOTE:    Since GDT views functionality is obsoleted in NX3, this function will
         always return TRUE. Because in NX3 and later, any view will have the
         same functionality as previous defined gdt view does.

Environment: Internal  and  External
See Also:
History:Original release was in 18.0.
 ******************************************************************************/
extern UFUNEXPORT int UF_GDT_is_gdt_view(
    tag_t view,           /* <I> The view tag to query */
    logical *is_gdt_view  /* <O> TRUE if the view is a
                           *     GD&T view.
                           */
);

/******************************************************************************
This function allows the calling program to query a view to determine the
view matrix.

Return Codes -
              UF_GDT_NO_ERRORS
              UF_err_program_not_initialized

NOTE:    GDT views functionality is obsoleted in NX3. In NX3 and later,
         any view will have the same functionality as previous defined
         gdt view does, so this function will just return the given's
         view's orientation.

Environment: Internal  and  External
See Also:
History:Original release was in 18.0.
 ******************************************************************************/
extern UFUNEXPORT int UF_GDT_ask_gdt_view_matrix(
    tag_t view,           /* <I> The view tag to query   */
    double gdt_matrix[9]  /* <O> Matrix of the GD&T view */
);

/******************************************************************************
This function will initialize data structures in UF_GDT

Return Codes -
              UF_GDT_NO_ERRORS
              UF_err_program_not_initialized

Environment: Internal  and  External
See Also:
History:Original release was in 18.0.4 and v19.0
 ******************************************************************************/
extern UFUNEXPORT int UF_GDT_init(
    UF_GDT_data_type_t type, /* -<I>  Type of data structure to free         */
    void * data /* <I/O> data structure to be initialized to */
);

/******************************************************************************
Determines if the feature is a datum target feature or not.

Return Codes -
              UF_GDT_NO_ERRORS
              UF_err_program_not_initialized
              UF_GDT_ERR_NOT_TOL_FEAT

Environment: Internal  and  External
See Also:
History:Original release was in 19.0.
 ****************************************************************************/
extern UFUNEXPORT int UF_GDT_is_datum_target(
    tag_t tolerance_feature ,/* <I>Tolerance Feature to inquire*/
    logical * is_datum_target  /* <O>Status of query*/
);

/******************************************************************************
This function allows the calling program to query the thread tolerance
information for a given tolerance feature.

Return Codes -
       UF_GDT_NO_ERRORS
       UF_GDT_ERR_NOT_TOL_FEAT
       UF_err_program_not_initialized

Environment: Internal  and  External
See Also:
History: Original release was in 18.0.5, NX1.0.1 and NX2.0.0
 *****************************************************************************/
extern UFUNEXPORT int UF_GDT_ask_thread_tolerance_parms(
    tag_t tolerance_feature ,           /* <I>
                                            Tolerance feature to inquire
                                        */
     UF_GDT_thread_tolerance_p_t *data   /* <OF,free:UF_GDT_free>
                                            Information on the thread
                                            tolerance parms. The data
                                            allocated for this structure must
                                            be freed by calling UF_GDT_free.
                                         */
);

/******************************************************************************
This function allows the calling program to set the thread tolerance
information for a given tolerance feature.

Return Codes -
       UF_GDT_NO_ERRORS
       UF_GDT_ERR_NOT_TOL_FEAT
       UF_err_program_not_initialized
       UF_GDT_ERR_INVALID_THREAD_TOL
       UF_GDT_ERR_TOL_VALIDATION_FAILED
       UF_GDT_ERR_INVALID_FEAT_TYPE_FOR_THREAD_TOL

Environment: Internal  and  External
See Also:
History: Original release was in 18.0.5, NX1.0.1 and NX2.0.0
 *****************************************************************************/
extern UFUNEXPORT int UF_GDT_set_thread_tolerance_parms(
     tag_t tolerance_feature ,           /*
                                           <I> Tolerance feature to inquire
                                         */
     UF_GDT_thread_tolerance_p_t data   /* <I> Thread tolerance parms to
                                           apply to the tolerance feature.
                                        */
);

/******************************************************************************
Does this tolerance feature reference modeling features.

Return:
  Return Codes -
        UF_GDT_NO_ERRORS
        UF_GDT_ERR_NOT_TOL_FEAT
        UF_err_program_not_initialized

Environment: Internal  and  External
See Also:
History: Original release NX2.0.0
 ****************************************************************************/
extern UFUNEXPORT int UF_GDT_is_modl_based(
    tag_t tolerance_feature,  /* <I>
                                 Tolerance feature to inquire
                              */
    logical *is_modl_based    /* <O>
                                 Status of query
                              */
);

/******************************************************************************
Allows the calling program to create a model based tolerance feature. A model
based tolerance feature references NX modeling features. This function does not
create a display instance.

Return:
  Return Codes -
        UF_GDT_NO_ERRORS
        UF_err_program_not_initialized
        UF_GDT_ERR_INVALID_MODL_DATA
        UF_GDT_ERR_MODL_FEATURES_NOT_FULLY_LOADED
        UF_GDT_ERR_INVALID_FACE_MAP
        UF_GDT_ERR_FACE_MAP_MISMATCH
        UF_GDT_ERR_INVALID_MODL_FEATURE_TYPE
        UF_GDT_ERR_INVALID_MODL_PARAM
        UF_GDT_ERR_MODL_PARAM_MISMATCH

Environment: Internal  and  External
See Also:
History: Original release NX2.0.0
********************************************************************************/
extern UFUNEXPORT int UF_GDT_create_modl_based_feature(
    UF_GDT_feature_parms_p_t feat_parms,  /* <I>
                                             Tolerance feature parms
                                          */
    int *num_tol_feats,                   /* <O>
                                             Number of tolerance
                                             features created
                                          */
    tag_t **tol_feat_list                 /* <OF,len:num_tol_feats>
                                             List of tolerance
                                             features created.
                                             Use UF_free to free
                                             the memory.
                                          */
);

/******************************************************************************
Ask the modeling feature data referenced by the tolerance feature. Modeling
feature list will be NULL if the modeling features are not fully loaded.

Return:
  Return Codes -
        UF_GDT_NO_ERRORS
        UF_GDT_ERR_NOT_TOL_FEAT
        UF_err_program_not_initialized

Environment: Internal  and  External
See Also:
History: Original release NX2.0.0
********************************************************************************/
extern UFUNEXPORT int UF_GDT_ask_modl_data(
    tag_t tolerance_feature,            /* <I>
                                           Tolerance feature to set
                                        */
    int *num_modl_sets,                 /* <O>
                                           Number of model sets
                                        */
    UF_GDT_modl_data_p_t **modl_sets    /* <OF,len:num_modl_sets>
                                           Function_to_free = UF_GDT_free
                                           Modeling feature data sets.
                                           Use UF_GDT_free to free the
                                           memory.
                                        */
);

/******************************************************************************
Ask the modeling features referenced by the tolerance feature. Modeling feature
list will be NULL if the modeling features are not fully loaded.

Return:
  Return Codes -
        UF_GDT_NO_ERRORS
        UF_GDT_ERR_NOT_TOL_FEAT
        UF_err_program_not_initialized

Environment: Internal  and  External
See Also:
History: Original release NX2.0.0
 ****************************************************************************/
extern UFUNEXPORT int UF_GDT_ask_modl_features(
    tag_t tolerance_feature,  /* <I>
                                 Tolerance feature to set
                              */
    int *num_modl_features,   /* <O>
                                 Number of modeling features
                              */
    tag_t **modl_features     /* <OF,len:num_modl_features>
                                 Modeling feature list.
                                 Use UF_free to the memory.
                              */
);

/******************************************************************************
Modify the reference to the modeling feature data.

Return:
  Return Codes -
       UF_GDT_NO_ERRORS
       UF_GDT_ERR_NOT_TOL_FEAT
       UF_err_program_not_initialized
       UF_GDT_ERR_MODL_FEATURES_NOT_FULLY_LOADED
       UF_GDT_ERR_INVALID_MODL_FEATURE_TYPE
       UF_GDT_ERR_MODL_TOL_FEAT_FEATURE_TYPE_MISMATCH

Environment: Internal  and  External
See Also:
History: Original release NX2.0.0
 ****************************************************************************/
extern UFUNEXPORT int UF_GDT_set_modl_data(
    tag_t tolerance_feature,         /* <I>
                                        Tolerance feature to set
                                     */
    int num_modl_sets,               /* <I>
                                        Number of model sets
                                     */
    UF_GDT_modl_data_p_t *modl_sets  /* <I,len:num_modl_sets>
                                        Modeling feature data sets for
                                        tolerance creation
                                     */
);

/****************************************************************************
 This routine queries all the size tolerances and associated tolerance types
 on the given tolerance feature.

 NOTE: This function will not return any FCFs, to query FCFs, use function
       UF_GDT_ask_fcf_tags.

 Return Codes -
              UF_GDT_NO_ERRORS
              UF_err_program_not_initialized
              UF_GDT_ERR_NOT_TOL_FEAT

 Environment: Internal and External
 See Also:
 History: Originally released in NX2.0
 ****************************************************************************/
extern UFUNEXPORT int UF_GDT_ask_tolerances(
       tag_t tol_feat,          /* <I>The tolerance feature to inquire */
       tag_p_t * tolerances,    /* <OF,len:num_tolerances> All the tolerances associated with the feature,
                                Use UF_GDT_free to deallocate memory when done. */
       int *num_tolerances,      /* <O> Number of tolerances */
       UF_GDT_tolerance_type_p_t *types /* <OF,len:num_tolerances> The corresponding tolerance types */
);

/****************************************************************************
 This routine queries the tolerance on the tolerance feature by given type.

 Return Codes -
              UF_GDT_NO_ERRORS
              UF_err_program_not_initialized
              UF_GDT_ERR_NOT_TOL_FEAT
              UF_GDT_ERR_BAD_TOLERANCE_TYPE

 Environment: Internal and External
 See Also:
 History: Originally released in NX2.0
 ****************************************************************************/
extern UFUNEXPORT int UF_GDT_ask_tolerance(
       tag_t tol_feat,                  /* <I>The tolerance feature to inquire */
       UF_GDT_tolerance_type_t type,     /* <I> The tolerance type to inquire */
       tag_t *tolerance               /* <O>The tolerance associated with the type */

);

/****************************************************************************
 This routine queries the DFA file name on the given GDT object.

 The GDT object could be one of the following:

 Tolerance feature
 Datum Reference Frame
 Datum
 Target
 FCF
 Tolerance

 Return Codes -
              UF_GDT_NO_ERRORS
              UF_err_program_not_initialized
              UF_err_bad_parameter_number_1
              UF_err_bad_parameter_number_2

 Environment: Internal and External
 See Also:
 History: Originally released in NX2.0
 ****************************************************************************/
extern UFUNEXPORT int UF_GDT_ask_gdt_object_dfa_file(
    tag_t gdt_object,  /* <I> The GDT object to query */
    char **dfa_file     /* <OF> The DFA file name of the given object */
);

/****************************************************************************
 This routine creates tolerance features with product attributes. Please
 refer UF_PD application for details about product attributes.
 Currently, the following tolerance feature types can be created with product
 attributes -
 UF_GDT_GEAR_FEATURE
 UF_GDT_SPLINE_FEATURE

 When UF_GDT_GEAR_FEATURE feature type is passed, this routine creates a gear
 tolerance feature and its sub features.
 The created tolerance features are returned in the following order -
 Gear type tolerance feature
 Pin/Hole type tolerance feature representing pitch diameter
 Pin/Hole type tolerance feature representing major diameter
 Pin/Hole type tolerance feature representing minor diameter
 Circular Tooth Thickness type tolerance feature for external gear
 Circular Space Width type tolerance feature for internal gear
 Measurement type tolerance feature

 Following product attribute type can be specified to create a gear type
 tolerance feature -
 UF_PD_SPUR_GEAR_TYPE
 UF_PD_HELICAL_GEAR_TYPE

 When UF_GDT_SPLINE_FEATURE feature type is passed, this routine creates a
 spline tolerance feature and its sub features.
 The created tolerance features are returned in the following order -
 Spline type tolerance feature
 Pin/Hole type tolerance feature representing pitch diameter
 Pin/Hole type tolerance feature representing major diameter
 Pin/Hole type tolerance feature representing minor diameter
 Measurement type tolerance feature

 Following product attribute type can be specified to create a gear type
 tolerance feature -
 UF_PD_STRAIGHT_SIDED_SPLINE_TYPE
 UF_PD_INVOLUTE_SPLINE_TYPE

 The function does not create a display instance.

 Return Codes -
              UF_GDT_NO_ERRORS
              UF_GDT_ERR_INVALID_PRODUCT_ATTRIBUTES
              UF_err_program_not_initialized

 Environment: Internal and External
 See Also:
 History: Originally released in NX3.0
 ****************************************************************************/
extern UFUNEXPORT int UF_GDT_create_feature_with_product_att(
    UF_GDT_feature_parms_p_t feat_parms,      /* <I>
                                                 Tolerance feature parms
                                              */
    UF_GDT_product_attribute_p_t uf_atts,     /* <I>
                                                 Product attributes data
                                              */
    int *num_tol_feats,                       /* <O>
                                                 Number of tolerance
                                                 features created
                                              */
    tag_t **tol_feat_list                    /* <OF,len:num_tol_feats>
                                                List of tolerance
                                                features created.
                                                Use UF_free to free
                                                the memory.
                                             */
);

/****************************************************************************
 This routine queries the product attributes of the tolerance feature.
 Currently, only the Spline and Gear type tolerance features have product
 attributes.

 Please refer UF_PD application for details about the product attributes.
 Return Codes -
              UF_GDT_NO_ERRORS
              UF_err_program_not_initialized

 Environment: Internal and External
 See Also:
 History: Originally released in NX3.0
 ****************************************************************************/
extern UFUNEXPORT int UF_GDT_ask_product_attributes(
    tag_t tolerance_feature,      /* <I>
                                     Tolerance feature to query
                                  */
    int *num_product_atts,        /* <O>
                                     Number of product attributes
                                  */
    tag_t **product_atts          /* <OF,len:num_product_atts>
                                     List of product attributes
                                  */
);

/****************************************************************************
 This routine returns the sub feature representing the pitch diameter of the
 spline/gear tolerance feature.

 Return Codes -
              UF_GDT_NO_ERRORS
              UF_err_program_not_initialized

 Environment: Internal and External
 See Also:
 History: Originally released in NX3.0
 ****************************************************************************/
extern UFUNEXPORT int UF_GDT_ask_pitch_dia_feature_of_spline_gear(
    tag_t tolerance_feature,     /* <I>
                                    Spline/Gear tolerance
                                    feature to query
                                 */
    tag_t *pitch_dia_feature    /* <O>
                                   Sub feature representing the
                                   pitch diameter of the spline/
                                   gear tolerance feature
                                */
);

/****************************************************************************
 This routine returns the sub feature representing the major diameter of the
 spline/gear tolerance feature.

 Return Codes -
              UF_GDT_NO_ERRORS
              UF_err_program_not_initialized

 Environment: Internal and External
 See Also:
 History: Originally released in NX3.0
 ****************************************************************************/
extern UFUNEXPORT int UF_GDT_ask_major_dia_feature_of_spline_gear(
    tag_t tolerance_feature,     /* <I>
                                    Spline/Gear tolerance
                                    feature to query
                                 */
    tag_t *major_dia_feature    /* <O>
                                   Sub feature representing the
                                   major diameter of the spline/
                                   gear tolerance feature
                                */
);

/****************************************************************************
 This routine returns the sub feature representing the minor diameter of the
 spline/gear tolerance feature.

 Return Codes -
              UF_GDT_NO_ERRORS
              UF_err_program_not_initialized

 Environment: Internal and External
 See Also:
 History: Originally released in NX3.0
 ****************************************************************************/
extern UFUNEXPORT int UF_GDT_ask_minor_dia_feature_of_spline_gear(
    tag_t tolerance_feature,     /* <I>
                                    Spline/Gear tolerance
                                    feature to query
                                 */
    tag_t *minor_dia_feature    /* <O>
                                   Sub feature representing the
                                   minor diameter of the spline/
                                   gear tolerance feature
                                */
);

/******************************************************************************
 This routine creates a table instance of a tolerance feature. The table
 instance references a tabular note and displays the tolerance feature data in
 the table format.

 Following tolerance feature types can have a table instance -
 UF_GDT_SPLINE_FEATURE
 UF_GDT_GEAR_FEATURE

 Please refer UF_TABNOT application for a detailed description of tabular notes.

 Return Codes -
              UF_GDT_NO_ERRORS
              UF_err_program_not_initialized

 Environment: Internal  and  External
 See Also:
 History:Original release was in NX3.0
 * ******************************************************************************/
extern UFUNEXPORT int UF_GDT_create_table_instance(
    tag_t  tolerance_feature, /* <I>
                                 Referenced tolerance feature
                              */
    tag_t view,              /* <I>
                                Tag of the view where the instance is
                                displayed
                             */
    double origin[3],        /* <I>
                                Location of instance origin
                             */

    tag_t *feature_instance  /* <O>
                                Identification tag of created feature
                                instance
                             */
);

/******************************************************************************
 This routine returns the table of the instance. The table is a type of tabular
 note.

 Please refer UF_TABNOT application for a detailed description of tabular notes.

 Return Codes -
              UF_GDT_NO_ERRORS
              UF_err_program_not_initialized

 Environment: Internal  and  External
 See Also:
 History:Original release was in NX3.0
 * ******************************************************************************/
extern UFUNEXPORT int UF_GDT_ask_table_of_instance(
    tag_t  feature_instance, /* <I>
                                Instance of tolerance feature
                              */
    tag_t *table            /* <O>
                                 Identification tag of table referenced
                                 by the instance
                             */
);

/************************************************************************
This routine exports the given set of drawings as well as their
embedded GD&T to the given part.

PLEASE NOTE THE FOLLOWING WHEN USING THIS ROUTINE:

- The export will retain parametrics but will NOT export referenced
  objects just to accomplish this. This mimics the
  UF_PART_maintain_parms part export option.
- The export will deeply copy expressions. This mimics the
  UF_PART_copy_exp_deeply part export option.
- The export will load any parts needed to resolve references ON
  DEMAND.

Return Codes -
              UG_GDT_NO_ERRORS
              PART_err_failed_to_load_part

Environment : Internal  and  External
See also:
History: Created in v16.0.3
************************************************************************/
extern UFUNEXPORT int UF_GDT_export_drawings(
    int num_drawings,           /* <I>
                                Number of drawings to export
                                */
    tag_p_t drawings,           /* <I,len:num_drawings>
                                Array of drawing tags to export
                                */
    tag_t target_part           /* <I>
                                Target part for the export operation
                                */
);

#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif   /* UF_GDT_H_INCLUDED */
