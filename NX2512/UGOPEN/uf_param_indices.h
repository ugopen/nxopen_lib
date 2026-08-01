/******************************************************************************
                   Copyright (c)  1999-2004 Unigraphics Solutions Inc.
                        Unpublished - All Rights Reserved
******************************************************************************/
/*****************************************************************************
 *
 * ###########################################################################
 *    NOTE:
 *        THE FILE uf_param_indices.h SHOULD NOT BE EDITED.  ANY CHANGES
 *        DESIRED IN THIS FILE SHOULD BE MADE IN THE FILE param_indices.h
 *        AND THEN THIS FILE IS GENERATED USING THE GENERATION SCRIPT
 *        make_uf_param_indices.pl located in /cam/bin.  THIS
 *        ENSURES THAT THE FILES REMAIN CONSISTENT.
 * ###########################################################################
 *
 * 
 * 
 * File description:
 *
 *    This file contains the list of available parameter indices in UF CAM.
 *    Each index represents a parameter of an NX data object. The description
 *    of that parameter describes what effect that parameter has on the
 *    behavior of the object that owns it.
 *
 *    The values of these paramaters may be asked for and set via the
 *    UF_PARAM modules. See the UF_PARAM module for other activities that
 *    can be performed on these activites.
 *
 ******************************************************************************/
#ifndef UF_PARAM_INDICES_H_INCLUDED
#define UF_PARAM_INDICES_H_INCLUDED

#include <uf_defs.h>

#ifdef __cplusplus
extern "C" {
#endif




typedef struct UF_PARAM_disp_path_s
{
    double silh_percent;  /* silhouette percentage [1.0 - 100.0] */
    double normx; /* normal on x-direction */
    double normy;  /* normal on y-direction */
    double normz;  /* normal on z-direction */
    short arrow;  /* = 0 (undefined), = 1 (on), = 2 (off) */
    short number;  /* paint line number = 0 (undefined), = 1 (on), = 2 (inactive) */
    short speed;  /* = 0 (off), = 1-10 (on) */
    short type;  /*  = 0 (solid) , = 1 (dash), = 2 (silhouette) */
    short feed;  /* = 0 (undefined), = 1 (on), = 2 (off) */
    short norm_flag; /* paint path normal flag =0 (tool axis),
                                               =1 (i,j,k components) */
                        
} UF_PARAM_disp_path_t;


/* UF_PARAM_DISP_PATH
 *
 *  Description:
 *  This index contains a pointer to a set of parameters to display a tool path
 *
 *  Type: UF_PARAM_type_pointer
 *
 *  Name: Display Path Option
 *  Variable Name: <prefix>_display_path_option
 *
 *  Possible Values: UF_PARAM_disp_path_t
 *
 * 
 */
#define UF_PARAM_DISP_PATH   5  /* UF_PARAM_type_pointer */


typedef struct UF_PARAM_disp_tool_s
{
    short type;      /* display type- off = 0, 2D = 1, 3D = 2, Axis = 3
                        NOTE: Axis is only valid for Variable Axis operations or Method Groups  */
    short frequency; /* tool display frequency */

} UF_PARAM_disp_tool_t;


/* UF_PARAM_DISP_TOOL
 *
 *  Description:
 *  This index contains a pointer to a set of parameters to display a tool
 *
 *  Type: UF_PARAM_type_pointer
 *
 *  Name: Display Tool Options
 *  Variable Name: <prefix>_display_tool_options
 *
 *  Possible Values: UF_PARAM_disp_tool_t
 *
 * 
 */
#define UF_PARAM_DISP_TOOL   6  /* UF_PARAM_type_pointer */


typedef struct UF_PARAM_disp_pattern_s
{
    char name[133];  /* name of pattern */
    double dx;                  /* offset distance to x-direction */
    double dy;                  /* offset distance to y-direction */
    double dz;                  /* offset distance to z-direction */
    short frequency;            /* pattern display frequency */

} UF_PARAM_disp_pattern_t;


/* UF_PARAM_DISP_PATTERN
 *
 *  Description:
 *  This index contains a pointer to a set of parameters to display a pattern
 *
 *  Type: UF_PARAM_type_pointer
 *
 *  Name: Display Pattern Options
 *  Variable Name: <prefix>_display_pattern_options
 *
 *  Possible Values: UF_PARAM_disp_pattern_t
 *
 * 
 */
#define UF_PARAM_DISP_PATTERN   7  /* UF_PARAM_type_pointer */


typedef enum
{
    UF_PARAM_feed_none = 0,
    UF_PARAM_feed_per_minute = 1,
    UF_PARAM_feed_per_revolution = 2

} UF_PARAM_feed_unit_t;

typedef enum
{
    UF_PARAM_spindle_mode_rpm = 0,
    UF_PARAM_spindle_mode_css = 1,
    UF_PARAM_spindle_mode_none = 2

} UF_PARAM_spindle_mode_t;

typedef struct UF_PARAM_feedrate_s
{
    UF_PARAM_feed_unit_t unit;       /* unit of feedrate = 0 (none), = 1 */
    double value;     /* value of feedrate */
    short color;      /* color of feedrate.  For possible color value, refer to uf_obj.h */

} UF_PARAM_feedrate_t;


/* UF_PARAM_FEED_SIDE_CUT
 *
 *  Description:
 *  This index contains a pointer to side cut feedrate structure
 *
 *  Type: UF_PARAM_type_pointer
 *
 *  Name: Feed Side Cut
 *  Variable Name: <prefix>_feed_side_cut
 *
 *  Possible Values: UF_PARAM_feedrate_t
 *
 * 
 */
#define UF_PARAM_FEED_SIDE_CUT   9  /* UF_PARAM_type_pointer */


/* UF_PARAM_FEED_RAPID
 *
 *  Description:
 *  This index contains a pointer to rapid feedrate structure
 *
 *  Type: UF_PARAM_type_pointer
 *
 *  Name: Feed Rapid
 *  Variable Name: <prefix>_feed_rapid
 *
 *  Possible Values: UF_PARAM_feedrate_t
 *
 * 
 */
#define UF_PARAM_FEED_RAPID   10  /* UF_PARAM_type_pointer */


/* UF_PARAM_FEED_ENGAGE
 *
 *  Description:
 *  This index contains a pointer to engage feedrate structure
 *
 *  Type: UF_PARAM_type_pointer
 *
 *  Name: Feed Engage
 *  Variable Name: <prefix>_feed_engage
 *
 *  Possible Values: UF_PARAM_feedrate_t
 *
 * 
 */
#define UF_PARAM_FEED_ENGAGE   11  /* UF_PARAM_type_pointer */


/* UF_PARAM_FEED_RETRACT
 *
 *  Description:
 *  This index contains a pointer to retract feedrate structure
 *
 *  Type: UF_PARAM_type_pointer
 *
 *  Name: Feed Retract
 *  Variable Name: <prefix>_feed_retract
 *
 *  Possible Values: UF_PARAM_feedrate_t
 *
 * 
 */
#define UF_PARAM_FEED_RETRACT   12  /* UF_PARAM_type_pointer */


/* UF_PARAM_FEED_APPROACH
 *
 *  Description:
 *  This index contains a pointer to approach feedrate structure
 *
 *  Type: UF_PARAM_type_pointer
 *
 *  Name: Feed Approach
 *  Variable Name: <prefix>_feed_approach
 *
 *  Possible Values: UF_PARAM_feedrate_t
 *
 * 
 */
#define UF_PARAM_FEED_APPROACH   13  /* UF_PARAM_type_pointer */


/* UF_PARAM_FEED_DEPARTURE
 *
 *  Description:
 *  This index contains a pointer to departure feedrate structure
 *
 *  Type: UF_PARAM_type_pointer
 *
 *  Name: Feed Departure
 *  Variable Name: <prefix>_feed_departure
 *
 *  Possible Values: UF_PARAM_feedrate_t
 *
 * 
 */
#define UF_PARAM_FEED_DEPARTURE   14  /* UF_PARAM_type_pointer */


/* UF_PARAM_FEED_RETURN
 *
 *  Description:
 *  This index contains a pointer to return feedrate structure
 *
 *  Type: UF_PARAM_type_pointer
 *
 *  Name: Feed Return
 *  Variable Name: <prefix>_feed_return
 *
 *  Possible Values: UF_PARAM_feedrate_t
 *
 * 
 */
#define UF_PARAM_FEED_RETURN   15  /* UF_PARAM_type_pointer */


/* UF_PARAM_FEED_TRAVERSAL
 *
 *  Description:
 *  This index contains a pointer to traversal feedrate structure
 *
 *  Type: UF_PARAM_type_pointer
 *
 *  Name: Feed Traversal
 *  Variable Name: <prefix>_feed_traversal
 *
 *  Possible Values: UF_PARAM_feedrate_t
 *
 * 
 */
#define UF_PARAM_FEED_TRAVERSAL   16  /* UF_PARAM_type_pointer */


/* UF_PARAM_FEED_CUT
 *
 *  Description:
 *  This index contains a pointer to cut feedrate structure
 *
 *  Type: UF_PARAM_type_pointer
 *
 *  Name: Feed Cut
 *  Variable Name: <prefix>_feed_cut
 *
 *  Possible Values: UF_PARAM_feedrate_t
 *
 * 
 */
#define UF_PARAM_FEED_CUT   17  /* UF_PARAM_type_pointer */


/* UF_PARAM_FEED_FIRST_CUT
 *
 *  Description:
 *  This index contains a pointer to first cut feedrate structure
 *
 *  Type: UF_PARAM_type_pointer
 *
 *  Name: Feed First_Cut
 *  Variable Name: <prefix>_feed_first_cut
 *
 *  Possible Values: UF_PARAM_feedrate_t
 *
 * 
 */
#define UF_PARAM_FEED_FIRST_CUT   18  /* UF_PARAM_type_pointer */


/* UF_PARAM_FEED_STEPOVER
 *
 *  Description:
 *  This index contains a pointer to stepover feedrate structure
 *
 *  Type: UF_PARAM_type_pointer
 *
 *  Name: Feed Stepover
 *  Variable Name: <prefix>_feed_stepover
 *
 *  Possible Values: UF_PARAM_feedrate_t
 *
 * 
 */
#define UF_PARAM_FEED_STEPOVER   19  /* UF_PARAM_type_pointer */


/* UF_PARAM_CORNER_CONTROL_METHOD
 *
 *  Description:  corner control method
 *
 *  Type: UF_PARAM_type_int
 *
 *  Name: Corner Control Method
 *  Variable Name: <prefix>_corner_control_method
 *  Possible Values:
 *
 *  FOR LATHE:
 *                0 = UNDEFINED
 *                1 = ROLL AROUND (ADD ARCS)
 *                2 = CLEAR CORNER (EXTEND TANGENTS)
 *                3 = ROUND CORNER
 *                4 = CHAMFER CORNER
 *  FOR 2-2 1/2 AXIS MILL:
 *                0 = UNDEFINED
 *                1 = ACTIVE (ADD ARCS)
 *                2 = INACTIVE (EXTEND TANGENTS)
 *  FOR 3-5 AXIS MILL:
 *                0 = UNDEFINED
 *                1 = NO CORNER CONTROL
 *                2 = ISSUE WARNING
 *                3 = LIFT UNTIL PAST CORNER
 *                4 = USE TANGENT EXTENSIONS
 *                5 = STOP PROCESSING
 *
 * 
 */
#define UF_PARAM_CORNER_CONTROL_METHOD   24  /* UF_PARAM_type_int */


/* UF_PARAM_FROM_STATUS
 *
 *  Description:  From point status
 *
 *  Type: UF_PARAM_type_int
 *
 *  Name: From Status
 *  Variable Name: <prefix>_from_status
 *
 *  Possible Values:
 *                 0 = undefined
 *                 1 = active
 *                 2 = inactive
 *
 * 
 */
#define UF_PARAM_FROM_STATUS   27  /* UF_PARAM_type_int */


typedef enum
{
    UF_PARAM_turn_return_method_automatic = 0,
    UF_PARAM_turn_return_method_direct,
    UF_PARAM_turn_return_method_radial_then_axial,
    UF_PARAM_turn_return_method_axial_then_radial,
    UF_PARAM_turn_return_method_clear_radial_then_direct,
    UF_PARAM_turn_return_method_clear_axial_then_direct,
    UF_PARAM_turn_return_method_clear_radial_only,
    UF_PARAM_turn_return_method_clear_axial_only
} UF_PARAM_turn_return_method_t, *UF_PARAM_turn_return_method_p_t;

/* UF_PARAM_RETURN_METHOD
 *
 *  Description:
 *     This parameter defines the strategy how the tool is moved from the
 *     operation's last tool position to the return point.
 *     This parameter is used by multiple operation types and its definition
 *     depends on the operation being parameterized (see below for possible
 *     values).
 *
 *  Type: UF_PARAM_type_int
 *
 *  Name: Return Method
 *  Variable Name: <prefix>_return_method
 *
 *  Possible Values: 
 *     For Turning use: UF_PARAM_turn_return_method_t
 *     else use:
 *                 0 = AUTOMATIC
 *                 1 = DIRECT MOVE
 *                 2 = VERTICAL THEN HORIZONTAL
 *                 3 = HORIZONTAL THEN VERTICAL
 *                 4 = VERTICAL CLEARANCE PLANE THEN DIRECT
 *                 5 = HORIZONTAL CLEARANCE PLANE THEN DIRECT
 *                 6 = VERTICAL CLEARANCE
 *                 7 = HORIZONTAL CLEARANCE
 *                 8 = VERTICAL THEN HORIZONTAL THEN DIRECT (ID ONLY)
 *                 9 = VERTICAL THEN HORIZONTAL THEN VERTICAL (ID ONLY)
 *                10 = VERTICAL THEN TO HORIZONTAL CLEARANCE (ID ONLY)
 *
 * 
 */
#define UF_PARAM_RETURN_METHOD   30  /* UF_PARAM_type_int */


/* UF_PARAM_RETURN_STATUS
 *
 *  Description: (Return point status)
 *     This parameter specifies the avoidance return status.
 *
 *  Type: UF_PARAM_type_int
 *
 *  Name: Return Status
 *  Variable Name: <prefix>_return_status
 *
 *  Possible Values:
 *                  = 0 - undefined,
 *                  = 1 - active,
 *                  = 2 - inactive
 *
 * 
 */
#define UF_PARAM_RETURN_STATUS   32  /* UF_PARAM_type_int */


/* UF_PARAM_GOHOME_STATUS
 *
 *  Description:  Gohome point status
 *
 *  Type: UF_PARAM_type_int
 *
 *  Name: Gohome Status
 *  Variable Name: <prefix>_gohome_status
 *
 *  Possible Values:
 *                  = 0 - undefined,
 *                  = 1 - active,
 *                  = 2 - inactive,
 *                  = 3 - use from position,
 *                  = 4 - output 'GOHOME
 *
 * 
 */
#define UF_PARAM_GOHOME_STATUS   34  /* UF_PARAM_type_int */


/* UF_PARAM_BOUNDARY_TOL
 *
 *   Description:
 *      This parameters specifies boundary Tolerances
 *
 *   Type: UF_PARAM_type_2d_length
 *
 *   Name: Boundary Tolerances
 *  Variable Name: <prefix>_boundary_tolerances
 *
 *   Possible Values: Positive doubles
 *
 *
 * 
 */
#define UF_PARAM_BOUNDARY_TOL   37  /* UF_PARAM_type_2d_length */


/* UF_PARAM_RCS_LINKED_TO_MCS
 *
 *  Description:  the status of RCS linked to MCS
 *
 *  Type: UF_PARAM_type_logical
 *
 *  Name: RCS Linked To MCS Status
 *  Variable Name: <prefix>_rcs_linked_to_mcs_status
 *
 *  Possible Values:
 *                 = FALSE - not linked
 *                 = TRUE -  linked
 *
 * 
 */
#define UF_PARAM_RCS_LINKED_TO_MCS   41  /* UF_PARAM_type_logical */


/* UF_PARAM_CLR_MIN
 *
 *  Description:  Minimum clearance distance (safe distance)
 *
 *  Type: UF_PARAM_type_double_length
 *
 *  Name: Clearance Min
 *  Variable Name: <prefix>_clearance_min
 *
 *  Possible Values: zero or positive UF_PARAM_type_double_length
 *
 * 
 */
#define UF_PARAM_CLR_MIN   42  /* UF_PARAM_type_double_length  */


typedef enum
{
    UF_PARAM_turn_start_method_direct = 0,
    UF_PARAM_turn_start_method_radial_then_axial,
    UF_PARAM_turn_start_method_axial_then_radial,
    UF_PARAM_turn_start_method_clear_radial_then_direct,
    UF_PARAM_turn_start_method_clear_axial_then_direct
} UF_PARAM_turn_start_method_t, *UF_PARAM_turn_start_method_p_t;

/* UF_PARAM_START_METHOD
 *
 *  Description:
 *     This parameter defines the strategy how the tool is moved from the
 *     last tool position to the operation's start point.
 *     This parameter is used by multiple operation types and it's definition
 *     depends on the operation being parameterized (see below for possible
 *     values).
 *
 *  Type: UF_PARAM_type_int
 *
 *  Name: Start Method
 *  Variable Name: <prefix>_start_method
 *
 *  Possible Values:
 *     For Turning use: UF_PARAM_turn_start_method_t
 *     else use:
 *                 0 = UNDEFINED
 *                 1 = DIRECT MOVE
 *                 2 = VERTICAL THEN HORIZONTAL
 *                 3 = HORIZONTAL THEN VERTICAL
 *                 4 = HORIZONTAL CLEARANCE THEN DIRECT
 *                 5 = VERTICAL CLEARANCE THEN DIRECT
 *
 * 
 */
#define UF_PARAM_START_METHOD   45  /* UF_PARAM_type_int */


/* UF_PARAM_START_STATUS
 *
 *  Description:  start point status
 *
 *  Type: UF_PARAM_type_int
 *
 *  Name: Start Status
 *  Variable Name: <prefix>_start_status
 *
 *  Possible Values:
 *                = 0 - undefined,
 *                = 1 - active,
 *                = 2 - inactive
 *
 * 
 */
#define UF_PARAM_START_STATUS   47  /* UF_PARAM_type_int */


typedef enum
{
    UF_PARAM_turn_start_of_engage_method_automatic = 0,
    UF_PARAM_turn_start_of_engage_method_direct,
    UF_PARAM_turn_start_of_engage_method_radial_then_axial,
    UF_PARAM_turn_start_of_engage_method_axial_then_radial,
    UF_PARAM_turn_start_of_engage_method_clear_radial_then_direct,
    UF_PARAM_turn_start_of_engage_method_clear_axial_then_direct
} UF_PARAM_turn_start_of_engage_method_t, *UF_PARAM_turn_start_of_engage_method_p_t;

/* UF_PARAM_START_OF_ENGAGE_METHOD
 *
 *  Description:
 *     This parameter defines the strategy how the tool is moved from the
 *     last tool position to the operation's start of engage point.
 *
 *  Type: UF_PARAM_type_int
 *
 *  Name: Start of Engage Method
 *  Variable Name: <prefix>_start_of_engage_method
 *
 *  Possible Values: UF_PARAM_turn_start_ofengage_method_t
 *
 * 
 */
#define UF_PARAM_START_OF_ENGAGE_METHOD   48  /* UF_PARAM_type_int */


typedef enum
{
    UF_PARAM_turn_gohome_method_direct = 0,
    UF_PARAM_turn_gohome_method_radial_then_axial,
    UF_PARAM_turn_gohome_method_axial_then_radial,
    UF_PARAM_turn_gohome_method_clear_radial_then_direct,
    UF_PARAM_turn_gohome_method_clear_axial_then_direct
} UF_PARAM_turn_gohome_method_t, UF_PARAM_turn_gohome_method_p_t;

/* UF_PARAM_GOHOME_METHOD
 *
 *  Description:
 *     This parameter defines the strategy how the tool is moved from the
 *     last tool position to the operation's gohome point.
 *
 *  Type: UF_PARAM_type_int
 *
 *  Name: Gohome Method
 *  Variable Name: <prefix>_gohome_method
 *
 *  Possible Values: UF_PARAM_turn_gohome_method_t
 *
 * 
 */
#define UF_PARAM_GOHOME_METHOD   49  /* UF_PARAM_type_int */


/* UF_PARAM_STOCK_DRIVE
 *
 *   Description:
 *      Stock for drive geometry 
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Stock Drive
 *  Variable Name: <prefix>_stock_drive
 *
 *   Possible Values: double
 *
 * 
 */
#define UF_PARAM_STOCK_DRIVE   54  /*  UF_PARAM_type_double_length */


typedef enum UF_PARAM_motion_output_e
{
    UF_PARAM_motion_output_linear_only = -1,
    UF_PARAM_motion_output_cir_perp_to_taxis = 0,
    UF_PARAM_motion_output_cir_perp_parallel_to_taxis = 1,
    UF_PARAM_motion_output_nurbs = 2
} UF_PARAM_motion_output_t;


/* UF_PARAM_MOTION_OUTPUT_TYPE
 *
 *   Description:
 *     Type of motions output to the tool path
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Motion Output Type
 *  Variable Name: <prefix>_motion_output_type
 *
 *   Possible Values: UF_PARAM_motion_output_t
 *
 * 
 */
#define UF_PARAM_MOTION_OUTPUT_TYPE   55  /* UF_PARAM_type_int */


typedef enum UF_PARAM_nurbs_output_flag_e
{
    UF_PARAM_nurbs_output_flag_join_segment_off = 0,
    UF_PARAM_nurbs_output_flag_join_segment_on = 1
} UF_PARAM_nurbs_output_flag_t;


/* UF_PARAM_NURBS_OP
 *
 *   Description:
 *      NURBS Output Flag to join segments
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: NURBS Joining Segments Flag
 *  Variable Name: <prefix>_nurbs_joining_segments_flag
 *
 *   Possible Values: UF_PARAM_nurbs_output_flag_t
 *
 * 
 */
#define UF_PARAM_NURBS_OP   56  /* UF_PARAM_type_int */


/* UF_PARAM_NURBS_FIT_TOL
 *
 *   Description:
 *      NURBS fitting tolerance
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: NURBS Fitting Tolerance
 *  Variable Name: <prefix>_nurbs_fitting_tolerance
 *
 *   Possible Values: UF_PARAM_type_double_length
 *
 * 
 */
#define UF_PARAM_NURBS_FIT_TOL   57  /*   */


/* UF_PARAM_NURBS_ANG_TOL
 *
 *   Description:
 *      NURBS angle tolerance
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: NURBS Angular Tolerance
 *  Variable Name: <prefix>_nurbs_angular_tolerance
 *
 *   Possible Values: UF_PARAM_type_double
 *
 * 
 */
#define UF_PARAM_NURBS_ANG_TOL   58  /*   */


/* UF_PARAM_MCS
 *
 *   Description:
 *      Machine coordinate system
 *
 *   Type: UF_PARAM_type_tag
 *
 *   Name: MCS
 *  Variable Name: <prefix>_mcs
 *
 *   Possible Values: tag 
 *
 *
 *
 * 
 */
#define UF_PARAM_MCS   59  /* UF_PARAM_type_tag */


/* UF_PARAM_RCS
 *
 *   Description:
 *      Reference coordinate system
 *
 *   Type: UF_PARAM_type_tag
 *
 *   Name: RCS
 *  Variable Name: <prefix>_rcs
 *
 *   Possible Values:
 *
 * 
 */
#define UF_PARAM_RCS   60  /* Param_type_tag */


/* UF_PARAM_FIXTURE_OFFSET_STATUS
 *
 *   Description:
 *     Fixture offset status
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Fixture offset status
 *  Variable Name: <prefix>_fixture_offset_status
 *
 *   Possible Values: 0/1 (on/off)
 *
 * 
 */
#define UF_PARAM_FIXTURE_OFFSET_STATUS   61  /* Param_type_int */


/* UF_PARAM_FIXTURE_OFFSET_NUM
 *
 *   Description:
 *      Fixture offset value
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Fixture offset value
 *  Variable Name: <prefix>_fixture_offset_value
 *
 *   Possible Values:
 *
 * 
 */
#define UF_PARAM_FIXTURE_OFFSET_NUM   62  /* Param_type_int */


typedef enum
{
    UF_PARAM_scs_type_use_xm_ym = 0,
    UF_PARAM_scs_type_use_zm_xm = 1,
    UF_PARAM_scs_type_undefined = 2
} UF_PARAM_scs_type_t;

/* UF_PARAM_SCS_TYPE
 *
 *   Description:
 *      Spindle coordinate system definition type
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Spindle Definition Type
 *  Variable Name: <prefix>_spindle_definition_type
 *
 *   Possible Values: UF_PARAM_scs_type_t
 *
 * 
 */
#define UF_PARAM_SCS_TYPE   64  /* UF_PARAM_type_int */


/* UF_PARAM_SUPPRESS_PATH_DISPLAY
 *
 *  Description:
 *  This index contains a toggle indicating whether to suppress the display of 
 *    a tool path while it is being computed.
 *
 *  Type: UF_PARAM_type_int
 *
 *  Name: Suppress Path Display Option
 *  Variable Name: <prefix>_suppress_path_display_option
 *
 *  Possible Values: 0 = Do not suppress display of the tool path during generation
 *                   1 = Suppress display of the tool path during path generation
 *
 * 
 */
#define UF_PARAM_SUPPRESS_PATH_DISPLAY   65  /* UF_PARAM_type_int */


typedef enum
{
    UF_PARAM_csys_purpose_local = 0,
    UF_PARAM_csys_purpose_main
} UF_PARAM_csys_purpose_t;

/* UF_PARAM_CSYS_PURPOSE
 *
 *  Description:
 *
 *  Type: UF_PARAM_type_int
 *
 *  Name: Coordinate System Purpose
 *  Variable Name: <prefix>_coordinate_system_purpose
 *
 *  Possible Values: UF_PARAM_csys_purpose_t
 *
 * 
 */
#define UF_PARAM_CSYS_PURPOSE   66  /* UF_PARAM_type_int*/


typedef enum
{
    UF_PARAM_special_output_none = 0,
    UF_PARAM_special_output_use_main_mcs,
    UF_PARAM_special_output_fixture_offset,
    UF_PARAM_special_output_csys_rotation
} UF_PARAM_special_output_t;

/* UF_PARAM_SPECIAL_OUTPUT
 *
 *  Description:
 *
 *  Type: UF_PARAM_type_int
 *
 *  Name: Special Output
 *  Variable Name: <prefix>_special_output
 *
 *  Possible Values: UF_PARAM_special_output_t
 *
 * 
 */
#define UF_PARAM_SPECIAL_OUTPUT   67  /* UF_PARAM_type_int*/


/* UF_PARAM_TEMPLATE_TYPE
 *
 *   Description:
 *      Object template type
 *
 *   Type: UF_PARAM_type_string
 *
 *   Name: Template Type
 *  Variable Name: <prefix>_template_type
 *
 *   Possible Values:
 *
 * 
 */
#define UF_PARAM_TEMPLATE_TYPE   105  /* UF_PARAM_type_string */


/* UF_PARAM_TEMPLATE_SUBTYPE
 *
 *   Description:
 *      Tepmlate subtype
 *
 *   Type: UF_PARAM_type_string
 *
 *   Name: "Template Subtype
 *  Variable Name: <prefix>__template_subtype
 *
 *   Possible Values:
 *
 * 
 */
#define UF_PARAM_TEMPLATE_SUBTYPE   106  /* UF_PARAM_type_string */


/* UF_PARAM_TOL_IN_OUT
 *
 *   Description:
 *      Inside outside tolerance
 *
 *   Type: UF_PARAM_type_2d_length
 *
 *   Name: Inside Outside Tolerances
 *  Variable Name: <prefix>_inside_outside_tolerances
 *
 *   Possible Values:
 *
 * 
 */
#define UF_PARAM_TOL_IN_OUT   109  /* UF_PARAM_type_2d_length */


/* UF_PARAM_OUTPUT_LOAD_TOOL
 *
 *   Description:
 *      Flag indicatiing the LOAD/TOOL post command to be output
 *      when marker is added
 *   Type: UF_PARAM_type_logical
 *
 *   Name: Output load tool Status
 *  Variable Name: <prefix>_output_load_tool_status
 *
 *   Possible Values: True/False
 *
 * 
 */
#define UF_PARAM_OUTPUT_LOAD_TOOL   117 


/* UF_PARAM_DIAGNOSTICS
 *
 *   Description:
 *      During the process of generating an operation, if any
 *      conditions are encountered, The parameter will contain
 *      the error codes of the condition found.
 *      It will only support a maximum of 10 conditions.
 *      Any message associated with the error codes can be
 *      inquired like any other error codes.
 *      If the parameter does not exist, then no conditions were
 *      encountered.
 *      NOTE: This parameter is removed from an operation
 *      everytime the operation is generated.
 *
 *   Type: UF_PARAM_type_vla_int
 *
 *   Name: Diagnositics array
 *  Variable Name: <prefix>_diagnositics_array
 *
 *   Possible Values: array of positive integers
 *
 * 
 */
#define UF_PARAM_DIAGNOSTICS   123  /* UF_PARAM_type_vla_int */


typedef enum
{
    UF_PARAM_corner_cir_feed_comp_off = 0,
    UF_PARAM_corner_cir_feed_comp_on  = 1
} UF_PARAM_corner_cir_feed_comp_t;


/* UF_PARAM_CORNER_CIR_FEED_COMP
 *
 *   Description:
 *      Parameter indicates whether Circular
 *      Feedrate Compensation is on or off.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Corner Circular Feed Compensation
 *  Variable Name: <prefix>_corner_circular_feed_compensation
 *
 *   Possible Values: UF_PARAM_corner_cir_feed_comp_t
 *
 * 
 */
#define UF_PARAM_CORNER_CIR_FEED_COMP   201  /* UF_PARAM_type_int */


typedef enum
{
    UF_PARAM_corner_fillet_type_none       = 0,
    UF_PARAM_corner_fillet_type_all_passes = 1

} UF_PARAM_corner_fillet_type_t;


/* UF_PARAM_CORNER_FILLET_TYPE
 *
 *   Description:
 *      Parameter indicates filleting types at corners of
 *      the toolpaths.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Corner Fillet Type
 *  Variable Name: <prefix>_corner_fillet_type
 *
 *   Possible Values: UF_PARAM_corner_fillet_type_t
 *
 * 
 */
#define UF_PARAM_CORNER_FILLET_TYPE   202  /* UF_PARAM_type_int */


/* UF_PARAM_CORNER_FILLET_PATH_RADIUS
 *
 *   Description:
 *      Paramter is the radius of corner fillet.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Corner Fillet Path Radius
 *  Variable Name: <prefix>_corner_fillet_path_radius
 *
 *   Possible Values: positive UF_PARAM_type_double_length.
 *
 * 
 */
#define UF_PARAM_CORNER_FILLET_PATH_RADIUS   203  /* UF_PARAM_type_double_length */


/* UF_PARAM_CORNER_MAX_TLAXIS
 *
 *   Description: Maximum tool axis change at corner.
 *
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Corner Max Tool Axis
 *  Variable Name: <prefix>_corner_max_tool_axis
 *
 *   Possible Values:
 *
 * 
 */
#define UF_PARAM_CORNER_MAX_TLAXIS   204  /* UF_PARAM_type_double */


/* UF_PARAM_CORNER_MAX_ANGLE
 *
 *   Description:
 *      Parameter is the maximum angle for corner control,
 *         i.e. for corner filleting of corner slowdowns.
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Corner Max Included Angle
 *  Variable Name: <prefix>_corner_max_included_angle
 *
 *   Possible Values: 0.0 < maximum angle < 180.0.
 *
 * 
 */
#define UF_PARAM_CORNER_MAX_ANGLE   205  /* UF_PARAM_type_double */


/* UF_PARAM_CORNER_MIN_ANGLE
 *
 *   Description:
 *      Parameter is the minimum angle for corner control,
 *         i.e. for corner filleting of corner slowdowns.
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Corner Min Included Angle
 *  Variable Name: <prefix>_corner_min_included_angle
 *
 *   Possible Values: 0.0 <= minimum angle < 180.0
 *
 * 
 */
#define UF_PARAM_CORNER_MIN_ANGLE   206  /* UF_PARAM_type_double */


typedef enum
{
    UF_PARAM_corner_slowdown_status_off = 0,
    UF_PARAM_corner_slowdown_status_on  = 1

} UF_PARAM_corner_slowdown_status_t;


/* UF_PARAM_CORNER_SLOWDOWN_STATUS
 *
 *   Description:
 *      Parameter indicates whether corner slowdown
 *      is on or off.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Corner Slowdown Status
 *  Variable Name: <prefix>_corner_slowdown_status
 *
 *   Possible Values: UF_PARAM_corner_slowdown_status_t
 *
 * 
 */
#define UF_PARAM_CORNER_SLOWDOWN_STATUS   207  /* UF_PARAM_type_int */


typedef enum
{
    UF_PARAM_corner_slowdown_length_method_previous_tool = 0,
    UF_PARAM_corner_slowdown_length_method_percent_tool  = 1

} UF_PARAM_corner_slowdown_length_method_t;


/* UF_PARAM_CORNER_SLOWDOWN_LENGTH_METHOD
 *
 *   Description:
 *      Parameter determines which slowdown method
 *      is to be used if slowdowns are on.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Corner Slowdown Length Method
 *  Variable Name: <prefix>_corner_slowdown_length_method
 *
 *   Possible Values: UF_PARAM_corner_slowdown_length_method_t
 *
 * 
 */
#define UF_PARAM_CORNER_SLOWDOWN_LENGTH_METHOD   208  /* UF_PARAM_type_int */


/* UF_PARAM_CORNER_TL_DIAM_PERCENT
 *
 *   Description:
 *      Parameter, used by corner slowdown if the
 *      Percent Tool method is selected, is 100.0
 *      times the ratio of the slowdown length to
 *      the tool diameter.
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Corner Tool Diameter Percent
 *  Variable Name: <prefix>_corner_tool_diameter_percent
 *
 *   Possible Values:  positive UF_PARAM_type_double
 *
 * 
 */
#define UF_PARAM_CORNER_TL_DIAM_PERCENT   209  /* UF_PARAM_type_double */


/* UF_PARAM_CORNER_NUM_STEPS
 *
 *   Description:
 *      Parameter is the number of decrements
 *      in feedrate used to accomplish a slowdown.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Corner Slowdown Num Steps
 *  Variable Name: <prefix>_corner_slowdown_num_steps
 *
 *   Possible Values: positive UF_PARAM_type_int
 *
 * 
 */
#define UF_PARAM_CORNER_NUM_STEPS   210  /* UF_PARAM_type_int */


/* UF_PARAM_CORNER_PREV_TL_DIAM
 *
 *   Description:
 *      Parameter, used by corner slowdown if the
 *      previous tool diameter method is selected,
 *      is the tool diameter of the last tool used
 *      in cutting a part.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Corner Previous Tool Diameter
 *  Variable Name: <prefix>_corner_previous_tool_diameter
 *
 *   Possible Values: positive UF_PARAM_type_double_length
 *
 * 
 */
#define UF_PARAM_CORNER_PREV_TL_DIAM   211  /* UF_PARAM_type_double_length */


/* UF_PARAM_CORNER_FEED_ADJUST_PERCENT
 *
 *   Description:
 *      Parameter, used by corner slowdown only, is
 *      the 100 times the ratio of the feedrate at
 *      the end of a slowdown to the feedrate at the
 *      start of a slowdown.
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Corner Feed Adjust Percent
 *  Variable Name: <prefix>_corner_feed_adjust_percent
 *
 *   Possible Values: positive UF_PARAM_type_double
 *
 * 
 */
#define UF_PARAM_CORNER_FEED_ADJUST_PERCENT   212  /* UF_PARAM_type_double */


typedef enum
{
    UF_PARAM_engret_auto_type_linear   = 0,
    UF_PARAM_engret_auto_type_circular = 1

} UF_PARAM_engret_auto_type_t;


/* UF_PARAM_ENGRET_AUTO_TYPE
 *
 *   Description:
 *      Parmeter denotes the type of automatic
 *      engages and retracts currently selected.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Engage Retract Auto Type
 *  Variable Name: <prefix>_engage_retract_auto_type
 *
 *   Possible Values: 0 - linear
 *                    1 - circular
 *
 * 
 */
#define UF_PARAM_ENGRET_AUTO_TYPE   214  /* UF_PARAM_type_int */


/* UF_PARAM_ENGRET_AUTO_OVERLAP
 *
 *   Description:
 *      Parameter is the overlap distance used by
 *      automatic engages and automatic retracts.
 *      (It is used only when a closed path is cut.)
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Engage Retract Auto Overlap
 *  Variable Name: <prefix>_engage_retract_auto_overlap
 *
 *   Possible Values: non-negative UF_PARAM_type_double_length
 *
 * 
 */
#define UF_PARAM_ENGRET_AUTO_OVERLAP   215  /* UF_PARAM_type_double_length */


/* UF_PARAM_ENGRET_AUTO_RADIUS
 *
 *   Description:
 *      Parameter is the arc radius used for
 *      circular engages and circular retracts.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Engage Retract Auto Radius
 *  Variable Name: <prefix>_engage_retract_auto_radius
 *
 *   Possible Values: positive UF_PARAM_type_double_length
 *
 * 
 */
#define UF_PARAM_ENGRET_AUTO_RADIUS   216  /* UF_PARAM_type_double_length */


/* UF_PARAM_ENGRET_AUTO_ACTIVE_RANGE
 *
 *   Description:
 *      Parameter is the activation range used by
 *      automatic engages and retracts.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Engage Retract Auto Activation Range
 *  Variable Name: <prefix>_engage_retract_auto_activation_range
 *
 *   Possible Values: UF_PARAM_type_double_length
 *
 * 
 */
#define UF_PARAM_ENGRET_AUTO_ACTIVE_RANGE   217  /* UF_PARAM_type_double_length */


typedef enum
{
    UF_PARAM_eng_auto_ramp_method_ramp_on_lines          = 1,
    UF_PARAM_eng_auto_ramp_method_ramp_on_lines_and_arcs = 2,
    UF_PARAM_eng_auto_ramp_method_helical_ramping        = 3

} UF_PARAM_eng_auto_ramp_method_t;


/* UF_PARAM_ENG_AUTO_RAMP_METHOD
 *
 *   Description:
 *      Parameter denotes the type of ramping
 *      to be used if automatic engages are active.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Engage Auto Ramp Method
 *  Variable Name: <prefix>_engage_auto_ramp_method
 *
 *   Possible Values: UF_PARAM_eng_auto_ramp_method_t
 *
 * 
 */
#define UF_PARAM_ENG_AUTO_RAMP_METHOD   218  /* UF_PARAM_type_int */


/* UF_PARAM_ENG_AUTO_RAMP_ANGLE
 *
 *   Description:
 *      Parameter is the ramping angle used by
 *      automatic engages when ramping is required.
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Engage Auto Ramp Angle
 *  Variable Name: <prefix>_engage_auto_ramp_angle
 *
 *   Possible Values: UF_PARAM_type_double
 *                    0 < ramp angle < 90
 *
 * 
 */
#define UF_PARAM_ENG_AUTO_RAMP_ANGLE   219  /* UF_PARAM_type_double */


typedef enum
{
    UF_PARAM_clrplane_undefined           = 0,
    UF_PARAM_clrplane_define_and_active   = 1,
    UF_PARAM_clrplane_define_and_inactive = 2

} UF_PARAM_clrplane_status_t;


/* UF_PARAM_CLRPLANE_STATUS
 *
 *   Description:
 *      Parameter is the clearance plane status.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Clearance Plane Status
 *  Variable Name: <prefix>_clearance_plane_status
 *
 *   Possible Values: UF_PARAM_clrplane_status_t
 *
 * 
 */
#define UF_PARAM_CLRPLANE_STATUS   220  /* UF_PARAM_type_int */


typedef enum
{
    UF_PARAM_clrplane_usage_at_operation_start_and_end    = 1,
    UF_PARAM_clrplane_usage_at_operation_start_only       = 2,
    UF_PARAM_clrplane_usage_at_operation_end_only         = 3,
    UF_PARAM_clrplane_usage_at_start_min_clearance_at_end = 4,
    UF_PARAM_clrplane_usage_at_end_min_clearance_at_start = 5

} UF_PARAM_clrplane_usage_t;


/* UF_PARAM_CLRPLANE_USAGE
 *
 *   Description:
 *      Parameter denotes when a move to or from the
 *      clearance plane is to be made. (Parameter is not
 *      used unless UF_PARAM_CLRPLANE_STATUS is 1.)
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Clearance Plane Usage
 *  Variable Name: <prefix>_clearance_plane_usage
 *
 *   Possible Values: UF_PARAM_clrplane_usage_t
 *
 * 
 */
#define UF_PARAM_CLRPLANE_USAGE   221  /* UF_PARAM_type_int */


/* UF_PARAM_ENG_AUTO_MIN_RAMP_LENGTH
 *
 *   Description:
 *      Parameter is the minimum ramp length
 *      used by automatic engages when ramping 
 *      is required.  
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Engage Auto Minimum Ramp Length
 *  Variable Name: <prefix>_engage_auto_minimum_ramp_length
 *
 *   Possible Values: positive UF_PARAM_type_double
 *
 * 
 */
#define UF_PARAM_ENG_AUTO_MIN_RAMP_LENGTH   224  /* UF_PARAM_type_double */


/* UF_PARAM_ENG_AUTO_HELICAL_DIAMETER
 *
 *   Description:
 *      Parameter is the helical diameter, presented as 
 *      percentage 0f tool diameter,
 *      used by automatic engages when helical ramping 
 *      is required.  
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Engage Auto Helical Diameter
 *  Variable Name: <prefix>_engage_auto_helical_diameter
 *
 *   Possible Values: positive UF_PARAM_type_double
 *
 * 
 */
#define UF_PARAM_ENG_AUTO_HELICAL_DIAMETER   225  /* UF_PARAM_type_double */


typedef enum
{
    UF_PARAM_lwplane_status_undefined            = 0,
    UF_PARAM_lwplane_status_defined_and_active   = 1,
    UF_PARAM_lwplane_status_defined_and_inactive = 2

} UF_PARAM_lwplane_status_t;


/* UF_PARAM_LWPLANE_STATUS
 *
 *   Description:
 *      Parameter is the status of lower limit plane
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Lower Plane Status
 *  Variable Name: <prefix>_lower_plane_status
 *
 *   Possible Values: UF_PARAM_lwplane_status_t
 *
 * 
 */
#define UF_PARAM_LWPLANE_STATUS   226  /* UF_PARAM_type_int */


typedef enum
{
    UF_PARAM_output_warning_only                      = 0,
    UF_PARAM_project_to_lwplane_along_normal_to_plane = 1,
    UF_PARAM_project_to_lwplane_along_tool_axis       = 2

} UF_PARAM_lwplane_usage_t;


/* UF_PARAM_LWPLANE_USAGE
 *
 *   Description:
 *      Parameter denotes the action to be taken when
 *      an active lower limit plane (LLP) exits and
 *      the tool end is below the LLP.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Lower Plane Usage
 *  Variable Name: <prefix>_lower_plane_usage
 *
 *   Possible Values: UF_PARAM_lwplane_usage_t
 *
 * 
 */
#define UF_PARAM_LWPLANE_USAGE   229  /* UF_PARAM_type_int */


typedef enum
{
    UF_PARAM_cutcom_type_none           = 0,
    UF_PARAM_cutcom_type_engage_retract = 1,
    UF_PARAM_cutcom_type_against_wall   = 2

} UF_PARAM_cutcom_type_t;


/* UF_PARAM_CUTCOM_TYPE
 *
 *   Description:
 *      Parameter indicates what kind of
 *      cutcom, if any, is to be performed.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Cutcom Type
 *  Variable Name: <prefix>_cutcom_type
 *
 *   Possible Values: UF_PARAM_cutcom_type_t
 *
 * 
 */
#define UF_PARAM_CUTCOM_TYPE   230  /* UF_PARAM_type_int */


/* UF_PARAM_CUTCOM_ANGLE
 *
 *   Description:
 *      Parameter is the minimum angle allowed
 *      a cutcom move and a cut move.
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Cutcom Angle
 *  Variable Name: <prefix>_cutcom_angle
 *
 *   Possible Values: non-negative UF_PARAM_type_double
 *
 * 
 */
#define UF_PARAM_CUTCOM_ANGLE   231  /* UF_PARAM_type_double */


/* UF_PARAM_CUTCOM_DIST
 *
 *   Description:
 *      Parameter is the minimum length
 *      of a cutcom move.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Cutcom Distance
 *  Variable Name: <prefix>_cutcom_distance
 *
 *   Possible Values: positive UF_PARAM_type_double_length
 *
 * 
 */
#define UF_PARAM_CUTCOM_DIST   232  /* UF_PARAM_type_double_length */


/* UF_PARAM_CUTCOM_REGISTER_NUM
 *
 *   Description:
 *      Parameter is the cutcom register number. This parameter is obseleted
 *      with UF_PARAM_TL_CUTCOM_REG in NX2.0. This parameter is going to be
 *      obseleted in User function from NX4.0
 *      (Parameter is used only if the parameter,
 *      UF_PARAM_CUTCOM_REGISTER_STATUS is 1.)
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Cutcom Register Number
 *  Variable Name: <prefix>_cutcom_register_number
 *
 *   Possible Values: UF_PARAM_type_int
 *
 * 
 */
#define UF_PARAM_CUTCOM_REGISTER_NUM   233  /* UF_PARAM_type_int */


typedef enum
{
    UF_PARAM_cutcom_register_number_not_used       = 0,
    UF_PARAM_cutcom_register_number_output_to_clsf = 1

} UF_PARAM_cutcom_register_status_t;


/* UF_PARAM_CUTCOM_REGISTER_STATUS
 *
 *   Description:
 *      Parameter determines if the register
 *      number is output when a cutcom
 *      statment is output to the CLSF.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Cutcom Register Status
 *  Variable Name: <prefix>_cutcom_register_status
 *
 *   Possible Values: UF_PARAM_cutcom_register_status_t
 *
 * 
 */
#define UF_PARAM_CUTCOM_REGISTER_STATUS   234  /* UF_PARAM_type_int */


typedef enum
{
    UF_PARAM_cutcom_plane_not_used       = 0,
    UF_PARAM_cutcom_plane_output_to_clsf = 1

} UF_PARAM_cutcom_plane_status_t;


/* UF_PARAM_CUTCOM_PLANE_STATUS
 *
 *   Description:
 *      Parameter determines if the plane in which
 *      cutcom moves are made is output to the CLSF.
 *      (No output is maded is the cutcom move is not
 *      in a principle plane.)
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Cutcom Plane Status
 *  Variable Name: <prefix>_cutcom_plane_status
 *
 *   Possible Values: 0 - no cutcom plane data to be output
 *                    1 - cutcom plane data to be output to CLSF
 *                        (provided cutcom move is in a principle plane)
 *
 * 
 */
#define UF_PARAM_CUTCOM_PLANE_STATUS   235  /* UF_PARAM_type_int */


typedef enum
{
    UF_PARAM_cutlev_method_user_defined          = 0,
    UF_PARAM_cutlev_method_floor_only            = 1,
    UF_PARAM_cutlev_method_floor_and_island_tops = 2,
    UF_PARAM_cutlev_method_levels_at_island_tops = 3,
    UF_PARAM_cutlev_method_fixed_depth           = 4

} UF_PARAM_cutlev_method_t;


/* UF_PARAM_CUTLEV_METHOD
 *
 *   Description:
 *      Parameter determines the depth-of_cut type.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Cut Level Method
 *  Variable Name: <prefix>_cut_level_method
 *
 *   Possible Values: UF_PARAM_cutlev_method_t
 *
 * 
 */
#define UF_PARAM_CUTLEV_METHOD   236  /* UF_PARAM_type_int */


typedef enum
{
    UF_PARAM_eng_init_type_none                 = 0,
    UF_PARAM_eng_init_type_vector               = 1,
    UF_PARAM_eng_init_type_vector_plane         = 2,
    UF_PARAM_eng_init_type_angle_angle_plane    = 3,
    UF_PARAM_eng_init_type_angle_angle_distance = 4,
    UF_PARAM_eng_init_type_tool_axis            = 6,
    UF_PARAM_eng_init_type_from_a_point         = 7,
    UF_PARAM_eng_init_type_automatic            = 8

} UF_PARAM_eng_init_type_t;


/* UF_PARAM_ENG_INIT_TYPE
 *
 *   Description:
 *      Parameter is the initial engage type.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Engage Initial Type
 *  Variable Name: <prefix>_engage_initial_type
 *
 *   Possible Values: UF_PARAM_eng_init_type_t
 *
 * 
 */
#define UF_PARAM_ENG_INIT_TYPE   240  /* UF_PARAM_type_int */


typedef enum
{
    UF_PARAM_eng_inter_type_automatic  = 0,
    UF_PARAM_eng_inter_type_tool_axis  = 1,
    UF_PARAM_eng_inter_type_none       = 2,
    UF_PARAM_eng_inter_type_as_initial = 3

} UF_PARAM_eng_inter_type_t;


/* UF_PARAM_ENG_INTER_TYPE
 *
 *   Description:
 *      Parameter is the internal engage type.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Engage Internal Type
 *  Variable Name: <prefix>_engage_internal_type
 *
 *   Possible Values: UF_PARAM_eng_inter_type_t
 *
 * 
 */
#define UF_PARAM_ENG_INTER_TYPE   241  /* UF_PARAM_type_int */


/* UF_PARAM_ENG_DIST
 *
 *   Description:
 *      Parameter is the length of the engage
 *      move. (It is used for the engage methods:
 *      tool axis; angle, angle, distance; and vector.)
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Engage Distance
 *  Variable Name: <prefix>_engage_distance
 *
 *   Possible Values: UF_PARAM_type_double_length
 *
 * 
 */
#define UF_PARAM_ENG_DIST   244  /* UF_PARAM_type_double_length */


/* UF_PARAM_ENG_ANGLES
 *
 *   Description:
 *      Parameter is the pair of angles used in
 *      the engage types: angle, angle, distance;
 *      and angle, angle, plane.
 *
 *   Type: UF_PARAM_type_2d
 *
 *   Name: Engage Angles
 *  Variable Name: <prefix>_engage_angles
 *
 *   Possible Values: UF_PARAM_type_2d
 *
 * 
 */
#define UF_PARAM_ENG_ANGLES   246  /* UF_PARAM_type_2d*/


typedef enum
{
    UF_PARAM_predrill_type_no_regions     = 1,
    UF_PARAM_predrill_type_all_regions    = 2,
    UF_PARAM_predrill_type_bottom_regions = 4

} UF_PARAM_predrill_type_t;


/* UF_PARAM_PREDRILL_TYPE
 *
 *   Description:
 *      Parameter indicates what regions, if any,
 *      are to have predrilled holes at the point
 *      where cutting starts. For the predrill option,
 *      all regions, either the initial or internal
 *      engages must be of type, tool axis. For the option,
 *      bottom regions, either the initial or internal
 *      engages must be automatic.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Pre Drill Type
 *  Variable Name: <prefix>_pre_drill_type
 *
 *   Possible Values: UF_PARAM_predrill_type_t
 *
 * 
 */
#define UF_PARAM_PREDRILL_TYPE   247  /* UF_PARAM_type_int */


typedef enum
{
    UF_PARAM_ret_final_type_none                 = 0,
    UF_PARAM_ret_final_type_vector               = 1,
    UF_PARAM_ret_final_type_vector_plane         = 2,
    UF_PARAM_ret_final_type_angle_angle_plane    = 3,
    UF_PARAM_ret_final_type_angle_angle_distance = 4,
    UF_PARAM_ret_final_type_tool_axis            = 6,
    UF_PARAM_ret_final_type_from_a_point         = 7,
    UF_PARAM_ret_final_type_automatic            = 8

} UF_PARAM_ret_final_type_t;


/* UF_PARAM_RET_FINAL_TYPE
 *
 *   Description:
 *      Parameter is the final retract type.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Retract Final Type
 *  Variable Name: <prefix>_retract_final_type
 *
 *   Possible Values: UF_PARAM_ret_final_type_t
 *
 * 
 */
#define UF_PARAM_RET_FINAL_TYPE   250  /* UF_PARAM_type_int */


typedef enum
{
    UF_PARAM_ret_inter_type_automatic  = 0,
    UF_PARAM_ret_inter_type_tool_axis  = 1,
    UF_PARAM_ret_inter_type_none       = 2,
    UF_PARAM_ret_inter_type_as_initial = 3

} UF_PARAM_ret_inter_type_t;


/* UF_PARAM_RET_INTER_TYPE
 *
 *   Description:
 *      Parameter is the internal retract type.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Retract Internal Type
 *  Variable Name: <prefix>_retract_internal_type
 *
 *   Possible Values: UF_PARAM_ret_inter_type_t
 *
 * 
 */
#define UF_PARAM_RET_INTER_TYPE   251  /* UF_PARAM_type_int */


/* UF_PARAM_RET_POINT
 *
 *   Description:
 *      Parameter is the point used in the final
 *      retract methods, from a point, etc.
 *
 *   Type: UF_PARAM_type_3d_length
 *
 *   Name: Retract Point
 *  Variable Name: <prefix>_retract_point
 *
 *   Possible Values: UF_PARAM_type_3d_length
 *
 * 
 */
#define UF_PARAM_RET_POINT   252  /* UF_PARAM_type_3d_length */


/* UF_PARAM_RET_DIST
 *
 *   Description:
 *      Parameter is the length of the retract
 *      move. (It is used for the retract methods:
 *      tool axis; angle, angle, distance; and vector.)
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Retract Distance
 *  Variable Name: <prefix>_retract_distance
 *
 *   Possible Values: UF_PARAM_type_double_length
 *
 * 
 */
#define UF_PARAM_RET_DIST   254  /* UF_PARAM_type_double_length */


/* UF_PARAM_RET_ANGLES
 *
 *   Description:
 *      Parameter is the pair of angles used in
 *      the retrace types: angle, angle, distance;
 *      and angle, angle, plane.
 *
 *   Type: UF_PARAM_type_2d
 *
 *   Name: Retract Angles
 *  Variable Name: <prefix>_retract_angles
 *
 *   Possible Values: UF_PARAM_type_2d
 *
 * 
 */
#define UF_PARAM_RET_ANGLES   256  /* UF_PARAM_type_2d */


/* UF_PARAM_RET_AUTO_DIST
 *
 *   Description:
 *      Paramter is the retract clearance for
 *      automatic retracts. (It is used only
 *      if the automatic type is linear.)
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Retract Auto Distance
 *  Variable Name: <prefix>_retract_auto_distance
 *
 *   Possible Values: positvie UF_PARAM_type_double_length
 *
 * 
 */
#define UF_PARAM_RET_AUTO_DIST   257  /* UF_PARAM_type_double_length */


/* UF_PARAM_CLR_HORIZ
 *
 *   Description:
 *      Parameter is the horizontal clearance.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Clearance Horizontal
 *  Variable Name: <prefix>_clearance_horizontal
 *
 *   Possible Values: non-negative UF_PARAM_type_double_length
 *
 * 
 */
#define UF_PARAM_CLR_HORIZ   258  /* UF_PARAM_type_double_length */


/* UF_PARAM_CLR_VERT
 *
 *   Description:
 *      Parameter is the vertical clearance distance.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Clearance Vertical
 *  Variable Name: <prefix>_clearance_vertical
 *
 *   Possible Values: non-negative UF_PARAM_type_double_length
 *
 * 
 */
#define UF_PARAM_CLR_VERT   259  /* UF_PARAM_type_double_length */


typedef enum
{
    UF_PARAM_cut_island_cleanup_status_off = 1,
    UF_PARAM_cut_island_cleanup_status_on  = 2

} UF_PARAM_cut_island_cleanup_status_t;


/* UF_PARAM_CUT_ISLAND_CLEANUP_STATUS
 *
 *   Description:
 *      Parameter denotes if island cleanup is to be
 *      done if one is using the cut method,
 *      Follow Periphery.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Cut Island Cleanup Status
 *  Variable Name: <prefix>_cut_island_cleanup_status
 *
 *   Possible Values: UF_PARAM_cut_island_cleanup_status_t
 *
 * 
 */
#define UF_PARAM_CUT_ISLAND_CLEANUP_STATUS   260  /* UF_PARAM_type_int */


typedef enum
{
    UF_PARAM_no_finish_pass = 0,
    UF_PARAM_finish_pass    = 1

} UF_PARAM_cut_profile_pass_status_t;


/* UF_PARAM_CUT_PROFILE_PASS_STATUS
 *
 *   Description:
 *      Parameter denotes if a finish pass is
 *      to be generated. (It is used by the various
 *      Zig cut methods, by Zig-zag, and by
 *      Follow Periphery.)
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Cut Profile Pass Status
 *  Variable Name: <prefix>_cut_profile_pass_status
 *
 *   Possible Values: UF_PARAM_cut_profile_pass_status_t
 *
 * 
 */
#define UF_PARAM_CUT_PROFILE_PASS_STATUS   262  /* UF_PARAM_type_int */


/* UF_PARAM_STOCK_PROFILE_PASS
 *
 *   Description:
 *      Parameter is the stock applied to the finish pass.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Stock Profile Pass
 *  Variable Name: <prefix>_stock_profile_pass
 *
 *   Possible Values: UF_PARAM_type_double_length
 *
 * 
 */
#define UF_PARAM_STOCK_PROFILE_PASS   263  /* UF_PARAM_type_double_length */


/* UF_PARAM_STOCK_FLOOR
 *
 *   Description:
 *      Parameter is the floor stock.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Stock Floor
 *  Variable Name: <prefix>_stock_floor
 *
 *   Possible Values: UF_PARAM_type_double_length
 *
 * 
 */
#define UF_PARAM_STOCK_FLOOR   264  /* UF_PARAM_type_double_length */


/* UF_PARAM_STOCK_PART
 *
 *   Description:
 *      Parameter is the part side stock.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Stock Part
 *  Variable Name: <prefix>_stock_part
 *
 *   Possible Values: UF_PARAM_type_double_length
 *
 * 
 */
#define UF_PARAM_STOCK_PART   265  /* UF_PARAM_type_double_length */


/* UF_PARAM_BLANK_DIST
 *
 *   Description:
 *      Parameter is the amount by which
 *      the part geometry is to be offset
 *      to product blank geometry without
 *      having to create CAD geometry.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Blank Distance
 *  Variable Name: <prefix>_blank_distance
 *
 *   Possible Values: positive UF_PARAM_type_double_length
 *
 * 
 */
#define UF_PARAM_BLANK_DIST   266  /* UF_PARAM_type_double_length */


/* UF_PARAM_BLANK_OVERHANG
 *
 *   Description:
 *      This parameter controls the maximum amount
 *      the tool may overhang the blank geometry.
 *      The distance is measured from the leading
 *      edge of the tool to the edge of the blank 
 *      and is expressed as a percentage of the
 *      tool diameter.
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Blank Overhang
 *  Variable Name: <prefix>_blank_overhang
 *
 *   Possible Values: UF_PARAM_type_double
 *                    0.0 <= blank overhang <= 100.0
 *
 * 
 */
#define UF_PARAM_BLANK_OVERHANG   267  /* UF_PARAM_type_double */


/* UF_PARAM_CTR_ANG_TOLER
 *
 *   Description:
 *      Angle tolerance for topology in tracing faces/bodies
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Tracing Angular Tolerance
 *  Variable Name: <prefix>_tracing_angular_tolerance
 *
 *   Possible Values: UF_PARAM_type_double
 *
 * 
 */
#define UF_PARAM_CTR_ANG_TOLER   268  /* UF_PARAM_type_double */


/* UF_PARAM_CTR_DIS_TOLER
 *
 *   Description:
 *      Distance tolerance for topology in tracing faces/bodies
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Tracing Linear Tolerance
 *  Variable Name: <prefix>_tracing_linear_tolerance
 *
 *   Possible Values: UF_PARAM_type_double_length
 *
 * 
 */
#define UF_PARAM_CTR_DIS_TOLER   269  /* UF_PARAM_type_double_length */


typedef enum
{
    UF_PARAM_stepover_type_none                  = 0,
    UF_PARAM_stepover_type_constant              = 1,
    UF_PARAM_stepover_type_scallop_height        = 2,
    UF_PARAM_stepover_type_variable              = 3,
    UF_PARAM_stepover_type_percent_tool_diameter = 4,
    UF_PARAM_stepover_type_number                = 5,
    UF_PARAM_stepover_type_angular               = 6,
    UF_PARAM_stepover_type_use_depth_of_cut      = 7

} UF_PARAM_stepover_type_t;


/* UF_PARAM_STEPOVER_TYPE
 *
 *   Description:
 *      Parameter is the stepover type.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Stepover Type
 *  Variable Name: <prefix>_stepover_type
 *
 *   Possible Values: UF_PARAM_stepover_type_t
 *
 * 
 */
#define UF_PARAM_STEPOVER_TYPE   270  /* UF_PARAM_type_int */


/* UF_PARAM_STEPOVER_SCALLOP
 *
 *   Description:
 *      Parameter is the scallop height.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Stepover Scallop
 *  Variable Name: <prefix>_stepover_scallop
 *
 *   Possible Values: positive UF_PARAM_type_double_length
 *
 * 
 */
#define UF_PARAM_STEPOVER_SCALLOP   271  /* UF_PARAM_type_double_length */


/* UF_PARAM_STEPOVER_DIST
 *
 *   Description:
 *      Parameter is the stepover size to be used
 *      if the stepover type is 1, i.e constant.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Stepover Distance
 *  Variable Name: <prefix>_stepover_distance
 *
 *   Possible Values: positive UF_PARAM_type_double_length
 *
 * 
 */
#define UF_PARAM_STEPOVER_DIST   272  /* UF_PARAM_type_double_length */


/* UF_PARAM_STEPOVER_PERCENT
 *
 *   Description:
 *      Parameter is the value of the percentage
 *      used by stepover type, % Tool Diameter.
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Stepover Percent
 *  Variable Name: <prefix>_stepover_percent
 *
 *   Possible Values: positive UF_PARAM_type_double
 *
 * 
 */
#define UF_PARAM_STEPOVER_PERCENT   273  /* UF_PARAM_type_double */


/* UF_PARAM_STEPOVER_VAR_DISTS
 *
 *   Description:
 *      Value of stepover size for stepover type = variable
 *      This parameter is obsolete. Use UF_PARAM_STEPOVER_VAR_DISTS_TOOL_DEPENDENT instead
 *
 *   Type: UF_PARAM_type_vla_length
 *
 *   Name: Stepover Variable Distances
 *  Variable Name: <prefix>_stepover_variable_distances
 *
 *   Possible Values: UF_PARAM_type_vla_length
 *                    array of double (size = 6)
 *
 * 
 */
#define UF_PARAM_STEPOVER_VAR_DISTS   274  /* UF_PARAM_type_vla_length, size 6, Obsolete in NX6 */


/* UF_PARAM_STEPOVER_VAR_PASSES
 *
 *   Description:
 *      Number of passes corresponding with the stepover size
 *      for stepover type = variable
 *
 *   Type: UF_PARAM_type_int_vla
 *
 *   Name: Stepover Variable Passes
 *  Variable Name: <prefix>_stepover_variable_passes
 *
 *   Possible Values: UF_PARAM_type_int_vla
 *                    array of integer (size = 6)
 *
 * 
 */
#define UF_PARAM_STEPOVER_VAR_PASSES   275  /* UF_PARAM_type_int_vla, size 6 */


/* UF_PARAM_STEPOVER_DEGREE
 *
 *   Description:
 *      Parameter is the value of the degree
 *      used by stepover type, Angular.
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Stepover Degree
 *  Variable Name: <prefix>_stepover_degree
 *
 *   Possible Values: positive UF_PARAM_type_double
 *
 * 
 */
#define UF_PARAM_STEPOVER_DEGREE   276  /* UF_PARAM_type_double */


typedef enum
{
    UF_PARAM_cut_follow_progression_inward  = 1,
    UF_PARAM_cut_follow_progression_outward = 2

} UF_PARAM_cut_follow_progression_t;


/* UF_PARAM_CUT_FOLLOW_PROGRESSION
 *
 *   Description:
 *      For the cut methods, follow periphery and trochoidal,
 *      parameter determines if successive cut moves move
 *      toward or away from the peripheral boundary.
 *
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Follow Progression
 *  Variable Name: <prefix>_follow_progression
 *
 *   Possible Values: UF_PARAM_cut_follow_progression_t
 *
 * 
 */
#define UF_PARAM_CUT_FOLLOW_PROGRESSION   277  /* UF_PARAM_type_int */


typedef enum
{
    UF_PARAM_cut_wall_cleanup_off = 0,
    UF_PARAM_cut_wall_cleanup_on  = 1,     /* Obsolete */
    UF_PARAM_cut_wall_cleanup_after_cutting_region = 1,
    UF_PARAM_cut_wall_cleanup_before_cutting_region = 2,
    UF_PARAM_cut_wall_cleanup_automatic = 3

} UF_PARAM_cut_wall_cleanup_status_t;



/* UF_PARAM_CUT_WALL_CLEANUP_STATUS
 *
 *   Description:
 *      Parmeter determines if a scallop removal pass
 *      is to be done (zig, zig-zag, zig-with_countour,
 *      zig-with-stepover, follow periphery only).
 *      The UF_PARAM_cut_wall_cleanup_automatic is only applied to
 *      follow periphery.
 *
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Cut Wall Cleanup Staus
 *  Variable Name: <prefix>_cut_wall_cleanup_staus
 *
 *   Possible Values: UF_PARAM_cut_wall_cleanup_status_t
 *
 * 
 */
#define UF_PARAM_CUT_WALL_CLEANUP_STATUS   278  /* UF_PARAM_type_int */


typedef enum
{
    UF_PARAM_tlaxis_type_none = 0,
    UF_PARAM_tlaxis_type_fixed  = 1,
    UF_PARAM_tlaxis_type_normal_to_part  = 2,
    UF_PARAM_tlaxis_type_normal_to_first_face  = 3,
    UF_PARAM_tlaxis_type_swarf  = 4,
    UF_PARAM_tlaxis_type_relative_to_part  = 7,
    UF_PARAM_tlaxis_type_4axis_normal_to_part  = 8,
    UF_PARAM_tlaxis_type_away_from_point  = 9,
    UF_PARAM_tlaxis_type_toward_point  = 10,
    UF_PARAM_tlaxis_type_away_from_line  = 11,
    UF_PARAM_tlaxis_type_toward_line  = 12,
    UF_PARAM_tlaxis_type_away_from_curve  = 13,
    UF_PARAM_tlaxis_type_toward_curve  = 14,
    UF_PARAM_tlaxis_type_normal_to_drive  = 16,
    UF_PARAM_tlaxis_type_relative_to_drive  = 19,
    UF_PARAM_tlaxis_type_4axis_normal_to_drive  = 20,
    UF_PARAM_tlaxis_type_4axis_relative_to_part  = 21,
    UF_PARAM_tlaxis_type_4axis_relative_to_drive  = 22,
    UF_PARAM_tlaxis_type_tool_path  = 23,
    UF_PARAM_tlaxis_type_relative_to_vector  = 24,
    UF_PARAM_tlaxis_type_dual4axis_relative_to_part  = 25,
    UF_PARAM_tlaxis_type_dual4axis_relative_to_drive  = 26,
    UF_PARAM_tlaxis_type_interpolate  = 27,
    UF_PARAM_tlaxis_type_user_defined_to_part  = 28,
    UF_PARAM_tlaxis_type_all  = 29
} UF_PARAM_tool_axis_type_t;

/* UF_PARAM_TLAXIS_TYPE
 *
 *   Description:
 *      Parameter denotes the tool axis type.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Tool Axis Type
 *  Variable Name: <prefix>_tool_axis_type
 *
 *   Possible Values: UF_PARAM_tool_axis_type_t
 *
 * 
 */
#define UF_PARAM_TLAXIS_TYPE   280  /* UF_PARAM_type_int */


typedef enum
{
    UF_PARAM_stepover_apply_on_plane  = 0,
    UF_PARAM_stepover_apply_on_part   = 1
} UF_PARAM_stepover_apply_t;


/* UF_PARAM_STEPOVER_APPLY_METHOD
 *
 *   Description:
 *      Determines the method that is used to determine
 *      how to calculate the stepover distance.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Stepover Apply Method
 *  Variable Name: <prefix>_stepover_apply_method
 *
 *   Possible Values: UF_PARAM_stepover_apply_t
 *
 * 
 */
#define UF_PARAM_STEPOVER_APPLY_METHOD   281  /* UF_PARAM_type_int */


typedef enum
{
   UF_PARAM_step_control_type_none          = 0,
   UF_PARAM_step_control_type_tool_diameter = 1,
   UF_PARAM_step_control_type_max_step      = 2

} UF_PARAM_step_control_t;


/* UF_PARAM_CUT_STEP_TYPE
 *   Description:
 *      This parameters specifies the type of step control that is used.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Cut Step Type
 *  Variable Name: <prefix>_cut_step_type
 *
 *   Possible Values: UF_PARAM_step_control_t
 *
 * 
 */
#define UF_PARAM_CUT_STEP_TYPE   282  /* UF_PARAM_type_int */


/* UF_PARAM_CUT_STEP_MAX
 *   Description:
 *      This parameter specifies maximum step distance allowed.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Cut Step Max Size
 *  Variable Name: <prefix>_cut_step_max_size
 *
 *   Possible Values: Positive double
 *
 * 
 */
#define UF_PARAM_CUT_STEP_MAX   283  /* UF_PARAM_type_double_length */


/* UF_PARAM_CUT_TLAXIS_DELTA
 *   Description:
 *      This parameter specifies maximum tool axis change
 *      allowed at a corner
 *
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Tool Axis Max Delta
 *  Variable Name: <prefix>_tool_axis_max_delta
 *
 *   Possible Values: double
 *
 * 
 */
#define UF_PARAM_CUT_TLAXIS_DELTA   284  /* UF_PARAM_type_double */


/* UF_PARAM_TLAXIS_HEEL_CLEARANCE
 *
 *   Description:
 *      This parameter specifies minimum heel clearance
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Minumum Heel Clearance
 *  Variable Name: <prefix>_minumum_heel_clearance
 *
 *   Possible Values:
 *             double
 *
 * 
 *
 */
#define UF_PARAM_TLAXIS_HEEL_CLEARANCE   286  /* UF_PARAM_type_double */


/* UF_PARAM_TLAXIS_LEAD_ANGLE
 *
 *   Description:
 *      This parameter specifies tool axis lead angle
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Tool Axis Lead Angle
 *  Variable Name: <prefix>_tool_axis_lead_angle
 *
 *   Possible Values:
 *             double
 *
 * 
 *
 */
#define UF_PARAM_TLAXIS_LEAD_ANGLE   287  /* UF_PARAM_type_double */


/* UF_PARAM_TLAXIS_THRU_POINT
 *
 *   Description:
 *      This parameter specifies tool axis focal point
 *
 *   Type: UF_PARAM_type_3d_length
 *
 *   Name: Tool Axis focal point
 *  Variable Name: <prefix>_tool_axis_focal_point
 *
 *   Possible Values:
 *             double array
 *
 * 
 *
 */
#define UF_PARAM_TLAXIS_THRU_POINT   289  /* UF_PARAM_type_3d_length */


/* UF_PARAM_TLAXIS_ANGLES
 *
 *   Description:
 *      This parameter specifies tool axis angles
 *
 *   Type: UF_PARAM_type_vla_real
 *
 *   Name: Tool Axis angles
 *  Variable Name: <prefix>_tool_axis_angles
 *
 *   Possible Values:
 *             double array(6)
 *               0 - 2  tool axis angle
 *               3 - 5  Dual 4_axis angle
 *
 * 
 *
 */
#define UF_PARAM_TLAXIS_ANGLES   290  /* UF_PARAM_type_vla_real(6) */


typedef enum
{
    UF_PARAM_dpm_type_none = 0,
    UF_PARAM_dpm_type_point  = 10,
    UF_PARAM_dpm_type_curve  = 20,
    UF_PARAM_dpm_type_surface  = 30,
    UF_PARAM_dpm_type_interpolated_tool_path = 35,
    UF_PARAM_dpm_type_boundary  = 40,
    UF_PARAM_dpm_type_path  = 50,
    UF_PARAM_dpm_type_radial  = 60,
    UF_PARAM_dpm_type_spiral  = 70,
    UF_PARAM_dpm_type_helical  = 80,   /*  for future use  */
    UF_PARAM_dpm_type_user_defined  = 90,
    UF_PARAM_dpm_type_area_milling  = 100,
    UF_PARAM_dpm_type_text = 110,      /* drafting notes */
    UF_PARAM_dpm_type_contour_milling  = 120
} UF_PARAM_dpm_type_t;

/* UF_PARAM_DRIVE_METHOD
 *
 *   Description:
 *      This parameter specifies surface contouring drive method
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Surface Contour Drive Method
 *  Variable Name: <prefix>_surface_contour_drive_method
 *
 *   Possible Values:
 *             UF_PARAM_dpm_type_t
 *
 * 
 *
 */
#define UF_PARAM_DRIVE_METHOD   291  /* UF_PARAM_type_int */


/* UF_PARAM_CTP_CHK_TOL
 *
 *   Description:
 *      This parameter specifies surface contouring check surface tolerance
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Surface Contour Check surface tolerance
 *  Variable Name: <prefix>_surface_contour_check_surface_tolerance
 *
 *   Possible Values:
 *             double
 *
 * 
 *
 */
#define UF_PARAM_CTP_CHK_TOL   292  /* UF_PARAM_type_double_length */


/* UF_PARAM_TLAXIS_PERP_VEC
 *
 *   Description:
 *     This parameter specifies the reference vector for these tool axis modes
 *       UF_PARAM_tlaxis_type_away_from_line
 *       UF_PARAM_tlaxis_type_toward_line
 *       UF_PARAM_tlaxis_type_4axis_normal_to_part
 *       UF_PARAM_tlaxis_type_4axis_normal_to_drive
 *       UF_PARAM_tlaxis_type_4axis_relative_to_part
 *       UF_PARAM_tlaxis_type_4axis_relative_to_drive
 *       UF_PARAM_tlaxis_type_dual4axis_relative_to_part
 *       UF_PARAM_tlaxis_type_dual4axis_relative_to_drive
 *
 *   Type: UF_PARAM_type_3d
 *
 *   Name: Surface Contour Perpto Vector
 *  Variable Name: <prefix>_surface_contour_perpto_vector
 *
 *   Possible Values:
 *             double array
 *
 * 
 *
 */
#define UF_PARAM_TLAXIS_PERP_VEC   295  /* UF_PARAM_type_3d */


/* UF_PARAM_TLAXIS_DUAL_VECS
 *
 *   Description:
 *     This parameter specifies the second reference vector for these
 *       tool axis modes
 *         UF_PARAM_tlaxis_type_dual4axis_relative_to_part
 *         UF_PARAM_tlaxis_type_dual4axis_relative_to_drive
 *
 *   Type: UF_PARAM_type_3d
 *
 *   Name: Surface Contour Dual Perpto Vector
 *  Variable Name: <prefix>_surface_contour_dual_perpto_vector
 *
 *   Possible Values:
 *             double array
 *
 * 
 *
 */
#define UF_PARAM_TLAXIS_DUAL_VECS   296  /* UF_PARAM_type_3d */


typedef enum
{
    UF_PARAM_avoid_none,
    UF_PARAM_avoid_warning,
    UF_PARAM_avoid_stepover,
    UF_PARAM_avoid_lift
} UF_PARAM_avoid_type_t;

/* UF_PARAM_AVOIDANCE
 *
 *   Description:
 *     This parameter specifies the action to be taken when a gouge of the
 *       check surface is detected by the processor.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Surface Contour Check Surface avoidance action
 *  Variable Name: <prefix>_surface_contour_check_surface_avoidance_action
 *
 *   Possible Values: UF_PARAM_avoid_type_t
 *
 * 
 *
 */
#define UF_PARAM_AVOIDANCE   297  /* UF_PARAM_type_int */


/* UF_PARAM_CONVEX_CORNER
 *
 *   Description:
 *     When convex corner extend is enabled, this parameter specifies the
 *       maximum angle two surfaces can make with each other for the processor
 *       to extend the corner
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Surface Contour convex corner extension angle
 *  Variable Name: <prefix>_surface_contour_convex_corner_extension_angle
 *
 *   Possible Values: angle between 0 and 180 degrees
 *
 * 
 *
 */
#define UF_PARAM_CONVEX_CORNER   298  /* UF_PARAM_type_double */


/* UF_PARAM_CONVEX_TAX_VAR
 *
 *   Description:
 *     When convex corner lift is enabled, this parameter specifies the
 *       minimum change of tool axis vector to result in a lift at the corner
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Surface Contour convex corner lift angle
 *  Variable Name: <prefix>_surface_contour_convex_corner_lift_angle
 *
 *   Possible Values: angle between 0 and 180 degrees
 *
 * 
 *
 */
#define UF_PARAM_CONVEX_TAX_VAR   299  /* UF_PARAM_type_double */


typedef enum UF_PARAM_cut_method_e
{
    UF_PARAM_cut_method_undefined        = 0,
    UF_PARAM_cut_method_zig_zag          = 1,
    UF_PARAM_cut_method_zig              = 2,
    UF_PARAM_cut_method_zig_with_contour = 3,
    UF_PARAM_cut_method_follow_periphery = 4,
    UF_PARAM_cut_method_profile          = 5,
    UF_PARAM_cut_method_standard_drive   = 6,
    UF_PARAM_cut_method_follow_part      = 7,
    UF_PARAM_cut_method_mixed            = 8,
    UF_PARAM_cut_method_trochoidal       = 9,
    UF_PARAM_cut_method_spiral           = 10,
    UF_PARAM_cut_method_helical          = 11

} UF_PARAM_cut_method_t;


/* UF_PARAM_CUT_METHOD
 *
 *   Description:
 *      This parameter specifies the cutting pattern of a region.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Cut Method
 *  Variable Name: <prefix>_cut_method
 *
 *   Possible Values: UF_PARAM_cut_method_t
 *
 * 
 */
#define UF_PARAM_CUT_METHOD   300  /* UF_PARAM_type_int */


typedef enum UF_PARAM_pattern_secondary_e
{
    UF_PARAM_pattern_secondary_undefined = 0,
    UF_PARAM_pattern_secondary_zig       = 1,
    UF_PARAM_pattern_secondary_zig_zag   = 2

} UF_PARAM_pattern_secondary_t;


/* UF_PARAM_PATTERN_SECONDARY
 *
 *   Description:
 *      This parameter specifies how to traverse the open passes
 *      during the cutting of a region with the follow part cut method.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Cut Pattern Secondary
 *  Variable Name: <prefix>_cut_pattern_secondary
 *
 *   Possible Values: UF_PARAM_pattern_secondary_t
 *
 * 
 */
#define UF_PARAM_PATTERN_SECONDARY   302  /* UF_PARAM_type_int */


typedef enum UF_PARAM_cut_level_order_e
{
    UF_PARAM_cut_level_order_level_first = 1,
    UF_PARAM_cut_level_order_depth_first = 2

} UF_PARAM_cut_level_order_t;


/* UF_PARAM_CUT_LEVEL_ORDER
 *
 *   Description:
 *      This parameter specifies the order of cutting of cut levels.
 *      The order of cutting can be level first or depth first.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Cut Level Order
 *  Variable Name: <prefix>_cut_level_order
 *
 *   Possible Values: UF_PARAM_cut_level_order_t
 *
 * 
 */
#define UF_PARAM_CUT_LEVEL_ORDER   303  /* UF_PARAM_type_int */


typedef enum UF_PARAM_transfer_method_e
{
    UF_PARAM_transfer_method_direct           = 0,
    UF_PARAM_transfer_method_clearance_plane  = 1,
    UF_PARAM_transfer_method_previous_plane   = 2,
    UF_PARAM_transfer_method_blank_plane      = 3,
    UF_PARAM_transfer_method_direct_with_clearance = 4

} UF_PARAM_transfer_method_t;


/* UF_PARAM_TRANSFER_METHOD
 *
 *   Description:
 *      This parameter specifies the level the tool
 *      will retract to during the transfer moves.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Region Transfer Method
 *  Variable Name: <prefix>_region_transfer_method
 *
 *   Possible Values: UF_PARAM_transfer_method_t
 *
 * 
 */
#define UF_PARAM_TRANSFER_METHOD   304  /* UF_PARAM_type_int */


typedef enum
{
    UF_PARAM_disp_region_status_inactive = 0,
    UF_PARAM_disp_region_status_active =   1

} UF_PARAM_disp_region_status_t;


/* UF_PARAM_DISP_REGION_STATUS
 *
 *   Description:
 *      This parameter specifies the status to display regions at each
 *      cut level.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Display Region Status
 *  Variable Name: <prefix>_display_region_status
 *
 *   Possible Values: UF_PARAM_disp_region_status_t
 *
 * 
 */
#define UF_PARAM_DISP_REGION_STATUS   307  /* UF_PARAM_type_int */


typedef enum
{
    UF_PARAM_disp_region_pause_status_inactive = 0,
    UF_PARAM_disp_region_pause_status_active   = 1

} UF_PARAM_disp_region_pause_status_t;


/* UF_PARAM_DISP_REGION_PAUSE_STATUS
 *
 *   Description:
 *      This parameter specifies the status to pause after processing
 *      each region or to pause after displaying the cut regions.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Region Pause Status
 *  Variable Name: <prefix>_region_pause_status
 *
 *   Possible Values: UF_PARAM_disp_region_pause_status_t
 *
 * 
 */
#define UF_PARAM_DISP_REGION_PAUSE_STATUS   308  /* UF_PARAM_type_int */


typedef enum
{
    UF_PARAM_disp_refresh_status_inactive = 0,
    UF_PARAM_disp_refresh_status_active = 1

} UF_PARAM_disp_refresh_status_t;


/* UF_PARAM_DISP_REFRESH_STATUS
 *
 *   Description:
 *      This parameter specifies the status to refresh graphics screen
 *      before each cut of a region.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Display Refresh Status
 *  Variable Name: <prefix>_display_refresh_status
 *
 *   Possible Values: UF_PARAM_disp_refresh_status_t
 *
 * 
 */
#define UF_PARAM_DISP_REFRESH_STATUS   309  /* UF_PARAM_type_int */


/* UF_PARAM_CUTLEV_FIRST_DEPTH
 *
 *   Description:
 *      This parameter specifies the first depth of cut used in the cut level.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Cut Level First Depth
 *  Variable Name: <prefix>_cut_level_first_depth
 *
 *   Possible Values: zero or positive double
 *
 * 
 */
#define UF_PARAM_CUTLEV_FIRST_DEPTH   310  /* UF_PARAM_type_double_length */


/* UF_PARAM_CUTLEV_LAST_DEPTH
 *
 *   Description:
 *      This parameter specifies the last depth of cut used in the cut level.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Cut Level Last Depth
 *  Variable Name: <prefix>_cut_level_last_depth
 *
 *   Possible Values: zero or positive double
 *
 * 
 */
#define UF_PARAM_CUTLEV_LAST_DEPTH   311  /* UF_PARAM_type_double_length */


/* UF_PARAM_CUTLEV_MAX_DEPTH
 *
 *   Description:
 *      This parameter specifies the maximum depth of cut used in the cut level.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Cut Level Max Depth
 *  Variable Name: <prefix>_cut_level_max_depth
 *
 *   Possible Values: zero or positive double
 *
 * 
 */
#define UF_PARAM_CUTLEV_MAX_DEPTH   312  /* UF_PARAM_type_double_length */


/* UF_PARAM_CUTLEV_MIN_DEPTH
 *
 *   Description:
 *      This parameter specifies the minimum depth of cut used in the cut level.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Cut Level Min Depth
 *  Variable Name: <prefix>_cut_level_min_depth
 *
 *   Possible Values: zero or positive double
 *
 * 
 */
#define UF_PARAM_CUTLEV_MIN_DEPTH   313  /* UF_PARAM_type_double_length */


/* UF_PARAM_CUTLEV_SIDE_STOCK_INCR
 *
 *   Description:
 *      This parameter specifies the side stock increment for each cut level.
 *      (Parameter is used in planar milling only.)
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Cut Level Side Stock Increment
 *  Variable Name: <prefix>_cut_level_side_stock_increment
 *
 *   Possible Values: double
 *
 * 
 */
#define UF_PARAM_CUTLEV_SIDE_STOCK_INCR   314  /* UF_PARAM_type_double_length */


typedef enum
{
    UF_PARAM_cutlev_topoff_status_inactive = 0,
    UF_PARAM_cutlev_topoff_status_active   = 1

} UF_PARAM_cutlev_topoff_status_t;


/* UF_PARAM_CUTLEV_TOPOFF_STATUS
 *
 *   Description:
 *      This parameter specifies the status to top off the islands.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Cut Level Topoff Status
 *  Variable Name: <prefix>_cut_level_topoff_status
 *
 *   Possible Values: UF_PARAM_cutlev_topoff_status_t
 *
 *
 *
 * 
 */
#define UF_PARAM_CUTLEV_TOPOFF_STATUS   315  /* UF_PARAM_type_int */


typedef enum UF_PARAM_cut_angle_method_e
{
    UF_PARAM_cut_angle_method_user_defined = 0,
    UF_PARAM_cut_angle_method_automatic    = 1,
    UF_PARAM_cut_angle_method_longest_line = 2

} UF_PARAM_cut_angle_method_t;


/* UF_PARAM_CUT_ANGLE_METHOD
 *
 *   Description:
 *      This parameter specifies the status of the cut angle: user-defined or
 *      automatic. In case of user-defined, the value of UF_PARAM_CUT_ANGLE
 *      will be used. In case of automatic, the process will find the best angle.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Cut Angle Method
 *  Variable Name: <prefix>_cut_angle_method
 *
 *   Possible Values: UF_PARAM_cut_angle_method_t
 *
 * 
 */
#define UF_PARAM_CUT_ANGLE_METHOD   316  /* UF_PARAM_type_int */


/* UF_PARAM_CUT_ANGLE
 *
 *   Description:
 *      This parameter specifies the cut angle in zig or zig-zag cut pattern.
 *      It only applies to Planar Milling operations.
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Cut Angle
 *  Variable Name: <prefix>_cut_angle
 *
 *   Possible Values: double
 *
 * 
 */
#define UF_PARAM_CUT_ANGLE   317  /* UF_PARAM_type_double */


/* UF_PARAM_STOCK_BLANK
 *
 *   Description:
 *      This parameter specifies the stock applied to blank geometry.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Stock Blank
 *  Variable Name: <prefix>_stock_blank
 *
 *   Possible Values: double
 *
 * 
 */
#define UF_PARAM_STOCK_BLANK   318  /* UF_PARAM_type_double_length */


/* UF_PARAM_CUT_EXTRA_PROFILE_PASSES
 *
 *   Description:
 *      This parameter specifies the number of extra profile passes.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Cut Extra Profile Passes
 *  Variable Name: <prefix>_cut_extra_profile_passes
 *
 *   Possible Values: non-negative integer
 *
 * 
 */
#define UF_PARAM_CUT_EXTRA_PROFILE_PASSES   319  /* UF_PARAM_type_int */


typedef enum
{
    UF_PARAM_cut_ctrl_predrill_status_inactive = 0,
    UF_PARAM_cut_ctrl_predrill_status_active   = 1

} UF_PARAM_cut_ctrl_predrill_status_t;


/* UF_PARAM_CUT_CTRL_PREDRILL_STATUS
 *
 *   Description:
 *      This parameter specifies the status of custom pre-drill
 *      engage points.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Cut Control Pri Drill Status
 *  Variable Name: <prefix>_cut_control_pri_drill_status
 *
 *   Possible Values: UF_PARAM_cut_ctrl_predrill_status_t
 *
 * 
 */
#define UF_PARAM_CUT_CTRL_PREDRILL_STATUS   320  /* UF_PARAM_type_int */


typedef enum
{
    UF_PARAM_cut_ctrl_start_point_togggle_inactive = 0,
    UF_PARAM_cut_ctrl_start_point_togggle_active   = 1

} UF_PARAM_cut_ctrl_start_point_togggle_t;


/* UF_PARAM_CUT_CTRL_START_POINT_TOGGLE
 *
 *   Description:
 *      This parameter specifies the toggle value of custom cut region
 *      start points.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Cut Control Pri Drill Toggle
 *  Variable Name: <prefix>_cut_control_pri_drill_toggle
 *
 *   Possible Values: UF_PARAM_cut_ctrl_start_point_togggle_t
 *
 * 
 */
#define UF_PARAM_CUT_CTRL_START_POINT_TOGGLE   321  /* UF_PARAM_type_int */


typedef enum UF_PARAM_cut_ctrl_start_point_mode_e
{
    UF_PARAM_cut_ctrl_start_point_mode_standard  = 0,
    UF_PARAM_cut_ctrl_start_point_mode_automatic = 1

} UF_PARAM_cut_ctrl_start_point_mode_t;


/* UF_PARAM_CUT_CTRL_START_POINT_MODE
 *
 *   Description:
 *      This parameter specifies the mode of default cut region start points.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Cut Control Start Point Mode
 *  Variable Name: <prefix>_cut_control_start_point_mode
 *
 *   Possible Values: UF_PARAM_standard_automatic_t
 *
 * 
 */
#define UF_PARAM_CUT_CTRL_START_POINT_MODE   322  /* UF_PARAM_type_int */


/* UF_PARAM_STEPOVER_MIN_MAX
 *
 *   Description:
 *      This parameter specifies the variable stepover for zig cut.
 *
 *   Type: UF_PARAM_type_2d_length
 *
 *   Name: Stepover Min Max
 *  Variable Name: <prefix>_stepover_min_max
 *
 *   Possible Values: double min, double max
 *
 * 
 */
#define UF_PARAM_STEPOVER_MIN_MAX   323  /* UF_PARAM_type_2d_length */


typedef enum
{
    UF_PARAM_uncut_region_display_off = 0,
    UF_PARAM_uncut_region_display_on  = 1

} UF_PARAM_uncut_display_t;


/* UF_PARAM_UNCUT_DISPLAY
 *
 *   Description:
 *      This parameter specifies the flag that indicates the display
 *      of the uncut region at each cut level. (It is used by planar
 *      milling only.)
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Uncut Display Flag
 *  Variable Name: <prefix>_uncut_display_flag
 *
 *   Possible Values: UF_PARAM_uncut_display_t
 *
 * 
 */
#define UF_PARAM_UNCUT_DISPLAY   325  /* UF_PARAM_type_int */


/* UF_PARAM_UNCUT_OVERLAP_DIST
 *
 *   Description:
 *      This parameter specifies the overlap distance to be stocked for the
 *      uncut boundary. (It is used by planar milling only.)
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Uncut Overlap Distance
 *  Variable Name: <prefix>_uncut_overlap_distance
 *
 *   Possible Values: double
 *
 * 
 */
#define UF_PARAM_UNCUT_OVERLAP_DIST   326  /* UF_PARAM_type_double_length */


typedef enum UF_PARAM_cut_trace_method_e
{
    UF_PARAM_cut_trace_method_non_tolerant = 0,
    UF_PARAM_cut_trace_method_tolerant     = 1

} UF_PARAM_cut_trace_method_t;


/* UF_PARAM_CUT_TRACE_METHOD
 *
 *   Description:
 *      This parameter specifies the tolerant machining tracing method:
 *      Non-tolerant or tolerant.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Cut Trace Method
 *  Variable Name: <prefix>_cut_trace_method
 *
 *   Possible Values: UF_PARAM_cut_trace_method_t
 *
 * 
 */
#define UF_PARAM_CUT_TRACE_METHOD   327  /* UF_PARAM_type_int */


typedef enum UF_PARAM_cut_ctrl_trim_method_e
{
    UF_PARAM_cut_ctrl_trim_method_none           = 0,
    UF_PARAM_cut_ctrl_trim_method_silhoutte      = 1,
    UF_PARAM_cut_ctrl_trim_method_exterior_edges = 1

} UF_PARAM_cut_ctrl_trim_method_t;


/* UF_PARAM_CUT_CTRL_TRIM_METHOD
 *   Description:
 *      This parameter specifies the trim-by method.
 *      The method enables to create Blank Geometry from exterior edges
 *      in case of non-tolerant machining, or from silhouette in case of
 *      tolerant machining.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Cut Control Trim Method
 *  Variable Name: <prefix>_cut_control_trim_method
 *
 *   Possible Values: UF_PARAM_cut_ctrl_trim_method_t
 *
 * 
 */
#define UF_PARAM_CUT_CTRL_TRIM_METHOD   328  /* UF_PARAM_type_int */


typedef enum
{
    UF_PARAM_cut_undercut_status_inactive = 0, /* Obsoleted in NX4 */
    UF_PARAM_cut_undercut_status_allow    = 0,
    UF_PARAM_cut_undercut_status_active   = 1, /* Obsoleted in NX4 */
    UF_PARAM_cut_undercut_status_prevent  = 1

} UF_PARAM_cut_undercut_toggle_t;


/* UF_PARAM_CUT_UNDERCUT_TOGGLE
 *
 *   Description:
 *      This parameter specifies the prevent undercutting flag.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Undercut Handle Flag
 *  Variable Name: <prefix>_undercut_handle_flag
 *
 *   Possible Values: UF_PARAM_cut_undercut_toggle_t
 *
 * 
 */
#define UF_PARAM_CUT_UNDERCUT_TOGGLE   329  /* UF_PARAM_type_int */


/* UF_PARAM_STOCK_CHECK
 *
 *   Description:
 *      This parameter specifies the stock for check geometry.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Stock Check
 *  Variable Name: <prefix>_stock_check
 *
 *   Possible Values: double
 *
 * 
 */
#define UF_PARAM_STOCK_CHECK   330  /* UF_PARAM_type_double_length */


/* UF_PARAM_STOCK_TRIM
 *
 *   Description:
 *      This parameter specifies the stock for trim geometry
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Stock Trim
 *  Variable Name: <prefix>_stock_trim
 *
 *   Possible Values: double
 *
 * 
 */
#define UF_PARAM_STOCK_TRIM   331  /* UF_PARAM_type_double_length */


typedef enum
{
    UF_PARAM_cut_follow_check_off = 0, /* During cutting the tool will not cut along check geometry. */
    UF_PARAM_cut_follow_check_on  = 1  /* During cutting the tool will cut along check geometry. */

} UF_PARAM_cut_follow_check_status_t;


/* UF_PARAM_CUT_FOLLOW_CHECK_STATUS
 *
 *   Description:
 *      This parameter specifies if the tool is to cut along check geometry
 *      for the cut method-follow part.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Follow Check Geometry Status
 *  Variable Name: <prefix>_follow_check_geometry_status
 *
 *   Possible Values: UF_PARAM_cut_follow_check_status_t
 *
 * 
 */
#define UF_PARAM_CUT_FOLLOW_CHECK_STATUS   332  /* UF_PARAM_type_int */


typedef enum
{
     UF_PARAM_do_not_allow_self_intersection_in_standard_drive = 0,
     UF_PARAM_allow_self_intersection_in_standard_drive        = 1

} UF_PARAM_cut_std_drive_self_intersect_t;


/* UF_PARAM_CUT_STD_DRIVE_SELF_INTERSECT
 *
 *   Description:
 *      This parameter specifies the status to allow self intersection
 *      in standard drive.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Standard Drive Self-Intersect Status
 *  Variable Name: <prefix>_standard_drive_self_intersect_status
 *
 *   Possible Values: UF_PARAM_cut_std_drive_self_intersect_t
 *
 * 
 */
#define UF_PARAM_CUT_STD_DRIVE_SELF_INTERSECT   333  /* UF_PARAM_type_int */


/* UF_PARAM_SIDE_STOCK
 *
 *   Description:
 *      This parameter specifies the side stock.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Stock Side
 *  Variable Name: <prefix>_stock_side
 *
 *   Possible Values: double
 *
 * 
 */
#define UF_PARAM_SIDE_STOCK   334  /*   */


typedef enum UF_PARAM_cut_reseq_region_method_e
{
    UF_PARAM_cut_reseq_region_method_standard        = 0,
    UF_PARAM_cut_reseq_region_method_optimize        = 1,
    UF_PARAM_cut_reseq_region_method_region_points   = 2,
    UF_PARAM_cut_reseq_region_method_predrill_points = 3

} UF_PARAM_cut_reseq_region_method_t;


/* UF_PARAM_CUT_RESEQ_REGION_METHOD
 *
 *   Description:
 *      This parameter specifies the method used in region resequencing.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Resequence Region Method
 *  Variable Name: <prefix>_resequence_region_method
 *
 *   Possible Values: UF_PARAM_cut_reseq_region_method_t
 *
 * 
 */
#define UF_PARAM_CUT_RESEQ_REGION_METHOD   335  /* UF_PARAM_type_int */


/* UF_PARAM_CUTLEV_DEPTH_PER_CUT
 *   Description:
 *      This parameter specifies the depth per cut.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Depth Per Cut
 *  Variable Name: <prefix>_depth_per_cut
 *
 *   Possible Values: zero or positive double
 *
 *
 * 
 */
#define UF_PARAM_CUTLEV_DEPTH_PER_CUT   336 


typedef enum
{
    UF_PARAM_boundary_approximation_off = 0,
    UF_PARAM_boundary_approximation_on  = 1

} UF_PARAM_bnd_approx_toggle_index_t;


/* UF_PARAM_BND_APPROX_TOGGLE
 *
 *   Description:
 *      This parameter specifies the toggle status of the boundary
 *      approximation.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Boundary Approximation
 *  Variable Name: <prefix>_boundary_approximation
 *
 *   Possible Values: UF_PARAM_bnd_approx_toggle_index_t
 *
 * 
 */
#define UF_PARAM_BND_APPROX_TOGGLE   337  /* UF_PARAM_type_int */


/* UF_PARAM_CUT_ADJUST_REGION
 *
 *   Description:
 *      This parameter specifies the status to adjust or not the region by
 *      stepover.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Adjust Region
 *  Variable Name: <prefix>_adjust_region
 *
 *   Possible Values: UF_PARAM_no_yes_t
 *
 * 
 */
#define UF_PARAM_CUT_ADJUST_REGION   339  /* UF_PARAM_type_int */


typedef enum UF_PARAM_ipw_save_method_e
{
    UF_PARAM_ipw_save_method_no_save = 0,
    UF_PARAM_ipw_save_method_save    = 1

} UF_PARAM_ipw_save_method_t;


/* UF_PARAM_IPW_SAVE_METHOD
 *
 *   Description:
 *      This parameter specifies the status to save automatically
 *      the in-process workpiece.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: In-Process Workpiece Save Method
 *  Variable Name: <prefix>_in_process_workpiece_save_method
 *
 *   Possible Values: UF_PARAM_ipw_save_method_t
 *
 * 
 */
#define UF_PARAM_IPW_SAVE_METHOD   340  /* UF_PARAM_type_int */


/* UF_PARAM_CUTLEV_GLOBAL_CUT_DEPTH
 *
 *   Description:
 *      This parameter specifies the global depth per cut value
 *      to be used when subdividing cut level ranges. It used
 *      to be named UF_PARAM_CUTLEV_DEPTH_PER_CUT_RANGE1 but
 *      has changed its meaning slightly. 
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Global Depth Per Cut
 *  Variable Name: <prefix>_global_depth_per_cut
 *
 *   Possible Values: zero or positive UF_PARAM_type_double_length
 *
 * 
 */
#define UF_PARAM_CUTLEV_GLOBAL_CUT_DEPTH   342 


typedef enum UF_PARAM_geom_steep_method_e
{
    UF_PARAM_geom_steep_method_not_applied = 0,
    UF_PARAM_geom_steep_method_applied     = 1

} UF_PARAM_geom_steep_method_t;


/* UF_PARAM_GEOM_STEEP_METHOD
 *
 *   Description:
 *      This parameter specifies if the steep method
 *      is to be appled during cutting.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Steep Method
 *  Variable Name: <prefix>_steep_method
 *
 *   Possible Values: UF_PARAM_geom_steep_method_t
 *
 * 
 */
#define UF_PARAM_GEOM_STEEP_METHOD   343 


/* UF_PARAM_CUT_MIN_LENGTH
 *   Description:
 *      This parameter specifies that if the length of segments is less than
 *      than this minimum cut length these segments will not be cut.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Minimum Cut Length
 *  Variable Name: <prefix>_minimum_cut_length
 *
 *   Possible Values: positive double
 *
 * 
 */
#define UF_PARAM_CUT_MIN_LENGTH   344 


/* UF_PARAM_Z_DEPTH_OFFSET
 *
 *   Description:
 *      This parameter specifies that for 3d-Curve, the extra depth will
 *      be added to the z coordinate when outputing a point.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Z-Depth Offset
 *  Variable Name: <prefix>_z_depth_offset
 *
 *   Possible Values: double
 *
 * 
 */
#define UF_PARAM_Z_DEPTH_OFFSET   345 


typedef enum UF_PARAM_stock_part_use_e
{
    UF_PARAM_stock_part_use_as_is = 0,
    UF_PARAM_stock_part_use_floor_same_as_side = 1

} UF_PARAM_stock_part_use_t;


/* UF_PARAM_STOCK_PART_USE
 *
 *   Description:
 *      This parameter specifies how the part stocks should be used
 *      in the processing.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Stock Part Use
 *  Variable Name: <prefix>_stock_part_use
 *
 *   Possible Values: UF_PARAM_stock_part_use_t
 *
 * 
 */
#define UF_PARAM_STOCK_PART_USE   346 


typedef enum
{
    UF_PARAM_across_voids_method_follow = 0,
    UF_PARAM_across_voids_method_cut = 1,
    UF_PARAM_across_voids_method_traverse = 2
} UF_PARAM_cut_across_voids_method_t;
 

/* UF_PARAM_ACROSS_VOIDS_METHOD
 *
 *   Description:  
 *      This parameter controls the behavior
 *      of the toolpath when the tool passes
 *      through a void for a Zig, Zig-Zag, or
 *      Zig with Contour cut type.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Across Voids Method
 *  Variable Name: <prefix>_across_voids_method
 *
 *   Possible Values: UF_PARAM_across_voids_method_t
 *
 * 
 */
#define UF_PARAM_ACROSS_VOIDS_METHOD   347 


/* UF_PARAM_MIN_TRAVERSAL_DIST
 *
 *   Description:  
 *      This parameter specifies the minimum distance
 *      required to run the cutter at a traversal feed rate
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Minimum traversal distance
 *  Variable Name: <prefix>_minimum_traversal_distance
 *
 *   Possible Values: double
 *
 * 
 */
#define UF_PARAM_MIN_TRAVERSAL_DIST   348 


typedef enum
{
    UF_PARAM_tool_runoff_method_stay_on_part = 0,
    UF_PARAM_tool_runoff_method_retract_off_part = 1
} UF_PARAM_tool_runoff_method_t;
 

/* UF_PARAM_TOOL_RUNOFF_METHOD
 *
 *   Description:  
 *      This parameter controls whether the tool
 *      will retract off the part or stay on the 
 *      part after each cutting pass. This parameter 
 *      is valid for Zig and Zig-Zag cut types only.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Tool Runoff Method
 *  Variable Name: <prefix>_tool_runoff_method
 *
 *   Possible Values: UF_PARAM_tool_runoff_method_t
 *
 * 
 */
#define UF_PARAM_TOOL_RUNOFF_METHOD   349 


typedef enum
{
    UF_PARAM_level_to_level_method_use_transfer_method = 0,
    UF_PARAM_level_to_level_method_direct_on_part = 1,
    UF_PARAM_level_to_level_method_ramp_on_part = 2,
    UF_PARAM_level_to_level_method_staggered_ramp_on_part = 3
} UF_PARAM_level_to_level_cut_method_t;


/* UF_PARAM_LEVEL_TO_LEVEL_METHOD
 *
 *   Description:
 *      This parameter specifies how to move between
 *      consecutive levels in a zlevel operation.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Level to level method
 *  Variable Name: <prefix>_level_to_level_method
 *
 *   Possible Values: UF_PARAM_level_to_level_method_t
 *
 * 
 */
#define UF_PARAM_LEVEL_TO_LEVEL_METHOD   350  /* UF_PARAM_type_int */


typedef enum
{
    UF_PARAM_ipw_type_none        = 0,
    UF_PARAM_ipw_type_3d          = 1,
    UF_PARAM_ipw_type_level_based = 2

} UF_PARAM_ipw_type_t;


/* UF_PARAM_IPW_TYPE
 *
 *   Description:
 *      This parameter specifies the type of In-Process-Workpiece used in 
 *   an operation. It replaces the index UF_PARAM_IPW_3D_USAGE 
 *   and its enums UF_PARAM_ipw_3d_usage_none and UF_PARAM_ipw_3d_usage_applied used
 *   in NX1. The enums UF_PARAM_ipw_type_none and UF_PARAM_ipw_type_3d options, are equivalent
 *   to UF_PARAM_ipw_3d_usage_none and UF_PARAM_ipw_3d_usage_applied respectively.
 *
 *      When the value of the index is specified to UF_PARAM_ipw_type_3d, the operation 
 *   will use 3D In-Process-Workpiece based on the order of its previous operations in 
 *   the Program View and these operations inherit the same Blank Geometry group object.
 *
 *      When the value of the index is specified to UF_PARAM_ipw_type_level_based, the 
 *   operation will use Level Based In-Process-Workpiece from a previous Level Based 
 *   operation in the Program View and both operations inherit the same Part group object.  
 *   This enum is only for preview in NX2. If you want to use it, please contact GTAC.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: IPW Type
 *  Variable Name: <prefix>_ipw_type
 *
 *   Possible Values: UF_PARAM_ipw_type_t
 *
 * 
 */
#define UF_PARAM_IPW_TYPE   351  /* UF_PARAM_type_int */


typedef enum
{
    UF_PARAM_minimize_number_of_engages_not_apply = 0,
    UF_PARAM_minimize_number_of_engages_apply = 1

} UF_PARAM_min_num_eng_usage_t;


/* UF_PARAM_CUT_MINIMIZE_NUMBER_OF_ENGAGES
 *
 *   Description:
 *      This parameters determine if we are to  minimize 
 *      the number of engages. This parameter is used in 
 *      parallel (zig-zag, and zig later on) cut types and
 *      in automatic engage  
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Minimize Number of Engages
 *  Variable Name: <prefix>_minimize_number_of_engages
 *
 *   Possible Values:
 *      UF_PARAM_min_num_eng_usage_t
 *      0-not apply
 *      1-apply
 *
 *
 * 
*/
#define UF_PARAM_CUT_MINIMIZE_NUMBER_OF_ENGAGES   352  


typedef enum
{
    UF_PARAM_ret_back_out_type_none = 0,
    UF_PARAM_ret_back_out_type_pattern_center

} UF_PARAM_ret_back_out_type_t;


/* UF_PARAM_RETRACT_BACK_OUT_TYPE
 *
 *   Description:
 *      This parameter determines if the tool retracts
 *      back to the center of the pattern after the
 *      retract move.  It is applied for automatic retract.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Retract Back Out Type
 *  Variable Name: <prefix>_retract_back_out_type
 *
 *   Possible Values:
 *      UF_PARAM_ret_back_out_type_t
 *
 * 
*/
#define UF_PARAM_RETRACT_BACK_OUT_TYPE   353 


typedef enum
{
    UF_PARAM_engage_into_type_none = 0,
    UF_PARAM_engage_into_type_pattern_center_taxis,
    UF_PARAM_engage_into_type_pattern_center_ramp

} UF_PARAM_engage_into_type_t;


/* UF_PARAM_ENGAGE_INTO_TYPE
 *
 *   Description:
 *      This parameter determines if the tool engages
 *      along the tool axis or ramping to the center
 *      of the pattern.  It is applied for automatic
 *      engage.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Engage Into Type
 *  Variable Name: <prefix>_engage_into_type
 *
 *   Possible Values:
 *      UF_PARAM_engage_into_type_t
 *
 * 
*/
#define UF_PARAM_ENGAGE_INTO_TYPE   354 


/* UF_PARAM_MINIMUM_THICKNESS
 *
 *   Description:
 *      A distance offset applied to the traces of
 *      blank geometry selected from 3D-In-Process
 *      Workpiece or Facet Geometry.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Minimum Thickness
 *  Variable Name: <prefix>_minimum_thickness
 *
 *   Possible Values: UF_PARAM_type_double length
 *
 * 
*/
#define UF_PARAM_MINIMUM_THICKNESS   355 


/* UF_PARAM_CUT_TLAXIS_DELTA_TYPE
 *
 *   Description:
 *      This parameter specifies the tool axis change type.
 *
 *
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: tool axis change type
 *  Variable Name: <prefix>_tool_axis_change_type
 *
 *   Possible Values: SCOPR_change_per_step=0,
 *                   SCOPR_change_per_minute=1,
 *                   SCOPR_change_total=2
 *
 * 
 */
#define UF_PARAM_CUT_TLAXIS_DELTA_TYPE   360  /* UF_PARAM_type_int */


/* UF_PARAM_CUT_CONVEX_CORNER_EXTEND
 *
 *   Description:
 *      This parameter specifies whether to extend the tool path at convex corners
 *      rather than tracing around the corner. This is intended to improve sharp corners.
 *      Retricted to fixed axis.
 *
 *   Type: UF_PARAM_type_logical
 *
 *   Name: tool axis change type
 *  Variable Name: <prefix>_tool_axis_change_type
 *
 *   Possible Values: true -extend
 *                    false- not extend
 *
 * 
 */
#define UF_PARAM_CUT_CONVEX_CORNER_EXTEND   361  /* UF_PARAM_type_logical */


typedef enum
{
    UF_PARAM_up_down_extend_off,
    UF_PARAM_up_down_extend_on
  
} UF_PARAM_up_down_extend_t;





/* UF_PARAM_CUT_UPDOWN_EXTEND
 *
 *   Description:
 *      This parameter specifies Up Down Extend
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Up Down Extend
 *  Variable Name: <prefix>_up_down_extend
 *
 *   Possible Values: UF_PARAM_up_down_extend_t
 *
 * 
 */
#define UF_PARAM_CUT_UPDOWN_EXTEND   362  /* UF_PARAM_type_int */


/* UF_PARAM_CUT_CONVEX_LIFT
 *
 *   Description:
 *      This parameter specifies whether to lift at Convex Corners. This is intended
 *      to give the NC programer controll at the convex corners in order to improve
 *      quality of the corners.
 *      Retricted to variable axis.
 *
 *   Type: UF_PARAM_type_logical
 *
 *   Name: Convex Lift
 *  Variable Name: <prefix>_convex_lift
 *
 *   Possible Values: true - lift at convex corner
 *                    false- not lift at convex corner
 *
 * 
 *
 */
#define UF_PARAM_CUT_CONVEX_LIFT   363  /* UF_PARAM_type_logical */


typedef enum
{ 
    UF_PARAM_cleanup_type_off = 0,
    UF_PARAM_cleanup_type_uncut_valley = 1,
    UF_PARAM_cleanup_type_steep_area = 2,
    UF_PARAM_cleanup_type_both = 3,
    UF_PARAM_cleanup_type_flowcut_contacts = 4,
    UF_PARAM_cleanup_type_flowcut_toolend = 5,
    UF_PARAM_cleanup_type_flowcut_both = 6
  
} UF_PARAM_cleanup_type_t; 


/* UF_PARAM_CLEANUP_TYPE
 *
 *   Description:
 *      This parameter specifies the cleanup type
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: cleanup type
 *  Variable Name: <prefix>_cleanup_type
 *
 *   Possible Values: UF_PARAM_cleanup_type_t 
 *
 * 
 */
#define UF_PARAM_CLEANUP_TYPE   364  /* UF_PARAM_type_int */


typedef enum
{ 
    UF_PARAM_cleanup_geom_type_point = 0,
    UF_PARAM_cleanup_geom_type_bnd   = 1 
  
} UF_PARAM_cleanup_geom_type_t; 


/* UF_PARAM_CLEANUP_GEOM_TYPE
 *
 *   Description:
 *      This parameter specifies the cleanup output geometry type
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: cleanup outputing geometry type
 *  Variable Name: <prefix>_cleanup_outputing_geometry_type
 *
 *   Possible Values: UF_PARAM_cleanup_geom_type_t
 *
 * 
 */
#define UF_PARAM_CLEANUP_GEOM_TYPE   365  /* UF_PARAM_type_int */


/* UF_PARAM_VALLEY_STEEP_ANGLE
 *
 *   Description:
 *      This paramete specifies the cleanup steep angle
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Valley Steep Angle
 *  Variable Name: <prefix>_valley_steep_angle
 *
 *   Possible Values: double
 *
 * 
 */
#define UF_PARAM_VALLEY_STEEP_ANGLE   366  /* UF_PARAM_type_double */


/* UF_PARAM_VALLEY_OVERLAP_DIST
 *
 *   Description:
 *      This parameter specifies the overlap distance for valley uncut areas
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Valley overlap distance
 *  Variable Name: <prefix>_valley_overlap_distance
 *
 *   Possible Values: double
 *
 * 
 */
#define UF_PARAM_VALLEY_OVERLAP_DIST   367  /* UF_PARAM_type_double_length */


/* UF_PARAM_VALLEY_MERGE_DIST
 *
 *   Description:
 *      This parameter specifies merge distance for valley uncut area
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Valley merge distance
 *  Variable Name: <prefix>_valley_merge_distance
 *
 *   Possible Values: double
 *
 * 
 */
#define UF_PARAM_VALLEY_MERGE_DIST   368  /* UF_PARAM_type_double_length */


/* UF_PARAM_STEEP_OVERLAP_DIST
 *
 *   Description:
 *      This parameter specifies overlap distance for steep uncut area
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: steep overlap distance
 *  Variable Name: <prefix>_steep_overlap_distance
 *
 *   Possible Values: double
 *
 * 
 */
#define UF_PARAM_STEEP_OVERLAP_DIST   369  /* UF_PARAM_type_double_length */


/* UF_PARAM_STEEP_MERGE_DIST
 *
 *   Description:
 *      This parameter specifies merge distance for steep uncut area
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Steep merge distance
 *  Variable Name: <prefix>_steep_merge_distance
 *
 *   Possible Values: double
 *
 * 
 */
#define UF_PARAM_STEEP_MERGE_DIST   370  /* UF_PARAM_type_double_length */


/* UF_PARAM_EXTRA_CROSS_METHOD
 *
 *   Description:
 *      This parameters specifies if cleanup extra cross-cut is generated
 *
 *   Type: UF_PARAM_type_logical
 *
 *   Name: cleanup extra cross cut
 *  Variable Name: <prefix>_cleanup_extra_cross_cut
 *
 *   Possible Values:
 *       false-off
 *     true-on
 *
 * 
 */
#define UF_PARAM_EXTRA_CROSS_METHOD   371  /* UF_PARAM_type_logical */


typedef enum
{
    UF_PARAM_cleanup_directional_steep_none = 0,
    UF_PARAM_cleanup_non_directional_steep = 1,
    UF_PARAM_cleanup_directional_steep = 2

} UF_PARAM_cleanup_directional_steep_t;


/* UF_PARAM_CLEANUP_DIRED_STEEP
 *
 *   Description:
 *      This parameter specifies steep types
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: steep types to be detected
 *  Variable Name: <prefix>_steep_types_to_be_detected
 *
 *   Possible Values: UF_PARAM_cleanup_directional_steep_t
 *
 * 
 */
#define UF_PARAM_CLEANUP_DIRED_STEEP   372  /* UF_PARAM_type_int */


/* UF_PARAM_GEOM_CHECK_CLR_MIN
 *
 *   Description:
 *      This parameter specifies Safe Clearance for Check
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Safe Clearance for Check
 *  Variable Name: <prefix>_safe_clearance_for_check
 *
 *   Possible Values: Positive double
 *
 * 
 */
#define UF_PARAM_GEOM_CHECK_CLR_MIN   374  /* UF_PARAM_type_double_length */


/* UF_PARAM_CUT_TL_HOLDER_USAGE
 *
 *   Description:
 *      This parameters specifies Use Tool Holder flag
 *
 *   Type: UF_PARAM_type_logical
 *
 *   Name: Use Tool Holder flag
 *  Variable Name: <prefix>_use_tool_holder_flag
 *
 *   Possible Values:
 *       false - Use Tool Holder off
 *     true  - Use Tool Holder on
 *
 * 
 */
#define UF_PARAM_CUT_TL_HOLDER_USAGE   375  /* UF_PARAM_type_logical */


/* UF_PARAM_STOCK_PART_OFFSET
 *
 *   Description:
 *      This parameter specifies initial part stock minus part stock
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Surface Contour Part Stock Offset
 *  Variable Name: <prefix>_surface_contour_part_stock_offset
 *
 *   Possible Values: Zero or positive double
 *
 * 
 *
 */
#define UF_PARAM_STOCK_PART_OFFSET   376  /* UF_PARAM_type_double_length */


typedef enum UF_PARAM_use_previous_ipw_e
{
    UF_PARAM_use_previous_ipw_no = 0,
    UF_PARAM_use_previous_ipw_yes = 1

} UF_PARAM_use_previous_ipw_t;


/* UF_PARAM_USE_PREVIOUS_IPW
 *
 *   Description:
 *      This parameter specifies whether the IPW from a previously generated
 *      operation is to be used as input to the current operation
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Use Previous IPW Flag
 *  Variable Name: <prefix>_use_previous_ipw_flag
 *
 *   Possible Values: UF_PARAM_use_previous_ipw_t
 *
 * 
 *
 */
#define UF_PARAM_USE_PREVIOUS_IPW   377  /* UF_PARAM_type_logical */


typedef enum
{
    UF_PARAM_cut_walls_only_off = 0,    /* Tool will cut along all part segments of the region. */
    UF_PARAM_cut_walls_only_on  = 1    /* Tool will only cut along part segments that lie on a wall. */

} UF_PARAM_cut_walls_only_status_t;


/* UF_PARAM_CUT_WALLS_ONLY
 *
 *   Description:
 *      This parameter specifies if the tool is to cut along all
 *      part segments of the machine regions or only along
 *      part segments that lie on a wall.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Cut Walls Only
 *  Variable Name: <prefix>_cut_walls_only
 *
 *   Possible Values: UF_PARAM_cut_walls_only_status_t
 *
 * 
 */
#define UF_PARAM_CUT_WALLS_ONLY   383  /* UF_PARAM_type_int */


/* UF_PARAM_RAMP_BETWEEN_LEVELS_ANGLE
 *
 *   Description:
 *      Parameter is the ramping angle used by
 *      Zlevel operations to ramp from one level
 *      to the next
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Ramp Between Levels Angle
 *  Variable Name: <prefix>_ramp_between_levels_angle
 *
 *   Possible Values: UF_PARAM_type_double
 *                    0 < ramp angle < 90
 *
 * 
 */
#define UF_PARAM_RAMP_BETWEEN_LEVELS_ANGLE   384  /* UF_PARAM_type_double */


typedef enum UF_PARAM_trochoid_path_width_type_e
{
    UF_PARAM_trochoid_path_width_type_distance = 0,
    UF_PARAM_trochoid_path_width_type_percent_tool_diameter = 1

} UF_PARAM_trochoid_path_width_type_t;


/* UF_PARAM_TROCHOID_PATH_WIDTH_TYPE
 *
 *   Description:
 *      This parameter specifies the path width type for
 *      the trochoidal cut method.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Trochoidal Path Width Type
 *  Variable Name: <prefix>_trochoidal_path_width_type
 *
 *   Possible Values: UF_PARAM_trochoid_path_width_type_t
 *
 * 
 *
 */
#define UF_PARAM_TROCHOID_PATH_WIDTH_TYPE   390  /* UF_PARAM_type_int */


/* UF_PARAM_TROCHOID_PATH_WIDTH_DIST
 *
 *   Description:
 *      Parameter is the distance value used by the path
 *      width type - Distance for the trochoidal cut method.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Trochoidal Path Width Distance
 *  Variable Name: <prefix>_trochoidal_path_width_distance
 *
 *   Possible Values: non-negative UF_PARAM_type_double_length
 *
 * 
 *
 */
#define UF_PARAM_TROCHOID_PATH_WIDTH_DIST   391  /* UF_PARAM_type_double_length */


/* UF_PARAM_TROCHOID_PATH_WIDTH_PERCENT
 *
 *   Description:
 *      Parameter is the value of the percentage used by
 *      the path width type - % Tool Diameter for the 
 *      trochoidal cut method.
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Trochoidal Path Width Percent
 *  Variable Name: <prefix>_trochoidal_path_width_percent
 *
 *   Possible Values: non-negative double
 *
 * 
 *
 */
#define UF_PARAM_TROCHOID_PATH_WIDTH_PERCENT   392  /* UF_PARAM_type_double */


typedef enum
{
    UF_PARAM_corner_loops_status_off,
    UF_PARAM_corner_loops_status_on

} UF_PARAM_corner_loops_status_t;


/* UF_PARAM_CORNER_LOOPS
 *
 *   Description:
 *      This parameter indicates if the trochoidal pattern will insert
 *      loops, as needed, to maintain a continous tangent vector at 
 *      all corners.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Corner Loops
 *  Variable Name: <prefix>_corner_loops
 *
 *   Possible Values: UF_PARAM_corner_loops_status_t.
 *
 * 
 *
 */
#define UF_PARAM_CORNER_LOOPS   394  /* UF_PARAM_type_int */


/* UF_PARAM_CUTAREA_EXTENSION_DIST
 *
 *   Description:
 *      This parameter is the 2D distance by which the system 
 *   will extend the machining area when not totally contained 
 *   inside a cavity.
 *
 *   Type: UF_PARAM_double_length
 *
 *   Name: Cut Area Extension Distance
 *  Variable Name: <prefix>_cut_area_extension_distance
 *
 *   Possible Values: 0.0 or positive UF_PARAM_double_length
 *
 * 
 *
 */
#define UF_PARAM_CUTAREA_EXTENSION_DIST   395  /* UF_PARAM_type_double_length */


typedef enum UF_PARAM_max_cut_traverse_type_e
{
    UF_PARAM_max_cut_traverse_type_inactive,
    UF_PARAM_max_cut_traverse_type_distance,
    UF_PARAM_max_cut_traverse_type_percent_tool_diameter

} UF_PARAM_max_cut_traverse_type_t;

/* Obseleted synonym
   #define UF_PARAM_TROCHOID_MAXIMUM_STEPOVER_TYPE_INDEX   397   UF_PARAM_type_int */

/* UF_PARAM_MAX_CUT_TRAVERSE_TYPE
 *
 *   Description:
 *      This parameter determines how the maximum cut traverse distance is specified.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Maximum Cut Traverse Specification Type
 *  Variable Name: <prefix>_maximum_cut_traverse_specification_type
 *
 *   Possible Values: UF_PARAM_max_cut_traverse_type_t
 *
 * 
 *
 */
#define UF_PARAM_MAX_CUT_TRAVERSE_TYPE   397  /* UF_PARAM_type_int */


/* UF_PARAM_MAX_CUT_TRAVERSE_DISTANCE
 *
 *   Description:
 *      Parameter is the maximum cut traverse distance.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Maximum Stepover Traverse Specified By Distance
 *  Variable Name: <prefix>_maximum_stepover_traverse_specified_by_distance
 *
 *   Possible Values: non-negative UF_PARAM_type_double_length
 *
 * 
 *
 */
#define UF_PARAM_MAX_CUT_TRAVERSE_DISTANCE   398  /* UF_PARAM_type_double_length */


/* UF_PARAM_MAX_CUT_TRAVERSE_PERCENT
 *
 *   Description:
 *      Parameter is the value of the percentage used by
 *      the max cut traverse type - % Tool Diameter for the 
 *      max cut traverse.
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Maximum Cut Traverse Specified As Percent Tool Diameter
 *  Variable Name: <prefix>_maximum_cut_traverse_specified_as_percent_tool_diameter
 *
 *   Possible Values: non-negative double
 *
 * 
 *
 */
#define UF_PARAM_MAX_CUT_TRAVERSE_PERCENT   399  /* UF_PARAM_type_double */


typedef enum UF_PARAM_edge_trace_removal_e
{
    UF_PARAM_edge_trace_removal_off = 0,
    UF_PARAM_edge_trace_removal_on = 1

} UF_PARAM_edge_trace_removal_t;


/* UF_PARAM_CUT_EDGE_TRACE_REMOVAL
 *
 *   Description:
 *      This parameters specifies Edge Trace Removed Flag
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Edge Trace Removal Flag
 *  Variable Name: <prefix>_edge_trace_removal_flag
 *
 *   Possible Values: UF_PARAM_edge_trace_removal_t
 *
 * 
 */
#define UF_PARAM_CUT_EDGE_TRACE_REMOVAL   400  /* UF_PARAM_type_int */


/* UF_PARAM_CUT_RAMP_DOWN_MAX_ANGLE
 *
 *   Description:
 *      This parameter specifies maximum ramp down angle
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Ramp Down Angle
 *  Variable Name: <prefix>_ramp_down_angle
 *
 *   Possible Values: a value in radians, in the range of
 *                    0 to 90 degrees
 *
 * 
 */
#define UF_PARAM_CUT_RAMP_DOWN_MAX_ANGLE   401  /*   */


/* UF_PARAM_CUT_RAMP_UP_MAX_ANGLE
 *
 *   Description:
 *      This parameter specifies maximum ramp up angle
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Ramp Up Angle
 *  Variable Name: <prefix>_ramp_up_angle
 *
 *   Possible Values: a value in radians, in the range of 
 *                    0 to 90 degrees
 *
 * 
 */
#define UF_PARAM_CUT_RAMP_UP_MAX_ANGLE   402  /*   */


typedef enum
{
    UF_PARAM_cut_ramp_method_off,
    UF_PARAM_cut_ramp_method_on

} UF_PARAM_cut_ramp_method_t; 


/* UF_PARAM_CUT_RAMP_METHOD
 *
 *   Description:
 *      This parameter specifies whether to use the cut ramp method
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Ramp Up Down Flag
 *  Variable Name: <prefix>_ramp_up_down_flag
 *
 *   Possible Values: UF_PARAM_cut_ramp_method_t
 *
 * 
 */
#define UF_PARAM_CUT_RAMP_METHOD   403  /* UF_PARAM_type_int */


typedef enum
{
    UF_PARAM_ramp_optimize_flag_off,
    UF_PARAM_ramp_optimize_flag_on

} UF_PARAM_ramp_optimize_flag_t; 


/* UF_PARAM_CUT_RAMP_OPTIMIZE_METHOD
 *
 *   Description:
 *      This parameter specifies Ramp Up Down Optimize Flag
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Ramp Up Down Optimize Flag
 *  Variable Name: <prefix>_ramp_up_down_optimize_flag
 *
 *   Possible Values: UF_PARAM_ramp_optimize_flag_t
 *
 * 
 */
#define UF_PARAM_CUT_RAMP_OPTIMIZE_METHOD   404  /* UF_PARAM_type_int */


typedef enum
{
    UF_PARAM_cut_dir_undefined,
    UF_PARAM_cut_dir_climb,
    UF_PARAM_cut_dir_conventional
 
} UF_PARAM_cut_dir_type_t;


/* UF_PARAM_CUT_DIR_TYPE
 *
 *   Description:
 *      This parameter specifies cut direction type
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Cut Direction Type
 *  Variable Name: <prefix>_cut_direction_type
 *
 *   Possible Values: UF_PARAM_cut_dir_type_t
 *
 * 
 */
#define UF_PARAM_CUT_DIR_TYPE   405  /* UF_PARAM_type_int */


typedef enum
{
    UF_PARAM_cut_multi_depth_flag_off,
    UF_PARAM_cut_multi_depth_flag_on 
 
} UF_PARAM_cut_multi_depth_flag_t;


/* UF_PARAM_CUT_MULTI_DEPTH_METHOD
 *
 *   Description:
 *      This parameter specifies Multi-Depth cut flag
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Multi-Depth Cut Flag
 *  Variable Name: <prefix>_multi_depth_cut_flag
 *
 *   Possible Values: UF_PARAM_cut_multi_depth_flag_t
 *
 * 
*/
#define UF_PARAM_CUT_MULTI_DEPTH_METHOD   406  /* UF_PARAM_type_int */


typedef enum
{
    UF_PARAM_cut_multi_depth_type_increment,
    UF_PARAM_cut_multi_depth_type_passes 
 
} UF_PARAM_cut_multi_depth_type_t;


/* UF_PARAM_MCUTTY
 *
 *   Description:
 *      This parameter specifies Multi-Depth cut type
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Multi-Depth Cut Type
 *  Variable Name: <prefix>_multi_depth_cut_type
 *
 *   Possible Values: UF_PARAM_cut_multi_depth_type_t
 *
 * 
*/
#define UF_PARAM_MCUTTY   407  /* UF_PARAM_type_int */


/* UF_PARAM_CUT_MULTI_DEPTH_PASSES
 *
 *   Description:
 *      This parameter specifies Number of passes for
 *   multiple depth cut
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Number of passes for multiple depth cut
 *  Variable Name: <prefix>_number_of_passes_for_multiple_depth_cut
 *
 *   Possible Values: positive integer
 *
 * 
*/
#define UF_PARAM_CUT_MULTI_DEPTH_PASSES   408  /* UF_PARAM_type_int */


/* UF_PARAM_TLAXIS_MAX_LEAD_ANGLE
 *
 *   Description:
 *      This parameter specifies maximum tool axis lead angle
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Max Tool Axis Lead Angle
 *  Variable Name: <prefix>_max_tool_axis_lead_angle
 *
 *   Possible Values:
 *             double
 *
 *
 * 
 */
#define UF_PARAM_TLAXIS_MAX_LEAD_ANGLE   410  /*   */


/* UF_PARAM_TLAXIS_MIN_LEAD_ANGLE
 *
 *   Description:
 *      This parameter specifies minimum tool axis lead angle
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Min Tool Axis Lead Angle
 *  Variable Name: <prefix>_min_tool_axis_lead_angle
 *
 *   Possible Values:
 *             double
 *
 *
 * 
 */
#define UF_PARAM_TLAXIS_MIN_LEAD_ANGLE   411  /*   */


/* UF_PARAM_TLAXIS_MAX_TILT_ANGLE
 *
 *   Description:
 *      This parameter specifies maximum tool axis tilt angle
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Max Tool Axis Tilt Angle
 *  Variable Name: <prefix>_max_tool_axis_tilt_angle
 *
 *   Possible Values:
 *             double
 *
 *
 * 
 */
#define UF_PARAM_TLAXIS_MAX_TILT_ANGLE   412  /*   */


/* UF_PARAM_TLAXIS_MIN_TILT_ANGLE
 *
 *   Description:
 *      This parameter specifies minimum tool axis tilt angle
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Min Tool Axis Tilt Angle
 *  Variable Name: <prefix>_min_tool_axis_tilt_angle
 *
 *   Possible Values:
 *             double
 *
 * 
 */
#define UF_PARAM_TLAXIS_MIN_TILT_ANGLE   413  /*   */


/* UF_PARAM_CUT_MULTI_DEPTH_INCR
 *
 *   Description:
 *      This parameter specifies cut multiple depth
 *      increment.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Multi-Depth Cut Increment
 *  Variable Name: <prefix>_multi_depth_cut_increment
 *
 *   Possible Values:
 *             double
 *
 * 
*/
#define UF_PARAM_CUT_MULTI_DEPTH_INCR   414  /*   */


/* UF_PARAM_MIN_CUT_LENGHT
 *
 *  Description:
 *      This parameters specifies minimum length of cutting moves
 *
 *  Type: UF_PARAM_type_double_length
 *
 *  Name: Min Cut Length
 *  Variable Name: <prefix>_min_cut_length
 *
 *  Possible Values: positive UF_PARAM_type_double_length
 *
 * 
*/
#define UF_PARAM_MIN_CUT_LENGHT   415  /* UF_PARAM_type_double_length */


/* UF_PARAM_MAX_CONCAVITY_ANGLE
 *
 *  Description:
 *      This parameters specifies maximum angle of concavity
 *
 *  Type: UF_PARAM_type_double
 *
 *  Name: Max Concavity Angle
 *  Variable Name: <prefix>_max_concavity_angle
 *
 *  Possible Values: > 0. and <= 179. degrees
 *             
 * 
*/
#define UF_PARAM_MAX_CONCAVITY_ANGLE   416  /* UF_PARAM_type_double */


/* UF_PARAM_MERGE_DIST
 *
 *  Description:
 *      This parameters specifies merge distance to connect the disjoined cutting motions.
 *
 *  Type: UF_PARAM_type_double_length
 *
 *  Name: Hookup Distance
 *  Variable Name: <prefix>_hookup_distance
 *
 *  Possible Values: positive UF_PARAM_type_double_length
 *
 * 
*/
#define UF_PARAM_MERGE_DIST   417  /* UF_PARAM_type_double_length */


typedef enum
{
    UF_PARAM_fcut_mode_single   = 0,
    UF_PARAM_fcut_mode_multiple = 1,
    UF_PARAM_fcut_mode_reftool  = 2
    
} UF_PARAM_fcut_mode_t;


/* UF_PARAM_FLOWCUT_MODE
 *
 *  Description:
 *      This parameters specifies flow cut mode
 *
 *  Type:  UF_PARAM_type_int
 *
 *  Name: Flow Cut Mode
 *  Variable Name: <prefix>_flow_cut_mode
 *
 *  Possible Values: UF_PARAM_fcut_mode_t
 *
 * 
*/
#define UF_PARAM_FLOWCUT_MODE   418  /* UF_PARAM_type_int */


/* UF_PARAM_FLOWCUT_OVERLAP_DIST
 *
 *  Description: 
 *      This parameter specifies the width of the extended area defined by the flow cut 
 *  Reference Tool Diameter along the tangent surfaces.
 *
 *  Type: UF_PARAM_type_double_length
 *
 *  Name: Flow Cut Overlap Distance
 *  Variable Name: <prefix>_flow_cut_overlap_distance
 *
 *  Possible Values: positive UF_PARAM_type_double_length
 *
 * 
 */
#define UF_PARAM_FLOWCUT_OVERLAP_DIST   419  /* UF_PARAM_type_double_length */


/* UF_PARAM_OFFSETS_NUM
 *
 *   Description:
 *      This parameter specifies the number of offset passes to be generated.          
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Offsets Number
 *  Variable Name: <prefix>_offsets_number
 *
 *   Possible Values: 0 or positive UF_PARAM_type_int
 *
 * 
 */
#define UF_PARAM_OFFSETS_NUM   420  /* UF_PARAM_type_int */


typedef enum
{
    UF_PARAM_inside_out,
    UF_PARAM_outside_in,
    UF_PARAM_steep_last,
    UF_PARAM_steep_first,
    UF_PARAM_inside_out_alternate,
    UF_PARAM_outside_in_alternate

} UF_PARAM_sequence_opt_t;


/* UF_PARAM_SEQUENCE_OPT
 *
 *   Description:
 *      This parameter specifies the order in which the cut passes are excuted.      
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Sequence Option
 *  Variable Name: <prefix>_sequence_option
 *
 *   Possible Values: UF_PARAM_sequence_opt_t
 *
 * 
 */
#define UF_PARAM_SEQUENCE_OPT   421  /* UF_PARAM_type_int */


typedef enum
{
    UF_PARAM_steep_mixed,
    UF_PARAM_steep_high_to_low,
    UF_PARAM_steep_low_to_high

} UF_PARAM_steep_cut_dir_t;


/* UF_PARAM_STEEP_CUT_DIR
 *
 *   Description:
 *      This parameter specifies the cut direction of passes in steep sections.      
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Steep Cut Directin
 *  Variable Name: <prefix>_steep_cut_directin
 *
 *   Possible Values: UF_PARAM_steep_cut_dir_t
 *
 * 
 */
#define UF_PARAM_STEEP_CUT_DIR   423  /* UF_PARAM_type_int */


typedef enum
{
    UF_PARAM_fcut_steep_opt_none,
    UF_PARAM_fcut_steep_opt_steep, 
    UF_PARAM_fcut_steep_opt_non_steep

} UF_PARAM_fcut_steep_opt_t;


/* UF_PARAM_FLOWCUT_STEEP_OPT
 *
 *   Description:
 *      This parameter specifies the steep option of the flow cut.      
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Flow Cut Steep Option
 *  Variable Name: <prefix>_flow_cut_steep_option
 *
 *   Possible Values: UF_PARAM_fcut_steep_opt_t
 *
 * 
 */
#define UF_PARAM_FLOWCUT_STEEP_OPT   424  /* UF_PARAM_type_int */


typedef enum
{
    UF_PARAM_plunge_direction_cut_down = 0,
    UF_PARAM_plunge_direction_cut_up_and_down = 1

} UF_PARAM_plunge_direction_t;


/* UF_PARAM_PLUNGE_DIRECTION
 *
 *   Description:
 *      This parameter specifies the plunge direction
 *      for profile pattern in plunge milling.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Plunge Direction
 *  Variable Name: <prefix>_plunge_direction
 *
 *   Possible Values: UF_PARAM_plunge_direction_t
 *
 * 
 */
#define UF_PARAM_PLUNGE_DIRECTION   427   /* UF_PARAM_type_int */


/* UF_PARAM_RET_AUTO_ANGLE
 *
 *   Description:
 *      This parameter specifies the retract angle in degrees
 *      used in plunge milling.
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Retract Out Angle
 *  Variable Name: <prefix>_retract_out_angle
 *
 *   Possible Values: non-negative UF_PARAM_type_double
 *
 * 
 */
#define UF_PARAM_RET_AUTO_ANGLE   428   /* UF_PARAM_type_double */


typedef enum
{
    UF_PARAM_max_cut_width_type_distance = 0,
    UF_PARAM_max_cut_width_type_percent_tool_diameter = 1

} UF_PARAM_max_cut_width_type_t;


/* UF_PARAM_MAX_CUT_WIDTH_TYPE
 *
 *   Description:
 *      This parameter specifies the maximum cut width type for
 *      Plunge Milling.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Max Cut Width Type
 *  Variable Name: <prefix>_max_cut_width_type
 *
 *   Possible Values: UF_PARAM_max_cut_width_type_t
 *
 * 
 */
#define UF_PARAM_MAX_CUT_WIDTH_TYPE   429  /* UF_PARAM_type_int */


/* UF_PARAM_MAX_CUT_WIDTH_DIST
 *
 *   Description:
 *      Parameter is the distance value used by the maximum cut
 *      width type - Distance for Plunge Milling.

 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Max Cut Width Distance
 *  Variable Name: <prefix>_max_cut_width_distance
 *
 *   Possible Values: positive UF_PARAM_type_double_length
 *
 * 
 */
#define UF_PARAM_MAX_CUT_WIDTH_DIST   430   /* UF_PARAM_type_double_length */


/* UF_PARAM_MAX_CUT_WIDTH_PERCENT
 *
 *   Description:
 *      Parameter is the distance value used by the maximum cut
 *      width type - % Tool Diameter for Plunge Milling.

 *   Type: UF_PARAM_type_double
 *
 *   Name: Max Cut Width Percent
 *  Variable Name: <prefix>_max_cut_width_percent
 *
 *   Possible Values: positive UF_PARAM_type_double
 *
 * 
 */
#define UF_PARAM_MAX_CUT_WIDTH_PERCENT   431   /* UF_PARAM_type_double */


typedef enum
{
    UF_PARAM_step_ahead_type_distance = 0,
    UF_PARAM_step_ahead_type_percent_tool_diameter = 1

} UF_PARAM_step_ahead_type_t;


/* UF_PARAM_STEP_AHEAD_TYPE
 *
 *   Description:
 *      This parameter specifies the step ahead type for
 *      Plunge Milling.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Step Ahead Type
 *  Variable Name: <prefix>_step_ahead_type
 *
 *   Possible Values: UF_PARAM_step_ahead_type_t
 *
 * 
 */
#define UF_PARAM_STEP_AHEAD_TYPE   432  /* UF_PARAM_type_int */


/* UF_PARAM_STEP_AHEAD_DIST
 *
 *   Description:
 *      Parameter is the distance value used by the step ahead
 *      type - Distance for Plunge Milling.

 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Step Ahead Distance
 *  Variable Name: <prefix>_step_ahead_distance
 *
 *   Possible Values: positive UF_PARAM_type_double_length
 *
 * 
 */
#define UF_PARAM_STEP_AHEAD_DIST   433   /* UF_PARAM_type_double_length */


/* UF_PARAM_STEP_AHEAD_PERCENT
 *
 *   Description:
 *      Parameter is the distance value used by the step ahead
 *      type - % Tool Diameter for Plunge Milling.

 *   Type: UF_PARAM_type_double
 *
 *   Name: Step Ahead Percent
 *  Variable Name: <prefix>_step_ahead_percent
 *
 *   Possible Values: positive UF_PARAM_type_double
 *
 * 
 */
#define UF_PARAM_STEP_AHEAD_PERCENT   434   /* UF_PARAM_type_double */


typedef enum UF_PARAM_trochoid_path_stepover_type_e
{
    UF_PARAM_trochoid_path_stepover_type_distance = 0,
    UF_PARAM_trochoid_path_stepover_type_percent_tool_diameter = 1

} UF_PARAM_trochoid_path_stepover_type_t;


/* UF_PARAM_TROCHOID_PATH_STEPOVER_TYPE
 *
 *   Description:
 *      This parameter specifies the path stepover type for
 *      the trochoidal outward cut method. This controls the
 *      value by which the trochoidal circles are spread along
 *      the original toolpath.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Trochoidal Path Stepover Type
 *  Variable Name: <prefix>_trochoidal_path_stepover_type
 *
 *   Possible Values: UF_PARAM_trochoid_path_stepover_type_t
 *
 * 
 *
 */
#define UF_PARAM_TROCHOID_PATH_STEPOVER_TYPE   450  /* UF_PARAM_type_int */


/* UF_PARAM_TROCHOID_PATH_STEPOVER_DIST
 *
 *   Description:
 *      Parameter is the distance value used by the path
 *      stepover type - Distance for the trochoidal outward
 *      cut method.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Trochoidal Path Stepover Distance
 *  Variable Name: <prefix>_trochoidal_path_stepover_distance
 *
 *   Possible Values: non-negative UF_PARAM_type_double_length
 *
 * 
 *
 */
#define UF_PARAM_TROCHOID_PATH_STEPOVER_DIST   451  /* UF_PARAM_type_double_length */


/* UF_PARAM_TROCHOID_PATH_STEPOVER_PERCENT
 *
 *   Description:
 *      Parameter is the value of the percentage used by
 *      the path stepover type - % Tool Diameter for the 
 *      trochoidal outward cut method.
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Trochoidal Path Stepover Percent
 *  Variable Name: <prefix>_trochoidal_path_stepover_percent
 *
 *   Possible Values: non-negative double
 *
 * 
 *
 */
#define UF_PARAM_TROCHOID_PATH_STEPOVER_PERCENT   452  /* UF_PARAM_type_double */


/* UF_PARAM_TOOL_EMBEDDING_LIMIT_PERCENT
 *
 *   Description:
 *      This parameter specifies the maximum stepover that
 *      can occur before the tool is considered to be embedded
 *      It is a percentage of the stepover value.
 *      This is for the trochoidal outward cut method
 *      as well as for corner rounding
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Tool Embedding Limit
 *  Variable Name: <prefix>_tool_embedding_limit
 *
 *   Possible Values: Within the range [100, 300]
 *
 * 
 *
 */
#define UF_PARAM_TOOL_EMBEDDING_LIMIT_PERCENT   453  /* UF_PARAM_type_double */


/* UF_PARAM_TROCHOID_STEPOVER_LIMIT_PERCENT
 *
 *   Description:
 *      This parameter specifies the maximum stepover that
 *      can occur before the path is converted to trochoidal geometry.
 *      It is a percentage of the stepover value.
 *      This is for the trochoidal outward cut method.
 *
 *      This parameter is obsolete.
 *      Use UF_PARAM_TOOL_EMBEDDING_LIMIT_PERCENT instead
 *      
 *   Type: UF_PARAM_type_double
 *
 *   Name: Trochoidal Stepover Limit
 *  Variable Name: <prefix>_trochoidal_stepover_limit
 *
 *   Possible Values: Within the range [100, 300]
 *
 * 
 *
 */
#define UF_PARAM_TROCHOID_STEPOVER_LIMIT_PERCENT   453  /* UF_PARAM_type_double */


typedef enum UF_PARAM_trochoid_path_min_width_type_e
{
    UF_PARAM_trochoid_path_min_width_type_distance = 0,
    UF_PARAM_trochoid_path_min_width_type_percent_tool_diameter = 1

} UF_PARAM_trochoid_path_min_width_type_t;


/* UF_PARAM_TROCHOID_PATH_MIN_WIDTH_TYPE
 *
 *   Description:
 *      This parameter specifies the path minimum width type for
 *      the trochoidal outward cut method.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Trochoidal Path Min Width Type
 *  Variable Name: <prefix>_trochoidal_path_min_width_type
 *
 *   Possible Values: UF_PARAM_trochoid_path_min_width_type_t
 *
 * 
 *
 */
#define UF_PARAM_TROCHOID_PATH_MIN_WIDTH_TYPE   454  /* UF_PARAM_type_int */


/* UF_PARAM_TROCHOID_PATH_MIN_WIDTH_DIST
 *
 *   Description:
 *      Parameter is the distance value used by the path
 *      min width type - Distance for the trochoidal outward
 *      cut method.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Trochoidal Path Min Width Distance
 *  Variable Name: <prefix>_trochoidal_path_min_width_distance
 *
 *   Possible Values: non-negative UF_PARAM_type_double_length
 *
 * 
 *
 */
#define UF_PARAM_TROCHOID_PATH_MIN_WIDTH_DIST   455  /* UF_PARAM_type_double_length */


/* UF_PARAM_TROCHOID_PATH_MIN_WIDTH_PERCENT
 *
 *   Description:
 *      Parameter is the value of the percentage used by
 *      the path min width type - % Tool Diameter for the 
 *      trochoidal outward cut method.
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Trochoidal Path Min Width Percent
 *  Variable Name: <prefix>_trochoidal_path_min_width_percent
 *
 *   Possible Values: non-negative double
 *
 * 
 *
 */
#define UF_PARAM_TROCHOID_PATH_MIN_WIDTH_PERCENT   456  /* UF_PARAM_type_double */


/* UF_PARAM_FACE_STOCK
 *
 *   Description:
 *      Parameter is the Face Stock for Lathe applications
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Face Stock
 *  Variable Name: <prefix>_face_stock
 *
 *   Possible Values: UF_PARAM_type_double_length
 *
 * 
 */
#define UF_PARAM_FACE_STOCK   502  /*   */


/* UF_PARAM_RAD_STOCK
 *
 *   Description:
 *      Parameter is the Diameter Stock for Lathe applications
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Radial Stock
 *  Variable Name: <prefix>_radial_stock
 *
 *   Possible Values: UF_PARAM_type_double_length
 *
 * 
 */
#define UF_PARAM_RAD_STOCK   503  /*   */


/* UF_PARAM_LOCAL_RTN_PT
 *
 *   Description:
 *      This index specifies the tag to the local return point.
 *
 *   Type: UF_PARAM_type_tag
 *
 *   Name: Local Return Point
 *  Variable Name: <prefix>_local_return_point
 *
 *   Possible Values:
 *         0 (no entity)
 *         entity value referencing local return point
 *
 * 
 */
#define UF_PARAM_LOCAL_RTN_PT   519  /* UF_PARAM_type_tag */


/* UF_PARAM_LOCAL_RTN_ORDER
 *
 *   Description:
 *      This index specifies the sequence of local return events in turning.
 *
 *   Type: UF_PARAM_type_vla_int
 *
 *   Name: Local Return Point Output Order
 *  Variable Name: <prefix>_local_return_point_output_order
 *
 *   Possible Values: Array (size of 4) of positive integers (or zero)
 *
 * 
 */
#define UF_PARAM_LOCAL_RTN_ORDER   520  /* UF_PARAM_type_vla_int, size 4*/


/* UF_PARAM_NOPSTOPS
 *
 *   Description:
 *      This index specifies the number of optional stops (opstops)
 *      for a turn threading operation.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Num Optional Stops
 *  Variable Name: <prefix>_num_optional_stops
 *
 *   Possible Values:
 *      integer number of opstops
 *
 * 
 */
#define UF_PARAM_NOPSTOPS   523  /* UF_PARAM_type_int */


/* UF_PARAM_LOC_RTN_MV
 *
 *   Description:
 *      This index specifies the strategy for the local return move
 *      (see possible values).
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Local Return Move
 *  Variable Name: <prefix>_local_return_move
 *
 *   Possible Values:
 *      0 = undefined
 *      1 = direct move
 *      2 = vertical then horizontal
 *      3 = horizontal then vertical
 *      4 = vertical (clearance then direct)
 *      5 = horizontal (clearance then direct)
 *      6 = vertical clearance
 *      7 = horizontal clearance
 *      8 = vertical then horizontal then direct (ID only)
 *      9 = vertical then horizontal then vertical (ID only)
 *     10 = vertical then to horizontal clear plane (ID only)   
 *
 *   In Turning module possible values are:
 *     -1 = none
 *      0 = direct move
 *      1 = radial then axial
 *      2 = axial then radial
 *      3 = clear radial then direct
 *      4 = clear axial then direct
 *      5 = clear radial only
 *      6 = clear axial only
 *      7 = radial then clear axial then direct
 *      8 = radial then axial then radial
 *      9 = radial then clear axial
 *
 * 
 */
#define UF_PARAM_LOC_RTN_MV   525  /* UF_PARAM_type_int */


/* UF_PARAM_LOC_RTN_STATUS
 *
 *   Description:
 *      This index specifies the status of the local return point.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Local Return Status
 *  Variable Name: <prefix>_local_return_status
 *
 *   Possible Values:
 *      0 = undefined 
 *      1 = active 
 *      2 = inactive 
 *
 * 
 */
#define UF_PARAM_LOC_RTN_STATUS   526  /* UF_PARAM_type_int */


/* UF_PARAM_LOC_RTN_MV_STATUS
 *
 *   Description:
 *      This index specifies the status of the local return move.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Local Return Move Status
 *  Variable Name: <prefix>_local_return_move_status
 *
 *   Possible Values:
 *      0 = active 
 *      1 = inactive 
 *
 * 
 */
#define UF_PARAM_LOC_RTN_MV_STATUS   527  /* UF_PARAM_type_int */


/* UF_PARAM_VAR_INCR
 *
 *   Description:
 *      In Turning:
 *      This parameter specifies a set of variable increments for Centerline
 *      Drill methods Variable Break Chip or Peck Drill.
 *      The number of times each increment is repeated is defined by the 
 *      parameter UF_PARAM_NUM_PASSES.
 *
 *   Type: UF_PARAM_type_vla_length
 *
 *   Name: Variable Depth Increment
 *  Variable Name: <prefix>_variable_depth_increment
 *
 *   Possible Values: (In Turning: Array (size of 6) of positive doubles
 *                                 (or zeros))
 *
 *   Developer: (Used in Turning: Oliver Bruegge)
 */
#define UF_PARAM_VAR_INCR   533 


/* UF_PARAM_NUM_PASSES
 *
 *   Description:
 *      In Turning:
 *      This parameter specifies the number of times each increment is repeated
 *      in Centerline Drill methods Variable Break Chip or Peck Drill.
 *      The increments are defined by the parameter UF_PARAM_VAR_INCR.
 *
 *   Type: UF_PARAM_type_vla_int
 *
 *   Name: Num of Passes
 *  Variable Name: <prefix>_num_of_passes
 *
 *   Possible Values: (In Turning: Array (size of 6) of positive ints
 *                                 (or zeros))
 *
 *   Developer: (Used in Turning: Oliver Bruegge)
 */
#define UF_PARAM_NUM_PASSES   534 


typedef enum
{
    UF_PARAM_ttdopr_depth_type_depth = 0,
    UF_PARAM_ttdopr_depth_type_end_point,
    UF_PARAM_ttdopr_depth_type_cross_hole_data,
    UF_PARAM_ttdopr_depth_type_cross_hole,
    UF_PARAM_ttdopr_depth_type_shoulder_depth,
    UF_PARAM_ttdopr_depth_type_countersink_diameter
} UF_PARAM_ttdopr_depth_type_t;

/* UF_PARAM_DEPTH_TYPE
 *
 *   Description:
 *      In Turning:
 *      This parameter specifies the mode how the total depth of a Centerline
 *      Drill hole is defined.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Depth Type
 *  Variable Name: <prefix>_depth_type
 *
 *   Possible Values: (In Turning: UF_PARAM_ttdopr_depth_type_t)
 *
 *   Developer: (Used in Turning: Oliver Bruegge)
 */
#define UF_PARAM_DEPTH_TYPE   603 


/* UF_PARAM_STEEP_ANGLE
 *
 *   Description:
 *      This Parameter specifies an angle used to define steep containment regions.
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Steep Angle
 *  Variable Name: <prefix>_steep_angle
 *
 *   Possible Values: 0.0 <= Steep Angle <= 90.0.
 *
 * 
 */
#define UF_PARAM_STEEP_ANGLE   609  /* UF_PARAM_type_double */


/* UF_PARAM_CONST_INCR
 *
 *   Description:
 *      In Turning:
 *      This parameter specifies the constant increment for Centerline Drill 
 *      methods Constant Break Chip or Peck Drill.
 *
 *   Type: PUF_PARAM_type_double_length
 *
 *   Name: Constant Increment
 *  Variable Name: <prefix>_constant_increment
 *
 *   Possible Values: (In Turning: Positive double (greater than zero))
 *
 *   Developer: (Used in Turning: Oliver Bruegge)
 */
#define UF_PARAM_CONST_INCR   725 


/* UF_PARAM_NUM_STARTS
 *
 *   Description:
 *      This index specifies the number of starts per operation in threading.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Number of Starts
 *  Variable Name: <prefix>_number_of_starts
 *
 *   Possible Values:
 *      UF_PARAM_type_int
 *
 * 
 */
#define UF_PARAM_NUM_STARTS   750  /* UF_PARAM_type_int */


/* UF_PARAM_PITCH_VAR_TYPE
 *
 *   Description:
 *      This index specifies the pitch type for a threading operation.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Pitch Variable Type
 *  Variable Name: <prefix>_pitch_variable_type
 *
 *   Possible Values:
 *      0 = undefined 
 *      1 = constant 
 *      2 = increasing 
 *      3 = decreasing
 *      In Turning: 0 = Constant
 *                  1 = Start & End
 *                  2 = Start & Increment
 *
 * 
 */
#define UF_PARAM_PITCH_VAR_TYPE   754  /* UF_PARAM_type_int */


/* UF_PARAM_PITCH_OUTPUT
 *
 *   Description:
 *      This index specifies the pitch type to output in post command.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Pitch Output Type
 *  Variable Name: <prefix>_pitch_output_type
 *
 *   Possible Values:
 *      1 = pitch
 *      2 = lead
 *      3 = threads per unit
 *      In Turning: 0 = Use input unit
 *                  1 = Pitch
 *                  2 = Lead
 *                  3 = Thread/Unit
 *
 * 
 */
#define UF_PARAM_PITCH_OUTPUT   756  /* UF_PARAM_type_int */


/* UF_PARAM_NUM_CHASES
 *
 *   Description:
 *      This index specifies the number of chase passes for a turn
 *      threading operation.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Number of Chases
 *  Variable Name: <prefix>_number_of_chases
 *
 *   Possible Values:
 *      integer number of chase passes
 *
 * 
 */
#define UF_PARAM_NUM_CHASES   758  /* UF_PARAM_type_int */


/* UF_PARAM_ENTRANCE_DIAM
 *
 *   Description:
 *      In Turning:
 *      This parameter specifies the diameter of an existing countersink. Using
 *      this diameter the system adjusts the contact point of the drill with 
 *      the material.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Entrance Diameter
 *  Variable Name: <prefix>_entrance_diameter
 *
 *   Possible Values: (In Turning: Positive double (or zero))
 *
 *   Developer: (Used in Turning: Oliver Bruegge)
 */
#define UF_PARAM_ENTRANCE_DIAM   800 


/* UF_PARAM_BREAKTHRU_METHOD
 *
 *   Description:
 *      In Turning:
 *      This parameter activates the Break Through to control the distance 
 *      past the shoulder that the tool can exceed the specified depth.
 *      The Break Through Distance is defined by parameter 
 *      UF_PARAM_BREAKTHRU_DIST.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Breakthru Method
 *  Variable Name: <prefix>_breakthru_method
 *
 *   Possible Values: (In Turning: 0 = inactive
 *                                 1 = active)
 *
 *   Developer: (Used in Turning: Oliver Bruegge)
 */
#define UF_PARAM_BREAKTHRU_METHOD   805 


/* UF_PARAM_BREAKTHRU_DIST
 *
 *   Description:
 *      In Turning:
 *      This parameter specifies the Break Through distance to control the 
 *      distance past the shoulder that the tool can exceed the specified depth.
 *      The Break Through is activated by parameter 
 *      UF_PARAM_BREAKTHRU_METHOD.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Breakthru Distance
 *  Variable Name: <prefix>_breakthru_distance
 *
 *   Possible Values: (In Turning: Positive double (or zero))
 *
 *   Developer: (Used in Turning: Oliver Bruegge)
 */
#define UF_PARAM_BREAKTHRU_DIST   806 


/* UF_PARAM_CROSS_HOLE_DIST
 *
 *   Description:
 *      In Turning:
 *      Used in combination with parameters UF_PARAM_CROSS_HOLE_DIAM and
 *      UF_PARAM_CROSS_HOLE_ANG to define the total depth of a Centerline
 *      Drill hole.
 *      This parameter specifies the distance between a Centerline Drill 
 *      start point and the intersection of a cross hole axis with the drill
 *      axis.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Cross Hole Distance
 *  Variable Name: <prefix>_cross_hole_distance
 *
 *   Possible Values: (In Turning: Positive double (or zero))
 *
 *   Developer: (Used in Turning: Oliver Bruegge)
 */
#define UF_PARAM_CROSS_HOLE_DIST   807 


/* UF_PARAM_CROSS_HOLE_DIAM
 *
 *   Description:
 *      In Turning:
 *      Used in combination with parameters UF_PARAM_CROSS_HOLE_DIST and
 *      UF_PARAM_CROSS_HOLE_ANG to define the total depth of a Centerline
 *      Drill hole.
 *      This parameter specifies the diameter of a Centerline Drill cross hole.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Cross Hole Diameter
 *  Variable Name: <prefix>_cross_hole_diameter
 *
 *   Possible Values: (In Turning: Positive double (or zero))
 *
 *   Developer: (Used in Turning: Oliver Bruegge)
 */
#define UF_PARAM_CROSS_HOLE_DIAM   808 


/* UF_PARAM_CROSS_HOLE_ANG
 *
 *   Description:
 *      In Turning:
 *      Used in combination with parameters UF_PARAM_CROSS_HOLE_DIST and
 *      UF_PARAM_CROSS_HOLE_DIAM to define the total depth of a Centerline
 *      Drill hole.
 *      This parameter specifies the angle of the cross hole in radians.
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Cross Hole Angle
 *  Variable Name: <prefix>_cross_hole_angle
 *
 *   Possible Values: Double (In Turning: Angle in radians)
 *
 *   Developer: (Used in Turning: Oliver Bruegge)
 */
#define UF_PARAM_CROSS_HOLE_ANG   809  /*   */


/* UF_PARAM_CROSS_HOLE_TAG
 *
 *   Description:
 *      In Turning:
 *      This parameter holds the object ID of a circle object representing a 
 *      cross hole, which defines the total depth of a Centerline Drill hole.
 *
 *   Type: UF_PARAM_type_tag
 *
 *   Name: Cross Hole Tag
 *  Variable Name: <prefix>_cross_hole_tag
 *
 *   Possible Values: (In Turning: 0 (no entity)
 *                                 entity ID)
 *
 *   Developer: (Used in Turning: Oliver Bruegge)
 */
#define UF_PARAM_CROSS_HOLE_TAG   810 


/* UF_PARAM_WEDM_LOWER_PLANE
 *
 *  Description: Lower wire guide height in Z-axis
 *
 *  Type: UF_PARAM_type_double_length
 *
 *  Name: Wire Guides Lower Plane
 *  Variable Name: <prefix>_wire_guides_lower_plane
 *
 *  Possible Values: UF_PARAM_type_double_length
 *
 * 
 */
#define UF_PARAM_WEDM_LOWER_PLANE   901 


/* UF_PARAM_WEDM_UPPER_PLANE
 *
 *  Description: Upper wire guide height in Z-axis
 *
 *  Type: UF_PARAM_type_double_length
 *
 *  Name: Wire Guides Upper Plane
 *  Variable Name: <prefix>_wire_guides_upper_plane
 *
 *  Possible Values: UF_PARAM_type_double_length
 *
 * 
 */
#define UF_PARAM_WEDM_UPPER_PLANE   902 


/* UF_PARAM_WEDM_LEADIN_DIST
 *
 *  Description: Lead in distance for direct or angular lead in
 *
 *  Type: UF_PARAM_type_double_length
 *
 *  Name: Lead In Distance
 *  Variable Name: <prefix>_lead_in_distance
 *
 *  Possible Values: UF_PARAM_type_double_length
 *
 * 
 */
#define UF_PARAM_WEDM_LEADIN_DIST   904 


/* UF_PARAM_WEDM_LEADIN_ANG
 *
 *  Description: Lead in angle for angular lead in
 *
 *  Type: UF_PARAM_type_double
 *
 *  Name: Lead In Angle
 *  Variable Name: <prefix>_lead_in_angle
 *
 *  Possible Values: UF_PARAM_type_double
 *
 * 
 */
#define UF_PARAM_WEDM_LEADIN_ANG   905 


/* UF_PARAM_WEDM_LEADIN_CUTCOM_DIST
 *
 *  Description: Lead in cutcom distance
 *
 *  Type: UF_PARAM_type_double_length
 *
 *  Name: Lead In Cutcom Distance
 *  Variable Name: <prefix>_lead_in_cutcom_distance
 *
 *  Possible Values: UF_PARAM_type_double_length
 *
 * 
 */
#define UF_PARAM_WEDM_LEADIN_CUTCOM_DIST   906 


/* UF_PARAM_WEDM_LEADIN_RAD
 *
 *  Description: Lead in radius for circular lead in
 *
 *  Type: UF_PARAM_type_double_length
 *
 *  Name: Lead In Radius
 *  Variable Name: <prefix>_lead_in_radius
 *
 *  Possible Values: UF_PARAM_type_double_length
 *
 * 
 */
#define UF_PARAM_WEDM_LEADIN_RAD   907 


/* UF_PARAM_WEDM_LEADIN_CIR_ANG
 *
 *  Description: Lead in angle for circular lead in
 *
 *  Type: UF_PARAM_type_double
 *
 *  Name: Lead In Circular Angle
 *  Variable Name: <prefix>_lead_in_circular_angle
 *
 *  Possible Values: UF_PARAM_type_double
 *
 * 
 */
#define UF_PARAM_WEDM_LEADIN_CIR_ANG   908 


/* UF_PARAM_WEDM_LEADOUT_DIST
 *
 *  Description: Lead out distance for direct or angular lead out
 *
 *  Type: UF_PARAM_type_double_length
 *
 *  Name: Lead Out Distance
 *  Variable Name: <prefix>_lead_out_distance
 *
 *  Possible Values: UF_PARAM_type_double_length
 *
 * 
 */
#define UF_PARAM_WEDM_LEADOUT_DIST   909 


/* UF_PARAM_WEDM_LEADOUT_ANG
 *
 *  Description: Lead out angle for angular lead out
 *
 *  Type: UF_PARAM_type_double
 *
 *  Name: Lead Out Angle
 *  Variable Name: <prefix>_lead_out_angle
 *
 *  Possible Values: UF_PARAM_type_double
 *
 * 
 */
#define UF_PARAM_WEDM_LEADOUT_ANG   910 


/* UF_PARAM_WEDM_LEADOUT_CUTCOM_DIST
 *
 *  Description: Lead out cutcom distance
 *
 *  Type: UF_PARAM_type_double_length
 *
 *  Name: Lead Out Cutcom Distance
 *  Variable Name: <prefix>_lead_out_cutcom_distance
 *
 *  Possible Values: UF_PARAM_type_double_length
 *
 * 
 */
#define UF_PARAM_WEDM_LEADOUT_CUTCOM_DIST   911 


/* UF_PARAM_WEDM_LEADOUT_RAD
 *
 *  Description: Lead out radius for angular lead out
 *
 *  Type: UF_PARAM_type_double_length
 *
 *  Name: Lead Out Radius
 *  Variable Name: <prefix>_lead_out_radius
 *
 *  Possible Values: UF_PARAM_type_double_length
 *
 * 
 */
#define UF_PARAM_WEDM_LEADOUT_RAD   912 


/* UF_PARAM_WEDM_LEADOUT_CIR_ANG
 *
 *  Description: Lead out angle for circular lead out
 *
 *  Type: UF_PARAM_type_double
 *
 *  Name: Lead Out Circular Angle
 *  Variable Name: <prefix>_lead_out_circular_angle
 *
 *  Possible Values: UF_PARAM_type_double
 *
 * 
 */
#define UF_PARAM_WEDM_LEADOUT_CIR_ANG   913 


/* UF_PARAM_OVERLAP_DIST
 *
 *  Description: Lead in and lead out overlap distance
 *
 *  Type: UF_PARAM_type_double_length
 *
 *  Name: Overlap Distance
 *  Variable Name: <prefix>_overlap_distance
 *
 *  Possible Values: UF_PARAM_type_double_length
 *
 * 
 */
#define UF_PARAM_OVERLAP_DIST   914 


/* UF_PARAM_WEDM_BACKBURN_DIST
 *
 *  Description: Backburn distance for internal trim
 *
 *  Type: UF_PARAM_type_double_length
 *
 *  Name: Backburn Distance
 *  Variable Name: <prefix>_backburn_distance
 *
 *  Possible Values: UF_PARAM_type_double_length
 *
 * 
 */
#define UF_PARAM_WEDM_BACKBURN_DIST   915 


/* UF_PARAM_WEDM_CUTOFF_DIST
 *
 *  Description: Cutoff distance for external trim
 *
 *  Type: UF_PARAM_type_double_length
 *
 *  Name: Cutoff Distance
 *  Variable Name: <prefix>_cutoff_distance
 *
 *  Possible Values: UF_PARAM_type_double_length
 *
 * 
 */
#define UF_PARAM_WEDM_CUTOFF_DIST   916 


/* UF_PARAM_WEDM_STOP_DIST
 *
 *  Description: Distance before complete cut off to output STOP or OPSTOP
 *
 *  Type: UF_PARAM_type_double_length
 *
 *  Name: Stop Distance
 *  Variable Name: <prefix>_stop_distance
 *
 *  Possible Values: UF_PARAM_type_double_length
 *
 * 
 */
#define UF_PARAM_WEDM_STOP_DIST   917 


/* UF_PARAM_LOOP_RAD
 *
 *  Description: Corner control English D loop radius
 *
 *  Type: UF_PARAM_type_double_length
 *
 *  Name: Loop Radius
 *  Variable Name: <prefix>_loop_radius
 *
 *  Possible Values: UF_PARAM_type_double_length
 *
 * 
 */
#define UF_PARAM_LOOP_RAD   919 


/* UF_PARAM_MAX_LOOP_ANG
 *
 *  Description: Maximum angle size of a convex corner that will be cut
 *               Using an English D loop
 *
 *  Type: UF_PARAM_type_double
 *
 *  Name: Max Loop Angle
 *  Variable Name: <prefix>_max_loop_angle
 *
 *  Possible Values: UF_PARAM_type_double
 *
 * 
 */
#define UF_PARAM_MAX_LOOP_ANG   920 


/* UF_PARAM_MIN_LOOP_ANG
 *
 *  Description: Minimum angle size of a convex corner that will be cut
 *               Using an English D loop
 *
 *  Type: UF_PARAM_type_double
 *
 *  Name: Min Loop Angle
 *  Variable Name: <prefix>_min_loop_angle
 *
 *  Possible Values: UF_PARAM_type_double
 *
 * 
 */
#define UF_PARAM_MIN_LOOP_ANG   921 


/* UF_PARAM_WEDM_CUTOFF_STOCK
 *
 *  Description: The stock to be left for a cutoff operation (only applied
 *               when the cutoff is specified as a separate operation)
 *
 *  Type: UF_PARAM_type_double_length
 *
 *  Name: Cutoff Stock
 *  Variable Name: <prefix>_cutoff_stock
 *
 *  Possible Values: UF_PARAM_type_double_length
 *
 * 
 */
#define UF_PARAM_WEDM_CUTOFF_STOCK   922 


/* UF_PARAM_WEDM_NOCORE_STOCK
 *
 *  Description: The stock to be left for a nocore operation
 *
 *  Type: UF_PARAM_type_double_length
 *
 *  Name: Nocore Stock
 *  Variable Name: <prefix>_nocore_stock
 *
 *  Possible Values: UF_PARAM_type_double_length
 *
 * 
 */
#define UF_PARAM_WEDM_NOCORE_STOCK   923 


/* UF_PARAM_ROUGH_PASSES
 *
 *  Description: Number of rough passes
 *
 *  Type: UF_PARAM_type_int
 *
 *  Name: Rough Passes
 *  Variable Name: <prefix>_rough_passes
 *
 *  Possible Values: Larger than 0 UF_PARAM_type_int
 *
 * 
 */
#define UF_PARAM_ROUGH_PASSES   930 


/* UF_PARAM_FINISH_PASSES
 *
 *  Description: Number of finish passes
 *               If it's zero, there are no finish passes.
 *
 *  Type: UF_PARAM_type_int
 *
 *  Name: Finish Passes
 *  Variable Name: <prefix>_finish_passes
 *
 *  Possible Values: Equal or larger than 0 UF_PARAM_type_int
 *
 * 
 */
#define UF_PARAM_FINISH_PASSES   931 


/* UF_PARAM_WEDM_CUT_DIR
 *
 *  Description: Cutting direction
 *
 *  Type: UF_PARAM_type_int
 *
 *  Name: WEDM Cut Direction
 *  Variable Name: <prefix>_wedm_cut_direction
 *
 *  Possible Values:
 *        0 = WE_CUT_ALTERNATE
 *        1 = WE_CUT_CW
 *        2 = WE_CUT_CCW
 *
 * 
 */
#define UF_PARAM_WEDM_CUT_DIR   932 


/* UF_PARAM_WEDM_TRAVERSAL_METHOD
 *
 *  Description: Traversal method if glue tabs are present
 *
 *  Type: UF_PARAM_type_int
 *
 *  Name: WEDM Traversal Method
 *  Variable Name: <prefix>_wedm_traversal_method
 *
 *  Possible Values:
 *        0 = WE_PASS_FIRST
 *        1 = WE_REGION_FIRST
 *
 * 
 */
#define UF_PARAM_WEDM_TRAVERSAL_METHOD   933 


/* UF_PARAM_WEDM_LEADIN_METHOD
 *
 *  Description: Lead in method
 *
 *  Type: UF_PARAM_type_int
 *
 *  Name: Lead In Method
 *  Variable Name: <prefix>_lead_in_method
 *
 *  Possible Values:
 *       0 = WE_LEAD_IN_DIRECT   orthogonal to the boundary
 *       1 = WE_LEAD_IN_ANGLE    linear to the boundary with an angle
 *       2 = WE_LEAD_IN_CIRCULAR consists of an arc and a linear segment
 *
 * 
 */
#define UF_PARAM_WEDM_LEADIN_METHOD   934 


/* UF_PARAM_WEDM_LEADIN_POINT_TOGGLE
 *
 *  Description: This index indicates whether to use user defined
 *               lead in point.
 *
 *  Type: UF_PARAM_type_int
 *
 *  Name: Lead In Point Toggle
 *  Variable Name: <prefix>_lead_in_point_toggle
 *
 *  Possible Values:
 *       0 = No lead in point
 *       1 = Use selected lead in point
 *
 * 
 */
#define UF_PARAM_WEDM_LEADIN_POINT_TOGGLE   935 


/* UF_PARAM_WEDM_LEADOUT_POINT_TOGGLE
 *
 *  Description: This index indicates whether to use user defined
 *               lead out point.
 *
 *  Type: UF_PARAM_type_int
 *
 *  Name: Lead Out Point Toggle
 *  Variable Name: <prefix>_lead_out_point_toggle
 *
 *  Possible Values:
 *       0 = No lead out point
 *       1 = Use selected lead out point
 *
 * 
 */
#define UF_PARAM_WEDM_LEADOUT_POINT_TOGGLE   936 


/* UF_PARAM_WEDM_OVERLAP_TOGGLE
 *
 *  Description: This index indicates whether to apply overlap before
 *               lead out.
 *
 *  Type: UF_PARAM_type_int
 *
 *  Name: Overlap Toggle
 *  Variable Name: <prefix>_overlap_toggle
 *
 *  Possible Values:
 *       0 = No overlap
 *       1 = Apply overlap distance to the tool path
 *
 * 
 */
#define UF_PARAM_WEDM_OVERLAP_TOGGLE   937 


/* UF_PARAM_WEDM_STOP_POINT_TOGGLE
 *
 *  Description: This index indicates whether to output STOP/OPSTOP
 *               before completely cut off.
 *
 *  Type: UF_PARAM_type_int
 *
 *  Name: Stop Point Toggle
 *  Variable Name: <prefix>_stop_point_toggle
 *
 *  Possible Values:
 *       0 = Do not output stop point
 *       1 = Output stop point
 *
 * 
 */
#define UF_PARAM_WEDM_STOP_POINT_TOGGLE   938 


/* UF_PARAM_WEDM_STOP_METHOD
 *
 *  Description: This index indicates to output a STOP command or an
 *               OPSTOP command.
 *
 *  Type: UF_PARAM_type_int
 *
 *  Name: Stop Method
 *  Variable Name: <prefix>_stop_method
 *
 *  Possible Values:
 *       0 = Output STOP
 *       1 = Output OPSTOP
 *
 * 
 */
#define UF_PARAM_WEDM_STOP_METHOD   939 


/* UF_PARAM_WEDM_APPROACH_WITH_WIRE_TOGGLE
 *
 *  Description: This index indicates whether to approach with wire.
 *
 *  Type: UF_PARAM_type_int
 *
 *  Name: Approach With Wire Toggle
 *  Variable Name: <prefix>_approach_with_wire_toggle
 *
 *  Possible Values:
 *       0 = Do not approach with wire
 *       1 = Approach with wire
 *
 * 
 */
#define UF_PARAM_WEDM_APPROACH_WITH_WIRE_TOGGLE   940 


/* UF_PARAM_WEDM_DEPART_WITH_WIRE_TOGGLE
 *
 *  Description: This index indicates whether to depart with wire.
 *
 *  Type: UF_PARAM_type_int
 *
 *  Name: Depart With Wire Toggle
 *  Variable Name: <prefix>_depart_with_wire_toggle
 *
 *  Possible Values:
 *       0 = Do not depart with wire
 *       1 = Depart with wire
 *
 * 
 */
#define UF_PARAM_WEDM_DEPART_WITH_WIRE_TOGGLE   941 


/* UF_PARAM_WEDM_WIRE_POSITION
 *
 *  Description: This index indicates whether the wire position is ON or
 *               TANTO.
 *
 *  Type: UF_PARAM_type_int
 *
 *  Name: Wire Position
 *  Variable Name: <prefix>_wire_position
 *
 *  Possible Values:
 *       0 = ON
 *       1 = TANTO
 *
 * 
 */
#define UF_PARAM_WEDM_WIRE_POSITION   943 


/* UF_PARAM_WEDM_OUTPUT_CUTCOM_OFF_TOGGLE
 *
 *  Description: This index indicates whether to output CUTCOM/OFF.
 *
 *  Type: UF_PARAM_type_int
 *
 *  Name: Output Cutcom Off Toggle
 *  Variable Name: <prefix>_output_cutcom_off_toggle
 *
 *  Possible Values:
 *       0 = Do not output cutcom off
 *       1 = Output cutcom off
 *
 * 
 */
#define UF_PARAM_WEDM_OUTPUT_CUTCOM_OFF_TOGGLE   944 


/* UF_PARAM_WEDM_FEED_OUTPUT_METHOD
 *
 *  Description: This index indicates the feed rate output control method.
 *
 *  Type: UF_PARAM_type_int
 *
 *  Name: Feed Output Method
 *  Variable Name: <prefix>_feed_output_method
 *
 *  Possible Values:
 *       0 = Do not output
 *       1 = Output non cutting feedrates
 *       2 = Output all feedrates
 *
 * 
 */
#define UF_PARAM_WEDM_FEED_OUTPUT_METHOD   945 


/* UF_PARAM_WEDM_FEED_OUTPUT_UNIT_TOGGLE
 *
 *  Description: This index indicates whether to output feedrate unit.
 *
 *  Type: UF_PARAM_type_int
 *
 *  Name: Feed Output Unit Toggle
 *  Variable Name: <prefix>_feed_output_unit_toggle
 *
 *  Possible Values:
 *       0 = Do not output feedrate unit
 *       1 = Output feedrate unit
 *
 * 
 */
#define UF_PARAM_WEDM_FEED_OUTPUT_UNIT_TOGGLE   946 


/* UF_PARAM_WEDM_LEADOUT_SAME_AS_LEADIN_TOGGLE
 *
 *  Description: This index indicates whether to apply all lead in parameters
 *               as lead out parameters.
 *
 *  Type: UF_PARAM_type_int
 *
 *  Name: Lead Out Same As Lead In Toggle
 *  Variable Name: <prefix>_lead_out_same_as_lead_in_toggle
 *
 *  Possible Values:
 *       0 = Do not use lead in parameters as lead out parameters
 *       1 = Use all lead in parameters as lead out parameters
 *
 * 
 */
#define UF_PARAM_WEDM_LEADOUT_SAME_AS_LEADIN_TOGGLE   947 


/* UF_PARAM_WEDM_LEADOUT_METHOD
 *
 *  Description: Lead out method
 *
 *  Type: UF_PARAM_type_int
 *
 *  Name: Lead Out Method
 *  Variable Name: <prefix>_lead_out_method
 *
 *  Possible Values:
 *       0 = WE_LEAD_OUT_DIRECT   orthogonal to the boundary
 *       1 = WE_LEAD_OUT_ANGLE    linear to the boundary with an angle
 *       2 = WE_LEAD_OUT_CIRCULAR consists of an arc and a linear segment
 *
 * 
 */
#define UF_PARAM_WEDM_LEADOUT_METHOD   948 


/* UF_PARAM_WEDM_CUTCOM_REGISTER_POSITION
 *
 *  Description: This index indicates the position to output CUTCOM register
 *               number.
 *
 *  Type: UF_PARAM_type_int
 *
 *  Name: Cutcom Register Position
 *  Variable Name: <prefix>_cutcom_register_position
 *
 *  Possible Values:
 *        0 = Before cutcom/leadin move
 *        1 = After cutcom/leadin move
 *
 * 
 */
#define UF_PARAM_WEDM_CUTCOM_REGISTER_POSITION   949 


/* UF_PARAM_WEDM_CUTCOM_OFF_POSITION
 *
 *  Description: This index indicates the position to output CUTCOM/OFF.
 *
 *  Type: UF_PARAM_type_int
 *
 *  Name: Cutcom Off Position
 *  Variable Name: <prefix>_cutcom_off_position
 *
 *  Possible Values:
 *        0 = Before cutcom/leadout move
 *        1 = After cutcom/leadout move
 *
 * 
 */
#define UF_PARAM_WEDM_CUTCOM_OFF_POSITION   950 


/* UF_PARAM_WEDM_LEADIN_POINT
 *
 *  Description: User defined lead in point
 *
 *  Type: UF_PARAM_type_tag
 *
 *  Name: WEDM Lead In Point
 *  Variable Name: <prefix>_wedm_lead_in_point
 *
 *  Possible Values: UF_PARAM_type_tag
 *
 * 
 */
#define UF_PARAM_WEDM_LEADIN_POINT   952 


/* UF_PARAM_WEDM_LEADOUT_POINT
 *
 *  Description: User defined lead out point
 *
 *  Type: UF_PARAM_type_tag
 *
 *  Name: WEDM Lead Out Point
 *  Variable Name: <prefix>_wedm_lead_out_point
 *
 *  Possible Values: UF_PARAM_type_tag
 *
 * 
 */
#define UF_PARAM_WEDM_LEADOUT_POINT   953 


/* UF_PARAM_WEDM_THREAD_TOOL_AXIS
 *
 *  Description: Wire axis at thread point
 *
 *  Type: UF_PARAM_type_tag
 *
 *  Name: WEDM Thread Tool Axis
 *  Variable Name: <prefix>_wedm_thread_tool_axis
 *
 *  Possible Values: UF_PARAM_type_tag
 *
 * 
 */
#define UF_PARAM_WEDM_THREAD_TOOL_AXIS   958 


/* UF_PARAM_WEDM_RETRACT_TOOL_AXIS
 *
 *  Description: Wire axis at retract point
 *
 *  Type: UF_PARAM_type_tag
 *
 *  Name: WEDM Retract Tool Axis
 *  Variable Name: <prefix>_wedm_retract_tool_axis
 *
 *  Possible Values: UF_PARAM_type_tag
 *
 * 
 */
#define UF_PARAM_WEDM_RETRACT_TOOL_AXIS   959 


/* UF_PARAM_WEDM_MULTIPLE_CUTOFF_OR_BACKBURN_PASSES_TOGGLE
 *
 *  Description: This index indicates whether to apply multiple passes
 *               on cutoff, backburn, and tab area.
 *
 *  Type: UF_PARAM_type_int
 *
 *  Name: WEDM Multiple Cutoff Or Backburn Passes Toggle
 *  Variable Name: <prefix>_wedm_multiple_cutoff_or_backburn_passes_toggle
 *
 *  Possible Values:
 *        1 = Cut cutoff/backburn with multiple passes
 *        0 = Cut cutoff/backburn with single pass
 *
 * 
 */
#define UF_PARAM_WEDM_MULTIPLE_CUTOFF_OR_BACKBURN_PASSES_TOGGLE   964 


/* UF_PARAM_WEDM_NON_TILT_LEADIN_TOGGLE
 *
 *  Description: This index indicates whether to apply non-tile lead in.
 *
 *  Type: UF_PARAM_type_int
 *
 *  Name: Non Tilt Lead In Toggle
 *  Variable Name: <prefix>_non_tilt_lead_in_toggle
 *
 *  Possible Values:
 *        0 = Do not apply non tilt lead in
 *        1 = Apply non tilt lead in
 *
 * 
 */
#define UF_PARAM_WEDM_NON_TILT_LEADIN_TOGGLE   965 


/* UF_PARAM_WEDM_MULTIPLE_CUTOFF_OR_BACKBURN_PASSES_METHOD
 *
 *  Description: This index indicates how to cut cutoff or backburn area
 *               with multiple passes
 *
 *  Type: UF_PARAM_type_int
 *
 *  Name: WEDM Multiple Cutoff Or Backburn Passes Method
 *  Variable Name: <prefix>_wedm_multiple_cutoff_or_backburn_passes_method
 *
 *  Possible Values:
 *        1 = Cutoff First
 *        0 = Region First
 *
 * 
 */
#define UF_PARAM_WEDM_MULTIPLE_CUTOFF_OR_BACKBURN_PASSES_METHOD   966 


/* UF_PARAM_WEDM_SMOOTH_LEAD_IN_TOGGLE
 *
 *  Description: This index indicates whether to output a smooth lead in register
 *               at a distance after lead in
 *
 *  Type: UF_PARAM_type_int
 *
 *  Name: Smooth Lead In Toggle
 *  Variable Name: <prefix>_smooth_lead_in_toggle
 *
 *  Possible Values:
 *       0 = Do not output smooth lead in register
 *       1 = Output smooth lead in register
 *
 * 
 */
#define UF_PARAM_WEDM_SMOOTH_LEAD_IN_TOGGLE   970 


/* UF_PARAM_WEDM_SMOOTH_LEAD_OUT_TOGGLE
 *
 *  Description: This index indicates whether to output a smooth lead out register
 *               at a distance before lead out
 *
 *  Type: UF_PARAM_type_int
 *
 *  Name: Smooth Lead Out Toggle
 *  Variable Name: <prefix>_smooth_lead_out_toggle
 *
 *  Possible Values:
 *       0 = Do not output smooth lead out register
 *       1 = Output smooth lead out register
 *
 * 
 */
#define UF_PARAM_WEDM_SMOOTH_LEAD_OUT_TOGGLE   971 


/* UF_PARAM_WEDM_SMOOTH_LEAD_IN_DIST
 *
 *  Description: Distance after lead in to output smooth lead in register
 *
 *  Type: UF_PARAM_type_double_length
 *
 *  Name: Smooth Lead In Distance
 *  Variable Name: <prefix>_smooth_lead_in_distance
 *
 *  Possible Values: UF_PARAM_type_double_length
 *
 * 
 */
#define UF_PARAM_WEDM_SMOOTH_LEAD_IN_DIST   972 


/* UF_PARAM_WEDM_SMOOTH_LEAD_OUT_DIST
 *
 *  Description: Distance before lead out to output smooth lead out register
 *
 *  Type: UF_PARAM_type_double_length
 *
 *  Name: Smooth Lead Out Distance
 *  Variable Name: <prefix>_smooth_lead_out_distance
 *
 *  Possible Values: UF_PARAM_type_double_length
 *
 * 
 */
#define UF_PARAM_WEDM_SMOOTH_LEAD_OUT_DIST   973 


/* UF_PARAM_WEDM_LEADIN_CUTCOM_ANG
 *
 *  Description: Angle for Cutcom move before lead in.
 *
 *  Type: UF_PARAM_type_double_length
 *
 *  Name: Lead In Cutcomp Angle
 *  Variable Name: <prefix>_lead_in_cutcomp_angle
 *
 *  Possible Values: UF_PARAM_type_double_length
 *
 * 
 */
#define UF_PARAM_WEDM_LEADIN_CUTCOM_ANG   974 


/* UF_PARAM_WEDM_LEADOUT_CUTCOM_ANG
 *
 *  Description: Angle for Cutcom move after lead out.
 *
 *  Type: UF_PARAM_type_double_length
 *
 *  Name: Lead Out Cutcomp Angle
 *  Variable Name: <prefix>_lead_out_cutcomp_angle
 *
 *  Possible Values: UF_PARAM_type_double_length
 *
 * 
 */
#define UF_PARAM_WEDM_LEADOUT_CUTCOM_ANG   975 


/* UF_PARAM_TL_DIAMETER
 *
 *  Description:
 *  This index specifies the diameter of the tool.
 *
 *  Type: UF_PARAM_type_length
 *
 *  Name: Tool Diameter
 *  Variable Name: <prefix>_tool_diameter
 *
 *  Possible Values:
 *    Valid for cutter types
 *         UF_CUTTER_TYPE_MILL
 *         UF_CUTTER_TYPE_DRILL
 *         UF_CUTTER_TYPE_BARREL
 *         UF_CUTTER_TYPE_T
 *
 *
 * 
 */
#define UF_PARAM_TL_DIAMETER   1000 


/* UF_PARAM_TL_HEIGHT
 *
 *  Description:
 *  This index specifies the actual height of the tool.
 *
 *  Type: UF_PARAM_type_length
 *
 *  Name: Tool Length
 *  Variable Name: <prefix>_tool_length
 *
 *  Possible Values:
 *    Valid for cutter types
 *         UF_CUTTER_TYPE_MILL
 *         UF_CUTTER_TYPE_DRILL
 *         UF_CUTTER_TYPE_BARREL
 *         UF_CUTTER_TYPE_T
 *
 * 
 */
#define UF_PARAM_TL_HEIGHT   1001 


/* UF_PARAM_TL_FLUTE_LN
 *
 *  Description:
 *  This index specifies the measured distance between the beginning and end
 *  teeth of the flute. The flute length does not necessarily indicate the
 *  length of cut.
 *
 *  Type: UF_PARAM_type_length
 *
 *  Name: Tool Flute Length
 *  Variable Name: <prefix>_tool_flute_length
 *
 *  Possible Values:
 *    Valid for cutter types
 *         UF_CUTTER_TYPE_MILL
 *         UF_CUTTER_TYPE_DRILL
 *         UF_CUTTER_TYPE_BARREL
 *         UF_CUTTER_TYPE_T
 *
 * 
 */
#define UF_PARAM_TL_FLUTE_LN   1002 


/* UF_PARAM_TL_TAPER_ANG
 *
 *  Description:
 *  This index specifies the angle of the sides of a tapered
 *  tool. The angle is measured from the tool axis. If the Taper Angle is
 *  positive, the tool is wider at the top than it is at the bottom.
 *  If the Taper Angle is negative, the tool is wider at the bottom than it
 *  is at the top. If the Taper Angle is zero, the sides of the tool are
 *  parallel to the tool axis.
 *
 *  Type: UF_PARAM_type_double
 *
 *  Name: Tool Taper Angle
 *  Variable Name: <prefix>_tool_taper_angle
 *
 *  Possible Values: Angle is measured in radians
 *    Valid for cutter types
 *         UF_CUTTER_TYPE_MILL
 *
 * 
 */
#define UF_PARAM_TL_TAPER_ANG   1003 


/* UF_PARAM_TL_TIP_ANG
 *
 *  Description:
 *  This index specifies the angle of the tip of the tool. This is a
 *  non-negative angle measured from a line through the tool end point and
 *  perpendicular to the tool axis. If the Tip Angle is positive, the tool
 *  has a sharp point at the very bottom (like the vertex of a cone).
 *  For turning, the tip angle defines how the tip of a grooving tool is
 *  oriented. It is an angle measured perpendicular from the tool orientation
 *  axis and a line through the insert's tip edge. The tip angle may be 
 *  positive, negative or zero for standard grooving inserts.
 *
 *  Type: UF_PARAM_type_double
 *
 *  Name: Tool Tip Angle
 *  Variable Name: <prefix>_tool_tip_angle
 *
 *  Possible Values: Angle is measured in radians
 *    Valid for cutter types
 *         UF_CUTTER_TYPE_MILL
 *         UF_CUTTER_TYPE_GROOVE
 *
 * 
 */
#define UF_PARAM_TL_TIP_ANG   1004 


/* UF_PARAM_TL_COR1_RAD
 *
 *  Description:
 *  This index specifies the radius of the lower corner arc of the tool. The
 *  lower radius of a tool.
 *
 *  Type: UF_PARAM_type_length
 *
 *  Name: Tool Corner1 Radius
 *  Variable Name: <prefix>_tool_corner1_radius
 *
 *  Possible Values:
 *    Valid for cutter types
 *         UF_CUTTER_TYPE_MILL
 *         UF_CUTTER_TYPE_DRILL
 *
 * 
 */
#define UF_PARAM_TL_COR1_RAD   1005 


/* UF_PARAM_TL_XCEN_COR1
 *
 *  Description:
 *  This index is a part of the definition of the center of the arc
 *  representing the lower radius of the tool profile. It is the horizontal
 *  distance between the center of the lower corner arc and the tool axis;
 *  it can be positive (lower arc and its center on the same side of the tool
 *  axis) or negative (lower arc and its center on opposite sides of the tool
 *  axis) or zero.
 *
 *
 *  Type: UF_PARAM_type_length
 *
 *  Name: Tool Corner1 Center X
 *  Variable Name: <prefix>_tool_corner1_center_x
 *
 *  Possible Values:
 *    Valid for cutter subtype
 *             UF_CUTTER_SUBTYPE_MILL_7
 *             UF_CUTTER_SUBTYPE_MILL_10
 *
 * 
 */
#define UF_PARAM_TL_XCEN_COR1   1006 


/* UF_PARAM_TL_YCEN_COR1
 *
 *  Description:
 *  This index is a part of the definition of the center of the arc
 *  representing the lower radius of the tool profile. It is the vertical
 *  distance between the center of the lower corner arc and the tool end.
 *  Its value must be non-negative.
 *
 *  Type: UF_PARAM_type_length
 *
 *  Name: Tool Corner1 Center Y
 *  Variable Name: <prefix>_tool_corner1_center_y
 *
 *  Possible Values:
 *    Valid for cutter subtype
 *             UF_CUTTER_SUBTYPE_MILL_7
 *             UF_CUTTER_SUBTYPE_MILL_10
 *
 * 
 */
#define UF_PARAM_TL_YCEN_COR1   1007 


/* UF_PARAM_TL_COR2_RAD
 *
 *  Description:
 *  This index specifies the upper corner radius of the tool.
 *  The value must be positive.
 *
 *  Type: UF_PARAM_type_length
 *
 *  Name: Tool Corner2 Radius
 *  Variable Name: <prefix>_tool_corner2_radius
 *
 *  Possible Values:
 *    Valid for cutter subtype
 *             UF_CUTTER_SUBTYPE_MILL_10
 *
 * 
 */
#define UF_PARAM_TL_COR2_RAD   1008 


/* UF_PARAM_TL_XCEN_COR2
 *
 *  Description:
 *  This index is a part of the definition of the center of the arc
 *  representing the upper radius of the tool profile. It is the horizontal
 *  distance between the center of the upper corner arc and the tool axis.
 *  It can be positive (upper arc and its center on the same side of the tool
 *  axis) or negative (upper arc and its center on opposite sides of the tool
 *  axis) or zero.
 *
 *  Type: UF_PARAM_type_length
 *
 *  Name: Tool Corner2 Center X
 *  Variable Name: <prefix>_tool_corner2_center_x
 *
 *  Possible Values:
 *    Valid for cutter subtype
 *             UF_CUTTER_SUBTYPE_MILL_10
 *
 * 
 */
#define UF_PARAM_TL_XCEN_COR2   1009 


/* UF_PARAM_TL_YCEN_COR2
 *
 *  Description:
 *  This index is a part of the definition of the center of the arc
 *  representing the upper radius of the tool profile. It is the vertical
 *  distance between the center of the upper corner arc and the tool end.
 *  Its value must be non-negative.
 *
 *  Type: UF_PARAM_type_length
 *
 *  Name: Tool Corner2 Center Y
 *  Variable Name: <prefix>_tool_corner2_center_y
 *
 *  Possible Values:
 *    Valid for cutter subtype
 *             UF_CUTTER_SUBTYPE_MILL_10
 *
 * 
 */
#define UF_PARAM_TL_YCEN_COR2   1010 


/* UF_PARAM_TL_BARREL_RAD
 *
 *  Description:
 *  This index specifies the radius of the arc defining the profile shape of
 *  the sides of the cutter.
 *
 *  Type: UF_PARAM_type_length
 *
 *  Name: Tool Barrel Radius
 *  Variable Name: <prefix>_tool_barrel_radius
 *
 *  Possible Values:
 *    Valid for cutter type
 *             UF_CUTTER_TYPE_BARREL
 *
 * 
 */
#define UF_PARAM_TL_BARREL_RAD   1011 


/* UF_PARAM_TL_SHANK_DIA
 *
 *  Description:
 *  This index specifies the diameter of the shank at the top of the Barrel
 *  Cutter.
 *
 *  Type: UF_PARAM_type_length
 *
 *  Name: Tool Shank Diameter
 *  Variable Name: <prefix>_tool_shank_diameter
 *
 *  Possible Values:
 *    Valid for cutter type
 *             UF_CUTTER_TYPE_BARREL
 *             UF_CUTTER_TYPE_T
 *
 * 
 */
#define UF_PARAM_TL_SHANK_DIA   1012 


/* UF_PARAM_TL_LOW_COR_RAD
 *
 *  Description:
 *  This index specifies the lower corner radius of the profile of the tool.
 *
 *  Type: UF_PARAM_type_length
 *
 *  Name: Tool Lower Corner Radius
 *  Variable Name: <prefix>_tool_lower_corner_radius
 *
 *  Possible Values:
 *    Valid for cutter type
 *             UF_CUTTER_TYPE_BARREL
 *             UF_CUTTER_TYPE_T
 *
 * 
 */
#define UF_PARAM_TL_LOW_COR_RAD   1013 


/* UF_PARAM_TL_UP_COR_RAD
 *
 *  Description:
 *  This index specifies the upper corner radius of the profile of the tool.
 *
 *  Type: UF_PARAM_type_length
 *
 *  Name: Tool Upper Corner Radius
 *  Variable Name: <prefix>_tool_upper_corner_radius
 *
 *  Possible Values:
 *    Valid for cutter type
 *             UF_CUTTER_TYPE_BARREL
 *             UF_CUTTER_TYPE_T
 *
 * 
 */
#define UF_PARAM_TL_UP_COR_RAD   1014 


/* UF_PARAM_TL_YCEN_BARREL
 *
 *  Description:
 *  This index specifies the height of the center of the arc defining the
 *  profile of the outside edge of the cutter.
 *
 *  Type: UF_PARAM_type_length
 *
 *  Name: Tool Barrel Center Y
 *  Variable Name: <prefix>_tool_barrel_center_y
 *
 *  Possible Values:
 *    Valid for cutter type
 *             UF_CUTTER_TYPE_BARREL
 *
 * 
 */
#define UF_PARAM_TL_YCEN_BARREL   1015 


/* UF_PARAM_TL_POINT_ANG
 *
 *  Description:
 *  This index specifies the angle of the point of the tool.
 *
 *  Type: UF_PARAM_type_double
 *
 *  Name: Tool Point Angle
 *  Variable Name: <prefix>_tool_point_angle
 *
 *  Possible Values: Angle is measured in radians
 *    Valid for cutter type
 *             UF_CUTTER_TYPE_DRILL
 *
 * 
 */
#define UF_PARAM_TL_POINT_ANG   1016 


/* UF_PARAM_TL_NUM_FLUTES
 *
 *  Description:
 *  This index specifies the number of flutes in the tool.
 *
 *  Type: UF_PARAM_type_int
 *
 *  Name: Tool Flutes Number
 *  Variable Name: <prefix>_tool_flutes_number
 *
 *  Possible Values:
 *    Valid for cutter type
 *             UF_CUTTER_TYPE_MILL
 *             UF_CUTTER_TYPE_DRILL
 *             UF_CUTTER_TYPE_BARREL
 *             UF_CUTTER_TYPE_T
 *
 * 
 */
#define UF_PARAM_TL_NUM_FLUTES   1017  /*   */


/* UF_PARAM_TL_RELIEF_ANG
 *
 *   Description:
 *      This index specifies the angle caused by the slope of the
 *      cutter away from the cutting edge of the turning tool
 *      insert (degrees).
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Tool Relief Angle
 *  Variable Name: <prefix>_tool_relief_angle
 *
 *   Possible Values: UF_PARAM_type_double
 *
 * 
 */
#define UF_PARAM_TL_RELIEF_ANG   1019 


/* UF_PARAM_TL_HOLDER_WIDTH
 *
 *   Description:
 *      This index specifies the width of the button tool holder.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Tool Holder Width
 *  Variable Name: <prefix>_tool_holder_width
 *
 *   Possible Values: UF_PARAM_type_double_length
 *
 * 
 */
#define UF_PARAM_TL_HOLDER_WIDTH   1021 


/* UF_PARAM_TL_INSERT_WIDTH
 *
 *   Description:
 *      This index describes the insert width. This is the width
 *      of a grooving tool that would result from a straight cut
 *      (radial cut for OD grooving tool) into material. This
 *      parameter appears with the Standard, Ring Type Joint and
 *      User Defined Tools.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Tool Insert Width
 *  Variable Name: <prefix>_tool_insert_width
 *
 *   Possible Values: UF_PARAM_type_double_length
 *
 * 
 */
#define UF_PARAM_TL_INSERT_WIDTH   1022 


/* UF_PARAM_TL_NOSE_WIDTH
 *
 *   Description:
 *      This index describes the nose width of a turning tool.
 *      It represents the width of the tool cutting surface of
 *      either a Ring Type Joint grooving tool or a Trapezoidal
 *      threading tool.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Tool Nose Width
 *  Variable Name: <prefix>_tool_nose_width
 *
 *   Possible Values: UF_PARAM_type_double_length
 *
 * 
 */
#define UF_PARAM_TL_NOSE_WIDTH   1023 


/* UF_PARAM_TL_ORIENTATION
 *
 *   Description:
 *      This index specifies the angle between the cutting edge
 *      and the cutting surface of the turning tool insert (radians).
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Tool Orientation
 *  Variable Name: <prefix>_tool_orientation
 *
 *   Possible Values: UF_PARAM_type_double
 *
 * 
 */
#define UF_PARAM_TL_ORIENTATION   1025 


/* UF_PARAM_TL_INSERT_ANG
 *
 *   Description:
 *      This index specifies the polar angle of the first edge
 *      of a Form turning tool (radians).
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Tool Insert Angle
 *  Variable Name: <prefix>_tool_insert_angle
 *
 *   Possible Values: UF_PARAM_type_double
 *
 * 
 */
#define UF_PARAM_TL_INSERT_ANG   1029 


/* UF_PARAM_TL_LEFT_COR_RAD
 *
 *   Description:
 *      This index defines the left corner radius of grooving
 *      asymmetrical tools.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Tool Left Corner Radius
 *  Variable Name: <prefix>_tool_left_corner_radius
 *
 *   Possible Values: UF_PARAM_type_double_length
 *
 * 
 */
#define UF_PARAM_TL_LEFT_COR_RAD   1030 


/* UF_PARAM_TL_RIGHT_COR_RAD
 *
 *   Description:
 *      This index defines the left corner radius of grooving
 *      asymmetrical tools.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Right Corner Radius
 *  Variable Name: <prefix>_right_corner_radius
 *
 *   Possible Values: UF_PARAM_type_double_length
 *
 * 
 */
#define UF_PARAM_TL_RIGHT_COR_RAD   1031 


/* UF_PARAM_TL_MAX_DEPTH
 *
 *   Description:
 *      This index describes the maximum depth of cut which the
 *      tool insert can achieve. This is dependant upon the
 *      geometry of the insert.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Tool Max Depth
 *  Variable Name: <prefix>_tool_max_depth
 *
 *   Possible Values: UF_PARAM_type_double_length
 *
 * 
 */
#define UF_PARAM_TL_MAX_DEPTH   1032 


/* UF_PARAM_TL_TIP_OFFSET
 *
 *   Description:
 *      This index describes the tip offset of a threading tool.
 *      For standard insert type it is the offset of the tool
 *      nose's bottom point to the tool's left flank.
 *      For trapezoidal insert type it is the offset of the right
 *      end of the tool's bottom edge to the left flank.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Tool Tip Offset
 *  Variable Name: <prefix>_tool_tip_offset
 *
 *   Possible Values: UF_PARAM_type_double_length
 *
 * 
 */
#define UF_PARAM_TL_TIP_OFFSET   1033 


/* UF_PARAM_TL_Z_OFFSET
 *
 *  Description:
 *  This index specifies the correction to the positioning of the tool due to
 *  variations in tool length
 *
 *  Type: UF_PARAM_type_length
 *
 *  Name: Tool Z-Offset
 *  Variable Name: <prefix>_tool_z_offset
 *
 *  Possible Values:
 *    Valid for cutter type
 *             UF_CUTTER_TYPE_MILL
 *             UF_CUTTER_TYPE_DRILL
 *             UF_CUTTER_TYPE_BARREL
 *             UF_CUTTER_TYPE_T
 *
 * 
 */
#define UF_PARAM_TL_Z_OFFSET   1034  /*   */


/* UF_PARAM_TL_X_OFFSET
 *
 *   Description:
 *      This index specifies the x offset, which is the x coordinate
 *      of the distance between the tool's reference point and its
 *      tracking point. Parameter UF_PARAM_TL_X_OFFSET_TOG has
 *      to be turned on in order to activate this index.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Tool X-Offset
 *  Variable Name: <prefix>_tool_x_offset
 *
 *   Possible Values: UF_PARAM_type_double_length
 *
 * 
 */
#define UF_PARAM_TL_X_OFFSET   1035 


/* UF_PARAM_TL_Y_OFFSET
 *
 *   Description:
 *      This index specifies the y offset, which is the y coordinate
 *      of the distance between the tool's reference point and it's
 *      tracking point. Parameter UF_PARAM_TL_Y_OFFSET_TOG has
 *      to be turned on in order to activate this index.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Tool Y-Offset
 *  Variable Name: <prefix>_tool_y_offset
 *
 *   Possible Values: UF_PARAM_type_double_length
 *
 * 
 */
#define UF_PARAM_TL_Y_OFFSET   1036 


/* UF_PARAM_TL_NOSE_RAD
 *
 *   Description:
 *      This index specifies the radius of the inscribed circle
 *      at the cutter tip of the turning tool insert.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Tool Nose Radius
 *  Variable Name: <prefix>_tool_nose_radius
 *
 *   Possible Values: UF_PARAM_type_double_length
 *
 * 
 */
#define UF_PARAM_TL_NOSE_RAD   1037 


/* UF_PARAM_TL_NUMBER
 *
 *  Description: This index specifies the tool number. It has to be a
 *               non-negative number not exceeding 2147483647.
 *
 *  Type: UF_PARAM_type_int
 *
 *  Name: Tool Number
 *  Variable Name: <prefix>_tool_number
 *
 *  Possible Values:
 *    Valid for cutter type
 *             UF_CUTTER_TYPE_MILL
 *             UF_CUTTER_TYPE_DRILL
 *             UF_CUTTER_TYPE_BARREL
 *             UF_CUTTER_TYPE_T
 *
 * 
 */
#define UF_PARAM_TL_NUMBER   1038  /* UF_PARAM_type_int */


/* UF_PARAM_TL_ADJ_REG
 *
 *  Description:
 *  This index specifies the register number value on the controller which
 *  contain the tool offset coordinates.
 *
 *  Type: UF_PARAM_type_int
 *
 *  Name: Tool Length Adjust Register
 *  Variable Name: <prefix>_tool_length_adjust_register
 *
 *  Possible Values:
 *    Valid for cutter type
 *             UF_CUTTER_TYPE_MILL
 *             UF_CUTTER_TYPE_DRILL
 *             UF_CUTTER_TYPE_BARREL
 *             UF_CUTTER_TYPE_T
 *
 * 
 */
#define UF_PARAM_TL_ADJ_REG   1040  /* UF_PARAM_type_int */


/* UF_PARAM_TL_CUTCOM_REG
 *
 *  Description:
 *  This index specifies the register number value on the controller which
 *  contains the value that the system uses to adjust the tool path to allow
 *  for variation due to an undersized or oversized cutter or tool.
 *  (Parameter is used if the parameter,
 *      UF_PARAM_CUTCOM_REGISTER_STATUS is 1 in the operation only.)
 *
 *  Type: UF_PARAM_type_int
 *
 *  Name: Tool Cutcom Register
 *  Variable Name: <prefix>_tool_cutcom_register
 *
 *  Possible Values:
 *    Valid for cutter type
 *             UF_CUTTER_TYPE_MILL
 *             UF_CUTTER_TYPE_DRILL
 *             UF_CUTTER_TYPE_BARREL
 *             UF_CUTTER_TYPE_T
 *
 * 
 */
#define UF_PARAM_TL_CUTCOM_REG   1041  /* UF_PARAM_type_int */


/* UF_PARAM_TL_DIRECTION
 *
 *  Description:
 *  This index specifies the direction of rotation of the spindle.
 *
 *  Type: UF_PARAM_type_int
 *
 *  Name: Tool Direction
 *  Variable Name: <prefix>_tool_direction
 *
 *  Possible Values:
 *    Valid for cutter type
 *             UF_CUTTER_TYPE_MILL
 *             UF_CUTTER_TYPE_DRILL
 *             UF_CUTTER_TYPE_BARREL
 *             UF_CUTTER_TYPE_T
 *
 * 
 */
#define UF_PARAM_TL_DIRECTION   1042  /* UF_PARAM_type_int */


/* UF_PARAM_TL_CTLG_NUM
 *
 *  Description:
 *  This index specifies the catalog number or a tool tracking number.
 *
 *  Type: UF_PARAM_type_string
 *
 *  Name: Tool Catalog Number
 *  Variable Name: <prefix>_tool_catalog_number
 *
 *  Possible Values:
 *    Valid for cutter type
 *             UF_CUTTER_TYPE_MILL
 *             UF_CUTTER_TYPE_DRILL
 *             UF_CUTTER_TYPE_BARREL
 *             UF_CUTTER_TYPE_T
 *
 * 
 */
#define UF_PARAM_TL_CTLG_NUM   1043  /* UF_PARAM_type_string */


/* UF_PARAM_TL_INSERT_POSITION
 *
 *   Description:
 *      This index specifies the spindle direction for machining.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Tool Insert Position
 *  Variable Name: <prefix>_tool_insert_position
 *
 *   Possible Values: 
 *    1   Topside, spindle turns clockwise.
 *    2   Underside, spindle turns counterclockwise.
 *
 * 
 */
#define UF_PARAM_TL_INSERT_POSITION   1045 


/* UF_PARAM_TL_HOLDER_OFFSET
 *
 *   Description:
 *      This index specifies the tool offset in the holder.
 *
 *   Type: UF_PARAM_type_length
 *
 *   Name: Tool Offset
 *  Variable Name: <prefix>_tool_offset
 *
 *   Possible Values:
 *
 * 
 */
#define UF_PARAM_TL_HOLDER_OFFSET   1049  /* UF_PARAM_type_length */


typedef enum UF_PARAM_tap_holder_type_e
{
    UF_PARAM_tap_holder_type_rigid = 0,
    UF_PARAM_tap_holder_type_floating = 1
} UF_PARAM_tap_holder_type_t;

/* UF_PARAM_TL_TAP_HOLDER_TYPE
 *
 *   Description:
 *      This index defines the type of holder for a tap tool
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Tool Holder Type
 *  Variable Name: <prefix>_tool_holder_type
 *
 *   Possible Values: UF_PARAM_tap_holder_type_t
 *
 *    Valid for cutter type
 *             UF_CUTTER_TYPE_DRILL
 *                UF_CUTTER_SUBTYPE_TAP
 *
 * 
 */
#define UF_PARAM_TL_TAP_HOLDER_TYPE   1051 


/* UF_PARAM_TL_RIGIDITY
 *
 *   Description:
 *      This index specifies the tool rigidity factor.
 *
 *   Type: UF_PARAM_type_length
 *
 *   Name: Tool Rigidity
 *  Variable Name: <prefix>_tool_rigidity
 *
 *   Possible Values:
 *
 * 
 */
#define UF_PARAM_TL_RIGIDITY   1052  /* UF_PARAM_type_length */


/* UF_PARAM_CUTTER_TRACKING_POINTS
 *
 *   Description:
 *      This index defines the list of tracking points
 *      associated with a cutter or operation.
 *
 *   Type: UF_PARAM_type_vla_tag
 *
 *   Name: Cutter Tracking Points
 *  Variable Name: <prefix>_cutter_tracking_points
 *
 *   Possible Values: 
 *
 * 
 */
#define UF_PARAM_CUTTER_TRACKING_POINTS   1060 


/* UF_PARAM_TRACKING_POINT
 *
 *   Description:
 *      This index specifies the tracking point(s)
 *      selected for use in an operation
 *
 *   Type: UF_PARAM_type_vla_tag
 *
 *   Name: Active Tracking Points
 *  Variable Name: <prefix>_active_tracking_points
 *
 *   Possible Values: 
 *
 * 
 */
#define UF_PARAM_TRACKING_POINT   1061 


/* UF_PARAM_HOLDER_SECTION
 *
 *   Description:
 *      This index specifies the cylindrical sections
 *      defined as a holder for the parent cutter
 *
 *   Type: UF_PARAM_type_vla_tag
 *
 *   Name: Cutter Holder Sections
 *  Variable Name: <prefix>_cutter_holder_sections
 *
 *   Possible Values: 
 *
 * 
 */
#define UF_PARAM_HOLDER_SECTION   1062 


/* UF_PARAM_TL_HOLDER_LIBREF
 *
 *   Description:
 *      This index specifies the current libref of a
 *      library tool holder.  This may differ from the
 *      original libref if the user wishes to rename a
 *      library holder or create a copy of it.
 *
 *   Type: UF_PARAM_type_string
 *
 *   Name: Cutter Holder Libref
 *  Variable Name: <prefix>_cutter_holder_libref
 *
 *   Possible Values: 
 *
 * 
 */
#define UF_PARAM_TL_HOLDER_LIBREF   1063 


/* UF_PARAM_TL_HOLDER_DESCRIPTION
 *
 *   Description:
 *      This index specifies the description 
 *      attribute of a library tool holder
 *
 *   Type: UF_PARAM_type_string
 *
 *   Name: Cutter Holder Description
 *  Variable Name: <prefix>_cutter_holder_description
 *
 *   Possible Values: 
 *
 * 
 */
#define UF_PARAM_TL_HOLDER_DESCRIPTION   1064 


/* UF_PARAM_TL_HOLDER_MAX_OFFSET
 *
 *   Description:
 *      This index specifies the maximum tool offset in the holder.
 *
 *   Type: UF_PARAM_type_length
 *
 *   Name: Tool Max Offset
 *  Variable Name: <prefix>_tool_max_offset
 *
 *   Possible Values:
 *
 * 
 */
#define UF_PARAM_TL_HOLDER_MAX_OFFSET   1065  /* UF_PARAM_type_length */


/* UF_PARAM_DRIVE_POINT
 *
 *   Description:
 *      This index specifies the drive point(s)
 *      selected for use in an operation
 *
 *   Type: UF_PARAM_type_vla_tag
 *
 *   Name: Active drive Points
 *  Variable Name: <prefix>_active_drive_points
 *
 *   Possible Values:
 *
 * 
 */
#define UF_PARAM_DRIVE_POINT   1066 


/* UF_PARAM_TL_LIBREF
 *
 *   Description:
 *      This index specifies the current libref of a
 *      tool. This value will be used to export the
 *      tool to the tool library.
 *
 *   Type: UF_PARAM_type_string
 *
 *   Name: Cutter Libref
 *  Variable Name: <prefix>_cutter_libref
 *
 *   Possible Values: 
 *
 * 
 */
#define UF_PARAM_TL_LIBREF   1067 


/* UF_PARAM_TL_DESCRIPTION
 *
 *   Description:
 *      This index specifies the description 
 *      attribute of a tool.
 *
 *   Type: UF_PARAM_type_string
 *
 *   Name: Cutter Description
 *  Variable Name: <prefix>_cutter_description
 *
 *   Possible Values: 
 *
 * 
 */
#define UF_PARAM_TL_DESCRIPTION   1068 


/* UF_PARAM_TL_TRACKPOINT_LIBREF
 *
 *   Description:
 *      This index specifies the current libref of a
 *      library trackpoint set.  This may differ from the
 *      original libref if the user wishes to rename the
 *      trackpoint set or create a copy of it.
 *
 *   Type: UF_PARAM_type_string
 *
 *   Name: Cutter Trackpoint Libref
 *  Variable Name: <prefix>_cutter_trackpoint_libref
 *
 *   Possible Values: 
 *
 * 
 */
#define UF_PARAM_TL_TRACKPOINT_LIBREF   1069 


/* UF_PARAM_TL_TURN_HOLDER_TOG
 *
 *  Description:
 *      This index has to be activated, if you want to use
 *      the turn holder.
 *
 *  Type: UF_PARAM_type_logical
 *
 *  Name: Turn Holder Use
 *  Variable Name: <prefix>_turn_holder_use
 *
 *  Possible Values: 1 (active) or 0 (inactive)
 *    Valid for cutter type
 *             CUTTER_TYPE_TURN
 *             CUTTER_TYPE_THREAD
 *             CUTTER_TYPE_GROOVE
 *             CUTTER_TYPE_FORM
 *
 * 
 */
#define UF_PARAM_TL_TURN_HOLDER_TOG   1070 


typedef enum
{
    UF_PARAM_tl_turn_holder_style_A =  0,
    UF_PARAM_tl_turn_holder_style_B =  1,
    UF_PARAM_tl_turn_holder_style_C =  2,
    UF_PARAM_tl_turn_holder_style_D =  3,
    UF_PARAM_tl_turn_holder_style_E =  4,
    UF_PARAM_tl_turn_holder_style_F =  5,
    UF_PARAM_tl_turn_holder_style_G =  6,
    UF_PARAM_tl_turn_holder_style_H =  7,
    UF_PARAM_tl_turn_holder_style_I =  8,
    UF_PARAM_tl_turn_holder_style_J =  9,
    UF_PARAM_tl_turn_holder_style_K = 10,
    UF_PARAM_tl_turn_holder_style_L = 11,
    UF_PARAM_tl_turn_holder_style_M = 12,
    UF_PARAM_tl_turn_holder_style_N = 13,
    UF_PARAM_tl_turn_holder_style_O = 14,
    UF_PARAM_tl_turn_holder_style_P = 15,
    UF_PARAM_tl_turn_holder_style_Q = 16,
    UF_PARAM_tl_turn_holder_style_R = 17,
    UF_PARAM_tl_turn_holder_style_S = 18,
    UF_PARAM_tl_turn_holder_style_T = 19,
    UF_PARAM_tl_turn_holder_style_U = 20,
    UF_PARAM_tl_turn_holder_style_V = 21,
    UF_PARAM_tl_turn_holder_style_UD = 22,
    UF_PARAM_tl_turn_holder_style_groove_0 = 23,
    UF_PARAM_tl_turn_holder_style_groove_45 = 24,
    UF_PARAM_tl_turn_holder_style_groove_90 = 25,
    UF_PARAM_tl_turn_holder_style_groove_user_defined = 26

}UF_PARAM_tl_turn_holder_style_t, *UF_PARAM_tl_turn_holder_style_p_t;


/* UF_PARAM_TL_TURN_HOLDER_STYLE
 *
 *  Description:
 *      This index defines the ISO/ANSI style of the turn holder.
 *
 *  Type: UF_PARAM_type_int
 *
 *  Name: Turn Holder Style
 *  Variable Name: <prefix>_turn_holder_style
 *
 *  Possible Values: UF_PARAM_tl_turn_holder_style_t
 *    Valid for cutter type
 *             CUTTER_TYPE_TURN
 *             CUTTER_TYPE_THREAD
 *             CUTTER_TYPE_GROOVE
 *             CUTTER_TYPE_FORM
 *
 * 
 */
#define UF_PARAM_TL_TURN_HOLDER_STYLE   1071 


typedef enum
{
    UF_PARAM_tl_turn_holder_hand_left = 0,
    UF_PARAM_tl_turn_holder_hand_neutral,
    UF_PARAM_tl_turn_holder_hand_right

}UF_PARAM_tl_turn_holder_hand_t, *UF_PARAM_tl_turn_holder_hand_p_t;


/* UF_PARAM_TL_TURN_HOLDER_HAND
 *
 *  Description:
 *      This index defines the tool hand designation of the turn holder.
 *
 *  Type: UF_PARAM_type_int
 *
 *  Name: Turn Holder Hand
 *  Variable Name: <prefix>_turn_holder_hand
 *
 *  Possible Values: UF_PARAM_tl_turn_holder_hand_t
 *    Valid for cutter type
 *             CUTTER_TYPE_TURN
 *             CUTTER_TYPE_THREAD
 *             CUTTER_TYPE_GROOVE
 *             CUTTER_TYPE_FORM
 *
 * 
 */
#define UF_PARAM_TL_TURN_HOLDER_HAND   1072 


typedef enum
{
    UF_PARAM_tl_turn_holder_shank_type_square = 0,
    UF_PARAM_tl_turn_holder_shank_type_round = 1

}UF_PARAM_tl_turn_holder_shank_type_t;


/* UF_PARAM_TL_TURN_HOLDER_SHANK_TYPE
 *
 *  Description:
 *      This index defines the type of the turn holder shank, square or round.
 *
 *  Type: UF_PARAM_type_int
 *
 *  Name: Turn Holder Shank Type
 *  Variable Name: <prefix>_turn_holder_shank_type
 *
 *  Possible Values: UF_PARAM_tl_turn_holder_shank_type_t
 *    Valid for cutter type
 *             CUTTER_TYPE_TURN
 *             CUTTER_TYPE_THREAD
 *             CUTTER_TYPE_GROOVE
 *             CUTTER_TYPE_FORM
 *
 * 
 */
#define UF_PARAM_TL_TURN_HOLDER_SHANK_TYPE   1073 


/* UF_PARAM_TL_TURN_HOLDER_ANGLE
 *
 *   Description:
 *      This parameter defines the orientation angle of the
 *      turning holder.
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Tool Holder Orient Angle
 *  Variable Name: <prefix>_tool_holder_orient_angle
 *
 *   Possible Values: double (radians)
 *
 * 
 */
#define UF_PARAM_TL_TURN_HOLDER_ANGLE   1074 


/* UF_PARAM_TL_TURN_HOLDER_LENGTH
 *
 *   Description:
 *      This index describes the qualified dimension from the tangent position
 *      on the tool nose radius to the opposite side of the turn holder.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Turn Holder Length
 *  Variable Name: <prefix>_turn_holder_length
 *
 *   Possible Values: UF_PARAM_type_double_length
 *    Valid for cutter type
 *             CUTTER_TYPE_TURN
 *             CUTTER_TYPE_THREAD
 *             CUTTER_TYPE_GROOVE
 *             CUTTER_TYPE_FORM
 *
 * 
 */
#define UF_PARAM_TL_TURN_HOLDER_LENGTH   1075 


/* UF_PARAM_TL_TURN_HOLDER_WIDTH
 *
 *   Description:
 *      This index describes the qualified dimension from the tangent position
 *      on the tool nose radius to the locating side of the turn holder.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Turn Holder Width
 *  Variable Name: <prefix>_turn_holder_width
 *
 *   Possible Values: UF_PARAM_type_double_length
 *    Valid for cutter type
 *             CUTTER_TYPE_TURN
 *             CUTTER_TYPE_THREAD
 *             CUTTER_TYPE_GROOVE
 *             CUTTER_TYPE_FORM
 *
 * 
 */
#define UF_PARAM_TL_TURN_HOLDER_WIDTH   1076 


/* UF_PARAM_TL_TURN_HOLDER_SHANK_WIDTH
 *
 *   Description:
 *      This index describes the width of the turn holder shank.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Turn Holder Shank Width
 *  Variable Name: <prefix>_turn_holder_shank_width
 *
 *   Possible Values: UF_PARAM_type_double_length
 *    Valid for cutter type
 *             CUTTER_TYPE_TURN
 *             CUTTER_TYPE_THREAD
 *             CUTTER_TYPE_GROOVE
 *             CUTTER_TYPE_FORM
 *
 * 
 */
#define UF_PARAM_TL_TURN_HOLDER_SHANK_WIDTH   1077 


/* UF_PARAM_TL_TURN_HOLDER_HEAD_WIDTH
 *
 *   Description:
 *      This index describes the head width of the turn holder.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Turn Holder Head Width
 *  Variable Name: <prefix>_turn_holder_head_width
 *
 *   Possible Values: UF_PARAM_type_double_length
 *    Valid for cutter type
 *             CUTTER_TYPE_TURN
 *             CUTTER_TYPE_THREAD
 *             CUTTER_TYPE_GROOVE
 *             CUTTER_TYPE_FORM
 *
 * 
 */
#define UF_PARAM_TL_TURN_HOLDER_HEAD_WIDTH   1078 


/* UF_PARAM_TL_TURN_HOLDER_SHANK_LINE
 *
 *   Description:
 *      This index describes the dimension from the tangent position on the
 *      tool nose radius to the break line between the tool head and the shank.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Turn Holder Shank Line
 *  Variable Name: <prefix>_turn_holder_shank_line
 *
 *   Possible Values: UF_PARAM_type_double_length
 *    Valid for cutter type
 *             CUTTER_TYPE_TURN
 *             CUTTER_TYPE_THREAD
 *             CUTTER_TYPE_GROOVE
 *             CUTTER_TYPE_FORM
 *
 * 
 */
#define UF_PARAM_TL_TURN_HOLDER_SHANK_LINE   1079 


/* UF_PARAM_TL_XMOUNT
 *
 *   Description:
 *      This index specifies the distance between tool tip and
 *      mounting point in X.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Tool XMount
 *  Variable Name: <prefix>_tool_xmount
 *
 *   Possible Values: UF_PARAM_type_double_length
 *    Valid for cutter type
 *             CUTTER_TYPE_TURN
 *             CUTTER_TYPE_THREAD
 *             CUTTER_TYPE_GROOVE
 *             CUTTER_TYPE_FORM
 *
 * 
 */
#define UF_PARAM_TL_XMOUNT   1080 


/* UF_PARAM_TL_YMOUNT
 *
 *   Description:
 *      This index specifies the distance between tool tip and
 *      mounting point in Y.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Tool YMount
 *  Variable Name: <prefix>_tool_ymount
 *
 *   Possible Values: UF_PARAM_type_double_length
 *    Valid for all cutter types
 *
 * 
 */
#define UF_PARAM_TL_YMOUNT   1081 


/* UF_PARAM_TL_ZMOUNT
 *
 *   Description:
 *      This index specifies the distance between tool tip and
 *      mounting point in Z.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Tool ZMount
 *  Variable Name: <prefix>_tool_zmount
 *
 *   Possible Values: UF_PARAM_type_double_length
 *    Valid for all cutter types
 *
 * 
 */
#define UF_PARAM_TL_ZMOUNT   1082 


/* UF_PARAM_TL_TURN_HOLDER_INSERT_EXTENSION
 *
 *   Description:
 *      This index describes the dimension from the tangent position on the
 *      tool nose radius to the edge of the holder, where the support 
 *      arm/insert sticks out.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Turn Holder Insert Extension
 *  Variable Name: <prefix>_turn_holder_insert_extension
 *
 *   Possible Values: UF_PARAM_type_double_length
 *    Valid for cutter type
 *             CUTTER_TYPE_GROOVE
 *
 * 
 */
#define UF_PARAM_TL_TURN_HOLDER_INSERT_EXTENSION   1083 


/* UF_PARAM_TL_TURN_HOLDER_LOCK
 *
 *  Description:
 *      This index has to be activated, if you want to lock
 *      the turn holder to the insert for user defined holder style.
 *
 *  Type: UF_PARAM_type_int
 *
 *  Name: Turn Holder Lock
 *  Variable Name: <prefix>_turn_holder_lock
 *
 *  Possible Values: 1 (active) or 0 (inactive)
 *    Valid for cutter type
 *             CUTTER_TYPE_TURN
 *             CUTTER_TYPE_THREAD
 *             CUTTER_TYPE_GROOVE
 *             CUTTER_TYPE_FORM
 *
 * 
 */
#define UF_PARAM_TL_TURN_HOLDER_LOCK   1084 


/* UF_PARAM_TL_LEFT_ANG
 *
 *   Description:
 *      This index defines the left clearance angle of grooving
 *      and threading asymmetrical tools (radians).
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Tool Left Angle
 *  Variable Name: <prefix>_tool_left_angle
 *
 *   Possible Values: UF_PARAM_type_double
 *
 * 
 */
#define UF_PARAM_TL_LEFT_ANG   1100 


/* UF_PARAM_TL_RIGHT_ANG
 *
 *   Description:
 *      This index defines the right clearance angle of grooving
 *      and threading asymmetrical tools (radians).
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Tool Right Angle
 *  Variable Name: <prefix>_tool_right_angle
 *
 *   Possible Values: UF_PARAM_type_double
 *
 * 
 */
#define UF_PARAM_TL_RIGHT_ANG   1101 


/* UF_PARAM_TL_INSERT_LENGTH
 *
 *   Description:
 *      This index specifies the total length of the insert of
 *      grooving and threading tools.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Tool Insert Length
 *  Variable Name: <prefix>_tool_insert_length
 *
 *   Possible Values: UF_PARAM_type_double_length
 *
 * 
 */
#define UF_PARAM_TL_INSERT_LENGTH   1102 


/* UF_PARAM_TL_MAX_DEPTH_TOG
 *
 *   Description:
 *      This index has to be turned on, if you want to use
 *      parameter UF_PARAM_TL_MAX_DEPTH.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Tool Max Depth Toggle
 *  Variable Name: <prefix>_tool_max_depth_toggle
 *
 *   Possible Values: 
 *     0 = inactive
 *     1 = active
 *
 * 
 */
#define UF_PARAM_TL_MAX_DEPTH_TOG   1103 


/* UF_PARAM_TL_X_OFFSET_TOG
 *
 *   Description:
 *      This index has to be turned on, if you want to use
 *      parameter UF_PARAM_TL_X_OFFSET.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Tool X-Offset Toggle
 *  Variable Name: <prefix>_tool_x_offset_toggle
 *
 *   Possible Values: 
 *     0 = inactive
 *     1 = active
 *
 * 
 */
#define UF_PARAM_TL_X_OFFSET_TOG   1104 


/* UF_PARAM_TL_Y_OFFSET_TOG
 *
 *   Description:
 *      This index has to be turned on, if you want to use
 *      parameter UF_PARAM_TL_Y_OFFSET.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Tool Y-Offset Toggle
 *  Variable Name: <prefix>_tool_y_offset_toggle
 *
 *   Possible Values: 
 *     0 = inactive
 *     1 = active
 *
 * 
 */
#define UF_PARAM_TL_Y_OFFSET_TOG   1105 


/* UF_PARAM_TL_THICKNESS
 *
 *   Description:
 *      This index specifies the thickness of the turning tool insert.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Tool Thickness
 *  Variable Name: <prefix>_tool_thickness
 *
 *   Possible Values: UF_PARAM_type_double_length
 *
 * 
 */
#define UF_PARAM_TL_THICKNESS   1106 


/* UF_PARAM_TL_ADJ_REG_TOG
 *
 *   Description:
 *      This index has to be turned on, if you want to use
 *      parameter UF_PARAM_TL_ADJ_REG.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Tool Adjust Register Toggle
 *  Variable Name: <prefix>_tool_adjust_register_toggle
 *
 *   Possible Values: 
 *     0 = inactive
 *     1 = active
 *
 *   Developer: 
 */
#define UF_PARAM_TL_ADJ_REG_TOG   1107 


/* UF_PARAM_TL_CUTCOM_REG_TOG
 *
 *   Description:
 *      This index has to be turned on, if you want to use
 *      parameter UF_PARAM_TL_CUTCOM_REG.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Tool Cutcom Reg Toggle
 *  Variable Name: <prefix>_tool_cutcom_reg_toggle
 *
 *   Possible Values: 
 *     0 = inactive
 *     1 = active
 *
 * 
 */
#define UF_PARAM_TL_CUTCOM_REG_TOG   1108 


/* UF_PARAM_TL_INSERTTYPE
 *
 *   Description:
 *      This index specifies the insert shapes for standard turning,
 *      grooving and threading tools. For standard turning tools,
 *      parallelogram, diamond, hexagon, parallelogram, rectangle,
 *      octagon, pentagon, round, square, triangle, triagon or user
 *      defined inserts are possible. For grooving tools, standard,
 *      full nose radius, ring type joint or user defined inserts
 *      are possible. For threading tools, standard and trapeziodal
 *      inserts are possible.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Tool Insert Type
 *  Variable Name: <prefix>_tool_insert_type
 *
 *   Possible Values: 
 *
 *     Standard turning tools:
 *      UF_TURN_INSERTTYPE_PARALLEL_85  Parallelogram 85  ( ISO A )
 *      UF_TURN_INSERTTYPE_PARALLEL_82  Parallelogram 82  ( ISO B )
 *      UF_TURN_INSERTTYPE_DIAMOND_80   Diamond 80        ( ISO C )
 *      UF_TURN_INSERTTYPE_DIAMOND_100  Diamond 100       ( ISO C turned 90deg )
 *      UF_TURN_INSERTTYPE_DIAMOND_55   Diamond 55        ( ISO D )
 *      UF_TURN_INSERTTYPE_DIAMOND_75   Diamond 75        ( ISO E )
 *      UF_TURN_INSERTTYPE_HEXAGON      Hexagon           ( ISO H )
 *      UF_TURN_INSERTTYPE_PARALLEL_55  Parallelogram 55  ( ISO K )
 *      UF_TURN_INSERTTYPE_RECTANGLE    Rectangle         ( ISO L )
 *      UF_TURN_INSERTTYPE_DIAMOND_86   Diamond 86        ( ISO M )
 *      UF_TURN_INSERTTYPE_OCTAGON      Octagon           ( ISO O )
 *      UF_TURN_INSERTTYPE_PENTAGON     Pentagon          ( ISO P )
 *      UF_TURN_INSERTTYPE_ROUND        Round             ( ISO R )
 *      UF_TURN_INSERTTYPE_SQUARE       Square            ( ISO S )
 *      UF_TURN_INSERTTYPE_TRIANGLE     Triangle          ( ISO T )
 *      UF_TURN_INSERTTYPE_DIAMOND_35   Diamond 35        ( ISO V )
 *      UF_TURN_INSERTTYPE_TRIGON       Trigon            ( ISO W )
 *      UF_TURN_INSERTTYPE_USER         User defined
 *
 *     Grooving tools:
 *      UF_TURN_INSERTTYPE_GRV_STD   Standard grooving tool
 *      UF_TURN_INSERTTYPE_GRV_FNR   Full nose radius grooving tool
 *      UF_TURN_INSERTTYPE_GRV_RTJ   Ring type joint grooving tool
 *      UF_TURN_INSERTTYPE_GRV_USER  User defined grooving tool
 *
 *     Threading tools:
 *      UF_TURN_INSERTTYPE_THREAD_STD   Standard threading tool
 *      UF_TURN_INSERTTYPE_THREAD_TRAP  Trapezoidal threading tool
 *
 * 
 */
#define UF_PARAM_TL_INSERTTYPE   1110 


/* UF_PARAM_TL_BUTTON_DIAMETER
 *
 *   Description:
 *      This index specifies the diameter of the button tool
 *      ( ISO R, Round ).
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Tool Button Diameter
 *  Variable Name: <prefix>_tool_button_diameter
 *
 *   Possible Values: UF_PARAM_type_double_length
 *
 * 
 */
#define UF_PARAM_TL_BUTTON_DIAMETER   1111 


/* UF_PARAM_TL_HOLDER_ANG
 *
 *   Description:
 *      This index specifies the holder angle of the button
 *      tool holder (radians).
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Tool Holder Angle
 *  Variable Name: <prefix>_tool_holder_angle
 *
 *   Possible Values: UF_PARAM_type_double
 *
 * 
 */
#define UF_PARAM_TL_HOLDER_ANG   1112 


/* UF_PARAM_TL_NOSE_ANG
 *
 *   Description:
 *      This index specifies the angle caused by the intersection
 *      of the two edges of the turning tool insert (radians).
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Tool Nose Angle
 *  Variable Name: <prefix>_tool_nose_angle
 *
 *   Possible Values: UF_PARAM_type_double
 *
 * 
 */
#define UF_PARAM_TL_NOSE_ANG   1113 


/* UF_PARAM_TL_CUT_EDGE_LENGTH
 *
 *   Description:
 *      This index specifies the cutting edge length of the turning
 *      tool insert.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Tool Cut Edge Length
 *  Variable Name: <prefix>_tool_cut_edge_length
 *
 *   Possible Values: UF_PARAM_type_double_length
 *
 * 
 */
#define UF_PARAM_TL_CUT_EDGE_LENGTH   1114 


/* UF_PARAM_TL_THICKNESS_OPT
 *
 *   Description:
 *      This index specifies the thickness of the turning tool insert.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Tool Thickness O
 *  Variable Name: <prefix>_tool_thickness_o
 *
 *   Possible Values: 
 *    0   01
 *    1   T1
 *    2   02
 *    3   T2
 *    4   03
 *    5   T3
 *    6   04
 *    7   05
 *    8   06
 *    9   07
 *   10   09
 *   11   11
 *   12   12
 *   13   User defined (use UF_PARAM_TL_THICKNESS)
 *
 * 
 */
#define UF_PARAM_TL_THICKNESS_OPT   1115 


/* UF_PARAM_TL_RELIEF_ANG_OPT
 *
 *   Description:
 *      This index specifies the angle caused by the slope of the
 *      cutter away from the cutting edge of the turning tool
 *      insert.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Tool Relief Angle O
 *  Variable Name: <prefix>_tool_relief_angle_o
 *
 *   Possible Values: 
 *    1   A (3)
 *    2   B (5)
 *    3   C (7)
 *    4   D (15)
 *    5   E (20)
 *    6   F (25)
 *    7   G (30)
 *    8   N (0)
 *    9   P (11)
 *   10   O (other)  (use UF_PARAM_TL_RELIEF_ANG)
 *
 * 
 */
#define UF_PARAM_TL_RELIEF_ANG_OPT   1116 


/* UF_PARAM_TL_TRACKING_POINT
 *
 *   Description:
 *      This index specifies the tracking point of the turning tool.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Tool Tracking Point
 *  Variable Name: <prefix>_tool_tracking_point
 *
 *   Possible Values: 
 *    0   P2
 *    1   P6
 *    2   P1
 *    3   P7
 *    4   P9
 *    5   P5
 *    6   P3
 *    7   P8
 *    8   P4
 *
 * 
 */
#define UF_PARAM_TL_TRACKING_POINT   1117 


/* UF_PARAM_TL_MAX_TOOLREACH
 *
 *   Description:
 *      This index describes the maximum distance which a tool
 *      and its holder can travel into a part. This is dependant
 *      upon the geometry of a part and the tool holder. The
 *      purpose of this parameter is to prevent collision of 
 *      the tool holder with the part.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Tool Max Toolreach
 *  Variable Name: <prefix>_tool_max_toolreach
 *
 *   Possible Values: UF_PARAM_type_double_length
 *
 * 
 */
#define UF_PARAM_TL_MAX_TOOLREACH   1118 


/* UF_PARAM_TL_MAX_TOOLREACH_TOG
 *
 *   Description:
 *      This index has to be turned on, if you want to use
 *      parameter UF_PARAM_TL_MAX_TOOLREACH.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Tool Max Toolreach Toggle
 *  Variable Name: <prefix>_tool_max_toolreach_toggle
 *
 *   Possible Values: 
 *     0 = inactive
 *     1 = active
 *
 * 
 */
#define UF_PARAM_TL_MAX_TOOLREACH_TOG   1119 


/* UF_PARAM_TL_MIN_BORING_DIA
 *
 *   Description:
 *      This index describes the minimum distance needed to prevent
 *      a tool and its holder from colliding with the part. For
 *      instance, when drilling a hole of one centimeter, a tool
 *      holder that is wider than 1 centimeter cannot be used if
 *      the holder is expected to travel into the hole that is
 *      being drilled.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Tool Min Boring Diameter
 *  Variable Name: <prefix>_tool_min_boring_diameter
 *
 *   Possible Values: UF_PARAM_type_double_length
 *
 * 
 */
#define UF_PARAM_TL_MIN_BORING_DIA   1120 


/* UF_PARAM_TL_MIN_BORING_DIA_TOG
 *
 *   Description:
 *      This index has to be turned on, if you want to use
 *      parameter UF_PARAM_TL_MIN_BORING_DIA.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Tool Min Boring Diameter T
 *  Variable Name: <prefix>_tool_min_boring_diameter_t
 *
 *   Possible Values: 
 *     0 = inactive
 *     1 = active
 *
 * 
 */
#define UF_PARAM_TL_MIN_BORING_DIA_TOG   1121 


/* UF_PARAM_TURN_IGNORE_MIN_BORING_DIA
 *
 *   Description:
 *      This index lets you ignore the value tool value 
 *      UF_PARAM_TL_MIN_BORING_DIA on operation level.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Ignore Min Boring Diameter
 *  Variable Name: <prefix>_ignore_min_boring_diameter
 *
 *   Possible Values: 
 *     0 = Off
 *     1 = On
 *
 * 
 */
#define UF_PARAM_TURN_IGNORE_MIN_BORING_DIA   1125 


/* UF_PARAM_TL_SIZE_OPT
 *
 *   Description:
 *      This index specifies the size of the turning tool insert.
 *      Cut Edge Length, Inscribed Circle or Inscribed Circle ANSI
 *      are possible. The ISO insert size definition uses Cut Edge
 *      Length while the ANSI standard uses the inscribed circle.
 *      Depending on which standard the tool manufacturer uses, the
 *      corresponding method has to be set to determine the size.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Tool Size O
 *  Variable Name: <prefix>_tool_size_o
 *
 *   Possible Values: 
 *    0 Cut Edge Length
 *    1 Inscribed Circle
 *    2 Inscribed Circle ANSI
 *
 * 
 */
#define UF_PARAM_TL_SIZE_OPT   1122 


/* UF_PARAM_TL_NOSE_ANG_TOG
 *
 *   Description:
 *      This index specifies toggle for the angle caused by the intersection
 *      of the two edges of the turning tool insert (radians).
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Tool Nose Angle toggle
 *  Variable Name: <prefix>_tool_nose_angle_toggle
 *
 *   Possible Values: 
 *             0  -- Inactive
 *             1  -- Active
 *
 * 
 */
#define UF_PARAM_TL_NOSE_ANG_TOG   1123 


/* UF_PARAM_TL_NOSE_RAD_TOG
 *
 *   Description:
 *      This index specifies toggle for the radius of the inscribed circle
 *      at the cutter tip of the turning tool insert.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Tool Nose Radius Toggle
 *  Variable Name: <prefix>_tool_nose_radius_toggle
 *
 *   Possible Values: 
 *             0  -- Inactive
 *             1  -- Active
 *
 * 
 */
#define UF_PARAM_TL_NOSE_RAD_TOG   1124 


/* UF_PARAM_TL_RADIUS
 *
 *   Description:
 *      This index specifies the radius of the inscribed circle
 *      at the cutter tip. The Standard tool Radius assumes the
 *      tool's left and right nose radii are equal. You may define
 *      a left and right Radius in User Defined tool types.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Tool Radius
 *  Variable Name: <prefix>_tool_radius
 *
 *   Possible Values: UF_PARAM_type_double_length
 *
 * 
 */
#define UF_PARAM_TL_RADIUS   1130 


/* UF_PARAM_TL_SIDE_ANG
 *
 *   Description:
 *      The side angle defines the clearance angles of a grooving
 *      tool on the left and on the right side as equal (radians).
 *      A narrowing insert shape represents a positive value of the
 *      side angle, a widening insert shape a negative value. This
 *      parameter appears only in the Standard and Full Nose Radius
 *      tool types.
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Tool Side Angle
 *  Variable Name: <prefix>_tool_side_angle
 *
 *   Possible Values: UF_PARAM_type_double
 *
 * 
 */
#define UF_PARAM_TL_SIDE_ANG   1131 


/* UF_PARAM_TL_PRESET_CUTTER
 *
 *   Description:
 *      Defines which sides of the cutter are available for
 *      tracking on the machine (left, right or both). For each
 *      preset cutter there are three attributes available to be
 *      specified: Cutter Tracking Point, X Offset, Y Offset.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Tool Preset Cutter
 *  Variable Name: <prefix>_tool_preset_cutter
 *
 *   Possible Values: 
 *    0        Left
 *    1        Left & Right
 *    2        Right
 *
 * 
 */
#define UF_PARAM_TL_PRESET_CUTTER   1132 


/* UF_PARAM_TL_LEFT_TP
 *
 *   Description:
 *      This index specifies the tracking point of the left cutter
 *      of the grooving tool.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Tool Left Tracking Point
 *  Variable Name: <prefix>_tool_left_tracking_point
 *
 *   Possible Values: 
 *    0   P2
 *    1   P6
 *    2   P1
 *    3   P7
 *    4   P9
 *    5   P5
 *    6   P3
 *    7   P8
 *    8   P4
 *
 * 
 */
#define UF_PARAM_TL_LEFT_TP   1133 


/* UF_PARAM_TL_LEFT_XOFF
 *
 *   Description:
 *      This index specifies the left x offset, which is the x
 *      coordinate of the distance between the tool's reference
 *      point and it's left tracking point. Parameter
 *      UF_PARAM_TL_LEFT_XOFF_TOG has to be turned on.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Tool Left X-Offset
 *  Variable Name: <prefix>_tool_left_x_offset
 *
 *   Possible Values: UF_PARAM_type_double_length
 *
 * 
 */
#define UF_PARAM_TL_LEFT_XOFF   1134 


/* UF_PARAM_TL_LEFT_XOFF_TOG
 *
 *   Description:
 *      This index has to be turned on, if you want to use
 *      parameter UF_PARAM_TL_LEFT_XOFF.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Tool Left X-Offset Toggle
 *  Variable Name: <prefix>_tool_left_x_offset_toggle
 *
 *   Possible Values: 
 *     0 = inactive
 *     1 = active
 *
 * 
 */
#define UF_PARAM_TL_LEFT_XOFF_TOG   1135 


/* UF_PARAM_TL_LEFT_YOFF
 *
 *   Description:
 *      This index specifies the left y offset, which is the y
 *      coordinate of the distance between the tool's reference
 *      point and it's left tracking point. Parameter
 *      UF_PARAM_TL_LEFT_YOFF_TOG has to be turned on.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Tool Left Y-Offset
 *  Variable Name: <prefix>_tool_left_y_offset
 *
 *   Possible Values: UF_PARAM_type_double_length
 *
 * 
 */
#define UF_PARAM_TL_LEFT_YOFF   1136 


/* UF_PARAM_TL_LEFT_YOFF_TOG
 *
 *   Description:
 *      This index has to be turned on, if you want to use
 *      parameter UF_PARAM_TL_LEFT_YOFF.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Tool Left Y-Offset Toggle
 *  Variable Name: <prefix>_tool_left_y_offset_toggle
 *
 *   Possible Values: 
 *     0 = inactive
 *     1 = active
 *
 * 
 */
#define UF_PARAM_TL_LEFT_YOFF_TOG   1137 


/* UF_PARAM_TL_RIGHT_TP
 *
 *   Description:
 *      This index specifies the tracking point of the right cutter
 *      of the grooving tool.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Tool Right Tracking Point
 *  Variable Name: <prefix>_tool_right_tracking_point
 *
 *   Possible Values: 
 *    0   P2
 *    1   P6
 *    2   P1
 *    3   P7
 *    4   P9
 *    5   P5
 *    6   P3
 *    7   P8
 *    8   P4
 *
 * 
 */
#define UF_PARAM_TL_RIGHT_TP   1138 


/* UF_PARAM_TL_RIGHT_XOFF
 *
 *   Description:
 *      This index specifies the right x offset, which is the x
 *      coordinate of the distance between the tool's reference
 *      point and it's right tracking point. Parameter
 *      UF_PARAM_TL_RIGHT_XOFF_TOG has to be turned on.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Tool Right X-Offset
 *  Variable Name: <prefix>_tool_right_x_offset
 *
 *   Possible Values: UF_PARAM_type_double_length
 *
 * 
 */
#define UF_PARAM_TL_RIGHT_XOFF   1139 


/* UF_PARAM_TL_RIGHT_XOFF_TOG
 *
 *   Description:
 *      This index has to be turned on, if you want to use
 *      parameter UF_PARAM_TL_RIGHT_XOFF.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Tool Right X-Offset T
 *  Variable Name: <prefix>_tool_right_x_offset_t
 *
 *   Possible Values: 
 *     0 = inactive
 *     1 = active
 *
 * 
 */
#define UF_PARAM_TL_RIGHT_XOFF_TOG   1140 


/* UF_PARAM_TL_RIGHT_YOFF
 *
 *   Description:
 *      This index specifies the right y offset, which is the y
 *      coordinate of the distance between the tool's reference
 *      point and it's right tracking point. Parameter
 *      UF_PARAM_TL_RIGHT_YOFF_TOG has to be turned on.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Tool Right Y-Offset
 *  Variable Name: <prefix>_tool_right_y_offset
 *
 *   Possible Values: UF_PARAM_type_double_length
 *
 * 
 */
#define UF_PARAM_TL_RIGHT_YOFF   1141 


/* UF_PARAM_TL_RIGHT_YOFF_TOG
 *
 *   Description:
 *      This index has to be turned on, if you want to use
 *      parameter UF_PARAM_TL_RIGHT_YOFF.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Tool Right Y-Offset T
 *  Variable Name: <prefix>_tool_right_y_offset_t
 *
 *   Possible Values: 
 *     0 = inactive
 *     1 = active
 *
 * 
 */
#define UF_PARAM_TL_RIGHT_YOFF_TOG   1142 


/* UF_PARAM_TL_MIN_FACING_DIA
 *
 *   Description:
 *      This index describes the minimum admissible diameter
 *      for facing operations with grooving and form turning
 *      tools.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Tool Min Facing Diameter
 *  Variable Name: <prefix>_tool_min_facing_diameter
 *
 *   Possible Values: UF_PARAM_type_double_length
 *
 * 
 */
#define UF_PARAM_TL_MIN_FACING_DIA   1143 


/* UF_PARAM_TL_MIN_FACING_DIA_TOG
 *
 *   Description:
 *      This index has to be turned on, if you want to use
 *      parameter UF_PARAM_TL_MIN_FACING_DIA.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Tool Min Facing Diameter T
 *  Variable Name: <prefix>_tool_min_facing_diameter_t
 *
 *   Possible Values: 
 *     0 = inactive
 *     1 = active
 *
 * 
 */
#define UF_PARAM_TL_MIN_FACING_DIA_TOG   1144 


/* UF_PARAM_TL_MAX_FACING_DIA
 *
 *   Description:
 *      This index describes the maximum admissible diameter
 *      for facing operations with grooving and form turning
 *      tools.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Tool Max Facing Diameter
 *  Variable Name: <prefix>_tool_max_facing_diameter
 *
 *   Possible Values: UF_PARAM_type_double_length
 *
 * 
 */
#define UF_PARAM_TL_MAX_FACING_DIA   1145 


/* UF_PARAM_TL_MAX_FACING_DIA_TOG
 *
 *   Description:
 *      This index has to be turned on, if you want to use
 *      parameter UF_PARAM_TL_MAX_FACING_DIA.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Tool Max Facing Diameter T
 *  Variable Name: <prefix>_tool_max_facing_diameter_t
 *
 *   Possible Values: 
 *     0 = inactive
 *     1 = active
 *
 * 
 */
#define UF_PARAM_TL_MAX_FACING_DIA_TOG   1146 


/* UF_PARAM_TL_LEFT_ADJUST
 *
 *   Description:
 *      This index specifies the register number value on the
 *      controller which contains the tool offset coordinates
 *      for the left cutter.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Tool Left Adjust Reg
 *  Variable Name: <prefix>_tool_left_adjust_reg
 *
 *   Possible Values: UF_PARAM_type_int
 *
 * 
 */
#define UF_PARAM_TL_LEFT_ADJUST   1147 


/* UF_PARAM_TL_LEFT_ADJUST_TOG
 *
 *   Description:
 *      This index has to be turned on, if you want to use
 *      parameter UF_PARAM_TL_LEFT_ADJUST.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Tool Left Adjust Reg T
 *  Variable Name: <prefix>_tool_left_adjust_reg_t
 *
 *   Possible Values: 
 *     0 = inactive
 *     1 = active
 *
 * 
 */
#define UF_PARAM_TL_LEFT_ADJUST_TOG   1148 


/* UF_PARAM_TL_RIGHT_ADJUST
 *
 *   Description:
 *      This index specifies the register number value on the
 *      controller which contains the tool offset coordinates
 *      for the right cutter.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Tool Right Adjust Reg
 *  Variable Name: <prefix>_tool_right_adjust_reg
 *
 *   Possible Values: UF_PARAM_type_int
 *
 * 
 */
#define UF_PARAM_TL_RIGHT_ADJUST   1149 


/* UF_PARAM_TL_RIGHT_ADJUST_TOG
 *
 *   Description:
 *      This index has to be turned on, if you want to use
 *      parameter UF_PARAM_TL_RIGHT_ADJUST.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Tool Right Adjust Reg T
 *  Variable Name: <prefix>_tool_right_adjust_reg_t
 *
 *   Possible Values: 
 *     0 = inactive
 *     1 = active
 *
 * 
 */
#define UF_PARAM_TL_RIGHT_ADJUST_TOG   1150 


/* UF_PARAM_TL_LEFT_CUTCOM
 *
 *   Description:
 *      This index specifies the register number value on the
 *      controller which contains the value that the system uses
 *      to adjust the tool path to allow for variation due to an
 *      undersized or oversized cutter or tool (left cutter).
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Tool Left Cutcom Reg
 *  Variable Name: <prefix>_tool_left_cutcom_reg
 *
 *   Possible Values: UF_PARAM_type_int
 *
 * 
 */
#define UF_PARAM_TL_LEFT_CUTCOM   1151 


/* UF_PARAM_TL_LEFT_CUTCOM_TOG
 *
 *   Description:
 *      This index has to be turned on, if you want to use
 *      parameter UF_PARAM_TL_LEFT_CUTCOM.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Tool Left Cutcom Reg T
 *  Variable Name: <prefix>_tool_left_cutcom_reg_t
 *
 *   Possible Values: 
 *     0 = inactive
 *     1 = active
 *
 * 
 */
#define UF_PARAM_TL_LEFT_CUTCOM_TOG   1152 


/* UF_PARAM_TL_RIGHT_CUTCOM
 *
 *   Description:
 *      This index specifies the register number value on the
 *      controller which contains the value that the system uses
 *      to adjust the tool path to allow for variation due to an
 *      undersized or oversized cutter or tool (right cutter).
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Tool Right Cutcom Reg
 *  Variable Name: <prefix>_tool_right_cutcom_reg
 *
 *   Possible Values: UF_PARAM_type_int
 *
 * 
 */
#define UF_PARAM_TL_RIGHT_CUTCOM   1153 


/* UF_PARAM_TL_RIGHT_CUTCOM_TOG
 *
 *   Description:
 *      This index has to be turned on, if you want to use
 *      parameter UF_PARAM_TL_RIGHT_CUTCOM.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Tool Right Cutcom Reg T
 *  Variable Name: <prefix>_tool_right_cutcom_reg_t
 *
 *   Possible Values: 
 *     0 = inactive
 *     1 = active
 *
 * 
 */
#define UF_PARAM_TL_RIGHT_CUTCOM_TOG   1154 


/* UF_PARAM_TL_MANUAL_TOOLCHANGE
 *
 *  Description:
 *  This index is the status of whether a tool can be loaded manually.
 *
 *  Type: UF_PARAM_type_logical
 *
 *  Name: Tool Manual toolchange
 *  Variable Name: <prefix>_tool_manual_toolchange
 *
 *  Possible Values: 1 or 0
 *    Valid for cutter type
 *              All
 * 
 */
#define UF_PARAM_TL_MANUAL_TOOLCHANGE   1155 


/* UF_PARAM_TL_HOLDER_NUMBER
 *
 *  Description:
 *  This index is the tool holder number in which tool is loaded.
 *
 *  Type: UF_PARAM_type_int
 *
 *  Name: Tool Holder Num
 *  Variable Name: <prefix>_tool_holder_num
 *
 *  Possible Values: All
 *    Valid for cutter type
 *              All
 * 
 */
#define UF_PARAM_TL_HOLDER_NUMBER   1156 


/* UF_PARAM_TL_HEAD_DESIGN
 *
 *  Description:
 *  This index is the type of tool head  for turning tools.
 *
 *  Type: UF_PARAM_type_int
 *
 *  Name: Tool Head Designation
 *  Variable Name: <prefix>_tool_head_designation
 *
 *  Possible Values: All
 *    Valid for cutter type
 *              All
 * 
 */
#define UF_PARAM_TL_HEAD_DESIGN   1157 


/* UF_PARAM_TL_TEXT
 *
 *  Description:
 *  This index for additional parameters for the tool.
 *
 *  Type: UF_PARAM_type_string
 *
 *  Name: Tool text
 *  Variable Name: <prefix>_tool_text
 *
 *  Possible Values: All
 *    Valid for cutter type
 *              All
 * 
 */
#define UF_PARAM_TL_TEXT   1158 


/* UF_PARAM_TL_NUMBER_TOG
 *
 *  Description:
 *  This index for additional parameters for the tool.
 *
 *  Type: UF_PARAM_type_int
 *
 *  Name: Tool Number Toggle
 *  Variable Name: <prefix>_tool_number_toggle
 *
 *   Possible Values:
 *     0 = inactive
 *     1 = active
 *    Valid for cutter type
 *              All
 * 
 */
#define UF_PARAM_TL_NUMBER_TOG   1159 


/* UF_PARAM_TL_Z_OFFSET_TOG
 *
 *  Description:
 *  This index for additional parameters for the tool.
 *
 *  Type: UF_PARAM_type_int
 *
 *  Name: Tool Z-Offset toggle
 *  Variable Name: <prefix>_tool_z_offset_toggle
 *
 *  Possible Values:
 *     0 = inactive
 *     1 = active
 *    Valid for cutter type
 *             UF_CUTTER_TYPE_MILL
 *             UF_CUTTER_TYPE_DRILL
 *             UF_CUTTER_TYPE_BARREL
 *             UF_CUTTER_TYPE_T
 *
 * 
 */
#define UF_PARAM_TL_Z_OFFSET_TOG   1160  


/* UF_PARAM_TL_HOLDER_NUMBER_TOG
 *
 *  Description:
 *  This index is the tool holder number toggle to control output to the
 *  down stream
 *
 *  Type: UF_PARAM_type_int
 *
 *  Name: Tool Holder Num toggle
 *  Variable Name: <prefix>_tool_holder_num_toggle
 *
 *  Possible Values:
 *     0 = inactive
 *     1 = active
 *    Valid for cutter type
 *              All
 * 
 */
#define UF_PARAM_TL_HOLDER_NUMBER_TOG   1161 


/* UF_PARAM_TL_TEXT_TOG
 *
 *  Description:
 *  This index for additional parameters for the tool.
 *
 *  Type: UF_PARAM_type_int
 *
 *  Name: Tool text toggle
 *  Variable Name: <prefix>_tool_text_toggle
 *
 *  Possible Values:
 *     0 = inactive
 *     1 = active
 *    Valid for cutter type
 *              All
 * 
 */
#define UF_PARAM_TL_TEXT_TOG   1162 


/* UF_PARAM_TL_NOSE_RADIUS_ARRAY
 *
 *   Description:
 *      This index describes the shape of a turning form tool
 *      in parametric form. It represents an array holding the
 *      tool nose radii information (see manufacturing turning
 *      help for more information).
 *
 *   Type: UF_PARAM_type_vla_length
 *
 *   Name: Tool Nose Radius A
 *  Variable Name: <prefix>_tool_nose_radius_a
 *
 *   Possible Values: double_length Array (size of 20)
 *
 * 
 */
#define UF_PARAM_TL_NOSE_RADIUS_ARRAY   1170 


/* UF_PARAM_TL_NOSE_ANGLE_ARRAY
 *
 *   Description:
 *      This index describes the shape of a turning form tool
 *      in parametric form. It represents an array holding the
 *      tool nose angle (radians) information (see manufacturing
 *      turning help for more information).
 *
 *   Type: UF_PARAM_type_vla_real
 *
 *   Name: Tool Nose Angle A
 *  Variable Name: <prefix>_tool_nose_angle_a
 *
 *   Possible Values: double Array (size of 20)
 *
 * 
 */
#define UF_PARAM_TL_NOSE_ANGLE_ARRAY   1171 


/* UF_PARAM_TL_EDGE_LENGTH_ARRAY
 *
 *   Description:
 *      This index describes the shape of a turning form tool
 *      in parametric form. It represents an array holding the
 *      tool edge length information (see manufacturing turning
 *      help for more information).
 *
 *   Type: UF_PARAM_type_vla_length
 *
 *   Name: Tool Edge Length A
 *  Variable Name: <prefix>_tool_edge_length_a
 *
 *   Possible Values: double_length Array (size of 20)
 *
 * 
 */
#define UF_PARAM_TL_EDGE_LENGTH_ARRAY   1172 


/* UF_PARAM_TL_TRACKING_ARRAY
 *
 *   Description:
 *      This index describes the shape of a turning form tool
 *      in parametric form. It represents an array holding the
 *      tracking point location information (see manufacturing
 *      turning help for more information).
 *
 *   Type: UF_PARAM_type_vla_int
 *
 *   Name: Tool Tracking A
 *  Variable Name: <prefix>_tool_tracking_a
 *
 *   Possible Values: Array (size of 20)
 *    0        Left
 *    1        Left & Right
 *    2        Right
 *
 * 
 */
#define UF_PARAM_TL_TRACKING_ARRAY   1173 


/* UF_PARAM_TL_NO_OF_NOSES
 *
 *   Description:
 *      This index contains the number of noses of a Form
 *      turning tool.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Tool Number of Noses
 *  Variable Name: <prefix>_tool_number_of_noses
 *
 *   Possible Values: UF_PARAM_type_int
 *
 * 
 */
#define UF_PARAM_TL_NO_OF_NOSES   1174 


/* UF_PARAM_TL_PITCH
 *
 *  Description:
 *  This is the distance from one cutting opint to an adjacent cutting point.
 *
 *  Type: UF_PARAM_type_double_length
 *
 *  Name: Tool Pitch
 *  Variable Name: <prefix>_tool_pitch
 *
 *  Possible Values: non-negative UF_PARAM_type_double_length
 *    Valid for cutter type
 *             CUTTER_TYPE_DRILL
 *
 * 
 */
#define UF_PARAM_TL_PITCH   1185  /*    */


/* UF_PARAM_TL_THREAD_FORMING_METHOD
 *
 *  Description:
 *  This defines the types/methods of thread forming.
 *
 *  Type: UF_PARAM_type_int
 *
 *  Name: Tool Thread Forming Method
 *  Variable Name: <prefix>_tool_thread_forming_method
 *
 *  Possible Values:
 *        UF_PARAM_tl_thread_forming_method_t
 *    Valid for cutter type
 *             CUTTER_TYPE_DRILL
 *
 * 
 */
#define UF_PARAM_TL_THREAD_FORMING_METHOD   1186  /*    */


/* UF_PARAM_TL_NUM_STEPS
 *
 *  Description:
 *  The parameter indicates the number of steps for step drill
 *
 *  Type: UF_PARAM_type_int
 *
 *  Name: Tool Number of Steps for Step Drill
 *  Variable Name: <prefix>_tool_number_of_steps_for_step_drill
 *
 *  Possible Values:
 *        UF_PARAM_type_int
 *    Valid for cutter type
 *             CUTTER_TYPE_DRILL
 *
 * 
 */
#define UF_PARAM_TL_NUM_STEPS   1190  


/* UF_PARAM_TL_STEP_DIA_ARRAY 
 *
 *   Description:
 *      Value of step diameter
 *
 *   Type: UF_PARAM_type_vla_length
 *
 *   Name: Step Diameter Array 
 *  Variable Name: <prefix>_step_diameter_array
 *
 *   Possible Values: UF_PARAM_type_vla_length
 *                    array of double (size = 20)
 *
 * 
 */
#define UF_PARAM_TL_STEP_DIA_ARRAY   1191  


/* UF_PARAM_TL_STEP_HEIGHT_ARRAY 
 *
 *   Description:
 *      Value of step length
 *
 *   Type: UF_PARAM_type_vla_length
 *
 *   Name: Step length Array 
 *  Variable Name: <prefix>_step_length_array
 *
 *   Possible Values: UF_PARAM_type_vla_length
 *                    array of double (size = 20)
 *
 * 
 */
#define UF_PARAM_TL_STEP_HEIGHT_ARRAY   1192  


/* UF_PARAM_TL_STEP_ANGLE_ARRAY 
 *
 *   Description:
 *      Value of step angle
 *
 *   Type: UF_PARAM_type_vla_real
 *
 *   Name: Step Angle Array 
 *  Variable Name: <prefix>_step_angle_array
 *
 *   Possible Values: UF_PARAM_type_vla_real
 *                    (size = 20)
 *
 * 
 */
#define UF_PARAM_TL_STEP_ANGLE_ARRAY   1193  


/* UF_PARAM_TL_STEP_RADIUS_ARRAY 
 *
 *   Description:
 *      Value of step corner radius
 *
 *   Type: UF_PARAM_type_vla_length
 *
 *   Name: Step Corner Radii Array 
 *  Variable Name: <prefix>_step_corner_radii_array
 *
 *   Possible Values: UF_PARAM_type_vla_length
 *                    array of double (size = 20)
 *
 * 
 */
#define UF_PARAM_TL_STEP_RADIUS_ARRAY   1194 


/* UF_PARAM_TL_SHOULDER_DISTANCE
 *
 *  Description:
 *  The parameter indicates the Shoulder Distance on a Step/Combination
 *  Drill. 
 *
 *  Type: UF_PARAM_type_length
 *
 *  Name: Shoulder Distance 
 *  Variable Name: <prefix>_shoulder_distance
 *
 *  Possible Values:
 *        UF_PARAM_type_length
 *
 * 
 */
#define UF_PARAM_TL_SHOULDER_DISTANCE   1195   


/* UF_PARAM_CLR_PLANE
 *
 *  Description:
 *  This index is the tag of the clearane plane entity (actually the
 *    XFORM that defines the plane)
 *
 *  Type:  UF_PARAM_type_tag
 *
 *  Name:  Clearance Plane
 *  Variable Name: <prefix>_clearance_plane
 *
 *  Possible Values:
 *         0 (no entity)
 *         entity value
 *
 * 
 */
#define UF_PARAM_CLR_PLANE   1200 


/* UF_PARAM_LOWER_LIMIT_PLANE
 *
 *  Description:
 *  This index is the tag of the lower limit plane entity
 *
 *  Type:  UF_PARAM_type_tag
 *
 *  Name:  Lower Limit Plane
 *  Variable Name: <prefix>_lower_limit_plane
 *
 *  Possible Values:
 *         0 (no entity)
 *         entity value
 *
 * 
 */
#define UF_PARAM_LOWER_LIMIT_PLANE   1201 


/* UF_PARAM_TLAXIS_VECTOR
 *
 *  Description:
 *  This index is the tag of the tool axis vector
 *
 *  Type:  UF_PARAM_type_tag
 *
 *  Name:  Tool Axis Vector
 *  Variable Name: <prefix>_tool_axis_vector
 *
 *  Possible Values:
 *         0 (no entity)
 *         entity value
 *
 * 
 */
#define UF_PARAM_TLAXIS_VECTOR   1202 


/* UF_PARAM_START_POINT
 *
 *  Description:
 *  This index is the tag of the start_point
 *
 *  Type:  UF_PARAM_type_tag
 *
 *  Name:  Start point
 *  Variable Name: <prefix>_start_point
 *
 *  Possible Values:
 *         0 (no entity)
 *         entity value
 *
 * 
 */
#define UF_PARAM_START_POINT   1203 


/* UF_PARAM_RETURN_POINT
 *
 *  Description:
 *  This index is the tag of the return point
 *
 *  Type:  UF_PARAM_type_tag
 *
 *  Name:  Return Point
 *  Variable Name: <prefix>_return_point
 *
 *  Possible Values:
 *         0 (no entity)
 *         entity value
 *
 * 
 */
#define UF_PARAM_RETURN_POINT   1204 


/* UF_PARAM_FROM_POINT
 *
 *  Description:
 *  This index is the tag of the FROM point
 *
 *  Type:  UF_PARAM_type_tag
 *
 *  Name:  FROM Point
 *  Variable Name: <prefix>_from_point
 *
 *  Possible Values:
 *         0 (no entity)
 *         entity value
 *
 * 
 */
#define UF_PARAM_FROM_POINT   1205 


/* UF_PARAM_GOHOME_POINT
 *
 *  Description:
 *  This index is the tag of the GOHOME point
 *
 *  Type:  UF_PARAM_type_tag
 *
 *  Name:  GOHOME Point
 *  Variable Name: <prefix>_gohome_point
 *
 *  Possible Values:
 *         0 (no entity)
 *         entity value
 *
 * 
 */
#define UF_PARAM_GOHOME_POINT   1206 


/* UF_PARAM_ENGAGE_POINT
 *
 *  Description:
 *  This index is the tag of the engage point entity
 *
 *  Type:  UF_PARAM_type_tag
 *
 *  Name:  Engage Point
 *  Variable Name: <prefix>_engage_point
 *
 *  Possible Values:
 *         0 (no entity)
 *         entity value
 *
 * 
 */
#define UF_PARAM_ENGAGE_POINT   1207 


/* UF_PARAM_ENGAGE_PLANE
 *
 *  Description:
 *  This index is the tag of the engage plane
 *
 *  Type:  UF_PARAM_type_tag
 *
 *  Name:  Engage Plane
 *  Variable Name: <prefix>_engage_plane
 *
 *  Possible Values:
 *         0 (no entity)
 *         entity value
 *
 * 
 */
#define UF_PARAM_ENGAGE_PLANE   1208 


/* UF_PARAM_ENGAGE_VECTOR
 *
 *  Description:
 *  This index is the tag of the engage vector
 *
 *  Type:  UF_PARAM_type_tag
 *
 *  Name:  Engage Vector
 *  Variable Name: <prefix>_engage_vector
 *
 *  Possible Values:
 *         0 (no entity)
 *         entity value
 *
 * 
 */
#define UF_PARAM_ENGAGE_VECTOR   1209 


/* UF_PARAM_RETRACT_POINT
 *
 *  Description:
 *  This index is the tag of the retract point
 *
 *  Type:  UF_PARAM_type_tag
 *
 *  Name:  Retract Point
 *  Variable Name: <prefix>_retract_point
 *
 *  Possible Values:
 *         0 (no entity)
 *         entity value
 *
 * 
 */
#define UF_PARAM_RETRACT_POINT   1210 


/* UF_PARAM_RETRACT_PLANE
 *
 *  Description:
 *  This index is the tag of the retract plane
 *
 *  Type:  UF_PARAM_type_tag
 *
 *  Name:  Retract Plane
 *  Variable Name: <prefix>_retract_plane
 *
 *  Possible Values:
 *         0 (no entity)
 *         entity value
 *
 * 
 */
#define UF_PARAM_RETRACT_PLANE   1211 


/* UF_PARAM_RETRACT_VECTOR
 *
 *  Description:
 *  This index is the tag of the retract vector
 *
 *  Type:  UF_PARAM_type_tag
 *
 *  Name:  Retract Vector
 *  Variable Name: <prefix>_retract_vector
 *
 *  Possible Values:
 *         0 (no entity)
 *         entity value
 *
 * 
 */
#define UF_PARAM_RETRACT_VECTOR   1212 


/* UF_PARAM_PROJECTION_VECTOR
 *
 *  Description:
 *  This index is the tag of the projection vector
 *
 *  Type:  UF_PARAM_type_tag
 *
 *  Name:  Projection Vector
 *  Variable Name: <prefix>_projection_vector
 *
 *  Possible Values:
 *         0 (no entity)
 *         entity value
 *
 * 
 */
#define UF_PARAM_PROJECTION_VECTOR   1213 


/* UF_PARAM_MATERIAL_SIDE_VECTOR
 *
 *  Description:
 *  This index is the tag of the material side vector
 *
 *  Type:  UF_PARAM_type_tag
 *
 *  Name:  Material Side Vector
 *  Variable Name: <prefix>_material_side_vector
 *
 *  Possible Values:
 *         0 (no entity)
 *         entity value
 *
 * 
 */
#define UF_PARAM_MATERIAL_SIDE_VECTOR   1214 


/* UF_PARAM_FROM_TOOL_AXIS
 *
 *  Description:
 *  This index is the tag of the FROM point's tool axis
 *
 *  Type:  UF_PARAM_type_tag
 *
 *  Name:  FROM Tool Axis
 *  Variable Name: <prefix>_from_tool_axis
 *
 *  Possible Values:
 *         0 (no entity)
 *         entity value
 *
 * 
 */
#define UF_PARAM_FROM_TOOL_AXIS   1215 


/* UF_PARAM_GOHOME_TOOL_AXIS
 *
 *  Description:
 *  This index is the tag of the GOHOME point's tool axis
 *
 *  Type:  UF_PARAM_type_tag
 *
 *  Name:  GOHOME Tool Axis
 *  Variable Name: <prefix>_gohome_tool_axis
 *
 *  Possible Values:
 *         0 (no entity)
 *         entity value
 *
 * 
 */
#define UF_PARAM_GOHOME_TOOL_AXIS   1216 


/* UF_PARAM_STEPOVER_VAR_DISTS_TOOL_DEPENDENT
 *
 *   Description:
 *      Tool dependent values of stepover size for stepover type = variable,
 *      This index is used instead of UF_PARAM_STEPOVER_VAR_DISTS.
 *
 *   Type: UF_PARAM_type_vla_length_composite
 *
 *   Name: Stepover Variable Tool Dependent Values
 *  Variable Name: <prefix>_stepover_variable_tool_dependent_values
 *
 *   Possible Values: UF_PARAM_type_vla_length_composite
 *                    array of double (size = 6)
 *
 * 
 */
#define UF_PARAM_STEPOVER_VAR_DISTS_TOOL_DEPENDENT   1690  /* UF_PARAM_type_vla_length_composite, size 6 */


/* UF_PARAM_TURN_CUT_DEPTH_ARRAY_TOOL_DEPENDENT
 *
 *   Description:
 *      Tool dependent values of individual stepover for turn roughing,
 *      This index is used instead of UF_PARAM_TURN_CUT_DEPTH_ARRAY.
 *
 *   Type: UF_PARAM_type_vla_length_composite
 *
 *   Name: Tool Dependent Cut Depth Array
 *  Variable Name: <prefix>_tool_dependent_cut_depth_array
 *
 *   Possible Values: UF_PARAM_type_vla_length_composite
 *                    array of double (size = 10)
 *
 * 
 */
#define UF_PARAM_TURN_CUT_DEPTH_ARRAY_TOOL_DEPENDENT   1691  /* UF_PARAM_type_vla_length_composite, size 10 */


/* UF_PARAM_TURN_FINISH_CUT_DEPTH_ARRAY_TOOL_DEPENDENT
 *
 *   Description:
 *      Tool dependent values of individual Cut Depth increments for turn finish/profiling,
 *      This index is used instead of UF_PARAM_TURN_FINISH_CUT_DEPTH_ARRAY.
 *
 *   Type: UF_PARAM_type_vla_length_composite
 *
 *   Name: Tool Dependent Turn Finish Cut Depth Array
 *  Variable Name: <prefix>_tool_dependent_turn_finish_cut_depth_array
 *
 *   Possible Values: UF_PARAM_type_vla_length_composite
 *                    array of double (size = 10)
 *
 * 
 */
#define UF_PARAM_TURN_FINISH_CUT_DEPTH_ARRAY_TOOL_DEPENDENT   1692  /* UF_PARAM_type_vla_length_composite, size 10 */


/* UF_PARAM_TTDOPR_VARIABLE_INCREMENT_TOOL_DEPENDENT
 *
 *   Description:
 *      Tool dependent values of individual Cut Depth increments for thread turning,
 *      This index is used instead of UF_PARAM_TTDOPR_VARIABLE_INCREMENT.
 *
 *   Type: UF_PARAM_type_vla_length_composite
 *
 *   Name: Tool Dependent Thread Turning Cut Depth Array
 *  Variable Name: <prefix>_tool_dependent_thread_turning_cut_depth_array
 *
 *   Possible Values: UF_PARAM_type_vla_length_composite
 *                    array of double (size = 6)
 *
 * 
 */
#define UF_PARAM_TTDOPR_VARIABLE_INCREMENT_TOOL_DEPENDENT   1693  /* UF_PARAM_type_vla_length_composite, size 6 */


typedef enum
{
    UF_PARAM_dpm_proj_type_fixed = 1,
    UF_PARAM_dpm_proj_type_toolaxis,
    UF_PARAM_dpm_proj_type_awaypt,
    UF_PARAM_dpm_proj_type_towardpt,
    UF_PARAM_dpm_proj_type_awayline,
    UF_PARAM_dpm_proj_type_towardline,
    UF_PARAM_dpm_proj_type_ruling,
    UF_PARAM_dpm_proj_type_normdrive,
    UF_PARAM_dpm_proj_type_user_defined,
    UF_PARAM_dpm_proj_type_towarddrive

} UF_PARAM_dpm_proj_type_t;


/* UF_PARAM_DPM_PROJ_TYPE
 *
 *   Description:
 *      This parameters specifies DPM projection type
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Project Type
 *  Variable Name: <prefix>_project_type
 *
 *   Possible Values: UF_PARAM_dpm_proj_type_t
 *
 * 
 */
#define UF_PARAM_DPM_PROJ_TYPE   1700  /* Param_type_int */


/* UF_PARAM_DPM_PROJ_VEC
 *
 *   Description:
 *      Parameter is projection vector in absolute
 *      coordinates, used in DPM projection methods
 *
 *   Type: UF_PARAM_type_3d
 *
 *   Name: Project Vector
 *  Variable Name: <prefix>_project_vector
 *
 *   Possible Values: UF_PARAM_type_3d
 *
 * 
 */
#define UF_PARAM_DPM_PROJ_VEC   1701  /* Param_type_3d */


/* UF_PARAM_DPM_PROJ_POINT
 *
 *   Description:
 *      Parameter is point of projection in absolute
 *      coordinates, used in DPM projection methods
 *
 *   Type: UF_PARAM_type_3d_length
 *
 *   Name: Project Point
 *  Variable Name: <prefix>_project_point
 *
 *   Possible Values: UF_PARAM_type_3d_length
 *
 *
 * 
 */
#define UF_PARAM_DPM_PROJ_POINT   1702  /* Param_type_3d_length */


/* UF_PARAM_DPM_PROJ_DIR
 *
 *   Description:
 *      Parameter is direction of projection in absolute
 *      coordinates, used in DPM projection methods
 *
 *   Type: UF_PARAM_type_3d
 *
 *   Name: Project Direction
 *  Variable Name: <prefix>_project_direction
 *
 *   Possible Values: UF_PARAM_type_3d
 *
 *
 * 
 */
#define UF_PARAM_DPM_PROJ_DIR   1703  /* Param_type_3d */


/* UF_PARAM_DPM_STEPOVER_MAX
 *
 *   Description:
 *      Parameter is maximum stepover allowed
 *
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Stepover Max
 *  Variable Name: <prefix>_stepover_max
 *
 *   Possible Values: double >0.0
 *
 *
 * 
 */
#define UF_PARAM_DPM_STEPOVER_MAX   1706  /* Param_type_double_length */


/* UF_PARAM_DPM_STEPOVER_MIN
 *
 *   Description:
 *      Parameter is minimum stepover allowed
 *
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Stepover Min
 *  Variable Name: <prefix>_stepover_min
 *
 *   Possible Values: double >0.0
 *
 *
 * 
 */
#define UF_PARAM_DPM_STEPOVER_MIN   1707  /* Param_type_double_length */


/* UF_PARAM_DPM_STEPOVER_NUM
 *
 *   Description:
 *      This parameters specifies DPM Stepover Number
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Stepover Number
 *  Variable Name: <prefix>_stepover_number
 *
 *   Possible Values:
 *                integer >0
 *
 *
 * 
 */
#define UF_PARAM_DPM_STEPOVER_NUM   1712 


typedef enum
{
    UF_PARAM_dpm_cut_pattern_none         = 0,
    UF_PARAM_dpm_cut_pattern_zig_zag      = 1,
    UF_PARAM_dpm_cut_pattern_zig          = 2,
    UF_PARAM_dpm_cut_pattern_zig_contour  = 3,

    UF_PARAM_dpm_cut_pattern_follow       = 4,
    UF_PARAM_dpm_cut_pattern_profile      = 5,
    UF_PARAM_dpm_cut_pattern_drive_curve  = 6,

    UF_PARAM_dpm_cut_pattern_zig_zag_lift = 7,
    UF_PARAM_dpm_cut_pattern_zig_stepover = 8,

    UF_PARAM_dpm_cut_pattern_concentric   = 9,
    UF_PARAM_dpm_cut_pattern_radial       = 10,

    UF_PARAM_dpm_cut_pattern_radial_zig_zag      = 11,
    UF_PARAM_dpm_cut_pattern_radial_zig          = 12,
    UF_PARAM_dpm_cut_pattern_radial_zig_contour  = 13,
    UF_PARAM_dpm_cut_pattern_radial_zig_stepover = 14,

    UF_PARAM_dpm_cut_pattern_concentric_zig_zag      = 15,
    UF_PARAM_dpm_cut_pattern_concentric_zig          = 16,
    UF_PARAM_dpm_cut_pattern_concentric_zig_contour  = 17,
    UF_PARAM_dpm_cut_pattern_concentric_zig_stepover = 18,

    UF_PARAM_dpm_cut_pattern_radial_zig_zag_lift      = 19,
    UF_PARAM_dpm_cut_pattern_helical = 30

} UF_PARAM_dpm_cut_pattern_t;


/* UF_PARAM_DPM_CUT_PATTERN
 *
 *   Description:
 *      This parameters specifies DPM Cut Pattern
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Cut Pattern
 *  Variable Name: <prefix>_cut_pattern
 *
 *   Possible Values: UF_PARAM_dpm_cut_pattern_t
 *
 * 
 */
#define UF_PARAM_DPM_CUT_PATTERN   1713 


/* UF_PARAM_REGION_TOLS
 *
 *   Description:
 *      This parameters specifies Region Inside and Outside Tolerances
 *
 *   Type: UF_PARAM_type_2d_length
 *
 *   Name: Region Tolerances
 *  Variable Name: <prefix>_region_tolerances
 *
 *   Possible Values: Positive doubles
 *
 * 
 */
#define UF_PARAM_REGION_TOLS   1715 


/* UF_PARAM_FINISH_PASS
 *
 *   Description:
 *      This parameter for the boundary method (dpmbd) specifies if a Finish Pass
 *      is to be applied to the part.
 *
 *   Type: UF_PARAM_type_logical
 *
 *   Name: DPMBD Finish Pass
 *  Variable Name: <prefix>_dpmbd_finish_pass
 *
 *   Possible Values:
 *               true  -not apply
 *               false -apply
 *
 * 
 */
#define UF_PARAM_FINISH_PASS   1728  /* Param_type_logical */


typedef enum
{
    UF_PARAM_part_contain_off,
    UF_PARAM_part_contain_largest_loop,
    UF_PARAM_part_contain_all_loops

} UF_PARAM_part_contain_t;


/* UF_PARAM_ENTIRE_PART
 *
 *   Description:
 *      This parameter specifies an option for part containment.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: DPMBD Entire Part
 *  Variable Name: <prefix>_dpmbd_entire_part
 *
 *   Possible Values: UF_PARAM_part_contain_t
 *
 * 
 */
#define UF_PARAM_ENTIRE_PART   1729  /* Param_type_int */


/* UF_PARAM_CUSTOM_START
 *
 *   Description:
 *      This parameter specifies if custom start points are to be used.
 *
 *   Type: UF_PARAM_type_logical
 *
 *   Name: Custom Start
 *  Variable Name: <prefix>_custom_start
 *
 *   Possible Values:
 *                false-automatic
 *                true-custom
 *
 * 
 */
#define UF_PARAM_CUSTOM_START   1730  /* Param_type_logical */


/* UF_PARAM_DISP_TOOL_END
 *
 *   Description:
 *      This parameter specifies that the cut region display is represented by the
 *      tool end.
 *
 *   Type: UF_PARAM_type_logical
 *
 *   Name: DPMBD Display Tool End
 *  Variable Name: <prefix>_dpmbd_display_tool_end
 *
 *   Possible Values:
 *                false-not display
 *                true-display
 *
 * 
 */
#define UF_PARAM_DISP_TOOL_END   1731  /* Param_type_logical */


/* UF_PARAM_DISP_TOOL_END_PROJ
 *
 *   Description:
 *      This parameter specifies that the tool end cut region display is
 *      projected onto the boundary plane or a plane normal to the projection
 *      vector.
 *
 *   Type: UF_PARAM_type_logical
 *
 *   Name: DPMBD Display Tool End Proj
 *  Variable Name: <prefix>_dpmbd_display_tool_end_proj
 *
 *   Possible Values:
 *                false-not display
 *                true-display
 *
 * 
 */
#define UF_PARAM_DISP_TOOL_END_PROJ   1732  /* Param_type_logical */


/* UF_PARAM_DISP_CONTACT
 *
 *   Description:
 *      This parameter specifies that the cut region display is represented by the
 *      contact points.
 *
 *   Type: UF_PARAM_type_logical
 *
 *   Name: DPMBD Display Contact
 *  Variable Name: <prefix>_dpmbd_display_contact
 *
 *   Possible Values:
 *                false-not display
 *                true-display
 *
 * 
 */
#define UF_PARAM_DISP_CONTACT   1733  /* Param_type_logical */


/* UF_PARAM_DISP_CONTACT_NORMAL
 *
 *   Description:
 *      This parameter specifies that contact normals will be displayed along the
 *      contact boundary of the cut region.
 *
 *   Type: UF_PARAM_type_logical
 *
 *   Name: DPMBD Display Contact Normal
 *  Variable Name: <prefix>_dpmbd_display_contact_normal
 *
 *   Possible Values:
 *                false-not display
 *                true-display
 *
 * 
 */
#define UF_PARAM_DISP_CONTACT_NORMAL   1734  /* Param_type_logical */


/* UF_PARAM_START_LIST
 *
 *   Description:
 *      This parameter specifies a pointer to the list of custom start points
 *
 *   Type: UF_PARAM_type_vla_length
 *
 *   Name: DPMBD Start List
 *  Variable Name: <prefix>_dpmbd_start_list
 *
 *   Possible Values:
 *                pointer to a list of start points
 *
 * 
 */
#define UF_PARAM_START_LIST   1735 


/* UF_PARAM_PAT_CENTER
 *
 *   Description:
 *      This parameter specifies a 3d point for the pattern center.
 *
 *   Type: UF_PARAM_type_3d_length
 *
 *   Name: DPMBD Pat Center
 *  Variable Name: <prefix>_dpmbd_pat_center
 *
 *   Possible Values:
 *                double[3]
 *
 * 
 */
#define UF_PARAM_PAT_CENTER   1736  /* Param_type_3d_length */


/* UF_PARAM_AUTO_PAT_CENTER
 *
 *   Description:
 *      This parameter specifies whether to use automatic center pattern.
 *
 *   Type: UF_PARAM_type_logical
 *
 *   Name: DPMBD Auto Pat Center
 *  Variable Name: <prefix>_dpmbd_auto_pat_center
 *
 *   Possible Values:
 *                true -automatic
 *                false-other
 *
 * 
 */
#define UF_PARAM_AUTO_PAT_CENTER   1737  /* Param_type_logical */


/* UF_PARAM_DPMCV_NUM_SEGS
 *
 *   Description:
 *      This parameter specifies the number of segments to use in the drive curve cut
 *      method (dpmcv).
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: DPMCV Num 0f Segs
 *  Variable Name: <prefix>_dpmcv_num_0f_segs
 *
 *   Possible Values:
 *                integer
 *
 * 
 */
#define UF_PARAM_DPMCV_NUM_SEGS   1740  /* Param_type_int */


typedef enum
    {
        UF_PARAM_dpmcv_step_types_undefined = 0,
        UF_PARAM_dpmcv_step_type_points    = 10,
        UF_PARAM_dpmcv_step_type_tolerance = 20
 
    } UF_PARAM_dpmcv_step_type_t;


/* UF_PARAM_DPMCV_STEP_TYPE
 *
 *   Description:
 *      This parameter specifies the step type for the drive curve cut method
 *      (DPMCV).
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: DPMCV Step Type
 *  Variable Name: <prefix>_dpmcv_step_type
 *
 *   Possible Values: UF_PARAM_dpmcv_step_type_t
 *
 * 
 */
#define UF_PARAM_DPMCV_STEP_TYPE   1741  /* Param_type_int */


/* UF_PARAM_DPMCV_STEP_TOL
 *
 *   Description:
 *      This parameter specifies the step tolerance for the drive curve cut
 *      method (dpmcv).
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: DPMCV Step Tolerance
 *  Variable Name: <prefix>_dpmcv_step_tolerance
 *
 *   Possible Values:
 *            double
 *
 * 
 */
#define UF_PARAM_DPMCV_STEP_TOL   1744 


/* UF_PARAM_DPMCV_DATA_TYPE
 *
 *   Description:
 *      When using interpolated tool axis this parameter specifies the type
 *      of data to be interpolated in the drive curve cut method (dpmcv).
 *
 *      If the data type is vector then xyz vector data will be associated to
 *      a number of points on the drive curve and interpolated.
 *
 *      If the data is angle then pairs of angles representing lead and tilt
 *      will be associated to a number of points on the drive curve. These
 *      angle pairs will be interpolated. When the tool is projected to the part
 *      then the tool axis will be determined.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: DPMCV Data Type
 *  Variable Name: <prefix>_dpmcv_data_type
 *
 *   Possible Values:
 *            0-vector interpolation
 *            1-angle interpolation
 *
 * 
 */
#define UF_PARAM_DPMCV_DATA_TYPE   1745  /* Param_type_int */


/* UF_PARAM_DPMCV_INTERPOLATION_METHOD
 *
 *   Description:
 *      When using interpolation this parameter specifies the method
 *      of interpolation in the drive curve cut method (dpmcv).
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: DPMCV Interpolation Method
 *  Variable Name: <prefix>_dpmcv_interpolation_method
 *
 *   Possible Values:
 *            0-TAXDS_INTP_LINEAR
 *            1-TAXDS_INTP_CUBIC_SPLINE
 *
 * 
 */
#define UF_PARAM_DPMCV_INTERPOLATION_METHOD   1746  /* Param_type_int */


typedef enum
    {
        UF_PARAM_dpmrc_bnd_dir_forward,
        UF_PARAM_dpmrc_bnd_dir_backward
    } UF_PARAM_dpmrc_bnd_dir_t;


/* UF_PARAM_DPMRC_BOUNDARY_DIR
 *
 *   Description:
 *      This parameter specifies the boundary direction in the radial cut drive method
 *      (dpmrc).
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: DPMRC Boundary Dir
 *  Variable Name: <prefix>_dpmrc_boundary_dir
 *
 *   Possible Values: UF_PARAM_dpmrc_bnd_dir_t
 *
 * 
 */
#define UF_PARAM_DPMRC_BOUNDARY_DIR   1751  /* Param_type_int */


/* UF_PARAM_DPMRC_BOUNDARY_RIGHT
 *
 *   Description:
 *      This parameter specifies how far the radial cut goes to the right side of
 *      the boundary in the radial cut drive method (dpmrc). This may also
 *      be called the right side band width.
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: DPMRC Boundary Right
 *  Variable Name: <prefix>_dpmrc_boundary_right
 *
 *   Possible Values:
 *             double
 *
 * 
 */
#define UF_PARAM_DPMRC_BOUNDARY_RIGHT   1753 


/* UF_PARAM_DPMRC_BOUNDARY_LEFT
 *
 *   Description:
 *      This parameter specifies how far the radial cut goes to the left side of
 *      the boundary in the radial cut drive method (dpmrc). This may also
 *      be called the left side band width.
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: DPMRC Boundary Left
 *  Variable Name: <prefix>_dpmrc_boundary_left
 *
 *   Possible Values:
 *             double
 *
 * 
 */
#define UF_PARAM_DPMRC_BOUNDARY_LEFT   1754 


/* UF_PARAM_SC_MAX_STEP_PERC
 *
 *   Description:
 *      This parameter specifies the maximum step as a percentage of
 *      the tool diameter.
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Max step as percentage of tool
 *  Variable Name: <prefix>_max_step_as_percentage_of_tool
 *
 *   Possible Values:
 *             double
 *
 * 
 */
#define UF_PARAM_SC_MAX_STEP_PERC   1755  /* UF_PARAM_type_double */


typedef enum
{
    UF_PARAM_bnd_diagonal_pts = 10,
    UF_PARAM_bnd_grid_percent = 20

} UF_PARAM_bnd_method_t;


/* UF_PARAM_BND_METHOD
 *
 *  Description:
 *      This index specifies the boundary method for setting the cut area
 *
 *  Type:  UF_PARAM_type_int
 *
 *  Name: Surface Drive Cut Area Method
 *  Variable Name: <prefix>_surface_drive_cut_area_method
 *
 *  Possible Values: UF_PARAM_bnd_method_t
 *
 * 
 */
#define UF_PARAM_BND_METHOD   1756  /* UF_PARAM_type_int */


/* UF_PARAM_CUT_PERC 
 * 
 *  Description: 
 *       This index specifies the cut percentages of the cut area 
 *
 *  Type: UF_PARAM_type_vla_real 
 * 
 *  Name: Surface Percentages 
 *  Variable Name: <prefix>_surface_percentages
 * 
 *  Possible Values:  double array [6] 
 * 
 * 
 */ 
#define UF_PARAM_CUT_PERC   1757   /* UF_PARAM_type_vla_real */ 


typedef enum
{
    UF_PARAM_cut_uv_dir_undefined         =       0, 
    UF_PARAM_cut_uv_dir_posU              =       1, 
    UF_PARAM_cut_uv_dir_negU              =       2, 
    UF_PARAM_cut_uv_dir_posV              =       3, 
    UF_PARAM_cut_uv_dir_negV              =       4 
 
}UF_PARAM_cut_uv_dir_t;


/* UF_PARAM_CUT_UV_DIR 
 * 
 *  Description: 
 *      This index specifies the cut direction of drive path 
 *  in UV space. 
 * 
 *  Type: UF_PARAM_type_int 
 * 
 *  Name: Surface UV Direction 
 *  Variable Name: <prefix>_surface_uv_direction
 * 
 *  Possible Values: UF_PARAM_cut_uv_dir_t
 * 
 * 
 */
#define UF_PARAM_CUT_UV_DIR   1758   /* UF_PARAM_type_int */ 


typedef enum
{
    UF_PARAM_step_type_points          =       10, 
    UF_PARAM_step_type_tolerance       =       20 
 
}UF_PARAM_step_type_t;


/* UF_PARAM_STEP_METHOD 
 * 
 *  Description: 
 *      This index specifies the step method of drive path.
 * 
 *  Type: UF_PARAM_type_int 
 * 
 *  Name: Step Method 
 *  Variable Name: <prefix>_step_method
 * 
 *  Possible Values: UF_PARAM_step_type_t
 * 
 * 
 */ 
#define UF_PARAM_STEP_METHOD   1759   /* UF_PARAM_type_int */ 


/* UF_PARAM_STEP_POINTS 
 * 
 *  Description: 
 *      This index specifies the step points (step and stepover parameters) of drive path.
 *      This index is only valid for the Surface Area Drive Method and
 *        UF_PARAM_STEP_METHOD = UF_PARAM_step_type_points and
 *        UF_PARAM_STEPOVER_TYPE = UF_PARAM_stepover_type_number.
 * 
 *  Type: UF_PARAM_type_vla_int 
 * 
 *  Name: Step Points 
 *  Variable Name: <prefix>_step_points
 * 
 *  Possible Values:  int array [5]
 *
 *    For UF_PARAM_DPM_CUT_PATTERN = UF_PARAM_dpm_cut_pattern_follow
 *
 *        [0] = Number of first cut points
 *        [1] = Number of second cut points
 *        [2] = Number of third and subsequent cut points
 *        [3] = Number of stepovers in first direction
 *        [4] = Number of stepovers in second direction
 *
 *    For UF_PARAM_DPM_CUT_PATTERN = all other values
 *
 *        [0] = Number of first cut points
 *        [1] = Number of last cut points
 *        [2] = Number of stepovers
 * 
 * 
 */ 
#define UF_PARAM_STEP_POINTS   1760   /* UF_PARAM_type_vla_int */ 


/* UF_PARAM_STEP_INTOL 
 * 
 *  Description: 
 *      This index specifies the cut step intol of drive path 
 * 
 *  Type: UF_PARAM_type_double_length 
 * 
 *  Name: Step Intol 
 *  Variable Name: <prefix>_step_intol
 * 
 *  Possible Values:  Positive double 
 * 
 * 
 */ 
#define UF_PARAM_STEP_INTOL   1761   /* UF_PARAM_type_double_length */ 


/* UF_PARAM_STEP_OUTTOL 
 * 
 *  Description: 
 *      This index specifies the cut step outtol of drive path 
 * 
 *  Type: UF_PARAM_type_double_length 
 * 
 *  Name: Step Outtol 
 *  Variable Name: <prefix>_step_outtol
 * 
 *  Possible Values:  Positive double 
 * 
 * 
 */ 
#define UF_PARAM_STEP_OUTTOL   1762   /* UF_PARAM_type_double_length */ 


typedef enum
{
    UF_PARAM_tool_posi_on_same     =       1, 
    UF_PARAM_tool_posi_on_opp      =       2, 
    UF_PARAM_tool_posi_tanto_same  =       3, 
    UF_PARAM_tool_posi_tanto_opp   =       4,
    UF_PARAM_tool_posi_contact     =       5
 
}UF_PARAM_tool_posi_t;


/* UF_PARAM_TOOL_POSITION 
 * 
 *  Description: 
 *      This index specifies the tool position of drive path 
 *       
 *  Type: UF_PARAM_type_int 
 * 
 *  Name: Tool Position 
 *  Variable Name: <prefix>_tool_position
 * 
 *  Possible Values: UF_PARAM_dpmsa_tool_posi_t
 * 
 * 
 */ 
#define UF_PARAM_TOOL_POSITION   1763   /* UF_PARAM_type_int */ 


/* UF_PARAM_STOCK_DRIVE_GEOM 
 * 
 *  Description: 
 *      This index specifies the stock for drive geometry.
 * 
 *  Type: UF_PARAM_type_double_length 
 * 
 *  Name: Drive Geometry Stock 
 *  Variable Name: <prefix>_drive_geometry_stock
 * 
 *  Possible Values: double 
 * 
 * 
 */ 
#define UF_PARAM_STOCK_DRIVE_GEOM   1764   /* UF_PARAM_type_double_length */ 


typedef enum
{
    UF_PARAM_stepover_uv_dir_undefined         =       0, 
    UF_PARAM_stepover_uv_dir_posU              =       1, 
    UF_PARAM_stepover_uv_dir_negU              =       2, 
    UF_PARAM_stepover_uv_dir_posV              =       3, 
    UF_PARAM_stepover_uv_dir_negV              =       4  
 
} UF_PARAM_stepover_uv_dir_t;


/* UF_PARAM_STEPOVER_UV_DIR 
 * 
 *  Description: 
 *      This index specifies the stepover direction of drive path 
 *  in UV space.
 * 
 *  Type: UF_PARAM_type_int 
 * 
 *  Name: Stepover UV Direction 
 *  Variable Name: <prefix>_stepover_uv_direction
 * 
 *  Possible Values: UF_PARAM_stepover_uv_dir_t
 * 
 * 
 */ 
#define UF_PARAM_STEPOVER_UV_DIR   1765   /* UF_PARAM_type_int */ 


/* UF_PARAM_HORIZONAL_LIMIT 
 * 
 *  Description: 
 *      This index specifies the horizontal limit for stepover of drive path 
 * 
 *  Type: UF_PARAM_type_double_length 
 * 
 *  Name: Horizontal Limit 
 *  Variable Name: <prefix>_horizontal_limit
 * 
 *  Possible Values:  double 
 * 
 * 
 */ 
#define UF_PARAM_HORIZONAL_LIMIT   1766   /* UF_PARAM_type_double_length */ 


/* UF_PARAM_VERTICAL_LIMIT 
 * 
 *  Description: 
 *      This index specifies the vertical limit for stepover of drive path 
 * 
 *  Type: UF_PARAM_type_double_length 
 * 
 *  Name: Vertical Limit 
 *  Variable Name: <prefix>_vertical_limit
 * 
 *  Possible Values:  double 
 * 
 * 
 */ 
#define UF_PARAM_VERTICAL_LIMIT   1767   /* UF_PARAM_type_double_length */ 


typedef enum
{
    UF_PARAM_drive_avoid_none,
    UF_PARAM_drive_avoid_warning,
    UF_PARAM_drive_avoid_stepover,
    UF_PARAM_drive_avoid_lift

} UF_PARAM_drive_avoid_type_t;


/* UF_PARAM_DRIVE_AVOIDANCE 
 * 
 *  Description:
 *      This parameter specifies the action to be taken when a gouge of the
 *  drive surface is detected by the processor.
 *
 *  Type: UF_PARAM_type_int 
 * 
 *  Name: Drive Avoidance 
 *  Variable Name: <prefix>_drive_avoidance
 * 
 *  Possible Values: UF_PARAM_drive_avoid_type_t
 * 
 * 
 */ 
#define UF_PARAM_DRIVE_AVOIDANCE   1777   /* UF_PARAM_type_int */ 


/* UF_PARAM_DPMSA_DATA_TYPE 
 * 
 *  Description: 
 *      This index specifies the interpolation data type 
 *  of the Surface Countoring surface area method (dpmsa).
 * 
 *  Type: UF_PARAM_type_int 
 * 
 *  Name: Surface Drive Data Type 
 *  Variable Name: <prefix>_surface_drive_data_type
 * 
 *  Possible Values: int 
 * 
 * 
 */ 
#define UF_PARAM_DPMSA_DATA_TYPE   1778   /* UF_PARAM_type_int */ 


/* UF_PARAM_DPMSA_INTERPOLATION_METHOD 
 * 
 *  Description: 
 *      This index specifies the interpolation method 
 *  of the Surface Countoring surface area method (dpmsa).
 * 
 *  Type: UF_PARAM_type_int 
 * 
 *  Name: Surface Drive Interpolation Method 
 *  Variable Name: <prefix>_surface_drive_interpolation_method
 * 
 *  Possible Values: int 
 * 
 * 
 */ 
#define UF_PARAM_DPMSA_INTERPOLATION_METHOD   1779   /* UF_PARAM_type_int */ 


typedef enum
{
     UF_PARAM_steep_contain_none,
     UF_PARAM_non_steep_non_directional,
     UF_PARAM_steep_directional

} UF_PARAM_steep_opt_t;



/* UF_PARAM_STEEP_OPT
 *
 *  Description:
 *      This parameter specifies a steep containment option for an operation.
 *
 *  Type: UF_PARAM_type_int
 *
 *  Name: Steep Option
 *  Variable Name: <prefix>_steep_option
 *
 *  Possible Values: UF_PARAM_steep_opt_t
 *             
 * 
 */
#define UF_PARAM_STEEP_OPT   1780  /* UF_PARAM_type_int */ 


typedef enum
{
     UF_PARAM_swarf_ruling_type_grid_or_trim,
     UF_PARAM_swarf_ruling_type_uv

} UF_PARAM_swarf_ruling_type_t;



/* UF_PARAM_SWARF_RULING_TYPE
 *
 *  Description:
 *      This parameter specifies an option for swarf cutting.
 *
 *  Type: UF_PARAM_type_int
 *
 *  Name: SWARF RULING TYPE
 *  Variable Name: <prefix>_swarf_ruling_type
 *
 *  Possible Values: UF_PARAM_swarf_ruling_type_t
 *
 * 
 */
#define UF_PARAM_SWARF_RULING_TYPE   1785  /* UF_PARAM_type_int */


/* UF_PARAM_AUTO_WALL_SELECTION 
 * 
 *  Description: 
 *       This index specifies whether the automatic wall selection is specified.
 * 
 *  Type: UF_PARAM_type_logical 
 * 
 *  Name: Automatic Wall Selection 
 *  Variable Name: <prefix>_automatic_wall_selection
 * 
 *  Possible Values: logical 
 * 
 * 
 */ 
#define UF_PARAM_AUTO_WALL_SELECTION   1786   /* UF_PARAM_type_logical */ 


/* UF_PARAM_START_CUT_FACE 
 * 
 *  Description: 
 *      This index specifies the start cut face.
 * 
 *  Type: UF_PARAM_type_tag 
 * 
 *  Name: Start Cut Face 
 *  Variable Name: <prefix>_start_cut_face
 * 
 *  Possible Values: tag
 * 
 * 
 */ 
#define UF_PARAM_START_CUT_FACE   1787   /* UF_PARAM_type_tag */ 


/* UF_PARAM_START_CUT_UV 
 * 
 *  Description: 
 *      This index specifies the start cut UV parameters.
 * 
 *  Type: UF_PARAM_type_2d 
 * 
 *  Name: Start Cut UV 
 *  Variable Name: <prefix>_start_cut_uv
 * 
 *  Possible Values:  double[2] 
 * 
 * 
 */ 
#define UF_PARAM_START_CUT_UV   1788   /* UF_PARAM_type_2d */ 


/* UF_PARAM_DPMUD_ENV_VAR_NAME 
 * 
 *  Description: 
 *      This index specifies the environment variable name 
 *  of the Surface Countoring user-defined method (dpmud).
 * 
 *  Type: UF_PARAM_type_string 
 * 
 *  Name: User Defined Drive Env Var Name
 *  Variable Name: <prefix>_user_defined_drive_env_var_name
 * 
 *  Possible Values:  char[45] 
 * 
 * 
 */ 
#define UF_PARAM_DPMUD_ENV_VAR_NAME   1792   /* UF_PARAM_type_string */ 


/* UF_PARAM_DPMUD_ENTRY_PT_NAME 
 * 
 *  Description: 
 *      This index specifies the entry point name 
 *  of the Surface Countoring user-defined method (dpmud).
 * 
 *  Type: UF_PARAM_type_string 
 * 
 *  Name: User Defined Drive Entry Point Name
 *  Variable Name: <prefix>_user_defined_drive_entry_point_name
 * 
 *  Possible Values:  char[7] 
 * 
 * 
 */ 
#define UF_PARAM_DPMUD_ENTRY_PT_NAME   1793   /* UF_PARAM_type_string */ 


/* UF_PARAM_WITH_RADIUS 
 * 
 *  Description: 
 *      This index specifies the flag indicating if maximum radius is used in 
 *  spiral cut pattern.
 * 
 *  Type: UF_PARAM_type_logical 
 * 
 *  Name: With Radius
 *  Variable Name: <prefix>_with_radius
 * 
 *  Possible Values:  logical 
 * 
 * 
 */ 
#define UF_PARAM_WITH_RADIUS   1794   /* UF_PARAM_type_logical */ 


/* UF_PARAM_SPIRAL_RADIUS 
 * 
 *  Description: 
 *      This index specifies the maximum radius of the circle.
 * 
 *  Type: UF_PARAM_type_double_length 
 * 
 *  Name: Spiral Radius
 *  Variable Name: <prefix>_spiral_radius
 * 
 *  Possible Values:  double 
 * 
 * 
 */ 
#define UF_PARAM_SPIRAL_RADIUS   1795   /* UF_PARAM_type_double_length */ 


/* UF_PARAM_SPIRAL_CENTER 
 * 
 *  Description: 
 *      This index specifies the center point of the spiral pattern.
 * 
 *  Type: UF_PARAM_type_3d_length 
 * 
 *  Name: Spiral Center
 *  Variable Name: <prefix>_spiral_center
 * 
 *  Possible Values: double[3] 
 * 
 * 
 */ 
#define UF_PARAM_SPIRAL_CENTER   1796   /* UF_PARAM_type_3d_length */ 


/* UF_PARAM_END_CUT_FACE
 *
 *  Description:
 *      This index specifies the end cut face.
 *
 *  Type: UF_PARAM_type_tag
 *
 *  Name: End Cut Face
 *  Variable Name: <prefix>_end_cut_face
 *
 *  Possible Values: tag
 *
 * 
 */
#define UF_PARAM_END_CUT_FACE   1797   /* UF_PARAM_type_tag */


/* UF_PARAM_END_CUT_UV
 *
 *  Description:
 *      This index specifies the end cut UV parameters.
 *
 *  Type: UF_PARAM_type_2d
 *
 *  Name: End Cut UV
 *  Variable Name: <prefix>_end_cut_uv
 *
 *  Possible Values:  double[2]
 *
 * 
 */
#define UF_PARAM_END_CUT_UV   1798   /* UF_PARAM_type_2d */


/* UF_PARAM_SWARF_TILT_ANGLE
 *
 *  Description:
 *      This parameter specifies an option for swarf cutting.
 *
 *  Type: UF_PARAM_type_double
 *
 *  Name: SWARF TILT ANGLE
 *  Variable Name: <prefix>_swarf_tilt_angle
 *
 *  Possible Values: 0.0
 *
 * 
 */
#define UF_PARAM_SWARF_TILT_ANGLE   1799  /* UF_PARAM_type_double */


typedef enum UF_PARAM_engage_type_e
{
    UF_PARAM_engage_type_undefined = -1,
    UF_PARAM_engage_type_auto_circular = 0,
    UF_PARAM_engage_type_auto_linear = 1,
    UF_PARAM_engage_type_vector = 2,
    UF_PARAM_engage_type_angle_distance = 3,
    UF_PARAM_engage_type_rel_linear = 4,
    UF_PARAM_engage_type_point = 5,
    UF_PARAM_engage_type_two_circles = 6,
    UF_PARAM_engage_type_2pt_tang = 7

} UF_PARAM_engage_type_t;


/* UF_PARAM_ENGAGE_TYPE
 *
 *   Description:
 *      For turning teachmode operations, this parameter defines the type
 *      of the engage motion.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Engage Type
 *  Variable Name: <prefix>_engage_type
 *
 *   Possible Values: UF_PARAM_engage_type_t
 *
 * 
 *
 */
#define UF_PARAM_ENGAGE_TYPE   1809 


typedef enum UF_PARAM_retract_type_e
{
    UF_PARAM_retract_type_undefined = -1,
    UF_PARAM_retract_type_auto_circular = 0,
    UF_PARAM_retract_type_auto_linear = 1,
    UF_PARAM_retract_type_vector = 2,
    UF_PARAM_retract_type_angle_distance = 3,
    UF_PARAM_retract_type_rel_linear = 4,
    UF_PARAM_retract_type_point = 5,
    UF_PARAM_retract_type_two_circles = 6,
    UF_PARAM_retract_type_2pt_tang = 7

} UF_PARAM_retract_type_t;


/* UF_PARAM_RETRACT_TYPE
 *
 *   Description:
 *      For turning teachmode operations, this parameter defines the type
 *      of the retract motion.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Retract Type
 *  Variable Name: <prefix>_retract_type
 *
 *   Possible Values: UF_PARAM_retract_type_t
 *
 * 
 *
 */
#define UF_PARAM_RETRACT_TYPE   1816 


/* UF_PARAM_MINIMUM_CORNER_FILLET_RADIUS
 *
 *   Description:
 *      Paramter is the smalled permitted radius of a corner fillet.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Minimum Corner Fillet Path Radius
 *  Variable Name: <prefix>_minimum_corner_fillet_path_radius
 *
 *   Possible Values: positive UF_PARAM_type_double_length.
 *
 * 
 */
#define UF_PARAM_MINIMUM_CORNER_FILLET_RADIUS   1824  /* UF_PARAM_type_int */


typedef enum UF_PARAM_gouge_checking_flag_e
{
    UF_PARAM_gouge_checking_flag_off = 0,
    UF_PARAM_gouge_checking_flag_on = 1

} UF_PARAM_gouge_checking_flag_t;


/* UF_PARAM_GOUGE_CHECKING_FLAG
 *
 *   Description:
 *      Paramter is used to perform gouge checking during 
 *      generation of a tool path.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Gouge Checking Flag
 *  Variable Name: <prefix>_gouge_checking_flag
 *
 *   Possible Values: UF_PARAM_gouge_checking_flag_t
 *
 * 
 */
#define UF_PARAM_GOUGE_CHECKING_FLAG   1825  /* UF_PARAM_type_int */


/* UF_PARAM_CUSTOM_END
 *
 *  Description:
 *      This parameter specifies if custom end points are to be used.
 *
 *  Type: UF_PARAM_type_logical
 *
 *  Name: Custom End
 *  Variable Name: <prefix>_custom_end
 *
 *  Possible Values:
 *                false-automatic
 *                true-custom
 *
 * 
 */
#define UF_PARAM_CUSTOM_END   1826  /* Param_type_logical */


/* UF_PARAM_MULTI_WALL_PASSES
 *
 *  Description:
 *      This parameter specifies if custom wall multiple passes are to be used.
 *
 *  Type: UF_PARAM_type_logical
 *
 *  Name: Multiple wall passes
 *  Variable Name: <prefix>_multiple_wall_passes
 *
 *  Possible Values:
 *                false (default)
 *                true-custom
 *
 * 
 */
#define UF_PARAM_MULTI_WALL_PASSES   1827  /* Param_type_logical */


/* UF_PARAM_WALL_STOCK_OFFSET
 *
 *  Description:
 *      This parameter specifies the custom wall stock offset.
 *
 *  Type: UF_PARAM_type_double_length
 *
 *  Name: Wall stock offset
 *  Variable Name: <prefix>_wall_stock_offset
 *
 *  Possible Values:
 *                0.0 -- default
 *                positive number
 *
 * 
 */
#define UF_PARAM_WALL_STOCK_OFFSET   1828  /* Param_type_double_length */


/* UF_PARAM_WALL_STEP_METHOD
 *
 *  Description:
 *      This parameter specifies the custom wall step method.
 *
 *  Type: UF_PARAM_type_int
 *
 *  Name: Wall step method 
 *  Variable Name: <prefix>_wall_step_method
 *
 *  Possible Values:
 *      UF_PARAM_wall_step_method_flag_increment --- increment (default)
 *      UF_PARAM_wall_step_method_flag_num_passes --- number of passes
 *
 * 
 */
#define UF_PARAM_WALL_STEP_METHOD   1829  /* Param_type_int */


/* UF_PARAM_WALL_INCREMENT
 *
 *  Description:
 *      This parameter specifies the custom wall increment of stocks.
 *
 *  Type: UF_PARAM_type_double_length
 *
 *  Name: Wall increment 
 *  Variable Name: <prefix>_wall_increment
 *
 *  Possible Values:
 *                0.0 -- default
 *                positive number
 *
 * 
 */
#define UF_PARAM_WALL_INCREMENT   1830  /* Param_type_double_length */


/* UF_PARAM_WALL_NUMBER_PASSES
 *
 *  Description:
 *      This parameter specifies the custom wall number of passes.
 *
 *  Type: UF_PARAM_type_int
 *
 *  Name: Wall number passes 
 *  Variable Name: <prefix>_wall_number_passes
 *
 *  Possible Values:
 *                0 --- default
 *                positive integer
 *
 * 
 */
#define UF_PARAM_WALL_NUMBER_PASSES   1831  /* Param_type_int */


/* UF_PARAM_MULTIPASS_ORDER
 *
 *  Description:
 *      This parameter specifies the order of multiple passes.
 *
 *  Type: UF_PARAM_type_int
 *
 *  Name: Multipass order 
 *  Variable Name: <prefix>_multipass_order
 *
 *  Possible Values:
 *      UF_PARAM_multipass_order_wall_first --- wall first (default)
 *      UF_PARAM_multipass_order_floor_first --- floor first
 *
 * 
 */
#define UF_PARAM_MULTIPASS_ORDER   1832  /* Param_type_int */


/* UF_PARAM_MULTI_FLOOR_PASSES
 *
 *  Description:
 *      This parameter specifies if custom floor multiple passes are to be used.
 *
 *  Type: UF_PARAM_type_logical
 *
 *  Name: Multiple floor passes
 *  Variable Name: <prefix>_multiple_floor_passes
 *
 *  Possible Values:
 *                false (default)
 *                true-custom
 *
 * 
 */
#define UF_PARAM_MULTI_FLOOR_PASSES   1833  /* Param_type_logical */


/* UF_PARAM_START_EXT_DIST_TYPE
 *
 *  Description:
 *      This parameter specifies start extension distance type
 *
 *  Type: UF_PARAM_type_int
 *
 *  Name: Start ext distance type
 *  Variable Name: <prefix>_start_ext_distance_type
 *
 *  Possible Values:
 *     UF_PARAM_start_ext_dist_type_spec --- specified value
 *     UF_PARAM_start_ext_dist_type_tool --- percentage of tool diameter
 *
 * 
 */
#define UF_PARAM_START_EXT_DIST_TYPE   1834  /* Param_type_int */


/* UF_PARAM_START_EXT_DIST_SPEC_VALUE
 *
 *  Description:
 *      This parameter specifies start extension distance specified value
 *
 *  Type: UF_PARAM_type_double_length
 *
 *  Name: Start ext distance specified value
 *  Variable Name: <prefix>_start_ext_distance_specified_value
 *
 *  Possible Values:
 *                0.5 (default) --- specified value
 *
 * 
 */
#define UF_PARAM_START_EXT_DIST_SPEC_VALUE   1835  /* Param_type_double_length */


/* UF_PARAM_END_EXT_DIST_TYPE
 *
 *  Description:
 *      This parameter specifies end extension distance type
 *
 *  Type: UF_PARAM_type_int
 *
 *  Name: End ext distance type
 *  Variable Name: <prefix>_end_ext_distance_type
 *
 *  Possible Values:
 *     UF_PARAM_end_ext_dist_type_spec --- specified value
 *     UF_PARAM_end_ext_dist_type_tool --- percentage of tool diameter
 *
 * 
 */
#define UF_PARAM_END_EXT_DIST_TYPE   1836  /* Param_type_int */


/* UF_PARAM_END_EXT_DIST_SPEC_VALUE
 *
 *  Description:
 *      This parameter specifies end extension distance specified value
 *
 *  Type: UF_PARAM_type_double_length
 *
 *  Name: End ext distance specified value
 *  Variable Name: <prefix>_end_ext_distance_specified_value
 *
 *  Possible Values:
 *                0.5 (default) --- specified value
 *
 * 
 */
#define UF_PARAM_END_EXT_DIST_SPEC_VALUE   1837  /* Param_type_double_length */


/* UF_PARAM_START_EXT_DIST_USAGE
 * 
 *  Description: 
 *       This parameter specifies if the extension of the start of cut is to be used.
 *
 *  Type: UF_PARAM_type_int
 *
 *  Name: Extend
 *  Variable Name: <prefix>_extend
 *
 *  Possible Values:
 *                0 (default)
 *                1 extended
 *
 * 
 */ 
#define UF_PARAM_START_EXT_DIST_USAGE   1839   /* Param_type_logical */ 


/* UF_PARAM_END_EXT_DIST_USAGE
 * 
 *  Description: 
 *       This parameter specifies if the extension of the end of cut is to be used.
 *
 *  Type: UF_PARAM_type_int
 *
 *  Name: Extend
 *  Variable Name: <prefix>_extend
 *
 *  Possible Values:
 *                0 (default)
 *                1 extended
 *
 * 
 */ 
#define UF_PARAM_END_EXT_DIST_USAGE   1840   /* Param_type_logical */ 


typedef enum
{
    UF_PARAM_mct_turret_wpl_type_x_y = 0,
    UF_PARAM_mct_turret_wpl_type_z_x = 1
}UF_PARAM_mct_turret_wpl_type_t;

/* UF_PARAM_MCT_TURRET_WPL_TYPE
 *
 *   Description:
 *      Parameter defines the plane of workplane
 *      coordinate system to be designated as
 *      The carrier's Lathe Work Plane (either XY or ZX).
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Carrier Workplane Type
 *  Variable Name: <prefix>_carrier_workplane_type
 *
 *   Possible Values: UF_PARAM_mct_turret_wpl_type_t
 *
 * 
 */
#define UF_PARAM_MCT_TURRET_WPL_TYPE   2011 


/* UF_PARAM_MCT_TURRET_WPL_TAG
 *
 *   Description:
 *      Parameter defines the orientation of the
 *      carrier's work plane by a coordinate system.
 *
 *   Type: UF_PARAM_type_tag (References CSYSTEM_xform object)
 *
 *   Name: Carrier Workplane Tag
 *  Variable Name: <prefix>_carrier_workplane_tag
 *
 *   Possible Values: valid CSYSTEM_xform tag
 *
 * 
 */
#define UF_PARAM_MCT_TURRET_WPL_TAG   2012 


/* UF_PARAM_MCT_CHANNEL_ID
 *
 *  Description:
 *      This parameter specifies the current output channel
 *
 *  Type: UF_PARAM_type_string
 *
 *  Name: Channel ID
 *  Variable Name: <prefix>_channel_id
 *
 *   Possible Values:
 *
 * 
 */
#define UF_PARAM_MCT_CHANNEL_ID   2033  /* Param_type_string */


/* UF_PARAM_MCT_ALL_CHANNEL_IDS
 *
 *  Description:
 *      This parameter specifies all channels which can control the device
 *
 *  Type: UF_PARAM_type_vla_string
 *
 *  Name: All Channel IDS
 *  Variable Name: <prefix>_all_channel_ids
 *
 *   Possible Values:
 *
 * 
 */
#define UF_PARAM_MCT_ALL_CHANNEL_IDS   2034  /* Param_type_vla_string */


typedef enum
{
    UF_PARAM_tool_preNX2_contact_data_2D = -1,
    UF_PARAM_tool_centerline_data = 0,
    UF_PARAM_tool_contact_data_2D = 1,
    UF_PARAM_tool_contact_data_3D = 2
}UF_PARAM_cutter_data_output_type_t;

/* UF_PARAM_CUTTER_DATA_OUTPUT
 *
 *   Description:
 *      Indicates to the processor the type of cutter data to output to
 *      the tool path.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Cutter data output indicator
 *  Variable Name: <prefix>_cutter_data_output_indicator
 *
 *   Possible Values: UF_PARAM_cutter_data_output_type_t
 *
 * 
 */
#define UF_PARAM_CUTTER_DATA_OUTPUT   2401 


typedef enum
{
    UF_PARAM_contact_point = 0,
    UF_PARAM_user_defined_point = 1
}UF_PARAM_tracking_point_type_t;

/* UF_PARAM_TRACKING_POINT_TYPE
 *
 *   Description:
 *      Indicates the type of tracking point active for 
 *      the operation.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Active tracking point type indicator
 *  Variable Name: <prefix>_active_tracking_point_type_indicator
 *
 *   Possible Values: UF_PARAM_tracking_point_type_t
 *
 * 
 */
#define UF_PARAM_TRACKING_POINT_TYPE   2402 


/* UF_PARAM_TURN_DWELL_FLAG
 *
 *   Description:
 *      This parameter controls the activation of Dwell after Rough cut.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Dwell Flag
 *  Variable Name: <prefix>_dwell_flag
 *
 *   Possible Values: 
 *     0 = inactive
 *     1 = active
 *
 * 
 */
#define UF_PARAM_TURN_DWELL_FLAG   2500  /* Param_type_int */


/* UF_PARAM_TURN_DWELL
 *
 *   Description:
 *      This parameter controls the dwell time. It represents the time in
 *      seconds or the number of revolutions based on the setting of the
 *      dwell units parameter.
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Dwell
 *  Variable Name: <prefix>_dwell
 *
 *   Possible Values: 
 *     positive double (don't use decimals for revolutions)
 *
 * 
 */
#define UF_PARAM_TURN_DWELL   2501  /* UF_PARAM_type_double */


typedef enum UF_PARAM_turn_dwell_unit_e
{
    UF_PARAM_turn_dwell_unit_seconds = 0,
    UF_PARAM_turn_dwell_unit_revolutions
} UF_PARAM_turn_dwell_unit_t;

/* UF_PARAM_TURN_DWELL_UNIT
 *
 *   Description:
 *      This parameter controls whether dwell is using seconds or revolutions.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Dwell Unit
 *  Variable Name: <prefix>_dwell_unit
 *
 *   Possible Values: UF_PARAM_turn_dwell_unit_t
 *
 * 
 */
#define UF_PARAM_TURN_DWELL_UNIT   2502 


/* UF_PARAM_TURN_DWELL_TOG
 *
 *   Description:
 *      This parameter activates/deactivates dwell for centerline drilling.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Dwell Toggle
 *  Variable Name: <prefix>_dwell_toggle
 *
 *   Possible Values: 
 *     0 = inactive
 *     1 = active
 *
 * 
 */
#define UF_PARAM_TURN_DWELL_TOG   2503  /* UF_PARAM_type_int */


typedef enum UF_PARAM_turn_displ_coll_e
{
    UF_PARAM_turn_displ_coll_inactive_insert_only = 0,
    UF_PARAM_turn_displ_coll_active_insert_only,
    UF_PARAM_turn_displ_coll_inactive_insert_and_holder,
    UF_PARAM_turn_displ_coll_active_insert_and_holder
} UF_PARAM_turn_displ_coll_t, *UF_PARAM_turn_displ_coll_p_t;


/* UF_PARAM_TURN_DISPL_COLL_TOG
 *
 *   Description:
 *      This parameter controls the visual representation of collisions
 *      in turning operations. That's rapid motions where the insert
 *      or insert & holder gouges the actual in-process workpiece.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Display Collisions
 *  Variable Name: <prefix>_display_collisions
 *
 *   Possible Values: UF_PARAM_turn_displ_coll_t
 *
 * 
 */
#define UF_PARAM_TURN_DISPL_COLL_TOG   2504  /* UF_PARAM_type_int */


/* UF_PARAM_TURN_ENG_RET_MIN_DIST
 *
 *   Description:
 *      Specifies the minimum length of automatic linear engage and
 *      retract motions for all turning operations. For automatic
 *      circular engage and retract it defines the minimum radius.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Minimum Eng Ret Distance
 *  Variable Name: <prefix>_minimum_eng_ret_distance
 *
 *   Possible Values: double
 *
 * 
 */
#define UF_PARAM_TURN_ENG_RET_MIN_DIST   2505  /* UF_PARAM_type_double_length */


typedef enum
{
    UF_PARAM_turn_avoidance_start_mode_point = 0,
    UF_PARAM_turn_avoidance_start_mode_delta
} UF_PARAM_turn_avoidance_start_mode_t;

/* UF_PARAM_TURN_AVOIDANCE_START_MODE
 *
 *  Description:
 *     This parameter defines how the start point coordinates are defined.
 *
 *  Type: UF_PARAM_type_int
 *
 *  Name: Turn Avoidance Start Mode
 *  Variable Name: <prefix>_turn_avoidance_start_mode
 *
 *  Possible Values: UF_PARAM_turn_avoidance_start_mode_t
 *
 * 
 */
#define UF_PARAM_TURN_AVOIDANCE_START_MODE   2508 


typedef enum
{
    UF_PARAM_turn_avoidance_return_mode_point = 0,
    UF_PARAM_turn_avoidance_return_mode_delta,
    UF_PARAM_turn_avoidance_return_mode_same_as_start
} UF_PARAM_turn_avoidance_return_mode_t;

/* UF_PARAM_TURN_AVOIDANCE_RETURN_MODE
 *
 *  Description:
 *     This parameter defines how the return point coordinates are defined.
 *
 *  Type: UF_PARAM_type_int
 *
 *  Name: Turn Avoidance Return Mode
 *  Variable Name: <prefix>_turn_avoidance_return_mode
 *
 *  Possible Values: UF_PARAM_turn_avoidance_return_mode_t
 *
 * 
 */
#define UF_PARAM_TURN_AVOIDANCE_RETURN_MODE   2509 


typedef enum
{
    UF_PARAM_turn_avoidance_gohome_mode_point = 0,
    UF_PARAM_turn_avoidance_gohome_mode_same_as_from
} UF_PARAM_turn_avoidance_gohome_mode_t;


/* UF_PARAM_TURN_AVOIDANCE_GOHOME_MODE
 *
 *  Description:
 *     This parameter defines how the gohome point coordinates are defined.
 *
 *  Type: UF_PARAM_type_int
 *
 *  Name: Turn Avoidance Gohome Mode
 *  Variable Name: <prefix>_turn_avoidance_gohome_mode
 *
 *  Possible Values: UF_PARAM_turn_avoidance_gohome_mode_t
 *
 * 
 */
#define UF_PARAM_TURN_AVOIDANCE_GOHOME_MODE   2510 


typedef enum
{
    UF_PARAM_turn_avoidance_departure_mode_points = 0,
    UF_PARAM_turn_avoidance_departure_mode_same_as_approach,
    UF_PARAM_turn_avoidance_departure_mode_points_before_tool_change,
    UF_PARAM_turn_avoidance_departure_mode_same_as_approach_before_tool_change
} UF_PARAM_turn_avoidance_departure_mode_t;


/* UF_PARAM_TURN_AVOIDANCE_DEPARTURE_MODE
 *
 *  Description:
 *     This parameter defines how the departure point coordinates are defined.
 *
 *  Type: UF_PARAM_type_int
 *
 *  Name: Turn Avoidance Departure Mode
 *  Variable Name: <prefix>_turn_avoidance_departure_mode
 *
 *  Possible Values: UF_PARAM_turn_avoidance_departure_mode_t
 *
 * 
 */
#define UF_PARAM_TURN_AVOIDANCE_DEPARTURE_MODE   2511 


typedef enum
{
    UF_PARAM_turn_avoidance_delta_type_angle_distance = 0,
    UF_PARAM_turn_avoidance_delta_type_delta_move,
    UF_PARAM_turn_avoidance_delta_type_vector_distance
} UF_PARAM_turn_avoidance_delta_type_t;

/* UF_PARAM_TURN_AVOIDANCE_START_DELTA_TYPE
 *
 *  Description:
 *     This parameter defines how the start point delta is defined.
 *
 *  Type: UF_PARAM_type_int
 *
 *  Name: Turn Avoidance Start Delta Type
 *  Variable Name: <prefix>_turn_avoidance_start_delta_type
 *
 *  Possible Values: UF_PARAM_turn_avoidance_delta_type_t
 *
 * 
 */
#define UF_PARAM_TURN_AVOIDANCE_START_DELTA_TYPE   2512 


/* UF_PARAM_TURN_AVOIDANCE_START_ANGLE_TAG
 *
 *   Description:
 *      This parameter holds the object ID of a vector referencing
 *      the angle for the start point distance definition.
 *
 *   Type: UF_PARAM_type_tag
 *
 *   Name: Turn Avoidance Start Angle Tag
 *  Variable Name: <prefix>_turn_avoidance_start_angle_tag
 *
 *   Possible Values: UF_PARAM_type_tag
 *
 * 
 */
#define UF_PARAM_TURN_AVOIDANCE_START_ANGLE_TAG   2513 


/* UF_PARAM_TURN_AVOIDANCE_START_ANGLE_VALUE
 *
 *  Description:
 *      This parameter holds the a manually entered angle for the 
 *      start point distance definition.
 *      The parameter is only valid if 
 *      UF_PARAM_TURN_AVOIDANCE_START_ANGLE_TAG equals to NULL_TAG.
 *
 *  Type: UF_PARAM_type_double
 *
 *  Name: Turn Avoidance Start Angle Value
 *  Variable Name: <prefix>_turn_avoidance_start_angle_value
 *
 *  Possible Values: double
 *
 * 
 */
#define UF_PARAM_TURN_AVOIDANCE_START_ANGLE_VALUE   2514 


/* UF_PARAM_TURN_AVOIDANCE_START_DISTANCE
 *
 *  Description:
 *      This parameter holds the distance for the start point distance
 *      definition.
 *
 *  Type: UF_PARAM_type_double_length
 *
 *  Name: Turn Avoidance Start Distance
 *  Variable Name: <prefix>_turn_avoidance_start_distance
 *
 *  Possible Values: double
 *
 * 
 */
#define UF_PARAM_TURN_AVOIDANCE_START_DISTANCE   2515 


/* UF_PARAM_TURN_AVOIDANCE_START_DELTA_X
 *
 *  Description:
 *      This parameter holds the X coordinate for the start point distance
 *      definition.
 *
 *  Type: UF_PARAM_type_double_length
 *
 *  Name: Turn Avoidance Start Delta X
 *  Variable Name: <prefix>_turn_avoidance_start_delta_x
 *
 *  Possible Values: double
 *
 * 
 */
#define UF_PARAM_TURN_AVOIDANCE_START_DELTA_X   2516 


/* UF_PARAM_TURN_AVOIDANCE_START_DELTA_Y
 *
 *  Description:
 *      This parameter holds the Y coordinate for the start point distance
 *      definition.
 *
 *  Type: UF_PARAM_type_double_length
 *
 *  Name: Turn Avoidance Start Delta Y
 *  Variable Name: <prefix>_turn_avoidance_start_delta_y
 *
 *  Possible Values: double
 *
 * 
 */
#define UF_PARAM_TURN_AVOIDANCE_START_DELTA_Y   2517 


/* UF_PARAM_TURN_AVOIDANCE_RETURN_DELTA_TYPE
 *
 *  Description:
 *     This parameter defines how the return point delta is defined.
 *
 *  Type: UF_PARAM_type_int
 *
 *  Name: Turn Avoidance Return Delta Type
 *  Variable Name: <prefix>_turn_avoidance_return_delta_type
 *
 *  Possible Values: UF_PARAM_turn_avoidance_delta_type_t
 *
 * 
 */
#define UF_PARAM_TURN_AVOIDANCE_RETURN_DELTA_TYPE   2518 


/* UF_PARAM_TURN_AVOIDANCE_RETURN_ANGLE_TAG
 *
 *   Description:
 *      This parameter holds the object ID of a vector referencing
 *      the angle for the return point distance definition.
 *
 *   Type: UF_PARAM_type_tag
 *
 *   Name: Turn Avoidance Return Angle Tag
 *  Variable Name: <prefix>_turn_avoidance_return_angle_tag
 *
 *   Possible Values: UF_PARAM_type_tag
 *
 * 
 */
#define UF_PARAM_TURN_AVOIDANCE_RETURN_ANGLE_TAG   2519 


/* UF_PARAM_TURN_AVOIDANCE_RETURN_ANGLE_VALUE
 *
 *  Description:
 *      This parameter holds the a manually entered angle for the 
 *      return point distance definition.
 *      The parameter is only valid if 
 *      UF_PARAM_TURN_AVOIDANCE_RETURN_ANGLE_TAG equals to NULL_TAG.
 *
 *  Type: UF_PARAM_type_double
 *
 *  Name: Turn Avoidance Return Angle Value
 *  Variable Name: <prefix>_turn_avoidance_return_angle_value
 *
 *  Possible Values: double
 *
 * 
 */
#define UF_PARAM_TURN_AVOIDANCE_RETURN_ANGLE_VALUE   2520 


/* UF_PARAM_TURN_AVOIDANCE_RETURN_DISTANCE
 *
 *  Description:
 *      This parameter holds the distance for the return point distance
 *      definition.
 *
 *  Type: UF_PARAM_type_double_length
 *
 *  Name: Turn Avoidance Return Distance
 *  Variable Name: <prefix>_turn_avoidance_return_distance
 *
 *  Possible Values: double
 *
 * 
 */
#define UF_PARAM_TURN_AVOIDANCE_RETURN_DISTANCE   2521 


/* UF_PARAM_TURN_AVOIDANCE_RETURN_DELTA_X
 *
 *  Description:
 *      This parameter holds the X coordinate for the return point distance
 *      definition.
 *
 *  Type: UF_PARAM_type_double_length
 *
 *  Name: Turn Avoidance Return Delta X
 *  Variable Name: <prefix>_turn_avoidance_return_delta_x
 *
 *  Possible Values: double
 *
 * 
 */
#define UF_PARAM_TURN_AVOIDANCE_RETURN_DELTA_X   2522 


/* UF_PARAM_TURN_AVOIDANCE_RETURN_DELTA_Y
 *
 *  Description:
 *      This parameter holds the Y coordinate for the return point distance
 *      definition.
 *
 *  Type: UF_PARAM_type_double_length
 *
 *  Name: Turn Avoidance Return Delta Y
 *  Variable Name: <prefix>_turn_avoidance_return_delta_y
 *
 *  Possible Values: double
 *
 * 
 */
#define UF_PARAM_TURN_AVOIDANCE_RETURN_DELTA_Y   2523 


/* UF_PARAM_TURN_AVOIDANCE_APPROACH_STATUS
 *
 *  Description:
 *      Activates the Avoidance Approach path.
 *
 *  Type: UF_PARAM_type_int
 *
 *  Name: Turn Avoidance Approach Status
 *  Variable Name: <prefix>_turn_avoidance_approach_status
 *
 *  Possible Values: 0 -- off
 *                   1 -- on
 *                   2 -- on, but only after tool change
 *
 * 
 */
#define UF_PARAM_TURN_AVOIDANCE_APPROACH_STATUS   2524 


/* UF_PARAM_TURN_AVOIDANCE_DEPARTURE_STATUS
 *
 *  Description:
 *      Activates the Avoidance Departure path.
 *
 *  Type: UF_PARAM_type_int
 *
 *  Name: Turn Avoidance Departure Status
 *  Variable Name: <prefix>_turn_avoidance_departure_status
 *
 *  Possible Values: 0 -- off
 *                   1 -- on
 *
 * 
 */
#define UF_PARAM_TURN_AVOIDANCE_DEPARTURE_STATUS   2525 


typedef enum
{
    UF_PARAM_turn_avoidance_path_cs_mode_wcs = 0,
    UF_PARAM_turn_avoidance_path_cs_mode_mcs
} UF_PARAM_turn_avoidance_path_cs_mode_t;

/* UF_PARAM_TURN_APPROACH_PATH_CS_MODE
 *
 *  Description:
 *      Holds coordinate system modeffor displaying the 
 *      approach path points coordinates.
 *
 *  Type: UF_PARAM_type_int
 *
 *  Name: Turn Approach Path CS Mode
 *  Variable Name: <prefix>_turn_approach_path_cs_mode
 *
 *  Possible Values: UF_PARAM_turn_avoidance_path_cs_mode_t
 *
 * 
 */
#define UF_PARAM_TURN_APPROACH_PATH_CS_MODE   2526 


/* UF_PARAM_TURN_APPROACH_PATH_NO_OF_POINTS
 *
 *  Description:
 *      Holds the number of approach path point.
 *
 *  Type: UF_PARAM_type_int
 *
 *  Name: Turn Approach Path No Of Points
 *  Variable Name: <prefix>_turn_approach_path_no_of_points
 *
 *  Possible Values: positive number or zero
 *
 * 
 */
#define UF_PARAM_TURN_APPROACH_PATH_NO_OF_POINTS   2527 


/* UF_PARAM_TURN_APPROACH_PATH_FLAGS
 *
 *  Description:
 *      Activates the points in the approach path.
 *      The array has the maximum element number
 *      MAX_NO_OF_AVOIDANCE_PATH_POINTS.
 *
 *  Type: UF_PARAM_type_vla_int
 *
 *  Name: Turn Approach Path Flags
 *  Variable Name: <prefix>_turn_approach_path_flags
 *
 *  Possible Values: 0 -- off
 *                   1 -- on
 *
 * 
 */
#define UF_PARAM_TURN_APPROACH_PATH_FLAGS   2528 


typedef enum
{
    UF_PARAM_turn_approach_path_method_direct = 0,
    UF_PARAM_turn_approach_path_method_radial_then_axial,
    UF_PARAM_turn_approach_path_method_axial_then_radial
} UF_PARAM_turn_approach_path_method_t;

/* UF_PARAM_TURN_APPROACH_PATH_METHODS
 *
 *  Description:
 *      Defines the strategy how the tool is moved to the
 *      approach points.
 *      The array has the maximum element number
 *      MAX_NO_OF_AVOIDANCE_PATH_POINTS.
 *
 *  Type: UF_PARAM_type_vla_int
 *
 *  Name: Turn Approach Path Methods
 *  Variable Name: <prefix>_turn_approach_path_methods
 *
 *  Possible Values: UF_PARAM_turn_approach_path_method_t
 *
 * 
 */
#define UF_PARAM_TURN_APPROACH_PATH_METHODS   2529 


/* UF_PARAM_TURN_APPROACH_PATH_POINTS
 *
 *  Description:
 *      Holds the point tags of the approach path.
 *      The array has the maximum element number
 *      MAX_NO_OF_AVOIDANCE_PATH_POINTS.
 *
 *  Type: UF_PARAM_type_vla_tag
 *
 *  Name: Turn Approach Path Points
 *  Variable Name: <prefix>_turn_approach_path_points
 *
 *  Possible Values: tags
 *
 * 
 */
#define UF_PARAM_TURN_APPROACH_PATH_POINTS   2530 


/* UF_PARAM_TURN_APPROACH_PATH_FEEDRATE_MODES
 *
 *  Description:
 *      Holds the feedrate modes of the approach path.
 *      Mode can be Custom or a predifend feedrate (Rapid,
 *      Approach, Cut, ...).
 *      The predefined feedrate modes can defer depending on
 *      the operation.
 *      The array has the maximum element number
 *      MAX_NO_OF_AVOIDANCE_PATH_POINTS.
 *
 *  Type: UF_PARAM_type_vla_int
 *
 *  Name: Turn Approach Path Feedrate Modes
 *  Variable Name: <prefix>_turn_approach_path_feedrate_modes
 *
 *  Possible Values: positive number or zero
 *
 * 
 */
#define UF_PARAM_TURN_APPROACH_PATH_FEEDRATE_MODES   2531 


/* UF_PARAM_TURN_APPROACH_PATH_CUSTOM_FEEDRATES
 *
 *  Description:
 *      Holds the custom feedrates of the approach path.
 *      This value is only valid if feedrate mode
 *      (UF_PARAM_TURN_APPROACH_PATH_FEEDRATE_MODES) is 
 *      Custom.
 *      The array has the maximum element number
 *      MAX_NO_OF_AVOIDANCE_PATH_POINTS.
 *
 *  Type: UF_PARAM_type_vla_double
 *
 *  Name: Turn Approach Path Custom Feedrates
 *  Variable Name: <prefix>_turn_approach_path_custom_feedrates
 *
 *  Possible Values: positive double or zero
 *
 * 
 */
#define UF_PARAM_TURN_APPROACH_PATH_CUSTOM_FEEDRATES   2532 


/* UF_PARAM_TURN_APPROACH_PATH_CUSTOM_FEEDRATE_UNITS
 *
 *  Description:
 *      Holds the custom feedrate units of the approach path.
 *      This value is only valid if feedrate mode
 *      (UF_PARAM_TURN_APPROACH_PATH_FEEDRATE_MODES) is 
 *      Custom.
 *      The array has the maximum element number
 *      MAX_NO_OF_AVOIDANCE_PATH_POINTS.
 *
 *  Type: UF_PARAM_type_vla_int
 *
 *  Name: Turn Approach Path Custom Feedrate Units
 *  Variable Name: <prefix>_turn_approach_path_custom_feedrate_units
 *
 *  Possible Values: FEED_unit_t
 *
 * 
 */
#define UF_PARAM_TURN_APPROACH_PATH_CUSTOM_FEEDRATE_UNITS   2533 


/* UF_PARAM_TURN_APPROACH_PATH_A_AXIS_FLAGS
 *
 *  Description:
 *      Holds the Flip Tool Around Tool Holder (A axis) flags 
 *      of the approach path.
 *      The array has the maximum element number
 *      MAX_NO_OF_AVOIDANCE_PATH_POINTS.
 *
 *  Type: UF_PARAM_type_vla_int
 *
 *  Name: Turn Approach Path A Axis Flags
 *  Variable Name: <prefix>_turn_approach_path_a_axis_flags
 *
 *  Possible Values: 0 -- off
 *                   1 -- on
 *
 * 
 */
#define UF_PARAM_TURN_APPROACH_PATH_A_AXIS_FLAGS   2534 


/* UF_PARAM_TURN_APPROACH_PATH_B_AXIS_FLAGS
 *
 *  Description:
 *      Holds the Reorient Tool Holder (B axis) flags of the 
 *      approach path.
 *      The array has the maximum element number
 *      MAX_NO_OF_AVOIDANCE_PATH_POINTS.
 *
 *  Type: UF_PARAM_type_vla_int
 *
 *  Name: Turn Approach Path B Axis Flags
 *  Variable Name: <prefix>_turn_approach_path_b_axis_flags
 *
 *  Possible Values: 0 -- off
 *                   1 -- on
 *
 * 
 */
#define UF_PARAM_TURN_APPROACH_PATH_B_AXIS_FLAGS   2535 


/* UF_PARAM_TURN_APPROACH_PATH_B_AXIS_ANGLES
 *
 *  Description:
 *      Holds the Reorient Tool Holder (B axis) angles of the 
 *      approach path.
 *      The array has the maximum element number
 *      MAX_NO_OF_AVOIDANCE_PATH_POINTS.
 *
 *  Type: UF_PARAM_type_vla_double
 *
 *  Name: Turn Approach Path B Axis Angles
 *  Variable Name: <prefix>_turn_approach_path_b_axis_angles
 *
 *  Possible Values: double
 *
 * 
 */
#define UF_PARAM_TURN_APPROACH_PATH_B_AXIS_ANGLES   2536 


/* UF_PARAM_TURN_DEPARTURE_PATH_CS_MODE
 *
 *  Description:
 *      Holds coordinate system modeffor displaying the 
 *      departure path points coordinates.
 *
 *  Type: UF_PARAM_type_int
 *
 *  Name: Turn Departure Path CS Mode
 *  Variable Name: <prefix>_turn_departure_path_cs_mode
 *
 *  Possible Values: UF_PARAM_turn_avoidance_path_cs_mode_t
 *
 * 
 */
#define UF_PARAM_TURN_DEPARTURE_PATH_CS_MODE   2537 


/* UF_PARAM_TURN_DEPARTURE_PATH_NO_OF_POINTS
 *
 *  Description:
 *      Holds the number of departure path point.
 *
 *  Type: UF_PARAM_type_int
 *
 *  Name: Turn Departure Path No Of Points
 *  Variable Name: <prefix>_turn_departure_path_no_of_points
 *
 *  Possible Values: positive number or zero
 *
 * 
 */
#define UF_PARAM_TURN_DEPARTURE_PATH_NO_OF_POINTS   2538 


/* UF_PARAM_TURN_DEPARTURE_PATH_FLAGS
 *
 *  Description:
 *      Activates the points in the departure path.
 *      The array has the maximum element number
 *      MAX_NO_OF_AVOIDANCE_PATH_POINTS.
 *
 *  Type: UF_PARAM_type_vla_int
 *
 *  Name: Turn Departure Path Flags
 *  Variable Name: <prefix>_turn_departure_path_flags
 *
 *  Possible Values: 0 -- off
 *                   1 -- on
 *
 * 
 */
#define UF_PARAM_TURN_DEPARTURE_PATH_FLAGS   2539 


typedef enum
{
    UF_PARAM_turn_departure_path_method_automatic = 0,
    UF_PARAM_turn_departure_path_method_direct,
    UF_PARAM_turn_departure_path_method_radial_then_axial,
    UF_PARAM_turn_departure_path_method_axial_then_radial,
    UF_PARAM_turn_departure_path_method_clear_radial_then_direct, /* Last two items are only available for motion to first */
    UF_PARAM_turn_departure_path_method_clear_axial_then_direct   /* departure point, if departure path is locked to appraoch path.  */
} UF_PARAM_turn_departure_path_method_t;

/* UF_PARAM_TURN_DEPARTURE_PATH_METHODS
 *
 *  Description:
 *      Defines the strategy how the tool is moved to the
 *      departure points.
 *      The array has the maximum element number
 *      MAX_NO_OF_AVOIDANCE_PATH_POINTS.
 *
 *  Type: UF_PARAM_type_vla_int
 *
 *  Name: Turn Departure Path Methods
 *  Variable Name: <prefix>_turn_departure_path_methods
 *
 *  Possible Values: UF_PARAM_turn_departure_path_method_t
 *
 * 
 */
#define UF_PARAM_TURN_DEPARTURE_PATH_METHODS   2540 


/* UF_PARAM_TURN_DEPARTURE_PATH_POINTS
 *
 *  Description:
 *      Holds the point tags of the departure path.
 *      The array has the maximum element number
 *      MAX_NO_OF_AVOIDANCE_PATH_POINTS.
 *
 *  Type: UF_PARAM_type_vla_tag
 *
 *  Name: Turn Departure Path Points
 *  Variable Name: <prefix>_turn_departure_path_points
 *
 *  Possible Values: tags
 *
 * 
 */
#define UF_PARAM_TURN_DEPARTURE_PATH_POINTS   2541 


/* UF_PARAM_TURN_DEPARTURE_PATH_FEEDRATE_MODES
 *
 *  Description:
 *      Holds the feedrate modes of the departure path.
 *      Mode can be Custom or a predifend feedrate (Rapid,
 *      Departure, Cut, ...).
 *      The predefined feedrate modes can defer depending on
 *      the operation.
 *      The array has the maximum element number
 *      MAX_NO_OF_AVOIDANCE_PATH_POINTS.
 *
 *  Type: UF_PARAM_type_vla_int
 *
 *  Name: Turn Departure Path Feedrate Modes
 *  Variable Name: <prefix>_turn_departure_path_feedrate_modes
 *
 *  Possible Values: positive number or zero
 *
 * 
 */
#define UF_PARAM_TURN_DEPARTURE_PATH_FEEDRATE_MODES   2542 


/* UF_PARAM_TURN_DEPARTURE_PATH_CUSTOM_FEEDRATES
 *
 *  Description:
 *      Holds the custom feedrates of the departure path.
 *      This value is only valid if feedrate mode
 *      (UF_PARAM_TURN_DEPARTURE_PATH_FEEDRATE_MODES) is 
 *      Custom.
 *      The array has the maximum element number
 *      MAX_NO_OF_AVOIDANCE_PATH_POINTS.
 *
 *  Type: UF_PARAM_type_vla_double
 *
 *  Name: Turn Departure Path Custom Feedrates
 *  Variable Name: <prefix>_turn_departure_path_custom_feedrates
 *
 *  Possible Values: positive double or zero
 *
 * 
 */
#define UF_PARAM_TURN_DEPARTURE_PATH_CUSTOM_FEEDRATES   2543 


/* UF_PARAM_TURN_DEPARTURE_PATH_CUSTOM_FEEDRATE_UNITS
 *
 *  Description:
 *      Holds the custom feedrate units of the departure path.
 *      This value is only valid if feedrate mode
 *      (UF_PARAM_TURN_DEPARTURE_PATH_FEEDRATE_MODES) is 
 *      Custom.
 *      The array has the maximum element number
 *      MAX_NO_OF_AVOIDANCE_PATH_POINTS.
 *
 *  Type: UF_PARAM_type_vla_int
 *
 *  Name: Turn Departure Path Custom Feedrate Units
 *  Variable Name: <prefix>_turn_departure_path_custom_feedrate_units
 *
 *  Possible Values: FEED_unit_t
 *
 * 
 */
#define UF_PARAM_TURN_DEPARTURE_PATH_CUSTOM_FEEDRATE_UNITS   2544 


/* UF_PARAM_TURN_DEPARTURE_PATH_A_AXIS_FLAGS
 *
 *  Description:
 *      Holds the Flip Tool Around Tool Holder (A axis) flags 
 *      of the departure path.
 *      The array has the maximum element number
 *      MAX_NO_OF_AVOIDANCE_PATH_POINTS.
 *
 *  Type: UF_PARAM_type_vla_int
 *
 *  Name: Turn Departure Path A Axis Flags
 *  Variable Name: <prefix>_turn_departure_path_a_axis_flags
 *
 *  Possible Values: 0 -- off
 *                   1 -- on
 *
 * 
 */
#define UF_PARAM_TURN_DEPARTURE_PATH_A_AXIS_FLAGS   2545 


/* UF_PARAM_TURN_DEPARTURE_PATH_B_AXIS_FLAGS
 *
 *  Description:
 *      Holds the Reorient Tool Holder (B axis) flags of the 
 *      departure path.
 *      The array has the maximum element number
 *      MAX_NO_OF_AVOIDANCE_PATH_POINTS.
 *
 *  Type: UF_PARAM_type_vla_int
 *
 *  Name: Turn Departure Path B Axis Flags
 *  Variable Name: <prefix>_turn_departure_path_b_axis_flags
 *
 *  Possible Values: 0 -- off
 *                   1 -- on
 *
 * 
 */
#define UF_PARAM_TURN_DEPARTURE_PATH_B_AXIS_FLAGS   2546 


/* UF_PARAM_TURN_DEPARTURE_PATH_B_AXIS_ANGLES
 *
 *  Description:
 *      Holds the Reorient Tool Holder (B axis) angles of the 
 *      departure path.
 *      The array has the maximum element number
 *      MAX_NO_OF_AVOIDANCE_PATH_POINTS.
 *
 *  Type: UF_PARAM_type_vla_double
 *
 *  Name: Turn Departure Path B Axis Angles
 *  Variable Name: <prefix>_turn_departure_path_b_axis_angles
 *
 *  Possible Values: double
 *
 * 
 */
#define UF_PARAM_TURN_DEPARTURE_PATH_B_AXIS_ANGLES   2547 


typedef enum UF_PARAM_turn_direction_e
{
    UF_PARAM_turn_direction_backward = 0,
    UF_PARAM_turn_direction_forward
} UF_PARAM_turn_direction_t;

/* UF_PARAM_TURN_DIRECTION
 *
 *   Description:
 *      This parameter lets the user revert the cut direction in linear/contour 
 *      roughing operations or the direction of stepover in plunge roughing 
 *      turning operations.
 *      It is interpreted relative to the major direction given thru the level angle
 *      in linear/contour roughing or the step angle in plunge roughing.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Direction
 *  Variable Name: <prefix>_direction
 *
 *   Possible Values: see 'UF_PARAM_turn_direction_t'
 *
 * 
 */
#define UF_PARAM_TURN_DIRECTION   2550  /* Param_type_int */


/* UF_PARAM_TURN_OMIT_REVERSALS
 *
 *   Description:
 *      If this parameter is set activate, reversals will not be cut by the 
 *      respective Turn Roughing/Finishing operation.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Omit Reversals
 *  Variable Name: <prefix>_omit_reversals
 *
 *   Possible Values: 
 *     0 = inactive
 *     1 = active
 *
 * 
 */
#define UF_PARAM_TURN_OMIT_REVERSALS   2553  /* Param_type_int */


/* UF_PARAM_TURN_TRIM_RADIAL1_TOG
 *
 *   Description:
 *      This parameter controls the usage of the first radial containment
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Use First Radial Containment
 *  Variable Name: <prefix>_use_first_radial_containment
 *
 *   Possible Values:
 *     0 = inactive
 *     1 = active
 *
 * 
 */
#define UF_PARAM_TURN_TRIM_RADIAL1_TOG   2555  /* Param_type_int */


/* UF_PARAM_TURN_TRIM_RADIAL1_TAG
 *
 *   Description:
 *      This parameter holds the object ID of a smart point referencing
 *      the position for first radial containment
 *
 *   Type: UF_PARAM_type_tag
 *
 *   Name: First Radial Containment Tag
 *  Variable Name: <prefix>_first_radial_containment_tag
 *
 *   Possible Values: 
 *         0 (no entity)
 *         entity ID
 *
 * 
 */
#define UF_PARAM_TURN_TRIM_RADIAL1_TAG   2556  /* Param_type_tag */


/* UF_PARAM_TURN_TRIM_RADIAL1_VAL
 *
 *   Description:
 *      This parameter describes the radial location for the first
 *      radial containment. It can be set alternatively to the parameter
 *      UF_PARAM_TURN_TRIM_RADIAL1_TAG, if no smart point is used.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: First Radial Containment
 *  Variable Name: <prefix>_first_radial_containment
 *
 *   Possible Values: double
 *
 * 
 */
#define UF_PARAM_TURN_TRIM_RADIAL1_VAL   2557  /* Param_type_double_length */


/* UF_PARAM_TURN_TRIM_RADIAL2_TOG
 *
 *   Description:
 *      This parameter controls the usage of the second radial containment
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Use Second Radial Containment
 *  Variable Name: <prefix>_use_second_radial_containment
 *
 *   Possible Values:
 *     0 = inactive
 *     1 = active
 *
 * 
 */
#define UF_PARAM_TURN_TRIM_RADIAL2_TOG   2558  /* Param_type_int */


/* UF_PARAM_TURN_TRIM_RADIAL2_TAG
 *
 *   Description:
 *      This parameter holds the object ID of a smart point referencing
 *      the position for second radial containment
 *
 *   Type: UF_PARAM_type_tag
 *
 *   Name: Second Radial Containment Tag
 *  Variable Name: <prefix>_second_radial_containment_tag
 *
 *   Possible Values: 
 *         0 (no entity)
 *         entity ID
 *
 * 
 */
#define UF_PARAM_TURN_TRIM_RADIAL2_TAG   2559  /* Param_type_tag */


/* UF_PARAM_TURN_TRIM_RADIAL2_VAL
 *
 *   Description:
 *      This parameter describes the radial location for the second
 *      radial containment. It can be set alternatively to the parameter
 *      UF_PARAM_TURN_TRIM_RADIAL2_TAG, if no smart point is used.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Second Radial Containment
 *  Variable Name: <prefix>_second_radial_containment
 *
 *   Possible Values: double
 *
 * 
 */
#define UF_PARAM_TURN_TRIM_RADIAL2_VAL   2560  /* Param_type_double_length */


/* UF_PARAM_TURN_TRIM_AXIAL1_TOG
 *
 *   Description:
 *      This parameter controls the usage of the first axial containment
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Use First Axial Containment
 *  Variable Name: <prefix>_use_first_axial_containment
 *
 *   Possible Values:
 *     0 = inactive
 *     1 = active
 *
 * 
 */
#define UF_PARAM_TURN_TRIM_AXIAL1_TOG   2561  /* Param_type_int */


/* UF_PARAM_TURN_TRIM_AXIAL1_TAG
 *
 *   Description:
 *      This parameter holds the object ID of a smart point referencing
 *      the position for first axial containment
 *
 *   Type: UF_PARAM_type_tag
 *
 *   Name: First Axial Containment Tag
 *  Variable Name: <prefix>_first_axial_containment_tag
 *
 *   Possible Values: 
 *         0 (no entity)
 *         entity ID
 *
 * 
 */
#define UF_PARAM_TURN_TRIM_AXIAL1_TAG   2562  /* Param_type_tag */


/* UF_PARAM_TURN_TRIM_AXIAL1_VAL
 *
 *   Description:
 *      This parameter describes the radial location for the first
 *      axial containment. It can be set alternatively to the parameter
 *      UF_PARAM_TURN_TRIM_AXIAL1_TAG, if no smart point is used.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: First Axial Containment
 *  Variable Name: <prefix>_first_axial_containment
 *
 *   Possible Values: double
 *
 * 
 */
#define UF_PARAM_TURN_TRIM_AXIAL1_VAL   2563  /* Param_type_double_length */


/* UF_PARAM_TURN_TRIM_AXIAL2_TOG
 *
 *   Description:
 *      This parameter controls the usage of the second axial containment
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Use Second Axial Containment
 *  Variable Name: <prefix>_use_second_axial_containment
 *
 *   Possible Values: 
 *     0 = inactive
 *     1 = active
 *
 * 
 */
#define UF_PARAM_TURN_TRIM_AXIAL2_TOG   2564  /* Param_type_int */


/* UF_PARAM_TURN_TRIM_AXIAL2_TAG
 *
 *   Description:
 *      This parameter holds the object ID of a smart point referencing
 *      the position for second axial containment
 *
 *   Type: UF_PARAM_type_tag
 *
 *   Name: Second Axial Containment Tag
 *  Variable Name: <prefix>_second_axial_containment_tag
 *
 *   Possible Values: 
 *         0 (no entity)
 *         entity ID
 *
 * 
 */
#define UF_PARAM_TURN_TRIM_AXIAL2_TAG   2565  /* Param_type_tag */


/* UF_PARAM_TURN_TRIM_AXIAL2_VAL
 *
 *   Description:
 *      This parameter describes the radial location for the second
 *      axial containment. It can be set alternatively to the parameter
 *      UF_PARAM_TURN_TRIM_AXIAL2_TAG, if no smart point is used.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Second Axial Containment
 *  Variable Name: <prefix>_second_axial_containment
 *
 *   Possible Values: double
 *
 * 
 */
#define UF_PARAM_TURN_TRIM_AXIAL2_VAL   2566  /* Param_type_double_length */


/* UF_PARAM_TURN_MIN_AREA_TOG
 *
 *   Description:
 *     This parameter lets you activate Minimum Area parameter.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Minimum Region Area Toggle
 *  Variable Name: <prefix>_minimum_region_area_toggle
 *
 *   Possible Values:     0: off
 *                     else: on
 *
 * 
 */
#define UF_PARAM_TURN_MIN_AREA_TOG   2608 


/* UF_PARAM_TURN_MIN_AREA
 *
 *   Description:
 *     This parameter defines the minimum size of a cut region to be accepted
 *     by the turning rough and finish operations
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Minimum Region Area
 *  Variable Name: <prefix>_minimum_region_area
 *
 *   Possible Values: 
 *
 * 
 */
#define UF_PARAM_TURN_MIN_AREA   2567  /* Param_type_double_length */


/* UF_PARAM_TURN_START_OFFSET
 *
 *   Description:
 *      Rough/Finish: The value defines the offset at the cut region start
 *                    point (for open boundaries only)
 *      Threading: A positive value extend the thread by shifting the thread
 *                 geometry start point along the crestline. A negative value 
 *                 shortes the thread by shifting the start point in the 
 *                 inverted direction.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Area Start Point Offset
 *  Variable Name: <prefix>_area_start_point_offset
 *
 *   Possible Values: 
 *
 * 
 */
#define UF_PARAM_TURN_START_OFFSET   2568  /* Param_type_double_length */


/* UF_PARAM_TURN_END_OFFSET
 *
 *   Description:
 *      Rough/Finish: The value defines the offset at the cut region end
 *                    point (for open boundaries only)
 *      Threading: A positive value extend the thread by shifting the thread
 *                 geometry end point along the crestline. A negative value 
 *                 shortens the thread by shifting the end point in the 
 *                 inverted direction.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Area End Point Offset
 *  Variable Name: <prefix>_area_end_point_offset
 *
 *   Possible Values: 
 *
 * 
 */
#define UF_PARAM_TURN_END_OFFSET   2569  /* Param_type_double_length */


/* UF_PARAM_TURN_CREST_OFFSET
 *
 *   Description:
 *      Threading: A positive value increases the thread crest diameter by adding an offset
 *                 to the crestline. A negative value decreases the thread crest diameter
 *                 by subtracting an offset from the crestline.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Crest Line Offset
 *  Variable Name: <prefix>_crest_line_offset
 *
 *   Possible Values: 
 *
 * 
 */
#define UF_PARAM_TURN_CREST_OFFSET   2602  /* Param_type_double_length */


/* UF_PARAM_TURN_ROOT_OFFSET
 *
 *   Description:
 *      Threading: A positive value increases the thread root diameter by adding an offset
 *                 to the rootline. A negative value decreases the thread root diameter
 *                 by subtracting an offset from the rootline.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Root Line Offset
 *  Variable Name: <prefix>_root_line_offset
 *
 *   Possible Values: 
 *
 * 
 */
#define UF_PARAM_TURN_ROOT_OFFSET   2603  /* Param_type_double_length */


/* UF_PARAM_TURN_START_ANGLE
 *
 *   Description:
 *      This parameter controls an offset angle to close the cut region from
 *      part boundary start point to the in-process shape. This angle only
 *      takes effect for open part boundaries. Positive values enlarge the
 *      cut region while negative angles shrink the cut region size.
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Area Start Angle Offset
 *  Variable Name: <prefix>_area_start_angle_offset
 *
 *   Possible Values: -90 < angle < 90 (degree)
 *
 * 
 */
#define UF_PARAM_TURN_START_ANGLE   2570  /* Param_type_double */


/* UF_PARAM_TURN_END_ANGLE
 *
 *   Description:
 *      This parameter controls an offset angle to close the cut region from
 *      part boundary end point to the in-process shape. This angle only
 *      takes effect for open part boundaries. Positive values enlarge the
 *      cut region while negative angles shrink the cut region size.
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Area End Angle Offset
 *  Variable Name: <prefix>_area_end_angle_offset
 *
 *   Possible Values: -90 < angle < 90 (degree)
 *
 * 
 */
#define UF_PARAM_TURN_END_ANGLE   2571  /* Param_type_double */


/* UF_PARAM_TURN_TANG_EXTENSION
 *
 *   Description:
 *      This parameter activates the automatic, tangential extension of
 *      open chained part boundaries. Trim points are generated automatically
 *      at start and at end point of the part boundary. The trim rays are
 *      tangential extensions of the start/end segments.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Tangential Start/End Extension
 *  Variable Name: <prefix>_tangential_start_end_extension
 *
 *   Possible Values:
 *     0 = inactive
 *     1 = active
 *
 * 
 */
#define UF_PARAM_TURN_TANG_EXTENSION   2589 


typedef enum
{
    UF_PARAM_trim_point_off_geom_check_off = 0,
    UF_PARAM_trim_point_on_geom_check_off,
    UF_PARAM_trim_point_off_geom_check_on,
    UF_PARAM_trim_point_on_geom_check_on
} UF_PARAM_turn_trim_point_type_t;


/* UF_PARAM_TURN_TRIM_POINT1_TOG
 *
 *   Description:
 *      This parameter controls the use of trim point 1.
 *      Bit 0 activates trim point 1.
 *      Bit 1 controls "Geometry Check" mode: 0->Part Geometry Check off
 *                                            1->Part Geometry Check on
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Use First Point Containment
 *  Variable Name: <prefix>_use_first_point_containment
 *
 *   Possible Values: UF_PARAM_turn_trim_point_type_t
 *
 * 
 */
#define UF_PARAM_TURN_TRIM_POINT1_TOG   2575 


/* UF_PARAM_TURN_TRIM_POINT1_TAG
 *
 *   Description:
 *      This parameter holds the object ID of a smart point referencing
 *      the position of trim point 1.
 *
 *   Type: UF_PARAM_type_tag
 *
 *   Name: First Point Containment Tag
 *  Variable Name: <prefix>_first_point_containment_tag
 *
 *   Possible Values: 
 *         0 (no entity)
 *         entity ID
 *
 * 
 */
#define UF_PARAM_TURN_TRIM_POINT1_TAG   2576 


/* UF_PARAM_TURN_TRIM_POINT1_EXTEND_TOG
 *
 *   Description:
 *      This parameter lets you activate Trim Point 1 Extend Distance.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Use First Point Extend Distance
 *  Variable Name: <prefix>_use_first_point_extend_distance
 *
 *   Possible Values:    0: off
 *                    else: on
 *
 * 
 */
#define UF_PARAM_TURN_TRIM_POINT1_EXTEND_TOG   2604 


/* UF_PARAM_TURN_TRIM_POINT1_EXTEND_VAL
 *
 *   Description:
 *      This parameter specifies the Trim Point 1 Extend Distance.
 *      It is only effective if parameter 
 *      UF_PARAM_TURN_TRIM_POINT1_EXTEND_TOG is on.
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: First Point Extend Distance
 *  Variable Name: <prefix>_first_point_extend_distance
 *
 *   Possible Values: Doubles
 *
 * 
 */
#define UF_PARAM_TURN_TRIM_POINT1_EXTEND_VAL   2605 


/* UF_PARAM_TURN_TRIM_POINT1_ANGLE_TOG
 *
 *   Description:
 *      This parameter lets you activate Trim Angle 1, i.e., the trim angle 
 *      that can be specified for/at Trim Point 1.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Use First Point Containment Angle
 *  Variable Name: <prefix>_use_first_point_containment_angle
 *
 *   Possible Values:    0: off
 *                    else: on
 *
 * 
 */
#define UF_PARAM_TURN_TRIM_POINT1_ANGLE_TOG   2577 


/* UF_PARAM_TURN_TRIM_POINT1_ANGLE_TAG
 *
 *   Description:
 *      This parameter holds the object ID of a line object specifying
 *      Trim Angle 1, i.e., it makes the Trim Angle 1 associative to geometry.
 *      It is only effective if parameter UF_PARAM_TURN_TRIM_POINT1_ANGLE_TOG is
 *      on.
 *
 *   Type: UF_PARAM_type_tag
 *
 *   Name: First Point Containment Angle Tag
 *  Variable Name: <prefix>_first_point_containment_angle_tag
 *
 *   Possible Values: 
 *         0 (no entity)
 *         entity ID
 *
 * 
 */
#define UF_PARAM_TURN_TRIM_POINT1_ANGLE_TAG   2578 


/* UF_PARAM_TURN_TRIM_POINT1_ANGLE_VAL
 *
 *   Description:
 *      This parameter specifies the Trim Angle 1 (the trim angle at Trim Point 1)
 *      in radians.
 *      It is only effective if parameter UF_PARAM_TURN_TRIM_POINT1_ANGLE_TOG is
 *      on and parameter UF_PARAM_TURN_TRIM_POINT1_ANGLE_TAG 
 *      is 0 (NULL_TAG).
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: First Point Containment Angle Value
 *  Variable Name: <prefix>_first_point_containment_angle_value
 *
 *   Possible Values: Double (angle in radians)
 *
 * 
 */
#define UF_PARAM_TURN_TRIM_POINT1_ANGLE_VAL   2579 


/* UF_PARAM_TURN_TRIM_POINT1_ANGLE_OFFSET
 *
 *  Description:
 *     This parameter specifies an angle offset (in radians) which is added 
 *     to Trim Angle 1 (the Trim Angle at Trim Point 1).
 *
 *  Type: UF_PARAM_type_double
 *
 *  Name: First Point Containment Angle Offset
 *  Variable Name: <prefix>_first_point_containment_angle_offset
 *
 *  Possible Values: Double (positive and negative in radians)
 *
 * 
 */
#define UF_PARAM_TURN_TRIM_POINT1_ANGLE_OFFSET   2587 


/* UF_PARAM_TURN_TRIM_POINT2_TOG
 *
 *   Description:
 *      This parameter controls the use of trim point 2.
 *      Bit 0 activates trim point 2.
 *      Bit 1 controls "Geometry Check" mode: 0->Part Geometry Check off
 *                                            1->Part Geometry Check on
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Use Second Point Containment
 *  Variable Name: <prefix>_use_second_point_containment
 *
 *   Possible Values: UF_PARAM_turn_trim_point_type_t
 *
 * 
 */
#define UF_PARAM_TURN_TRIM_POINT2_TOG   2580 


/* UF_PARAM_TURN_TRIM_POINT2_TAG
 *
 *   Description:
 *      This parameter holds the object ID of a smart point referencing
 *      the position of trim point 2.
 *
 *   Type: UF_PARAM_type_tag
 *
 *   Name: Second Point Containment Tag
 *  Variable Name: <prefix>_second_point_containment_tag
 *
 *   Possible Values: 
 *         0 (no entity)
 *         entity ID
 *
 * 
 */
#define UF_PARAM_TURN_TRIM_POINT2_TAG   2581 


/* UF_PARAM_TURN_TRIM_POINT2_EXTEND_TOG
 *
 *   Description:
 *      This parameter lets you activate Trim Point 1 Extend Distance.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Use Second Point Extend Distance
 *  Variable Name: <prefix>_use_second_point_extend_distance
 *
 *   Possible Values:    0: off
 *                    else: on
 *
 * 
 */
#define UF_PARAM_TURN_TRIM_POINT2_EXTEND_TOG   2606 


/* UF_PARAM_TURN_TRIM_POINT2_EXTEND_VAL
 *
 *   Description:
 *      This parameter specifies the Trim Point 2 Extend Distance.
 *      It is only effective if parameter 
 *      UF_PARAM_TURN_TRIM_POINT2_EXTEND_TOG is on.
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Second Point Extend Distance
 *  Variable Name: <prefix>_second_point_extend_distance
 *
 *   Possible Values: Doubles
 *
 * 
 */
#define UF_PARAM_TURN_TRIM_POINT2_EXTEND_VAL   2607 


/* UF_PARAM_TURN_TRIM_POINT2_ANGLE_TOG
 *
 *   Description:
 *      This parameter lets you activate Trim Angle 2, i.e., the trim angle 
 *      that can be specified for/at Trim Point 2.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Use Second Point Containment Angle
 *  Variable Name: <prefix>_use_second_point_containment_angle
 *
 *   Possible Values:    0: off
 *                    else: on
 *
 * 
 */
#define UF_PARAM_TURN_TRIM_POINT2_ANGLE_TOG   2582 


/* UF_PARAM_TURN_TRIM_POINT2_ANGLE_TAG
 *
 *   Description:
 *      This parameter holds the object ID of a line object referencing
 *      the trim point 2 angle.
 *      It is only used if parameter UF_PARAM_TURN_TRIM_POINT2_ANGLE_TOG is
 *      on.
 *
 *   Type: UF_PARAM_type_tag
 *
 *   Name: Second Point Containment Angle Tag
 *  Variable Name: <prefix>_second_point_containment_angle_tag
 *
 *   Possible Values: 
 *         0 (no entity)
 *         entity ID
 *
 * 
 */
#define UF_PARAM_TURN_TRIM_POINT2_ANGLE_TAG   2583 


/* UF_PARAM_TURN_TRIM_POINT2_ANGLE_VAL
 *
 *   Description:
 *      This parameter specifies the trim point 2 angle in radians.
 *      It is only used if parameter UF_PARAM_TURN_TRIM_POINT2_ANGLE_TOG is
 *      on and parameter UF_PARAM_TURN_TRIM_POINT2_ANGLE_TAG 
 *      is 0 (NULL_TAG).
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Second Point Containment Angle Value
 *  Variable Name: <prefix>_second_point_containment_angle_value
 *
 *   Possible Values: Double (angle in radians)
 *
 * 
 */
#define UF_PARAM_TURN_TRIM_POINT2_ANGLE_VAL   2584 


/* UF_PARAM_TURN_TRIM_POINT2_ANGLE_OFFSET
 *
 *  Description:
 *     This parameter specifies an angle offset (in radians) which is added 
 *     to the Trim Angle of Trim Point 2.
 *
 *  Type: UF_PARAM_type_double
 *
 *  Name: Second Point Containment Angle Offset
 *  Variable Name: <prefix>_second_point_containment_angle_offset
 *
 *  Possible Values: Double (positive and negative in radians)
 *
 * 
 */
#define UF_PARAM_TURN_TRIM_POINT2_ANGLE_OFFSET   2588 


/* UF_PARAM_TURN_SURFACE_SENSITIVITY_TOG
 *
 *   Description:
 *      This parameter lets you activate Surface Sensitivity,
 *      which is specified by parameter
 *      UF_PARAM_TURN_SURFACE_SENSITIVITY.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Use Surface Sensitivity
 *  Variable Name: <prefix>_use_surface_sensitivity
 *
 *   Possible Values:    0: off
 *                    else: on
 *
 * 
 */
#define UF_PARAM_TURN_SURFACE_SENSITIVITY_TOG   2616 


/* UF_PARAM_TURN_SURFACE_SENSITIVITY
 *
 *   Description:
 *      This parameter controls Surface Sensitivity for the 
 *      Turning application.
 *      Surface Sensitivity makes containment in Turning react
 *      to member data on surfaces (boundary members) that are 
 *      in close proximity to the latter, i.e., that are closer 
 *      to the containment than the specified distance value.
 *      It is only applied if parameter 
 *      UF_PARAM_TURN_SURFACE_SENSITIVITY_TOG is on.
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Surface Sensitivity
 *  Variable Name: <prefix>_surface_sensitivity
 *
 *   Possible Values: Double
 *
 * 
 */
#define UF_PARAM_TURN_SURFACE_SENSITIVITY   2617 


/* UF_PARAM_TURN_TOL_OFFSET_BEFORE_CONTAINMENT
 *
 *   Description:
 *      This parameter controls if tolerance offset is applied
 *      before or after containment.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Tol Offset Before Containment
 *  Variable Name: <prefix>_tol_offset_before_containment
 *
 *   Possible Values:   0  ->  Tolerance offset is applied after containment 
 *                      1  ->  Tolerance offset is applied before containment 
 *
 * 
 */
#define UF_PARAM_TURN_TOL_OFFSET_BEFORE_CONTAINMENT   2648 


/* UF_PARAM_TURN_CUT_REG_SELECT_TOG
 *
 *   Description:
 *      This parameter activates and deactivates the cut
 *      region selection point usage.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Cut Region Select Toggle
 *  Variable Name: <prefix>_cut_region_select_toggle
 *
 *   Possible Values:   0  ->  Deactivate cut region selection point
 *                      1  ->  Activate cut region selection point
 *
 * 
 */
#define UF_PARAM_TURN_CUT_REG_SELECT_TOG   2585  /* Param_type_tag */


/* UF_PARAM_TURN_CUT_REG_SELECT_TAG
 *
 *   Description:
 *      This parameter defines the cut region selection point.
 *
 *   Type: UF_PARAM_type_tag
 *
 *   Name: Cut Region Select Point
 *  Variable Name: <prefix>_cut_region_select_point
 *
 *   Possible Values:
 *
 * 
 */
#define UF_PARAM_TURN_CUT_REG_SELECT_TAG   2586  /* Param_type_tag */


typedef enum UF_PARAM_turn_eng_profiling_e
{
    UF_PARAM_turn_eng_profiling_undefined      = -1,
    UF_PARAM_turn_eng_profiling_auto_circular  = 0,
    UF_PARAM_turn_eng_profiling_auto_linear    = 1,
    UF_PARAM_turn_eng_profiling_vector         = 2,
    UF_PARAM_turn_eng_profiling_angle_distance = 3,
    UF_PARAM_turn_eng_profiling_rel_linear     = 4,
    UF_PARAM_turn_eng_profiling_point          = 5
} UF_PARAM_turn_eng_profiling_t;

/* UF_PARAM_TURN_ENG_PROFILING
 *
 *   Description:
 *      Defines the method for engage to profile cuts.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Engage Profiling
 *  Variable Name: <prefix>_engage_profiling
 *
 *   Possible Values: UF_PARAM_turn_eng_profiling_t
 *
 * 
 */
#define UF_PARAM_TURN_ENG_PROFILING   2590  /* UF_PARAM_type_int */


typedef enum UF_PARAM_turn_eng_level_blank_e
{
    UF_PARAM_turn_eng_level_blank_undefined      = -1,
    UF_PARAM_turn_eng_level_blank_auto_linear    = 1,
    UF_PARAM_turn_eng_level_blank_vector         = 2,
    UF_PARAM_turn_eng_level_blank_angle_distance = 3,
    UF_PARAM_turn_eng_level_blank_point          = 5,
    UF_PARAM_turn_eng_level_blank_two_circles    = 6
} UF_PARAM_turn_eng_level_blank_t;

/* UF_PARAM_TURN_ENG_LEVEL_BLANK
 *
 *   Description:
 *      Defines the method for engage to rough cuts starting at blank geometry.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Engage Level/Blank
 *  Variable Name: <prefix>_engage_level_blank
 *
 *   Possible Values: UF_PARAM_turn_eng_level_blank_t
 *
 * 
 */
#define UF_PARAM_TURN_ENG_LEVEL_BLANK   2591  /* UF_PARAM_type_int */


typedef enum UF_PARAM_turn_eng_level_part_e
{
    UF_PARAM_turn_eng_level_part_undefined      = -1,
    UF_PARAM_turn_eng_level_part_auto_linear    = 1,
    UF_PARAM_turn_eng_level_part_vector         = 2,
    UF_PARAM_turn_eng_level_part_angle_distance = 3,
    UF_PARAM_turn_eng_level_part_point          = 5,
    UF_PARAM_turn_eng_level_part_2pt_tang       = 7
} UF_PARAM_turn_eng_level_part_t;

/* UF_PARAM_TURN_ENG_LEVEL_PART
 *
 *   Description:
 *      Defines the method for engage to rough cuts starting at part geometry.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Engage Level/Part
 *  Variable Name: <prefix>_engage_level_part
 *
 *   Possible Values: UF_PARAM_turn_eng_level_part_t
 *
 * 
 */
#define UF_PARAM_TURN_ENG_LEVEL_PART   2592  /* UF_PARAM_type_int */


typedef enum UF_PARAM_turn_eng_level_safe_e
{
    UF_PARAM_turn_eng_level_safe_undefined      = -1,
    UF_PARAM_turn_eng_level_safe_auto_linear    = 1,
    UF_PARAM_turn_eng_level_safe_vector         = 2,
    UF_PARAM_turn_eng_level_safe_angle_distance = 3,
    UF_PARAM_turn_eng_level_safe_point          = 5
} UF_PARAM_turn_eng_level_safe_t;

/* UF_PARAM_TURN_ENG_LEVEL_SAFE
 *
 *   Description:
 *      Defines the method for engage to the the very last rough cut.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Engage Level/Safe
 *  Variable Name: <prefix>_engage_level_safe
 *
 *   Possible Values: UF_PARAM_turn_eng_level_safe_t
 *
 * 
 */
#define UF_PARAM_TURN_ENG_LEVEL_SAFE   2593  /* UF_PARAM_type_int */


typedef enum UF_PARAM_turn_eng_plunge_e
{
    UF_PARAM_turn_eng_plunge_undefined      = -1,
    UF_PARAM_turn_eng_plunge_auto_linear    = 1,
    UF_PARAM_turn_eng_plunge_vector         = 2,
    UF_PARAM_turn_eng_plunge_angle_distance = 3,
    UF_PARAM_turn_eng_plunge_point          = 5
} UF_PARAM_turn_eng_plunge_t;

/* UF_PARAM_TURN_ENG_PLUNGE
 *
 *   Description:
 *      Defines the method for engage to plunge cuts.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Engage Plunge
 *  Variable Name: <prefix>_engage_plunge
 *
 *   Possible Values: UF_PARAM_turn_eng_plunge_t
 *
 * 
 */
#define UF_PARAM_TURN_ENG_PLUNGE   2594  /* UF_PARAM_type_int */


typedef enum UF_PARAM_turn_eng_1plunge_e
{
    UF_PARAM_turn_eng_1plunge_undefined      = -1,
    UF_PARAM_turn_eng_1plunge_auto_linear    = 1,
    UF_PARAM_turn_eng_1plunge_vector         = 2,
    UF_PARAM_turn_eng_1plunge_angle_distance = 3,
    UF_PARAM_turn_eng_1plunge_point          = 5
} UF_PARAM_turn_eng_1plunge_t;

/* UF_PARAM_TURN_ENG_1PLUNGE
 *
 *   Description:
 *      Defines the method for engage to first plunge cuts.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Engage First Plunge
 *  Variable Name: <prefix>_engage_first_plunge
 *
 *   Possible Values: UF_PARAM_turn_eng_1plunge_t
 *
 * 
 */
#define UF_PARAM_TURN_ENG_1PLUNGE   2595  /* UF_PARAM_type_int */


typedef enum UF_PARAM_turn_ret_profiling_e
{
    UF_PARAM_turn_ret_profiling_undefined      = -1,
    UF_PARAM_turn_ret_profiling_auto_circular  = 0,
    UF_PARAM_turn_ret_profiling_auto_linear    = 1,
    UF_PARAM_turn_ret_profiling_vector         = 2,
    UF_PARAM_turn_ret_profiling_angle_distance = 3,
    UF_PARAM_turn_ret_profiling_rel_linear     = 4,
    UF_PARAM_turn_ret_profiling_point          = 5
} UF_PARAM_turn_ret_profiling_t;

/* UF_PARAM_TURN_RET_PROFILING
 *
 *   Description:
 *      Defines the method for retract from profiling cut.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Retract Profiling
 *  Variable Name: <prefix>_retract_profiling
 *
 *   Possible Values: UF_PARAM_turn_ret_profiling_t
 *
 * 
 */
#define UF_PARAM_TURN_RET_PROFILING   2596  /* UF_PARAM_type_int */


typedef enum UF_PARAM_turn_ret_level_blank_e
{
    UF_PARAM_turn_ret_level_blank_undefined      = -1,
    UF_PARAM_turn_ret_level_blank_auto_linear    = 1,
    UF_PARAM_turn_ret_level_blank_vector         = 2,
    UF_PARAM_turn_ret_level_blank_angle_distance = 3,
    UF_PARAM_turn_ret_level_blank_point          = 5
} UF_PARAM_turn_ret_level_blank_t;

/* UF_PARAM_TURN_RET_LEVEL_BLANK
 *
 *   Description:
 *      Defines the method for retract from rough cuts ending at blank geometry.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Retract Level/Blank
 *  Variable Name: <prefix>_retract_level_blank
 *
 *   Possible Values: UF_PARAM_turn_ret_level_blank_t
 *
 * 
 */
#define UF_PARAM_TURN_RET_LEVEL_BLANK   2597  /* UF_PARAM_type_int */


typedef enum UF_PARAM_turn_ret_level_part_e
{
    UF_PARAM_turn_ret_level_part_undefined      = -1,
    UF_PARAM_turn_ret_level_part_auto_linear    = 1,
    UF_PARAM_turn_ret_level_part_vector         = 2,
    UF_PARAM_turn_ret_level_part_angle_distance = 3,
    UF_PARAM_turn_ret_level_part_point          = 5,
    UF_PARAM_turn_ret_level_part_two_circles    = 6
} UF_PARAM_turn_ret_level_part_t;

/* UF_PARAM_TURN_RET_LEVEL_PART
 *
 *   Description:
 *      Defines the method for retract from rough cuts ending at part geometry.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Retract Level/Part
 *  Variable Name: <prefix>_retract_level_part
 *
 *   Possible Values: UF_PARAM_turn_ret_level_part_t
 *
 * 
 */
#define UF_PARAM_TURN_RET_LEVEL_PART   2598  /* UF_PARAM_type_int */


typedef enum UF_PARAM_turn_ret_plunge_e
{
    UF_PARAM_turn_ret_plunge_undefined      = -1,
    UF_PARAM_turn_ret_plunge_auto_linear    = 1,
    UF_PARAM_turn_ret_plunge_vector         = 2,
    UF_PARAM_turn_ret_plunge_angle_distance = 3
} UF_PARAM_turn_ret_plunge_t;

/* UF_PARAM_TURN_RET_PLUNGE
 *
 *   Description:
 *      Defines the method for retract from plunge cut.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Retract Level/Part
 *  Variable Name: <prefix>_retract_level_part
 *
 *   Possible Values: UF_PARAM_turn_ret_plunge_t
 *
 * 
 */
#define UF_PARAM_TURN_RET_PLUNGE   2599  /* UF_PARAM_type_int */


typedef enum UF_PARAM_turn_ret_1plunge_e
{
    UF_PARAM_turn_ret_1plunge_undefined      = -1,
    UF_PARAM_turn_ret_1plunge_auto_linear    = 1,
    UF_PARAM_turn_ret_1plunge_vector         = 2,
    UF_PARAM_turn_ret_1plunge_angle_distance = 3
} UF_PARAM_turn_ret_1plunge_t;

/* UF_PARAM_TURN_RET_1PLUNGE
 *
 *   Description:
 *      Defines the method for retract from first plunge cuts.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Retract First Plunge
 *  Variable Name: <prefix>_retract_first_plunge
 *
 *   Possible Values: UF_PARAM_turn_ret_1plunge_t
 *
 * 
 */
#define UF_PARAM_TURN_RET_1PLUNGE   2600  /* UF_PARAM_type_int */


/* UF_PARAM_TURN_CLEAR_RADIAL_TOG
 *
 *   Description:
 *      This parameter controls the availability of a radial clearance plane
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Use Radial Clearance
 *  Variable Name: <prefix>_use_radial_clearance
 *
 *   Possible Values: 
 *     0 = inactive
 *     1 = active
 *
 * 
 */
#define UF_PARAM_TURN_CLEAR_RADIAL_TOG   2610  /* UF_PARAM_type_int */


/* UF_PARAM_TURN_CLEAR_RADIAL_TAG
 *
 *   Description:
 *      This parameter holds the object ID of a smart point referencing
 *      the position for the radial clearance plane.
 *
 *   Type: UF_PARAM_type_tag
 *
 *   Name: Radial Clearance Tag
 *  Variable Name: <prefix>_radial_clearance_tag
 *
 *   Possible Values: 
 *         0 (no entity)
 *         entity ID
 *
 * 
 */
#define UF_PARAM_TURN_CLEAR_RADIAL_TAG   2611  /* UF_PARAM_type_tag */


/* UF_PARAM_TURN_CLEAR_RADIAL_VAL
 *
 *   Description:
 *      This parameter describes the location for the radial clearance plane.
 *      It can be set alternatively to the parameter
 *      UF_PARAM_TURN_CLEAR_RADIAL_TAG, if no smart point is used.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Radial Clearance Value
 *  Variable Name: <prefix>_radial_clearance_value
 *
 *   Possible Values: double
 *
 * 
 */
#define UF_PARAM_TURN_CLEAR_RADIAL_VAL   2612  /* UF_PARAM_type_double_length */


/* UF_PARAM_TURN_CLEAR_AXIAL_TOG
 *
 *   Description:
 *      This parameter controls the availability of an axial clearance plane
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Use Axial Clearance
 *  Variable Name: <prefix>_use_axial_clearance
 *
 *   Possible Values: 
 *     0 = inactive
 *     1 = active
 *
 * 
 */
#define UF_PARAM_TURN_CLEAR_AXIAL_TOG   2613  /* UF_PARAM_type_int */


/* UF_PARAM_TURN_CLEAR_AXIAL_TAG
 *
 *   Description:
 *      This parameter holds the object ID of a smart point referencing
 *      the position for the radial clearance plane.
 *
 *   Type: UF_PARAM_type_tag
 *
 *   Name: Axial Clearance Tag
 *  Variable Name: <prefix>_axial_clearance_tag
 *
 *   Possible Values: 
 *         0 (no entity)
 *         entity ID
 *
 * 
 */
#define UF_PARAM_TURN_CLEAR_AXIAL_TAG   2614  /* UF_PARAM_type_tag */


/* UF_PARAM_TURN_CLEAR_AXIAL_VAL
 *
 *   Description:
 *      This parameter describes the location for the axial clearance plane.
 *      It can be set alternatively to the parameter
 *      UF_PARAM_TURN_CLEAR_AXIAL_TAG, if no smart point is used.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Axial Clearance Value
 *  Variable Name: <prefix>_axial_clearance_value
 *
 *   Possible Values: double
 *
 * 
 */
#define UF_PARAM_TURN_CLEAR_AXIAL_VAL   2615  /* UF_PARAM_type_double_length */


/* UF_PARAM_TURN_MULTIPLE_CUT_REGIONS_TOG
 *
 *   Description:
 *      Controls the use of multiple cut regions option menu.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Multiple Cut Regions Toggle
 *  Variable Name: <prefix>_multiple_cut_regions_toggle
 *
 *   Possible Values: 
 *     0 = inactive
 *     1 = active
 *
 * 
 */
#define UF_PARAM_TURN_MULTIPLE_CUT_REGIONS_TOG   2618 


typedef enum UF_PARAM_turn_multiple_cut_regions_e
{
    UF_PARAM_turn_multiple_cut_regions_single_direction = 0,
    UF_PARAM_turn_multiple_cut_regions_inverse_direction,
    UF_PARAM_turn_multiple_cut_regions_bi_directional,
    UF_PARAM_turn_multiple_cut_regions_alternate
} UF_PARAM_turn_multiple_cut_regions_t;

/* UF_PARAM_TURN_MULTIPLE_CUT_REGIONS
 *
 *   Description:
 *      Controls the sequence of machining multiple cut regions.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Multiple Cut Regions
 *  Variable Name: <prefix>_multiple_cut_regions
 *
 *   Possible Values: UF_PARAM_turn_multiple_cut_regions_t
 *
 * 
 */
#define UF_PARAM_TURN_MULTIPLE_CUT_REGIONS   2619 


/* UF_PARAM_TURN_LEAD_ANG
 *
 *   Description:
 *      Defines the first clearance angle for turning inserts.
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Lead Angle
 *  Variable Name: <prefix>_lead_angle
 *
 *   Possible Values: 
 *
 * 
 */
#define UF_PARAM_TURN_LEAD_ANG   2620  /* Param_type_double */


/* UF_PARAM_TURN_HEEL_ANG
 *
 *   Description:
 *      Defines the second clearance angle for turning inserts.
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Heel Angle
 *  Variable Name: <prefix>_heel_angle
 *
 *   Possible Values: 
 *
 * 
 */
#define UF_PARAM_TURN_HEEL_ANG   2621  /* Param_type_double */


/* UF_PARAM_TURN_FROM_DIA
 *
 *   Description:
 *      Defines the clearance distance from diameters.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Clearance from Diameters
 *  Variable Name: <prefix>_clearance_from_diameters
 *
 *   Possible Values: double
 *
 * 
 */
#define UF_PARAM_TURN_FROM_DIA   2622  /* Param_type_double_length */


/* UF_PARAM_TURN_FROM_FACES
 *
 *   Description:
 *      Defines the clearance distance from faces.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Clearance from Faces
 *  Variable Name: <prefix>_clearance_from_faces
 *
 *   Possible Values: double
 *
 * 
 */
#define UF_PARAM_TURN_FROM_FACES   2623  /* UF_PARAM_type_double_length */


/* UF_PARAM_TURN_MIN_DEPTH
 *
 *   Description:
 *      Defines the minimum depth of cut for rough cuts (Cut constraints).
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Min. Depth
 *  Variable Name: <prefix>_min__depth
 *
 *   Possible Values: 
 *
 * 
 */
#define UF_PARAM_TURN_MIN_DEPTH   2624  /* UF_PARAM_type_double_length */


/* UF_PARAM_TURN_MIN_DEPTH_TOG
 *
 *   Description:
 *      Controls the use of minimum depth of cut setting (Cut constraints).
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Min. Depth Toggle
 *  Variable Name: <prefix>_min__depth_toggle
 *
 *   Possible Values: 
 *     0 = inactive
 *     1 = active
 *
 * 
 */
#define UF_PARAM_TURN_MIN_DEPTH_TOG   2625  /* UF_PARAM_type_int */


/* UF_PARAM_TURN_MIN_LENGTH
 *
 *   Description:
 *      Defines the minimum length of cut for rough cuts (Cut constraints).
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Min. Length
 *  Variable Name: <prefix>_min__length
 *
 *   Possible Values: double
 *
 * 
 */
#define UF_PARAM_TURN_MIN_LENGTH   2626  /* UF_PARAM_type_double_length */


/* UF_PARAM_TURN_MIN_LENGTH_TOG
 *
 *   Description:
 *      Controls the use of minimum length of cut setting (Cut constraints).
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Min. Length Toggle
 *  Variable Name: <prefix>_min__length_toggle
 *
 *   Possible Values: 
 *     0 = inactive
 *     1 = active
 *
 * 
 */
#define UF_PARAM_TURN_MIN_LENGTH_TOG   2627  /* UF_PARAM_type_int */


/* UF_PARAM_TURN_UNDERCUT_TOG
 *
 *   Description:
 *      If activated this parameter allows the processors to machine undercuts.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Undercut Toggle
 *  Variable Name: <prefix>_undercut_toggle
 *
 *   Possible Values: 
 *     0 = inactive
 *     1 = active
 *
 * 
 */
#define UF_PARAM_TURN_UNDERCUT_TOG   2628  /* UF_PARAM_type_int */


/* UF_PARAM_TURN_RELIEF_PLUNGE_TOG
 *
 *   Description:
 *      Controls the use of relief plunge cuts (Cut Control).
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Relief Plunge Toggle
 *  Variable Name: <prefix>_relief_plunge_toggle
 *
 *   Possible Values: 
 *     0 = inactive
 *     1 = active
 *
 * 
 */
#define UF_PARAM_TURN_RELIEF_PLUNGE_TOG   2629  /* UF_PARAM_type_int */


/* UF_PARAM_TURN_WALL_DISTANCE
 *
 *   Description:
 *      Defines the distance to the wall for relief plunges (Cut Control).
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Distance to Wall 
 *  Variable Name: <prefix>_distance_to_wall
 *
 *   Possible Values: 
 *
 * 
 */
#define UF_PARAM_TURN_WALL_DISTANCE   2630  /* UF_PARAM_type_double_length */


/* UF_PARAM_TURN_DISTANCE
 *
 *   Description:
 *      Defines the distance for constant break chip mode (Chip Control) 
 *      in plunge roughing.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Distance 
 *  Variable Name: <prefix>_distance
 *
 *   Possible Values: 
 *
 * 
 */
#define UF_PARAM_TURN_DISTANCE   2632  /* UF_PARAM_type_double_length */


/* UF_PARAM_TURN_WALL_DISTANCE_PERCENT
 *
 *   Description:
 *      Defines the distance to the wall for relief plunges in percent of the
 *      insert width (Cut Control).
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Distance to Wall Percent
 *  Variable Name: <prefix>_distance_to_wall_percent
 *
 *   Possible Values: 
 *
 * 
 */
#define UF_PARAM_TURN_WALL_DISTANCE_PERCENT   2634  /* UF_PARAM_type_double */


typedef enum UF_PARAM_turn_relief_plunge_unit_e
{
    UF_PARAM_turn_relief_plunge_unit_distance = 0,
    UF_PARAM_turn_relief_plunge_unit_percent
} UF_PARAM_turn_relief_plunge_unit_t;

/* UF_PARAM_TURN_RELIEF_PLUNGE_UNIT
 *
 *   Description:
 *      Controls how the distance to the wall is to be measured (Cut Control).
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Relief Plunge Unit
 *  Variable Name: <prefix>_relief_plunge_unit
 *
 *   Possible Values: UF_PARAM_turn_relief_plunge_unit_t
 *
 * 
 */
#define UF_PARAM_TURN_RELIEF_PLUNGE_UNIT   2635  /* UF_PARAM_type_int */


/* UF_PARAM_TURN_SAFE_DISTANCE
 *
 *   Description:
 *      Defines the safe distance (Cut Control).
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Safe Distance
 *  Variable Name: <prefix>_safe_distance
 *
 *   Possible Values: 
 *
 * 
 */
#define UF_PARAM_TURN_SAFE_DISTANCE   2636  /* UF_PARAM_type_double_length */


/* UF_PARAM_TROPR_CONTINUOUS_CUTS_ONLY
 *
 *   Description:
 *      Activates the 'Continous Cuts Only' mode in Rough/Contour Zig and 
 *      ZigZag.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Continuous Cuts Only
 *  Variable Name: <prefix>_continuous_cuts_only
 *
 *   Possible Values:     0: off
 *                     else: on
 *
 * 
 */
#define UF_PARAM_TROPR_CONTINUOUS_CUTS_ONLY   2637 


/* UF_PARAM_TROPR_CLEANUP_CONTROL
 *
 *   Description:
 *      Activates the 'Continous Cuts Only' mode in Rough/Contour Zig and 
 *      ZigZag.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Cleanup Control
 *  Variable Name: <prefix>_cleanup_control
 *
 *   Possible Values:     0: off
 *                     else: on
 *
 * 
 */
#define UF_PARAM_TROPR_CLEANUP_CONTROL   2638 


typedef enum UF_PARAM_turn_corner_ctrl_type_e
{
    UF_PARAM_turn_corner_ctrl_roll_around = 0,
    UF_PARAM_turn_corner_ctrl_extend_tang,
    UF_PARAM_turn_corner_ctrl_round,
    UF_PARAM_turn_corner_ctrl_break
} UF_PARAM_turn_corner_ctrl_type_t;


/* UF_PARAM_TURN_NORMAL_TYPE
 *
 *   Description:
 *      This parameter controls the processing of normal corners. Normal corners
 *      are convex corners not being treated as shallow corners.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Normal Corner Type
 *  Variable Name: <prefix>_normal_corner_type
 *
 *   Possible Values: UF_PARAM_turn_corner_ctrl_type_t
 *
 * 
 */
#define UF_PARAM_TURN_NORMAL_TYPE   2640  /* Param_type_int */


/* UF_PARAM_TURN_NORMAL_DIST_RAD
 *
 *   Description:
 *      Gives the radius for round corners and the distance for chamfers,
 *      depending on normal corner control type (UF_PARAM_TURN_NORMAL_TYPE).
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Normal Corner Distance/Radius
 *  Variable Name: <prefix>_normal_corner_distance_radius
 *
 *   Possible Values: double
 *
 * 
 */
#define UF_PARAM_TURN_NORMAL_DIST_RAD   2641  /* Param_type_double_length */


/* UF_PARAM_TURN_SHALLOW_TYPE
 *
 *   Description:
 *      This parameter controls the corner processing for shallow corners.
 *      Shallow corners are convex corners whose included angle is larger than
 *      the minimum angle for shallow corners (cf. UF_PARAM_TURN_SHALLOW_ANGLE)
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Shallow Corner Type
 *  Variable Name: <prefix>_shallow_corner_type
 *
 *   Possible Values: UF_PARAM_turn_corner_ctrl_type_t
 *
 * 
 */
#define UF_PARAM_TURN_SHALLOW_TYPE   2642  /* Param_type_int */


/* UF_PARAM_TURN_SHALLOW_DIST_RAD
 *
 *   Description:
 *      Gives the radius for round corners and the distance for chamfers,
 *      depending on shallow corner control type (UF_PARAM_TURN_SHALLOW_TYPE).
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Shallow Corner Distance/Radius
 *  Variable Name: <prefix>_shallow_corner_distance_radius
 *
 *   Possible Values: double
 *
 * 
 */
#define UF_PARAM_TURN_SHALLOW_DIST_RAD   2643  /* Param_type_double_length */


/* UF_PARAM_TURN_SHALLOW_ANGLE
 *
 *   Description:
 *      This parameter identifies the minimum included angle of a convex corner
 *      to have that corner be treated as a shallow corner (in contrast to
 *      normal corners, which have a smaller included angle than the given one).
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Shallow Min. Angle
 *  Variable Name: <prefix>_shallow_min__angle
 *
 *   Possible Values: 0 <= angle <= 180 (degree)
 *
 * 
 */
#define UF_PARAM_TURN_SHALLOW_ANGLE   2644  /* Param_type_double */


/* UF_PARAM_TURN_STOCK_F_EQUI
 *
 *   Description:
 *      Defines the equidistant stock for profile cuts in a turn roughing operation.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Finish Equidistant Stock
 *  Variable Name: <prefix>_finish_equidistant_stock
 *
 *   Possible Values: 
 *
 * 
 */
#define UF_PARAM_TURN_STOCK_F_EQUI   2650  /* Param_type_double_length */


/* UF_PARAM_TURN_STOCK_F_FACE
 *
 *   Description:
 *      Defines the face stock for profile cuts in a turn roughing operation.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Finish Face Stock
 *  Variable Name: <prefix>_finish_face_stock
 *
 *   Possible Values: 
 *
 * 
 */
#define UF_PARAM_TURN_STOCK_F_FACE   2651  /* Param_type_double_length */


/* UF_PARAM_TURN_STOCK_F_RAD
 *
 *   Description:
 *      Defines the radial stock for profile cuts in a turn roughing operation.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Finish Radial Stock
 *  Variable Name: <prefix>_finish_radial_stock
 *
 *   Possible Values: 
 *
 * 
 */
#define UF_PARAM_TURN_STOCK_F_RAD   2652  /* Param_type_double_length */


/* UF_PARAM_TURN_STOCK_B_EQUI
 *
 *   Description:
 *      Defines the equidistant stock for blank geometry in turn roughing and
 *      turn finishing operations.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Blank Equidistant Stock
 *  Variable Name: <prefix>_blank_equidistant_stock
 *
 *   Possible Values: 
 *
 * 
 */
#define UF_PARAM_TURN_STOCK_B_EQUI   2656  /* Param_type_double_length */


/* UF_PARAM_TURN_STOCK_B_FACE
 *
 *   Description:
 *      Defines the face stock for blank geometry in turn roughing and
 *      turn finishing operations.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Blank Face Stock
 *  Variable Name: <prefix>_blank_face_stock
 *
 *   Possible Values: 
 *
 * 
 */
#define UF_PARAM_TURN_STOCK_B_FACE   2657  /* Param_type_double_length */


/* UF_PARAM_TURN_STOCK_B_RAD
 *
 *   Description:
 *      Defines the radial stock for blank geometry in turn roughing and
 *      turn finishing operations.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Blank Radial Stock
 *  Variable Name: <prefix>_blank_radial_stock
 *
 *   Possible Values: 
 *
 * 
 */
#define UF_PARAM_TURN_STOCK_B_RAD   2658  /* Param_type_double_length */


/* UF_PARAM_TURN_FEED_CLEAR
 *
 *   Description:
 *      Feedrate for clearance motions.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Feedrate Clear
 *  Variable Name: <prefix>_feedrate_clear
 *
 *   Possible Values: 
 *
 * 
 */
#define UF_PARAM_TURN_FEED_CLEAR   2660  


/* UF_PARAM_TURN_FEED_CLEAR_UNIT
 *
 *   Description:
 *      Feedrate unit for clearance motions.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Feedrate Clear Unit
 *  Variable Name: <prefix>_feedrate_clear_unit
 *
 *   Possible Values: UF_PARAM_feed_unit_t
 *
 * 
 */
#define UF_PARAM_TURN_FEED_CLEAR_UNIT   2661  


/* UF_PARAM_TURN_FEED_LINEAR
 *
 *   Description:
 *      Feedrate for linear contouring motions.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Feedrate Linear
 *  Variable Name: <prefix>_feedrate_linear
 *
 *   Possible Values: 
 *
 * 
 */
#define UF_PARAM_TURN_FEED_LINEAR   2662  


/* UF_PARAM_TURN_FEED_LINEAR_UNIT
 *
 *   Description:
 *      Feedrate unit for linear contouring motions.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Feedrate Linear Unit
 *  Variable Name: <prefix>_feedrate_linear_unit
 *
 *   Possible Values: UF_PARAM_feed_unit_t
 *
 * 
 */
#define UF_PARAM_TURN_FEED_LINEAR_UNIT   2663  


/* UF_PARAM_TURN_FEED_FACE
 *
 *   Description:
 *      Feedrate for face contouring motions.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Feedrate Face
 *  Variable Name: <prefix>_feedrate_face
 *
 *   Possible Values: 
 *
 * 
 */
#define UF_PARAM_TURN_FEED_FACE   2664  


/* UF_PARAM_TURN_FEED_FACE_UNIT
 *
 *   Description:
 *      Feedrate unit for face contouring motions.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Feedrate Face Unit
 *  Variable Name: <prefix>_feedrate_face_unit
 *
 *   Possible Values: UF_PARAM_feed_unit_t
 *
 * 
 */
#define UF_PARAM_TURN_FEED_FACE_UNIT   2665  


/* UF_PARAM_TURN_FEED_DIAMETER
 *
 *   Description:
 *      Feedrate for radial contouring motions.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Feedrate Diameter
 *  Variable Name: <prefix>_feedrate_diameter
 *
 *   Possible Values: 
 *
 * 
 */
#define UF_PARAM_TURN_FEED_DIAMETER   2666  


/* UF_PARAM_TURN_FEED_DIAMETER_UNIT
 *
 *   Description:
 *      Feedrate unit for radial contouring motions.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Feedrate Diameter Unit
 *  Variable Name: <prefix>_feedrate_diameter_unit
 *
 *   Possible Values: UF_PARAM_feed_unit_t
 *
 * 
 */
#define UF_PARAM_TURN_FEED_DIAMETER_UNIT   2667  


/* UF_PARAM_TURN_FEED_CIRC_CW
 *
 *   Description:
 *      Feedrate for clockwise circular contouring motions.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Feedrate Circ. CW
 *  Variable Name: <prefix>_feedrate_circ__cw
 *
 *   Possible Values: 
 *
 * 
 */
#define UF_PARAM_TURN_FEED_CIRC_CW   2668  


/* UF_PARAM_TURN_FEED_CIRC_CW_UNIT
 *
 *   Description:
 *      Feedrate unit for clockwise circular contouring motions.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Feedrate Circ. CW Unit
 *  Variable Name: <prefix>_feedrate_circ__cw_unit
 *
 *   Possible Values: UF_PARAM_feed_unit_t
 *
 * 
 */
#define UF_PARAM_TURN_FEED_CIRC_CW_UNIT   2669  


/* UF_PARAM_TURN_FEED_CIRC_CCW
 *
 *   Description:
 *      Feedrate for counter clockwise circular contouring motions.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Feedrate Circ. CCW
 *  Variable Name: <prefix>_feedrate_circ__ccw
 *
 *   Possible Values: 
 *
 * 
 */
#define UF_PARAM_TURN_FEED_CIRC_CCW   2670  


/* UF_PARAM_TURN_FEED_CIRC_CCW_UNIT
 *
 *   Description:
 *      Feedrate unit for counter clockwise circular contouring motions.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Feedrate Circ. CCW Unit
 *  Variable Name: <prefix>_feedrate_circ__ccw_unit
 *
 *   Possible Values: UF_PARAM_feed_unit_t
 *
 * 
 */
#define UF_PARAM_TURN_FEED_CIRC_CCW_UNIT   2671  


/* UF_PARAM_TURN_FEED_ACCEL
 *
 *   Description:
 *      Feedrate for acceleration phase/section of rough cut.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Feedrate Accelerate
 *  Variable Name: <prefix>_feedrate_accelerate
 *
 *   Possible Values: 
 *
 * 
 */
#define UF_PARAM_TURN_FEED_ACCEL   2672  


/* UF_PARAM_TURN_FEED_ACCEL_UNIT
 *
 *   Description:
 *      Feedrate unit for acceleration phase/section of rough cut.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Feedrate Accelerate Unit
 *  Variable Name: <prefix>_feedrate_accelerate_unit
 *
 *   Possible Values: UF_PARAM_feed_unit_t
 *
 * 
 */
#define UF_PARAM_TURN_FEED_ACCEL_UNIT   2673  


/* UF_PARAM_TURN_FEED_ACCEL_LENGTH
 *
 *   Description:
 *      Length of acceleration phase/section of rough cut,
 *      i.e., the portion of the roughing motion that the 
 *      tool shall perform at 'Acceleration Feedrate'.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Feedrate Accelerate Length
 *  Variable Name: <prefix>_feedrate_accelerate_length
 *
 *   Possible Values: 
 *
 * 
 */
#define UF_PARAM_TURN_FEED_ACCEL_LENGTH   2674  


/* UF_PARAM_TURN_FEED_DECEL
 *
 *   Description:
 *      Feedrate for deceleration section of rough cut.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Feedrate Decelerate
 *  Variable Name: <prefix>_feedrate_decelerate
 *
 *   Possible Values: 
 *
 * 
 */
#define UF_PARAM_TURN_FEED_DECEL   2675  


/* UF_PARAM_TURN_FEED_DECEL_UNIT
 *
 *   Description:
 *      Feedrate unit for deceleration section of rough cut.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Feedrate Decelerate Unit
 *  Variable Name: <prefix>_feedrate_decelerate_unit
 *
 *   Possible Values: UF_PARAM_feed_unit_t
 *
 * 
 */
#define UF_PARAM_TURN_FEED_DECEL_UNIT   2676  


/* UF_PARAM_TURN_FEED_DECEL_LENGTH
 *
 *   Description:
 *      Length of deceleration section of rough cut.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Feedrate Decelerate Length
 *  Variable Name: <prefix>_feedrate_decelerate_length
 *
 *   Possible Values: 
 *
 * 
 */
#define UF_PARAM_TURN_FEED_DECEL_LENGTH   2677  


typedef enum UF_PARAM_turn_feed_accel_length_unit_e
{
    UF_PARAM_turn_feed_accel_length_unit_length = 0,
    UF_PARAM_turn_feed_accel_length_unit_percent
} UF_PARAM_turn_feed_accel_length_unit_t;

/* UF_PARAM_TURN_FEED_ACCEL_LENGTH_UNIT
 *
 *   Description:
 *      Unit for length of acceleration section of rough cut.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Feedrate Accelerate Length Unit
 *  Variable Name: <prefix>_feedrate_accelerate_length_unit
 *
 *   Possible Values: UF_PARAM_turn_feed_accel_length_unit_t
 *
 * 
 */
#define UF_PARAM_TURN_FEED_ACCEL_LENGTH_UNIT   2678  


typedef enum UF_PARAM_turn_feed_decel_length_unit_e
{
    UF_PARAM_turn_feed_decel_length_unit_length = 0,
    UF_PARAM_turn_feed_decel_length_unit_percent
} UF_PARAM_turn_feed_decel_length_unit_t;

/* UF_PARAM_TURN_FEED_DECEL_LENGTH_UNIT
 *
 *   Description:
 *      Unit for length of acceleration section of rough cut.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Feedrate Decelerate Length Unit
 *  Variable Name: <prefix>_feedrate_decelerate_length_unit
 *
 *   Possible Values: UF_PARAM_turn_feed_decel_length_unit_t
 *
 * 
 */
#define UF_PARAM_TURN_FEED_DECEL_LENGTH_UNIT   2679  


/* UF_PARAM_TURN_MACH_MOTION
 *
 *   Description:
 *      This parameter controls whether motions are output as lines and arcs
 *      or whether motions are only ouput as lines (linearization of arcs).
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Machine Control Motion Output
 *  Variable Name: <prefix>_machine_control_motion_output
 *
 *   Possible Values: 
 *     0 = Linear output only
 *     1 = Linear and circular motions output
 *
 * 
 */
#define UF_PARAM_TURN_MACH_MOTION   2680  /* UF_PARAM_type_int */


typedef enum UF_PARAM_turn_mach_init_track_e
{
    UF_PARAM_turn_mach_init_track_left = 0,
    UF_PARAM_turn_mach_init_track_right
} UF_PARAM_turn_mach_init_track_t;

/* UF_PARAM_TURN_MACH_INIT_TRACK
 *
 *   Description:
 *      Defines the initial tracking side when using a grooving tool.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Machine Control Initial Track Side
 *  Variable Name: <prefix>_machine_control_initial_track_side
 *
 *   Possible Values: UF_PARAM_turn_mach_init_track_t
 *
 * 
 */
#define UF_PARAM_TURN_MACH_INIT_TRACK   2683  /* UF_PARAM_type_int */


/* UF_PARAM_TURN_MACH_AUTOSWITCH
 *
 *   Description:
 *      Controls automatic switching of tracking sides for grooving tools.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Machine Control Autoswitch Tracking Side
 *  Variable Name: <prefix>_machine_control_autoswitch_tracking_side
 *
 *   Possible Values: 
 *     0 = inactive
 *     1 = active
 *
 * 
 */
#define UF_PARAM_TURN_MACH_AUTOSWITCH   2684  /* UF_PARAM_type_int */


/* UF_PARAM_TURN_MACH_AT_NOSE
 *
 *   Description:
 *      Controls which nose radius of a form tool is used for tool tracking.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Machine Control At Nose Radius
 *  Variable Name: <prefix>_machine_control_at_nose_radius
 *
 *   Possible Values: Value must match existing nose radius of used form tool.
 *
 * 
 */
#define UF_PARAM_TURN_MACH_AT_NOSE   2685  /* UF_PARAM_type_int */


/* UF_PARAM_TURN_MACH_ADJUST_TOG
 *
 *   Description:
 *      Controls use of adjust register.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Machine Control Adjust Reg. Toggle
 *  Variable Name: <prefix>_machine_control_adjust_reg__toggle
 *
 *   Possible Values: 
 *     0 = inactive
 *     1 = active
 *
 * 
 */
#define UF_PARAM_TURN_MACH_ADJUST_TOG   2686  /* UF_PARAM_type_int */


/* UF_PARAM_TURN_MACH_ADJUST
 *
 *   Description:
 *      Defines the adjust register value to be used.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Machine Control Adjust Reg.
 *  Variable Name: <prefix>_machine_control_adjust_reg_
 *
 *   Possible Values: 
 *
 * 
 */
#define UF_PARAM_TURN_MACH_ADJUST   2687  /* UF_PARAM_type_int */


/* UF_PARAM_TURN_MACH_CUTCOM_TOG
 *
 *   Description:
 *      Controls use of cutter compensation register.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Machine Control CUTCOM  Reg. Toggle
 *  Variable Name: <prefix>_machine_control_cutcom__reg__toggle
 *
 *   Possible Values: 
 *     0 = inactive
 *     1 = active
 *
 * 
 */
#define UF_PARAM_TURN_MACH_CUTCOM_TOG   2688  


/* UF_PARAM_TURN_MACH_CUTCOM
 *
 *   Description:
 *      Defines the cutter compensation register to be used.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Machine Control CUTCOM  Reg.
 *  Variable Name: <prefix>_machine_control_cutcom__reg_
 *
 *   Possible Values: 
 *
 * 
 */
#define UF_PARAM_TURN_MACH_CUTCOM   2689  


/* UF_PARAM_TURN_MACH_ADJUST_2_TOG
 *
 *   Description:
 *      Controls use of the second adjust register for groove tools.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Machine Control Adjust Reg. 2 Toggle
 *  Variable Name: <prefix>_machine_control_adjust_reg__2_toggle
 *
 *   Possible Values: 
 *     0 = inactive
 *     1 = active
 *
 * 
 */
#define UF_PARAM_TURN_MACH_ADJUST_2_TOG   2690  


/* UF_PARAM_TURN_MACH_ADJUST_2
 *
 *   Description:
 *      Defines the second adjust register to be used for groove tools.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Machine Control Adjust Reg. 2
 *  Variable Name: <prefix>_machine_control_adjust_reg__2
 *
 *   Possible Values: 
 *
 * 
 */
#define UF_PARAM_TURN_MACH_ADJUST_2   2691  


/* UF_PARAM_TURN_MACH_CUTCOM_2_TOG
 *
 *   Description:
 *      Controls use of the second cutter compensation register for groove tools.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Machine Control CUTCOM  Reg. 2 Toggle
 *  Variable Name: <prefix>_machine_control_cutcom__reg__2_toggle
 *
 *   Possible Values: 
 *     0 = inactive
 *     1 = active
 *
 * 
 */
#define UF_PARAM_TURN_MACH_CUTCOM_2_TOG   2692  


/* UF_PARAM_TURN_MACH_CUTCOM_2
 *
 *   Description:
 *      Defines the second cutter compensation register to be used for groove tools.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Machine Control CUTCOM  Reg. 2
 *  Variable Name: <prefix>_machine_control_cutcom__reg__2
 *
 *   Possible Values: 
 *
 * 
 */
#define UF_PARAM_TURN_MACH_CUTCOM_2   2693  


/* UF_PARAM_TURN_MACH_USE_MACHINE
 *
 *   Description:
 *      Controls use of machine cycle output for threading and centerline
 *      drilling operations.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Machine Control Use Machine Cycle
 *  Variable Name: <prefix>_machine_control_use_machine_cycle
 *
 *   Possible Values: 
 *     0 = inactive
 *     1 = active
 *
 * 
 */
#define UF_PARAM_TURN_MACH_USE_MACHINE   2694  


/* UF_PARAM_TURN_MACH_ADDITIONAL
 *
 *   Description:
 *      Holds additional text for activated machine cycle.
 *
 *   Type: UF_PARAM_type_string
 *
 *   Name: Machine Control Additional Commands
 *  Variable Name: <prefix>_machine_control_additional_commands
 *
 *   Possible Values: 
 *
 * 
 */
#define UF_PARAM_TURN_MACH_ADDITIONAL   2695  


/* UF_PARAM_TURN_FEED_ACCEL_LENGTH_PERCENT
 *
 *   Description:
 *      Value for acceleration length using unit "percent"
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Feedrate Accelerate Length Percent
 *  Variable Name: <prefix>_feedrate_accelerate_length_percent
 *
 *   Possible Values: 
 *
 * 
 */
#define UF_PARAM_TURN_FEED_ACCEL_LENGTH_PERCENT   2698  


/* UF_PARAM_TURN_FEED_DECEL_LENGTH_PERCENT
 *
 *   Description:
 *      Value for deceleration length using unit "percent"
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Feedrate Decelerate Length Percent
 *  Variable Name: <prefix>_feedrate_decelerate_length_percent
 *
 *   Possible Values: 
 *
 * 
 */
#define UF_PARAM_TURN_FEED_DECEL_LENGTH_PERCENT   2699  


/* UF_PARAM_TURN_LOCAL_FREQUENCY
 *
 *   Description:
 *      IMPORTANT: This parameter is obsolete. Use 
 *                 UF_PARAM_TURN_LOCAL_NO_OF_PASSES instead.
 * 
 *      Defines frequence for local return moves
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Turn Local Return Frequency
 *  Variable Name: <prefix>_turn_local_return_frequency
 *
 *   Possible Values: 
 *
 * 
 */
#define UF_PARAM_TURN_LOCAL_FREQUENCY   2700  


/* UF_PARAM_TURN_LOCAL_LOCAL_RET_PT
 *
 *   Description:
 *      Controls use of the local return point
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Local Return Point Flag
 *  Variable Name: <prefix>_local_return_point_flag
 *
 *   Possible Values: 
 *     0 = inactive
 *     1 = active
 *
 * 
 */
#define UF_PARAM_TURN_LOCAL_LOCAL_RET_PT   2701  


/* UF_PARAM_TURN_LOCAL_OPSTOP
 *
 *   Description:
 *      Controls use of Opstop event in local return
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Local Return Opstop
 *  Variable Name: <prefix>_local_return_opstop
 *
 *   Possible Values: 
 *     0 = inactive
 *     1 = active
 *
 * 
 */
#define UF_PARAM_TURN_LOCAL_OPSTOP   2702  


/* UF_PARAM_TURN_LOCAL_OPSKIP
 *
 *   Description:
 *      Controls use of Opskip event in local return.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Local Return Opskip
 *  Variable Name: <prefix>_local_return_opskip
 *
 *   Possible Values: 
 *     0 = inactive
 *     1 = active
 *
 * 
 */
#define UF_PARAM_TURN_LOCAL_OPSKIP   2703  


/* UF_PARAM_TURN_LOCAL_OPERATOR_MSG_TOG
 *
 *   Description:
 *      Controls use of operator message in local return.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Local Return Operator Flag
 *  Variable Name: <prefix>_local_return_operator_flag
 *
 *   Possible Values: 
 *     0 = inactive
 *     1 = active
 *
 * 
 */
#define UF_PARAM_TURN_LOCAL_OPERATOR_MSG_TOG   2704  


/* UF_PARAM_TURN_LOCAL_OPERATOR_MSG
 *
 *   Description:
 *      Defines the operator message for local return.
 *
 *   Type: UF_PARAM_type_string
 *
 *   Name: Local Return Operator Message
 *  Variable Name: <prefix>_local_return_operator_message
 *
 *   Possible Values: 
 *
 * 
 */
#define UF_PARAM_TURN_LOCAL_OPERATOR_MSG   2705  


/* UF_PARAM_TURN_LOCAL_STOP
 *
 *   Description:
 *      Controls use of Stop event in local return
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Local Return Stop
 *  Variable Name: <prefix>_local_return_stop
 *
 *   Possible Values: 
 *     0 = inactive
 *     1 = active
 *
 * 
 */
#define UF_PARAM_TURN_LOCAL_STOP   2706 


/* UF_PARAM_FEED_MAX_APPROACH_LEN_FLAG
 *
 *   Description:
 *      Activates the parameter UF_PARAM_FEED_MAX_APPROACH_LEN.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Feed Max Approach Length Flag
 *  Variable Name: <prefix>_feed_max_approach_length_flag
 *
 *   Possible Values: 
 *     0 = inactive
 *     1 = active
 *
 * 
 */
#define UF_PARAM_FEED_MAX_APPROACH_LEN_FLAG   2708 


/* UF_PARAM_FEED_MIN_ACCELERATE_DECELERATE_LEN_FLAG
 *
 *   Description:
 *      Activates the parameter UF_PARAM_FEED_MIN_ACCELERATE_DECELERATE_LEN.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Feed Feed Min Accelerate Decelerate Length Flag
 *  Variable Name: <prefix>_feed_feed_min_accelerate_decelerate_length_flag
 *
 *   Possible Values: 
 *     0 = inactive
 *     1 = active
 *
 * 
 */
#define UF_PARAM_FEED_MIN_ACCELERATE_DECELERATE_LEN_FLAG   2715 


/* UF_PARAM_TURN_LOCAL_DWELL_FLAG
 *
 *   Description:
 *      Controls use of dwell settings for local return.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Local Return Dwell Flag
 *  Variable Name: <prefix>_local_return_dwell_flag
 *
 *   Possible Values: 
 *     0 = inactive
 *     1 = active
 *
 * 
 */
#define UF_PARAM_TURN_LOCAL_DWELL_FLAG   2710  


/* UF_PARAM_TURN_LOCAL_DWELL
 *
 *   Description:
 *      Defines length of dwell for local return.
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Local Return Dwell
 *  Variable Name: <prefix>_local_return_dwell
 *
 *   Possible Values: 
 *
 * 
 */
#define UF_PARAM_TURN_LOCAL_DWELL   2711  


typedef enum UF_PARAM_turn_local_dwell_e
{
    UF_PARAM_turn_local_dwell_seconds = 0,
    UF_PARAM_turn_local_dwell_revolutions
} UF_PARAM_turn_local_dwell_t;

/* UF_PARAM_TURN_LOCAL_DWELL_UNIT
 *
 *   Description:
 *      Defines the unit for dwell in local return.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Local Return Dwell Unit
 *  Variable Name: <prefix>_local_return_dwell_unit
 *
 *   Possible Values: UF_PARAM_turn_local_dwell_t
 *
 * 
 */
#define UF_PARAM_TURN_LOCAL_DWELL_UNIT   2712  


typedef enum
{
    UF_PARAM_topr_local_frequency_mode_per_cut = 0,
    UF_PARAM_topr_local_frequency_mode_per_pass
} UF_PARAM_topr_local_frequency_mode_t;

/* UF_PARAM_TURN_LOCAL_FREQUENCY_MODE
 *
 *  Description:
 *      IMPORTANT: This parameter is obsolete. It will be consolidated in  
 *                 new parameter UF_PARAM_TURN_LOCAL_MODE.
 *
 *     This parameter is only available in the Rough/Plunge modes.
 *     It specifies if parameter UF_PARAM_TURN_LOCAL_FREQUENCY defines if the
 *     Local Return frequency is interpreted per Plunge cut or per Plunge pass.
 *
 *  Type: Param_type_int
 *
 *  Name: Local Return Frequency Mode
 *  Variable Name: <prefix>_local_return_frequency_mode
 *
 *  Possible Values: UF_PARAM_topr_local_frequency_mode_t
 *
 * 
 */
#define UF_PARAM_TURN_LOCAL_FREQUENCY_MODE   2713 


/* UF_PARAM_TURN_TRACKING_CHANGE_IN_ROUGHING_TOG
 *
 *   Description:
 *      Lets you activate the automatic change of tracking side/points in roughing operations.
 *      Notice that in finishing or additional profiling the automatic change of tracking is always
 *      active if two tracking points have been selected for the operation.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Turn Tracking Change In Roughing Flag
 *  Variable Name: <prefix>_turn_tracking_change_in_roughing_flag
 *
 *   Possible Values: 
 *     0 = inactive
 *     1 = active
 *
 * 
 */
#define UF_PARAM_TURN_TRACKING_CHANGE_IN_ROUGHING_TOG   2717  


/* UF_PARAM_TURN_TRACKING_CHANGE_ACTIVATION_DISTANCE
 *
 *   Description:
 *      Defines the distance from "walls" below which the automatic change of the
 *      tracking side is triggered in roughing operations.
 *      This parameter is only valid for plunge roughing operations.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Turn Tracking Change Activation Distance
 *  Variable Name: <prefix>_turn_tracking_change_activation_distance
 *
 *   Possible Values: double (positive)
 *                    double  zero (activation distance inactive)
 *
 * 
 */
#define UF_PARAM_TURN_TRACKING_CHANGE_ACTIVATION_DISTANCE   2718 


/* UF_PARAM_TURN_TRACKING_CHANGE_MIN_CUT_LENGTH
 *
 *   Description:
 *      Defines the minimum cut length for automatic change of the tracking side
 *      in roughing operations. An automatic change of tracking points is not 
 *      made unless the plunge cut length exceeds the "minimum cut length for
 *      tracking change".
 *      This parameter is only valid for plunge roughing operations.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Turn Tracking Change Minimum Cut Length
 *  Variable Name: <prefix>_turn_tracking_change_minimum_cut_length
 *
 *   Possible Values: double (positive) 
 *                    double  zero (minimum cut length not considered for automatic change of tracking)
 *
 * 
 */
#define UF_PARAM_TURN_TRACKING_CHANGE_MIN_CUT_LENGTH   2719 


/* UF_PARAM_TURN_FINISH_STATUS
 *
 *   Description:
 *      Controls use of local return during profiling.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Turn Finish Local Return Status
 *  Variable Name: <prefix>_turn_finish_local_return_status
 *
 *   Possible Values: 
 *     0 = inactive
 *     1 = active
 *
 * 
 */
#define UF_PARAM_TURN_FINISH_STATUS   2720  


/* UF_PARAM_TURN_FINISH_LOCAL_FREQUENCY
 *
 *   Description:
 *      IMPORTANT: This parameter is obsolete. Use 
 *                 UF_PARAM_TURN_FINISH_LOCAL_NO_OF_PASSES instead.
 *
 *      Defines the frequency for local return moves during profiling.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Turn Finish Local Return Frequency
 *  Variable Name: <prefix>_turn_finish_local_return_frequency
 *
 *   Possible Values: 
 *
 * 
 */
#define UF_PARAM_TURN_FINISH_LOCAL_FREQUENCY   2721  


/* UF_PARAM_TURN_FINISH_LOCAL_RET_PT_STATUS
 *
 *   Description:
 *      Controls use of local return point during profiling.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Turn Finish Local Return Point Flag
 *  Variable Name: <prefix>_turn_finish_local_return_point_flag
 *
 *   Possible Values: 
 *     0 = inactive
 *     1 = active
 *
 * 
 */
#define UF_PARAM_TURN_FINISH_LOCAL_RET_PT_STATUS   2722  


/* UF_PARAM_TURN_FINISH_LOCAL_RTN_PT
 *
 *   Description:
 *      Identifies the local return point for profiling.
 *
 *   Type: UF_PARAM_type_tag
 *
 *   Name: Turn Finish Local Return Point
 *  Variable Name: <prefix>_turn_finish_local_return_point
 *
 *   Possible Values: 
 *
 * 
 */
#define UF_PARAM_TURN_FINISH_LOCAL_RTN_PT   2723  


typedef enum UF_PARAM_turn_finish_loc_rtn_mv_e
{
    UF_PARAM_turn_finish_loc_rtn_mv_none = -1,
    UF_PARAM_turn_finish_loc_rtn_mv_direct = 0,
    UF_PARAM_turn_finish_loc_rtn_mv_radial_axial,
    UF_PARAM_turn_finish_loc_rtn_mv_axial_radial,
    UF_PARAM_turn_finish_loc_rtn_mv_clear_radial_direct,
    UF_PARAM_turn_finish_loc_rtn_mv_clear_axial_direct,
    UF_PARAM_turn_finish_loc_rtn_mv_clear_radial_only,
    UF_PARAM_turn_finish_loc_rtn_mv_clear_axial_only,
    UF_PARAM_turn_finish_loc_rtn_mv_radial_clear_axial_direct,
    UF_PARAM_turn_finish_loc_rtn_mv_radial_axial_radial,
    UF_PARAM_turn_finish_loc_rtn_mv_radial_clear_axial
} UF_PARAM_turn_finish_loc_rtn_mv_t;

/* UF_PARAM_TURN_FINISH_LOC_RTN_MV
 *
 *   Description:
 *      Defines the local return move type for profiling.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Turn Finish Local Return Move Status
 *  Variable Name: <prefix>_turn_finish_local_return_move_status
 *
 *   Possible Values: UF_PARAM_turn_finish_loc_rtn_mv_t
 *
 * 
 */
#define UF_PARAM_TURN_FINISH_LOC_RTN_MV   2724  


/* UF_PARAM_TURN_FINISH_LOCAL_OPSTOP
 *
 *   Description:
 *      Controls use of OPSTOP in local return during profiling.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Turn Finish Local Return Opstop
 *  Variable Name: <prefix>_turn_finish_local_return_opstop
 *
 *   Possible Values: 
 *     0 = inactive
 *     1 = active
 *
 * 
 */
#define UF_PARAM_TURN_FINISH_LOCAL_OPSTOP   2725  


/* UF_PARAM_TURN_FINISH_LOCAL_OPSKIP
 *
 *   Description:
 *      Controls use of OPSKIP in local return during profiling.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Turn Finish Local Return Opskip
 *  Variable Name: <prefix>_turn_finish_local_return_opskip
 *
 *   Possible Values: 
 *     0 = inactive
 *     1 = active
 *
 * 
 */
#define UF_PARAM_TURN_FINISH_LOCAL_OPSKIP   2726  


/* UF_PARAM_TURN_FINISH_LOCAL_OPERATOR_MSG_TOG
 *
 *   Description:
 *      Controls use of operator message in local return during profiling.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Turn Finish Local Return Operator Flag
 *  Variable Name: <prefix>_turn_finish_local_return_operator_flag
 *
 *   Possible Values: 
 *     0 = inactive
 *     1 = active
 *
 * 
 */
#define UF_PARAM_TURN_FINISH_LOCAL_OPERATOR_MSG_TOG   2727  


/* UF_PARAM_TURN_FINISH_LOCAL_OPERATOR_MSG
 *
 *   Description:
 *      Defines the operator message for local return during profiling.
 *
 *   Type: UF_PARAM_type_string
 *
 *   Name: Turn Finish Local Return Operator Message
 *  Variable Name: <prefix>_turn_finish_local_return_operator_message
 *
 *   Possible Values: 
 *
 * 
 */
#define UF_PARAM_TURN_FINISH_LOCAL_OPERATOR_MSG   2728  


/* UF_PARAM_TURN_FINISH_LOCAL_DWELL_FLAG
 *
 *   Description:
 *      Controls use of dwell for local return during profiling.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Turn Finish Local Return Dwell Flag
 *  Variable Name: <prefix>_turn_finish_local_return_dwell_flag
 *
 *   Possible Values: 
 *     0 = inactive
 *     1 = active
 *
 * 
 */
#define UF_PARAM_TURN_FINISH_LOCAL_DWELL_FLAG   2729  


/* UF_PARAM_TURN_FINISH_LOCAL_DWELL
 *
 *   Description:
 *      Defines length of dwell for local return during profiling.
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Turn Finish Local Return Dwell
 *  Variable Name: <prefix>_turn_finish_local_return_dwell
 *
 *   Possible Values: 
 *
 * 
 */
#define UF_PARAM_TURN_FINISH_LOCAL_DWELL   2730  


typedef enum UF_PARAM_turn_finish_local_dwell_e
{
    UF_PARAM_turn_finish_local_dwell_seconds = 0,
    UF_PARAM_turn_finish_local_dwell_revolutions
} UF_PARAM_turn_finish_local_dwell_t;

/* UF_PARAM_TURN_FINISH_LOCAL_DWELL_UNIT
 *
 *   Description:
 *      Defines unit for dwell for local return during profiling.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Turn Finish Local Return Dwell Unit
 *  Variable Name: <prefix>_turn_finish_local_return_dwell_unit
 *
 *   Possible Values: UF_PARAM_turn_finish_local_dwell_t
 *
 * 
 */
#define UF_PARAM_TURN_FINISH_LOCAL_DWELL_UNIT   2731  


/* UF_PARAM_TURN_FINISH_LOCAL_RTN_ORDER
 *
 *   Description:
 *      Defines sequence for local return output during profiling.
 *
 *   Type: UF_PARAM_type_vla_int
 *
 *   Name: Turn Finish Local Return Point Output Order
 *  Variable Name: <prefix>_turn_finish_local_return_point_output_order
 *
 *   Possible Values: (array size 5)
 *
 * 
 */
#define UF_PARAM_TURN_FINISH_LOCAL_RTN_ORDER   2732  


/* UF_PARAM_TURN_FINISH_LOCAL_STOP
 *
 *   Description:
 *      Controls use of STOP in local return during profiling.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Turn Finish Local Return Stop
 *  Variable Name: <prefix>_turn_finish_local_return_stop
 *
 *   Possible Values: 
 *     0 = inactive
 *     1 = active
 *
 * 
 */
#define UF_PARAM_TURN_FINISH_LOCAL_STOP   2733 


/* UF_PARAM_TURN_CONTOUR_FACE_MIN
 *
 *   Description:
 *      Minimum angle for contour class "Face" in turning.
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Contour Classes Face Min.
 *  Variable Name: <prefix>_contour_classes_face_min_
 *
 *   Possible Values: angle in degree
 *
 * 
 */
#define UF_PARAM_TURN_CONTOUR_FACE_MIN   2740  


/* UF_PARAM_TURN_CONTOUR_FACE_MAX
 *
 *   Description:
 *      Maximum angle for contour class "Face" in turning. 
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Contour Classes Face Max.
 *  Variable Name: <prefix>_contour_classes_face_max_
 *
 *   Possible Values: angle in degree
 *
 * 
 */
#define UF_PARAM_TURN_CONTOUR_FACE_MAX   2741  


/* UF_PARAM_TURN_CONTOUR_DIAMETER_MIN
 *
 *   Description:
 *      Minimum angle for contour class "Diameter" in turning.
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Contour Classes Diameter Min.
 *  Variable Name: <prefix>_contour_classes_diameter_min_
 *
 *   Possible Values: angle in degree
 *
 * 
 */
#define UF_PARAM_TURN_CONTOUR_DIAMETER_MIN   2742  


/* UF_PARAM_TURN_CONTOUR_DIAMETER_MAX
 *
 *   Description:
 *      Maximum angle for contour class "Diameter" in turning.
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Contour Classes Diameter Max.
 *  Variable Name: <prefix>_contour_classes_diameter_max_
 *
 *   Possible Values: angle in degree
 *
 * 
 */
#define UF_PARAM_TURN_CONTOUR_DIAMETER_MAX   2743  


/* UF_PARAM_TURN_CONTOUR_STEEP_MIN
 *
 *   Description:
 *      Minimum angle for contour class "Steep" in turning.
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Contour Classes Steep Min.
 *  Variable Name: <prefix>_contour_classes_steep_min_
 *
 *   Possible Values: angle in degree
 *
 * 
 */
#define UF_PARAM_TURN_CONTOUR_STEEP_MIN   2744  


/* UF_PARAM_TURN_CONTOUR_STEEP_MAX
 *
 *   Description:
 *      Maximum angle for contour class "Steep" in turning.
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Contour Classes Steep Max.
 *  Variable Name: <prefix>_contour_classes_steep_max_
 *
 *   Possible Values: angle in degree
 *
 * 
 */
#define UF_PARAM_TURN_CONTOUR_STEEP_MAX   2745  


/* UF_PARAM_TURN_CONTOUR_LEVEL_MIN
 *
 *   Description:
 *      Minimum angle for contour class "Level" in turning.
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Contour Classes Level Min.
 *  Variable Name: <prefix>_contour_classes_level_min_
 *
 *   Possible Values: angle in degree
 *
 * 
 */
#define UF_PARAM_TURN_CONTOUR_LEVEL_MIN   2746  


/* UF_PARAM_TURN_CONTOUR_LEVEL_MAX
 *
 *   Description:
 *      Maximum angle for contour class "Level" in turning.
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Contour Classes Level Max.
 *  Variable Name: <prefix>_contour_classes_level_max_
 *
 *   Possible Values: angle in degree
 *
 * 
 */
#define UF_PARAM_TURN_CONTOUR_LEVEL_MAX   2747  


/* UF_PARAM_TURN_APPROACH_PATH_START_EVENTS_FLAGS
 *
 *   Description:
 *      Holds the Start Events (MCE) flags of the approach path.
 *      The array has the maximum element number
 *      MAX_NO_OF_AVOIDANCE_PATH_POINTS.
 *      The start events paths are stored in parameter
 *      UF_PARAM_TURN_APPROACH_PATH_START_EVENTS_PATHS.
 *
 *   Type: UF_PARAM_type_vla_int
 *
 *   Name: Turn Approach Path Start Events Flags
 *  Variable Name: <prefix>_turn_approach_path_start_events_flags
 *
 *   Possible Values: List of ints: 0 -- inactive
 *                                  1 -- active
 *
 * 
 */
#define UF_PARAM_TURN_APPROACH_PATH_START_EVENTS_FLAGS   2750 


/* UF_PARAM_TURN_APPROACH_PATH_START_EVENTS_PATHS
 *
 *   Description:
 *      Holds the Start Events (MCEs) Paths of the approach path.
 *      The array has the maximum element number
 *      MAX_NO_OF_AVOIDANCE_PATH_POINTS.
 *      The Start Events Paths are activated by parameter
 *      UF_PARAM_TURN_APPROACH_PATH_START_EVENTS_FLAGS.
 *
 *   Type: UF_PARAM_type_vla_tag
 *
 *   Name: Turn Approach Path Start Events Paths
 *  Variable Name: <prefix>_turn_approach_path_start_events_paths
 *
 *   Possible Values: List of tags
 *
 * 
 */
#define UF_PARAM_TURN_APPROACH_PATH_START_EVENTS_PATHS   2751 


/* UF_PARAM_TURN_APPROACH_PATH_END_EVENTS_FLAGS
 *
 *   Description:
 *      Holds the End Events (MCE) flags of the approach path.
 *      The array has the maximum element number
 *      MAX_NO_OF_AVOIDANCE_PATH_POINTS.
 *      The End Events Paths are stored in parameter
 *      UF_PARAM_TURN_APPROACH_PATH_END_EVENTS_PATHS.
 *
 *   Type: UF_PARAM_type_vla_int
 *
 *   Name: Turn Approach Path End Events Flags
 *  Variable Name: <prefix>_turn_approach_path_end_events_flags
 *
 *   Possible Values: List of ints: 0 -- inactive
 *                                  1 -- active
 *
 * 
 */
#define UF_PARAM_TURN_APPROACH_PATH_END_EVENTS_FLAGS   2752 


/* UF_PARAM_TURN_APPROACH_PATH_END_EVENTS_PATHS
 *
 *   Description:
 *      Holds the End Events Paths (MCEs) of the approach path.
 *      The array has the maximum element number
 *      MAX_NO_OF_AVOIDANCE_PATH_POINTS.
 *      The End Events Paths are activated by parameter
 *      UF_PARAM_TURN_APPROACH_PATH_END_EVENTS_FLAGS.
 *
 *   Type: UF_PARAM_type_vla_tag
 *
 *   Name: Turn Approach Path End Events Paths
 *  Variable Name: <prefix>_turn_approach_path_end_events_paths
 *
 *   Possible Values: List of tags
 *
 * 
 */
#define UF_PARAM_TURN_APPROACH_PATH_END_EVENTS_PATHS   2753 


/* UF_PARAM_TURN_DEPARTURE_PATH_START_EVENTS_FLAGS
 *
 *   Description:
 *      Holds the Start Events (MCE) flags of the departure path.
 *      The array has the maximum element number
 *      MAX_NO_OF_AVOIDANCE_PATH_POINTS.
 *      The Start Events Paths are stored in parameter
 *      UF_PARAM_TURN_DEPARTURE_PATH_START_EVENTS_PATHS.
 *
 *   Type: UF_PARAM_type_vla_int
 *
 *   Name: Turn Departure Path Start Events Flags
 *  Variable Name: <prefix>_turn_departure_path_start_events_flags
 *
 *   Possible Values: List of ints: 0 -- inactive
 *                                  1 -- active
 *
 * 
 */
#define UF_PARAM_TURN_DEPARTURE_PATH_START_EVENTS_FLAGS   2754 


/* UF_PARAM_TURN_DEPARTURE_PATH_START_EVENTS_PATHS
 *
 *   Description:
 *      Holds the Start Events Paths (MCEs) of the departure path.
 *      The array has the maximum element number
 *      MAX_NO_OF_AVOIDANCE_PATH_POINTS.
 *      The Start Events Paths are activated by parameter
 *      UF_PARAM_TURN_DEPARTURE_PATH_START_EVENTS_FLAGS.
 *
 *   Type: UF_PARAM_type_vla_tag
 *
 *   Name: Turn Departure Path Start Events Paths
 *  Variable Name: <prefix>_turn_departure_path_start_events_paths
 *
 *   Possible Values: List of tags
 *
 * 
 */
#define UF_PARAM_TURN_DEPARTURE_PATH_START_EVENTS_PATHS   2755 


/* UF_PARAM_TURN_DEPARTURE_PATH_END_EVENTS_FLAGS
 *
 *   Description:
 *      Holds the End Events (MCE) flags of the departure path.
 *      The array has the maximum element number
 *      MAX_NO_OF_AVOIDANCE_PATH_POINTS.
 *      The End Events Paths are stored in parameter
 *      UF_PARAM_TURN_DEPARTURE_PATH_END_EVENTS_PATHS.
 *
 *   Type: UF_PARAM_type_vla_int
 *
 *   Name: Turn Departure Path End Events Flags
 *  Variable Name: <prefix>_turn_departure_path_end_events_flags
 *
 *   Possible Values: List of ints: 0 -- inactive
 *                                  1 -- active
 *
 * 
 */
#define UF_PARAM_TURN_DEPARTURE_PATH_END_EVENTS_FLAGS   2756 


/* UF_PARAM_TURN_DEPARTURE_PATH_END_EVENTS_PATHS
 *
 *   Description:
 *      Holds the End Events Paths (MCEs) of the departure path.
 *      The array has the maximum element number
 *      MAX_NO_OF_AVOIDANCE_PATH_POINTS.
 *      The End Events Paths are activated by parameter
 *      UF_PARAM_TURN_DEPARTURE_PATH_END_EVENTS_FLAGS.
 *
 *   Type: UF_PARAM_type_vla_tag
 *
 *   Name: Turn Departure Path End Events Paths
 *  Variable Name: <prefix>_turn_departure_path_end_events_paths
 *
 *   Possible Values: List of tags
 *
 * 
 */
#define UF_PARAM_TURN_DEPARTURE_PATH_END_EVENTS_PATHS   2757 


/* UF_PARAM_TURN_MACH_USE_A_AXIS
 *
 *   Description:
 *      Activates the operation level A-axis setting. A-axis is available if
 *      value is set to 1.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Use A axis
 *  Variable Name: <prefix>_use_a_axis
 *
 *   Possible Values: 0, 1
 *
 * 
 */
#define UF_PARAM_TURN_MACH_USE_A_AXIS   2760  /* UF_PARAM_type_int */


/* UF_PARAM_TURN_MACH_FLIP_A_AXIS
 *
 *   Description:
 *      Specifies the operation level A-axis setting. A-axis is flipped if
 *      value is set to 1.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Flip A axis
 *  Variable Name: <prefix>_flip_a_axis
 *
 *   Possible Values: 0, 1
 *
 * 
 */
#define UF_PARAM_TURN_MACH_FLIP_A_AXIS   2761  /* UF_PARAM_type_int */


/* UF_PARAM_TURN_MACH_USE_B_AXIS
 *
 *   Description:
 *      Activates the operation level B-axis setting. B-axis is available if
 *      value is set to 1.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Use B axis
 *  Variable Name: <prefix>_use_b_axis
 *
 *   Possible Values: 0, 1
 *
 * 
 */
#define UF_PARAM_TURN_MACH_USE_B_AXIS   2762  /* UF_PARAM_type_int */


/* UF_PARAM_TURN_MACH_TL_HOLDER_ANGLE
 *
 *   Description:
 *      Specifies the operation level angle to set the tool holder angle to.
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Tool Holder Angle
 *  Variable Name: <prefix>_tool_holder_angle
 *
 *   Possible Values: double (radians)
 *
 * 
 */
#define UF_PARAM_TURN_MACH_TL_HOLDER_ANGLE   2763  /* UF_PARAM_type_double */


/* UF_PARAM_TURN_MACH_TL_ANGLE
 *
 *   Description:
 *      Specifies the operation level angle between tool center and  the tool tip.
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Tool Mach Angle
 *  Variable Name: <prefix>_tool_mach_angle
 *
 *   Possible Values: double (degrees)
 *
 * 
 */
#define UF_PARAM_TURN_MACH_TL_ANGLE   2764  /* UF_PARAM_type_double */


/* UF_PARAM_TURN_MACH_TL_ANGLE_TOG
 *
 *   Description:
 *      Specifies the operation level toggle for angle between 
 *      tool center and  the tool tip.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Tool Mach Angle Toggle
 *  Variable Name: <prefix>_tool_mach_angle_toggle
 *
 *   Possible Values: 0 -- False
 *                    1 -- True  
 *
 * 
 */
#define UF_PARAM_TURN_MACH_TL_ANGLE_TOG   2765  /* UF_PARAM_type_int */


/* UF_PARAM_TURN_MACH_TL_RADIUS
 *
 *   Description:
 *      Specifies the operation level radius between tool center and  the tool tip.
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Tool Mach Radius
 *  Variable Name: <prefix>_tool_mach_radius
 *
 *   Possible Values: double 
 *
 * 
 */
#define UF_PARAM_TURN_MACH_TL_RADIUS   2766  /* UF_PARAM_type_double */


/* UF_PARAM_TURN_MACH_TL_RADIUS_TOG
 *
 *   Description:
 *      Specifies the operation level toggle for radius between 
 *      tool center and  the tool tip.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Tool Mach Radius Toggle
 *  Variable Name: <prefix>_tool_mach_radius_toggle
 *
 *   Possible Values: 0 -- False
 *                    1 -- True  
 *
 * 
 */
#define UF_PARAM_TURN_MACH_TL_RADIUS_TOG   2767  /* UF_PARAM_type_int */


/* UF_PARAM_TURN_FINISH_LOCAL_MODE
 *
 *   Description:
 *      Defines the mode of Profile Local Return frequency.
 *      For Turn/Rough Plunge operations There are four modes:
 *        Distance, Time, Per Cut and Per Level.
 *      For all other Turn operation there are only three modes:
 *        Distance, Time, No. Passes.
 *      The mode No. of Passes (or Per Cut/Per Level respectively)
 *      correspondes to the legacy (pre NX3) Frequency mode.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Turn Finish Local Return Mode
 *  Variable Name: <prefix>_turn_finish_local_return_mode
 *
 *   Possible Values: UF_PARAM_turn_local_mode_t
 *
 * 
 */
#define UF_PARAM_TURN_FINISH_LOCAL_MODE   2770 


/* UF_PARAM_TURN_FINISH_LOCAL_DISTANCE
 *
 *   Description:
 *      Defines the tool travel distance after which a 
 *      Profile Local Return is triggered.
 *      This parameter is only valid if Local Return mode
 *      (UF_PARAM_TURN_FINISH_LOCAL_MODE) is 'Distance'
 *      (UF_PARAM_turn_local_mode_distance).
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Turn Finish Local Return Distance
 *  Variable Name: <prefix>_turn_finish_local_return_distance
 *
 *   Possible Values: double (positive)
 *
 * 
 */
#define UF_PARAM_TURN_FINISH_LOCAL_DISTANCE   2771 


/* UF_PARAM_TURN_FINISH_LOCAL_TIME
 *
 *   Description:
 *      Defines the tool travel time after which a Profile 
 *      Local Return is triggered.
 *      This parameter is only valid if Local Return mode
 *      (UF_PARAM_TURN_FINISH_LOCAL_MODE) is 'Time'
 *      (UF_PARAM_turn_local_mode_time).
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Turn Finish Local Return Time
 *  Variable Name: <prefix>_turn_finish_local_return_time
 *
 *   Possible Values: double (positive)
 *
 * 
 */
#define UF_PARAM_TURN_FINISH_LOCAL_TIME   2772 


/* UF_PARAM_TURN_FINISH_LOCAL_NO_OF_PASSES
 *
 *   Description:
 *      Defines the number of passes after which a Profile 
 *      Local Return is triggered.
 *      This parameter is only valid if Local Return mode
 *      (UF_PARAM_TURN_FINISH_LOCAL_MODE) is 'No of Passes',
 *      'No of Cuts' or 'No of Levels'
 *      (UF_PARAM_turn_local_mode_no_of_passes,
 *       UF_PARAM_turn_local_mode_no_of_cuts   
 *       UF_PARAM_turn_local_mode_no_of_levels).
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Turn Finish Local Return No of Passes
 *  Variable Name: <prefix>_turn_finish_local_return_no_of_passes
 *
 *   Possible Values: int (positive)
 *
 * 
 */
#define UF_PARAM_TURN_FINISH_LOCAL_NO_OF_PASSES   2773 


/* UF_PARAM_TURN_FINISH_LOCAL_ADJUSTMENT_FLAG
 *
 *   Description:
 *      Defines if Profile Local Return Adjustment is active.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Turn Finish Local Return Adjustment Flag
 *  Variable Name: <prefix>_turn_finish_local_return_adjustment_flag
 *
 *   Possible Values: 0 -- Off
 *                    1 -- On
 *
 * 
 */
#define UF_PARAM_TURN_FINISH_LOCAL_ADJUSTMENT_FLAG   2774 


/* UF_PARAM_TURN_FINISH_LOCAL_ADJUSTMENT_MODE
 *
 *   Description:
 *      Defines the Profile Local Return Adjustment mode.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Turn Finish Local Return Adjustment Mode
 *  Variable Name: <prefix>_turn_finish_local_return_adjustment_mode
 *
 *   Possible Values: UF_PARAM_turn_local_adjustment_mode_t
 *
 * 
 */
#define UF_PARAM_TURN_FINISH_LOCAL_ADJUSTMENT_MODE   2775 


/* UF_PARAM_TURN_FINISH_LOCAL_LOWER_LIMIT_DISTANCE
 *
 *   Description:
 *      Defines the lower limit of Profile Local Return 
 *      adjustment.
 *      This parameter is only valid if Local Return mode
 *      (UF_PARAM_TURN_FINISH_LOCAL_MODE) is 'Distance'
 *      (UF_PARAM_turn_local_mode_distance) and
 *      lower limit mode
 *      (UF_PARAM_TURN_FINISH_LOCAL_LOWER_LIMIT_MODE) is
 *      'Distance or Time'
 *      (UF_PARAM_turn_local_limit_distance_or_time).
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Turn Finish Local Return Lower Limit Distance
 *  Variable Name: <prefix>_turn_finish_local_return_lower_limit_distance
 *
 *   Possible Values: double (negative or zero)
 *
 * 
 */
#define UF_PARAM_TURN_FINISH_LOCAL_LOWER_LIMIT_DISTANCE   2776 


/* UF_PARAM_TURN_FINISH_LOCAL_LOWER_LIMIT_TIME
 *
 *   Description:
 *      Defines the lower limit of Profile Local Return 
 *      adjustment.
 *      This parameter is only valid if Local Return mode
 *      (UF_PARAM_TURN_FINISH_LOCAL_MODE) is 'Time'
 *      (UF_PARAM_turn_local_mode_time) and
 *      lower limit mode
 *      (UF_PARAM_TURN_FINISH_LOCAL_LOWER_LIMIT_MODE) is
 *      'Distance or Time'
 *      (UF_PARAM_turn_local_limit_distance_or_time).
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Turn Finish Local Return Lower Limit Time
 *  Variable Name: <prefix>_turn_finish_local_return_lower_limit_time
 *
 *   Possible Values: double (negative or zero)
 *
 * 
 */
#define UF_PARAM_TURN_FINISH_LOCAL_LOWER_LIMIT_TIME   2777 


/* UF_PARAM_TURN_FINISH_LOCAL_LOWER_LIMIT_PERCENT
 *
 *   Description:
 *      Defines the lower limit of Profile Local Return 
 *      adjustment.
 *      This parameter is only valid if Local Return mode
 *      (UF_PARAM_TURN_FINISH_LOCAL_MODE) is 'Distance' or
 *      'Time' (UF_PARAM_turn_local_mode_distance, 
 *      UF_PARAM_turn_local_mode_time) and
 *      lower limit mode
 *      (UF_PARAM_TURN_FINISH_LOCAL_LOWER_LIMIT_MODE) is
 *      'Percent' (UF_PARAM_turn_local_limit_percent).
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Turn Finish Local Return Lower Limit Percent
 *  Variable Name: <prefix>_turn_finish_local_return_lower_limit_percent
 *
 *   Possible Values: double (negative or zero)
 *
 * 
 */
#define UF_PARAM_TURN_FINISH_LOCAL_LOWER_LIMIT_PERCENT   2778 


/* UF_PARAM_TURN_FINISH_LOCAL_LOWER_LIMIT_MODE
 *
 *   Description:
 *      Defines the lower limit mode of Profile Local Return 
 *      adjustment.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Turn Finish Local Return Lower Limit Percent
 *  Variable Name: <prefix>_turn_finish_local_return_lower_limit_percent
 *
 *   Possible Values: UF_PARAM_turn_local_limit_t
 *
 * 
 */
#define UF_PARAM_TURN_FINISH_LOCAL_LOWER_LIMIT_MODE   2779 


/* UF_PARAM_TURN_FINISH_LOCAL_UPPER_LIMIT_DISTANCE
 *
 *   Description:
 *      Defines the upper limit of Profile Local Return 
 *      adjustment.
 *      This parameter is only valid if Local Return mode
 *      (UF_PARAM_TURN_FINISH_LOCAL_MODE) is 'Distance'
 *      (UF_PARAM_turn_local_mode_distance) and
 *      upper limit mode
 *      (UF_PARAM_TURN_FINISH_LOCAL_UPPER_LIMIT_MODE) is
 *      'Distance or Time'
 *      (UF_PARAM_turn_local_limit_distance_or_time).
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Turn Finish Local Return Upper Limit Distance
 *  Variable Name: <prefix>_turn_finish_local_return_upper_limit_distance
 *
 *   Possible Values: double (positive or zero)
 *
 * 
 */
#define UF_PARAM_TURN_FINISH_LOCAL_UPPER_LIMIT_DISTANCE   2780 


/* UF_PARAM_TURN_FINISH_LOCAL_UPPER_LIMIT_TIME
 *
 *   Description:
 *      Defines the upper limit of Profile Local Return 
 *      adjustment.
 *      This parameter is only valid if Local Return mode
 *      (UF_PARAM_TURN_FINISH_LOCAL_MODE) is 'Time'
 *      (UF_PARAM_turn_local_mode_time) and
 *      upper limit mode
 *      (UF_PARAM_TURN_FINISH_LOCAL_UPPER_LIMIT_MODE) is
 *      'Distance or Time'
 *      (UF_PARAM_turn_local_limit_distance_or_time).
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Turn Finish Local Return Upper Limit Time
 *  Variable Name: <prefix>_turn_finish_local_return_upper_limit_time
 *
 *   Possible Values: double (positive or zero)
 *
 * 
 */
#define UF_PARAM_TURN_FINISH_LOCAL_UPPER_LIMIT_TIME   2781 


/* UF_PARAM_TURN_FINISH_LOCAL_UPPER_LIMIT_PERCENT
 *
 *   Description:
 *      Defines the upper limit of Profile Local Return 
 *      adjustment.
 *      This parameter is only valid if Local Return mode
 *      (UF_PARAM_TURN_FINISH_LOCAL_MODE) is 'Distance' or
 *      'Time' (UF_PARAM_turn_local_mode_distance, 
 *      UF_PARAM_turn_local_mode_time) and
 *      upper limit mode
 *      (UF_PARAM_TURN_FINISH_LOCAL_UPPPER_LIMIT_MODE) is
 *      'Percent' (UF_PARAM_turn_local_limit_percent).
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Turn Finish Local Return Upper Limit Percent
 *  Variable Name: <prefix>_turn_finish_local_return_upper_limit_percent
 *
 *   Possible Values: double (positive or zero)
 *
 * 
 */
#define UF_PARAM_TURN_FINISH_LOCAL_UPPER_LIMIT_PERCENT   2782 


typedef enum UF_PARAM_turn_local_mode_e
{
    UF_PARAM_turn_local_mode_distance     = 0,
    UF_PARAM_turn_local_mode_time         = 1,
    UF_PARAM_turn_local_mode_no_of_passes = 2,
    UF_PARAM_turn_local_mode_no_of_cuts   = 2,
    UF_PARAM_turn_local_mode_no_of_levels = 3
} UF_PARAM_turn_local_mode_t;
#define UF_PARAM_TURN_LOCAL_MODE_INDEX                      2784

/* @HEAD UF_PARAM_TURN_LOCAL_DISTANCE_INDEX EXT
 *
 *   Description:
 *      Defines the tool travel distance after which a Local Return
 *      is triggered.
 *      This parameter is only valid if Local Return mode
 *      (UF_PARAM_TURN_LOCAL_MODE_INDEX) is 'Distance'
 *      (UF_PARAM_turn_local_mode_distance).
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Local Return Distance
 *
 *   Possible Values: double (positive)
 *
 *   Developer: Oliver Bruegge
 */
#define UF_PARAM_TURN_LOCAL_DISTANCE_INDEX                  2785

/* @HEAD UF_PARAM_TURN_LOCAL_TIME_INDEX EXT
 *
 *   Description:
 *      Defines the tool travel time after which a Local Return
 *      is triggered.
 *      This parameter is only valid if Local Return mode
 *      (UF_PARAM_TURN_LOCAL_MODE_INDEX) is 'Time'
 *      (UF_PARAM_turn_local_mode_time).
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Local Return Time
 *
 *   Possible Values: double (positive)
 *
 *   Developer: Oliver Bruegge
 */
#define UF_PARAM_TURN_LOCAL_TIME_INDEX                      2786

/* @HEAD UF_PARAM_TURN_LOCAL_NO_OF_PASSES_INDEX EXT
 *
 *   Description:
 *      Defines the number of passes after which a Local Return
 *      is triggered.
 *      This parameter is only valid if Local Return mode
 *      (UF_PARAM_TURN_LOCAL_MODE_INDEX) is 'No of Passes',
 *      'No of Cuts' or 'No of Levels'
 *      (UF_PARAM_turn_local_mode_no_of_passes,
 *       UF_PARAM_turn_local_mode_no_of_cuts   
 *       UF_PARAM_turn_local_mode_no_of_levels).
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Local Return No of Passes
 *
 *   Possible Values: double (positive)
 *
 *   Developer: Oliver Bruegge
 */
#define UF_PARAM_TURN_LOCAL_NO_OF_PASSES_INDEX              2787

/* @HEAD UF_PARAM_TURN_LOCAL_ADJUSTMENT_FLAG_INDEX EXT
 *
 *   Description:
 *      Defines if Local Return Adjustment is active.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Local Return Adjustment Flag
 *
 *   Possible Values: 0 -- Off
 *                    1 -- On
 *
 *   Developer: Oliver Bruegge
 */
#define UF_PARAM_TURN_LOCAL_ADJUSTMENT_FLAG_INDEX           2788

/* @HEAD UF_PARAM_TURN_LOCAL_ADJUSTMENT_MODE_INDEX EXT
 *
 *   Description:
 *      Defines the Local Return Adjustment mode.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Local Return Adjustment Mode
 *
 *   Possible Values: UF_PARAM_turn_local_adjustment_mode_t
 *
 *   Developer: Oliver Bruegge
 */
typedef enum UF_PARAM_turn_local_adjustment_mode_e
{
    UF_PARAM_turn_local_adjustment_mode_range = 0,
    UF_PARAM_turn_local_adjustment_mode_alignment
} UF_PARAM_turn_local_adjustment_mode_t;
#define UF_PARAM_TURN_LOCAL_ADJUSTMENT_MODE_INDEX           2789

/* @HEAD UF_PARAM_TURN_LOCAL_LOWER_LIMIT_DISTANCE_INDEX EXT
 *
 *   Description:
 *      Defines the lower limit of Local Return adjustment.
 *      This parameter is only valid if Local Return mode
 *      (UF_PARAM_TURN_LOCAL_MODE_INDEX) is 'Distance'
 *      (UF_PARAM_turn_local_mode_distance) and
 *      lower limit mode
 *      (UF_PARAM_TURN_LOCAL_LOWER_LIMIT_MODE_INDEX) is
 *      'Distance or Time'
 *      (UF_PARAM_turn_local_limit_distance_or_time).
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Local Return Lower Limit Distance
 *
 *   Possible Values: double (negative or zero)
 *
 *   Developer: Oliver Bruegge
 */
#define UF_PARAM_TURN_LOCAL_LOWER_LIMIT_DISTANCE_INDEX      2790

/* @HEAD UF_PARAM_TURN_LOCAL_LOWER_LIMIT_TIME_INDEX EXT
 *
 *   Description:
 *      Defines the lower limit of Local Return adjustment.
 *      This parameter is only valid if Local Return mode
 *      (UF_PARAM_TURN_LOCAL_MODE_INDEX) is 'Time'
 *      (UF_PARAM_turn_local_mode_time) and
 *      lower limit mode
 *      (UF_PARAM_TURN_LOCAL_LOWER_LIMIT_MODE_INDEX) is
 *      'Distance or Time'
 *      (UF_PARAM_turn_local_limit_distance_or_time).
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Local Return Lower Limit Time
 *
 *   Possible Values: double (negative or zero)
 *
 *   Developer: Oliver Bruegge
 */
#define UF_PARAM_TURN_LOCAL_LOWER_LIMIT_TIME_INDEX          2791

/* @HEAD UF_PARAM_TURN_LOCAL_LOWER_LIMIT_PERCENT_INDEX EXT
 *
 *   Description:
 *      Defines the lower limit of Local Return adjustment.
 *      This parameter is only valid if Local Return mode
 *      (UF_PARAM_TURN_LOCAL_MODE_INDEX) is 'Distance' or
 *      'Time' (UF_PARAM_turn_local_mode_distance, 
 *      UF_PARAM_turn_local_mode_time) and
 *      lower limit mode
 *      (UF_PARAM_TURN_LOCAL_LOWER_LIMIT_MODE_INDEX) is
 *      'Percent' (UF_PARAM_turn_local_limit_percent).
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Local Return Lower Limit Percent
 *
 *   Possible Values: double (negative or zero)
 *
 *   Developer: Oliver Bruegge
 */
#define UF_PARAM_TURN_LOCAL_LOWER_LIMIT_PERCENT_INDEX       2792

/* @HEAD UF_PARAM_TURN_LOCAL_LOWER_LIMIT_MODE_INDEX EXT
 *
 *   Description:
 *      Defines the lower limit mode of Local Return adjustment.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Local Return Lower Limit Percent
 *
 *   Possible Values: UF_PARAM_turn_local_limit_t
 *
 *   Developer: Oliver Bruegge
 */
typedef enum UF_PARAM_turn_local_limit_mode_e
{
    UF_PARAM_turn_local_limit_distance_or_time = 0,
    UF_PARAM_turn_local_limit_percent
} UF_PARAM_turn_local_limit_t;
#define UF_PARAM_TURN_LOCAL_LOWER_LIMIT_MODE_INDEX          2793

/* @HEAD UF_PARAM_TURN_LOCAL_UPPER_LIMIT_DISTANCE_INDEX EXT
 *
 *   Description:
 *      Defines the upper limit of Local Return adjustment.
 *      This parameter is only valid if Local Return mode
 *      (UF_PARAM_TURN_LOCAL_MODE_INDEX) is 'Distance'
 *      (UF_PARAM_turn_local_mode_distance) and
 *      upper limit mode
 *      (UF_PARAM_TURN_LOCAL_UPPER_LIMIT_MODE_INDEX) is
 *      'Distance or Time'
 *      (UF_PARAM_turn_local_limit_distance_or_time).
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Local Return Upper Limit Distance
 *
 *   Possible Values: double (positive or zero)
 *
 *   Developer: Oliver Bruegge
 */
#define UF_PARAM_TURN_LOCAL_UPPER_LIMIT_DISTANCE_INDEX      2794

/* @HEAD UF_PARAM_TURN_LOCAL_UPPER_LIMIT_TIME_INDEX EXT
 *
 *   Description:
 *      Defines the upper limit of Local Return adjustment.
 *      This parameter is only valid if Local Return mode
 *      (UF_PARAM_TURN_LOCAL_MODE_INDEX) is 'Time'
 *      (UF_PARAM_turn_local_mode_time) and
 *      upper limit mode
 *      (UF_PARAM_TURN_LOCAL_UPPER_LIMIT_MODE_INDEX) is
 *      'Distance or Time'
 *      (UF_PARAM_turn_local_limit_distance_or_time).
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Local Return Upper Limit Time
 *
 *   Possible Values: double (positive or zero)
 *
 *   Developer: Oliver Bruegge
 */
#define UF_PARAM_TURN_LOCAL_UPPER_LIMIT_TIME_INDEX          2795

/* @HEAD UF_PARAM_TURN_LOCAL_UPPER_LIMIT_PERCENT_INDEX EXT
 *
 *   Description:
 *      Defines the upper limit of Local Return adjustment.
 *      This parameter is only valid if Local Return mode
 *      (UF_PARAM_TURN_LOCAL_MODE_INDEX) is 'Distance' or
 *      'Time' (UF_PARAM_turn_local_mode_distance, 
 *      UF_PARAM_turn_local_mode_time) and
 *      upper limit mode
 *      (UF_PARAM_TURN_LOCAL_UPPPER_LIMIT_MODE_INDEX) is
 *      'Percent' (UF_PARAM_turn_local_limit_percent).
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Local Return Upper Limit Percent
 *
 *   Possible Values: double (positive or zero)
 *
 *   Developer: Oliver Bruegge
 */
#define UF_PARAM_TURN_LOCAL_UPPER_LIMIT_PERCENT_INDEX       2796

/* @HEAD UF_PARAM_TURN_LOCAL_UPPER_LIMIT_MODE_INDEX EXT
 *
 *   Description:
 *      Defines the upper limit mode of Local Return adjustment.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Local Return Upper Limit Percent
 *
 *   Possible Values: UF_PARAM_turn_local_limit_t
 *
 *   Developer: Oliver Bruegge
 */

/* UF_PARAM_TURN_LOCAL_UPPER_LIMIT_MODE
 *
 *   Description:
 *      Defines the upper limit mode of Profile 
 *      Local Return adjustment.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Turn Finish Local Return Upper Limit Percent
 *
 *   Possible Values: UF_PARAM_turn_local_limit_t
 *
 * 
 */
#define UF_PARAM_TURN_LOCAL_UPPER_LIMIT_MODE   2797 


typedef enum UF_PARAM_tropr_cut_strategy_e
{
    UF_PARAM_tropr_cut_strategy_level_zig = 0,
    UF_PARAM_tropr_cut_strategy_level_zig_zag,
    UF_PARAM_tropr_cut_strategy_contour_zig,
    UF_PARAM_tropr_cut_strategy_contour_zig_zag,
    UF_PARAM_tropr_cut_strategy_plunge_zig,
    UF_PARAM_tropr_cut_strategy_plunge_alt,
    UF_PARAM_tropr_cut_strategy_plunge_castleing,
    UF_PARAM_tropr_cut_strategy_plunge_zig_zag,
    UF_PARAM_tropr_cut_strategy_ramping_zig,
    UF_PARAM_tropr_cut_strategy_ramping_zig_zag
} UF_PARAM_tropr_cut_strategy_t;

/* UF_PARAM_TROPR_CUT_STRATEGY
 *
 *   Description:
 *      Rough cut strategy
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Roughing Cut Method
 *  Variable Name: <prefix>_roughing_cut_method
 *
 *   Possible Values: UF_PARAM_tropr_cut_strategy_t
 *
 * 
 */
#define UF_PARAM_TROPR_CUT_STRATEGY   2800  /* Param_type_int */


typedef enum UF_PARAM_turn_stepover_e
{
    UF_PARAM_turn_stepover_level_constant       = 0,
    UF_PARAM_turn_stepover_level_var_max        = 1,
    UF_PARAM_turn_stepover_level_var_avg        = 2,
    UF_PARAM_turn_stepover_level_no_of_levels   = 3,
    UF_PARAM_turn_stepover_level_individual     = 4,
    UF_PARAM_turn_stepover_ramp_constant        = 0,
    UF_PARAM_turn_stepover_ramp_var_max         = 1,
    UF_PARAM_turn_stepover_ramp_var_avg         = 2,
    UF_PARAM_turn_stepover_contour_constant     = 0,
    UF_PARAM_turn_stepover_contour_no_of_levels = 1,
    UF_PARAM_turn_stepover_contour_individual   = 2,
    UF_PARAM_turn_stepover_plunge_constant      = 0,
    UF_PARAM_turn_stepover_plunge_var_max       = 1,
    UF_PARAM_turn_stepover_plunge_var_avg       = 2
} UF_PARAM_turn_stepover_t;

/* UF_PARAM_TURN_STEPOVER
 *
 *   Description:
 *      Defines the stepover type. Interpretation depends on the cut strategy
 *      selected.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Stepover
 *  Variable Name: <prefix>_stepover
 *
 *   Possible Values: UF_PARAM_turn_stepover_t
 *
 * 
 */
#define UF_PARAM_TURN_STEPOVER   2810  /* Param_type_double_length */


/* UF_PARAM_TURN_CUT_DEPTH
 *
 *   Description:
 *      Defines cut depth for constant stepover.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Cut Depth
 *  Variable Name: <prefix>_cut_depth
 *
 *   Possible Values: 
 *
 * 
 */
#define UF_PARAM_TURN_CUT_DEPTH   2811  /* Param_type_double_length */


/* UF_PARAM_TURN_MINIMUM
 *
 *   Description:
 *      Minimum cut depth for variable stepover and ramping
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Minimum
 *  Variable Name: <prefix>_minimum
 *
 *   Possible Values: 
 *
 * 
 */
#define UF_PARAM_TURN_MINIMUM   2812  


/* UF_PARAM_TURN_MAXIMUM
 *
 *   Description:
 *      Maximum cut depth for variable stepover and ramping
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Maximum
 *  Variable Name: <prefix>_maximum
 *
 *   Possible Values: 
 *
 * 
 */
#define UF_PARAM_TURN_MAXIMUM   2813  


/* UF_PARAM_TURN_NO_OF_LEVELS
 *
 *   Description:
 *      Number of cuts for turn roughing operations.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: No. of Levels
 *  Variable Name: <prefix>_no__of_levels
 *
 *   Possible Values: 
 *
 * 
 */
#define UF_PARAM_TURN_NO_OF_LEVELS   2814  


/* UF_PARAM_TURN_NO_OF_ADD_PASSES
 *
 *   Description:
 *      Number of additional passes for individual stepover in turn 
 *      roughing operations.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: No. of Additional Passes
 *  Variable Name: <prefix>_no__of_additional_passes
 *
 *   Possible Values: 
 *
 * 
 */
#define UF_PARAM_TURN_NO_OF_ADD_PASSES   2815  


/* UF_PARAM_TURN_NO_OF_PASSES_ARRAY
 *
 *   Description:
 *      List of pass counts for individual stepover in turn 
 *      roughing operations.
 *
 *   Type: UF_PARAM_type_vla_int
 *
 *   Name: No. of Passes Array
 *  Variable Name: <prefix>_no__of_passes_array
 *
 *   Possible Values: Array (size of 10)
 *
 * 
 */
#define UF_PARAM_TURN_NO_OF_PASSES_ARRAY   2816  


/* UF_PARAM_TURN_CUT_DEPTH_ARRAY
 *
 *   Description:
 *      List of stepover values for individual stepover in turn 
 *      roughing operations. This parameter is obsolete.
 *      Use UF_PARAM_TURN_CUT_DEPTH_ARRAY_TOOL_DEPENDENT instead
 *
 *   Type: UF_PARAM_type_vla_length
 *
 *   Name: Cut Depth Array
 *  Variable Name: <prefix>_cut_depth_array
 *
 *   Possible Values: Array  (size of 10)
 *
 * 
 */
#define UF_PARAM_TURN_CUT_DEPTH_ARRAY   2817  /* Obsolete in NX6 */


typedef enum UF_PARAM_turn_step_value_unit_e
{
    UF_PARAM_turn_step_value_unit_length = 0,
    UF_PARAM_turn_step_value_unit_percentage
} UF_PARAM_turn_step_value_unit_t;

/* UF_PARAM_TURN_STEP_VALUE_UNIT
 *
 *   Description:
 *      Type of stepover for plunge cutting
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Step Value Unit
 *  Variable Name: <prefix>_step_value_unit
 *
 *   Possible Values: UF_PARAM_turn_step_value_unit_t
 *
 * 
 */
#define UF_PARAM_TURN_STEP_VALUE_UNIT   2818  


typedef enum UF_PARAM_turn_reversal_mode_e
{
    UF_PARAM_turn_reversal_mode_as_level  = 0,
    UF_PARAM_turn_reversal_mode_inverse   = 1,
    UF_PARAM_turn_reversal_mode_closest   = 2,
    UF_PARAM_turn_reversal_mode_cut_later = 3,
    UF_PARAM_turn_reversal_mode_omit      = 4
} UF_PARAM_turn_reversal_mode_t;

/* UF_PARAM_TURN_REVERSAL_MODE
 *
 *   Description:
 *      Controls the strategy for cutting reversals in roughing operation.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Reversal Mode
 *  Variable Name: <prefix>_reversal_mode
 *
 *   Possible Values: UF_PARAM_turn_reversal_mode_t
 *
 * 
 */
#define UF_PARAM_TURN_REVERSAL_MODE   2820  /* Param_type_int */


typedef enum UF_PARAM_turn_cleanup_e
{
    UF_PARAM_turn_cleanup_none       = 0,
    UF_PARAM_turn_cleanup_all        = 1,
    UF_PARAM_turn_cleanup_down_only  = 2,
    /* The following to be used for level cutting */
    UF_PARAM_turn_cleanup_linear_none           = 0,
    UF_PARAM_turn_cleanup_linear_all,
    UF_PARAM_turn_cleanup_linear_steep_only,
    UF_PARAM_turn_cleanup_linear_all_but_steep,
    UF_PARAM_turn_cleanup_linear_level_only,
    UF_PARAM_turn_cleanup_linear_all_but_level,
    UF_PARAM_turn_cleanup_linear_down_only,
    UF_PARAM_turn_cleanup_linear_per_reversal
} UF_PARAM_turn_cleanup_t;

/* UF_PARAM_TURN_CLEANUP
 *
 *   Description:
 *      Controls cleanup after rough cuts in turning operations.
 *      For linear roughing use values UF_PARAM_turn_cleanup_linear_* !!!
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Cleanup
 *  Variable Name: <prefix>_cleanup
 *
 *   Possible Values: UF_PARAM_turn_cleanup_t
 *
 * 
 */
#define UF_PARAM_TURN_CLEANUP   2825  /* Param_type_int */


/* UF_PARAM_TURN_PROFILING
 *
 *   Description:
 *      Controls use of profiling cuts in roughing operation
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Profiling
 *  Variable Name: <prefix>_profiling
 *
 *   Possible Values: 
 *     0 = inactive
 *     1 = active
 *
 * 
 */
#define UF_PARAM_TURN_PROFILING   2830  /* Param_type_int */


/* UF_PARAM_TURN_UPDATE_IPW
 *
 *   Description:
 *      Activates the 'Update IPW' functionality in roughing,
 *      finishish or teachmode operations.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Update IPW
 *  Variable Name: <prefix>_update_ipw
 *
 *   Possible Values: 
 *     0 = inactive
 *     1 = active
 *
 * 
 */
#define UF_PARAM_TURN_UPDATE_IPW   2833 


/* UF_PARAM_TURN_LEVEL_STEP_ANGLE
 *
 *   Description:
 *      Angle for rough cut levels (stepover angle for plunge cutting).
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Level/Step Angle
 *  Variable Name: <prefix>_level_step_angle
 *
 *   Possible Values: angle in degree
 *
 * 
 */
#define UF_PARAM_TURN_LEVEL_STEP_ANGLE   2835  


/* UF_PARAM_TURN_LEVEL_STEP_ANGLE_TAG
 *
 *   Description:
 *      Identifier of a smart vector providing the level/stepover angle.
 *
 *   Type: UF_PARAM_type_tag
 *
 *   Name: Level/Step Angle Tag
 *  Variable Name: <prefix>_level_step_angle_tag
 *
 *   Possible Values: 
 *
 * 
 */
#define UF_PARAM_TURN_LEVEL_STEP_ANGLE_TAG   2836  


/* UF_PARAM_TURN_FP_TOG
 *
 *   Description:
 *      Controls use of first plunge position.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: First Plunge Toggle
 *  Variable Name: <prefix>_first_plunge_toggle
 *
 *   Possible Values: 
 *     0 = inactive
 *     1 = active
 *
 * 
 */
#define UF_PARAM_TURN_FP_TOG   2840  


/* UF_PARAM_TURN_FP_AXIAL
 *
 *   Description:
 *      Axial position for first plunge.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: First Plunge Axial
 *  Variable Name: <prefix>_first_plunge_axial
 *
 *   Possible Values: 
 *
 * 
 */
#define UF_PARAM_TURN_FP_AXIAL   2841  


/* UF_PARAM_TURN_FP_RADIAL
 *
 *   Description:
 *      Radial position for first plunge move (used for trepanning only).
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: First Plunge Radial
 *  Variable Name: <prefix>_first_plunge_radial
 *
 *   Possible Values: 
 *
 * 
 */
#define UF_PARAM_TURN_FP_RADIAL   2842  


/* UF_PARAM_TURN_FP_TAG
 *
 *   Description:
 *      Identifier of smart point defining first plunge position.
 *
 *   Type: UF_PARAM_type_tag
 *
 *   Name: First Plunge Tag
 *  Variable Name: <prefix>_first_plunge_tag
 *
 *   Possible Values: 
 *
 * 
 */
#define UF_PARAM_TURN_FP_TAG   2843  


typedef enum UF_PARAM_turn_finish_dwell_mode_e
{
    UF_PARAM_turn_dwell_finish_mode_none = 0,
    UF_PARAM_turn_dwell_finish_mode_time,
    UF_PARAM_turn_dwell_finish_mode_revolutions
} UF_PARAM_turn_finish_dwell_mode_t;

/* UF_PARAM_TURN_FINISH_DWELL_MODE
 *
 *   Description:
 *      This parameter controls the activation and mode
 *      of Dwell after Finish/Profile cut.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Finish Dwell Flag
 *  Variable Name: <prefix>_finish_dwell_flag
 *
 *   Possible Values: UF_PARAM_turn_finish_dwell_mode_t
 *
 * 
 */
#define UF_PARAM_TURN_FINISH_DWELL_MODE   2845    /* Param_type_int */


/* UF_PARAM_TURN_FINISH_DWELL
 *
 *   Description:
 *      This parameter controls the dwell time for 'Dwell after
 *      Finish/Porfile Cut'. It represents the time in seconds or
 *      the number of revolutions based on the setting of the dwell
 *      units parameter.
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Finish Dwell
 *  Variable Name: <prefix>_finish_dwell
 *
 *   Possible Values: 
 *     positive double (don't use decimals for revolutions)
 *
 * 
 */
#define UF_PARAM_TURN_FINISH_DWELL   2846    /* UF_PARAM_type_double */


typedef enum UF_PARAM_turn_chipctrl_mode_e
{
    UF_PARAM_turn_chipctrl_mode_const_break = 0,
    UF_PARAM_turn_chipctrl_mode_var_break,
    UF_PARAM_turn_chipctrl_mode_const_clear,
    UF_PARAM_turn_chipctrl_mode_var_clear
} UF_PARAM_turn_chipctrl_mode_t;

/* UF_PARAM_TURN_CHIPCTRL_MODE
 *
 *   Description:
 *      Defines the chip control mode to be used in turn plunge roughing.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Chip Control Mode
 *  Variable Name: <prefix>_chip_control_mode
 *
 *   Possible Values: UF_PARAM_turn_chipctrl_mode_t
 *
 * 
 */
#define UF_PARAM_TURN_CHIPCTRL_MODE   2850  


/* UF_PARAM_TURN_CHIPCTRL_TOG
 *
 *   Description:
 *      Controls use of chip control
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Chip Control Toggle
 *  Variable Name: <prefix>_chip_control_toggle
 *
 *   Possible Values: 
 *     0 = inactive
 *     1 = active
 *
 * 
 */
#define UF_PARAM_TURN_CHIPCTRL_TOG   2851  


/* UF_PARAM_TURN_CHIPCTRL_FPO_TOG
 *
 *   Description:
 *      Controls whether chip control is to be used for first plunge only
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Chip Control for 1st Plunge Only Toggle
 *  Variable Name: <prefix>_chip_control_for_1st_plunge_only_toggle
 *
 *   Possible Values: 
 *     0 = inactive
 *     1 = active
 *
 * 
 */
#define UF_PARAM_TURN_CHIPCTRL_FPO_TOG   2852  


/* UF_PARAM_TURN_CHIPCTRL_DISTANCE
 *
 *   Description:
 *      Defines the chip control departure distance in turn plunge roughing.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Chip Control Distance
 *  Variable Name: <prefix>_chip_control_distance
 *
 *   Possible Values: 
 *
 * 
 */
#define UF_PARAM_TURN_CHIPCTRL_DISTANCE   2853  


/* UF_PARAM_TURN_CHIPCTRL_CONST_INCREMENT
 *
 *   Description:
 *      Defines the constant increment for chip control motions in turn plunge roughing.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Chip Control Constant Increment
 *  Variable Name: <prefix>_chip_control_constant_increment
 *
 *   Possible Values: 
 *
 * 
 */
#define UF_PARAM_TURN_CHIPCTRL_CONST_INCREMENT   2855  /* double_length */


/* UF_PARAM_TURN_CHIPCTRL_VAR_NO_OF_PASSES
 *
 *   Description:
 *      Defines the list of variable increment counts in turn plunge roughing,
 *      i.e., how many chip control motions are to be made at the respective
 *      variable increment specified in an entry of that list (also 
 *      see UF_PARAM_TURN_CHIPCTRL_VAR_INCREMENT).
 *
 *   Type: UF_PARAM_type_vla_int
 *
 *   Name: Chip Control Variable Number of Passes
 *  Variable Name: <prefix>_chip_control_variable_number_of_passes
 *
 *   Possible Values: Array (size of 6)
 *
 * 
 */
#define UF_PARAM_TURN_CHIPCTRL_VAR_NO_OF_PASSES   2857  /* int_vla */


/* UF_PARAM_TURN_CHIPCTRL_VAR_INCREMENT
 *
 *   Description:
 *      Defines the list of variable increment values in turn plunge roughing,
 *      i.e., provides a list of entries each of which contains a specific
 *      increment value valid for a certain number of chip control motions 
 *      to be made (cf. UF_PARAM_TURN_CHIPCTRL_VAR_NO_OF_PASSES).
 *
 *   Type: UF_PARAM_type_vla_length
 *
 *   Name: Chip Control Variable Increment
 *  Variable Name: <prefix>_chip_control_variable_increment
 *
 *   Possible Values:    Array (size of 6)
 *
 * 
 */
#define UF_PARAM_TURN_CHIPCTRL_VAR_INCREMENT   2858  /* vla_length */


typedef enum
{
    UF_PARAM_tropr_ramping_mode_out_on_every_pass = 0,
    UF_PARAM_tropr_ramping_mode_in_on_every_pass,
    UF_PARAM_tropr_ramping_mode_out_first,
    UF_PARAM_tropr_ramping_mode_in_first
} UF_PARAM_tropr_ramping_mode_t;


/* UF_PARAM_TROPR_RAMPING_MODE
 *
 *  Description:
 *     This parameter lets you essentially determine how the processor is 
 *     meant to generate roughing passes for the roughing strategies
 *     of Ramping Zig and Ramping ZigZag. The ramping passes may either be
 *     performed on "every other pass", being directed into the part or 
 *     ramping out or ramping on every pass, ramping in and ramping out
 *     in alternating sequence.
 *
 *  Type: Param_type_int
 *
 *  Name: Ramping Mode
 *  Variable Name: <prefix>_ramping_mode
 *
 *  Possible Values: UF_PARAM_tropr_ramping_mode_t
 *
 * 
 */
#define UF_PARAM_TROPR_RAMPING_MODE   2860 


/* UF_PARAM_TROPR_MULTI_RAMP
 *
 *  Description:
 *     Main toggle to activate the generation of "Multi Ramps" (also see 
 *     description of parameter UF_PARAM_TROPR_MULTI_RAMP_PATTERN).
 *
 *  Type: Param_type_int
 *
 *  Name: Multi Ramp
 *  Variable Name: <prefix>_multi_ramp
 *
 *  Possible Values:    0: off
 *                   else: on
 *
 * 
 */
#define UF_PARAM_TROPR_MULTI_RAMP   2865 


typedef enum
{
    UF_PARAM_tropr_multi_ramp_pattern_simple = 0,
    UF_PARAM_tropr_multi_ramp_pattern_double
} UF_PARAM_tropr_multi_ramp_pattern_t;


/* UF_PARAM_TROPR_MULTI_RAMP_PATTERN
 *
 *  Description:
 *     The Multi Ramp Pattern parameter specifies how a ramped roughing pass 
 *     is to be subdivided into "Multi Ramps". I.e., instead of creating a 
 *     "single" ramp along its entire length, the system performs multiple
 *     smaller ramping motions in case a Multi Ramp Pattern option is chosen
 *     (alse see description of parameter UF_PARAM_TROPR_MAX_RAMP_LENGTH).
 *
 *  Type: Param_type_int
 *
 *  Name: Multi Ramp Pattern
 *  Variable Name: <prefix>_multi_ramp_pattern
 *
 *  Possible Values: UF_PARAM_tropr_multi_ramp_pattern_t
 *                   The meaning of the values depend on the selected 
 *                   Ramping Mode (UF_PARAM_TROPR_RAMPING_MODE).
 *
 *                   TROPR_RAMP_OUT_ON_EVERY_OTHER_PASS:
 *                      UF_PARAM_tropr_multi_ramp_pattern_simple = 
 *                         MULTI_RAMP_PATTERN_OUT
 *                      UF_PARAM_tropr_multi_ramp_pattern_double =
 *                         MULTI_RAMP_PATTERN_OUT_IN
 *                
 *                   TROPR_RAMP_IN_ON_EVERY_OTHER_PASS:
 *                      UF_PARAM_tropr_multi_ramp_pattern_simple =
 *                         MULTI_RAMP_PATTERN_IN
 *                      UF_PARAM_tropr_multi_ramp_pattern_double =
 *                         MULTI_RAMP_PATTERN_IN_OUT
 *
 * 
 */
#define UF_PARAM_TROPR_MULTI_RAMP_PATTERN   2866  


/* UF_PARAM_TROPR_MAX_RAMP_LENGTH
 *
 *  Description:
 *     This parameter lets you define the maximum length for multi ramps 
 *     created by the turning processor in Ramping Zig or Ramping ZigZag 
 *     cut strategies (cf. description of parameter 
 *     UF_PARAM_TROPR_MULTI_RAMP_PATTERN).
 *
 *  Type: Param_type_double_length
 *
 *  Name: Max Ramp Length
 *  Variable Name: <prefix>_max_ramp_length
 *
 *  Possible Values: double (only positive values)
 *
 * 
 */
#define UF_PARAM_TROPR_MAX_RAMP_LENGTH   2867 


/* UF_PARAM_TROPR_OMIT_LAST_PASS
 *
 *  Description:
 *     Suppresses the generation of the last pass in roughing.
 *
 *  Type: Param_type_int
 *
 *  Name: Omit Last Pass
 *  Variable Name: <prefix>_omit_last_pass
 *
 *  Possible Values:    0: off - generate all passes
 *                   else: on  - omit last pass
 *
 * 
 */
#define UF_PARAM_TROPR_OMIT_LAST_PASS   2870 


/* UF_PARAM_TROPR_LEVEL_DEPTH_STATUS
 *
 *  Description:
 *     This parameter is applicable to plunge rouging.
 *     It activates the level option in plunge roughing 
 *     (UF_PARAM_TROPR_LEVEL_DEPTH, see below).
 *
 *  Type: Param_type_int
 *
 *  Name: Level Depth Status
 *  Variable Name: <prefix>_level_depth_status
 *
 *  Possible Values:    0: off
 *                   else: on
 *
 * 
 */
#define UF_PARAM_TROPR_LEVEL_DEPTH_STATUS   2875 


/* UF_PARAM_TROPR_LEVEL_DEPTH
 *
 *  Description:
 *     This parameter implements the level option for plunge roughing.
 *     If active, the plunge roughing is made "level by level" where each 
 *     series of subsequent plunge cuts removes another level of material. 
 *     The depth of such levels is defined by way of the 
 *     UF_PARAM_TROPR_LEVEL_DEPTH parameter.
 *
 *  Type: Param_type_double_length
 *
 *  Name: Level Depth
 *  Variable Name: <prefix>_level_depth
 *
 *  Possible Values: double (only positive values)
 *
 * 
 */
#define UF_PARAM_TROPR_LEVEL_DEPTH   2876 


typedef enum UF_PARAM_tfopr_cut_strategy_e
{
    UF_PARAM_tfopr_cut_strategy_diameters_only = 0,
    UF_PARAM_tfopr_cut_strategy_faces_only,
    UF_PARAM_tfopr_cut_strategy_diameters_then_faces,
    UF_PARAM_tfopr_cut_strategy_faces_then_diameters,
    UF_PARAM_tfopr_cut_strategy_towards_corner,
    UF_PARAM_tfopr_cut_strategy_away_from_corner,
    UF_PARAM_tfopr_cut_strategy_down_only,
    UF_PARAM_tfopr_cut_strategy_all
} UF_PARAM_tfopr_cut_strategy_t;

/* UF_PARAM_TFOPR_CUT_STRATEGY
 *
 *   Description:
 *      This parameter defines the cut strategy for profiling in roughing
 *      operations and for finishing operations.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Finishing Cut Method
 *  Variable Name: <prefix>_finishing_cut_method
 *
 *   Possible Values: UF_PARAM_tfopr_cut_strategy_t
 *
 * 
 */
#define UF_PARAM_TFOPR_CUT_STRATEGY   2900  /* Param_type_int */


typedef enum UF_PARAM_turn_finish_fillets_e
{
    UF_PARAM_turn_finish_fillets_add_to_faces = 0,
    UF_PARAM_turn_finish_fillets_add_to_diameters,
    UF_PARAM_turn_finish_fillets_split,
    UF_PARAM_turn_finish_fillets_omit
} UF_PARAM_turn_finish_fillets_t;

/* UF_PARAM_TURN_FINISH_FILLETS
 *
 *   Description:
 *      Defines the mode for cutting fillets
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Finish Fillets
 *  Variable Name: <prefix>_finish_fillets
 *
 *   Possible Values: UF_PARAM_turn_finish_fillets_t
 *
 * 
 */
#define UF_PARAM_TURN_FINISH_FILLETS   2910  


/* UF_PARAM_TURN_FINISH_SPRING_PASSES
 *
 *   Description:
 *      Defines the number of spring passes to be cut in turn rough profiling
 *      or turn finishing.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Finish Spring Passes
 *  Variable Name: <prefix>_finish_spring_passes
 *
 *   Possible Values: positive integer
 *
 * 
 */
#define UF_PARAM_TURN_FINISH_SPRING_PASSES   2911  


/* UF_PARAM_TURN_FINISH_ALTERNATE
 *
 *   Description:
 *      Controls whether spring passes should be cut with alternating direction.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Finish Alternate
 *  Variable Name: <prefix>_finish_alternate
 *
 *   Possible Values: 
 *     0 = inactive
 *     1 = active
 *
 * 
 */
#define UF_PARAM_TURN_FINISH_ALTERNATE   2912  


typedef enum UF_PARAM_turn_finish_direction_e
{
    UF_PARAM_turn_finish_direction_backward = 0,
    UF_PARAM_turn_finish_direction_forward
} UF_PARAM_turn_finish_direction_t;

/* UF_PARAM_TURN_FINISH_DIRECTION
 *
 *   Description:
 *      This parameter lets you revert the cut direction for turn finishing
 *      or for profiling in a turn roughing operation (related to first pass if
 *      "alternate" is active).
 *      It is interpreted relative to the major direction given thru the level angle
 *      of linear/contour roughing and finishing or the step angle of plunge roughing.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Finish Direction
 *  Variable Name: <prefix>_finish_direction
 *
 *   Possible Values: UF_PARAM_turn_finish_direction_t
 *
 * 
 */
#define UF_PARAM_TURN_FINISH_DIRECTION   2913  


/* UF_PARAM_TURN_FINISH_STOP_AT_TOG
 *
 *   Description:
 *      Controls use of "Stop At" functionality in turn finishing/profiling.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Finish Stop At Toggle
 *  Variable Name: <prefix>_finish_stop_at_toggle
 *
 *   Possible Values: 
 *     0 = inactive
 *     1 = active
 *
 * 
 */
#define UF_PARAM_TURN_FINISH_STOP_AT_TOG   2914  


/* UF_PARAM_TURN_FINISH_STOP_AT
 *
 *   Description:
 *      Defines "Stop At" distance value for "Stop At" unit set to length in 
 *      turn finishing/profiling.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Finish Stop At
 *  Variable Name: <prefix>_finish_stop_at
 *
 *   Possible Values: 
 *
 * 
 */
#define UF_PARAM_TURN_FINISH_STOP_AT   2915  


/* UF_PARAM_TURN_FINISH_STOP_AT_PERCENT
 *
 *   Description:
 *      Defines "Stop At" percentage value for "Stop At" unit set to percentage
 *      in turn finishing/profiling.
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Finish Stop At Percent
 *  Variable Name: <prefix>_finish_stop_at_percent
 *
 *   Possible Values: 
 *
 * 
 */
#define UF_PARAM_TURN_FINISH_STOP_AT_PERCENT   2916  


/* UF_PARAM_TURN_FINISH_STOP_AT_TAG
 *
 *   Description:
 *      Identifier of smart point for "Stop At" Position if "Stop At" unit is 
 *      set to smart point
 *
 *   Type: UF_PARAM_type_tag
 *
 *   Name: Finish Stop At Tag
 *  Variable Name: <prefix>_finish_stop_at_tag
 *
 *   Possible Values: 
 *
 * 
 */
#define UF_PARAM_TURN_FINISH_STOP_AT_TAG   2917  


typedef enum UF_PARAM_turn_finish_stop_at_unit_e
{
    UF_PARAM_turn_finish_stop_at_unit_distance = 0,
    UF_PARAM_turn_finish_stop_at_unit_percentage,
    UF_PARAM_turn_finish_stop_at_unit_smart_point
} UF_PARAM_turn_finish_stop_at_unit_t;

/* UF_PARAM_TURN_FINISH_STOP_AT_UNIT
 *
 *   Description:
 *      Defines the unit of "Stop At" location specification in turn finishing
 *      or profiling operations.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Finish Stop At Unit
 *  Variable Name: <prefix>_finish_stop_at_unit
 *
 *   Possible Values: UF_PARAM_turn_finish_stop_at_unit_t
 *
 * 
 */
#define UF_PARAM_TURN_FINISH_STOP_AT_UNIT   2918  


typedef enum UF_PARAM_turn_finish_overlap_unit_e
{
    UF_PARAM_turn_finish_overlap_unit_distance = 0,
    UF_PARAM_turn_finish_overlap_unit_percentage
} UF_PARAM_turn_finish_overlap_t;

/* UF_PARAM_TURN_FINISH_OVERLAP_UNIT
 *
 *   Description:
 *      Defines the unit for overlap used with down only cutting in turn
 *      finishing/profiling.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Finish Overlap Unit
 *  Variable Name: <prefix>_finish_overlap_unit
 *
 *   Possible Values: UF_PARAM_turn_finish_overlap_unit_t
 *
 * 
 */
#define UF_PARAM_TURN_FINISH_OVERLAP_UNIT   2919  


/* UF_PARAM_TURN_FINISH_OVERLAP
 *
 *   Description:
 *      Defines the overlap distance if "Overlap Unit" is selected to
 *      be related to a distance value in turn profiling/finishing.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Finish Overlap
 *  Variable Name: <prefix>_finish_overlap
 *
 *   Possible Values: 
 *
 * 
 */
#define UF_PARAM_TURN_FINISH_OVERLAP   2920  


/* UF_PARAM_TURN_FINISH_OVERLAP_PERCENT
 *
 *   Description:
 *      Defines the overlap percentage for if "Overlap Unit" is selected to
 *      be related to a percentage value in turn profiling/finishing.
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Finish Overlap Percent
 *  Variable Name: <prefix>_finish_overlap_percent
 *
 *   Possible Values: 
 *
 * 
 */
#define UF_PARAM_TURN_FINISH_OVERLAP_PERCENT   2921  


/* UF_PARAM_TURN_FINISH_OMIT_REVERSALS
 *
 *   Description:
 *      Controls whether reversals are to be cut for finish operation.
 *      This parameter is not used for profiling in the roughing operation.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Finish Omit Reversals
 *  Variable Name: <prefix>_finish_omit_reversals
 *
 *   Possible Values: 
 *     0 = Cut Reversals
 *     1 = Omit Reversals
 *
 * 
 */
#define UF_PARAM_TURN_FINISH_OMIT_REVERSALS   2922  /* Param_type_int */


typedef enum UF_PARAM_turn_finish_machining_sequence_e
{
    UF_PARAM_turn_finish_machining_sequence_same_as_faces_diameters = 0,
    UF_PARAM_turn_finish_machining_sequence_reversed
} UF_PARAM_turn_machining_sequence_direction_t;

/* UF_PARAM_TURN_FINISH_MACHINING_SEQUENCE
 *
 *   Description:
 *      Defines the machining sequence for turn finishing or for profiling in a
 *      turn roughing operation.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Finish Machining Sequence
 *  Variable Name: <prefix>_finish_machining_sequence
 *
 *   Possible Values: UF_PARAM_turn_machining_sequence_direction_t
 *
 * 
 */
#define UF_PARAM_TURN_FINISH_MACHINING_SEQUENCE   2923   


/* UF_PARAM_TURN_PROFILING_OVERRIDE_AUTODETECT
 *
 *   Description:
 *      Controls whether cut region autodetection should be disabled for
 *      profiling cut in roughing operation.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Override Autodetection for Profiling
 *  Variable Name: <prefix>_override_autodetection_for_profiling
 *
 *   Possible Values: 
 *     0 = inactive (evaluate cut regions for profiling)
 *     1 = active   (use cut region from rough pass)
 *
 * 
 */
#define UF_PARAM_TURN_PROFILING_OVERRIDE_AUTODETECT   2925  /* UF_PARAM_type_int */


/* UF_PARAM_TURN_FINISH_CUT_DEPTH_TOG
 *
 *   Description:
 *      Defines if Cut Depth is active in Turn Finishing/Profiling.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Turn Finish Cut Depth Toggle
 *  Variable Name: <prefix>_turn_finish_cut_depth_toggle
 *
 *   Possible Values: 0    - off
 *                    else - on
 *
 * 
 */
#define UF_PARAM_TURN_FINISH_CUT_DEPTH_TOG   2930 


typedef enum UF_PARAM_turn_finish_cut_depth_type_e
{
    UF_PARAM_turn_finish_cut_depth_type_constant    = 0,
    UF_PARAM_turn_finish_cut_depth_type_no_of_passes,
    UF_PARAM_turn_finish_cut_depth_type_individual
} UF_PARAM_turn_finish_cut_depth_type_t;

/* UF_PARAM_TURN_FINISH_CUT_DEPTH_TYPE
 *
 *   Description:
 *      Defines Cut Depth Type in Turn Finishing/Profiling.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Turn Finish Cut Depth Type
 *  Variable Name: <prefix>_turn_finish_cut_depth_type
 *
 *   Possible Values: 0 - Constant
 *                    1 - No. of Passes
 *                    2 - Individual
 *
 * 
 */
#define UF_PARAM_TURN_FINISH_CUT_DEPTH_TYPE   2931 


/* UF_PARAM_TURN_FINISH_CUT_DEPTH
 *
 *   Description:
 *      Defines Cut Depth value in Turn Finishing/Profiling.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Turn Finish Cut Depth
 *  Variable Name: <prefix>_turn_finish_cut_depth
 *
 *   Possible Values: positive double (greater than zero)
 *
 * 
 */
#define UF_PARAM_TURN_FINISH_CUT_DEPTH   2932 


/* UF_PARAM_TURN_FINISH_NO_OF_PASSES
 *
 *   Description:
 *      Defines the Number of Passes for Cut Depth in Turn
 *      Finishing/Profiling.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Turn Finish No of Passes
 *  Variable Name: <prefix>_turn_finish_no_of_passes
 *
 *   Possible Values: positive integer (greater than zero)
 *
 * 
 */
#define UF_PARAM_TURN_FINISH_NO_OF_PASSES   2933 


/* UF_PARAM_TURN_FINISH_CUT_DEPTH_ALTERNATE
 *
 *   Description:
 *      Defines if Alternate functionality is activated for Cut Depth
 *      in Turn Finishing/Profiling.
 *      Cut direction is reversed after every finish cut in this mode.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Turn Finish Cut Depth Alternate
 *  Variable Name: <prefix>_turn_finish_cut_depth_alternate
 *
 *   Possible Values: 0    - off
 *                    else - on
 *
 * 
 */
#define UF_PARAM_TURN_FINISH_CUT_DEPTH_ALTERNATE   2934 


/* UF_PARAM_TURN_FINISH_NO_OF_PASSES_ARRAY
 *
 *   Description:
 *      Defines the individual Number of Passes for Cut Depth in 
 *      Turn Finishing/Profiling.
 *      This parameter is used in combination with
 *      UF_PARAM_TURN_FINISH_CUT_DEPTH_ARRAY.
 *
 *   Type: UF_PARAM_type_vla_int
 *
 *   Name: Turn Finish No of Passes Array
 *  Variable Name: <prefix>_turn_finish_no_of_passes_array
 *
 *   Possible Values: array (size 10) of non-negative integers
 *
 * 
 */
#define UF_PARAM_TURN_FINISH_NO_OF_PASSES_ARRAY   2935 


/* UF_PARAM_TURN_FINISH_CUT_DEPTH_ARRAY
 *
 *   Description:
 *      Defines the individual Cut Depth increments in Turn 
 *      Finishing/Profiling.
 *      This parameter is used in combination with
 *      UF_PARAM_TURN_FINISH_NO_OF_PASSES_ARRAY.
 *      This parameter is obsolete, use 
 *      UF_PARAM_TURN_FINISH_CUT_DEPTH_ARRAY_TOOL_DEPENDENT instead
 *
 *   Type: UF_PARAM_type_vla_length
 *
 *   Name: Turn Finish Cut Depth Array
 *  Variable Name: <prefix>_turn_finish_cut_depth_array
 *
 *   Possible Values: array (size 10) of non-negative doubles
 *
 * 
 */
#define UF_PARAM_TURN_FINISH_CUT_DEPTH_ARRAY   2936    /* Obsolete in NX6 */


/* UF_PARAM_TURN_MIN_CLEARANCE
 *
 *   Description:
 *      This parameter establishes a safty zone around the workpiece for 
 *      non-cutting tool motions.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Minimum Clearance
 *  Variable Name: <prefix>_minimum_clearance
 *
 *   Possible Values: Positive double (or zero)
 *
 * 
 */
#define UF_PARAM_TURN_MIN_CLEARANCE   2950 


/* UF_PARAM_TCDOPR_CYCLE
 *
 *   Description:
 *      This parameter represents the cycle type in 
 *      Centerline Drilling.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Centerline Drill Cycle
 *  Variable Name: <prefix>_centerline_drill_cycle
 *
 *   Possible Values: UF_PARAM_tcdopr_cycle_t
 *
 * 
 */
#define UF_PARAM_TCDOPR_CYCLE   2952 


typedef enum
{
    UF_PARAM_tcdopr_application_type_drilling = 0,
    UF_PARAM_tcdopr_application_type_reaming,
    UF_PARAM_tcdopr_application_type_tapping
} UF_PARAM_tcdopr_application_type_t;


/* UF_PARAM_TCDOPR_APPLICATION_TYPE
 *
 *   Description:
 *      This parameter defines the application type (Drilling, 
 *      Reaming or Tapping) of a centeline drill operation.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Application Type
 *  Variable Name: <prefix>_application_type
 *
 *   Possible Values: UF_PARAM_tcdopr_application_type_t
 *
 * 
 */
#define UF_PARAM_TCDOPR_APPLICATION_TYPE   2955 


/* UF_PARAM_TURN_ENGAGE_DISTANCE
 *
 *   Description:
 *      This parameter defines an additional engage distance from the
 *      clearance position, where the engage motion starts.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Turn Engage Distance
 *  Variable Name: <prefix>_turn_engage_distance
 *
 *   Possible Values: Positive double (or zero)
 *
 * 
 */
#define UF_PARAM_TURN_ENGAGE_DISTANCE   2957 


/* UF_PARAM_TURN_SPINDLE_STOP
 *
 *   Description:
 *      This parameter activates a Spindle Off event when total drill depth
 *      is reached.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Spindle Stop Toggle
 *  Variable Name: <prefix>_spindle_stop_toggle
 *
 *   Possible Values:     0: off
 *                     else: on
 *
 * 
 */
#define UF_PARAM_TURN_SPINDLE_STOP   2960 


typedef enum
{
    UF_PARAM_turn_chip_removal_method_none = 0,
    UF_PARAM_turn_chip_removal_method_break_chip,
    UF_PARAM_turn_chip_removal_method_peck_drill
} UF_PARAM_turn_chip_removal_method_t;


/* UF_PARAM_TURN_REMOVAL_METHOD
 *
 *   Description:
 *      This parameter specifies the method for clearing or breaking chips
 *      in turn centerline drilling.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Chip Removal Method
 *  Variable Name: <prefix>_chip_removal_method
 *
 *   Possible Values: UF_PARAM_turn_chip_removal_method_t
 *
 * 
 */
#define UF_PARAM_TURN_REMOVAL_METHOD   2961 


typedef enum
{
    UF_PARAM_turn_removal_inc_type_constant = 0,
    UF_PARAM_turn_removal_inc_type_variable
} UF_PARAM_turn_removal_inc_type_t;


/* UF_PARAM_TURN_REMOVAL_INC_TYPE
 *
 *   Description:
 *      This parameter specifies the type of increment definition for Break 
 *      Chip or Peck Drill centerline drill operations in turning.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Chip Removal Increment Type
 *  Variable Name: <prefix>_chip_removal_increment_type
 *
 *   Possible Values: UF_PARAM_turn_removal_inc_type_t
 *
 * 
 */
#define UF_PARAM_TURN_REMOVAL_INC_TYPE   2962 


/* UF_PARAM_TCDOPR_AUTO_START_POSITION
 *
 *   Description:
 *      This parameter controls whether the start point for drilling should be
 *      created automatically based on the current in-process workpiece shape.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Center Drill Start Point
 *  Variable Name: <prefix>_center_drill_start_point
 *
 *   Possible Values: 
 *        0 = Use explicitly defined start position
 *        1 = Automatically evaluate start position
 *
 * 
 */
#define UF_PARAM_TCDOPR_AUTO_START_POSITION   2965 


/* UF_PARAM_TCDOPR_START_POINT
 *
 *   Description:
 *      This parameter holds the object ID of a smart point, which defines
 *      the start point of the centerline drill geometry.
 *
 *   Type: UF_PARAM_type_tag
 *
 *   Name: Center Drill Start Point
 *  Variable Name: <prefix>_center_drill_start_point
 *
 *   Possible Values:
 *         0 (no entity)
 *         entity ID
 *
 * 
 */
#define UF_PARAM_TCDOPR_START_POINT   2970 


/* UF_PARAM_TCDOPR_END_POINT
 *
 *   Description:
 *      This parameter holds the object ID of a smart point, which defines
 *      the end point of the centerline drill geometry.
 *
 *   Type: UF_PARAM_type_tag
 *
 *   Name: Center Drill End Point
 *  Variable Name: <prefix>_center_drill_end_point
 *
 *   Possible Values:
 *         0 (no entity)
 *         entity ID
 *
 * 
 */
#define UF_PARAM_TCDOPR_END_POINT   2973 


/* UF_PARAM_TCDOPR_DEPTH
 *
 *   Description:
 *      This parameter specifies the depth of a Centerline Drill operation.
 *      It is only used if parameter UF_PARAM_DEPTH_TYPE is set to mode
 *      Depth.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Center Drill Depth
 *  Variable Name: <prefix>_center_drill_depth
 *
 *   Possible Values: Double (or zero)
 *
 * 
 */
#define UF_PARAM_TCDOPR_DEPTH   2974 


/* UF_PARAM_TCDOPR_OFF_CENTER_TOG
 *
 *   Description:
 *      This parameter defines the whether off centerline drilling is activated.
 *      If it's set to zero, off centerline drilling is deactivated.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Off Center Drilling Toggle
 *  Variable Name: <prefix>_off_center_drilling_toggle
 *
 *   Possible Values: 
 *     0 = inactive
 *     1 = active
 *
 * 
 */
#define UF_PARAM_TCDOPR_OFF_CENTER_TOG   2976 


/* UF_PARAM_TCDOPR_OFF_CENTER_DIST
 *
 *   Description:
 *      This parameter defines the offset distance for off centerline drilling.
 *      If it's set to zero, off centerline drilling is deactivated.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Off Center Drilling Distance
 *  Variable Name: <prefix>_off_center_drilling_distance
 *
 *   Possible Values: Double (or zero)
 *
 * 
 */
#define UF_PARAM_TCDOPR_OFF_CENTER_DIST   2977 


/* UF_PARAM_TCDOPR_STEP
 *
 *   Description:
 *      This parameter specifies the cycle step 
 *      for Centerline Drilling
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Center Drill Step
 *  Variable Name: <prefix>_center_drill_step
 *
 *   Possible Values: double
 *
 * 
 */
#define UF_PARAM_TCDOPR_STEP   2986 


/* UF_PARAM_TCDOPR_STEP_MODIFIER_1
 *
 *   Description:
 *      This parameter specifies the cycle step modifier 1 
 *      for Centerline Drilling
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Center Drill Step Modifier 1
 *  Variable Name: <prefix>_center_drill_step_modifier_1
 *
 *   Possible Values: double
 *
 * 
 */
#define UF_PARAM_TCDOPR_STEP_MODIFIER_1   2987 


/* UF_PARAM_TCDOPR_STEP_MODIFIER_2
 *
 *   Description:
 *      This parameter specifies the cycle step modifier 2 
 *      for Centerline Drilling
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Center Drill Step Modifier 2
 *  Variable Name: <prefix>_center_drill_step_modifier_2
 *
 *   Possible Values: double
 *
 * 
 */
#define UF_PARAM_TCDOPR_STEP_MODIFIER_2   2988 


/* UF_PARAM_TURN_AVOIDANCE_PREFER_DIRECT_MOTION_TO_FIRST_ENGAGE_TOG
 *
 *   Description:
 *      This parameter specifies if direct motions are preferred for traversal
 *      to the operation's first engage.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Turn Avoidance Prefer Direct Motion To First Engage Toggle
 *  Variable Name: <prefix>_turn_avoidance_prefer_direct_motion_to_first_engage_toggle
 *
 *   Possible Values: 
 *     0 = inactive
 *     1 = active
 *
 * 
 */
#define UF_PARAM_TURN_AVOIDANCE_PREFER_DIRECT_MOTION_TO_FIRST_ENGAGE_TOG   2990 


/* UF_PARAM_TURN_AVOIDANCE_PREFER_DIRECT_MOTION_BETWEEN_REGIONS_TOG
 *
 *   Description:
 *      This parameter specifies if direct motions are preferred for traversal
 *      between cut regions or individual cuts.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Turn Avoidance Prefer Direct Motion Between Regions Toggle
 *  Variable Name: <prefix>_turn_avoidance_prefer_direct_motion_between_regions_toggle
 *
 *   Possible Values: 
 *     0 = inactive
 *     1 = active
 *
 * 
 */
#define UF_PARAM_TURN_AVOIDANCE_PREFER_DIRECT_MOTION_BETWEEN_REGIONS_TOG   2991 


/* UF_PARAM_TURN_AVOIDANCE_PREFER_DIRECT_MOTION_AFTER_LAST_RETRACT_TOG
 *
 *   Description:
 *      This parameter specifies if direct motions are preferred for traversal
 *      after the last retract has been made.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Turn Avoidance Prefer Direct Motion After Last Retract Toggle
 *  Variable Name: <prefix>_turn_avoidance_prefer_direct_motion_after_last_retract_toggle
 *
 *   Possible Values: 
 *     0 = inactive
 *     1 = active
 *
 * 
 */
#define UF_PARAM_TURN_AVOIDANCE_PREFER_DIRECT_MOTION_AFTER_LAST_RETRACT_TOG   2992 


/* UF_PARAM_TURN_AVOIDANCE_ADDITIONAL_CHECKING_FOR_AUTOMATIC_ENGAGE
 *
 *   Description:
 *      This parameter specifies if additional collision avoidance checking is 
 *      applied for automatic engage.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Turn Avoidance Additional Checking For Automatic Engage
 *  Variable Name: <prefix>_turn_avoidance_additional_checking_for_automatic_engage
 *
 *   Possible Values: 
 *     0 = inactive
 *     1 = active
 *
 * 
 */
#define UF_PARAM_TURN_AVOIDANCE_ADDITIONAL_CHECKING_FOR_AUTOMATIC_ENGAGE   2995 


/* UF_PARAM_TURN_AVOIDANCE_ADDITIONAL_CHECKING_FOR_AUTOMATIC_RETRACT
 *
 *   Description:
 *      This parameter specifies if additional collision avoidance checking is 
 *      applied for automatic retract.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Turn Avoidance Additional Checking For Automatic Retract
 *  Variable Name: <prefix>_turn_avoidance_additional_checking_for_automatic_retract
 *
 *   Possible Values: 
 *     0 = inactive
 *     1 = active
 *
 * 
 */
#define UF_PARAM_TURN_AVOIDANCE_ADDITIONAL_CHECKING_FOR_AUTOMATIC_RETRACT   2996 


/* UF_PARAM_TURN_AVOIDANCE_ADDITIONAL_CHECKING_FOR_MINIMUM_CLEARANCE
 *
 *   Description:
 *      This parameter specifies if additional collision avoidance checking is
 *      applied considering the minimum clearance around the in-process workpiece.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Turn Avoidance Additional Checking For Minimum Clearance
 *  Variable Name: <prefix>_turn_avoidance_additional_checking_for_minimum_clearance
 *
 *   Possible Values: 
 *     0 = inactive
 *     1 = active
 *
 * 
 */
#define UF_PARAM_TURN_AVOIDANCE_ADDITIONAL_CHECKING_FOR_MINIMUM_CLEARANCE   2997 


/* UF_PARAM_FLOOR
 *   Description:
 *      Floor is a smart plane object defined in a geometry group
 *      or an opertion object.
 *
 *   Type: UF_PARAM_type_tag
 *
 *   Name: Floor
 *  Variable Name: <prefix>_floor
 *
 *   Possible Values: UF_PARAM_type_tag
 *
 * 
 */
#define UF_PARAM_FLOOR   3007 


/* UF_PARAM_PART_THICKNESS
 *
 *   Description:
 *      A distance offset applied to part geometry of
 *      a geometry group object
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Part Thickness
 *  Variable Name: <prefix>_part_thickness
 *
 *   Possible Values: UF_PARAM_type_double length
 *
 * 
 */
#define UF_PARAM_PART_THICKNESS   3009 


/* UF_PARAM_BLANK_OFFSET
 *
 *   Description:
 *      A distance offset applied to blank geometry of
 *      a geometry group object
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Blank Offset
 *  Variable Name: <prefix>_blank_offset
 *
 *   Possible Values: UF_PARAM_type_double length
 *
 * 
 */
#define UF_PARAM_BLANK_OFFSET   3014 


/* UF_PARAM_CHECK_OFFSET
 *
 *   Description:
 *      A distance offset applied to check geometry of
 *      a geometry group object
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Check Offset
 *  Variable Name: <prefix>_check_offset
 *
 *   Possible Values: UF_PARAM_type_double length
 *
 * 
 */
#define UF_PARAM_CHECK_OFFSET   3015 


/* UF_PARAM_TRIM_OFFSET
 *
 *   Description:
 *      A distance offset applied to trim boundary geometry of
 *      a geometry group object
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Trim Offset
 *  Variable Name: <prefix>_trim_offset
 *
 *   Possible Values: UF_PARAM_type_double length
 *
 * 
 */
#define UF_PARAM_TRIM_OFFSET   3016 


/* UF_PARAM_STOCK_WALL
 *
 *   Description:
 *      Parameter is the wall stock to be applied to the
 *      defined wall geometry (UF_PARAM_WALL_GEOM).
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Stock Wall
 *  Variable Name: <prefix>_stock_wall
 *
 *   Possible Values: UF_PARAM_type_double_length
 *
 * 
 */
#define UF_PARAM_STOCK_WALL   3018  /* UF_PARAM_type_double_length */


/* UF_PARAM_FOLLOW_WALL_BOTTOM
 *
 *  Description:
 *      This parameter specifies if "follow wall bottom" is to be used.
 *
 *  Type: UF_PARAM_type_logical
 *
 *  Name: Follow Wall Bottom
 *  Variable Name: <prefix>_follow_wall_bottom
 *
 *  Possible Values:
 *                false (default)
 *                true-custom
 *
 * 
 */
#define UF_PARAM_FOLLOW_WALL_BOTTOM   3021 


/* UF_PARAM_TOOL_POSITION_OFFSET
 *
 *  Description:
 *      This parameter specifies the tool postion offset value
 *
 *  Type: UF_PARAM_type_double_length
 *
 *  Name: Tool Position Offset
 *  Variable Name: <prefix>_tool_position_offset
 *
 *  Possible Values: double
 *
 * 
 */
#define UF_PARAM_TOOL_POSITION_OFFSET   3022 


/* UF_PARAM_AUTO_AUX_FLOOR_DIS
 *
 *  Description:
 *      This parameter specifies the automatic auxiliary floor distance value
 *
 *  Type: UF_PARAM_type_double_length
 *
 *  Name: Automatic Auxiliary Floor Distance
 *  Variable Name: <prefix>_automatic_auxiliary_floor_distance
 *
 *  Possible Values: double
 *
 * 
 */
#define UF_PARAM_AUTO_AUX_FLOOR_DIS   3023 


/* UF_PARAM_APPLY_AUTO_AUX_FLOOR
 *
 *  Description:
 *      This parameter specifies if "automatic auxiliary floor" is to be used.
 *
 *  Type: UF_PARAM_type_logical
 *
 *  Name: Auto Aux Floor
 *  Variable Name: <prefix>_auto_aux_floor
 *
 *  Possible Values:
 *                false (default)
 *                true-custom
 *
 * 
 */
#define UF_PARAM_APPLY_AUTO_AUX_FLOOR   3024 


/* UF_PARAM_ACCESS_VECTOR
 *
 *  Description:
 *      This parameter specifies access vector for the contour profile method of 
 *      surface milling to determine the trace curve in no-floor case and to 
 *      work as the normal of the automatic auxiliary floor
 *
 *  Type: UF_PARAM_type_3d
 *
 *  Name: Access Vector
 *  Variable Name: <prefix>_access_vector
 *
 *  Possible Values: UF_PARAM_type_3d

 *
 * 
 */
#define UF_PARAM_ACCESS_VECTOR   3025 


typedef enum
{
    UF_PARAM_access_vector_method_zm = 0,  /* positive z-direction of MCS */
    UF_PARAM_access_vector_method_neg_zm,  /* negative z-direction of MCS */
    UF_PARAM_access_vector_method_specify  /* user specified */
} UF_PARAM_access_vector_method_t;


/* UF_PARAM_ACCESS_VECTOR_METHOD
 *
 *  Description:
 *      This parameter specifies method of the access vector for the 
 *      contour profile method of surface milling.
 *
 *  Type: UF_PARAM_type_int
 *
 *  Name: Access Vector Method
 *  Variable Name: <prefix>_access_vector_method
 *
 *  Possible Values: UF_PARAM_access_vector_method_t
 *
 * 
 */
#define UF_PARAM_ACCESS_VECTOR_METHOD   3026 


/* UF_PARAM_USE_AUX_FLOOR_MULTIPASS
 *
 *  Description:
 *      This parameter specifies if "auxiliary floor" is used for multipass.
 *
 *  Type: UF_PARAM_type_logical
 *
 *  Name: Aux Floor MULTIPASS
 *  Variable Name: <prefix>_aux_floor_multipass
 *
 *  Possible Values:
 *                false (default)
 *                true-custom
 *
 * 
 */
#define UF_PARAM_USE_AUX_FLOOR_MULTIPASS   3027 


/* UF_PARAM_START_TOOL_AXIS_GUIDE_VECTOR
 *
 *  Description:
 *  This index is the tag for the start tool axis guide vector
 *
 *  Type: UF_PARAM_type_tag 
 * 
 *  Name: Start Tool Axis Guide Vector 
 *  Variable Name: <prefix>_start_tool_axis_guide_vector
 * 
 *  Possible Values: UF_PARAM_type_tag 
 * 
 * 
 */
#define UF_PARAM_START_TOOL_AXIS_GUIDE_VECTOR   3028 


/* UF_PARAM_END_TOOL_AXIS_GUIDE_VECTOR
 *
 *  Description:
 *  This index is the tag for the end tool axis guide vector
 *
 *  Type: UF_PARAM_type_tag 
 * 
 *  Name: End Tool Axis Guide Vector 
 *  Variable Name: <prefix>_end_tool_axis_guide_vector
 * 
 *  Possible Values: UF_PARAM_type_tag 
 * 
 * 
 */
#define UF_PARAM_END_TOOL_AXIS_GUIDE_VECTOR   3029 


/* UF_PARAM_TEXT_DEPTH
 *
 *   Description:
 *      Text Depth is a positive distance indicating
 *      the depth of the text geometry to be cut.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Text Depth
 *  Variable Name: <prefix>_text_depth
 *
 *   Possible Values: Zero or positive double
 *
 * 
 */
#define UF_PARAM_TEXT_DEPTH   3031 


typedef enum
{
    UF_PARAM_tool_axis_guide_vector_method_auto = 0,  /* automatic */
    UF_PARAM_tool_axis_guide_vector_method_guide      /* user specified */
} UF_PARAM_tool_axis_guide_vector_method_t;


/* UF_PARAM_START_TOOL_AXIS_GUIDE_VEC_METHOD
 *
 *  Description:
 *      This parameter specifies method of the start tool axis guide vector
 *
 *  Type: UF_PARAM_type_int
 *
 *  Name: Start Tool Axis Guide Vector Method
 *  Variable Name: <prefix>_start_tool_axis_guide_vector_method
 *
 *  Possible Values: UF_PARAM_tool_axis_guide_vector_method_t
 *
 * 
 */
#define UF_PARAM_START_TOOL_AXIS_GUIDE_VEC_METHOD   3032 


/* UF_PARAM_END_TOOL_AXIS_GUIDE_VEC_METHOD
 *
 *  Description:
 *      This parameter specifies method of the end tool axis guide vector
 *
 *  Type: UF_PARAM_type_int
 *
 *  Name: End Tool Axis Guide Vector Method
 *  Variable Name: <prefix>_end_tool_axis_guide_vector_method
 *
 *  Possible Values: UF_PARAM_tool_axis_guide_vector_method_t
 *
 * 
 */
#define UF_PARAM_END_TOOL_AXIS_GUIDE_VEC_METHOD   3033 


typedef enum
{
    UF_PARAM_ttmopr_subop_type_rapid        = 0,
    UF_PARAM_ttmopr_subop_type_linfeed      = 1,
    UF_PARAM_ttmopr_subop_type_set_engage   = 4,
    UF_PARAM_ttmopr_subop_type_set_retract  = 5,
    UF_PARAM_ttmopr_subop_type_follow_curve = 6,
    UF_PARAM_ttmopr_subop_type_mce          = 7
} UF_PARAM_ttmopr_subop_type_t;

/* UF_PARAM_TTMOPR_SUBOP_TYPE
 *
 *   Description:
 *      This parameter identifies the type of the suboperation.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Teach Mode Item Type
 *  Variable Name: <prefix>_teach_mode_item_type
 *
 *   Possible Values: UF_PARAM_ttmopr_subop_type_t
 *
 * 
 */
#define UF_PARAM_TTMOPR_SUBOP_TYPE   3210  


typedef enum
{
    UF_PARAM_ttmopr_motion_axes_direct = 0,
    UF_PARAM_ttmopr_motion_axes_radial_only,
    UF_PARAM_ttmopr_motion_axes_axial_only,
    UF_PARAM_ttmopr_motion_axes_radial_axial,
    UF_PARAM_ttmopr_motion_axes_axial_radial
} UF_PARAM_ttmopr_motion_axes_type_t;

/* UF_PARAM_TTMOPR_MOTION_AXES
 *
 *   Description:
 *      This parameter defines the motion output for the linear
 *      Teachmode suboperations.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Teach Mode Motion axes locked
 *  Variable Name: <prefix>_teach_mode_motion_axes_locked
 *
 *   Possible Values: UF_PARAM_ttmopr_motion_axes_type_t
 *
 * 
 */
#define UF_PARAM_TTMOPR_MOTION_AXES   3211 


/* UF_PARAM_TTMOPR_END_POINT
 *
 *   Description:
 *      This parameter holds the tag of the end point (smart point) for a
 *      teachmode suboperation type rapid or linear feed with end point type
 *      set to "UF_PARAM_ttmopr_end_point_type_point".
 *      The end point mode is set in parameter UF_PARAM_TTMOPR_END_POINT_TYPE.
 *
 *   Type: UF_PARAM_type_tag
 *
 *   Name: Teach Mode Motion end point
 *  Variable Name: <prefix>_teach_mode_motion_end_point
 *
 *   Possible Values:
 *         0 (no entity)
 *         entity value
 *
 * 
 */
#define UF_PARAM_TTMOPR_END_POINT   3212  


typedef enum
{
    UF_PARAM_ttmopr_popaway_method_none = 0,
    UF_PARAM_ttmopr_popaway_method_automatic,
    UF_PARAM_ttmopr_popaway_method_manual
} UF_PARAM_ttmopr_popaway_method_t;

/* UF_PARAM_TTMOPR_POPAWAY_MTHD
 *
 *   Description:
 *      This parameter activates and defines the popaway move for rapid motion
 *      suboperation in Teachmode.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Teach Mode Pop-away method
 *  Variable Name: <prefix>_teach_mode_pop_away_method
 *
 *   Possible Values: UF_PARAM_ttmopr_popaway_method_t
 *
 * 
 */
#define UF_PARAM_TTMOPR_POPAWAY_MTHD   3213  


/* UF_PARAM_TTMOPR_POPAWAY_DIST
 *
 *   Description:
 *      This parameter defines the length of the popaway motion in teachmode
 *      rapid motion suboperation if the suboperation's popaway method is set
 *      to UF_PARAM_ttmopr_popaway_method_manual
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Teach Mode Pop-away distance
 *  Variable Name: <prefix>_teach_mode_pop_away_distance
 *
 *   Possible Values: positive double
 *
 * 
 */
#define UF_PARAM_TTMOPR_POPAWAY_DIST   3214 


/* UF_PARAM_TTMOPR_POPAWAY_ANGLE
 *
 *   Description:
 *      This parameter defines the angle of the popaway motion in teachmode
 *      rapid motion suboperation if the suboperation's popaway method is set
 *      to UF_PARAM_ttmopr_popaway_method_manual. The angle must be relative to
 *      the positive spindle axis.
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Teach Mode Pop-away angle
 *  Variable Name: <prefix>_teach_mode_pop_away_angle
 *
 *   Possible Values: angle (degree)
 *
 * 
 */
#define UF_PARAM_TTMOPR_POPAWAY_ANGLE   3215 


typedef enum
{
    UF_PARAM_ttmopr_feedrate_type_approach = 0,
    UF_PARAM_ttmopr_feedrate_type_engage,
    UF_PARAM_ttmopr_feedrate_type_cut,
    UF_PARAM_ttmopr_feedrate_type_retract,
    UF_PARAM_ttmopr_feedrate_type_depart,
    UF_PARAM_ttmopr_feedrate_type_traverse,
    UF_PARAM_ttmopr_feedrate_type_return,
    UF_PARAM_ttmopr_feedrate_type_custom
} UF_PARAM_ttmopr_feedrate_type_t;

/* UF_PARAM_TTMOPR_FEEDRATE_TYPE
 *
 *   Description:
 *      This parameter defines the feedrate type to be used for the linear motion
 *      suboperation in TURN/Teachmode.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Teach Mode Feedrate Type
 *  Variable Name: <prefix>_teach_mode_feedrate_type
 *
 *   Possible Values: UF_PARAM_ttmopr_feedrate_type_t
 *
 * 
 */
#define UF_PARAM_TTMOPR_FEEDRATE_TYPE   3216 


/* UF_PARAM_TTMOPR_FEEDRATE_VALUE
 *
 *   Description:
 *      With this parameter you set the feedrate value for TURN/Teachmode's
 *      linear feedrate suboperation, if the feedrate type is set to
 *      UF_PARAM_ttmopr_feedrate_type_custom in UF_PARAM_TTMOPR_FEEDRATE_TYPE
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Teach Mode Feedrate Value
 *  Variable Name: <prefix>_teach_mode_feedrate_value
 *
 *   Possible Values: double
 *
 * 
 */
#define UF_PARAM_TTMOPR_FEEDRATE_VALUE   3217  


typedef enum
{
    UF_PARAM_ttmopr_feedrate_unit_per_rev = 0,
    UF_PARAM_ttmopr_feedrate_unit_per_min
} UF_PARAM_ttmopr_feedrate_unit_t;

/* UF_PARAM_TTMOPR_FEEDRATE_UNIT
 *
 *   Description:
 *      With this parameter you set the feedrate unit for TURN/Teachmode's
 *      linear feedrate suboperation, if the feedrate type is set to
 *      UF_PARAM_ttmopr_feedrate_type_custom in UF_PARAM_TTMOPR_FEEDRATE_TYPE
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Teach Mode Feedrate Unit
 *  Variable Name: <prefix>_teach_mode_feedrate_unit
 *
 *   Possible Values: UF_PARAM_ttmopr_feedrate_unit_t
 *
 * 
 */
#define UF_PARAM_TTMOPR_FEEDRATE_UNIT   3218 


typedef enum
{
    UF_PARAM_ttmopr_end_point_type_point = 0,
    UF_PARAM_ttmopr_end_point_type_curves
} UF_PARAM_ttmopr_end_point_type_t;

/* UF_PARAM_TTMOPR_END_POINT_TYPE
 *
 *   Description:
 *      This parameter defines the type how the linear motion's endpoint
 *      is defined
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Teach Mode End point type
 *  Variable Name: <prefix>_teach_mode_end_point_type
 *
 *   Possible Values: UF_PARAM_ttmopr_end_point_type_t
 *
 * 
 */
#define UF_PARAM_TTMOPR_END_POINT_TYPE   3221  /* int */


/* UF_PARAM_TTMOPR_USE_TWO_CURVES
 *
 *   Description:
 *      This parameter defines whether two curves are used to define the
 *      linear motion's end point for the end point type set to
 *      UF_PARAM_ttmopr_end_point_type_curves in UF_PARAM_TTMOPR_END_POINT_TYPE
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Teach Mode Use two curves
 *  Variable Name: <prefix>_teach_mode_use_two_curves
 *
 *   Possible Values:
 *     0 = inactive
 *     1 = active
 *
 * 
 */
#define UF_PARAM_TTMOPR_USE_TWO_CURVES   3222  /* int */


typedef enum
{
    UF_PARAM_ttmopr_curve_tool_pos_to = 0,
    UF_PARAM_ttmopr_curve_tool_pos_on,
    UF_PARAM_ttmopr_curve_tool_pos_past
} UF_PARAM_ttmopr_curve_tool_pos_t;

/* UF_PARAM_TTMOPR_FIRST_CURVE_TOOL_POS
 *
 *   Description:
 *      This parameter defines the destination tool position relative to the
 *      first curve for linear motion suboperations in TURN/Teachmode.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Teach Mode First curve tool position
 *  Variable Name: <prefix>_teach_mode_first_curve_tool_position
 *
 *   Possible Values: UF_PARAM_ttmopr_curve_tool_pos_t
 *
 * 
 */
#define UF_PARAM_TTMOPR_FIRST_CURVE_TOOL_POS   3223  /* int */


/* UF_PARAM_TTMOPR_FIRST_CURVE_STOCK
 *
 *   Description:
 *      This parameter defines the stock remaining between tool and the first
 *      curve (distance between curve and tool nose) for linear motion
 *      suboperations in TURN/Teachmode.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Teach Mode First curve stock
 *  Variable Name: <prefix>_teach_mode_first_curve_stock
 *
 *   Possible Values: positive double (or 0)
 *
 * 
 */
#define UF_PARAM_TTMOPR_FIRST_CURVE_STOCK   3224  /* double_length */


/* UF_PARAM_TTMOPR_FIRST_CURVE_TAG
 *
 *   Description:
 *      This parameter stores the tag of the first curve for linear motion
 *      end point definition of type UF_PARAM_ttmopr_end_point_type_curves
 *
 *   Type: UF_PARAM_type_tag
 *
 *   Name: Teach Mode First curve tag
 *  Variable Name: <prefix>_teach_mode_first_curve_tag
 *
 *   Possible Values:
 *         0 (no entity)
 *         entity value referencing a 2D curve
 *
 * 
 */
#define UF_PARAM_TTMOPR_FIRST_CURVE_TAG   3225  /* tag */


/* UF_PARAM_TTMOPR_SECOND_CURVE_TOOL_POS
 *
 *   Description:
 *      This parameter defines the destination tool position relative to the
 *      second curve for linear motion suboperations in TURN/Teachmode.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Teach Mode Second curve tool position
 *  Variable Name: <prefix>_teach_mode_second_curve_tool_position
 *
 *   Possible Values: UF_PARAM_ttmopr_curve_tool_pos_t
 *
 * 
 */
#define UF_PARAM_TTMOPR_SECOND_CURVE_TOOL_POS   3226  /* int */


/* UF_PARAM_TTMOPR_SECOND_CURVE_STOCK
 *
 *   Description:
 *      This parameter defines the stock remaining between tool and the second
 *      curve (distance between curve and tool nose) for linear motion
 *      suboperations in TURN/Teachmode.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Teach Mode Second curve stock
 *  Variable Name: <prefix>_teach_mode_second_curve_stock
 *
 *   Possible Values: positive double (or 0)
 *
 * 
 */
#define UF_PARAM_TTMOPR_SECOND_CURVE_STOCK   3227  /* double_length */


/* UF_PARAM_TTMOPR_SECOND_CURVE_TAG
 *
 *   Description:
 *      This parameter stores the tag of the second curve for linear motion
 *      end point definitions of type UF_PARAM_ttmopr_end_point_type_curves
 *
 *   Type: UF_PARAM_type_tag
 *
 *   Name: Teach Mode Second curve tag
 *  Variable Name: <prefix>_teach_mode_second_curve_tag
 *
 *   Possible Values:
 *         0 (no entity)
 *         entity value referencing a 2D curve
 *
 * 
 */
#define UF_PARAM_TTMOPR_SECOND_CURVE_TAG   3228  /* tag */


typedef enum
{
    UF_PARAM_ttmopr_drive_type_prev_check_curve = 0,
    UF_PARAM_ttmopr_drive_type_prev_drive_curve,
    UF_PARAM_ttmopr_drive_type_new_drive_curve
} UF_PARAM_ttmopr_drive_type_t;

/* UF_PARAM_TTMOPR_DRIVE_TYPE
 *
 *   Description:
 *      With this parameter you can control where Follow Curve Motion suboperation
 *      of TURN/Teachmode retrieves it's drive geometry from.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Teach Mode Drive Geom Type
 *  Variable Name: <prefix>_teach_mode_drive_geom_type
 *
 *   Possible Values: UF_PARAM_ttmopr_drive_type_t
 *
 * 
 */
#define UF_PARAM_TTMOPR_DRIVE_TYPE   3250 


typedef enum
{
    UF_PARAM_ttmopr_cut_direction_forward = 0,
    UF_PARAM_ttmopr_cut_direction_reverse
} UF_PARAM_ttmopr_cut_direction_t;

/* UF_PARAM_TTMOPR_CUT_DIRECTION
 *
 *   Description:
 *      This parameter controls whether TURN/Teachmode suboperation "Follow
 *      Curve Motion" cuts with (forward) or against (reverse) boundary direction.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Teach Mode Cut Direction
 *  Variable Name: <prefix>_teach_mode_cut_direction
 *
 *   Possible Values: UF_PARAM_ttmopr_cut_direction_t
 *
 * 
 */
#define UF_PARAM_TTMOPR_CUT_DIRECTION   3252  


typedef enum
{
    UF_PARAM_ttmopr_start_type_start = 0,
    UF_PARAM_ttmopr_start_type_point,
    UF_PARAM_ttmopr_start_type_check,
    UF_PARAM_ttmopr_start_type_last_pos
} UF_PARAM_ttmopr_start_type_t;

/* UF_PARAM_TTMOPR_START_TYPE
 *
 *   Description:
 *      This parameter defines the Start method for Teachmode suboperations
 *      of type "Follow Curve Motion"
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Teach Mode Start Type
 *  Variable Name: <prefix>_teach_mode_start_type
 *
 *   Possible Values: UF_PARAM_ttmopr_start_type_t
 *
 * 
 */
#define UF_PARAM_TTMOPR_START_TYPE   3253 


/* UF_PARAM_TTMOPR_START_POINT_TAG
 *
 *   Description:
 *      This paramater holds the start point tag for follow curve motion using
 *      start type of UF_PARAM_ttmopr_start_type_point
 *
 *   Type: UF_PARAM_type_tag
 *
 *   Name: Teach Mode Start Point
 *  Variable Name: <prefix>_teach_mode_start_point
 *
 *   Possible Values:
 *         0 (no entity)
 *         entity value
 *
 * 
 */
#define UF_PARAM_TTMOPR_START_POINT_TAG   3254 


/* UF_PARAM_TTMOPR_START_CHECK_STOCK
 *
 *   Description:
 *      This parameter holds the equidistant, face and radial stock settings
 *      for the follow curve motion's start check geometry in TURN/Teachmode.
 *
 *   Type: UF_PARAM_type_3d_length
 *
 *   Name: Teach Mode Start Check Stock
 *  Variable Name: <prefix>_teach_mode_start_check_stock
 *
 *   Possible Values: [0] = equidistant stock
 *                    [1] = face stock
 *                    [2] = radial stock
 *
 * 
 */
#define UF_PARAM_TTMOPR_START_CHECK_STOCK   3256 


typedef enum
{
    UF_PARAM_ttmopr_stop_type_end = 0,
    UF_PARAM_ttmopr_stop_type_point,
    UF_PARAM_ttmopr_stop_type_check,
    UF_PARAM_ttmopr_stop_type_last_pos
} UF_PARAM_ttmopr_stop_type_t;

/* UF_PARAM_TTMOPR_STOP_TYPE
 *
 *   Description:
 *      This parameter defines the Stop method for Teachmode suboperations
 *      of type "Follow Curve Motion"
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Teach Mode Stop Type
 *  Variable Name: <prefix>_teach_mode_stop_type
 *
 *   Possible Values: UF_PARAM_ttmopr_stop_type_t
 *
 * 
 */
#define UF_PARAM_TTMOPR_STOP_TYPE   3257 


/* UF_PARAM_TTMOPR_STOP_POINT_TAG
 *
 *   Description:
 *      This paramater holds the stop point tag for follow curve motion using
 *      stop type of UF_PARAM_ttmopr_stop_type_point
 *
 *   Type: UF_PARAM_type_tag
 *
 *   Name: Teach Mode Stop Point
 *  Variable Name: <prefix>_teach_mode_stop_point
 *
 *   Possible Values: 
 *         0 (no entity)
 *         entity value
 *
 * 
 */
#define UF_PARAM_TTMOPR_STOP_POINT_TAG   3258 


/* UF_PARAM_TTMOPR_STOP_CHECK_STOCK
 *
 *   Description:
 *      This parameter holds the equidistant, face and radial stock settings
 *      for the follow curve motion's stop check geometry in TURN/Teachmode.
 *
 *   Type: UF_PARAM_type_3d_length
 *
 *   Name: Teach Mode Stop Check Stock
 *  Variable Name: <prefix>_teach_mode_stop_check_stock
 *
 *   Possible Values: [0] = equidistant stock
 *                    [1] = face stock
 *                    [2] = radial stock
 *
 * 
 */
#define UF_PARAM_TTMOPR_STOP_CHECK_STOCK   3260 


/* UF_PARAM_TTMOPR_USE_ENG_TOG
 *
 *   Description:
 *      This parameter activates/deactivates the engage setting to be applied
 *      for this suboperation. If this parameter is activated, the follow curve
 *      motion will create an engage motion even if the tool is already in
 *      tolerance with the drive curve. If deactivated, the suboperation will
 *      not create an engage motion using the last engage setting.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Teach Mode Use Engage Setting
 *  Variable Name: <prefix>_teach_mode_use_engage_setting
 *
 *   Possible Values: 
 *     0 = inactive
 *     1 = active
 *
 * 
 */
#define UF_PARAM_TTMOPR_USE_ENG_TOG   3261 


/* UF_PARAM_TTMOPR_USE_RET_TOG
 *
 *   Description:
 *      This parameter activates/deactivates the retract setting to be applied
 *      for this suboperation. If this parameter is activated, the follow curve
 *      motion will create a retract motion at the end of the drive path.
 *      If deactivated, the tool will stop at the end point of the drive path.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Teach Mode Use Retract Setting
 *  Variable Name: <prefix>_teach_mode_use_retract_setting
 *
 *   Possible Values: 
 *     0 = inactive
 *     1 = active
 *
 * 
 */
#define UF_PARAM_TTMOPR_USE_RET_TOG   3262 


typedef enum
{
    UF_PARAM_ttmopr_extend_method_by_value = 0,
    UF_PARAM_ttmopr_extend_method_to_blank
} UF_PARAM_ttmopr_extend_method_t;

/* UF_PARAM_TTMOPR_EXTEND_METHOD
 *
 *   Description:
 *      This indicates the method how the drive curve should be
 *      extended in the follow curve motion suboperation. This parameter is
 *      applicable in the engage and retract settings suboperations of
 *      TURN/Teachmode.
 *      Drive curve extension is deactivated by setting this parameter to
 *      UF_PARAM_ttmopr_extend_method_by_value and setting the extend distance to 0.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Teach Mode Extend Method
 *  Variable Name: <prefix>_teach_mode_extend_method
 *
 *   Possible Values: UF_PARAM_ttmopr_extend_method_t
 *
 * 
 */
#define UF_PARAM_TTMOPR_EXTEND_METHOD   3263 


/* UF_PARAM_TTMOPR_EXTEND_DISTANCE
 *
 *   Description:
 *      This parameter defines the extend distance by which the
 *      drive curve is extended in the follow curve motion suboperation.
 *      Set UF_PARAM_TTMOPR_EXTEND_METHOD to
 *      UF_PARAM_ttmopr_extend_method_by_value to use this parameter.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Teach Mode Extend Distance
 *  Variable Name: <prefix>_teach_mode_extend_distance
 *
 *   Possible Values: double
 *                    (0.0 will deactivate drive curve extension)
 *
 * 
 */
#define UF_PARAM_TTMOPR_EXTEND_DISTANCE   3264 


typedef enum
{
    UF_PARAM_ttmopr_start_stop_treatment_after = 0,
    UF_PARAM_ttmopr_start_stop_treatment_before
} UF_PARAM_ttmopr_start_stop_treatment_t;

/* UF_PARAM_TTMOPR_START_STOP_TREATMENT
 *
 *   Description:
 *      This indicates the method how the start and stop point or geometry
 *      is to be evaluated. I.e. whether start/stop are evaluated before or
 *      after offsetting and gouge checking the drive curve in the follow curve
 *      motion suboperation.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Teach Mode Start/Stop Treatment
 *  Variable Name: <prefix>_teach_mode_start_stop_treatment
 *
 *   Possible Values: UF_PARAM_ttmopr_start_stop_treatment_t
 *
 * 
 */
#define UF_PARAM_TTMOPR_START_STOP_TREATMENT   3265 


/* UF_PARAM_TTDOPR_PITCH_LEAD
 *
 *   Description:
 *      This parameter specifies the Pitch or the Lead value of a thread.
 *      The value is interpreted depending on the parameter 
 *      UF_PARAM_TTDOPR_PITCH_LEAD_TPU_INPUT.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Turn Thread Pitch Lead
 *  Variable Name: <prefix>_turn_thread_pitch_lead
 *
 *   Possible Values: Positive double (greater than zero)
 *
 * 
 */
#define UF_PARAM_TTDOPR_PITCH_LEAD   3300 


/* UF_PARAM_TTDOPR_PITCH_LEAD_TPU_END_INCREMENT
 *
 *   Description:
 *      This parameter specifies the End or Increment value for variable
 *      threads.
 *      The value is interpreted depending on the parameter
 *      UF_PARAM_PITCH_VAR_TYPE:
 *          0 - Constant:          Parameter is not use
 *          1 - Start & End:       Parameter specifies End value
 *          2 - Start & Increment: Parameter specifies Increment value
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Turn Thread Tpu
 *  Variable Name: <prefix>_turn_thread_tpu
 *
 *   Possible Values: Positive double (greater than zero)
 *
 * 
 */
#define UF_PARAM_TTDOPR_PITCH_LEAD_TPU_END_INCREMENT   3301 


typedef enum
{
    UF_PARAM_ttdopr_input_unit_pitch = 0,
    UF_PARAM_ttdopr_input_unit_lead,
    UF_PARAM_ttdopr_input_unit_tpu
} UF_PARAM_ttdopr_pitch_lead_tpu_input_unit_t;


/* UF_PARAM_TTDOPR_PITCH_LEAD_TPU_INPUT
 *
 *   Description:
 *      This parameter specifies the input unit of the Pitch/Lead/Tpu value.
 *      It also specifies which parameter is used as Pitch, Lead or TPU value:
 *      UF_PARAM_ttdopr_input_unit_pitch
 *        or
 *      UF_PARAM_ttdopr_input_unit_lead:  UF_PARAM_TTDOPR_PITCH_LEAD 
 *      UF_PARAM_ttdopr_input_unit_tpu:   UF_PARAM_TTDOPR_TPU
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Turn Thread Pitch End/Increment
 *  Variable Name: <prefix>_turn_thread_pitch_end_increment
 *
 *   Possible Values: UF_PARAM_ttdopr_pitch_lead_tpu_input_unit_t
 *
 * 
 */
#define UF_PARAM_TTDOPR_PITCH_LEAD_TPU_INPUT   3302 


/* UF_PARAM_TTDOPR_TPU
 *
 *   Description:
 *      This parameter specifies the Thread per Unit value of a thread.
 *      It could be Thread per Inch or Thread per mm depending on the part
 *      unit.
 *      This parameter is only used if parameter
 *      UF_PARAM_TTDOPR_PITCH_LEAD_TPU_INPUT is set to 
 *      UF_PARAM_ttdopr_input_unit_tpu.
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Turn Thread Pitch Input Unit
 *  Variable Name: <prefix>_turn_thread_pitch_input_unit
 *
 *   Possible Values: Positive double (greater than zero)
 *
 * 
 */
#define UF_PARAM_TTDOPR_TPU   3303 


/* UF_PARAM_TTDOPR_CREST_LINE_TAG
 *
 *   Description:
 *      This parameter holds the object ID of the crest line, which defines
 *      the thread geometry. The start and end point of the thread are 
 *      generated from the crest line.
 *
 *   Type: UF_PARAM_type_tag
 *
 *   Name: Crest Line Tag
 *  Variable Name: <prefix>_crest_line_tag
 *
 *   Possible Values:
 *         0 (no entity)
 *         entity ID
 *
 * 
 */
#define UF_PARAM_TTDOPR_CREST_LINE_TAG   3310 


/* UF_PARAM_TTDOPR_CREST_LINE_1ST_PT_IS_START_PT
 *
 *   Description:
 *      This flag indicates if the start point of the selected crestline
 *      (stored in parameter UF_PARAM_TTDOPR_CREST_LINE_TAG) is also the 
 *      start point of the thread or if it is the end point of the thread.
 *
 *   Type: UF_PARAM_type_logical
 *
 *   Name: Crest Line 1st Pt Is Start Pt Flag
 *  Variable Name: <prefix>_crest_line_1st_pt_is_start_pt_flag
 *
 *   Possible Values: 
 *        0 - False: Start point of line is end point of thread
 *        1 - True:  Start point of line is start point of thread
 *
 * 
 */
#define UF_PARAM_TTDOPR_CREST_LINE_1ST_PT_IS_START_PT   3311 


/* UF_PARAM_TTDOPR_END_LINE_TAG
 *
 *   Description:
 *      This parameter holds the tag of the thread end line. The instersection
 *      point of the crestline and the end line defines the end point of
 *      thread geometry.
 *      If end line tag is 0, the end point of the crestline is used as thread
 *      geometry end point.
 *
 *   Type: UF_PARAM_type_tag
 *
 *   Name: End Line Tag
 *  Variable Name: <prefix>_end_line_tag
 *
 *   Possible Values: 
 *         0 (no entity)
 *         entity ID
 *
 * 
 */
#define UF_PARAM_TTDOPR_END_LINE_TAG   3320 


typedef enum
{
    UF_PARAM_ttdopr_type_root_line = 0,
    UF_PARAM_ttdopr_type_depth_angle
} UF_PARAM_ttdopr_total_depth_type_t;


/* UF_PARAM_TTDOPR_TOTAL_DEPTH_TYPE
 *
 *   Description:
 *      This parameter specifies how the total depth of the thread is defined.
 *      In Root Line mode the parameter UF_PARAM_TTDOPR_ROOT_LINE_TAG holds
 *      the tag of an associative line, which defines the thread angle and 
 *      depth.
 *      In Depth & Angle mode these values are stored in parameters
 *      UF_PARAM_TTDOPR_TOTAL_DEPTH and
 *      UF_PARAM_TTDOPR_TOTAL_DEPTH_ANGLE.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Total Depth Type
 *  Variable Name: <prefix>_total_depth_type
 *
 *   Possible Values: UF_PARAM_ttdopr_total_depth_type_t
 *
 * 
 */
#define UF_PARAM_TTDOPR_TOTAL_DEPTH_TYPE   3330 


/* UF_PARAM_TTDOPR_ROOT_LINE_TAG
 *
 *   Description:
 *      This parameter holds the tag of the root line, which defines the 
 *      thread angle and depth.
 *      It is only used if UF_PARAM_TTDOPR_TOTAL_DEPTH_TYPE is set to 
 *      Root Line mode.
 *
 *   Type: UF_PARAM_type_tag
 *
 *   Name: Root Line Tag
 *  Variable Name: <prefix>_root_line_tag
 *
 *   Possible Values:
 *         0 (no entity)
 *         entity ID
 *
 * 
 */
#define UF_PARAM_TTDOPR_ROOT_LINE_TAG   3331 


/* UF_PARAM_TTDOPR_TOTAL_DEPTH
 *
 *   Description:
 *      This parameter specifies the depth of a thread.
 *      It is only used if UF_PARAM_TTDOPR_TOTAL_DEPTH_TYPE is set to 
 *      Depth & Angle mode.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Total Depth
 *  Variable Name: <prefix>_total_depth
 *
 *   Possible Values: Positive double (greater than zero)
 *
 * 
 */
#define UF_PARAM_TTDOPR_TOTAL_DEPTH   3332 


/* UF_PARAM_TTDOPR_TOTAL_DEPTH_ANGLE
 *
 *   Description:
 *      This parameter specifies the angle (in radians) of a thread.
 *      It is only used if UF_PARAM_TTDOPR_TOTAL_DEPTH_TYPE is set to 
 *      Depth & Angle mode.
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Total Depth Angle
 *  Variable Name: <prefix>_total_depth_angle
 *
 *   Possible Values: Double (angle in radians)
 *
 * 
 */
#define UF_PARAM_TTDOPR_TOTAL_DEPTH_ANGLE   3333 


typedef enum
{
    UF_PARAM_ttdopr_increment_type_constant = 0,
    UF_PARAM_ttdopr_increment_type_variable,
    UF_PARAM_ttdopr_increment_type_percentage
} UF_PARAM_ttdopr_increment_type_t;


/* UF_PARAM_TTDOPR_INCREMENT_TYPE
 *
 *   Description:
 *      This parameter specifies how the the total thread depth is divided
 *      into single thread passes.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Total Depth Increment Type
 *  Variable Name: <prefix>_total_depth_increment_type
 *
 *   Possible Values: UF_PARAM_ttdopr_increment_type_t
 *
 * 
 */
#define UF_PARAM_TTDOPR_INCREMENT_TYPE   3334 


/* UF_PARAM_TTDOPR_TOLERANCE
 *
 *   Description:
 *      This parameter specifies the depth tolerance of uncut material 
 *      between the depth of the last thread pass and the total thread depth.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Total Depth Tolerance
 *  Variable Name: <prefix>_total_depth_tolerance
 *
 *   Possible Values: Positive double (or zero)
 *
 * 
 */
#define UF_PARAM_TTDOPR_TOLERANCE   3335 


/* UF_PARAM_TTDOPR_CONST_INCREMENT
 *
 *   Description:
 *      This parameter specifies a single constant increment depth for the 
 *      thread passes.
 *      Only used if parameter UF_PARAM_TTDOPR_INCREMENT_TYPE is set to
 *      'Constant'.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Total Depth Constant Increment
 *  Variable Name: <prefix>_total_depth_constant_increment
 *
 *   Possible Values: Positive double (greater than zero)
 *
 * 
 */
#define UF_PARAM_TTDOPR_CONST_INCREMENT   3340 


/* UF_PARAM_TTDOPR_VARIABLE_NO_OF_PASSES
 *
 *   Description:
 *      This parameter specifies the number of times the belonging variable
 *      increment (parameter UF_PARAM_TTDOPR_VARIABLE_INCREMENT) is 
 *      repeated.
 *      Up to 6 different increment depths can be defined.
 *      Only used if parameter UF_PARAM_TTDOPR_INCREMENT_TYPE is set to
 *      'Variable'.
 *
 *   Type: UF_PARAM_type_vla_int
 *
 *   Name: Total Depth Variable Number of Passes
 *  Variable Name: <prefix>_total_depth_variable_number_of_passes
 *
 *   Possible Values: Array (size of 6) of positive integers (or zero)
 *
 * 
 */
#define UF_PARAM_TTDOPR_VARIABLE_NO_OF_PASSES   3345 


/* UF_PARAM_TTDOPR_VARIABLE_INCREMENT
 *
 *   Description:
 *      This parameter specifies a set of variable increments.
 *      Up to 6 different increment depths can be defined.
 *      Every increment is cut as often as specified in parameter
 *      UF_PARAM_TTDOPR_VARIABLE_NO_OF_PASSES.
 *      Only used if parameter UF_PARAM_TTDOPR_INCREMENT_TYPE is set to
 *      'Variable'.
 *      This parameter is obsolete, use 
 *      UF_PARAM_TTDOPR_VARIABLE_INCREMENT_TOOL_DEPENDENT instead
 *
 *   Type: UF_PARAM_type_vla_length
 *
 *   Name: Total Depth Variable Increment
 *  Variable Name: <prefix>_total_depth_variable_increment
 *
 *   Possible Values: Array (size of 6) of positive doubles (or zero)
 *
 * 
 */
#define UF_PARAM_TTDOPR_VARIABLE_INCREMENT   3346   /* Obsolete in NX6 */


/* UF_PARAM_TTDOPR_PERCENTAGE
 *
 *   Description:
 *      This parameter specifies the increment of each thread pass as a 
 *      percentage of the total depth that remains at the time of the pass.
 *      It causes the step distance to decrease as the tool moves deeper into
 *      the thread. 
 *      Only used if parameter UF_PARAM_TTDOPR_INCREMENT_TYPE is set to
 *      'Percentage'.
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Total Depth Percentage
 *  Variable Name: <prefix>_total_depth_percentage
 *
 *   Possible Values: Positive double in domain (0; 100]
 *                    (excluding 0, including 100).
 *
 * 
 */
#define UF_PARAM_TTDOPR_PERCENTAGE   3350 


/* UF_PARAM_TTDOPR_PERCENTAGE_MAX
 *
 *   Description:
 *      This parameter specifies the maximum increment depth of a thread pass.
 *      If the pass increment exceeds the maxium it is restricted to that 
 *      value.
 *      Only used if parameter UF_PARAM_TTDOPR_INCREMENT_TYPE is set to
 *      'Percentage'.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Total Depth Percentage Maximum
 *  Variable Name: <prefix>_total_depth_percentage_maximum
 *
 *   Possible Values: Positive double (greater than zero)
 *
 * 
 */
#define UF_PARAM_TTDOPR_PERCENTAGE_MAX   3351 


/* UF_PARAM_TTDOPR_PERCENTAGE_MIN
 *
 *   Description:
 *      This parameter specifies the minimum increment depth of a thread pass.
 *      If the pass increment falls below the minimum it is raised to that 
 *      value.
 *      Only used if parameter UF_PARAM_TTDOPR_INCREMENT_TYPE is set to
 *      'Percentage'.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Total Depth Percentage Minimum
 *  Variable Name: <prefix>_total_depth_percentage_minimum
 *
 *   Possible Values: Positive double (greater than zero)
 *
 * 
 */
#define UF_PARAM_TTDOPR_PERCENTAGE_MIN   3352 


/* UF_PARAM_TTDOPR_STEPOVER_DIRECTION_ANGLE
 *
 *   Description:
 *      This parameter specifies the Turn Thread
 *      stepover direction angle in radians as 
 *      polar angle relative to MCS.
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Turn Thread Stepover Direction Angle
 *  Variable Name: <prefix>_turn_thread_stepover_direction_angle
 *
 *   Possible Values: double (0.0 - 2*PI)
 *
 * 
 */
#define UF_PARAM_TTDOPR_STEPOVER_DIRECTION_ANGLE   3355 


/* UF_PARAM_TTDOPR_FINISH_PASSES_NO_OF_PASSES
 *
 *   Description:
 *      This parameter specifies the number of times the belonging finish
 *      pass (parameter UF_PARAM_TTDOPR_FINISH_PASSES_INCREMENT) is 
 *      repeated.
 *      Up to 6 different finish increments can be defined.
 *
 *   Type: UF_PARAM_type_vla_int
 *
 *   Name: Total Depth Finish Passes Number of Passes
 *  Variable Name: <prefix>_total_depth_finish_passes_number_of_passes
 *
 *   Possible Values: Array (size of 6) of positive integers (or zero)
 *
 * 
 */
#define UF_PARAM_TTDOPR_FINISH_PASSES_NO_OF_PASSES   3360 


/* UF_PARAM_TTDOPR_FINISH_PASSES_INCREMENT
 *
 *   Description:
 *      This parameter specifies a set of finish increments.
 *      Up to 6 different finish increments can be defined.
 *      Every increment is cut as often as specified in parameter
 *      UF_PARAM_TTDOPR_FINISH_PASSES_NO_OF_PASSES.
 *
 *   Type: UF_PARAM_type_vla_length
 *
 *   Name: Total Depth Finish Passes Increment
 *  Variable Name: <prefix>_total_depth_finish_passes_increment
 *
 *   Possible Values: Array (size of 6) of positive doubles (or zero)
 *
 * 
 */
#define UF_PARAM_TTDOPR_FINISH_PASSES_INCREMENT   3361 


typedef enum
{
    UF_PARAM_ttdopr_engage_type_auto = 0,
    UF_PARAM_ttdopr_engage_type_vector,
    UF_PARAM_ttdopr_engage_type_angle
} UF_PARAM_ttdopr_engage_type_t;


/* UF_PARAM_TTDOPR_ENGAGE_TYPE
 *
 *   Description:
 *      This parameter specifies how the thread infeed angle is defined. 
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Thread Engage Type
 *  Variable Name: <prefix>_thread_engage_type
 *
 *   Possible Values: UF_PARAM_ttdopr_engage_type_t
 *
 * 
 */
#define UF_PARAM_TTDOPR_ENGAGE_TYPE   3370 


typedef enum
{
    UF_PARAM_ttdopr_retract_type_auto = 0,
    UF_PARAM_ttdopr_retract_type_vector,
    UF_PARAM_ttdopr_retract_type_angle
} UF_PARAM_ttdopr_retract_type_t;


/* UF_PARAM_TTDOPR_RETRACT_TYPE
 *
 *   Description:
 *      This parameter specifies how the thread pullout angle is defined. 
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Thread Retract Type
 *  Variable Name: <prefix>_thread_retract_type
 *
 *   Possible Values: UF_PARAM_ttdopr_retract_type_t
 *
 * 
 */
#define UF_PARAM_TTDOPR_RETRACT_TYPE   3371 


/* UF_PARAM_TTDOPR_INFEED_VECTOR
 *
 *   Description:
 *      This parameter holds a vector which specifies the thread infeed angle.
 *      Only used if parameter UF_PARAM_TTDOPR_ENGAGE_TYPE is set to
 *      'Vector'.
 *
 *   Type: UF_PARAM_type_vla_length
 *
 *   Name: Thread Infeed Vector
 *  Variable Name: <prefix>_thread_infeed_vector
 *
 *   Possible Values: Array (size of 2) of doubles
 *
 * 
 */
#define UF_PARAM_TTDOPR_INFEED_VECTOR   3375 


/* UF_PARAM_TTDOPR_INFEED_ANGLE
 *
 *   Description:
 *      This parameter specifies the thread infeed angle in radians.
 *      Only used if parameter UF_PARAM_TTDOPR_ENGAGE_TYPE is set to
 *      'Angle'.
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Thread Infeed Angle
 *  Variable Name: <prefix>_thread_infeed_angle
 *
 *   Possible Values: Double (in radians)
 *
 * 
 */
#define UF_PARAM_TTDOPR_INFEED_ANGLE   3376 


typedef enum
{
    UF_PARAM_ttdopr_infeed_type_engage = 0,
    UF_PARAM_ttdopr_infeed_type_thread
} UF_PARAM_ttdopr_infeed_type_t;


/* UF_PARAM_TTDOPR_INFEED_TYPE
 *
 *   Description:
 *      Specifies whether the thread infeed move is to be at the engage feed 
 *      rate or in thread lead (as a thread motion).
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Thread Infeed Type
 *  Variable Name: <prefix>_thread_infeed_type
 *
 *   Possible Values: UF_PARAM_ttdopr_infeed_type_t
 *
 * 
 */
#define UF_PARAM_TTDOPR_INFEED_TYPE   3377 


/* UF_PARAM_TTDOPR_PULLOUT_VECTOR
 *
 *   Description:
 *      This parameter holds a vector which specifies the thread pullout angle.
 *      Only used if parameter UF_PARAM_TTDOPR_RETRACT_TYPE is set to
 *      'Vector'.
 *
 *   Type: UF_PARAM_type_vla_length
 *
 *   Name: Thread Pullout Vector
 *  Variable Name: <prefix>_thread_pullout_vector
 *
 *   Possible Values: Array (size of 2) of doubles
 *
 * 
 */
#define UF_PARAM_TTDOPR_PULLOUT_VECTOR   3380 


/* UF_PARAM_TTDOPR_PULLOUT_ANGLE
 *
 *   Description:
 *      This parameter specifies the thread pullout angle in radians.
 *      Only used if parameter UF_PARAM_TTDOPR_RETRACT_TYPE is set to
 *      'Angle'.
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Thread Pullout Angle
 *  Variable Name: <prefix>_thread_pullout_angle
 *
 *   Possible Values: Double (in radians)
 *
 * 
 */
#define UF_PARAM_TTDOPR_PULLOUT_ANGLE   3381 


typedef enum
{
    UF_PARAM_ttdopr_pullout_type_retract = 0,
    UF_PARAM_ttdopr_pullout_type_thread
} UF_PARAM_ttdopr_pullout_type_t;


/* UF_PARAM_TTDOPR_PULLOUT_TYPE
 *
 *   Description:
 *      Specifies whether the pullout move is to be at the retract feed rate or
 *      in thread lead (as a thread motion).
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Thread Pullout Type
 *  Variable Name: <prefix>_thread_pullout_type
 *
 *   Possible Values: UF_PARAM_ttdopr_pullout_type_t
 *
 * 
 */
#define UF_PARAM_TTDOPR_PULLOUT_TYPE   3382 


typedef enum
{
    UF_PARAM_turn_workpiece_type_undefined = -1,
    UF_PARAM_turn_workpiece_type_cylinder  =  0,
    UF_PARAM_turn_workpiece_type_tube      =  1,
    UF_PARAM_turn_workpiece_type_curves    =  3,
    UF_PARAM_turn_workpiece_type_workspace =  6
} UF_PARAM_turn_workpiece_type_t;

/* UF_PARAM_TURN_WORKPIECE_TYPE
 *
 *   Description:
 *      This parameter controls the turning workpiece (blank) definition type.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Turn Workpiece Type
 *  Variable Name: <prefix>_turn_workpiece_type
 *
 *   Possible Values: UF_PARAM_turn_workpiece_type_t
 *
 * 
 */
#define UF_PARAM_TURN_WORKPIECE_TYPE   3400 


/* UF_PARAM_TURN_WORKPIECE_STOCK_EQUI
 *
 *   Description:
 *      This parameter holds the equidistant stock for turning blank definition
 *      of type UF_PARAM_turn_workpiece_type_curves.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Turn Workpiece Stock Equi
 *  Variable Name: <prefix>_turn_workpiece_stock_equi
 *
 *   Possible Values: positive double
 *
 * 
 */
#define UF_PARAM_TURN_WORKPIECE_STOCK_EQUI   3403 


/* UF_PARAM_TURN_WORKPIECE_STOCK_FACE
 *
 *   Description:
 *      This parameter holds the face stock for turning blank definition
 *      of type UF_PARAM_turn_workpiece_type_curves.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Turn Workpiece Stock Face
 *  Variable Name: <prefix>_turn_workpiece_stock_face
 *
 *   Possible Values: positive double
 *
 * 
 */
#define UF_PARAM_TURN_WORKPIECE_STOCK_FACE   3404 


/* UF_PARAM_TURN_WORKPIECE_STOCK_RADIAL
 *
 *   Description:
 *      This parameter holds the radial stock for turning blank definition
 *      of type UF_PARAM_turn_workpiece_type_curves.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Turn Workpiece Stock Radial
 *  Variable Name: <prefix>_turn_workpiece_stock_radial
 *
 *   Possible Values: positive double
 *
 * 
 */
#define UF_PARAM_TURN_WORKPIECE_STOCK_RADIAL   3405 


/* UF_PARAM_TURN_WORKPIECE_LENGTH
 *
 *   Description:
 *      This parameter holds the workpiece length for turning blank definition
 *      of type UF_PARAM_turn_workpiece_type_cylinder or ~tube.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Turn Workpiece Length
 *  Variable Name: <prefix>_turn_workpiece_length
 *
 *   Possible Values: positive double (!= 0)
 *
 * 
 */
#define UF_PARAM_TURN_WORKPIECE_LENGTH   3411 


/* UF_PARAM_TURN_WORKPIECE_DIAMETER
 *
 *   Description:
 *      This parameter holds the workpiece diameter for turning blank definition
 *      of type UF_PARAM_turn_workpiece_type_cylinder or ~tube.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Turn Workpiece Diameter
 *  Variable Name: <prefix>_turn_workpiece_diameter
 *
 *   Possible Values: positive double (!= 0)
 *
 * 
 */
#define UF_PARAM_TURN_WORKPIECE_DIAMETER   3412 


/* UF_PARAM_TURN_WORKPIECE_INNER_DIAMETER
 *
 *   Description:
 *      This parameter holds the inner diameter for turning blank definition
 *      of type UF_PARAM_turn_workpiece_type_tube.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Turn Workpiece Inner Diameter
 *  Variable Name: <prefix>_turn_workpiece_inner_diameter
 *
 *   Possible Values: positive double (!= 0 and less than outer diameter)
 *
 * 
 */
#define UF_PARAM_TURN_WORKPIECE_INNER_DIAMETER   3413 


/* UF_PARAM_TURN_WORKPIECE_LOC_TAG
 *
 *   Description:
 *      This parameter identifies the smart point for parametric
 *      workpiece positioning.
 *      It also identifies the workpiece target location for workpieces retrieved
 *      from a different workspace
 *
 *   Type: UF_PARAM_type_tag
 *
 *   Name: Turn Workpiece Location Point
 *  Variable Name: <prefix>_turn_workpiece_location_point
 *
 *   Possible Values:
 *         0 (no entity)
 *         entity value
 *
 * 
 */
#define UF_PARAM_TURN_WORKPIECE_LOC_TAG   3420 


typedef enum
{
    UF_PARAM_turn_workpiece_direction_towards_head_stock = -1,
    UF_PARAM_turn_workpiece_direction_from_head_stock    =  1
} UF_PARAM_turn_workpiece_direction_t;

/* UF_PARAM_TURN_WORKPIECE_DIRECTION
 *
 *   Description:
 *      This parameter identifies the orientation of a parametric
 *      workpiece.
 *      It also identifies the orientation of the workpiece at the target
 *      workspace if the workpiece is retrieved from a different workspace.
 *      This is the direction of the workpiece from the location
 *      point along the centerline away from or towards headstock.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Turn Workpiece Direction
 *  Variable Name: <prefix>_turn_workpiece_direction
 *
 *   Possible Values: UF_PARAM_turn_workpiece_direction_t
 *
 * 
 */
#define UF_PARAM_TURN_WORKPIECE_DIRECTION   3421 


/* UF_PARAM_TURN_WORKPIECE_SRC_LOC_TAG
 *
 *   Description:
 *      This parameter identifies the source location of the workpiece
 *      from different workspace as a smart point.
 *
 *   Type: UF_PARAM_type_tag
 *
 *   Name: Turn Workpiece Source Location Point
 *  Variable Name: <prefix>_turn_workpiece_source_location_point
 *
 *   Possible Values:
 *         0 (no entity)
 *         entity value
 *
 * 
 */
#define UF_PARAM_TURN_WORKPIECE_SRC_LOC_TAG   3422  /* tag */


/* UF_PARAM_TURN_WORKPIECE_AUTO_POS
 *
 *   Description:
 *      This parameter activates the automatic positioning of
 *      the workpiece relative to the part.
 *
 *   Type: UF_PARAM_type_logical
 *
 *   Name: Turn Workpiece Source Location Point
 *  Variable Name: <prefix>_turn_workpiece_source_location_point
 *
 *   Possible Values:
 *         true  -- IPW relative to solid part geometry
 *         false -- IPW positioned by points and direction
 *
 * 
 */
#define UF_PARAM_TURN_WORKPIECE_AUTO_POS   3423 


/* UF_PARAM_TURN_FEED_SHORT_SEGS_ROUND
 *
 *  Description: 
 *      Specifies the feed rate for round segments 
 *      detected in convex corners.
 *      If the value is 0, the feed rate is inactive
 *      and a fallback feed rate (e.g. Cut feed rate)
 *      is used for such rounds.
 *
 *  Type: UF_PARAM_type_double_length
 *
 *  Name: Short Segments Round Feed
 *  Variable Name: <prefix>_short_segments_round_feed
 *
 *  Possible Values: Positive double or zero
 *      (the value 0 deactivates the feed rate)
 *
 * 
 */
#define UF_PARAM_TURN_FEED_SHORT_SEGS_ROUND   3430 


/* UF_PARAM_TURN_FEED_SHORT_SEGS_ROUND_UNIT
 *
 *  Description:
 *      Specifies the unit of the round feed rate,
 *      cf. UF_PARAM_TURN_FEED_SHORT_SEGS_ROUND.
 *
 *  Type: UF_PARAM_type_int
 *
 *  Name: Short Segments Round Feed Unit
 *  Variable Name: <prefix>_short_segments_round_feed_unit
 *
 *  Possible Values: 0 -- None
 *                   1 -- mmpm/ipm (mm/inch per minute)
 *                   2 -- mmpr/ipr (mm/inch per revolution)
 *
 * 
 */
#define UF_PARAM_TURN_FEED_SHORT_SEGS_ROUND_UNIT   3431 


/* UF_PARAM_TURN_FEED_SPECIFY_MAXIMUM_ROUND
 *
 *  Description:
 *      Activates the maximum round length threshold parameter
 *      (cf. UF_PARAM_TURN_FEED_SHORT_SEGS_ROUND_LENGTH).
 *
 *  Type: UF_PARAM_type_int
 *
 *  Name: Short Segments Specify Maximum Round Length
 *  Variable Name: <prefix>_short_segments_specify_maximum_round_length
 *
 *  Possible Values: 0 -- Maximum Round Length inactive
 *                   1 -- Maximum Round Length active
 *
 * 
 */
#define UF_PARAM_TURN_FEED_SPECIFY_MAXIMUM_ROUND   3432 


/* UF_PARAM_TURN_FEED_SHORT_SEGS_ROUND_LENGTH
 *
 *  Description:
 *      Specifies the maximum length for cutting motions along 
 *      rounds that are intended to be made at Round feed rate.
 *      This parameter is taken into account depending
 *      on UF_PARAM_TURN_FEED_SPECIFY_MAXIMUM_ROUND.
 *      The maximum length relates to the distance
 *      that the tool travels along the round segment.
 *      If that distance exceeds the maximum length,
 *      the motion is assigned a fallback feed rate
 *      (e.g. Cut feed rate).
 *
 *  Type: UF_PARAM_type_double_length
 *
 *  Name: Short Segments Round Maximum Length
 *  Variable Name: <prefix>_short_segments_round_maximum_length
 *
 *  Possible Values:  Positive double or zero
 *
 * 
 */
#define UF_PARAM_TURN_FEED_SHORT_SEGS_ROUND_LENGTH   3433 


/* UF_PARAM_TURN_FEED_SHORT_SEGS_CHAMFER
 *
 *  Description:
 *      Specifies the feed rate for chamfer segments 
 *      detected in convex corners.
 *      If the value is 0, the feed rate is inactive
 *      and a fallback feed rate (e.g. Cut feed rate)
 *      is used for such chamfers.
 *
 *  Type: UF_PARAM_type_double_length
 *
 *  Name: Short Segments Chamfer Feed
 *  Variable Name: <prefix>_short_segments_chamfer_feed
 *
 *  Possible Values: Positive double or zero
 *      (the value 0 deactivates the feed rate)
 *
 * 
 */
#define UF_PARAM_TURN_FEED_SHORT_SEGS_CHAMFER   3434 


/* UF_PARAM_TURN_FEED_SHORT_SEGS_CHAMFER_UNIT
 *
 *  Description:
 *      Specifies the unit of the chamfer feed rate,
 *      cf. UF_PARAM_TURN_FEED_SHORT_SEGS_CHAMFER.
 *
 *  Type: UF_PARAM_type_int
 *
 *  Name: Short Segments Chamfer Feed Unit
 *  Variable Name: <prefix>_short_segments_chamfer_feed_unit
 *
 *  Possible Values: 0 -- None
 *                   1 -- mmpm/ipm (mm/inch per minute)
 *                   2 -- mmpr/ipr (mm/inch per revolution)
 *
 * 
 */
#define UF_PARAM_TURN_FEED_SHORT_SEGS_CHAMFER_UNIT   3435 


/* UF_PARAM_TURN_FEED_SPECIFY_MAXIMUM_CHAMFER
 *
 *  Description:
 *      Activates the maximum round length threshold parameter
 *      (cf. UF_PARAM_TURN_FEED_SHORT_SEGS_CHAMFER_LENGTH).
 *
 *  Type: UF_PARAM_type_int
 *
 *  Name: Short Segments Specify Maximum Chamfer Length
 *  Variable Name: <prefix>_short_segments_specify_maximum_chamfer_length
 *
 *  Possible Values: 0 -- Maximum Chamfer Length inactive
 *                   1 -- Maximum Chamfer Length active
 *
 * 
 */
#define UF_PARAM_TURN_FEED_SPECIFY_MAXIMUM_CHAMFER   3436 


/* UF_PARAM_TURN_FEED_SHORT_SEGS_CHAMFER_LENGTH
 *
 *  Description:
 *      Specifies the maximum length for cutting motions along 
 *      chamfers that are intended to be made at Chamfer feed rate.
 *      This parameter is taken into account depending
 *      on UF_PARAM_TURN_FEED_SPECIFY_MAXIMUM_CHAMFER.
 *      The maximum length relates to the distance
 *      that the tool travels along the chamfer segment.
 *      If that distance exceeds the maximum length,
 *      the motion is assigned a fallback feed rate
 *      (e.g. Cut feed rate).
 *
 *  Type: UF_PARAM_type_double_length
 *
 *  Name: Short Segments Chamfer Maximum Length
 *  Variable Name: <prefix>_short_segments_chamfer_maximum_length
 *
 *  Possible Values: Positive double or zero
 *
 * 
 */
#define UF_PARAM_TURN_FEED_SHORT_SEGS_CHAMFER_LENGTH   3437 


/* UF_PARAM_TURN_FEED_CLEANUP_ACCEL
 *
 *  Description:
 *      Specifies the accelerate feed rate for Profiling, 
 *      Finishing and Cleanup cuts, which is assumed when
 *      the cutting motion leaves a concave corner.
 *      The length of the acceleration distance is specified
 *      by UF_PARAM_TURN_FEED_CLEANUP_ACCEL_LENGTH.
 *
 *  Type: UF_PARAM_type_double_length
 *
 *  Name: Cleanup and Profile Accelerate
 *  Variable Name: <prefix>_cleanup_and_profile_accelerate
 *
 *  Possible Values: Positive double or zero
 *      (the value 0 deactivates the feed rate)
 *
 * 
 */
#define UF_PARAM_TURN_FEED_CLEANUP_ACCEL   3438 


/* UF_PARAM_TURN_FEED_CLEANUP_ACCEL_UNIT
 *
 *  Description:
 *      Specifies the unit of the accelerate feed rate,
 *      cf. UF_PARAM_TURN_FEED_CLEANUP_ACCEL.
 *
 *  Type: UF_PARAM_type_int
 *
 *  Name: Cleanup and Profile Accelerate Unit
 *  Variable Name: <prefix>_cleanup_and_profile_accelerate_unit
 *
 *  Possible Values: 0 -- None
 *                   1 -- mmpm/ipm (mm/inch per minute)
 *                   2 -- mmpr/ipr (mm/inch per revolution)
 *
 * 
 */
#define UF_PARAM_TURN_FEED_CLEANUP_ACCEL_UNIT   3439 


/* UF_PARAM_TURN_FEED_CLEANUP_ACCEL_LENGTH
 *
 *  Description:
 *      Specifies the length of the acceleration phase
 *      to which the accelerate feed rate is applied.
 *      (cf. UF_PARAM_TURN_FEED_CLEANUP_ACCEL).
 *
 *  Type: UF_PARAM_type_double_length
 *
 *  Name: Cleanup and Profile Accelerate Length
 *  Variable Name: <prefix>_cleanup_and_profile_accelerate_length
 *
 *  Possible Values: Positive double or zero
 *
 * 
 */
#define UF_PARAM_TURN_FEED_CLEANUP_ACCEL_LENGTH   3440 


/* UF_PARAM_TURN_FEED_CLEANUP_DECEL
 *
 *  Description:
 *      Specifies the decelerate feed rate for Profiling, 
 *      Finishing and Cleanup cuts, which is assumed when
 *      the cutting motion approaches a concave corner.
 *      The length of the deceleration distance is specified
 *      by UF_PARAM_TURN_FEED_CLEANUP_DECEL_LENGTH.
 *
 *  Type: UF_PARAM_type_double_length
 *
 *  Name: Cleanup and Profile Decelerate
 *  Variable Name: <prefix>_cleanup_and_profile_decelerate
 *
 *  Possible Values: Positive double or zero
 *      (the value 0 deactivates the feed rate)
 *
 * 
 */
#define UF_PARAM_TURN_FEED_CLEANUP_DECEL   3441 


/* UF_PARAM_TURN_FEED_CLEANUP_DECEL_UNIT
 *
 *  Description:
 *      Specifies the unit of the decelerate feed rate,
 *      cf. UF_PARAM_TURN_FEED_CLEANUP_DECEL.
 *
 *  Type: UF_PARAM_type_int
 *
 *  Name: Cleanup and Profile Decelerate Unit
 *  Variable Name: <prefix>_cleanup_and_profile_decelerate_unit
 *
 *  Possible Values: 0 -- None
 *                   1 -- mmpm/ipm (mm/inch per minute)
 *                   2 -- mmpr/ipr (mm/inch per revolution)
 *
 * 
 */
#define UF_PARAM_TURN_FEED_CLEANUP_DECEL_UNIT   3442 


/* UF_PARAM_TURN_FEED_CLEANUP_DECEL_LENGTH
 *
 *  Description:
 *      Specifies the length of the deceleration phase
 *      to which the decelerate feed rate is applied.
 *      (cf. UF_PARAM_TURN_FEED_CLEANUP_DECEL).
 *
 *  Type: UF_PARAM_type_double_length
 *
 *  Name: Cleanup and Profile Decelerate Length
 *  Variable Name: <prefix>_cleanup_and_profile_decelerate_length
 *
 *  Possible Values: Positive double or zero
 *
 * 
 */
#define UF_PARAM_TURN_FEED_CLEANUP_DECEL_LENGTH   3443 


/* UF_PARAM_TURN_FEED_ALSO_APPLY_TO_START_AND_END_OF_PASS
 *
 *  Description:
 *      If this parameter holds the value 1 (on), an acceleration phase is
 *      performed at the beginning of Profile, Finish and Cleanup passes.
 *      Analogously, a deceleration is performed at the end of these
 *      passes.
 *      In case the pass is shorter than the sum of the lengths of
 *      the acceleration and deceleration phase, deceleration always
 *      takes precedence over acceleration.
 *      Accelerate and decelerate feed rates and lengths are specified
 *      by the following parameters:
 *         UF_PARAM_TURN_FEED_CLEANUP_ACCEL
 *         UF_PARAM_TURN_FEED_CLEANUP_ACCEL_LENGTH
 *         UF_PARAM_TURN_FEED_CLEANUP_DECEL
 *         UF_PARAM_TURN_FEED_CLEANUP_DECEL_LENGTH
 *      (cf. respective documentation)
 *
 *  Type: UF_PARAM_type_int
 *
 *  Name: Also Apply to Start and End of Pass
 *  Variable Name: <prefix>_also_apply_to_start_and_end_of_pass
 *
 *  Possible Values: 0 -- off
 *                   1 -- on
 *
 * 
 */
#define UF_PARAM_TURN_FEED_ALSO_APPLY_TO_START_AND_END_OF_PASS   3444 


/* UF_PARAM_TURN_ENG_PROFILING_VECTOR
 *
 *   Description:
 *      Defines the vector for profiling engage (2D).
 *
 *   Type: UF_PARAM_type_vla_length
 *
 *   Name: Engage Profiling Vector
 *  Variable Name: <prefix>_engage_profiling_vector
 *
 *   Possible Values: 2D vector
 *
 * 
 */
#define UF_PARAM_TURN_ENG_PROFILING_VECTOR   3500 


/* UF_PARAM_TURN_ENG_PROFILING_ANGLE
 *
 *   Description:
 *      Defines the angle for profiling engage.
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Engage Profiling Angle
 *  Variable Name: <prefix>_engage_profiling_angle
 *
 *   Possible Values: angle in degree
 *
 * 
 */
#define UF_PARAM_TURN_ENG_PROFILING_ANGLE   3501 


/* UF_PARAM_TURN_ENG_PROFILING_DISTANCE
 *
 *   Description:
 *      Defines the distance for profiling engage.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Engage Profiling Distance
 *  Variable Name: <prefix>_engage_profiling_distance
 *
 *   Possible Values: positive double
 *
 * 
 */
#define UF_PARAM_TURN_ENG_PROFILING_DISTANCE   3502 


/* UF_PARAM_TURN_ENG_PROFILING_RADIUS
 *
 *   Description:
 *      Defines the radius for profiling engage.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Engage Profiling Radius
 *  Variable Name: <prefix>_engage_profiling_radius
 *
 *   Possible Values: positive double
 *
 * 
 */
#define UF_PARAM_TURN_ENG_PROFILING_RADIUS   3503 


/* UF_PARAM_TURN_ENG_PROFILING_POINT
 *
 *   Description:
 *      Defines the identifier of the profiling engage smart point.
 *
 *   Type: UF_PARAM_type_tag
 *
 *   Name: Engage Profiling Point
 *  Variable Name: <prefix>_engage_profiling_point
 *
 *   Possible Values: 
 *
 * 
 */
#define UF_PARAM_TURN_ENG_PROFILING_POINT   3504 


/* UF_PARAM_TURN_ENG_TO_TRIMPOINT
 *
 *   Description:
 *      Controls direct engage to trim point.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Engage Profiling to Trim Point
 *  Variable Name: <prefix>_engage_profiling_to_trim_point
 *
 *   Possible Values: 
 *     0 = inactive
 *     1 = active
 *
 * 
 */
#define UF_PARAM_TURN_ENG_TO_TRIMPOINT   3505 


/* UF_PARAM_TURN_ENG_PROFILING_EXTEND
 *
 *   Description:
 *      Distance value for extension at start point 
 *      of Profiling/Finishing pass. 
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Engage Profiling Extend 
 *  Variable Name: <prefix>_engage_profiling_extend
 *
 *   Possible Values:
 *
 * 
 */
#define UF_PARAM_TURN_ENG_PROFILING_EXTEND   3506 


/* UF_PARAM_TURN_ENG_LEVEL_BLANK_VECTOR
 *
 *   Description:
 *      Defines the vector for level/blank engage (2D).
 *
 *   Type: UF_PARAM_type_vla_length
 *
 *   Name: Engage Level Blank Vector
 *  Variable Name: <prefix>_engage_level_blank_vector
 *
 *   Possible Values: 2D vector
 *
 * 
 */
#define UF_PARAM_TURN_ENG_LEVEL_BLANK_VECTOR   3510 


/* UF_PARAM_TURN_ENG_LEVEL_BLANK_ANGLE
 *
 *   Description:
 *      Defines the angle for level/blank engage.
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Engage Level Blank Angle
 *  Variable Name: <prefix>_engage_level_blank_angle
 *
 *   Possible Values: angle in degree
 *
 * 
 */
#define UF_PARAM_TURN_ENG_LEVEL_BLANK_ANGLE   3511 


/* UF_PARAM_TURN_ENG_LEVEL_BLANK_DISTANCE
 *
 *   Description:
 *      Defines the distance for level/blank engage.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Engage Level Blank Distance
 *  Variable Name: <prefix>_engage_level_blank_distance
 *
 *   Possible Values: 
 *
 * 
 */
#define UF_PARAM_TURN_ENG_LEVEL_BLANK_DISTANCE   3512 


/* UF_PARAM_TURN_ENG_LEVEL_BLANK_RADIUS
 *
 *   Description:
 *      Defines the radius for level/blank engage.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Engage Level Blank Radius
 *  Variable Name: <prefix>_engage_level_blank_radius
 *
 *   Possible Values: 
 *
 * 
 */
#define UF_PARAM_TURN_ENG_LEVEL_BLANK_RADIUS   3513 


/* UF_PARAM_TURN_ENG_LEVEL_BLANK_RADIUS_2
 *
 *   Description:
 *      Defines the second radius for level/blank engage using two circles.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Engage Level Blank Radius 2
 *  Variable Name: <prefix>_engage_level_blank_radius_2
 *
 *   Possible Values: 
 *
 * 
 */
#define UF_PARAM_TURN_ENG_LEVEL_BLANK_RADIUS_2   3514 


/* UF_PARAM_TURN_ENG_LEVEL_BLANK_POINT
 *
 *   Description:
 *      Identifies the smart point for level/blank engage.
 *
 *   Type: UF_PARAM_type_tag
 *
 *   Name: Engage Level Blank Point
 *  Variable Name: <prefix>_engage_level_blank_point
 *
 *   Possible Values: 
 *
 * 
 */
#define UF_PARAM_TURN_ENG_LEVEL_BLANK_POINT   3515 


/* UF_PARAM_TURN_ENG_LEVEL_BLANK_DISTANCE_IS_TANGENTIAL
 *
 *   Description:
 *      This flag indicates if the safe distance for a level/blank engage
 *      is to be applied tangentially.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Engage Level Blank Distance Is Tangential
 *  Variable Name: <prefix>_engage_level_blank_distance_is_tangential
 *
 *   Possible Values: 
 *        0 - Safe distance for level/blank engage is not tangential
 *        1 - Safe distance for level/blank engage is tangential
 *
 * 
 */
#define UF_PARAM_TURN_ENG_LEVEL_BLANK_DISTANCE_IS_TANGENTIAL   3516 


/* UF_PARAM_TURN_ENG_LEVEL_PART_VECTOR
 *
 *   Description:
 *      Defines the vector for level/part engage.
 *
 *   Type: UF_PARAM_type_vla_length
 *
 *   Name: Engage Level Part Vector
 *  Variable Name: <prefix>_engage_level_part_vector
 *
 *   Possible Values: 2D vector
 *
 * 
 */
#define UF_PARAM_TURN_ENG_LEVEL_PART_VECTOR   3520 


/* UF_PARAM_TURN_ENG_LEVEL_PART_ANGLE
 *
 *   Description:
 *      Defines the angle for level/part engage.
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Engage Level Part Angle
 *  Variable Name: <prefix>_engage_level_part_angle
 *
 *   Possible Values: angle in degree
 *
 * 
 */
#define UF_PARAM_TURN_ENG_LEVEL_PART_ANGLE   3521 


/* UF_PARAM_TURN_ENG_LEVEL_PART_DISTANCE
 *
 *   Description:
 *      Defines the distance for level/part engage.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Engage Level Part Distance
 *  Variable Name: <prefix>_engage_level_part_distance
 *
 *   Possible Values: 
 *
 * 
 */
#define UF_PARAM_TURN_ENG_LEVEL_PART_DISTANCE   3522 


/* UF_PARAM_TURN_ENG_LEVEL_PART_RADIUS
 *
 *   Description:
 *      Defines the radius for level/part engage.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Engage Level Part Radius
 *  Variable Name: <prefix>_engage_level_part_radius
 *
 *   Possible Values: 
 *
 * 
 */
#define UF_PARAM_TURN_ENG_LEVEL_PART_RADIUS   3523 


/* UF_PARAM_TURN_ENG_LEVEL_PART_POINT
 *
 *   Description:
 *      Identifies the smart point for level/part engage.
 *
 *   Type: UF_PARAM_type_tag
 *
 *   Name: Engage Level Part Point
 *  Variable Name: <prefix>_engage_level_part_point
 *
 *   Possible Values: 
 *
 * 
 */
#define UF_PARAM_TURN_ENG_LEVEL_PART_POINT   3524 


/* UF_PARAM_TURN_ENG_LEVEL_SAFE_VECTOR
 *
 *   Description:
 *      Defines the vector for level/safe engage (2D).
 *
 *   Type: UF_PARAM_type_vla_length
 *
 *   Name: Engage Level Safe Vector
 *  Variable Name: <prefix>_engage_level_safe_vector
 *
 *   Possible Values: 2D vector
 *
 * 
 */
#define UF_PARAM_TURN_ENG_LEVEL_SAFE_VECTOR   3530 


/* UF_PARAM_TURN_ENG_LEVEL_SAFE_ANGLE
 *
 *   Description:
 *      Defines the angle for level/safe engage.
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Engage Level Safe Angle
 *  Variable Name: <prefix>_engage_level_safe_angle
 *
 *   Possible Values: angle in degree
 *
 * 
 */
#define UF_PARAM_TURN_ENG_LEVEL_SAFE_ANGLE   3531 


/* UF_PARAM_TURN_ENG_LEVEL_SAFE_DISTANCE
 *
 *   Description:
 *      Defines the distance for level/safe engage.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Engage Level Safe Distance
 *  Variable Name: <prefix>_engage_level_safe_distance
 *
 *   Possible Values: 
 *
 * 
 */
#define UF_PARAM_TURN_ENG_LEVEL_SAFE_DISTANCE   3532 


/* UF_PARAM_TURN_ENG_LEVEL_SAFE_RADIUS
 *
 *   Description:
 *      Defines the radius for level/safe engage.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Engage Level Safe Radius
 *  Variable Name: <prefix>_engage_level_safe_radius
 *
 *   Possible Values: 
 *
 * 
 */
#define UF_PARAM_TURN_ENG_LEVEL_SAFE_RADIUS   3533 


/* UF_PARAM_TURN_ENG_LEVEL_SAFE_POINT
 *
 *   Description:
 *      Identifies the smart point for level/safe engage.
 *
 *   Type: UF_PARAM_type_tag
 *
 *   Name: Engage Level Safe Point
 *  Variable Name: <prefix>_engage_level_safe_point
 *
 *   Possible Values: 
 *
 * 
 */
#define UF_PARAM_TURN_ENG_LEVEL_SAFE_POINT   3534 


/* UF_PARAM_TURN_ENG_LEVEL_SAFE_EXTEND
 *
 *   Description:
 *      Distance value for level safe engage.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Engage Level Safe Extend
 *  Variable Name: <prefix>_engage_level_safe_extend
 *
 *   Possible Values: double
 *
 * 
 */
#define UF_PARAM_TURN_ENG_LEVEL_SAFE_EXTEND   3535 


/* UF_PARAM_TURN_ENG_LEVEL_SAFE_DISTANCE_IS_TANGENTIAL
 *
 *   Description:
 *      This flag indicates if the extend distance for a level/safe engage
 *      is to be applied tangentially.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Engage Level Safe Distance Is Tangential
 *  Variable Name: <prefix>_engage_level_safe_distance_is_tangential
 *
 *   Possible Values: 
 *        0 - Extend distance for level/safe engage is not tangential
 *        1 - Extend distance for level/safe engage is tangential
 *
 * 
 */
#define UF_PARAM_TURN_ENG_LEVEL_SAFE_DISTANCE_IS_TANGENTIAL   3536 


/* UF_PARAM_TURN_ENG_PLUNGE_VECTOR
 *
 *   Description:
 *      Defines the vector for plunge engage (2D).
 *
 *   Type: UF_PARAM_type_vla_length
 *
 *   Name: Engage Plunge Vector
 *  Variable Name: <prefix>_engage_plunge_vector
 *
 *   Possible Values: 2D vector
 *
 * 
 */
#define UF_PARAM_TURN_ENG_PLUNGE_VECTOR   3540 


/* UF_PARAM_TURN_ENG_PLUNGE_ANGLE
 *
 *   Description:
 *      Defines the angle for plunge engage.
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Engage Plunge Angle
 *  Variable Name: <prefix>_engage_plunge_angle
 *
 *   Possible Values: angle in degree
 *
 * 
 */
#define UF_PARAM_TURN_ENG_PLUNGE_ANGLE   3541 


/* UF_PARAM_TURN_ENG_PLUNGE_DISTANCE
 *
 *   Description:
 *      Defines the distance for plunge engage
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Engage Plunge Distance
 *  Variable Name: <prefix>_engage_plunge_distance
 *
 *   Possible Values: 
 *
 * 
 */
#define UF_PARAM_TURN_ENG_PLUNGE_DISTANCE   3542 


/* UF_PARAM_TURN_ENG_PLUNGE_POINT
 *
 *   Description:
 *      Identifies the smart point for plunge engage
 *
 *   Type: UF_PARAM_type_tag
 *
 *   Name: Engage Plunge Point
 *  Variable Name: <prefix>_engage_plunge_point
 *
 *   Possible Values: 
 *
 * 
 */
#define UF_PARAM_TURN_ENG_PLUNGE_POINT   3543 


/* UF_PARAM_TURN_ENG_1PLUNGE_VECTOR
 *
 *   Description:
 *      Defines the vector for first plunge engage (2D).
 *
 *   Type: UF_PARAM_type_vla_length
 *
 *   Name: Engage 1 Plunge Vector
 *  Variable Name: <prefix>_engage_1_plunge_vector
 *
 *   Possible Values: 2D vector
 *
 * 
 */
#define UF_PARAM_TURN_ENG_1PLUNGE_VECTOR   3550 


/* UF_PARAM_TURN_ENG_1PLUNGE_ANGLE
 *
 *   Description:
 *      Defines the angle for first plunge engage.
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Engage 1 Plunge Angle
 *  Variable Name: <prefix>_engage_1_plunge_angle
 *
 *   Possible Values: angle in degree
 *
 * 
 */
#define UF_PARAM_TURN_ENG_1PLUNGE_ANGLE   3551 


/* UF_PARAM_TURN_ENG_1PLUNGE_DISTANCE
 *
 *   Description:
 *      Defines the distance for first plunge engage.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Engage 1 Plunge Distance
 *  Variable Name: <prefix>_engage_1_plunge_distance
 *
 *   Possible Values: 
 *
 * 
 */
#define UF_PARAM_TURN_ENG_1PLUNGE_DISTANCE   3552 


/* UF_PARAM_TURN_ENG_1PLUNGE_POINT
 *
 *   Description:
 *      Identifies the smart point for first plunge engage.
 *
 *   Type: UF_PARAM_type_tag
 *
 *   Name: Engage 1 Plunge Point
 *  Variable Name: <prefix>_engage_1_plunge_point
 *
 *   Possible Values: 
 *
 * 
 */
#define UF_PARAM_TURN_ENG_1PLUNGE_POINT   3553 


/* UF_PARAM_TURN_RET_PROFILING_VECTOR
 *
 *   Description:
 *      Defines the vector for profiling retract (2D).
 *
 *   Type: UF_PARAM_type_vla_length
 *
 *   Name: Retract Profiling Vector
 *  Variable Name: <prefix>_retract_profiling_vector
 *
 *   Possible Values: 2D vector
 *
 * 
 */
#define UF_PARAM_TURN_RET_PROFILING_VECTOR   3600 


/* UF_PARAM_TURN_RET_PROFILING_ANGLE
 *
 *   Description:
 *      Defines the angle for profiling retract.
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Retract Profiling Angle
 *  Variable Name: <prefix>_retract_profiling_angle
 *
 *   Possible Values: angle in degree
 *
 * 
 */
#define UF_PARAM_TURN_RET_PROFILING_ANGLE   3601 


/* UF_PARAM_TURN_RET_PROFILING_DISTANCE
 *
 *   Description:
 *      Defines the distance for profiling retract.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Retract Profiling Distance
 *  Variable Name: <prefix>_retract_profiling_distance
 *
 *   Possible Values: 
 *
 * 
 */
#define UF_PARAM_TURN_RET_PROFILING_DISTANCE   3602 


/* UF_PARAM_TURN_RET_PROFILING_RADIUS
 *
 *   Description:
 *      Defines the radius for profiling retract.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Retract Profiling Radius
 *  Variable Name: <prefix>_retract_profiling_radius
 *
 *   Possible Values: 
 *
 * 
 */
#define UF_PARAM_TURN_RET_PROFILING_RADIUS   3603 


/* UF_PARAM_TURN_RET_PROFILING_POINT
 *
 *   Description:
 *      Identifies the smart point for profiling retract.
 *
 *   Type: UF_PARAM_type_tag
 *
 *   Name: Retract Profiling Point
 *  Variable Name: <prefix>_retract_profiling_point
 *
 *   Possible Values: 
 *
 * 
 */
#define UF_PARAM_TURN_RET_PROFILING_POINT   3604 


/* UF_PARAM_TURN_RET_FROM_TRIMPOINT
 *
 *   Description:
 *      Controls direct retract from trim point.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Retract Profiling from Trim Point
 *  Variable Name: <prefix>_retract_profiling_from_trim_point
 *
 *   Possible Values: 
 *     0 = inactive
 *     1 = active
 *
 * 
 */
#define UF_PARAM_TURN_RET_FROM_TRIMPOINT   3605 


/* UF_PARAM_TURN_RET_PROFILING_EXTEND
 *
 *   Description:
 *      Distance value for extension at end point 
 *      of Profiling/Finishing pass. 
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Retract Profiling Extend 
 *  Variable Name: <prefix>_retract_profiling_extend
 *
 *   Possible Values:
 *
 * 
 */
#define UF_PARAM_TURN_RET_PROFILING_EXTEND   3606 


/* UF_PARAM_TURN_RET_LEVEL_BLANK_VECTOR
 *
 *   Description:
 *      Defines the vector for level/blank retract (2D).
 *
 *   Type: UF_PARAM_type_vla_length
 *
 *   Name: Retract Level Blank Vector
 *  Variable Name: <prefix>_retract_level_blank_vector
 *
 *   Possible Values: 2D vector
 *
 * 
 */
#define UF_PARAM_TURN_RET_LEVEL_BLANK_VECTOR   3610 


/* UF_PARAM_TURN_RET_LEVEL_BLANK_ANGLE
 *
 *   Description:
 *      Defines the angle for level/blank retract.
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Retract Level Blank Angle
 *  Variable Name: <prefix>_retract_level_blank_angle
 *
 *   Possible Values: angle in degree
 *
 * 
 */
#define UF_PARAM_TURN_RET_LEVEL_BLANK_ANGLE   3611 


/* UF_PARAM_TURN_RET_LEVEL_BLANK_DISTANCE
 *
 *   Description:
 *      Defines the distance for level/blank retract.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Retract Level Blank Distance
 *  Variable Name: <prefix>_retract_level_blank_distance
 *
 *   Possible Values: 
 *
 * 
 */
#define UF_PARAM_TURN_RET_LEVEL_BLANK_DISTANCE   3612 


/* UF_PARAM_TURN_RET_LEVEL_BLANK_RADIUS
 *
 *   Description:
 *      Defines the radius for level/blank retract.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Retract Level Blank Radius
 *  Variable Name: <prefix>_retract_level_blank_radius
 *
 *   Possible Values: 
 *
 * 
 */
#define UF_PARAM_TURN_RET_LEVEL_BLANK_RADIUS   3613 


/* UF_PARAM_TURN_RET_LEVEL_BLANK_POINT
 *
 *   Description:
 *      Identifies the smart point for level/blank retract.
 *
 *   Type: UF_PARAM_type_tag
 *
 *   Name: Retract Level Blank Point
 *  Variable Name: <prefix>_retract_level_blank_point
 *
 *   Possible Values: 
 *
 * 
 */
#define UF_PARAM_TURN_RET_LEVEL_BLANK_POINT   3614 


/* UF_PARAM_TURN_RET_LEVEL_BLANK_EXTEND
 *
 *   Description:
 *      Distance value for extension at end point 
 *      of rough cut which ends at blank shape.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Retract Level Blank Extend
 *  Variable Name: <prefix>_retract_level_blank_extend
 *
 *   Possible Values:
 *
 * 
 */
#define UF_PARAM_TURN_RET_LEVEL_BLANK_EXTEND   3615 


/* UF_PARAM_TURN_RET_LEVEL_PART_VECTOR
 *
 *   Description:
 *      Defines the vector for level/part retract (2D).
 *
 *   Type: UF_PARAM_type_vla_length
 *
 *   Name: Retract Level Part Vector
 *  Variable Name: <prefix>_retract_level_part_vector
 *
 *   Possible Values: 2D vector
 *
 * 
 */
#define UF_PARAM_TURN_RET_LEVEL_PART_VECTOR   3620 


/* UF_PARAM_TURN_RET_LEVEL_PART_ANGLE
 *
 *   Description:
 *      Defines the angle for level/part retract.
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Retract Level Part Angle
 *  Variable Name: <prefix>_retract_level_part_angle
 *
 *   Possible Values: angle in degree
 *
 * 
 */
#define UF_PARAM_TURN_RET_LEVEL_PART_ANGLE   3621 


/* UF_PARAM_TURN_RET_LEVEL_PART_DISTANCE
 *
 *   Description:
 *      Defines the distance for level/part retract.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Retract Level Part Distance
 *  Variable Name: <prefix>_retract_level_part_distance
 *
 *   Possible Values: 
 *
 * 
 */
#define UF_PARAM_TURN_RET_LEVEL_PART_DISTANCE   3622 


/* UF_PARAM_TURN_RET_LEVEL_PART_RADIUS
 *
 *   Description:
 *      Defines the radius for level part retract.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Retract Level Part Radius
 *  Variable Name: <prefix>_retract_level_part_radius
 *
 *   Possible Values: 
 *
 * 
 */
#define UF_PARAM_TURN_RET_LEVEL_PART_RADIUS   3623 


/* UF_PARAM_TURN_RET_LEVEL_PART_POINT
 *
 *   Description:
 *      Identifies the smart point for level/part retract.
 *
 *   Type: UF_PARAM_type_tag
 *
 *   Name: Retract Level Part Point
 *  Variable Name: <prefix>_retract_level_part_point
 *
 *   Possible Values: 
 *
 * 
 */
#define UF_PARAM_TURN_RET_LEVEL_PART_POINT   3624 


/* UF_PARAM_TURN_RET_PLUNGE_VECTOR
 *
 *   Description:
 *      Defines the vector for plunge retract (2D).
 *
 *   Type: UF_PARAM_type_vla_length
 *
 *   Name: Retract Plunge Vector
 *  Variable Name: <prefix>_retract_plunge_vector
 *
 *   Possible Values: 2D vector
 *
 * 
 */
#define UF_PARAM_TURN_RET_PLUNGE_VECTOR   3630 


/* UF_PARAM_TURN_RET_PLUNGE_ANGLE
 *
 *   Description:
 *      Defines the angle for plunge retract.
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Retract Plunge Angle
 *  Variable Name: <prefix>_retract_plunge_angle
 *
 *   Possible Values: angle in degree
 *
 * 
 */
#define UF_PARAM_TURN_RET_PLUNGE_ANGLE   3631 


/* UF_PARAM_TURN_RET_PLUNGE_DISTANCE
 *
 *   Description:
 *      Defines the distance for plunge retract.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Retract Plunge Distance
 *  Variable Name: <prefix>_retract_plunge_distance
 *
 *   Possible Values: 
 *
 * 
 */
#define UF_PARAM_TURN_RET_PLUNGE_DISTANCE   3632 


/* UF_PARAM_TURN_RET_1PLUNGE_VECTOR
 *
 *   Description:
 *      Defines the vector for first plunge retract (2D).
 *
 *   Type: UF_PARAM_type_vla_length
 *
 *   Name: Retract 1 Plunge Vector
 *  Variable Name: <prefix>_retract_1_plunge_vector
 *
 *   Possible Values: 2D vector
 *
 * 
 */
#define UF_PARAM_TURN_RET_1PLUNGE_VECTOR   3640 


/* UF_PARAM_TURN_RET_1PLUNGE_ANGLE
 *
 *   Description:
 *      Defines the angle for first plunge retract.
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Retract 1 Plunge Angle
 *  Variable Name: <prefix>_retract_1_plunge_angle
 *
 *   Possible Values: angle in degree
 *
 * 
 */
#define UF_PARAM_TURN_RET_1PLUNGE_ANGLE   3641 


/* UF_PARAM_TURN_RET_1PLUNGE_DISTANCE
 *
 *   Description:
 *      Defines the distance for first plunge retract.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Retract 1 Plunge Distance
 *  Variable Name: <prefix>_retract_1_plunge_distance
 *
 *   Possible Values: 
 *
 * 
 */
#define UF_PARAM_TURN_RET_1PLUNGE_DISTANCE   3642 


/* UF_PARAM_TURN_ENG_PROFILING_AUTOTOG
 *
 *   Description:
 *      Controls automatic parameterization for automatic profiling engage.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Engage Profiling Auto Mode
 *  Variable Name: <prefix>_engage_profiling_auto_mode
 *
 *   Possible Values: 
 *     0 = inactive
 *     1 = active
 *
 * 
 */
#define UF_PARAM_TURN_ENG_PROFILING_AUTOTOG   3680 


/* UF_PARAM_TURN_ENG_LEVEL_BLANK_AUTOTOG
 *
 *   Description:
 *      Controls automatic parameterization for automatic level/blank engage.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Engage Level Blank Auto Mode
 *  Variable Name: <prefix>_engage_level_blank_auto_mode
 *
 *   Possible Values: 
 *     0 = inactive
 *     1 = active
 *
 * 
 */
#define UF_PARAM_TURN_ENG_LEVEL_BLANK_AUTOTOG   3681 


/* UF_PARAM_TURN_ENG_LEVEL_PART_AUTOTOG
 *
 *   Description:
 *      Controls automatic parameterization for automatic level/part engage.
 *
 *      Bit 0 controls 'Use automatic values' toggle button:
 *            0: Off
 *            1: On
 *      Bit 1 controls 'Auto Angle' optionmenu:
 *            0: Constant Angle
 *            1: Autoadjusted Angle
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Engage Level Part Auto Mode
 *  Variable Name: <prefix>_engage_level_part_auto_mode
 *
 *   Possible Values: 
 *     0 = 'Use automatic values' is off; Constant Angle
 *     1 = 'Use automatic values' is on;  Constant Angle
 *     2 = 'Use automatic values' is off; Autoadjusted Angle
 *     3 = 'Use automatic values' is on;  Autoadjusted Angle
 *
 * 
 */
#define UF_PARAM_TURN_ENG_LEVEL_PART_AUTOTOG   3682 


/* UF_PARAM_TURN_ENG_LEVEL_SAFE_AUTOTOG
 *
 *   Description:
 *      Controls automatic parameterization for automatic level/safe engage.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Engage Level Safe Auto Mode
 *  Variable Name: <prefix>_engage_level_safe_auto_mode
 *
 *   Possible Values: 
 *     0 = inactive
 *     1 = active
 *
 * 
 */
#define UF_PARAM_TURN_ENG_LEVEL_SAFE_AUTOTOG   3683 


/* UF_PARAM_TURN_ENG_PLUNGE_AUTOTOG
 *
 *   Description:
 *      Controls automatic parameterization for automatic plunge engage.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Engage Plunge Auto Mode
 *  Variable Name: <prefix>_engage_plunge_auto_mode
 *
 *   Possible Values: 
 *     0 = inactive
 *     1 = active
 *
 * 
 */
#define UF_PARAM_TURN_ENG_PLUNGE_AUTOTOG   3684 


/* UF_PARAM_TURN_ENG_1PLUNGE_AUTOTOG
 *
 *   Description:
 *      Controls automatic parameterization for autmoatic first plunge engage.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Engage 1 Plunge Auto Mode
 *  Variable Name: <prefix>_engage_1_plunge_auto_mode
 *
 *   Possible Values: 
 *     0 = inactive
 *     1 = active
 *
 * 
 */
#define UF_PARAM_TURN_ENG_1PLUNGE_AUTOTOG   3685 


/* UF_PARAM_TURN_RET_PROFILING_AUTOTOG
 *
 *   Description:
 *      Controls automatic parameterization for automatic profiling retract.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Retract Profiling Auto Mode
 *  Variable Name: <prefix>_retract_profiling_auto_mode
 *
 *   Possible Values: 
 *     0 = inactive
 *     1 = active
 *
 * 
 */
#define UF_PARAM_TURN_RET_PROFILING_AUTOTOG   3686 


/* UF_PARAM_TURN_RET_LEVEL_BLANK_AUTOTOG
 *
 *   Description:
 *      Controls automatic parameterization for automatic level/blank retract.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Retract Level Blank Auto Mode
 *  Variable Name: <prefix>_retract_level_blank_auto_mode
 *
 *   Possible Values: 
 *     0 = inactive
 *     1 = active
 *
 * 
 */
#define UF_PARAM_TURN_RET_LEVEL_BLANK_AUTOTOG   3687 


/* UF_PARAM_TURN_RET_LEVEL_PART_AUTOTOG
 *
 *   Description:
 *      Controls automatic parameterization for automatic level/part retract.
 *
 *      Bit 0 controls 'Use automatic values' toggle button:
 *            0: Off
 *            1: On
 *      Bit 1 controls 'Auto Angle' optionmenu:
 *            0: Constant Angle
 *            1: Autoadjusted Angle
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Retract Level Part Auto Mode
 *  Variable Name: <prefix>_retract_level_part_auto_mode
 *
 *   Possible Values: 
 *     0 = 'Use automatic values' is off; Constant Angle
 *     1 = 'Use automatic values' is on;  Constant Angle
 *     2 = 'Use automatic values' is off; Autoadjusted Angle
 *     3 = 'Use automatic values' is on;  Autoadjusted Angle
 *
 * 
 */
#define UF_PARAM_TURN_RET_LEVEL_PART_AUTOTOG   3688 


/* UF_PARAM_TURN_RET_PLUNGE_AUTOTOG
 *
 *   Description:
 *      Controls automatic parameterization for automatic plunge retract.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Retract Plunge Auto Mode
 *  Variable Name: <prefix>_retract_plunge_auto_mode
 *
 *   Possible Values: 
 *     0 = inactive
 *     1 = active
 *
 * 
 */
#define UF_PARAM_TURN_RET_PLUNGE_AUTOTOG   3689 


/* UF_PARAM_TURN_RET_1PLUNGE_AUTOTOG
 *
 *   Description:
 *      Controls automatic parameterization for automatic first plunge retract.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Retract 1 Plunge Auto Mode
 *  Variable Name: <prefix>_retract_1_plunge_auto_mode
 *
 *   Possible Values: 
 *     0 = inactive
 *     1 = active
 *
 * 
 */
#define UF_PARAM_TURN_RET_1PLUNGE_AUTOTOG   3690 


/* UF_PARAM_TURN_FEED_RAMP_IN
 *
 *   Description:
 *      Value for 'Ramp In' feed rate.
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Feedrate Ramp In
 *  Variable Name: <prefix>_feedrate_ramp_in
 *
 *   Possible Values: Positive double or zero
 *
 * 
 */
#define UF_PARAM_TURN_FEED_RAMP_IN   3700 


/* UF_PARAM_TURN_FEED_RAMP_IN_UNIT
 *
 *   Description:
 *      Unit for 'Ramp In' feed rate.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Feedrate Ramp In Unit
 *  Variable Name: <prefix>_feedrate_ramp_in_unit
 *
 *   Possible Values: UF_PARAM_feed_unit_t
 *
 * 
 */
#define UF_PARAM_TURN_FEED_RAMP_IN_UNIT   3701 


/* UF_PARAM_TURN_FEED_RAMP_OUT
 *
 *   Description:
 *      Value for 'Ramp Out' feed rate.
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Feedrate Ramp Out
 *  Variable Name: <prefix>_feedrate_ramp_out
 *
 *   Possible Values: Positive double or zero
 *
 * 
 */
#define UF_PARAM_TURN_FEED_RAMP_OUT   3702 


/* UF_PARAM_TURN_FEED_RAMP_OUT_UNIT
 *
 *   Description:
 *      Unit for 'Ramp Out' feed rate.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Feedrate Ramp Out Unit
 *  Variable Name: <prefix>_feedrate_ramp_out_unit
 *
 *   Possible Values: UF_PARAM_feed_unit_t
 *
 * 
 */
#define UF_PARAM_TURN_FEED_RAMP_OUT_UNIT   3703 


/* UF_PARAM_TURN_FEED_RAMP_LEVEL
 *
 *   Description:
 *      Value for 'Ramp Level' feed rate.
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Feedrate Ramp Level
 *  Variable Name: <prefix>_feedrate_ramp_level
 *
 *   Possible Values: Positive double or zero
 *
 * 
 */
#define UF_PARAM_TURN_FEED_RAMP_LEVEL   3704 


/* UF_PARAM_TURN_FEED_RAMP_LEVEL_UNIT
 *
 *   Description:
 *      Unit for 'Ramp Level' feed rate.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Feedrate Ramp Level Unit
 *  Variable Name: <prefix>_feedrate_ramp_level_unit
 *
 *   Possible Values: UF_PARAM_feed_unit_t
 *
 * 
 */
#define UF_PARAM_TURN_FEED_RAMP_LEVEL_UNIT   3705 


/* UF_PARAM_TURN_FEED_PROFILE_CUT
 *
 *   Description:
 *      Value for 'Profile Cut' feed rate.
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Feedrate Profile Cut
 *  Variable Name: <prefix>_feedrate_profile_cut
 *
 *   Possible Values: Positive double or zero
 *
 * 
 */
#define UF_PARAM_TURN_FEED_PROFILE_CUT   3706 


/* UF_PARAM_TURN_FEED_PROFILE_CUT_UNIT
 *
 *   Description:
 *      Unit for 'Profile Cut' feed rate.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Feedrate Profile Cut Unit
 *  Variable Name: <prefix>_feedrate_profile_cut_unit
 *
 *   Possible Values: UF_PARAM_feed_unit_t
 *
 * 
 */
#define UF_PARAM_TURN_FEED_PROFILE_CUT_UNIT   3707 


/* UF_PARAM_TURN_FEED_CLEANUP_CUT
 *
 *   Description:
 *      Value for 'Cleanup Cut' feed rate.
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Feedrate Cleanup Cut
 *  Variable Name: <prefix>_feedrate_cleanup_cut
 *
 *   Possible Values: Positive double or zero
 *
 * 
 */
#define UF_PARAM_TURN_FEED_CLEANUP_CUT   3708 


/* UF_PARAM_TURN_FEED_CLEANUP_CUT_UNIT
 *
 *   Description:
 *      Unit for 'Cleanup Cut' feed rate.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Feedrate Cleanup Cut Unit
 *  Variable Name: <prefix>_feedrate_cleanup_cut_unit
 *
 *   Possible Values: UF_PARAM_feed_unit_t
 *
 * 
 */
#define UF_PARAM_TURN_FEED_CLEANUP_CUT_UNIT   3709 


/* UF_PARAM_TURN_FEED_CLEANUP_LINEAR
 *
 *   Description:
 *      Value for 'Cleanup Linear' feed rate.
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Feedrate Cleanup Linear
 *  Variable Name: <prefix>_feedrate_cleanup_linear
 *
 *   Possible Values: Positive double or zero
 *
 * 
 */
#define UF_PARAM_TURN_FEED_CLEANUP_LINEAR   3710 


/* UF_PARAM_TURN_FEED_CLEANUP_LINEAR_UNIT
 *
 *   Description:
 *      Unit for 'Cleanup Linear' feed rate.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Feedrate Cleanup Linear Unit
 *  Variable Name: <prefix>_feedrate_cleanup_linear_unit
 *
 *   Possible Values: UF_PARAM_feed_unit_t
 *
 * 
 */
#define UF_PARAM_TURN_FEED_CLEANUP_LINEAR_UNIT   3711 


/* UF_PARAM_TURN_FEED_CLEANUP_FACE
 *
 *   Description:
 *      Value for 'Cleanup Face' feed rate.
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Feedrate Cleanup Face
 *  Variable Name: <prefix>_feedrate_cleanup_face
 *
 *   Possible Values: Positive double or zero
 *
 * 
 */
#define UF_PARAM_TURN_FEED_CLEANUP_FACE   3712 


/* UF_PARAM_TURN_FEED_CLEANUP_FACE_UNIT
 *
 *   Description:
 *      Unit for 'Cleanup Face' feed rate.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Feedrate Cleanup Face Unit
 *  Variable Name: <prefix>_feedrate_cleanup_face_unit
 *
 *   Possible Values: UF_PARAM_feed_unit_t
 *
 * 
 */
#define UF_PARAM_TURN_FEED_CLEANUP_FACE_UNIT   3713 


/* UF_PARAM_TURN_FEED_CLEANUP_DIAMETER
 *
 *   Description:
 *      Value for 'Cleanup Diameter' feed rate.
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Feedrate Cleanup Diameter
 *  Variable Name: <prefix>_feedrate_cleanup_diameter
 *
 *   Possible Values: Positive double or zero
 *
 * 
 */
#define UF_PARAM_TURN_FEED_CLEANUP_DIAMETER   3714 


/* UF_PARAM_TURN_FEED_CLEANUP_DIAMETER_UNIT
 *
 *   Description:
 *      Unit for 'Cleanup Diameter' feed rate.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Feedrate Cleanup Diameter Unit
 *  Variable Name: <prefix>_feedrate_cleanup_diameter_unit
 *
 *   Possible Values: UF_PARAM_feed_unit_t
 *
 * 
 */
#define UF_PARAM_TURN_FEED_CLEANUP_DIAMETER_UNIT   3715 


/* UF_PARAM_TURN_FEED_CLEANUP_CIRC_CW
 *
 *   Description:
 *      Value for 'Cleanup Circle CW' feed rate.
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Feedrate Cleanup Circle CW
 *  Variable Name: <prefix>_feedrate_cleanup_circle_cw
 *
 *   Possible Values: Positive double or zero
 *
 * 
 */
#define UF_PARAM_TURN_FEED_CLEANUP_CIRC_CW   3716 


/* UF_PARAM_TURN_FEED_CLEANUP_CIRC_CW_UNIT
 *
 *   Description:
 *      Unit for 'Cleanup Circle CW' feed rate.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Feedrate Cleanup Circle CW Unit
 *  Variable Name: <prefix>_feedrate_cleanup_circle_cw_unit
 *
 *   Possible Values: UF_PARAM_feed_unit_t
 *
 * 
 */
#define UF_PARAM_TURN_FEED_CLEANUP_CIRC_CW_UNIT   3717 


/* UF_PARAM_TURN_FEED_CLEANUP_CIRC_CCW
 *
 *   Description:
 *      Value for 'Cleanup Circle CCW' feed rate.
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Feedrate Cleanup Circle CCW
 *  Variable Name: <prefix>_feedrate_cleanup_circle_ccw
 *
 *   Possible Values: Positive double or zero
 *
 * 
 */
#define UF_PARAM_TURN_FEED_CLEANUP_CIRC_CCW   3718 


/* UF_PARAM_TURN_FEED_CLEANUP_CIRC_CCW_UNIT
 *
 *   Description:
 *      Unit for 'Cleanup Circle CCW' feed rate.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Feedrate Cleanup Circle CCW Unit
 *  Variable Name: <prefix>_feedrate_cleanup_circle_ccw_unit
 *
 *   Possible Values: UF_PARAM_feed_unit_t
 *
 * 
 */
#define UF_PARAM_TURN_FEED_CLEANUP_CIRC_CCW_UNIT   3719 


/* UF_PARAM_TURN_FEED_FINISH_RAMP_IN
 *
 *   Description:
 *      Value for 'Finish Ramp In' feed rate.
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Feedrate Finish Ramp In
 *  Variable Name: <prefix>_feedrate_finish_ramp_in
 *
 *   Possible Values: Positive double or zero
 *
 * 
 */
#define UF_PARAM_TURN_FEED_FINISH_RAMP_IN   3720 


/* UF_PARAM_TURN_FEED_FINISH_RAMP_IN_UNIT
 *
 *   Description:
 *      Unit for 'Finish Ramp In' feed rate.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Feedrate Finish Ramp In Unit
 *  Variable Name: <prefix>_feedrate_finish_ramp_in_unit
 *
 *   Possible Values: UF_PARAM_feed_unit_t
 *
 * 
 */
#define UF_PARAM_TURN_FEED_FINISH_RAMP_IN_UNIT   3721 


/* UF_PARAM_TURN_FEED_FINISH_RAMP_OUT
 *
 *   Description:
 *      Value for 'Finish Ramp Out' feed rate.
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Feedrate Finish Ramp Out
 *  Variable Name: <prefix>_feedrate_finish_ramp_out
 *
 *   Possible Values: Positive double or zero
 *
 * 
 */
#define UF_PARAM_TURN_FEED_FINISH_RAMP_OUT   3722 


/* UF_PARAM_TURN_FEED_FINISH_RAMP_OUT_UNIT
 *
 *   Description:
 *      Unit for 'Finish Ramp Out' feed rate.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Feedrate Finish Ramp Out Unit
 *  Variable Name: <prefix>_feedrate_finish_ramp_out_unit
 *
 *   Possible Values: UF_PARAM_feed_unit_t
 *
 * 
 */
#define UF_PARAM_TURN_FEED_FINISH_RAMP_OUT_UNIT   3723 


/* UF_PARAM_TURN_FEED_FINISH_RAMP_LEVEL
 *
 *   Description:
 *      Value for 'Finish Ramp Level' feed rate.
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Feedrate Finish Ramp Level
 *  Variable Name: <prefix>_feedrate_finish_ramp_level
 *
 *   Possible Values: Positive double or zero
 *
 * 
 */
#define UF_PARAM_TURN_FEED_FINISH_RAMP_LEVEL   3724 


/* UF_PARAM_TURN_FEED_FINISH_RAMP_LEVEL_UNIT
 *
 *   Description:
 *      Unit for 'Finish Ramp Level' feed rate.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Feedrate Finish Ramp Level Unit
 *  Variable Name: <prefix>_feedrate_finish_ramp_level_unit
 *
 *   Possible Values: UF_PARAM_feed_unit_t
 *
 * 
 */
#define UF_PARAM_TURN_FEED_FINISH_RAMP_LEVEL_UNIT   3725 


/* UF_PARAM_TURN_FEED_FINISH_ACCEL
 *
 *   Description:
 *      Value for 'Finish Accelerate' feed rate.
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Feedrate Finish Accelerate
 *  Variable Name: <prefix>_feedrate_finish_accelerate
 *
 *   Possible Values:  Positive double
 *
 * 
 */
#define UF_PARAM_TURN_FEED_FINISH_ACCEL   3726 


/* UF_PARAM_TURN_FEED_FINISH_ACCEL_UNIT
 *
 *   Description:
 *      Unit for 'Finish Accelerate' feed rate.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Feedrate Finish Accelerate Unit
 *  Variable Name: <prefix>_feedrate_finish_accelerate_unit
 *
 *   Possible Values: UF_PARAM_feed_unit_t
 *
 * 
 */
#define UF_PARAM_TURN_FEED_FINISH_ACCEL_UNIT   3727 


/* UF_PARAM_TURN_FEED_FINISH_ACCEL_LENGTH
 *
 *   Description:
 *      Value for 'Finish Accelerate Length'.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Feedrate Finish Accelerate Length
 *  Variable Name: <prefix>_feedrate_finish_accelerate_length
 *
 *   Possible Values: Positive double
 *
 * 
 */
#define UF_PARAM_TURN_FEED_FINISH_ACCEL_LENGTH   3728 


/* UF_PARAM_TURN_FEED_FINISH_ACCEL_LENGTH_PERCENT
 *
 *   Description:
 *      Percentage value for 'Finish Accelerate Length'.
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Feedrate Finish Accelerate Length Percent
 *  Variable Name: <prefix>_feedrate_finish_accelerate_length_percent
 *
 *   Possible Values: Positive double
 *
 * 
 */
#define UF_PARAM_TURN_FEED_FINISH_ACCEL_LENGTH_PERCENT   3729 


/* UF_PARAM_TURN_FEED_FINISH_ACCEL_LENGTH_UNIT
 *
 *   Description:
 *      Unit for 'Finish Accelerate Length'.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Feedrate Finish Accelerate Length Unit
 *  Variable Name: <prefix>_feedrate_finish_accelerate_length_unit
 *
 *   Possible Values: UF_PARAM_turn_feed_accel_length_unit_t
 *
 * 
 */
#define UF_PARAM_TURN_FEED_FINISH_ACCEL_LENGTH_UNIT   3730 


/* UF_PARAM_TURN_FEED_FINISH_DECEL
 *
 *   Description:
 *      Value for 'Finish Decelerate' feed rate.
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Feedrate Finish Decelerate
 *  Variable Name: <prefix>_feedrate_finish_decelerate
 *
 *   Possible Values:  Positive double
 *
 * 
 */
#define UF_PARAM_TURN_FEED_FINISH_DECEL   3731 


/* UF_PARAM_TURN_FEED_FINISH_DECEL_UNIT
 *
 *   Description:
 *      Unit for 'Finish Decelerate' feed rate.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Feedrate Finish Decelerate Unit
 *  Variable Name: <prefix>_feedrate_finish_decelerate_unit
 *
 *   Possible Values: UF_PARAM_feed_unit_t
 *
 * 
 */
#define UF_PARAM_TURN_FEED_FINISH_DECEL_UNIT   3732 


/* UF_PARAM_TURN_FEED_FINISH_DECEL_LENGTH
 *
 *   Description:
 *      Value for 'Finish Decelerate Length'.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Feedrate Finish Decelerate Length
 *  Variable Name: <prefix>_feedrate_finish_decelerate_length
 *
 *   Possible Values: Positive double
 *
 * 
 */
#define UF_PARAM_TURN_FEED_FINISH_DECEL_LENGTH   3733 


/* UF_PARAM_TURN_FEED_FINISH_DECEL_LENGTH_PERCENT
 *
 *   Description:
 *      Percentage value for 'Finish Decelerate Length'.
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Feedrate Finish Decelerate Length Percent
 *  Variable Name: <prefix>_feedrate_finish_decelerate_length_percent
 *
 *   Possible Values: Positive double
 *
 * 
 */
#define UF_PARAM_TURN_FEED_FINISH_DECEL_LENGTH_PERCENT   3734 


/* UF_PARAM_TURN_FEED_FINISH_DECEL_LENGTH_UNIT
 *
 *   Description:
 *      Unit for 'Finish Decelerate Length'.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Feedrate Finish Decelerate Length Unit
 *  Variable Name: <prefix>_feedrate_finish_decelerate_length_unit
 *
 *   Possible Values: UF_PARAM_turn_feed_decel_length_unit_t
 *
 * 
 */
#define UF_PARAM_TURN_FEED_FINISH_DECEL_LENGTH_UNIT   3735 


/* UF_PARAM_TURN_FEED_ROUGH_LAST_CUT
 *
 *   Description:
 *      Value for 'Rough Last Cut' feed rate.
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Feedrate Rough Last Cut
 *  Variable Name: <prefix>_feedrate_rough_last_cut
 *
 *   Possible Values: Positive double
 *
 * 
 */
#define UF_PARAM_TURN_FEED_ROUGH_LAST_CUT   3736 


/* UF_PARAM_TURN_FEED_ROUGH_LAST_CUT_UNIT
 *
 *   Description:
 *      Unit for 'Rough Last Cut' feed rate.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Feedrate Rough Last Cut Unit
 *  Variable Name: <prefix>_feedrate_rough_last_cut_unit
 *
 *   Possible Values: UF_PARAM_feed_unit_t
 *
 * 
 */
#define UF_PARAM_TURN_FEED_ROUGH_LAST_CUT_UNIT   3737 


/* UF_PARAM_TURN_FEED_ROUGH_LAST_CUT_FOR_ENTIRE_PASS_TOG
 *
 *  Description:
 *     This parameter represents the toggle for applying the last cut
 *     feed rate to the entire last roughing pass of a Turn/Roughing operation.
 *
 *  Type: UF_PARAM_type_int
 *
 *  Name: Feedrate rough last cut for entire pass Toggle
 *  Variable Name: <prefix>_feedrate_rough_last_cut_for_entire_pass_toggle
 *
 *  Possible Values: 
 *        0 -- Inactive
 *        1 -- Active
 *
 * 
 */
#define UF_PARAM_TURN_FEED_ROUGH_LAST_CUT_FOR_ENTIRE_PASS_TOG   3738  /* UF_PARAM_type_int */


/* UF_PARAM_TURN_LOCAL_START_EVENTS_FLAG
 *
 *   Description:
 *      Holds the Start Events (MCEs) flag of Local Return.
 *      The Start Events Path is stored in parameter
 *      UF_PARAM_TURN_LOCAL_START_EVENTS.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Turn Local Start Events Flag
 *  Variable Name: <prefix>_turn_local_start_events_flag
 *
 *   Possible Values: 0 -- inactive
 *                    1 -- active
 *
 * 
 */
#define UF_PARAM_TURN_LOCAL_START_EVENTS_FLAG   3800 


/* UF_PARAM_TURN_LOCAL_START_EVENTS
 *
 *   Description:
 *      Holds the Start Events Path (MCEs) of Local Return.
 *      The Start Events Path is activated by parameter
 *      UF_PARAM_TURN_LOCAL_START_EVENTS_FLAG.
 *
 *   Type: UF_PARAM_type_tag
 *
 *   Name: Turn Local Start Events Path
 *  Variable Name: <prefix>_turn_local_start_events_path
 *
 *   Possible Values: tag
 *
 * 
 */
#define UF_PARAM_TURN_LOCAL_START_EVENTS   3801 


/* UF_PARAM_TURN_LOCAL_END_EVENTS_FLAG
 *
 *   Description:
 *      Holds the End Events (MCEs) flag of Local Return.
 *      The End Events Path is stored in parameter
 *      UF_PARAM_TURN_LOCAL_END_EVENTS.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Turn Local End Events Flag
 *  Variable Name: <prefix>_turn_local_end_events_flag
 *
 *   Possible Values: 0 -- inactive
 *                    1 -- active
 *
 * 
 */
#define UF_PARAM_TURN_LOCAL_END_EVENTS_FLAG   3802 


/* UF_PARAM_TURN_LOCAL_END_EVENTS
 *
 *   Description:
 *      Holds the End Events Path (MCEs) of Local Return.
 *      The End Events Path is activated by parameter
 *      UF_PARAM_TURN_LOCAL_END_EVENTS_FLAG.
 *
 *   Type: UF_PARAM_type_tag
 *
 *   Name: Turn Local End Events Path
 *  Variable Name: <prefix>_turn_local_end_events_path
 *
 *   Possible Values: tag
 *
 * 
 */
#define UF_PARAM_TURN_LOCAL_END_EVENTS   3803 


/* UF_PARAM_TURN_FINISH_LOCAL_START_EVENTS_FLAG
 *
 *   Description:
 *      Holds the Start Events (MCEs) flag of Finish Local Return.
 *      The Start Events Path is stored in parameter
 *      UF_PARAM_TURN_FINISH_LOCAL_START_EVENTS.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Turn Finish Local Start Events Flag
 *  Variable Name: <prefix>_turn_finish_local_start_events_flag
 *
 *   Possible Values: 0 -- inactive
 *                    1 -- active
 *
 * 
 */
#define UF_PARAM_TURN_FINISH_LOCAL_START_EVENTS_FLAG   3804 


/* UF_PARAM_TURN_FINISH_LOCAL_START_EVENTS
 *
 *   Description:
 *      Holds the Start Events Path (MCEs) of Finish Local Return.
 *      The Start Events Path is activated by parameter
 *      UF_PARAM_TURN_FINISH_LOCAL_START_EVENTS_FLAG.
 *
 *   Type: UF_PARAM_type_tag
 *
 *   Name: Turn Finish Local Start Events Path
 *  Variable Name: <prefix>_turn_finish_local_start_events_path
 *
 *   Possible Values: tag
 *
 * 
 */
#define UF_PARAM_TURN_FINISH_LOCAL_START_EVENTS   3805 


/* UF_PARAM_TURN_FINISH_LOCAL_END_EVENTS_FLAG
 *
 *   Description:
 *      Holds the End Events (MCEs) flag of Finish Local Return.
 *      The End Events Path is stored in parameter
 *      UF_PARAM_TURN_FINISH_LOCAL_END_EVENTS.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Turn Finish Local End Events Flag
 *  Variable Name: <prefix>_turn_finish_local_end_events_flag
 *
 *   Possible Values: 0 -- inactive
 *                    1 -- active
 *
 * 
 */
#define UF_PARAM_TURN_FINISH_LOCAL_END_EVENTS_FLAG   3806 


/* UF_PARAM_TURN_FINISH_LOCAL_END_EVENTS
 *
 *   Description:
 *      Holds the End Events Path (MCEs) of Finish Local Return.
 *      The End Events Path is activated by parameter
 *      UF_PARAM_TURN_FINISH_LOCAL_END_EVENTS_FLAG.
 *
 *   Type: UF_PARAM_type_tag
 *
 *   Name: Turn Finish Local End Events Path
 *  Variable Name: <prefix>_turn_finish_local_end_events_path
 *
 *   Possible Values: tag
 *
 * 
 */
#define UF_PARAM_TURN_FINISH_LOCAL_END_EVENTS   3807 


/* UF_PARAM_SURFACE_SPEED
 *
 *  Description:
 *  This parameter specifies the spindle surface speed
 *
 *  Type: UF_PARAM_type_double
 *
 *  Name: Surface Speed
 *  Variable Name: <prefix>_surface_speed
 *
 *  Possible Values: All
 *
 *  Developer:
 */
#define UF_PARAM_SURFACE_SPEED   4003  /* Param_type_double */


/* UF_PARAM_FEED_PER_TOOTH
 *
 *  Description:
 *  This parameter specifies the feed per tooth
 *
 *  Type: UF_PARAM_type_double
 *
 *  Name: Feed Per Tooth
 *  Variable Name: <prefix>_feed_per_tooth
 *
 *  Possible Values: All
 *
 *  Developer:
 */
#define UF_PARAM_FEED_PER_TOOTH   4004  /* Param_type_double */


/* UF_PARAM_SPINDLE_RPM
 *
 *  Description:
 *  This parameter specifies the spindle speed in RPM
 *
 *  Type: UF_PARAM_type_double
 *
 *  Name: Spindle RPM
 *  Variable Name: <prefix>_spindle_rpm
 *
 *  Possible Values: All
 *
 *  Developer:
 */
#define UF_PARAM_SPINDLE_RPM   4005  /* Param_type_double */


/* UF_PARAM_ENGAGE_FEED_PERCENT
 *
 *  Description:
 *  This parameter specifies the engage feed in percent
 *
 *  Type: UF_PARAM_type_double
 *
 *  Name: Engage Feed Percent
 *  Variable Name: <prefix>_engage_feed_percent
 *
 *  Possible Values: All
 *
 *  Developer:
 */
#define UF_PARAM_ENGAGE_FEED_PERCENT   4006  /* Param_type_double */


/* UF_PARAM_FIRST_CUT_FEED_PERCENT
 *
 *  Description:
 *  This parameter specifies the cut feed in percent
 *
 *  Type: UF_PARAM_type_double
 *
 *  Name: First Cut Feed Percent
 *  Variable Name: <prefix>_first_cut_feed_percent
 *
 *  Possible Values: All
 *
 *  Developer:
 */
#define UF_PARAM_FIRST_CUT_FEED_PERCENT   4007  /* Param_type_double */


/* UF_PARAM_SPINDLE_MODE
 *
 *  Description:
 *  This parameter specifies the Spindle Mode
 *
 *  Type: UF_PARAM_type_int
 *
 *  Name: Spindle Mode
 *  Variable Name: <prefix>_spindle_mode
 *
 *  Possible Values: All
 *
 *  Developer:
 */
#define UF_PARAM_SPINDLE_MODE   4008  /* UF_PARAM_type_int */


/* UF_PARAM_SPINDLE_RANGE_TEXT
 *
 *  Description:
 *  This parameter specifies the Spindle range Text.
 *
 *  Type: UF_PARAM_type_string
 *
 *  Name: Spindle Range
 *  Variable Name: <prefix>_spindle_range
 *
 *  Possible Values: All
 *
 *  Developer:
 */
#define UF_PARAM_SPINDLE_RANGE_TEXT   4009  /* UF_PARAM_type_string */


/* UF_PARAM_SPINDLE_TEXT
 *
 *  Description:
 *  This parameter specifies the Spindle Text. User can add
 *  any Major/Minor words apart from std spindle Major/Minor words
 *
 *  Type: UF_PARAM_type_string
 *
 *  Name: Spindle Text
 *  Variable Name: <prefix>_spindle_text
 *
 *  Possible Values: All
 *
 *  Developer:
 */
#define UF_PARAM_SPINDLE_TEXT   4010  /* UF_PARAM_type_string */


/* UF_PARAM_SPINDLE_PRESET_RPM
 *
 *  Description:
 *  This parameter specifies the Spindle preset RPM for 
 *  Lathe/Turn operations.
 *
 *  Type: UF_PARAM_type_double
 *
 *  Name: Spindle preset RPM
 *  Variable Name: <prefix>_spindle_preset_rpm
 *
 *  Possible Values: All
 *
 *  Developer:
 */
#define UF_PARAM_SPINDLE_PRESET_RPM   4011  /* UF_PARAM_type_double */


/* UF_PARAM_SPINDLE_MAX_RPM
 *
 *  Description:
 *  This parameter specifies the maximum Spindle RPM .
 *
 *  Type: UF_PARAM_type_double
 *
 *  Name: Spindle maximum RPM
 *  Variable Name: <prefix>_spindle_maximum_rpm
 *
 *  Possible Values: All
 *
 *  Developer:
 */
#define UF_PARAM_SPINDLE_MAX_RPM   4012  /* UF_PARAM_type_double */


/* UF_PARAM_SPINDLE_RPM_TOG
 *
 *  Description:
 *  This parameter specifies toggle for the spindle speed in RPM
 *
 *  Type: UF_PARAM_type_int
 *
 *  Name: Spindle RPM Toggle
 *  Variable Name: <prefix>_spindle_rpm_toggle
 *
 *  Possible Values: 
 *        0 -- Inactive
 *        1 -- Active
 *
 *  Developer:
 */
#define UF_PARAM_SPINDLE_RPM_TOG   4013  /* Param_type_double */


/* UF_PARAM_SPINDLE_PRESET_RPM_TOG
 *
 *  Description:
 *  This parameter specifies the toggle for Spindle preset RPM in 
 *  Lathe/Turn operations.
 *
 *  Type: UF_PARAM_type_int
 *
 *  Name: Spindle preset RPM Toggle
 *  Variable Name: <prefix>_spindle_preset_rpm_toggle
 *
 *  Possible Values: 
 *        0 -- Inactive
 *        1 -- Active
 *
 *  Developer:
 */
#define UF_PARAM_SPINDLE_PRESET_RPM_TOG   4014  /* UF_PARAM_type_int */


/* UF_PARAM_SPINDLE_MAX_RPM_TOG
 *
 *  Description:
 *  This parameter specifies the toggle for maximum Spindle RPM .
 *
 *  Type: UF_PARAM_type_int
 *
 *  Name: Spindle maximum RPM Toggle
 *  Variable Name: <prefix>_spindle_maximum_rpm_toggle
 *
 *  Possible Values:
 *        0 -- Inactive
 *        1 -- Active
 *
 *  Developer:
 */
#define UF_PARAM_SPINDLE_MAX_RPM_TOG   4015  /* UF_PARAM_type_double */


/* UF_PARAM_APPROACH_FEED_PERCENT
 *
 *  Description:
 *  This parameter specifies the approach feed in percent of cut feed
 *
 *  Type: UF_PARAM_type_double
 *
 *  Name: Approach Feed Percent
 *  Variable Name: <prefix>_approach_feed_percent
 *
 *  Possible Values: All
 *
 *  Developer:
 */
#define UF_PARAM_APPROACH_FEED_PERCENT   4016  /* Param_type_double */


/* UF_PARAM_STEPOVER_FEED_PERCENT
 *
 *  Description:
 *  This parameter specifies the stepover feed in percent of cut feed
 *
 *  Type: UF_PARAM_type_double
 *
 *  Name: Stepover Feed Percent
 *  Variable Name: <prefix>_stepover_feed_percent
 *
 *  Possible Values: All
 *
 *  Developer:
 */
#define UF_PARAM_STEPOVER_FEED_PERCENT   4017  /* Param_type_double */


/* UF_PARAM_RETRACT_FEED_PERCENT
 *
 *  Description:
 *  This parameter specifies the retract feed in percent of cut feed
 *
 *  Type: UF_PARAM_type_double
 *
 *  Name: Retract Feed Percent
 *  Variable Name: <prefix>_retract_feed_percent
 *
 *  Possible Values: All
 *
 *  Developer:
 */
#define UF_PARAM_RETRACT_FEED_PERCENT   4018  /* Param_type_double */


/* UF_PARAM_RETURN_FEED_PERCENT
 *
 *  Description:
 *  This parameter specifies the return feed in percent of cut feed
 *
 *  Type: UF_PARAM_type_double
 *
 *  Name: Return Feed Percent
 *  Variable Name: <prefix>_return_feed_percent
 *
 *  Possible Values: All
 *
 *  Developer:
 */
#define UF_PARAM_RETURN_FEED_PERCENT   4019  /* Param_type_double */


/* UF_PARAM_DEPART_FEED_PERCENT
 *
 *  Description:
 *  This parameter specifies the departure feed in percent of cut feed
 *
 *  Type: UF_PARAM_type_double
 *
 *  Name: Departure Feed Percent
 *  Variable Name: <prefix>_departure_feed_percent
 *
 *  Possible Values: All
 *
 *  Developer:
 */
#define UF_PARAM_DEPART_FEED_PERCENT   4020  /* Param_type_double */


/* UF_PARAM_ENGAGE_SPINDLE_SPEED_TOG
 *
 *  Description:
 *  This parameter activates the engage spindle speed.
 *
 *  Type: UF_PARAM_type_int
 *
 *  Name: Engage Spindle Speed Toggle
 *  Variable Name: <prefix>_engage_spindle_speed_toggle
 *
 *  Possible Values: 
 *        0 -- Inactive
 *        1 -- Active
 *
 * 
 */
#define UF_PARAM_ENGAGE_SPINDLE_SPEED_TOG   4021 


/* UF_PARAM_ENGAGE_SPINDLE_SPEED
 *
 *  Description:
 *  This parameter specifies the engage spindle speed.
 *
 *  Type: UF_PARAM_type_double
 *
 *  Name: Engage Spindle Speed
 *  Variable Name: <prefix>_engage_spindle_speed
 *
 *  Possible Values: Positive double or zero.
 *
 * 
 */
#define UF_PARAM_ENGAGE_SPINDLE_SPEED   4022 


/* UF_PARAM_SPINDLE_DIR_AUTO
 *
 *  Description:
 *  This parameter identifies whether spindle direction is to be evaluated
 *  automatically.
 *
 *  Type: UF_PARAM_type_int
 *
 *  Name: Spindle Direction Automatic
 *  Variable Name: <prefix>_spindle_direction_automatic
 *
 *  Possible Values:
 *     0 = inactive
 *     1 = active
 *
 * 
 */
#define UF_PARAM_SPINDLE_DIR_AUTO   4100  /* UF_PARAM_type_int */


typedef enum
{
    UF_PARAM_spindle_dir_control_none = 0,
    UF_PARAM_spindle_dir_control_clw,
    UF_PARAM_spindle_dir_control_cclw
} UF_PARAM_spindle_dir_control_t;

/* UF_PARAM_SPINDLE_DIR_CONTROL
 *
 *  Description:
 *  This parameter identifies the desired spindle direction if automatic
 *  spindle direction control is turned off (=0)
 *
 *  This parameter is only valid for Turning Operations where 
 *    UF_PARAM_SPINDLE_DIR_AUTO is set to 0.  For all other cases,
 *    the spindle direction is specified using UF_PARAM_TL_DIRECTION.
 *
 *  Type: UF_PARAM_type_int
 *
 *  Name: Spindle Direciton Control
 *  Variable Name: <prefix>_spindle_direciton_control
 *
 *  Possible Values: UF_PARAM_spindle_dir_control_t
 *
 * 
 */
#define UF_PARAM_SPINDLE_DIR_CONTROL   4101  /* UF_PARAM_type_int */


/* UF_PARAM_CLR_DIST
 *
 *  Description:
 *  This index refers to the clearance distance when the specification of the
 *  Clearance distance s done as a rule.
 *
 *  Type: UF_PARAM_type_double_length
 *
 *  Name: Clearance Distance
 *  Variable Name: <prefix>_clearance_distance
 *
 *  Possible Values: UF_PARAM_type_double_length
 *
 * 
 */
#define UF_PARAM_CLR_DIST   5202 


/* UF_PARAM_RET_DISTANCE
 *
 *  Description:
 *  This index refers to the retract distance when the specification of the
 *  Retract distance is done as a rule.
 *
 *  Type: UF_PARAM_type_double_length
 *
 *  Name: Retract Dist
 *  Variable Name: <prefix>_retract_dist
 *
 *  Possible Values: UF_PARAM_type_double_length
 *
 * 
 */
#define UF_PARAM_RET_DISTANCE   5204 


/* UF_PARAM_HOLE_AXIS_IJK
 *
 *  Description:
 *  This index refers to the 3d vector when the specification of the Hole Axis
 *  is done as a rule.
 *
 *  Type: UF_PARAM_type_3d_length
 *
 *  Name: Hole Axis IJK
 *  Variable Name: <prefix>_hole_axis_ijk
 *
 *  Possible Values: UF_PARAM_type_3d_length
 *
 * 
 */
#define UF_PARAM_HOLE_AXIS_IJK   5206 


/* UF_PARAM_MAX_DEPTH_DIST
 *
 *  Description:
 *  This index refers to the distance when the specification of the Maximum
 *  depth is done as a distance.
 *
 *  Type: UF_PARAM_type_double_length
 *
 *  Name: Maximum Depth Distance
 *  Variable Name: <prefix>_maximum_depth_distance
 *
 *  Possible Values: UF_PARAM_type_double_length
 *
 * 
 */
#define UF_PARAM_MAX_DEPTH_DIST   5211 


/* UF_PARAM_RET_DIST_ON_TLAXIS_CHANGE
 *
 *  Description:
 *  This index refers to the additional distance that need to be added to 
 *  the retract distance when the tool axis changes during the processing 
 *  in Hole Making Operation.
 *
 *  Type: UF_PARAM_type_double_length
 *
 *  Name: Retract Distance on Tool Axis Change
 *  Variable Name: <prefix>_retract_distance_on_tool_axis_change
 *
 *  Possible Values: UF_PARAM_type_double_length
 *
 * 
 */
#define UF_PARAM_RET_DIST_ON_TLAXIS_CHANGE   5213 


/* UF_PARAM_HOLE_DIAM
 *
 *  Description:
 *  This index refers to the diameter of the hole that need to be cut
 *  in Hole Making Operation.
 *
 *  Type: UF_PARAM_type_double_length
 *
 *  Name: Hole Diameter
 *  Variable Name: <prefix>_hole_diameter
 *
 *  Possible Values: UF_PARAM_type_double_length
 *
 * 
 */
#define UF_PARAM_HOLE_DIAM   5214 


/* UF_PARAM_PREDRILL_HOLE_DIAM
 *
 *  Description:
 *  This index refers to the diameter of the predrill hole 
 *  in Hole Making Operation.
 *
 *  Type: UF_PARAM_type_double_length
 *
 *  Name: Predrill Hole Diameter
 *  Variable Name: <prefix>_predrill_hole_diameter
 *
 *  Possible Values: UF_PARAM_type_double_length
 *
 * 
 */
#define UF_PARAM_PREDRILL_HOLE_DIAM   5215 


typedef enum
{
    UF_PARAM_control_point_type_tool_tip    = 0,
    UF_PARAM_control_point_type_shoulder    = 1
} UF_PARAM_control_point_type_t;


/* UF_PARAM_CONTROL_POINT_TYPE
 *
 *  Description:
 *  This index refers to the type of control point
 *  in Hole Making Operation.
 *
 *  Type: UF_PARAM_type_int
 *
 *  Name: Control Point Type
 *  Variable Name: <prefix>_control_point_type
 *
 *  Possible Values: UF_PARAM_control_point_type_t
 *
 * 
 */
#define UF_PARAM_CONTROL_POINT_TYPE   5216 


typedef enum
{
    UF_PARAM_hole_axis_type_vector               = 0,
    UF_PARAM_hole_axis_type_rule                 = 1,
    UF_PARAM_hole_axis_type_rule_if_no_vector    = 2
} UF_PARAM_hole_axis_type_t;


/* UF_PARAM_HOLE_AXIS_TYPE
 *
 *  Description:
 *  This index refers to the type of hole axis to use
 *  in Hole Making Operation.
 *
 *  Type: UF_PARAM_type_int
 *
 *  Name: Hole Axis Type
 *  Variable Name: <prefix>_hole_axis_type
 *
 *  Possible Values: UF_PARAM_hole_axis_type_t
 *
 * 
 */
#define UF_PARAM_HOLE_AXIS_TYPE   5217 


typedef enum
{
    UF_PARAM_hole_depth_type_point        = 0,
    UF_PARAM_hole_depth_type_rule         = 1
} UF_PARAM_hole_depth_type_t;


/* UF_PARAM_HOLE_DEPTH_TYPE
 *
 *  Description:
 *  This index refers to the type of hole depth to use 
 *  in Hole Making Operation.
 *
 *  Type: UF_PARAM_type_int
 *
 *  Name: Hole Depth Type
 *  Variable Name: <prefix>_hole_depth_type
 *
 *  Possible Values: UF_PARAM_hole_depth_type_t
 *
 * 
 */
#define UF_PARAM_HOLE_DEPTH_TYPE   5218 


typedef enum
{
    UF_PARAM_model_depth_type_always    = 0,
    UF_PARAM_model_depth_type_rule      = 1
} UF_PARAM_model_depth_type_t;


/* UF_PARAM_MODEL_DEPTH_TYPE
 *
 *  Description:
 *  This index refers to the type of model depth to use
 *  in Hole Making Operation.
 *
 *  Type: UF_PARAM_type_int
 *
 *  Name: Model Depth Type
 *  Variable Name: <prefix>_model_depth_type
 *
 *  Possible Values: UF_PARAM_model_depth_type_t
 *
 * 
 */
#define UF_PARAM_MODEL_DEPTH_TYPE   5219 


/* UF_PARAM_CHECK_FLUTE_LENGTH
 *
 *  Description:
 *  This index states if the flute length of the tool 
 *  should be validated or not.  
 *
 *  Type: UF_PARAM_type_logical
 *
 *  Name: Check Flute Length
 *  Variable Name: <prefix>_check_flute_length
 *
 *  Possible Values: TRUE or FALSE
 *
 * 
 */
#define UF_PARAM_CHECK_FLUTE_LENGTH   5220 


/* UF_PARAM_CHECK_TOOL_LENGTH
 *
 *  Description:
 *  This index states if the tool length of the tool 
 *  should be validated or not.  
 *
 *  Type: UF_PARAM_type_logical
 *
 *  Name: Check Tool Length
 *  Variable Name: <prefix>_check_tool_length
 *
 *  Possible Values: TRUE or FALSE
 *
 * 
 */
#define UF_PARAM_CHECK_TOOL_LENGTH   5221 


typedef enum
{
    UF_PARAM_hole_top_output_type_holetop    = 0,
    UF_PARAM_hole_top_output_type_ipwtop     = 1
} UF_PARAM_hole_top_output_type_t;


/* UF_PARAM_HOLE_TOP_OUTPUT_TYPE
 *
 *  Description:
 *  This index refers to the type of output for hole top to use
 *  in Hole Making Operation. 
 *
 *  Type: UF_PARAM_type_int
 *
 *  Name: Hole Top Output Type
 *  Variable Name: <prefix>_hole_top_output_type
 *
 *  Possible Values: UF_PARAM_hole_top_output_type_t
 *
 * 
 */
#define UF_PARAM_HOLE_TOP_OUTPUT_TYPE   5222 


typedef enum
{
    UF_PARAM_rapto_offset_toggle_inactive = 0,
    UF_PARAM_rapto_offset_toggle_active   = 1

} UF_PARAM_rapto_offset_toggle_t;


/* UF_PARAM_RAPTO_OFFSET_TOGGLE
 *
 *  Description:
 *  This index indicates whether to use Rapto Offset value
 *  in CYCLE RAPTO parameter.
 *
 *  Type: UF_PARAM_type_int
 *
 *  Name: Rapto Offset Toggle
 *  Variable Name: <prefix>_rapto_offset_toggle
 *
 *  Possible Values: UF_PARAM_rapto_offset_toggle_t
 *
 * 
 */
#define UF_PARAM_RAPTO_OFFSET_TOGGLE   5223 


/* UF_PARAM_RAPTO_OFFSET
 *
 *  Description:
 *  This index refers to the RAPTO Offset that is used in
 *  the CYCLE RAPTO parameter. 
 *
 *  Type: UF_PARAM_type_double_length
 *
 *  Name: Rapto Offset
 *  Variable Name: <prefix>_rapto_offset
 *
 *  Possible Values: UF_PARAM_type_double_length
 *
 * 
 */
#define UF_PARAM_RAPTO_OFFSET   5224 


/* UF_PARAM_GEOM_PARENT
 *
 *  Description:
 *  This index refers to the name of the geometry parent.
 *
 *  Type: UF_PARAM_type_string
 *
 *  Name: Geometry Parent
 *  Variable Name: <prefix>_geometry_parent
 *
 *  Possible Values: UF_PARAM_type_string
 *
 * 
 */
#define UF_PARAM_GEOM_PARENT   5225 


/* UF_PARAM_FEATURE_TYPES
 *
 *  Description:
 *  This index refers to the list of feature types
 *
 *  Type: UF_PARAM_type_vla_string
 *
 *  Name: Feature Types
 *  Variable Name: <prefix>_feature_types
 *
 *  Possible Values: UF_PARAM_type_vla_string
 *
 * 
 */
#define UF_PARAM_FEATURE_TYPES   5226 


/* UF_PARAM_USER_DEFINED_TP
 *
 *  Description:
 *  This index refers to the option of using the user defined tool path
 *
 *  Type: UF_PARAM_type_logical
 *
 *  Name: Feature Types
 *  Variable Name: <prefix>_feature_types
 *
 *  Possible Values: UF_PARAM_type_logical
 *
 * 
 */
#define UF_PARAM_USER_DEFINED_TP   5227 


/* UF_PARAM_USE_USER_DEFINED_TP
 *
 *  Description:
 *  This index refers to the toggle indicating whether or not to use
 *  the user defined tool path.
 *
 *  Type: UF_PARAM_type_logical
 *
 *  Name: Use User Defined Tool Path
 *  Variable Name: <prefix>_use_user_defined_tool_path
 *
 *  Possible Values: UF_PARAM_type_logical
 *
 * 
 */
#define UF_PARAM_USE_USER_DEFINED_TP   5228 


/* UF_PARAM_USE_QUERY
 *
 *  Description:
 *  This index states whether the tool query should be
 *  executed or not.
 *
 *  Type: UF_PARAM_type_logical
 *
 *  Name: Use Query
 *  Variable Name: <prefix>_use_query
 *
 *  Possible Values: TRUE or FALSE
 *
 * 
 */
#define UF_PARAM_USE_QUERY   5230 


/* UF_PARAM_COLLISION_SAFE_CLEARANCE
 *
 *  Description:
 *  This index refers to the safe clearance applied to the collision check. 
 *
 *  Type: UF_PARAM_type_double_length
 *
 *  Name: Collision Safe Clearance
 *  Variable Name: <prefix>_collision_safe_clearance
 *
 *  Possible Values: UF_PARAM_type_double_length
 *
 * 
 */
#define UF_PARAM_COLLISION_SAFE_CLEARANCE   5233 


typedef enum
{
    UF_PARAM_clv_range_auto_generate  = 0,  /* cut levels defined by system */

    UF_PARAM_clv_range_user_defined   = 1,  /* cut levels are defined by user */

    UF_PARAM_clv_range_single         = 2   /* Single cut range */

} UF_PARAM_clv_range_type_t;


/* UF_PARAM_CUTLEV_RANGE_TYPE
 *
 *   Description:
 *      Specifies the type of cut level ranges.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Cut Level Range Type
 *  Variable Name: <prefix>_cut_level_range_type
 *
 *   NOTE: Read-Only Parameter
 *
 *   Possible Values: UF_PARAM_clv_range_type_t
 *
 * 
*/
#define UF_PARAM_CUTLEV_RANGE_TYPE   5400 


typedef enum
{
    UF_PARAM_clv_range_subdiv_equalise = 0,  /* subdivide cut range into equal steps */
    
    UF_PARAM_clv_range_subdiv_bottoms_only   = 1,  /* cut at range bottoms only */

    UF_PARAM_clv_range_subdiv_optimal = 2   /* subdivide cut range in an optimal
                                          * way such that max distance on part
                                          * between cuts is approximately the
                                          * same. */
} UF_PARAM_clv_range_subdiv_type_t; 


/* UF_PARAM_CUTLEV_RANGE_SUBDIV_TYPE
 *
 *   Description:
 *      Specifies how a cut level range is to be subdivided. Whether
 *      only the range bottoms are to be cut, or if the global depth
 *      per cut value is to be used to subdivide the cut level range
 *      into equal steps.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Cut Range Bottoms Only
 *  Variable Name: <prefix>_cut_range_bottoms_only
 *
 *   Possible Values: UF_PARAM_clv_range_subdiv_type_t
 *
 * 
 */
#define UF_PARAM_CUTLEV_RANGE_SUBDIV_TYPE   5401 


typedef enum
{
    UF_PARAM_clv_top_off_mode_off = 0,   /* Don't top off horizontal surfaces. */

    UF_PARAM_clv_top_off_mode_on  = 1    /* Do top off horizontal surfaces.  */

} UF_PARAM_clv_top_off_mode_t;


/* UF_PARAM_CUTLEV_TOP_OFF_MODE
 *
 *   Description:
 *      Specifies if the horizontal surfaces should be topped off.
 *      This is only available for 'single' range type.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Cut Level Top Off Mode
 *  Variable Name: <prefix>_cut_level_top_off_mode
 *
 *   Possible Values: UF_PARAM_clv_top_off_mode_t
 *
 * 
*/
#define UF_PARAM_CUTLEV_TOP_OFF_MODE   5402 


/* UF_PARAM_CIR_FEED_COMP_MAXIMUM
 *
 *   Description:
 *      Paramter is the maximum compensation factor
 *      for circular feedrate compensation..
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Maximum Circular Feedrate Compensation Factor.
 *  Variable Name: <prefix>_maximum_circular_feedrate_compensation_factor_
 *
 *   Possible Values: UF_PARAM_type_double >= 1.0.
 *
 * 
 */
#define UF_PARAM_CIR_FEED_COMP_MAXIMUM   5650        /* UF_PARAM_type_double_length */


/* UF_PARAM_CIR_FEED_COMP_MINIMUM
 *
 *   Description:
 *      Paramter is the minimum compensation factor
 *      for circular feedrate compensation..
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Minimum Circular Feedrate Compensation Factor.
 *  Variable Name: <prefix>_minimum_circular_feedrate_compensation_factor_
 *
 *   Possible Values: 0.0 < UF_PARAM_type_double <= 1.0.
 *
 * 
 */
#define UF_PARAM_CIR_FEED_COMP_MINIMUM   5651        /* UF_PARAM_type_double_length */


typedef enum
{
   UF_PARAM_edgext_type_none    = 0,
   UF_PARAM_edgext_type_specify = 1
} UF_PARAM_edgext_type_t;


/* UF_PARAM_EDGEXT_TYPE
 *   Description:
 *      This parameters specifies the status of toggle Extend at Edges. 
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Edge Extension Type
 *  Variable Name: <prefix>_edge_extension_type
 *
 *   Possible Values: UF_PARAM_edgext_control_t
 *
 * 
 */
#define UF_PARAM_EDGEXT_TYPE   5700  /* UF_PARAM_type_int */


/* UF_PARAM_EDGEXT_SPECIFY
 *   Description:
 *      This parameter specifies the edge extension length as a distance.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Edge Extension Length
 *  Variable Name: <prefix>_edge_extension_length
 *
 *   Possible Values: Positive double
 *
 * 
 */
#define UF_PARAM_EDGEXT_SPECIFY   5701  /* UF_PARAM_type_double_length */


/* UF_PARAM_EDGEXT_PERC
 *
 *   Description:
 *      This parameter specifies the tangent extension as a percentage of
 *      the tool diameter.
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Tangent extension as percentage of tool
 *  Variable Name: <prefix>_tangent_extension_as_percentage_of_tool
 *
 *   Possible Values:
 *             double
 *
 * 
 */
#define UF_PARAM_EDGEXT_PERC   5702  /* UF_PARAM_type_double */


typedef enum
{
    UF_PARAM_cut_volume_none = 0,
    UF_PARAM_cut_volume_calc = 1
} UF_PARAM_cut_volume_t;

/* UF_PARAM_CUT_VOLUME_USAGE
 *
 *   Description:
 *      This parameter specifies whether the volume of material removed
 *      by the tool should be calculated.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Cut Volume Usage
 *  Variable Name: <prefix>_cut_volume_usage
 *
 *   Possible Values: UF_PARAM_cut_volume_t
 *
 * 
 */
#define UF_PARAM_CUT_VOLUME_USAGE   5705  /* UF_PARAM_type_int */


/* UF_PARAM_CUT_VOLUME_MIN
 *
 *   Description:
 *      If the CUT VOLUME USAGE parameter is TRUE, this parameter
 *      determines the minimum percentage of material that must be removed.
 *      If this percentage is not met, then the operation's toolpath will
 *      be suppressed from output.
 *
 *   Type: UF_PARAM_type_double
 *
 *   Name: Cut Volume Minimum Percentage
 *  Variable Name: <prefix>_cut_volume_minimum_percentage
 *
 *   Possible Values:
 *       0.0 <= Cut Volume Percentage <= 100.0
 *
 * 
 */
#define UF_PARAM_CUT_VOLUME_MIN   5706  /* UF_PARAM_type_double */


/* UF_PARAM_CUT_VOLUME_ACTUAL
 *
 *   Description:
 *      If the CUT VOLUME USAGE parameter is TRUE, this parameter
 *      determines the actual volume of material that was removed and the
 *      maximum possible that could have been removed if holder collisions
 *      were not eliminated. If CUT TOOL HOLDER USAGE is false, both
 *      values will be the same.
 *
 *   Type: UF_PARAM_type_2d_length
 *
 *   Name: Cut Volume Actual Removed
 *  Variable Name: <prefix>_cut_volume_actual_removed
 *
 *   NOTE: Read-Only Parameter
 *
 *   Possible Values:
 *       [0] = Actual Material Volume Removed.
 *       [1] = Maximum possible material Volume.
 *
 * 
 */
#define UF_PARAM_CUT_VOLUME_ACTUAL   5707  /* UF_PARAM_type_2d_length */


typedef enum
{
    UF_PARAM_tl_min_len_none = 0,
    UF_PARAM_tl_min_len_calc = 1
} UF_PARAM_tl_min_len_t;

/* UF_PARAM_TL_MIN_LENGTH_USAGE
 *
 *   Description:
 *      This parameter specifies whether the minimum tool length that can
 *      cut the toolpath without having a holder collision should be determined.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Tool Minimum Length Usage
 *  Variable Name: <prefix>_tool_minimum_length_usage
 *
 *   Possible Values: UF_PARAM_tl_min_len_t
 *
 * 
 */
#define UF_PARAM_TL_MIN_LENGTH_USAGE   5708  /* UF_PARAM_type_int */


/* UF_PARAM_TL_MIN_LENGTH
 *
 *   Description:
 *      If the TOOL MIN LENGTH USAGE parameter is TRUE, this parameter
 *      returns the minimum tool length that can be used and avoid any tool holder
 *      collisions.
 *
 *   Type: UF_PARAM_type_double_length
 *
 *   Name: Tool Minimum Length
 *  Variable Name: <prefix>_tool_minimum_length
 *
 *   NOTE: Read-Only Parameter
 *
 *   Possible Values:
 *       Positive double
 *
 * 
 */
#define UF_PARAM_TL_MIN_LENGTH   5709  /* UF_PARAM_type_double_length */


typedef enum 
{
    UF_PARAM_cut_between_none          = 0,           /* Don't do cut between machining. */
    UF_PARAM_cut_between_using_follow_periphery = 1   /* Do cut between machining using a 
                                                      follow periphery pattern. */
} UF_PARAM_cut_between_method_t;


/* UF_PARAM_CUT_BETWEEN_METHOD
 *
 *   Description:
 *      This parameter specifies the type of cut between machining.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Cut Between Method
 *  Variable Name: <prefix>_cut_between_method
 *
 *   Possible Values:  - UF_PARAM_cut_between_method_t
 *
 * 
 *
 */
#define UF_PARAM_CUT_BETWEEN_METHOD   5721  /* UF_PARAM_type_int */


typedef enum
{
    UF_PARAM_path_unsuppressed = 0,
    UF_PARAM_path_suppressed   = 1
} UF_PARAM_suppress_path_t;

/* UF_PARAM_SUPPRESS_PATH
 *
 *   Description:
 *      This parameter specifies whether the generated toolpath should
 *      be suppressed from output because it did not meet defined requirements.
 *
 *   NOTE: Suppressed paths will not be posted and do not participate in the IPW.
 *         However, the operation can be edited.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Suppress Path
 *  Variable Name: <prefix>_suppress_path
 *
 *   Possible Values: UF_PARAM_suppress_path_t
 *
 * 
 */
#define UF_PARAM_SUPPRESS_PATH   5741  /* UF_PARAM_type_int */


typedef enum 
{
    UF_PARAM_round_point_output_status_off = 0,   /* Round point positions. */
    UF_PARAM_round_point_output_status_on = 1     /* Do not round point positions. */
} UF_PARAM_round_point_output_status_t;


/* UF_PARAM_ROUND_POINT_OUTPUT_STATUS
 *
 *   Description:
 *      This parameter specifies whether the point positions
 *      for certain Manual Cut Pattern actions (Move To Point
 *      and Reposition To Point) should be rounded to a 
 *      specific value.
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Round Point Output Status
 *  Variable Name: <prefix>_round_point_output_status
 *
 *   Possible Values:  - UF_PARAM_round_point_output_status_t
 *
 * 
 *
 */
#define UF_PARAM_ROUND_POINT_OUTPUT_STATUS   5761  /* UF_PARAM_type_int */


typedef enum 
{
    UF_PARAM_round_point_output_method_ten_to_minus_seven = -7,    /*  +/-    0.0000001  */
    UF_PARAM_round_point_output_method_ten_to_minus_six   = -6,    /*  +/-    0.000001  */
    UF_PARAM_round_point_output_method_ten_to_minus_five  = -5,    /*  +/-    0.00001  */
    UF_PARAM_round_point_output_method_ten_to_minus_four  = -4,    /*  +/-    0.0001  */
    UF_PARAM_round_point_output_method_ten_to_minus_three = -3,    /*  +/-    0.001  */
    UF_PARAM_round_point_output_method_ten_to_minus_two   = -2,    /*  +/-    0.01  */
    UF_PARAM_round_point_output_method_ten_to_minus_one   = -1,    /*  +/-    0.1  */
    UF_PARAM_round_point_output_method_one = 0,                    /*  +/-    1.0 */
    UF_PARAM_round_point_output_method_ten = 1,                    /*  +/-   10.0 */
    UF_PARAM_round_point_output_method_one_hundred = 2,            /*  +/-  100.0 */
    UF_PARAM_round_point_output_method_one_thousand = 3            /*  +/- 1000.0 */
} UF_PARAM_round_point_output_method_t;


/* UF_PARAM_ROUND_POINT_OUTPUT_METHOD
 *
 *   Description:
 *      This parameter specifies the method to use
 *      to round the point positions for certain
 *      Manual Cut Pattern Actions (Move To Point and
 *      Reposition to Point).
 *
 *   Type: UF_PARAM_type_int
 *
 *   Name: Round Point Output Method
 *  Variable Name: <prefix>_round_point_output_method
 *
 *   Possible Values:  - UF_PARAM_round_point_output_method_t
 *
 * 
 *
 */
#define UF_PARAM_ROUND_POINT_OUTPUT_METHOD   5762  /* UF_PARAM_type_int */


/* UF_PARAM_PATHCHECK_STATUS
 *
 *  Description:
 *  Status codes from the gouge checker.
 *
 *  Type: UF_PARAM_type_int
 *
 *  Name: External ID
 *  Variable Name: <prefix>_external_id
 *
 *  Possible Values: All valid integers
 *
 * 
 */
#define UF_PARAM_PATHCHECK_STATUS   5763  /* UF_PARAM_type_int */


/* UF_PARAM_PATHCHECK_COUNT
 *
 *  Description:
 *  Number of gouges or other violation
 *  found by the path checker.
 *
 *  Type: UF_PARAM_type_int
 *
 *  Name: External ID
 *  Variable Name: <prefix>_external_id
 *
 *  Possible Values: All valid integers
 *
 * 
 */
#define UF_PARAM_PATHCHECK_COUNT   5764  /* UF_PARAM_type_int */


/* UF_PARAM_TH_COLLISION_COUNT
 *
 *  Description:
 *  Number of toolholder collsions
 *  found by the path checker.
 *
 *  Type: UF_PARAM_type_int
 *
 *  Name: External ID
 *  Variable Name: <prefix>_external_id
 *
 *  Possible Values: All valid integers
 *
 * 
 */
#define UF_PARAM_TH_COLLISION_COUNT   5765  /* UF_PARAM_type_int */


typedef enum UF_PARAM_simplify_shapes_method_e
{
    UF_PARAM_simplify_shapes_method_none = 0,
    UF_PARAM_simplify_shapes_method_convex_hull = 1,
    UF_PARAM_simplify_shapes_method_minimum_box = 2
} UF_PARAM_simplify_shapes_method_t;


/* UF_PARAM_SIMPLIFY_SHAPES_METHOD
 *
 *  Description:
 *     Method to simplify shapes.
 *
 *  Type: UF_PARAM_type_int
 *
 *  Name: Simplify Shapes Method
 *  Variable Name: <prefix>_simplify_shapes_method
 *
 *  Possible Values: UF_PARAM_simplify_shapes_method_t
 *
 * 
 */
#define UF_PARAM_SIMPLIFY_SHAPES_METHOD   5766  /* UF_PARAM_type_int */


/* UF_PARAM_FINISH_STEPOVER
 *
 *  Description:
 *     This parameter indicates the stepover value of a finish pass.
 *
 *  Type: UF_PARAM_type_double_length
 *
 *  Name: Finish Stepover
 *  Variable Name: <prefix>_finish_stepover
 *
 *  Possible Values: Greater than 0
 *
 * 
 */
#define UF_PARAM_FINISH_STEPOVER   5767  /* UF_PARAM_type_double_length */


typedef enum UF_PARAM_small_area_status_e
{
    UF_PARAM_small_area_status_cut = 0,
    UF_PARAM_small_area_status_ignore = 1
} UF_PARAM_small_area_status_t;


/* UF_PARAM_SMALL_AREA_STATUS
 *
 *  Description:
 *     This parameter indicates the status of the region, either cut or ignored.
 *
 *  Type: UF_PARAM_type_int
 *
 *  Name: Small Area Status
 *  Variable Name: <prefix>_small_area_status
 *
 *  Possible Values: UF_PARAM_small_area_status_t
 *
 * 
 */
#define UF_PARAM_SMALL_AREA_STATUS   5768  /* UF_PARAM_type_int */


/* UF_PARAM_AREA_SIZE
 *
 *  Description:
 *     This parameter indicates the area size of the region to be ignored.
 *     It is used when the parameter UF_PARAM_SMALL_AREA_STATUS
 *     is set to UF_PARAM_small_area_status_ignore. 
 *
 *  Type: UF_PARAM_type_double_length
 *
 *  Name: Area Size
 *  Variable Name: <prefix>_area_size
 *
 *  Possible Values: Greater than 0
 *
 * 
 */
#define UF_PARAM_AREA_SIZE   5769  /* UF_PARAM_type_double_length */


/* UF_PARAM_EMPTY_PATH
 *
 *   Description:
 *    This parameter specifies whether the generated tool path is empty, i.e.
 *    does not contain any system generated motions
 *
 *   Type: UF_PARAM_type_logical
 *
 *   Name: Empty Path
 *  Variable Name: <prefix>_empty_path
 *
 *   Possible Values: 
 *         true  - Path is empty according to the definition
 *         false - Path is not empty according to the definition
 *
 * 
 */
#define UF_PARAM_EMPTY_PATH   6005  /* UF_PARAM_type_logical */


/* UF_PARAM_APPROVED_PATH_STATUS
 *
 *   Description:
 *    This parameter specifies whether the operation tool path is approved
 *
 *   Type: UF_PARAM_type_logical
 *
 *   Name: Approved Path
 *  Variable Name: <prefix>_approved_path
 *
 *   Possible Values: 
 *         true  - Path is approved according to the definition
 *         false - Path is not approved according to the definition
 *
 * 
 */
#define UF_PARAM_APPROVED_PATH_STATUS   6006  /* UF_PARAM_type_logical */


#ifdef __cplusplus
}
#endif
#endif /* UF_PARAM_INDICES_H_INCLUDED */
