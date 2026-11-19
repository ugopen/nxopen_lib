/*******************************************************************************

             Copyright (c) 1999,2000,2001,2002 Unigraphics Solutions, Inc.
                       Unpublished - All Rights Reserved

***************************************************************************
 

File description:

Contains Open API typedefs and macros that are used by the
Weld Assistant module.

 ****************************************************************************/

#ifndef UF_WELD_TYPES_INCLUDED
#define UF_WELD_TYPES_INCLUDED

/****************************************************************************

*****************************************************************************/

#include <uf_defs.h>

#ifdef __cplusplus
extern "C" {
#endif

/*************************************************************************
 Weld types
 

*************************************************************************/
typedef enum UF_WELD_types_e {
                UF_WELD_FILLET_TYPE   = 1,
                UF_WELD_GROOVE_TYPE   = 1<<1,
                UF_WELD_EDGE_TYPE     = 1<<2,
                UF_WELD_PLUG_TYPE     = 1<<3,
                UF_WELD_SLOT_TYPE     = 1<<4,
                UF_WELD_ARC_SPOT_TYPE = 1<<5,
                UF_WELD_SPOT_TYPE     = 1<<6,
                UF_WELD_SEAM_TYPE     = 1<<7,
                UF_WELD_TAPE_TYPE     = 1<<8,
                UF_WELD_BEAD_TYPE     = 1<<9,
                UF_WELD_DOLLOP_TYPE   = 1<<10,
                UF_WELD_CLINCH_TYPE   = 1<<11,

                UF_WELD_FILLET_NA_TYPE   = 1<<12,
                UF_WELD_GROOVE_NA_TYPE   = 1<<13,
                UF_WELD_EDGE_NA_TYPE     = 1<<14,
                UF_WELD_PLUG_NA_TYPE     = 1<<15,
                UF_WELD_SLOT_NA_TYPE     = 1<<16,
                UF_WELD_ARC_SPOT_NA_TYPE = 1<<17,
                UF_WELD_SPOT_NA_TYPE     = 1<<18,
                UF_WELD_SEAM_NA_TYPE     = 1<<19,
                UF_WELD_TAPE_NA_TYPE     = 1<<20,
                UF_WELD_BEAD_NA_TYPE     = 1<<21,
                UF_WELD_DOLLOP_NA_TYPE   = 1<<22,
                UF_WELD_CLINCH_NA_TYPE   = 1<<23,
                UF_FILLET_WELD_TYPE      = 1<<24,
                UF_WELD_ALL_TYPES        = (1<<25)-1  /* All the types */
} UF_WELD_types_t, *UF_WELD_types_p_t;

#define UF_WELD_TYPE_COUNT  25  /* Count is total enums - 1 */

/*************************************************************************
 Weld Feature types
 
*************************************************************************/
typedef enum UF_WELD_feature_types_e{
                UF_WELD_LEGACY_FILLET_TYPE = 0,
                UF_WELD_LEGACY_GROOVE_TYPE,
                UF_WELD_LEGACY_EDGE_TYPE,
                UF_WELD_LEGACY_PLUG_TYPE,
                UF_WELD_LEGACY_SLOT_TYPE,
                UF_WELD_LEGACY_ARC_SPOT_TYPE,
                UF_WELD_LEGACY_SPOT_TYPE,
                UF_WELD_LEGACY_SEAM_TYPE,
                UF_WELD_LEGACY_TAPE_TYPE,
                UF_WELD_LEGACY_BEAD_TYPE,
                UF_WELD_LEGACY_DOLLOP_TYPE,
                UF_WELD_LEGACY_CLINCH_TYPE,
                UF_WELD_LEGACY_FILLET_NA_TYPE,
                UF_WELD_LEGACY_GROOVE_NA_TYPE,
                UF_WELD_LEGACY_EDGE_NA_TYPE,
                UF_WELD_LEGACY_PLUG_NA_TYPE,
                UF_WELD_LEGACY_SLOT_NA_TYPE,
                UF_WELD_LEGACY_ARC_SPOT_NA_TYPE,
                UF_WELD_LEGACY_SPOT_NA_TYPE,
                UF_WELD_LEGACY_SEAM_NA_TYPE,
                UF_WELD_LEGACY_TAPE_NA_TYPE,
                UF_WELD_LEGACY_BEAD_NA_TYPE,
                UF_WELD_LEGACY_DOLLOP_NA_TYPE,
                UF_WELD_LEGACY_CLINCH_NA_TYPE,
                UF_WELD_FILLET_FEATURE,
                UF_WELD_GROOVE_FEATURE,
                UF_WELD_RESISTANCE_SPOT_FEATURE,
                UF_WELD_ARC_SPOT_FEATURE,
                UF_WELD_CLINCH_FEATURE,
                UF_WELD_DOLLOP_FEATURE,
                UF_WELD_WELDNUT_FEATURE,
                UF_WELD_WELDSTUD_FEATURE,
                UF_WELD_CUSTOM1_POINT_FEATURE,
                UF_WELD_CUSTOM2_POINT_FEATURE,
                UF_WELD_CUSTOM3_POINT_FEATURE,
                UF_WELD_CUSTOM4_POINT_FEATURE,
                UF_WELD_CUSTOM5_POINT_FEATURE,

                UF_WELD_BIW_DATUM_SURFACE_FEATURE,
                UF_WELD_BIW_DATUM_PIN_FEATURE,
                UF_WELD_BIW_DATUM_CUSTOM1_FEATURE,
                UF_WELD_BIW_DATUM_CUSTOM2_FEATURE,
                UF_WELD_BIW_DATUM_CUSTOM3_FEATURE,

                UF_WELD_BIW_MEASUREMENT_SURFACE_FEATURE,
                UF_WELD_BIW_MEASUREMENT_HOLE_FEATURE,
                UF_WELD_BIW_MEASUREMENT_SLOT_FEATURE,
                UF_WELD_BIW_MEASUREMENT_STUD_FEATURE,
                UF_WELD_BIW_MEASUREMENT_TRIM_FEATURE,
                UF_WELD_BIW_MEASUREMENT_HEM_FEATURE,
                UF_WELD_BIW_MEASUREMENT_CUSTOM1_FEATURE,
                UF_WELD_BIW_MEASUREMENT_CUSTOM2_FEATURE,
                UF_WELD_BIW_MEASUREMENT_CUSTOM3_FEATURE,
                UF_WELD_USER_DEFINED_FEATURE,
                UF_WELD_SEALER_FILL_FEATURE,
                UF_WELD_SEALER_BEAD_FEATURE,
                UF_WELD_JOINT_FEATURE,
                UF_WELD_PLUGSLOT_FEATURE,
                UF_WELD_PREPARATION_FEATURE,

                UF_WELD_SURFACE_WELD_FEATURE,
                UF_WELD_JOINTMARK_FEATURE,

                UF_WELD_FEATURE_COUNT   /* Insert new above this line */
}UF_WELD_feature_types_t, *UF_WELD_feature_types_p_t;

typedef logical UF_WELD_feature_types_array[UF_WELD_FEATURE_COUNT];

#define UF_WELD_INIT_FEATURE_TYPES_ARRAY(types_array,value)    \
do  {                                                          \
        int  idx;                                                  \
        for ( idx = 0; idx < UF_WELD_FEATURE_COUNT; idx++)         \
        {                                                          \
            (types_array)[idx] = (logical) value;                  \
        }                                                          \
    } while (0)


/*************************************************************************
    New Weld Feature Types
*************************************************************************/
#define FILLET_FEATURE           "FILLET_FEATURE"
#define GROOVE_FEATURE           "GROOVE_FEATURE"
#define RESISTANCE_SPOT_FEATURE  "RESISTANCE_SPOT_FEATURE"
#define ARC_SPOT_FEATURE         "ARC_SPOT_FEATURE"
#define CLINCH_FEATURE           "CLINCH_FEATURE"
#define DOLLOP_FEATURE           "DOLLOP_FEATURE"
#define WELDNUT_FEATURE          "WELDNUT_FEATURE"
#define WELDSTUD_FEATURE         "WELDSTUD_FEATURE"
#define CUSTOM1_POINT_FEATURE    "CUSTOM1_POINT_FEATURE"
#define CUSTOM2_POINT_FEATURE    "CUSTOM2_POINT_FEATURE"
#define CUSTOM3_POINT_FEATURE    "CUSTOM3_POINT_FEATURE"
#define CUSTOM4_POINT_FEATURE    "CUSTOM4_POINT_FEATURE"
#define CUSTOM5_POINT_FEATURE    "CUSTOM5_POINT_FEATURE"
#define USER_DEFINED_WELD        "USER_DEFINED_WELD"

/*----------------------------------------*/
/* BIW Locator datum and measurement type */
/*----------------------------------------*/
#define DATUM_SURFACE_FEATURE    "DATUM_SURFACE_FEATURE"
#define DATUM_PIN_FEATURE        "DATUM_PIN_FEATURE"
#define DATUM_CUSTOM1_FEATURE    "DATUM_CUSTOM1_FEATURE"
#define DATUM_CUSTOM2_FEATURE    "DATUM_CUSTOM2_FEATURE"
#define DATUM_CUSTOM3_FEATURE    "DATUM_CUSTOM3_FEATURE"

#define MEASUREMENT_SURFACE_FEATURE         "MEASUREMENT_SURFACE_FEATURE"
#define MEASUREMENT_HOLE_FEATURE            "MEASUREMENT_HOLE_FEATURE"
#define MEASUREMENT_SLOT_FEATURE            "MEASUREMENT_SLOT_FEATURE"
#define MEASUREMENT_STUD_FEATURE            "MEASUREMENT_STUD_FEATURE"
#define MEASUREMENT_TRIM_FEATURE            "MEASUREMENT_TRIM_FEATURE"
#define MEASUREMENT_HEM_FEATURE             "MEASUREMENT_HEM_FEATURE"
#define MEASUREMENT_CUSTOM1_FEATURE         "MEASUREMENT_CUSTOM1_FEATURE"
#define MEASUREMENT_CUSTOM2_FEATURE         "MEASUREMENT_CUSTOM2_FEATURE"
#define MEASUREMENT_CUSTOM3_FEATURE         "MEASUREMENT_CUSTOM3_FEATURE"

/*************************************************************************
    Weld Feature Types      - Max 30 characters
*************************************************************************/
#define FILLET_WELD                   "FILLET_WELD"
#define GROOVE_WELD                   "GROOVE_WELD"
#define EDGE_WELD                     "EDGE_WELD"
#define PLUG_WELD                     "PLUG_WELD"
#define SLOT_WELD                     "SLOT_WELD"
#define ARC_SPOT_WELD                 "ARC_SPOT_WELD"
#define SPOT_WELD                     "SPOT_WELD"
#define SEAM_WELD                     "SEAM_WELD"
#define TAPE_WELD                     "TAPE_WELD"
#define BEAD_WELD                     "BEAD_WELD"
#define DOLLOP_WELD                   "DOLLOP_WELD"
#define CLINCH_WELD                   "CLINCH_WELD"
#define WELD_FILLET                   "WELD_FILLET"
#define WELD_SPOT_PT                  "WELD_SPOT_PT"
#define WELD_SPOT                     "WELD_SPOT"
#define WELD_UDAW_FEATURE             "USER_DEFINED_WELD_FEATURE"
#define PLUGSLOT_WELD                 "WELD_PLUGSLOT"

#define FILLET_WELD_NON_ASSOCIATIVE   "FILLET_WELD_NON_ASSOCIATIVE"
#define GROOVE_WELD_NON_ASSOCIATIVE   "GROOVE_WELD_NON_ASSOCIATIVE"
#define EDGE_WELD_NON_ASSOCIATIVE     "EDGE_WELD_NON_ASSOCIATIVE"
#define PLUG_WELD_NON_ASSOCIATIVE     "PLUG_WELD_NON_ASSOCIATIVE"
#define SLOT_WELD_NON_ASSOCIATIVE     "SLOT_WELD_NON_ASSOCIATIVE"
#define ARC_SPOT_WELD_NON_ASSOCIATIVE "ARC_SPOT_WELD_NON_ASSOCIATIVE"
#define SPOT_WELD_NON_ASSOCIATIVE     "SPOT_WELD_NON_ASSOCIATIVE"
#define SEAM_WELD_NON_ASSOCIATIVE     "SEAM_WELD_NON_ASSOCIATIVE"
#define TAPE_WELD_NON_ASSOCIATIVE     "TAPE_WELD_NON_ASSOCIATIVE"
#define BEAD_WELD_NON_ASSOCIATIVE     "BEAD_WELD_NON_ASSOCIATIVE"
#define DOLLOP_WELD_NON_ASSOCIATIVE   "DOLLOP_WELD_NON_ASSOCIATIVE"
#define CLINCH_WELD_NON_ASSOCIATIVE   "CLINCH_WELD_NON_ASSOCIATIVE"

/* Old weld types. To avoid part conversion they are retained here */
#define TAPE                          "TAPE"
#define BEAD                          "BEAD"
#define DOLLOP                        "DOLLOP"
#define CLINCH                        "CLINCH"

#define TAPE_NON_ASSOCIATIVE          "TAPE_NON_ASSOCIATIVE"
#define BEAD_NON_ASSOCIATIVE          "BEAD_NON_ASSOCIATIVE"
#define DOLLOP_NON_ASSOCIATIVE        "DOLLOP_NON_ASSOCIATIVE"
#define CLINCH_NON_ASSOCIATIVE        "CLINCH_NON_ASSOCIATIVE"


/*************************************************************************
 Connection information
*************************************************************************/
struct UF_WELD_conn_parts_info_s {
                  int     num_sets;       /* Number of sets */
                  int     *num_tags_in_set; /* <len:num_sets> Number of tags in each set */
                  tag_p_t body_tag;    /* Body tags of connected parts
                                          and if the body tag is an
                                          occurrence then ask for its
                                          part occurrence tag to read the
                                          attributes on the connected parts.
                                          The body tags are stored in a linear
                                          array in blocks of "num_tags_in_set".
                                          That is body tags of first set starts
                                          at 0 to (num_tags_in_set[0]-1) and for
                                          second set it starts from
                                          (num_tags_in_set[0]) to
                                          (num_tags_in_set[1]-1)
                                          and so on for "num_sets".*/
};
typedef struct UF_WELD_conn_parts_info_s UF_WELD_conn_parts_info_t, *UF_WELD_conn_parts_info_p_t;

/*****************************************************************************
This structure contains the information regarding the faces involved in the
spot weld
*****************************************************************************/
struct UF_WELD_spot_face_location_s {
tag_t face_tag;              /* Tag of the face on which the Projected
                                point lies */
double point[3];             /* Projected point location */
double face_normal[3];       /* Surface normal at the projected point */
};
typedef struct UF_WELD_spot_face_location_s UF_WELD_spot_face_location_t, *UF_WELD_spot_face_location_p_t;

/*****************************************************************************
Spot weld Information
******************************************************************************/
struct UF_WELD_spot_info_s {
tag_t spot_point;            /* Spot point tag that
                                is in the Spot weld feature */
UF_WELD_spot_face_location_p_t  face_loc; /* Location of the spot on each set
                                             of faces.
                                             "face_loc[0]" corresponds to
                                             top face */
};
typedef struct UF_WELD_spot_info_s UF_WELD_spot_info_t, *UF_WELD_spot_info_p_t;

/*****************************************************************************
This structure contains the information regarding the faces involved in the
spot weld. This structure is made obsolete in V20
*****************************************************************************/
struct UF_WELD_spot_face_loc_s {
tag_t face_tag;              /* Tag of the face on which the Projected
                                point lies . This will be a NULL_TAG if component
                                is NOT fully loaded,  use 'face_handle' instead. */
double point[3];             /* Projected point location */
double face_normal[3];       /* Surface normal at the projected point */
char   *face_handle;         /* Entity handle of the face on which the Projected
                                point lies . This will be NULL if component
                                is fully loaded, use 'face_tag' instead.  Use
                                 UF_TAG_ask_tag_of_handle
                                to get the face tag once the corresponding component is loaded */
};
typedef struct UF_WELD_spot_face_loc_s UF_WELD_spot_face_loc_t, *UF_WELD_spot_face_loc_p_t;

/*****************************************************************************
Spot weld Information. This structure is made obsolete in V20
******************************************************************************/
struct UF_WELD_spot_data_s {
tag_t spot_point;            /* Spot point tag that
                                is in the Spot weld feature */
UF_WELD_spot_face_loc_p_t  face_loc; /* Location of the spot on each set
                                             of faces.
                                             "face_loc[0]" corresponds to
                                             top face */
};
typedef struct UF_WELD_spot_data_s UF_WELD_spot_data_t, *UF_WELD_spot_data_p_t;


#ifdef __cplusplus
}
#endif
#endif /* UF_WELD_TYPES_INCLUDED */
