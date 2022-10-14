/****************************************************************************
             Copyright (c) 2001 Unigraphics Solutions, Inc.
                       Unpublished - All Rights Reserved                       

****************************************************************************
 

File Description: 

This file cntains Open API typedefs and macros that are used by PROCESS AID 
ASSISTANT module.

*****************************************************************************/

#ifndef UF_PROCESS_AID_TYPES_INCLUDED
#define UF_PROCESS_AID_TYPES_INCLUDED

#include <uf_defs.h>

#ifdef __cplusplus
extern "C" {
#endif

/*************************************************************************
    Datum object types
    
*************************************************************************/

enum UF_PROCESS_AID_types_e
{
    UF_PROCESS_AID_DATUM_LOC_SURF_TYPE     = 1,
    UF_PROCESS_AID_DATUM_LOC_HOLE_TYPE     = 1<<1,
    UF_PROCESS_AID_DATUM_LOC_SLOT_TYPE     = 1<<2,
    UF_PROCESS_AID_DATUM_LOC_PIN_TYPE      = 1<<3,
    UF_PROCESS_AID_DATUM_LOC_SURF_NA_TYPE  = 1<<4,
    UF_PROCESS_AID_DATUM_LOC_HOLE_NA_TYPE  = 1<<5,
    UF_PROCESS_AID_DATUM_LOC_SLOT_NA_TYPE  = 1<<6,
    UF_PROCESS_AID_DATUM_LOC_PIN_NA_TYPE   = 1<<7,
    UF_PROCESS_AID_DATUM_PT_TYPE           = 1<<8,
    UF_PROCESS_AID_CERT_PT_TYPE            = 1<<9,
    UF_PROCESS_AID_CERT_PT_NA_TYPE         = 1<<10,
    UF_PROCESS_AID_MEA_SURF_VEC_TYPE       = 1<<11,
    UF_PROCESS_AID_MEA_HOLE_VEC_TYPE       = 1<<12,
    UF_PROCESS_AID_MEA_SLOT_VEC_TYPE       = 1<<13,
    UF_PROCESS_AID_MEA_STUD_VEC_TYPE       = 1<<14,
    UF_PROCESS_AID_MEA_TRIM_VEC_TYPE       = 1<<15,
    UF_PROCESS_AID_MEA_HEM_VEC_TYPE        = 1<<16,
    UF_PROCESS_AID_MEA_VEC_NA_TYPE         = 1<<17, 
    UF_PROCESS_AID_MEA_LOC_SURF_TYPE       = 1<<18,
    UF_PROCESS_AID_MEA_LOC_HOLE_TYPE       = 1<<19,
    UF_PROCESS_AID_MEA_LOC_SLOT_TYPE       = 1<<20,
    UF_PROCESS_AID_MEA_LOC_PIN_TYPE        = 1<<21,
    UF_PROCESS_AID_MEA_LOC_SURF_NA_TYPE    = 1<<22,
    UF_PROCESS_AID_MEA_LOC_HOLE_NA_TYPE    = 1<<23,
    UF_PROCESS_AID_MEA_LOC_SLOT_NA_TYPE    = 1<<24,
    UF_PROCESS_AID_MEA_LOC_PIN_NA_TYPE     = 1<<25,
    UF_PROCESS_AID_MEA_PT_TYPE             = 1<<26, 
    UF_PROCESS_AID_ALL_DATUM_TYPES         = (1<<27 )-1 /* All the types */
};
typedef enum UF_PROCESS_AID_types_e
             UF_PROCESS_AID_types_t, *UF_PROCESS_AID_types_p_t;

#define UF_PROCESS_AID_DATUM_COUNT 27    /* Count is total enums - 1 */

/*************************************************************************
    Datum Feature Types      - Max 30 characters
*************************************************************************/
#define SURFACE_DATUM_LOCATION             "SURFACE_DAT_LOCATION"
                                           /* Feature name is DATUM_LOCATION */
#define HOLE_DATUM_LOCATION                "HOLE_DAT_LOCATION"
                                           /* Feature name is DATUM_LOCATION */
#define SLOT_DATUM_LOCATION                "SLOT_DAT_LOCATION"
                                           /* Feature name is DATUM_LOCATION */
#define PIN_DATUM_LOCATION                 "PIN_DAT_LOCATION"
                                           /* Feature name is DATUM_LOCATION */
#define SURFACE_DATUM_LOCATION_NON_ASSOC   "SURFACE_DAT_LOCATION_NON_ASSOC"
                                           /* Feature name is DATUM_LOCATION */
#define HOLE_DATUM_LOCATION_NON_ASSOC      "HOLE_DAT_LOCATION_NON_ASSOC"
                                           /* Feature name is DATUM_LOCATION */
#define SLOT_DATUM_LOCATION_NON_ASSOC      "SLOT_DAT_LOCATION_NON_ASSOC"
                                           /* Feature name is DATUM_LOCATION */
#define PIN_DATUM_LOCATION_NON_ASSOC       "PIN_DAT_LOCATION_NON_ASSOC"
                                           /* Feature name is DATUM_LOCATION */
#define DATUM_POINT                        "DAT_POINT"
                                           /* Feature name is DATUM_POINT */
#define CERTIFICATION_POINT                "CERTIFICATION_POINT"
#define CERTIFICATION_POINT_NON_ASSOC      "CERTIFICATION_POINT_NON_ASSOC"
                                           /* Feature name is CERTIFICATION_POINT */
#define SURFACE_VECTOR                     "SURFACE_VECTOR"
#define HOLE_VECTOR                        "HOLE_VECTOR"
#define SLOT_VECTOR                        "SLOT_VECTOR"
#define STUD_VECTOR                        "STUD_VECTOR"
#define TRIM_VECTOR                        "TRIM_VECTOR"
#define HEM_VECTOR                         "HEM_VECTOR"
#define MEASUREMENT_VECTOR_NON_ASSOC       "MEASUREMENT_VECTOR_NON_ASSOC"
#define SURFACE_MEASUREMENT_LOCATION       "SURFACE_MEASUREMENT_LOCATION"
                                           /* Feature name is MEASUREMENT_LOCATION */
#define HOLE_MEASUREMENT_LOCATION          "HOLE_MEASUREMENT_LOCATION"
                                           /* Feature name is MEASUREMENT_LOCATION */
#define SLOT_MEASUREMENT_LOCATION          "SLOT_MEASUREMENT_LOCATION"
                                           /* Feature name is MEASUREMENT_LOCATION */
#define PIN_MEASUREMENT_LOCATION          "PIN_MEASUREMENT_LOCATION"
                                           /* Feature name is MEASUREMENT_LOCATION */
#define SURFACE_MEASUREMENT_LOCATION_NON_ASSOC "SURFACE_MEA_LOCATION_NON_ASSOC"
                                           /* Feature name is MEASUREMENT_LOCATION */
#define HOLE_MEASUREMENT_LOCATION_NON_ASSOC "HOLE_MEA_LOCATION_NON_ASSOC"
                                           /* Feature name is MEASUREMENT_LOCATION */
#define SLOT_MEASUREMENT_LOCATION_NON_ASSOC "SLOT_MEA_LOCATION_NON_ASSOC"
                                           /* Feature name is MEASUREMENT_LOCATION */
#define PIN_MEASUREMENT_LOCATION_NON_ASSOC "PIN_MEA_LOCATION_NON_ASSOC"
                                           /* Feature name is MEASUREMENT_LOCATION */
#define MEASUREMENT_POINT                  "MEASUREMENT_POINT"

/*************************************************************************
    Datum object types
    
*************************************************************************/
enum UF_PROCESS_AID_relation_type_e
{
    UF_PROCESS_AID_RELATION_NONE_TYPE = 0,
    UF_PROCESS_AID_RELATION_FLUSH_TYPE,
    UF_PROCESS_AID_RELATION_GAP_TYPE,
    UF_PROCESS_AID_RELATION_NON_SPECIFIC_TYPE
};
typedef enum UF_PROCESS_AID_relation_type_e
             UF_PROCESS_AID_relation_type_t, *UF_PROCESS_AID_relation_type_p_t;

/*************************************************************************
 Weld types applicable for distance checks
*************************************************************************/
enum UF_PROCESS_AID_WELD_types_e 
{
    UF_PROCESS_AID_WELD_ARC_SPOT_TYPE      = 1,
    UF_PROCESS_AID_WELD_SPOT_TYPE          = 1<<1,
    UF_PROCESS_AID_WELD_CLINCH_TYPE        = 1<<2,
    UF_PROCESS_AID_WELD_ARC_SPOT_NA_TYPE   = 1<<3,
    UF_PROCESS_AID_WELD_SPOT_NA_TYPE       = 1<<4,
    UF_PROCESS_AID_WELD_CLINCH_NA_TYPE     = 1<<5,
    UF_PROCESS_AID_ALL_WELD_TYPES          = (1<<6)-1
};
typedef enum UF_PROCESS_AID_WELD_types_e 
             UF_PROCESS_AID_WELD_types_t, *UF_PROCESS_AID_WELD_types_p_t;

#define UF_PROCESS_AID_WELD_COUNT 6    /* Count is total enums -1 */
#define ARC_SPOT_WELD   "ARC_SPOT_WELD"
#define SPOT_WELD       "SPOT_WELD"
#define CLINCH          "CLINCH"
#define ARC_SPOT_WELD_NON_ASSOC   "ARC_SPOT_WELD_NON_ASSOCIATIVE"
#define SPOT_WELD_NON_ASSOC       "SPOT_WELD_NON_ASSOCIATIVE"
#define CLINCH_NON_ASSOC          "CLINCH_NON_ASSOCIATIVE"

struct UF_PROCESS_AID_dlf_s
{
    uf_list_p_t  *sel_set; /* Can be faces and curves for Surface DLF
                              Edges and Curves for Hole/Slot DLF */
    int          num_set; /* Number of sets */
    tag_t        dlf_plane;  /* Selected Plane,
                                NULL_TAG for Hole/Slot DLF */
};
typedef struct UF_PROCESS_AID_dlf_s
               UF_PROCESS_AID_dlf_t, *UF_PROCESS_AID_dlf_p_t;

struct UF_PROCESS_AID_dpt_s
{
    tag_t            ref_dlf_daxis;                  /* Selected DLF datum 
                                                        axis */
    uf_list_p_t      sel_face_edges;                 /* Selected face/edges */
};
typedef struct UF_PROCESS_AID_dpt_s
               UF_PROCESS_AID_dpt_t, *UF_PROCESS_AID_dpt_p_t;

struct UF_PROCESS_AID_cpt_s
{
    tag_t                ref_dpt;                   /* Datum Point picked */
    uf_list_p_t          sel_faces;                 /* Selected Face */
    uf_list_p_t          sel_crvs_edgs;            /* List of tags of Bndry
                                                     curves and edges */
};
typedef struct UF_PROCESS_AID_cpt_s
               UF_PROCESS_AID_cpt_t, *UF_PROCESS_AID_cpt_p_t;

struct UF_PROCESS_AID_svec_s
{
    tag_t            sel_face; /* Selected Face */
};
typedef struct UF_PROCESS_AID_svec_s
               UF_PROCESS_AID_svec_t, *UF_PROCESS_AID_svec_p_t;

struct UF_PROCESS_AID_tvec_s
{
    tag_t             sel_face; /* Selected Face */
    tag_t             sel_edge; /* Selected Edge */
};
typedef struct UF_PROCESS_AID_tvec_s
               UF_PROCESS_AID_tvec_t, *UF_PROCESS_AID_tvec_p_t;

struct UF_PROCESS_AID_hsvec_s
{
    uf_list_p_t      sel_edges;            /* Selected Edges */
};
typedef struct UF_PROCESS_AID_hsvec_s
               UF_PROCESS_AID_hsvec_t, *UF_PROCESS_AID_hsvec_p_t;

struct UF_PROCESS_AID_hvec_s
{
    tag_t             sel_face; /* Selected Face */
    tag_t             hem_plane; /* Selected Plane */
};
typedef struct UF_PROCESS_AID_hvec_s
               UF_PROCESS_AID_hvec_t, *UF_PROCESS_AID_hvec_p_t;

union UF_PROCESS_AID_sel_data_u
{
    UF_PROCESS_AID_dlf_t  dlf_data; /* Datum Location */
    UF_PROCESS_AID_dpt_t  dpt_data; /* Datum_point */
    UF_PROCESS_AID_cpt_t  cpt_data; /* Certification Point */
    UF_PROCESS_AID_svec_t  svec_data; /* Surface Vector */
    UF_PROCESS_AID_tvec_t  tvec_data; /* Trim Vector */
    UF_PROCESS_AID_hsvec_t  hsvec_data; /* Hole/Slot Vector */
    UF_PROCESS_AID_hvec_t  hvec_data; /* Hem Vector */
   
};
typedef union UF_PROCESS_AID_sel_data_u
              UF_PROCESS_AID_sel_data_u_t, *UF_PROCESS_AID_sel_data_u_p_t;

#ifdef __cplusplus
}
#endif
#endif /* UF_PROCESS_AID_TYPES_INCLUDED */


