/*****************************************************************************
 *            Copyright (c) 2001 - 2004 Unigraphics Solutions, Inc.
 *                      Unpublished - All Rights Reserved
 * File Name: uf_cam_prefs.h
 *
 * 
 *
 * File description:
 *    This file contains the information required to use the UF_CAM module.
 *    This module allows the CAM User Function programmer to interface
 *    with the current CAM session object and the current CAM Object Parameter
 *    Templates object (OPT). See the documentation of the below functions for
 *    a description of the functionality provided by these objects.
 *
 *    If a function takes a file name as an input parameter then this can
 *    be a full path name or a relative path name. It can also contain
 *    environment variables. If it is not a full path name, UF CAM will use
 *    the directories found in the UGII_CAM_STANDARD_SEARCH_PATH to locate
 *    the specified file.
 *
 *    For a sample CAM application, please refer to ufx_cam.c in the UGOPEN
 *    kit.
 *
 ******************************************************************************/
#ifndef UF_CAM_PREFS_H_INCLUDED
#define UF_CAM_PREFS_H_INCLUDED

/***************************** Include Files **********************************/
#include <uf.h>
#include <uf_cam.h>
#include <uf_defs.h>
#include <uf_cam_spec.h>
#include <uf_cam_errors.h>
#include <uf_param.h>
#include <libufun_cam_exports.h>

/******************************** Defines *************************************/

#ifdef __cplusplus
extern "C" {
#endif

/***************************** Public Typedefs ********************************/


enum UF_CAM_PREF_e
{
   UF_CAM_PREF_blank_geom_color,                 /*  integer  */
   UF_CAM_PREF_blank_geom_type,                  /*  integer  */
   UF_CAM_PREF_check_geom_color,                 /*  integer  */
   UF_CAM_PREF_check_geom_type,                  /*  integer  */
   UF_CAM_PREF_clearance_geom_color,             /*  integer  */
   UF_CAM_PREF_clsf_decimal_place,               /*  integer  */
   UF_CAM_PREF_refresh_bef_path_replay,          /*  logical  */
   UF_CAM_PREF_collect_instances,                /*  logical  */
   UF_CAM_PREF_cut_area_geom_color,              /*  integer  */
   UF_CAM_PREF_cut_area_geom_type,               /*  integer  */
   UF_CAM_PREF_drive_geom_color,                 /*  integer  */
   UF_CAM_PREF_generate_instance,                /*  logical  */
   UF_CAM_PREF_info_csys,                        /*  integer  */
   UF_CAM_PREF_mcs_link_to_rcs,                  /*  integer  */
   UF_CAM_PREF_part_geom_color,                  /*  integer  */
   UF_CAM_PREF_part_geom_type,                   /*  integer  */
   UF_CAM_PREF_pause_aft_path,                   /*  logical  */
   UF_CAM_PREF_refresh_bef_path_generate,        /*  logical  */
   UF_CAM_PREF_relocate_parameters,              /*  logical  */
   UF_CAM_PREF_run_process_assistant,            /*  integer  */
   UF_CAM_PREF_suspect_bounding_box_color,       /*  integer  */
   UF_CAM_PREF_transform_toolpath,               /*  logical  */
   UF_CAM_PREF_trim_geom_color,                  /*  integer  */
   UF_CAM_PREF_uncut_geom_color,                 /*  integer  */
   UF_CAM_PREF_unlink_instance,                  /*  logical  */
   UF_CAM_PREF_update_post_from_tool,            /*  integer  */
   UF_CAM_PREF_force_load_and_turret_tool,       /*  integer  */
   UF_CAM_PREF_use_customized_interface,         /*  logical  */
   UF_CAM_PREF_visible_scrollable_items,         /*  integer  */
   UF_CAM_PREF_visualize_tool_display_color,     /*  integer  */
   UF_CAM_PREF_visualize_gouge_color,            /*  integer  */
   UF_CAM_PREF_visualize_collision_color,        /*  integer  */
   UF_CAM_PREF_visualize_excess_material_color,  /*  integer  */
   UF_CAM_PREF_visualize_auto_block_color,       /*  integer  */
   UF_CAM_PREF_visualize_DMR_tool1_color,        /*  integer  */
   UF_CAM_PREF_visualize_DMR_tool2_color,        /*  integer  */
   UF_CAM_PREF_visualize_DMR_tool3_color,        /*  integer  */
   UF_CAM_PREF_visualize_DMR_tool4_color,        /*  integer  */
   UF_CAM_PREF_visualize_DMR_tool5_color,        /*  integer  */
   UF_CAM_PREF_orient_wcs_to_mcs,                /*  integer  */
   UF_CAM_PREF_cre_fea_grp_in_manu_fea_mang,     /*  integer  */
   UF_CAM_PREF_autoset_machining_data,           /*  integer  */
   UF_CAM_PREF_automatically_update_when_loading /*  logical  NEW in NX 3.0 */
} ;
 typedef enum UF_CAM_PREF_e UF_CAM_PREF_t;

/************************* Public Function Definitions ************************/


/*****************************************************************************
 * This function provides the logical setting of the specified CAM Preference.
 *
 * Return:
 *    UF_CAM_ERROR_DATA_NOT_CORRECT_TYPE - if specified preference does not
 *                                         hold logical data
 * Environment : Internal  and  External
 * See Also:
 * History : Released in V19.0
 ****************************************************************************/
extern UFUN_CAMEXPORT int UF_CAM_PREF_ask_logical_value
(
   UF_CAM_PREF_t   pref,    /* <I> - the specific desired preference  */
   logical        *value    /* <O> - the value of the specified preference  */
);

/*****************************************************************************
 * This function provides the integer value of the specified CAM Preference.
 *
 * Return:
 *    UF_CAM_ERROR_DATA_NOT_CORRECT_TYPE - if specified preference does not
 *                                         hold integer data
 * Environment : Internal  and  External
 * See Also:
 * History : Released in V19.0
 ****************************************************************************/
extern UFUN_CAMEXPORT int UF_CAM_PREF_ask_integer_value
(
   UF_CAM_PREF_t   pref,    /* <I> - the specific desired preference  */
   int            *value    /* <O> - the value of the specified preference  */
);

/*****************************************************************************
 * This function sets the logical setting of the specified CAM Preference.
 *
 * Return:
 *    UF_CAM_ERROR_DATA_NOT_CORRECT_TYPE - if specified preference does not
 *                                         hold logical data
 * Environment : Internal  and  External
 * See Also:
 * History : Released in V19.0
 ****************************************************************************/
extern UFUN_CAMEXPORT int UF_CAM_PREF_set_logical_value
(
   UF_CAM_PREF_t   pref,    /* <I> - the specific desired preference  */
   logical         value    /* <I> - the value of the specified preference  */
);

/*****************************************************************************
 * This function sets the integer value of the specified CAM Preference.
 *
 * Return:
 *    UF_CAM_ERROR_DATA_NOT_CORRECT_TYPE - if specified preference does not
 *                                         hold integer data
 * Environment : Internal  and  External
 * See Also:
 * History : Released in V19.0
 ****************************************************************************/
extern UFUN_CAMEXPORT int UF_CAM_PREF_set_integer_value
(
   UF_CAM_PREF_t   pref,    /* <I> - the specific desired preference  */
   int             value    /* <I> - the value of the specified preference  */
);

/*****************************************************************************
 * This function provides the data type of the specified CAM Preference.
 *
 * Return:
 *    UF_CAM_ERROR_PREFERENCE_NOT_DEFINED - if the specified preference is not
 *                                          defined in the above enum
 * Environment : Internal  and  External
 * See Also:
 * History : Released in V19.0
 ****************************************************************************/
extern UFUN_CAMEXPORT int UF_CAM_PREF_ask_data_type
(
   UF_CAM_PREF_t     pref,   /* <I> - the specific desired preference  */
   UF_PARAM_type_t  *type    /* <O> - the data type of the specified preference -
                                      currently only UF_PARAM_TYPE_LOGICAL and
                                      UF_PARAM_TYPE_INT are supported  */
);

#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif /* UF_CAM_H_INCLUDED */
