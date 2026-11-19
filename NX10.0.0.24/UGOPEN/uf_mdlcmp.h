/*==============================================================================

             Copyright (c) 2002Unigraphics Solutions Inc.
                     Unpublished - All rights reserved



File description:

    User Functions for Model Compare
==============================================================================*/

#ifndef UF_MDLCMP_H_INCLUDED
#define UF_MDLCMP_H_INCLUDED

#include <uf.h>
#include <libufun_exports.h>
#include <uf_modl.h>

#ifdef __cplusplus
extern "C" {
#endif

#define UF_MODL_COMP_CURR_VER 0
#define UF_MODL_INIT_COMPARE_OPTIONS(__options) \
    { \
    (__options)->version                        = UF_MODL_COMP_CURR_VER;\
    UF_MODL_ask_distance_tolerance(&((__options)->tolerance));\
    (__options)->accuracy                       = UF_MODL_COMP_DEFAULT;\
    (__options)->compare_feat_and_exp           = true;\
    (__options)->identical_face_rule            = UF_MODL_COMP_ONLYEXTERNAL;\
    (__options)->continue_if_examine_geom_fails = false;\
    }

/**********************************************************************
 * Description:
 * Enumeration for classifying entities, features and expressions.
 *
 * Environment:
 * Internal and External
 *
 * History:
 * This enumeration was originally released in NX 2.0
 *******************************************************************/
typedef enum
{
   UF_MODL_COMP_ENT_UNKNOWN = 0,
   UF_MODL_COMP_ENT_IDENTICAL,
   UF_MODL_COMP_ENT_CHANGED,
   UF_MODL_COMP_ENT_UNIQUE,
   UF_MODL_COMP_ENT_SUPPRESSED,
   UF_MODL_COMP_ENT_NOT_COMPARED   /* New status from NX3.0
                                      This status will be set for
                                      - features which do not contribute
                                        to topology in the final part
                                      - faces and edges which are small or
                                        sliver relative to the tolerance
                                   */
} UF_MODL_compare_entity_type_e, UF_MODL_compare_entity_type_t;

/**********************************************************************
 * Description:
 * Enumeration for rule for identifying identical faces
 *
 * Environment:
 * Internal and External
 *
 * History:
 * This enumeration was originally released in NX 2.0
 ********************************************************************/
typedef enum
{
   UF_MODL_COMP_ALLEDGES = 0,
   UF_MODL_COMP_ONLYEXTERNAL,
   UF_MODL_COMP_NONE,
   UF_MODL_COMP_GEOM
} UF_MODL_compare_identicalface_rule_e, UF_MODL_compare_identicalface_rule_t;

/**********************************************************************
 * Description:
 * Enumeration for rule for classifying equivalent faces with
 * non identical surfaces as changed or unique
 *
 * Environment:
 * Internal and External
 *
 * History:
 * This enumeration was originally released in NX 2.0
 *
 * Note:  This is obsoleted for NX 3.0 version
********************************************************************/
typedef enum
{
   UF_MODL_COMP_NONIDENTICALSF_CHANGED = 0,
   UF_MODL_COMP_NONIDENTICALSF_UNIQUE
} UF_MODL_compare_changeduniqueface_rule_e, UF_MODL_compare_changeduniqueface_rule_t;

/**********************************************************************
 * Description:
 * Enumeration for comparison accuracy
 *
 * Environment:
 * Internal and External
 *
 * History:
 * This enumeration was originally released in NX 2.0
 ********************************************************************/
typedef enum
{
   UF_MODL_COMP_DEFAULT = 0,
   UF_MODL_COMP_COARSE,
   UF_MODL_COMP_FINE
} UF_MODL_compare_accuracy_e, UF_MODL_compare_accuracy_t;

/**********************************************************************
 * Description:
 * Structure for comparison options
 *
 * Environment:
 * Internal and External
 *
 * History:
 * This enumeration was originally released in NX 3.0
 *
 * Note:
 * This is new structure for NX3.0 version of the functionality
 ********************************************************************/
struct UF_MODL_compare_options_s
{

   int                                  version; /* Version number. For internal use. */
   double                               tolerance; /* Tolerance to be used to determine
                                                      if two geometries can be considered
                                                      coincident */
   UF_MODL_compare_accuracy_t           accuracy; /* Accuracy setting for comparison */
   logical                              compare_feat_and_exp; /* Whether to compare features and
                                                                 expressions. Applicable only if
                                                                 part1 and part2 are related. */
   UF_MODL_compare_identicalface_rule_t identical_face_rule; /* Rule for classifying faces as identical */
   logical                              continue_if_examine_geom_fails; /* If any body fails in examine
                                                                           geometry, continue with comparison,
                                                                           results may not be meaningful */
   logical                              generate_report; /* generate HTML report for the
                                                            compared parts */
};
typedef struct UF_MODL_compare_options_s
               UF_MODL_compare_options_t, *UF_MODL_compare_options_p_t;

/**********************************************************************
 * Description:
 * Structure for entity, feature and expression matches
 *
 * Environment:
 * Internal and External
 *
 * History:
 * This enumeration was originally released in NX 2.0
 ********************************************************************/
struct UF_MODL_compare_entity_match_s
{
   tag_t                         entity_tag;    /* entity of body */
   tag_t                         match_entity;  /* matching entity */
   UF_MODL_compare_entity_type_e type;          /* classifier */
   double                        max_deviation; /* maximum deviation calculated among all sampling points for geometry-related entities */
   double                        avg_deviation; /* average deviation of the sampling points for geometry-related entities   */
};
typedef struct UF_MODL_compare_entity_match_s
               UF_MODL_compare_entity_match_t, *UF_MODL_compare_entity_match_p_t;

typedef UF_MODL_compare_entity_match_p_t UF_MODL_compare_edge_match_p_t;

/**********************************************************************
 * Description:
 * Collection of entities, features and expressions
 *
 * Environment:
 * Internal and External
 *
 * History:
 * This enumeration was originally released in NX 2.0
 ********************************************************************/
struct UF_MODL_compare_entity_info_s
{
   int                             num_entities; /* number of entities */
   UF_MODL_compare_entity_match_t *entity_info;  /* <len:num_entities> array of matching data */
};
typedef struct UF_MODL_compare_entity_info_s
               UF_MODL_compare_entity_info_t, *UF_MODL_compare_entity_info_p_t;

typedef UF_MODL_compare_entity_info_p_t UF_MODL_compare_edge_info_p_t;

struct UF_MODL_compare_part_entities_data_s
{
   UF_MODL_compare_entity_info_t edges;         /* edges from part */
   UF_MODL_compare_entity_info_t faces;         /* faces from part */
   UF_MODL_compare_entity_info_t features;      /* features from part */
   UF_MODL_compare_entity_info_t expressions;   /* expressions from part */
};
typedef struct UF_MODL_compare_part_entities_data_s
               UF_MODL_compare_part_entities_data_t, *UF_MODL_compare_part_entities_data_p_t;

/**********************************************************************
 * Description:
 * Comparison results map data
 *
 * Environment:
 * Internal and External
 *
 * History:
 * This enumeration was originally released in NX 2.0
 ********************************************************************/
struct UF_MODL_compare_part_map_data_s
{
   UF_MODL_compare_part_entities_data_t   part1;           /* entities data for part 1*/
   UF_MODL_compare_part_entities_data_t   part2;           /* entities data for part 1*/
   logical                                identical_parts; /* flag whether parts are
                                                              identical */
};
typedef struct UF_MODL_compare_part_map_data_s
               UF_MODL_compare_part_map_data_t, *UF_MODL_compare_part_map_data_p_t;

/* Used as a replacement for UF_MODL_compare_part_entities_data_s in
the common API - Open C API programs may continue to use the original
UF_MODL_compare_part_entities_data_s structure.
*/
struct UF_MODL_compare_part_entities_data_3_s
{
   UF_MODL_compare_entity_info_p_t edges;         /* edges from part */
   UF_MODL_compare_entity_info_p_t faces;         /* faces from part */
   UF_MODL_compare_entity_info_p_t features;      /* features from part */
   UF_MODL_compare_entity_info_p_t expressions;   /* expressions from part */
};
typedef struct UF_MODL_compare_part_entities_data_3_s
               UF_MODL_compare_part_entities_data_3_t, *UF_MODL_compare_part_entities_data_3_p_t;

/**********************************************************************
 * Description:
 * Comparison results map data.
 * Used as a replacement for UF_MODL_compare_part_map_data_s in
 * the common API - Open C API programs may continue to use the original
 * UF_MODL_compare_part_map_data_s structure.
 *
 * Environment:
 * Internal and External
 *
 * History:
 * This structures is equivalent to UF_MODL_compare_part_map_data_s
 * only difference is members are pointers instead of objects.
 ********************************************************************/
struct UF_MODL_compare_part_map_data_3_s
{
   UF_MODL_compare_part_entities_data_3_p_t   part1;           /* entities data for part 1*/
   UF_MODL_compare_part_entities_data_3_p_t   part2;           /* entities data for part 2*/
   logical                                identical_parts;     /* flag whether parts are
                                                                  identical */
};
typedef struct UF_MODL_compare_part_map_data_3_s
               UF_MODL_compare_part_map_data_3_t, *UF_MODL_compare_part_map_data_3_p_t;
/**********************************************************************
 * Function Name: UF_MODL_initialize_compare_data
 *
 * Function Description:
 * Initialize compare map data. Initializes memory allocated for the
 * mapping data structure containing output of the model compare results.
 *
 * Input/Output:
 * mapping_data - Pointer to the mapping data structure
 *
 * Returns
 * 0 : successful, >0 : failing error number
 *
 * Environment:
 * Internal and External
 *
 * History:
 * This function was originally released in NX 2.0
 ***********************************************************************/
extern UFUNEXPORT int UF_MODL_initialize_compare_data
(
   UF_MODL_compare_part_map_data_t *mapping_data /* <I/O> */
);

/**********************************************************************
 * Function Name: UF_MODL_free_compare_data
 *
 * Function Description:
 * Free model compare map data. Frees the memory allocated for the mapping
 * data structure containing the output of the compare results.
 *
 * Input:
 * mapping_data - Pointer to the mapping data structure
 *
 * Output:
 * None
 *
 * Returns:
 * 0 : successful, >0 : failing error number
 *
 * Environment:
 * Internal and External
 *
 * History:
 * This function was originally released in NX 2.0
 ***********************************************************************/
extern UFUNEXPORT int UF_MODL_free_compare_data
(
    UF_MODL_compare_part_map_data_t *mapping_data  /* <I> */
);

/**********************************************************************
 * Function Name: UF_MODL_model_compare
 *
 * Function Description:
 * Compare parts. Compare bodies from the same part file or from different part files.
 *
 *
 * Input:
 * part1                 - tag of part1
 * body_eid_part1        - Body eid from part 1, if NULL, all bodies from part 1
 *                         Bodies from the part must pass examine geometry check.
 * transform_1           - Transform for body_eid_part_1. Transformation needed to
 *                         convert body 1 into the same co-ordinate system as body 2.
 *                         Initialize with UF_MTX4_identity if bodies are defined in
 *                         the same coordinate system.
 *                         ************************* NOTE ************************
 *                         Applicable only if part 1 and part 2 are not related and
 *                         body_eid_part1 and body_eid_part2 are not NULL. If they are
 *                         NULL, there should be only one body in part1 and part2.
 * part2                 - tag of part2
 * body_eid_part2        - Body eid from part 2, if NULL, all bodies from part 2
 *                         Bodies from the part must pass examine geometry check.
 * transform_2           - Transform for body_eid_part_2. Transformation needed to
 *                         convert body 2 into the same co-ordinate system as body 1.
 *                         Initialize with UF_MTX4_identity if bodies are defined in
 *                         the same coordinate system.
 *                         ************************* NOTE ************************
 *                         Applicable only if part 1 and part 2 are not related and
 *                         body_eid_part1 and body_eid_part2 are not NULL. If they are
 *                         NULL, there should be only one body in part1 and part2.
 * compare_feat_and_exp -  Whether to compare features and expressions. Applicable
 *                         only if part1 and part2 are related.
 * accuracy              - Accuracy setting for comparison
 * tolerance             - Tolerance to be used to determine if two geometries can be
 *                         considered coincident
 * identical_face_rule   - Rule for classifying faces as identical
 * changeduniquefacerule - Rule for classifying related faces as changed or unique
 * launch_ui             - Whether to launch ui
 *                         ************************* NOTE ************************
 *                         This option is not yet supported
 *
 * Output:
 * mapping_data - Mapping data, result of the comparison
 *                Note: Caller is responsible for freing the mapping data
 *
 * Returns:
 * 0 : successful, >0 : failing error number
 *
 * Environment:
 * Internal and External
 *
 * History:
 * This function was originally released in NX 2.0
 * Please use the new version UF_MODL_model_compare_2 from NX 3.0 onwards
 ***********************************************************************/
extern UFUNEXPORT int UF_MODL_model_compare
(
   tag_t                                    part1, /* <I> */
   tag_t                                    body_eids_part1, /* <I> */
   double                                   transform_1[16], /* <I> */
   tag_t                                    part2, /* <I> */
   tag_t                                    body_eids_part2, /* <I> */
   double                                   transform_2[16], /* <I> */
   logical                                  compare_feat_and_exp, /* <I> */
   UF_MODL_compare_accuracy_t               accuracy, /* <I> */
   double                                   tolerance, /* <I> */
   UF_MODL_compare_identicalface_rule_t     identical_face_rule, /* <I> */
   UF_MODL_compare_changeduniqueface_rule_t uniquechangedfacerule, /* <I> */
   logical                                  launch_ui, /* <I> */
   UF_MODL_compare_part_map_data_t          *mapping_data /* <O> */
);

/**********************************************************************
 * Function Name: UF_MODL_model_compare_2
 *
 * Function Description:
 * Compare parts. Compare bodies from the same part file or from different part files.
 * This new function takes in an compare options structure as input. An additional
 * option, continue_if_examine_geom_fails can be set in addition to the existing
 * options. Use this function from NX3.0 onwards instead of UF_MODL_model_compare.
 *
 * Input:
 * part1                 - tag of part1
 * body_eid_part1        - Body eid from part 1, if NULL, all bodies from part 1
 *                         Bodies from the part must pass examine geometry check.
 * transform_1           - Transform for body_eid_part_1. Transformation needed to
 *                         convert body 1 into the same co-ordinate system as body 2.
 *                         Initialize with UF_MTX4_identity if bodies are defined in
 *                         the same coordinate system.
 *                         ************************* NOTE ************************
 *                         Applicable only if part 1 and part 2 are not related and
 *                         body_eid_part1 and body_eid_part2 are not NULL. If they are
 *                         NULL, there should be only one body in part1 and part2.
 * part2                 - tag of part2
 * body_eid_part2        - Body eid from part 2, if NULL, all bodies from part 2
 *                         Bodies from the part must pass examine geometry check.
 * transform_2           - Transform for body_eid_part_2. Transformation needed to
 *                         convert body 2 into the same co-ordinate system as body 1.
 *                         Initialize with UF_MTX4_identity if bodies are defined in
 *                         the same coordinate system.
 *                         ************************* NOTE ************************
 *                         Applicable only if part 1 and part 2 are not related and
 *                         body_eid_part1 and body_eid_part2 are not NULL. If they are
 *                         NULL, there should be only one body in part1 and part2.
 * compare_options       - Comparison options. Use macro UF_MODL_INIT_COMPARE_OPTIONS
 *                         to initialize default options
 *
 * Output:
 * mapping_data - Mapping data, result of the comparison
 *                Note: Caller is responsible for freing the mapping data
 *
 * Returns:
 * 0 : successful, >0 : failing error number
 *
 * Environment:
 * Internal and External
 *
 * History:
 * This function was originally released in NX 3.0
 *
 * Note:
 * New status UF_MODL_COMP_ENT_NOT_COMPARED will be set for
 * - Features which do not contribute
 *   to topology in the final part
 * - Faces and edges which are small or
 *   sliver relative to the tolerance
 *
 ***********************************************************************/
extern UFUNEXPORT int UF_MODL_model_compare_2
(
   tag_t                            part1, /* <I> */
   tag_t                            body_eids_part1, /* <I> */
   double                           transform_1[16], /* <I> */
   tag_t                            part2, /* <I> */
   tag_t                            body_eids_part2, /* <I> */
   double                           transform_2[16], /* <I> */
   UF_MODL_compare_options_p_t      compare_options, /* <I> */
   UF_MODL_compare_part_map_data_t *mapping_data /* <O> */
);


/**********************************************************************
 * Function Name: UF_MODL_model_compare_3
 *
 * Function Description:
 * Used as a replacement for UF_MODL_model_compare_2 in the common API.
 * Open C API programs may continue to use the original
 * UF_MODL_model_compare_2 function.
 *
 * Compare parts. Compare bodies from the same part file or from different part files.
 * This new function takes in an compare options structure as input. An additional
 * option, continue_if_examine_geom_fails can be set in addition to the existing
 * options.
 *
 * Input:
 * part1                 - tag of part1
 * body_eid_part1        - Body eid from part 1, if NULL, all bodies from part 1
 *                         Bodies from the part must pass examine geometry check.
 * transform_1           - Transform for body_eid_part_1. Transformation needed to
 *                         convert body 1 into the same co-ordinate system as body 2.
 *                         Initialize with UF_MTX4_identity if bodies are defined in
 *                         the same coordinate system.
 *                         ************************* NOTE ************************
 *                         Applicable only if part 1 and part 2 are not related and
 *                         body_eid_part1 and body_eid_part2 are not NULL. If they are
 *                         NULL, there should be only one body in part1 and part2.
 * part2                 - tag of part2
 * body_eid_part2        - Body eid from part 2, if NULL, all bodies from part 2
 *                         Bodies from the part must pass examine geometry check.
 * transform_2           - Transform for body_eid_part_2. Transformation needed to
 *                         convert body 2 into the same co-ordinate system as body 1.
 *                         Initialize with UF_MTX4_identity if bodies are defined in
 *                         the same coordinate system.
 *                         ************************* NOTE ************************
 *                         Applicable only if part 1 and part 2 are not related and
 *                         body_eid_part1 and body_eid_part2 are not NULL. If they are
 *                         NULL, there should be only one body in part1 and part2.
 * compare_options       - Comparison options. Use macro UF_MODL_INIT_COMPARE_OPTIONS
 *                         to initialize default options
 *
 * Output:
 * mapping_data - Mapping data, result of the comparison
 *                Note: Caller is responsible for freeing the mapping data, by calling
 *                      UF_MODL_free_compare_data_3
 *
 * Returns:
 * 0 : successful, >0 : failing error number
 *
 * Environment:
 * Internal and External
 *
 * History:
 * This function is just a wrapper over UF_MODL_model_compare_2.
 *
 * Note:
 * New status UF_MODL_COMP_ENT_NOT_COMPARED will be set for
 * - Features which do not contribute
 *   to topology in the final part
 * - Faces and edges which are small or
 *   sliver relative to the tolerance
 *
 ***********************************************************************/
extern UFUNEXPORT int UF_MODL_model_compare_3
(
   tag_t                            part1, /* <I> */
   tag_t                            body_eids_part1, /* <I> */
   double                           transform_1[16], /* <I> */
   tag_t                            part2, /* <I> */
   tag_t                            body_eids_part2, /* <I> */
   double                           transform_2[16], /* <I> */
   UF_MODL_compare_options_p_t      compare_options, /* <I> */
   UF_MODL_compare_part_map_data_3_p_t *mapping_data /* <OF,free:UF_MODL_free_compare_data_3> Call UF_MODL_free_compare_data_3
                                                     to free mapping data.
                                                     */
);
/**********************************************************************
 * Function Name: UF_MODL_free_compare_data_3
 *
 * Function Description:
 * Free model compare map data. Frees the memory allocated for the mapping
 * data structure containing the output of the compare results.
 *
 * Input:
 * mapping_data - Pointer to the mapping data structure UF_MODL_compare_part_map_data_3_t
 *
 * Output:
 * None
 *
 * Returns:
 * 0 : successful, >0 : failing error number
 *
 * Environment:
 * Internal and External
 *
 * History:
 ***********************************************************************/
extern UFUNEXPORT int UF_MODL_free_compare_data_3
(
    UF_MODL_compare_part_map_data_3_t *mapping_data  /* <I> */
);
#ifdef __cplusplus
}
#endif
#undef EXPORTLIBRARY

#endif /* UF_MDLCMP_H_INCLUDED */
