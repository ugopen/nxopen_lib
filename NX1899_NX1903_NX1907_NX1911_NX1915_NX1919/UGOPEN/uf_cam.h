/*****************************************************************************
 *            Copyright (c) 1998-2000,2001,2002,2003,2004 Unigraphics Solutions, Inc.
 *                      Unpublished - All Rights Reserved
 * File Name: uf_cam.h
 *
 * 
 *
 * File description:
 *    This file contains the information required to use the UF_CAM module.
 *    This module allows the NX CAM User Function programmer to interface
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
 *    For sample CAM application's, please refer to the following files in
 *    the NX Open kit.
 *
 *    ufd_cam_create_ude.c    ufd_camgeom.c
 *    ufd_cam_sample.c        ufd_cambnd_grp_data_ude.c
 *    ufd_cam_udop.c        ufd_cam_turn_autoprog.c
 *    ufd_cambnd.c        ufx_cam.c
 *
 ******************************************************************************/
#ifndef UF_CAM_H_INCLUDED
#define UF_CAM_H_INCLUDED

/***************************** Include Files **********************************/
#include <uf.h>
#include <uf_defs.h>
#include <uf_cam_spec.h>
#include <uf_cam_errors.h>
#include <libufun_cam_exports.h>

/******************************** Defines *************************************/

#define UF_CAM_MAX_TEMPLATE_SET_NAME_NCHARS     256
#define UF_CAM_MAX_TEMPLATE_SET_NAME_BUFSIZE    NX_BUFSIZE(UF_CAM_MAX_TEMPLATE_SET_NAME_NCHARS)

/*  */
#define UF_CAM_MAX_TEMPLATE_SET_NAME_LEN         (UF_CAM_MAX_TEMPLATE_SET_NAME_BUFSIZE-1)
/*  */

#ifdef __cplusplus
extern "C" {
#endif

/*
   **************************************************************************
   ***************************     Definitions    ***************************
   **************************************************************************
*/

/*******************************************************************************

   This is the identifier of the object which represents the Machining Feature

   Environment: Internal  and  External

*******************************************************************************/

typedef  void  *UF_NCFEAT_t;




/***************************** Public Typedefs ********************************/

/*
 * An object which is used to access a Library object; for more information
 * please see the NX Libraries documentation in the NX Users Manual.
 */
typedef void   *UF_CAM_db_object_t;

/* A Object Parameter Template object */
typedef void   *UF_CAM_opt_t;
/*
 * The CAM geometry types.
 */
enum UF_CAM_geom_type_e
{
    UF_CAM_part,
    UF_CAM_blank,
    UF_CAM_check,
    UF_CAM_trim,
    UF_CAM_cut_area,
    UF_CAM_wall,
    UF_CAM_drive
};

typedef enum UF_CAM_geom_type_e UF_CAM_geom_type_t, *UF_CAM_geom_type_p_t;

enum UF_CAM_blank_geom_type_e
{
    UF_CAM_feature_geom_type,
    UF_CAM_geometry_geom_type,
    UF_CAM_facet_geom_type,
    UF_CAM_auto_block_type,
    UF_CAM_offset_from_part_type
};
typedef enum UF_CAM_blank_geom_type_e UF_CAM_blank_geom_type_t;

enum UF_CAM_avoidance_type_e
{
    UF_CAM_avoidance_type_none,
    UF_CAM_avoidance_type_warning,
    UF_CAM_avoidance_type_stepover,
    UF_CAM_avoidance_type_lift
};

typedef enum UF_CAM_avoidance_type_e UF_CAM_avoidance_type_t, *UF_CAM_avoidance_type_p_t;

enum UF_CAM_feedrate_unit_e
{
    UF_CAM_feedrate_unit_none,
    UF_CAM_feedrate_unit_per_minute,
    UF_CAM_feedrate_unit_per_revolution
};

typedef enum UF_CAM_feedrate_unit_e UF_CAM_feedrate_unit_t, *UF_CAM_feedrate_unit_p_t;

enum UF_CAM_tool_position_e
{
    UF_CAM_tool_position_undefined,
    UF_CAM_tool_position_on,
    UF_CAM_tool_position_tanto
};

typedef enum UF_CAM_tool_position_e UF_CAM_tool_position_t, *UF_CAM_tool_position_p_t;

enum UF_CAM_boundary_type_e
{
    UF_CAM_boundary_type_closed,
    UF_CAM_boundary_type_open
};

typedef enum UF_CAM_boundary_type_e UF_CAM_boundary_type_t, *UF_CAM_boundary_type_p_t;

enum UF_CAM_material_side_e
{
    UF_CAM_material_side_undefined,
    UF_CAM_material_side_in_left,       /* Inside if the boundary is closed.
                                           Left side if the boundary is open. */
    UF_CAM_material_side_out_right      /* Outside if the boundary is closed.
                                           Right side if the boundary is open. */
};

typedef enum UF_CAM_material_side_e UF_CAM_material_side_t, *UF_CAM_material_side_p_t;

/*  */
/* These are the Object Parameter Template (OPT) subtype classes */
enum UF_CAM_opt_stype_cls_e
{
   UF_CAM_OPT_STYPE_CLS_SETUP,     /* Setup */
   UF_CAM_OPT_STYPE_CLS_OPER,      /* Operations */
   UF_CAM_OPT_STYPE_CLS_PROG,      /* NC Program */
   UF_CAM_OPT_STYPE_CLS_TOOL,      /* Machine Tools and Cutters */
   UF_CAM_OPT_STYPE_CLS_METHOD,    /* Machining Method */
   UF_CAM_OPT_STYPE_CLS_GEOM,      /* Geometry */
   UF_CAM_OPT_STYPE_CLS_LAST       /* Do not use */
}  ;
 typedef enum UF_CAM_opt_stype_cls_e UF_CAM_opt_stype_cls_t;

/*
 * NOTES on UF_CAM_preferences_t:
 *
 *   1) all items that refer to color can take any of the color values that
 *      appear in uf_obj.h.
 *   2) all the item here have the same meaning as defined in the CAM
 *      Preferences chapter of the NX Users Manual.
 */
struct UF_CAM_preferences_s
{
   int       blank_geom_color;
   int       blank_geom_type;
   int       check_geom_color;
   int       check_geom_type;
   int       clearance_geom_color;
   int       clsf_decimal_place;
   logical   clsf_replay_advanced;
   logical   clsf_replay_refresh;
   logical   clsf_replay_vericut;
   int       clsf_type;
   logical   collect_instances;
   logical   create_tool_lib_entry;
   int       cut_area_geom_color;
   int       cut_area_geom_type;
   logical   delete_param_set;
   int       drive_geom_color;
   logical   generate_instance;
   int       info_csys;
   logical   macro_only;
   int       mcs_link_to_rcs;
   int       mcs_stat;
   logical   parent_display;
   int       part_geom_color;
   int       part_geom_type;
   logical   pause_aft_path;
   int       rcs_disp_stat;
   double    rcs_inv_matrix[9];
   int       rcs_map_stat;
   double    rcs_origin[3];
   int       rcs_stat;
   logical   refresh_bef_path;
   logical   show_edited_status;
   logical   show_standard_type;
   logical   show_template_type;
   logical   show_tool_name;
   logical   template_tool;
   logical   toolpath_only;
   char      template_set_used[UF_CAM_MAX_TEMPLATE_SET_NAME_BUFSIZE];
   logical   transform_toolpath;
   int       trim_geom_color;
   int       uncut_geom_color;
   logical   unlink_instance;
   logical   use_customized_interface;
   int       visible_scrollable_items;
   logical   automatically_update_when_loading;     /* NEW in NX 3.0 */

} ;
typedef struct UF_CAM_preferences_s UF_CAM_preferences_t,
               *UF_CAM_preferences_p_t;

/************************* Public Function Definitions ************************/

/*****************************************************************************
 * This function answers whether or not there exists a currently initialized
 * CAM session. A currently initialized CAM session must exist in order to
 * call any other NX CAM User Function except init_session.
 *
 * Environment : Internal  and  External
 * See Also:
 * History : Released in V16.0
 ****************************************************************************/
extern UFUN_CAMEXPORT int UF_CAM_is_session_initialized
(
   logical  *answer   /* <O> - TRUE if there exists an initialized CAM session;
                       *       FALSE otherwise.
                       */
);


/*****************************************************************************
 * This function initializes the current CAM session based upon the contents
 * of the configuration file specified by $UGII_CAM_CONFIG. If a CAM session
 * currently exists it is first unloaded.
 *
 * Environment : Internal  and  External
 * See Also:
 * History : Released in V16.0
 ****************************************************************************/
extern UFUN_CAMEXPORT int UF_CAM_init_session
(
   void
);


/*****************************************************************************
 * This function initializes the current CAM session based upon the contents
 * of the specified configuration file. If a CAM session currently exists it
 * is first unloaded.
 *
 * Environment : Internal  and  External
 * See Also:
 * History : Released in V16.0
 ****************************************************************************/
extern UFUN_CAMEXPORT int UF_CAM_reinit_session
(
   const char   *config_file  /* <I> - the name of the configuration file to use
                               *       to initialize the CAM session.
                               */
);


/*****************************************************************************
 * This function provides the current settings of the CAM preferences.
 *
 * Environment : Internal  and  External
 * See Also:
 * History : Released in V16.0
 ****************************************************************************/
extern UFUN_CAMEXPORT int UF_CAM_ask_cam_preferences
(
   UF_CAM_preferences_p_t   prefs  /* <O> - the current CAM preferences */
);


/*****************************************************************************
 * This function sets the current settings of the CAM preferences.
 *
 * Environment : Internal  and  External
 * See Also:
 * History : Released in V16.0
 ****************************************************************************/
extern UFUN_CAMEXPORT int UF_CAM_set_cam_preferences
(
   UF_CAM_preferences_p_t   prefs  /* <I> - the values to use to set the current
                                    *       CAM preferences settings.
                                    */
);


/*****************************************************************************
 * This function provides the database object which is currently used to
 * access the Cutter library.
 *
 * Environment : Internal  and  External
 * See Also:
 * History : Released in V16.0
 ****************************************************************************/
extern UFUN_CAMEXPORT int UF_CAM_ask_cutter_db_object
(
   UF_CAM_db_object_t   *db_obj /* <O> - see function description */
);


/*****************************************************************************
 * This function provides the database object which is currently used to
 * access the Machine Tool library.
 *
 * Environment : Internal  and  External
 * See Also:
 * History : Released in V16.0
 ****************************************************************************/
extern UFUN_CAMEXPORT int UF_CAM_ask_mach_tool_db_object
(
   UF_CAM_db_object_t   *db_obj /* <O> - see function description */
);


/*****************************************************************************
 * This function provides the database object which is currently used to
 * access the Tool Material library.
 *
 * Environment : Internal  and  External
 * See Also:
 * History : Released in V16.0
 ****************************************************************************/
extern UFUN_CAMEXPORT int UF_CAM_ask_tool_matl_db_object
(
   UF_CAM_db_object_t   *db_obj /* <O> - see function description */
);


/*****************************************************************************
 * This function provides the database object which is currently used to
 * access the Blank Material library.
 *
 * Environment : Internal  and  External
 * See Also:
 * History : Released in V16.0
 ****************************************************************************/
extern UFUN_CAMEXPORT int UF_CAM_ask_blank_matl_db_object
(
   UF_CAM_db_object_t   *db_obj /* <O> - see function description */
);


/*****************************************************************************
 * This function provides the database object which is currently used to
 * access the Feeds and Speeds library.
 *
 * Environment : Internal  and  External
 * See Also:
 * History : Released in V16.0
 ****************************************************************************/
extern UFUN_CAMEXPORT int UF_CAM_ask_f_s_db_object
(
   UF_CAM_db_object_t   *db_obj /* <O> - see function description */
);


/*****************************************************************************
 * This function provides the object which is used to interface with the
 * current Object Parameter Templates (OPTs). Refer to the
 * UF_CAM_opt_stype_cls_t definition to see the possible OPT subtype classes
 * available.
 *
 * Environment : Internal  and  External
 * See Also:
 * History : Released in V16.0
 ****************************************************************************/
extern UFUN_CAMEXPORT int UF_CAM_ask_opt_template_object
(
   UF_CAM_opt_t   *opt_object /* <O> - see function description */
);


/*****************************************************************************
 * This function provides a list of available post names. They are derived
 * from the post template file that is specified by the configuration file
 * that is used to initialize the CAM session. These names can be used
 * to generate a specified Post by calling the apppropriate UF_SETUP
 * function.
 *
 * Environment : Internal  and  External
 * See Also:
 * History : Released in V16.0
 ****************************************************************************/
extern UFUN_CAMEXPORT int UF_CAM_opt_ask_post_names
(
   int            *count,  /* <O> - the number of available post names */
   const char   ***names   /* <OF,len:count> - the available post names. The returned
                                     array must be freed by calling UF_free_string_array.
                            */
);


/*****************************************************************************
 * This function provides a list of available CLSF names. They are derived
 * from the CLSF template file that is specified by the configuration file
 * that is used to initialize the CAM session. These names can be used
 * to generate a specified CLSF by calling the apppropriate UF_SETUP
 * function.
 *
 * Environment : Internal  and  External
 * See Also:
 * History : Released in V16.0
 ****************************************************************************/
extern UFUN_CAMEXPORT int UF_CAM_opt_ask_clsf_names
(
   int            *count,  /* <O> - the number of available clsf names */
   const char   ***names   /* <OF,len:count> - the available clsf names. The returned
                                   array must be freed by calling
                                   UF_free_string_array.
                            */
);


/*****************************************************************************
 * This function provides a list of available SHOP DOC names. They are derived
 * from the SHOP DOC template file that is specified by the configuration file
 * that is used to initialize the CAM session. These names can be used
 * to generate a specified documentation format by calling the apppropriate
 * UF_SHOPDOC function.
 *
 * NOTE: you should use UF_free_string_array to free the returned memory.
 *
 * Environment : Internal  and  External
 * See Also:
 * History : Released in V16.0
 ****************************************************************************/
extern UFUN_CAMEXPORT int UF_CAM_opt_ask_doc_names
(
   int            *count,  /* <O> - the number of names */
   const char   ***names   /* <OF,len:count> - the available doc names. The returned
                                     array must be freed by calling UF_free_string_array.
                            */
);


/*****************************************************************************
 * This function reinitializes the Object Parameter Templates based upon the
 * contents of the specified template file.
 *
 * Environment : Internal  and  External
 * See Also:
 * History : Released in V16.0
 ****************************************************************************/
extern UFUN_CAMEXPORT int UF_CAM_reinit_opt
(
   const char   *template_filename  /* <I> - see function description */
);


/*****************************************************************************
 * This function provides the names of the available Object Parameter
 * Template types.
 *
 * Environment : Internal  and  External
 * See Also:
 * History : Released in V16.0
 ****************************************************************************/
extern UFUN_CAMEXPORT int UF_CAM_opt_ask_types
(
   int            *count,       /* <O> - the number of type names returned */
   const char   ***type_names   /* <OF,len:count> - the available type names. The returned
                                     array must be freed by calling UF_free_string_array.
                                 */
);


/*****************************************************************************
 * This function provides the names of the available Object Parameter
 * Template subtypes for the specified Object Parameter Type. Only those
 * subtypes  which have the specified Object Parameter Template subtype class
 * are returned.
 *
 * Environment : Internal  and  External
 * See Also:
 * History : Released in V16.0
 ****************************************************************************/
extern UFUN_CAMEXPORT int UF_CAM_opt_ask_subtypes
(
   const char              *opt_type_name, /* <I> - the name of the OPT type
                                                    whose subtypes are desired
                                            */
   UF_CAM_opt_stype_cls_t   subtype_class, /* <I> - the desired subtype class */
   int      *count,          /* <O> - the number of subtypes */
   const char   ***subtypes  /* <OF,len:count> - the available subtypes. The returned
                                     array must be freed by calling UF_free_string_array.
                              */
);


/*****************************************************************************
 * This function adds the specified part file as a new type to the existing
 * Object Parameter Templates. All the subtypes contained in the specified
 * part file are added as Object Parameter Templates subtypes.
 *
 * Environment : Internal  and  External
 * See Also:
 * History : Released in V16.0
 ****************************************************************************/
extern UFUN_CAMEXPORT int UF_CAM_opt_add_type
(
   const char   *filespec  /* <I> - the name of the file representing the new
                            *       type.
                            */
);


/*****************************************************************************
 * This function adds the specified part file as a new subtype to the existing
 * Object Parameter Templates.
 *
 * Environment : Internal  and  External
 * See Also:
 * History : Released in nx903
 ****************************************************************************/
extern UFUN_CAMEXPORT int UF_CAM_opt_add_template_part
(
   const char   *filespec  /* <I> - the name of the file representing the template part
                            */
);

/*****************************************************************************
 * This function provides the tag of the NX object which corresponds to the
 * specified Object Parameter Template type and subtype.
 * Templates.
 *
 * Environment : Internal  and  External
 * See Also:
 * History : Released in V16.0
 ****************************************************************************/
extern UFUN_CAMEXPORT int UF_CAM_opt_ask_object
(
   UF_CAM_opt_stype_cls_t  subtype_class, /* <I> - the desired subtype class */
   const char      *type,          /* <I> - the type of the object desired */
   const char      *subtype,       /* <I> - the subtype of the object desired */
   tag_t           *param          /* <O> - the tag of the desired object */
);


/*****************************************************************************
 * This function provides the name of the file that stores the list of
 * available POST templates. This is determined by the contents of
 * cam_config.dat.
 *
 * Environment : Internal  and  External
 * See Also:
 * History : Released in V16.0
 ****************************************************************************/
extern UFUN_CAMEXPORT int UF_CAM_ask_post_template_name
(
   const char   **post_template_filename /* <OF> - see function comments */
);


/*****************************************************************************
 * This function provides the name of the file that stores the list of
 * available Documentation templates. This is determined by the contents of
 * cam_config.dat.
 *
 * Environment : Internal  and  External
 * See Also:
 * History : Released in V16.0
 ****************************************************************************/
extern UFUN_CAMEXPORT int UF_CAM_ask_doc_template_name
(
   const char   **doc_template_filename /* <OF> - see function comments */
);

/*****************************************************************************
 * This function provides the name of the CAM configuration file used in the
 * current CAM Session.
 *
 * Environment : Internal  and  External
 * See Also:
 * History : Released in V18.0
 ****************************************************************************/
extern UFUN_CAMEXPORT int UF_CAM_ask_config_file
(
   const char   **cam_config_filename /* <OF> - configuration file name
                                       *        of the current CAM session.
                                       *        The returned string must be
                                       *        freed by calling UF_free.
                                       */
);

/***************************************************************************
 *
 * Query the type and data of an automatic blank.
 *
 * Return :
 *           Return code :
 *
 * Environment: Internal  and  External
 *
 * See Also:
 *   UF_CAM_set_auto_blank
 *
 * History: Released in V19.0
 ************************************************************************/
extern UFUN_CAMEXPORT int UF_CAM_ask_auto_blank
(
    tag_t                      object_tag,     /* <I> the operation or geometry group containing blank definition  */
    UF_CAM_blank_geom_type_t   *geom_type,     /* <O> type type of blank geometry defined */
    double                     offset[6]       /* <O>
        For geom_type = UF_CAM_auto_block_type, offset is an array of positive deltas to a minimal box
                                      aligned with the MCS which contains the specified part geometry.
           Offset[0] = offset along +XM
           Offset[1] = offset along -XM
           Offset[2] = offset along +YM
           Offset[3] = offset along -YM
           Offset[4] = offset along +ZM
           Offset[5] = offset along -ZM
        For geom_type = UF_CAM_offset_from_part, offset is a single positive offset from the specified
                                      Part geometry.
            Offset[0] = global offset of part geometry
            Offset[1-5]  unused  */
    );

/***************************************************************************
 *
 * Define the type and data of an automatic blank.
 *
 * Return :
 *           Return code :
 *
 * Environment: Internal  and  External
 *
 * See Also:
 *   UF_CAM_ask_auto_blank
 *
 * History: Released in V19.0
 ************************************************************************/
extern UFUN_CAMEXPORT int UF_CAM_set_auto_blank
(
    tag_t                      object_tag,      /* <I> the operation or geometry group containing blank definition  */
    UF_CAM_blank_geom_type_t   geom_type,       /* <I> type type of blank geometry defined */
    double                     offset[6]        /* <I>
        For geom_type = UF_CAM_auto_block_type, offset is an array of positive deltas to a minimal box
                                      aligned with the MCS which contains the specified part geometry.
           Offset[0] = offset along +XM
           Offset[1] = offset along -XM
           Offset[2] = offset along +YM
           Offset[3] = offset along -YM
           Offset[4] = offset along +ZM
           Offset[5] = offset along -ZM
        For geom_type = UF_CAM_offset_from_part, offset is a single positive offset from the specified
                                      Part geometry.
            Offset[0] = global offset of part geometry
            Offset[1-5]  unused  */
    );

/***************************************************************************
 *
 * This function provids the functionality to update the customization
 * information of an object to be the same as the template type and
 * subtype from which it was created.
 *
 * Environment: Internal or External
 *
 * History: Relaeased in NX3
 ************************************************************************/
 extern UFUN_CAMEXPORT int UF_CAM_update_single_object_customization
 (
        tag_t object_tag /*<I> The tag of the object for which the
                               customization should be updated based
                               on template type and subtype */
 );


/***************************************************************************
 *
 * This function provids the functionality to update the customization
 * information of a list of objects to be the same as the template type and
 * subtype from which it was created.
 *
 * Environment: Internal or External
 *
 * History: Relaeased in NX3
 ************************************************************************/
 extern UFUN_CAMEXPORT int UF_CAM_update_list_object_customization
 (
        tag_t *object_tags/*<I> The tags of the objects for which the
                               customization should be updated based
                               on template type and subtype */
);

/*****************************************************************************
 * This function sets the material type for the input object.
 *
 * Environment : Internal  and  External
 * See Also:
 * History : Released in NX6
 ****************************************************************************/
extern UFUN_CAMEXPORT int UF_CAM_set_material
(
    tag_t object_tag,    /* <I>  Tag to input object (cutter or geom group) */
    char *libref        /* <I>  library reference to desired material */
);
/*****************************************************************************
 *  DESCRIPTION:
 *  This utility function computes the center point and the radius of 
 *  least square sphere for a  given set of points.
 *           
 * Environment : Internal  and  External
 *
 * History : Released in NX8.5
 ****************************************************************************/
extern UFUN_CAMEXPORT int UF_CAM_ask_leastsq_sphere
(
    double **point_coords,     /* <I,len:3*point_count>
                                   coordinates of array of points for sphere fit.
                                   (3 * point_count values.)
                                */
    int      point_count,       /* <I> - Number of points   */
    double   tolerance,         /* <I> - Distance tolerance */
    double   sphere_center[3],  /* <O> - Coordinates of sphere center */
    double  *sphere_radius      /* <O> - Sphere radius      */
 );

#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif /* UF_CAM_H_INCLUDED */

