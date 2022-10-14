/*******************************************************************************
             Copyright (c) 2003 Unigraphics Solutions, Inc.
                       Unpublished - All Rights Reserved



File description:
This include file contains the Open C API of the VDA Checker.
The routines specified in this file enable you to access a Compliance Error Objects (*.ceo) file
containing an error report of a VDA Checker run.
Using the routines you can:

    .   Load comply errors from a *.ceo file of the work part.

    .   Ask for those check criteria of a VDA Checker class that diagnosed faulty objects.

    .   Ask for all comply error items of a given check criterion key.

    .   Ask for a list of object identifiers for a given check criterion key.

    .   Ask for all criteria violations of a faulty object.

    .   Ask for a list of object identifiers of all faulty objects diagnosed.

    .   Manipulate the identified faulty objects.

If the VDA Checker diagnoses a violation of some check criterion, a Comply Error Item is generated.
It contains information about the fautly object(s) and the violation condition.
Comply Error Items (UF_VDAC_ce_item_t) for the same (unique) check criterion key are kept in a list
and are delivered in a UF_VDAC_ce_t structure.
Check criterion keys are grouped into comply error object classes (UF_VDAC_class_e_t).
Class specific check criterion keys (cckey) are defined as UF_VDAC_CCKEY_<specific_key> somewhere bolow.
A check criterion key (cckey) is unique regardless of the owning class.
Check criterion key info is available in UF_VDAC_cckey_t.

*******************************************************************************/

#ifndef UF_VDAC_H_INCLUDED
#define UF_VDAC_H_INCLUDED

/*==========================================================================

  ==========================================================================*/

#include <uf_defs.h>
#include <uf_obj_types.h>
#include <libufun_vdac_exports.h>

/*---------------- Data Structure Section -----------------------------------*/

/* comply errors evaluator structure */
typedef struct       UF_VDAC_ceos_S *UF_VDAC_ceos_p_t;
typedef const struct UF_VDAC_ceos_S *UF_VDAC_ceos_pc_t;

/* NX/Open versions of comply error interface */
enum UF_VDAC_ce_vers_e
{
    UF_VDAC_ce_vers_none,
    UF_VDAC_ce_vers_vdac2,        /* VDA Checker version 2 data format */
    UF_VDAC_ce_vers_item_count,
    UF_VDAC_ce_vers_illegal = -1  /* For QAZ purposes only */
};
typedef enum UF_VDAC_ce_vers_e UF_VDAC_ce_vers_e_t, *UF_VDAC_ce_vers_e_p_t;
typedef const UF_VDAC_ce_vers_e_t UF_VDAC_ce_vers_e_c_t, *UF_VDAC_ce_vers_e_pc_t;

/* Version 2 comply error object classes */
enum UF_VDAC_class_e
{
    UF_VDAC_class_curves,
    UF_VDAC_class_faces,
    UF_VDAC_class_solids,
    UF_VDAC_class_drawings,
    UF_VDAC_class_model_errors,
    UF_VDAC_class_item_count,
    UF_VDAC_class_illegal = -1  /* For QAZ purposes only */
};
typedef enum UF_VDAC_class_e UF_VDAC_class_e_t, *UF_VDAC_class_e_p_t;
typedef const UF_VDAC_class_e_t UF_VDAC_class_e_c_t, *UF_VDAC_class_e_pc_t;


/* ----- Version 2 check criterion keys BEGIN ----- */


/*
UF_VDAC_class_curves
*/
#define UF_VDAC_CCKEY_M1c  "M1c"   /* Tiny Curve */
#define UF_VDAC_CCKEY_M1cs "M1cs"  /* Tiny Curve Segment */
#define UF_VDAC_CCKEY_M1e  "M1e"   /* Tiny Edge Curve */
#define UF_VDAC_CCKEY_M1es "M1es"  /* Tiny Edge Curve Segment */
#define UF_VDAC_CCKEY_M2c  "M2c"   /* Identical Curve */
#define UF_VDAC_CCKEY_M3ac "M3ac"  /* Gap/Overlap; Curve */
#define UF_VDAC_CCKEY_M3bc "M3bc"  /* Tangent Angle; Curve */
#define UF_VDAC_CCKEY_M3cc "M3cc"  /* Curvature; Curve */
#define UF_VDAC_CCKEY_M3ae "M3ae"  /* Gap/Overlap; Edge */
#define UF_VDAC_CCKEY_M3be "M3be"  /* Tangent Angle; Edge */
#define UF_VDAC_CCKEY_M3ce "M3ce"  /* Curvature; Edge */
#define UF_VDAC_CCKEY_U3bc "U3bc"  /* Tangent Angle Segment; Curve */
#define UF_VDAC_CCKEY_U3cc "U3cc"  /* Curvature Segment; Curve */
#define UF_VDAC_CCKEY_U3be "U3be"  /* Tangent Angle Segment; Edge */
#define UF_VDAC_CCKEY_U3ce "U3ce"  /* Curvature Segment; Edge */
#define UF_VDAC_CCKEY_M4c  "M4c"   /* Maximum Degree; Curve */
#define UF_VDAC_CCKEY_M4e  "M4e"   /* Maximum Degree; Edge */
#define UF_VDAC_CCKEY_M5c  "M5c"   /* Ripple; Curve */
#define UF_VDAC_CCKEY_M6c  "M6c"   /* Multiple Knots; Curve */
#define UF_VDAC_CCKEY_M6e  "M6e"   /* Multiple Knots; Edge */
#define UF_VDAC_CCKEY_C7c  "C7c"   /* Self Intersection; Curve */
#define UF_VDAC_CCKEY_U7c  "U7c"   /* Spike/Cut Angle; Curve */

/*
UF_VDAC_class_faces
*/
#define UF_VDAC_CCKEY_M1pa "M1pa"  /* Tiny Patch Absolute */
#define UF_VDAC_CCKEY_M1pr "M1pr"  /* Tiny Patch Relative */
#define UF_VDAC_CCKEY_M1sf "M1sf"  /* Tiny Surface */
#define UF_VDAC_CCKEY_M1f  "M1f"   /* Tiny Face Area */
#define UF_VDAC_CCKEY_U1f  "U1f"   /* Tiny Sliver Face */
#define UF_VDAC_CCKEY_M2sf "M2sf"  /* Identical Surface; Embedded surface: G-SU-EM */
#define UF_VDAC_CCKEY_M2f  "M2f"   /* Identical Face */
#define UF_VDAC_CCKEY_M3af "M3af"  /* Gap/Overlap; Face */
#define UF_VDAC_CCKEY_M3bf "M3bf"  /* Tangent Angle; Face */
#define UF_VDAC_CCKEY_M3cf "M3cf"  /* Curvature; Face */
#define UF_VDAC_CCKEY_U3bp "U3bp"  /* Tangent Angle Segment; Patch */
#define UF_VDAC_CCKEY_U3cp "U3cp"  /* Curvature Segment; Patch */
#define UF_VDAC_CCKEY_M4sf "M4sf"  /* Maximum Degree; Surface */
#define UF_VDAC_CCKEY_M5sf "M5sf"  /* Ripple; Surface */
#define UF_VDAC_CCKEY_M6s  "M6s"   /* Multiple Knots; Surface */
#define UF_VDAC_CCKEY_SU8  "SU8"   /* Degenerate Boundary  */
#define UF_VDAC_CCKEY_SU9  "SU9"   /* Minimum Radius */
#define UF_VDAC_CCKEY_SU10 "SU10"  /* Corner Angle between Boundary Curves */
#define UF_VDAC_CCKEY_SU11 "SU11"  /* Normal Flapping Angle */
#define UF_VDAC_CCKEY_SU12 "SU12"  /* Patch Count */
#define UF_VDAC_CCKEY_SU13 "SU13"  /* Unused Patch Row */
#define UF_VDAC_CCKEY_F14  "F14"   /* Self Intersection; Face */
#define UF_VDAC_CCKEY_U14  "U14"   /* Spike/Cut Angle; Face */
#define UF_VDAC_CCKEY_F15  "F15"   /* Edge-Curve Surface Distance */
#define UF_VDAC_CCKEY_F16  "F16"   /* Edge Orientation */
#define UF_VDAC_CCKEY_U16  "U16"   /* Closed Loop */
#define UF_VDAC_CCKEY_F17  "F17"   /* Edge-Curve Segment Count */
#define UF_VDAC_CCKEY_T18  "T18"   /* Overused Edge */
#define UF_VDAC_CCKEY_T19  "T19"   /* Reversed Normal */
#define UF_VDAC_CCKEY_T20  "T20"   /* Sharp Face Angle */

/*
UF_VDAC_class_solids
*/
#define UF_VDAC_CCKEY_M1s  "M1s"   /* Tiny Solid */
#define UF_VDAC_CCKEY_M1v  "M1v"   /* Tiny Volume */
#define UF_VDAC_CCKEY_M2s  "M2s"   /* M2s */
#define UF_VDAC_CCKEY_SO21 "SO21"  /* Vertex - Edge Distance */
#define UF_VDAC_CCKEY_SO22 "SO22"  /* Vertex - Face Distance */
#define UF_VDAC_CCKEY_SO23 "SO23"  /* Missing Solid History */
#define UF_VDAC_CCKEY_SO24 "SO24"  /* Unused Solid Construction History, G-SO-UH */
#define UF_VDAC_CCKEY_SO25 "SO25"  /* Unintentional Cavity, G-SO-VO */
#define UF_VDAC_CCKEY_SO26 "SO26"  /* Multi-Body Solid */
#define UF_VDAC_CCKEY_SO27 "SO27"  /* Multi-Solid Part */

/*
UF_VDAC_class_drawings
*/
#define UF_VDAC_CCKEY_D28  "D28"   /* Font */
#define UF_VDAC_CCKEY_U28a "U28a"  /* Maximum Text Length */
#define UF_VDAC_CCKEY_U28b "U28b"  /* Multi-Line Text */
#define UF_VDAC_CCKEY_U28c "U28c"  /* International Character */

/*
UF_VDAC_class_model_errors
*/
#define UF_VDAC_CCKEY_UG99 "UG99"  /* Model Error */

/* ----- Version 2 check criterion keys END ----- */

/* Version 2 Modeler Error object classes */
enum UF_VDAC_me_class_e
{
    UF_VDAC_me_class_curves,
    UF_VDAC_me_class_faces,
    UF_VDAC_me_class_solids,
    UF_VDAC_me_class_drawings,
    UF_VDAC_me_class_evaluation,
    UF_VDAC_me_class_item_count
};
typedef enum UF_VDAC_me_class_e UF_VDAC_me_class_e_t, *UF_VDAC_me_class_e_p_t;
typedef const UF_VDAC_me_class_e_t UF_VDAC_me_class_e_c_t, *UF_VDAC_me_class_e_pc_t;

/* union of item value types */
union UF_VDAC_item_u
{
    double          dval;       /* type double */
    int             ival;       /* type integer */
    const double*   dval_pc;    /* address of type constant double */
    const int*      ival_pc;    /* address of type constant integer */

};
typedef union UF_VDAC_item_u UF_VDAC_item_u_t, *UF_VDAC_item_u_p_t;
typedef const union UF_VDAC_item_u UF_VDAC_item_u_c_t, *UF_VDAC_item_u_pc_t;

struct UF_VDAC_point_s
{
    double  xyz[3]; /* 3D point / vertex, x,y,z coordinates, xyz[2] = z-coordinate */

};
typedef struct UF_VDAC_point_s UF_VDAC_point_t, *UF_VDAC_point_p_t;
typedef const struct UF_VDAC_point_s UF_VDAC_point_c_t, *UF_VDAC_point_pc_t;

/* Definition for 3-D vector */
struct UF_VDAC_vec3_s
{
    double  v3[3];
};
typedef struct UF_VDAC_vec3_s UF_VDAC_vec3_t, *UF_VDAC_vec3_p_t;
typedef const struct UF_VDAC_vec3_s UF_VDAC_vec3_c_t, *UF_VDAC_vec3_pc_t;

/* Comply error parametric point info */
struct UF_VDAC_ce_point_s
{
    double          params[2];  /* u and v parameters of point3 */
    UF_VDAC_point_t point3;     /* 3D coordinates of worst case */
    UF_VDAC_vec3_t  uvector;    /* (unit) vector */
    tag_t           ug_eid;     /* object identifier */
};
typedef struct UF_VDAC_ce_point_s UF_VDAC_ce_point_t  , *UF_VDAC_ce_point_p_t;
typedef const struct UF_VDAC_ce_point_s UF_VDAC_ce_point_c_t, *UF_VDAC_ce_point_pc_t;

/* Comply error Geometric Continuity Parameters */
struct UF_VDAC_ce_gc_par_s
{
    UF_VDAC_ce_point_t  ce_point[2];
};
typedef struct UF_VDAC_ce_gc_par_s UF_VDAC_ce_gc_par_t  , *UF_VDAC_ce_gc_par_p_t;
typedef const struct UF_VDAC_ce_gc_par_s UF_VDAC_ce_gc_par_c_t, *UF_VDAC_ce_gc_par_pc_t;

/* Modeler Error comply error info */
struct UF_VDAC_ce_me_par_s
{
    UF_VDAC_ce_point_t      ptpar;          /* optional point on failing objects */
    UF_VDAC_me_class_e_t    me_class;       /* Modeler Error object class */
    UF_VDAC_class_e_t       comply_class;   /* .. of active check criterion */
    int                     item;           /* .. of active check criterion (VDAC_crit_<comply_error>) */

};
typedef struct UF_VDAC_ce_me_par_s UF_VDAC_ce_me_par_t  , *UF_VDAC_ce_me_par_p_t;
typedef const struct UF_VDAC_ce_me_par_s UF_VDAC_ce_me_par_c_t, *UF_VDAC_ce_me_par_pc_t;

/* Union of comply error parameters */
union UF_VDAC_ce_par_u
{
    UF_VDAC_ce_gc_par_t gcpar;  /* Comply error Geometric Continuity Parameters */
    UF_VDAC_ce_me_par_t mepar;  /* Modeler Error comply error info */
    UF_VDAC_ce_point_t  ptpar;  /* Comply error parametric point info */

};
typedef union UF_VDAC_ce_par_u UF_VDAC_ce_par_u_t  , *UF_VDAC_ce_par_u_p_t;
typedef const union UF_VDAC_ce_par_u UF_VDAC_ce_par_u_c_t, *UF_VDAC_ce_par_u_pc_t;


/* toggles that describe an VDAC_item_t item */
struct UF_VDAC_item_options_s
{
    unsigned int    log_violations:1;   /* generate detailed criteria report */

    unsigned int    has_no_item_value:1;    /* the item has no check value; log no error value */
    unsigned int    is_integer_item:1;
    unsigned int    is_absolute_value:1;
    unsigned int    is_degree_value:1;      /* an angle [degree] */
    unsigned int    is_distance_value:1;    /* a distance;  usually [mm]    or [inch] */
    unsigned int    is_area_value:1;        /* an area;     usually [mm**2] or [inch**2] */
    unsigned int    is_volume_value:1;      /* an volume;   usually [mm**3] or [inch**3] */

    unsigned int    has_two_object_ids:1;   /* log two tags */
    unsigned int    is_object_edge_eid:1;   /* to distinguish an edge curve from a curve tag */
    unsigned int    is_object_id2_feat:1;   /* object_id2 represents a feature component */
    unsigned int    has_two_ce_values:1;    /* log two error values */
    unsigned int    is_font:1;              /* value is a font number */

    unsigned int    el_gcpar:1;     /* two point entries */
    unsigned int    el_ptpar:1;     /* one point entry */
    unsigned int    el_uv_pair:1;   /* log uv parameter pair */
    unsigned int    el_vector:1;    /* log vector variant of el_gcpar or el_ptpar */

};
typedef struct UF_VDAC_item_options_s UF_VDAC_item_options_t, *UF_VDAC_item_options_p_t;
typedef const struct UF_VDAC_item_options_s UF_VDAC_item_options_c_t, *UF_VDAC_item_options_pc_t;

/* Comply Error Item */
struct UF_VDAC_ce_item_s
{
    tag_t                   object_id;      /* object id of failing object */
    tag_t                   object_id2;     /* adjacent object id if any */
    UF_VDAC_item_u_t        value;          /* failing constraint value */
    UF_VDAC_item_u_t        value2;         /* failing constraint value2 */
    UF_VDAC_item_options_t  ce_options;     /* description of error case */
    UF_VDAC_ce_par_u_t      par;            /* diagnose parameters */

};
typedef struct UF_VDAC_ce_item_s UF_VDAC_ce_item_t, *UF_VDAC_ce_item_p_t;
typedef const struct UF_VDAC_ce_item_s UF_VDAC_ce_item_c_t, *UF_VDAC_ce_item_pc_t;

/* comply error check criterion key info */
struct UF_VDAC_cckey_s
{
    UF_VDAC_item_u_t        ceh_value;      /* check value */
    UF_VDAC_class_e_t       comply_class;   /* comply error object class */
    const char*             cckey;          /* VDA Checker comply error check criterion key */
    const char*             item_name;      /* criterion name */
    int                     violations;     /* number of violations */
    UF_VDAC_item_options_t  ceh_options;    /* item description */

};
typedef struct UF_VDAC_cckey_s UF_VDAC_cckey_t, *UF_VDAC_cckey_p_t;
typedef const struct UF_VDAC_cckey_s UF_VDAC_cckey_c_t, *UF_VDAC_cckey_pc_t;

/* comply error object class check criterion key info */
struct UF_VDAC_class_info_s
{
    UF_VDAC_class_e_t   comply_class;   /* comply error object class */
    int                 num_infos;      /* number of check criterion keys with violations
                                           size of array item_infos */
    UF_VDAC_cckey_pc_t  key_infos;      /* array of comply error check criterion key infos */

};
typedef struct UF_VDAC_class_info_s UF_VDAC_class_info_t  , *UF_VDAC_class_info_p_t;
typedef const struct UF_VDAC_class_info_s UF_VDAC_class_info_c_t, *UF_VDAC_class_info_pc_t;

/* comply errors of a check criterion key */
struct UF_VDAC_ce_s
{
    UF_VDAC_cckey_t         key_info;   /* comply error check criterion key info */
    int                     item_count; /* number of comply error items size of array items */
    UF_VDAC_ce_item_pc_t    items;      /* array of comply error items */

};
typedef struct UF_VDAC_ce_s UF_VDAC_ce_t  , *UF_VDAC_ce_p_t;
typedef const struct UF_VDAC_ce_s UF_VDAC_ce_c_t, *UF_VDAC_ce_pc_t;



typedef struct UF_VDAC_list_s UF_VDAC_list_t, *UF_VDAC_list_p_t;
/*
linked list of Object Identifiers
*/
struct UF_VDAC_list_s
{
    UF_VDAC_list_p_t    next;   /* Pointer to the next list member */
    tag_t               eid;    /* Object Identifier */
};
typedef const struct UF_VDAC_list_s UF_VDAC_list_c_t, *UF_VDAC_list_pc_t;

typedef struct       UF_VDAC_list_lh_S *UF_VDAC_list_lh_p_t;
typedef const struct UF_VDAC_list_lh_S *UF_VDAC_list_lh_pc_t;

/* Object Identifier list head */
struct UF_VDAC_list_head_s
{
    UF_VDAC_list_lh_p_t lh_p;   /* address of VDAC list header */
    UF_VDAC_list_pc_t   first;  /* address of first linked list member or NULL */
    int                 count;  /* number of list members */

};
typedef struct UF_VDAC_list_head_s UF_VDAC_list_head_t, *UF_VDAC_list_head_p_t;
typedef const struct UF_VDAC_list_head_s UF_VDAC_list_head_c_t, *UF_VDAC_list_head_pc_t;

/* Faulty Objects of comply error items of a check criterion key */
struct UF_VDAC_cckey_fo_s
{
    UF_VDAC_cckey_t     key_info;   /* comply error check criterion key info */
    UF_VDAC_list_head_t list_head;  /* Object Identifier list head */
};
typedef struct UF_VDAC_cckey_fo_s UF_VDAC_cckey_fo_t, *UF_VDAC_cckey_fo_p_t;
typedef const struct UF_VDAC_cckey_fo_s UF_VDAC_cckey_fo_c_t, *UF_VDAC_cckey_fo_pc_t;

/* Check Criterion Key Comply Error Item */
struct UF_VDAC_cckey_ce_item_s
{
    UF_VDAC_cckey_t     key_info;   /* comply error check criterion key info */
    UF_VDAC_ce_item_t   ce_item;    /* Comply Error Item */
    char                crit_name[ UF_OBJ_NAME_BUFSIZE ];   /* criterion name */

};
typedef struct UF_VDAC_cckey_ce_item_s UF_VDAC_cckey_ce_item_t, *UF_VDAC_cckey_ce_item_p_t;
typedef const struct UF_VDAC_cckey_ce_item_s UF_VDAC_cckey_ce_item_c_t, *UF_VDAC_cckey_ce_item_pc_t;

/* Faulty Object Check Criterion Key Comply Errors */
struct UF_VDAC_fo_ce_s
{
    tag_t                       faulty;     /* faulty object iddentifier */
    int                         crit_count; /* number of violated criteria */
    UF_VDAC_cckey_ce_item_pc_t  criteria;   /* array of criteria with violations */

};
typedef struct UF_VDAC_fo_ce_s UF_VDAC_fo_ce_t  , *UF_VDAC_fo_ce_p_t;
typedef const struct UF_VDAC_fo_ce_s UF_VDAC_fo_ce_c_t, *UF_VDAC_fo_ce_pc_t;

/* faulty object types */
enum UF_VDAC_fo_type_e
{
    UF_VDAC_fo_type_none,
    UF_VDAC_fo_type_curve,
    UF_VDAC_fo_type_edge,
    UF_VDAC_fo_type_face,
    UF_VDAC_fo_type_feature,
    UF_VDAC_fo_type_solid,
    UF_VDAC_fo_type_item_count
};
typedef enum UF_VDAC_fo_type_e UF_VDAC_fo_type_e_t  , *UF_VDAC_fo_type_e_p_t;
typedef const UF_VDAC_fo_type_e_t UF_VDAC_fo_type_e_c_t, *UF_VDAC_fo_type_e_pc_t;

typedef struct UF_VDAC_fo_neighbor_s UF_VDAC_fo_neighbor_t, *UF_VDAC_fo_neighbor_p_t;
/*
Linked List Item of neighbors of a faulty object
*/
struct UF_VDAC_fo_neighbor_s
{
    UF_VDAC_fo_neighbor_p_t next;
    tag_t                   neighbor;   /* neighbor object identifier */
    UF_VDAC_fo_type_e_t     fo_type;    /* type of neighbor object */
};
typedef const struct UF_VDAC_fo_neighbor_s UF_VDAC_fo_neighbor_c_t, *UF_VDAC_fo_neighbor_pc_t;

/* Faulty Object Neighbors Info */
struct UF_VDAC_fo_neighbors_s
{
    tag_t                       faulty;     /* faulty object identifier */
    UF_VDAC_fo_type_e_t         fo_type;    /* faulty object type */
    UF_VDAC_class_e_t           oclass;     /* comply error object class */
    UF_VDAC_fo_neighbor_pc_t    first;      /* address of first linked list neighbor member or NULL */
    int                         count;      /* number of list members */

};
typedef struct UF_VDAC_fo_neighbors_s UF_VDAC_fo_neighbors_t  , *UF_VDAC_fo_neighbors_p_t;
typedef const struct UF_VDAC_fo_neighbors_s UF_VDAC_fo_neighbors_c_t, *UF_VDAC_fo_neighbors_pc_t;

typedef struct UF_VDAC_text_list_s UF_VDAC_text_list_t, *UF_VDAC_text_list_p_t;
/*
linked list of text strings
*/
struct UF_VDAC_text_list_s
{
    UF_VDAC_text_list_p_t   next;           /* pointer to the next list member or NULL */
    const char*             text;           /* text pointer */
    int                     text_length;    /* text length: number of characters in string,
                                               excluding the '\0' terminator */
};
typedef const struct UF_VDAC_text_list_s UF_VDAC_text_list_c_t, *UF_VDAC_text_list_pc_t;

/*---------------- Function Prototypes Section -------------------------------*/

#ifdef __cplusplus
extern "C" {
#endif

/*
>>>>>>>>>  Initialization / Termination Functions  <<<<<<<<<<<<<<<<<<<<<<<<<<<<
*/

/******************************************************************************
Initializes comply errors evaluator structure.
Loads comply errors from *.ceo file of the work part.

Environment: Internal  and  External

See Also:   UF_VDAC_free_ceo

History:
 *****************************************************************************/
extern UFUN_VDACEXPORT int UF_VDAC_load_ceo
(
    const char*         ceo_file_name,  /* <I>  Compliance Error Objects file name, optional
                                                This file contains the session independent
                                                compliance error lists.
                                                If NULL is specified the actual file name (*.ceo)
                                                is derived from the part file name
                                                and has to be located in the same directory
                                                as the part file */
    const char*         log_file_name,  /* <I>  Optional log file name
                                                This file contains useful info in case of errors
                                                If NULL is specified the actual file name (*.log)
                                                is derived from the part file name
                                                and ends with *_uf_vdac.log
                                                and has to be located in the same directory
                                                as the part file */
    UF_VDAC_ce_vers_e_t api_version,    /* <I>  NX/Open version of comply error interface */
    UF_VDAC_ceos_p_t*   ceos            /* <OF,free:UF_VDAC_free_ceo> Address of Comply Errors Evaluator structure pointer.
                                                It must be freed by calling UF_VDAC_free_ceo. */
);

/******************************************************************************
Frees the Comply Errors Evaluator structure.
All object data that the NX/Open application asked for are invalid after this call.

Environment: Internal  and  External

See Also:   UF_VDAC_load_ceo

History:
 *****************************************************************************/
extern UFUN_VDACEXPORT int UF_VDAC_free_ceo
(
    UF_VDAC_ceos_p_t*   ceos    /* <I/O> address of comply errors evaluator structure pointer
                                        *ceos is set to NULL. */
);

/******************************************************************************
Returns the log and error log text list of the VDA module.
The text list is invalidated by a UF_VDAC_free_ceo call.
This function is intended to include logging information of the VDA module
in the log of the NX/Open application.

Environment: Internal  and  External

See Also:   UF_VDAC_load_ceo
            UF_VDAC_free_ceo

History:
 *****************************************************************************/
extern UFUN_VDACEXPORT int UF_VDAC_ask_log_text_list
(
    UF_VDAC_ceos_pc_t               ceop,   /* <I> comply errors evaluator structure pointer */
    UF_VDAC_text_list_pc_t* const   first,  /* <O> address of pointer to first text list item */
    int*                    const   count   /* <O> address of number of text list items or NULL */
);

/*
>>>>>>>>>  Comply Error Data Access Functions  <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
*/

/******************************************************************************
Returns all comply error items of a given check criterion key.

Environment: Internal  and  External

See Also:   UF_VDAC_load_ceo
            UF_VDAC_ask_class_info

History:
 *****************************************************************************/
extern UFUN_VDACEXPORT int UF_VDAC_ask_cckey_comply_errors
(
    UF_VDAC_ceos_pc_t       ceop,           /* <I> comply errors evaluator structure pointer */
    UF_VDAC_class_info_pc_t class_info,     /* <I> address of comply error class info */
    int                     info_index,     /* <I> class info index
                                                   range( 0, class_info->num_infos - 1) */
    UF_VDAC_ce_p_t const    ce              /* <O> address of comply error descriptor */
);

/******************************************************************************
Returns information about the number of criteria of a VDA Checker class that produced comply errors.

Environment: Internal  and  External

See Also:   UF_VDAC_load_ceo

History:
 *****************************************************************************/
extern UFUN_VDACEXPORT int UF_VDAC_ask_class_info
(
    UF_VDAC_ceos_pc_t               ceop,           /* <I> comply errors evaluator structure pointer */
    UF_VDAC_class_e_t               comply_class,   /* <I> comply error object class */
    UF_VDAC_class_info_p_t const    class_info      /* <O> address of comply error class info */
);

/******************************************************************************
Returns all comply errors of a faulty object.

Environment: Internal  and  External

See Also:   UF_VDAC_load_ceo
            UF_VDAC_ask_cckey_comply_errors
            UF_VDAC_ask_cckey_fo_list
            UF_VDAC_ask_class_info
            UF_VDAC_ask_fo_list

History:
 *****************************************************************************/
extern UFUN_VDACEXPORT int UF_VDAC_ask_fo_comply_errors
(
    UF_VDAC_ceos_pc_t       ceop,   /* <I> comply errors evaluator structure pointer */
    tag_t                   faulty, /* <I> faulty object identifier */
    UF_VDAC_fo_ce_p_t const ce_obj  /* <O> address of Faulty Object Check Criterion Key Comply Errors
                                           or NULL if none. */
);

/*
>>>>>>>>>  Faulty Object Info Functions  <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
*/

/******************************************************************************
Returns a list of faulty object identifiers for a given check criterion key.

Environment: Internal  and  External

See Also:   UF_VDAC_load_ceo
            UF_VDAC_ask_class_info
            UF_VDAC_delete_list_members

History:
 *****************************************************************************/
extern UFUN_VDACEXPORT int UF_VDAC_ask_cckey_fo_list
(
    UF_VDAC_ceos_pc_t           ceop,       /* <I> comply errors evaluator structure pointer */
    UF_VDAC_class_info_pc_t     class_info, /* <I> address of comply error class info */
    int                         info_index, /* <I> class info index
                                                   range( 0, class_info->ce_count - 1) */
    UF_VDAC_cckey_fo_p_t const  fo_list     /* <O> address of faulty object identifier list */
);

/******************************************************************************
Returns a list of all faulty object identifiers.

Environment: Internal  and  External

See Also:   UF_VDAC_load_ceo
            UF_VDAC_ask_fo_comply_errors

History:
 *****************************************************************************/
extern UFUN_VDACEXPORT int UF_VDAC_ask_fo_list
(
    UF_VDAC_ceos_pc_t           ceop,   /* <I> comply errors evaluator structure pointer */
    UF_VDAC_list_pc_t* const    first,  /* <O> address of pointer to first list item */
    int*               const    count   /* <O> address of number of list items or NULL */
);

/******************************************************************************
Returns a list of neighbor object identifiers for a given faulty object.

Environment: Internal  and  External

See Also:   UF_VDAC_load_ceo
            UF_VDAC_ask_cckey_fo_list
            UF_VDAC_ask_fo_list

History:
 *****************************************************************************/
extern UFUN_VDACEXPORT int UF_VDAC_ask_fo_neighbors
(
    UF_VDAC_ceos_pc_t               ceop,           /* <I> comply errors evaluator structure pointer */
    tag_t                           faulty,         /* <I> faulty object identifier */
    UF_VDAC_fo_neighbors_p_t const  fo_neighbors    /* <O> address of Faulty Object Neighbors Info */
);

/******************************************************************************
Deletes all members of a object identifier list.

Environment: Internal  and  External

See Also:   UF_VDAC_load_ceo
            UF_VDAC_ask_cckey_fo_list

History:
 *****************************************************************************/
extern UFUN_VDACEXPORT int UF_VDAC_delete_list_members
(
    UF_VDAC_ceos_pc_t           ceop,   /* <I> comply errors evaluator structure pointer */
    UF_VDAC_list_head_p_t const lh      /* <I/O> address of Object Identifier list head */
);

#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif /* UF_VDAC_H_INCLUDED */
