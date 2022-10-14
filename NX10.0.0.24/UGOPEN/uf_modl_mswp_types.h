/*==================================================================================================

                    Copyright (c) 2002-2005 Unigraphics Solutions Inc. 
                             Unpublished - All rights reserved
====================================================================================================


File description:

    Sweep (MSWP) data structures and types

==================================================================================================*/

#ifndef UF_MODL_MSWP_TYPES_H_INCLUDED
#define UF_MODL_MSWP_TYPES_H_INCLUDED

/*==========================================================================

==========================================================================*/
#include <uf_modl_types.h>

#ifdef __cplusplus
extern "C" {
#endif

/* Data definitions for limits including trimming */
typedef enum
{  
    UF_MODL_MSWP_LIMIT_DISTANCE = 0,      /* DISTANCE limit */
    UF_MODL_MSWP_LIMIT_UNTIL_NEXT,        /* UNITIL_NEXT limit */
    UF_MODL_MSWP_LIMIT_UNTIL_SELECTED,    /* UNTIL_SELECTED limit */
    UF_MODL_MSWP_LIMIT_THRU_ALL           /* THRU_ALL limit */
} UF_MODL_mswp_limit_type_t;

/* Single expression data that can be used by distance, angle, etc. */
struct UF_MODL_mswp_string_data_s
{
    char   string[ UF_MAX_EXP_BUFSIZE ];
    tag_t  expression_tag;
};
typedef struct UF_MODL_mswp_string_data_s
               UF_MODL_mswp_string_data_t, *UF_MODL_mswp_string_data_p_t;

struct UF_MODL_mswp_until_selected_data_s
{
    tag_t   selected_object;
};
typedef struct UF_MODL_mswp_until_selected_data_s
               UF_MODL_mswp_until_selected_data_t, *UF_MODL_mswp_until_selected_data_p_t;

union UF_MODL_mswp_limit_data_u
{
    UF_MODL_mswp_string_data_t         distance_data;
    UF_MODL_mswp_until_selected_data_t until_selected_data;
};
typedef union UF_MODL_mswp_limit_data_u
              UF_MODL_mswp_limit_data_t, *UF_MODL_mswp_limit_data_p_t;

struct UF_MODL_mswp_limit_s
{ 
    UF_MODL_mswp_limit_type_t  limit_type;
    UF_MODL_mswp_limit_data_t  limit_data;
    logical surf_extend;                            /* For until selected & face only */
};
typedef struct UF_MODL_mswp_limit_s
               UF_MODL_mswp_limit_t, *UF_MODL_mswp_limit_p_t;

struct UF_MODL_mswp_limits_s
{ 
    logical                       symmetry;         /* True: end_limit will not be used
                                                       and the limit type is DISTANCE only;
                                                       False: both limits will be used
                                                       and the limit can be of any type. */
    UF_MODL_mswp_limit_t  start_limit;
    UF_MODL_mswp_limit_t  end_limit;
};
typedef struct UF_MODL_mswp_limits_s
               UF_MODL_mswp_limits_t, *UF_MODL_mswp_limits_p_t;

/* Offset data definitions */
enum UF_MODL_mswp_offset_type_e
{  
    UF_MODL_MSWP_OFFSET_NONE = 0,         /* No offset */
    UF_MODL_MSWP_OFFSET_NORMAL,           /* Offset with two different distances */
    UF_MODL_MSWP_OFFSET_SYMMETRY,         /* Offset with same distance in both directions */
    UF_MODL_MSWP_OFFSET_SINGLE            /* Offset with single distance in one direction */
};
typedef enum UF_MODL_mswp_offset_type_e
             UF_MODL_mswp_offset_type_t;

struct UF_MODL_mswp_offsets_s
{ 
    UF_MODL_mswp_offset_type_t           type;
    UF_MODL_mswp_string_data_t           start_offset; 
    UF_MODL_mswp_string_data_t           end_offset; 
};
typedef struct UF_MODL_mswp_offsets_s
               UF_MODL_mswp_offsets_t, *UF_MODL_mswp_offsets_p_t;

/* Taper data definitions */
enum UF_MODL_mswp_taper_type_e
{  
    UF_MODL_MSWP_TAPER_NONE = 0,         /* No taper */
    UF_MODL_MSWP_TAPER_FROM_EDGE,        /* Simple taper from start edges */
    UF_MODL_MSWP_TAPER_FROM_PROFILE,     /* Simple taper from section */
    UF_MODL_MSWP_TAPER_SYMMETRY,         /* Symmetric taper from section */
    UF_MODL_MSWP_TAPER_MATCHED,           /* Matched end taper from section */
    UF_MODL_MSWP_TAPER_ASYMMETRIC       /* Asymmetric taper from section */
};
typedef enum UF_MODL_mswp_taper_type_e
             UF_MODL_mswp_taper_type_t;

struct UF_MODL_mswp_taper_chain_s
{ 
    UF_MODL_mswp_string_data_t         angle;
    UF_MODL_mswp_string_data_t         back_angle;
    int                                num_curves;    /* Number of curves in a tangent chain.  This can be determined by section only. */
    tag_t                             *curves;        /* Output curves of a tangent chain in a section */
};
typedef struct UF_MODL_mswp_taper_chain_s
               UF_MODL_mswp_taper_chain_t, *UF_MODL_mswp_taper_chain_p_t;

struct UF_MODL_mswp_multi_taper_s
{ 
    int                                num_chains;    /* Number of tangent chains for the section.  This can't be determined by the user. */
    UF_MODL_mswp_taper_chain_t        *chains;       /* Each chain contains a set of curve tags and an angle */
};
typedef struct UF_MODL_mswp_multi_taper_s
               UF_MODL_mswp_multi_taper_t, *UF_MODL_mswp_multi_taper_p_t;

struct UF_MODL_mswp_taper_s
{ 
    UF_MODL_mswp_taper_type_t          type;
    UF_MODL_mswp_string_data_t         angle;         /* angle for simple taper */
    UF_MODL_mswp_string_data_t         back_angle;    /* back angle for simple taper */
    UF_MODL_mswp_multi_taper_t         multi_taper;   /* multi-taper  */
};
typedef struct UF_MODL_mswp_taper_s
               UF_MODL_mswp_taper_t, *UF_MODL_mswp_taper_p_t;

/* The main data structure for Extrude */
struct UF_MODL_mswp_extrude_s
{ 
    tag_t                          section;
    tag_t                          direction;
    double                         dist_tol;
    double                         chain_tol;
    double                         planar_tol;
    double                         angle_tol;
    UF_MODL_mswp_limits_t          limits;
    UF_MODL_mswp_offsets_t         offsets;
    UF_MODL_mswp_taper_t           taper;
    UF_FEATURE_SIGN                sign;
    tag_t                          target_body;
    int                            heal_geom; /* 0 = no action
                                                 1 = fix the geometry defects of input curves
                                                 if within tolerance, including gap/overlay
                                                 between curves and off-planar condition for capping. */
    logical                        solid_preferred;
    logical                        allow_self_intersecting_section;
    logical                        openProfileSmartVolume; /*  the option for enabling open profile smart volume. 
                                                               When this option is set to true, extends the tool volume
                                                               along open end points of the profile to find 
                                                               closure with the target body.   */ 
    int                            closeProfileRule;     /*    the option defines how to extend the open profile 
                                                               to form a proper intersection with the target body.
                                                               0 = FCI, Extends the open profile to form 
                                                                        the first complete intersection with the target
                                                               1 = LCI, Extends the open profile to form
                                                                        the last complete intersection with the target
                                                               2 = CCI, For subtract boolean operation, extends the open profile
                                                                        to form the last complete intersection if the profile lies
                                                                        outside the target excluding the coincident portion.
                                                                        Otherwise, uses the first complete intersection. */
    int                          treatBsplineAsPline;   /* -1 unset, 0= false; 1= true; */
};
typedef struct UF_MODL_mswp_extrude_s
               UF_MODL_mswp_extrude_t, *UF_MODL_mswp_extrude_p_t;

#ifdef __cplusplus
}
#endif

#endif /* UF_MODL_MSWP_TYPES_H_INCLUDED */
