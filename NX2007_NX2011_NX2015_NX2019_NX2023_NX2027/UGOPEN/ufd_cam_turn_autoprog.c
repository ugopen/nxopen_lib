
/*=============================================================================
                 Copyright (c)  2002 Unigraphics Solutions, Inc.
                        Unpublished - All Rights Reserved
=============================================================================*/
/******************************************************************************
 * File Name: ufd_cam_turn_autoprog.c                                         *
 *                                                                            *
 * File Description:                                                          *
 *                                                                            *
 *   This program shows how to use the following UG/Open API routine(s):      *
 *                                                                            *
 *   UF_OPER_create                                                           *
 *   UF_PARAM_generate                                                        *
 *   UF_TURN_map_vec2_to_acs                                                  *
 *   UF_TURN_map_pnt2_to_acs                                                  *
 *   UF_TURN_ask_cut_regions_exist                                            *
 *   UF_TURN_ask_cut_region_of_index                                          *
 *   UF_TURN_ipw_box                                                          *
 *   UF_TURN_save_spinning_ipw_as_part                                        *
 *   UF_SETUP_generate_program                                                *
 *                                                                            *
 *   Furthermore, this sample program is meant to demonstrate an approach     *
 *   for automated rule based machining employing the new UG/Open API of      *
 *   the turning module.                                                      *
 *   In the course of the automatic processing, a variant part with an        *
 *   arbitrary number of grooves and one or more larger reversals on the      *
 *   outside diameter is analyzed for remaining material. Once the according  *
 *   cut regions have been detected, the system creates suitable turning      *
 *   operations following the rules implemented and generates the latter in   *
 *   sequence. Finally, the resulting In Process Workpiece is saved as        *
 *   3D solid.                                                                *
 *                                                                            *
 * Program Description:                                                       *
 *   This example requires an open part, a manufacturing setup with chained   *
 *   part geometry and a predefined blank of type "bar stock".                *
 *   Example: cam_turn_autoprog.prt                                           *
 *                                                                            *
 *                                                                     *
 ******************************************************************************/

/***************************** Include Files **********************************/
#include <stdlib.h>
#include <stdio.h>
#include <math.h>

#include <uf.h>
#include <uf_ui.h>
#include <uf_oper.h>
#include <uf_cutter.h>
#include <uf_ncgroup.h>
#include <uf_setup.h>
#include <uf_param.h>
#include <uf_param_indices.h>
#include <uf_obj.h>
#include <uf_part.h>
#include <uf_curve.h>
#include <uf_cam.h>

#include <uf_turn.h>

/************************************ Main ************************************/

#define CLEARANCE_FACTOR 2

static void do_create_turning_oper_api(void)
{
    int                    return_value;
    tag_t                  rough_eid, groove_eid, last_eid, tool_eid, point_tag;
    tag_t                  setup_tag, mct_root, geom_root, workp_tag, workp_location,
                           edge1, edge2, edge3, edge4;
    logical                exi, sort_flag, ret_val = TRUE;
    int                    num_regs, i, sort_arr[20], isort, workp_direct;
    double                 size, size_arr[20], point[3], point_arr[20][3], point_arr2[20][2], 
                           vec2[2], vec3[3], cutter_size, edge_length,nose_angle, insert_length,
                           insert_width, blank_length, blank_diameter, length, diameter,
                           bottom_left_scs[2], top_right_scs[2], bottom_left[3],top_left[3],
                           bottom_right[3],top_right[3], pnt2[2];
    char                   mess_buf[500], buffer[500];
    UF_TURN_cut_regions_location_t loc;
    UF_PARAM_disp_path_t   disp_path, *disp_ptr = &disp_path;
    UF_CURVE_line_t        curve_line;
    UF_CURVE_line_p_t      curve_ptr = &curve_line;
    char*                  mess;


/***************************************************************************************
 *  Rule implemented:
 *
 *  1. Rough cut major portion of material at high cutting speed
 *     with a 55 degree diamond insert tool but omit reversals. Apply
 *     cut strategy "linear zig". 
 *  2. Detect remaining cut regions for same tool as in step 1 in order
 *     to save machining time.
 *     Sort these cut regions from "right to left" (relative to spindle axis)
 *     and machine them in this order, if their area is greater than threshold
 *     value for roughing (computed based on insert size). Apply cut strategy
 *     "linear zig" for each cut region again. 
 *  3. Change tool to OD grooving tool. Detect cut regions and sort
 *     them from "right to left". 
 *  4. Machine remaining cut regions in this order, if their area is greater
 *     than threshold value and apply cut strategy "linear zig-zag" here. 
 *  5. Finally, machine all remaining "small" cut regions (expected to be
 *     groove features) using the "plunge zig-zag" cut strategy. 
 *
 * The implemented rule based machining method could be further generalized by
 * making use of library tool queries instead of resorting to predetermined tool 
 * templates only.
 ***************************************************************************************/


    if( UF_PART_ask_display_part() != null_tag )
    {
/*
 * generate first roughing operation
 */
        UF_OPER_create ("turning", "ROUGH_TURN_OD", &rough_eid);
/*
 * set reversal mode to omit, cleanup off, additional profiling on
 */
        UF_PARAM_set_int_value (rough_eid, UF_PARAM_TURN_REVERSAL_MODE,
                                UF_PARAM_turn_reversal_mode_omit);
        UF_PARAM_set_int_value (rough_eid, UF_PARAM_TURN_CLEANUP,
                                UF_PARAM_turn_cleanup_none);
        UF_PARAM_set_int_value (rough_eid, UF_PARAM_TURN_PROFILING, 1);
/*
 * create roughing tool
 */
        UF_CUTTER_create ("turning", "OD_55_L", &tool_eid);
/*
 * set orientation angle to 30 degrees (radians needed)
 */
        UF_PARAM_set_double_value (tool_eid, UF_PARAM_TL_ORIENTATION,
                                   30.0 * DEGRA);
/*
 * get insert length of tool
 */
        UF_PARAM_ask_double_value (tool_eid, UF_PARAM_TL_CUT_EDGE_LENGTH,
                                   &insert_length);
/*
 * add tool to machine and operation
 */
        UF_SETUP_ask_setup (&setup_tag);
        UF_SETUP_ask_mct_root (setup_tag, &mct_root);
        UF_NCGROUP_accept_member (mct_root, tool_eid);
        UF_NCGROUP_accept_member (tool_eid, rough_eid);
/*
 * add workpiece to operation
 */
        UF_SETUP_ask_geom_root (setup_tag, &geom_root);
        UF_NCGROUP_ask_object_of_name (geom_root, "WORKPIECE", &workp_tag);
        UF_NCGROUP_accept_member (workp_tag, rough_eid);
/*
 * get length and diameter of workpiece
 */
        UF_PARAM_ask_double_value (rough_eid, UF_PARAM_TURN_WORKPIECE_LENGTH,
                                   &blank_length);
        UF_PARAM_ask_double_value (rough_eid, UF_PARAM_TURN_WORKPIECE_DIAMETER,
                                   &blank_diameter);
/*
 * set from point
 */
        UF_PARAM_ask_tag_value (rough_eid, UF_PARAM_TURN_WORKPIECE_LOC_TAG, &workp_location);
        UF_CURVE_ask_point_data (workp_location, point);
        UF_PARAM_set_int_value (rough_eid, UF_PARAM_FROM_STATUS, 1);
        UF_PARAM_ask_int_value (rough_eid, UF_PARAM_TURN_WORKPIECE_DIRECTION, &workp_direct);
        if (workp_direct == UF_PARAM_turn_workpiece_direction_from_head_stock)
        {
            pnt2[0] = +blank_length;
        }
        else
        {
            pnt2[0] = -blank_length;
        }
        pnt2[1] = blank_diameter;
/*
 *  map point from spindle oriented coordinate system to absolute coordinate system
 */
        UF_TURN_map_pnt2_to_acs (NULL_TAG, pnt2, point);
        UF_CURVE_create_point (point, &point_tag);
        UF_PARAM_set_tag_value (rough_eid, UF_PARAM_FROM_POINT, point_tag);
/*
 *  set clearance
 */
        UF_PARAM_set_int_value (rough_eid, UF_PARAM_RETURN_STATUS, 1);
        UF_PARAM_set_int_value (rough_eid, UF_PARAM_RETURN_METHOD,
                                UF_PARAM_turn_return_method_clear_radial_only);
        UF_PARAM_set_int_value (rough_eid, UF_PARAM_TURN_CLEAR_RADIAL_TOG, 1);
/*
 * map clearance to absolute coordinate system
 */
        pnt2[0] = 0.0;
        pnt2[1] = (blank_diameter / 2.0) + (CLEARANCE_FACTOR * insert_length);
        UF_TURN_map_pnt2_to_acs (NULL_TAG, pnt2, point);
        UF_CURVE_create_point (point, &point_tag);
        UF_PARAM_set_tag_value (rough_eid, UF_PARAM_TURN_CLEAR_RADIAL_TAG, point_tag);
/*
 * generate first operation
 */
        UF_PARAM_generate (rough_eid, &ret_val);
        last_eid = rough_eid;
/*
 * generate empty roughing operation to update new cut regions
 */
        UF_OPER_create ("turning", "ROUGH_TURN_OD", &rough_eid);
/*
 * set reversal mode back to as_level
 */
        UF_PARAM_set_int_value (rough_eid, UF_PARAM_TURN_REVERSAL_MODE,
                                UF_PARAM_turn_reversal_mode_as_level);
/*
 * add tool and workpiece to operation
 */
        UF_NCGROUP_accept_member (tool_eid, rough_eid);
        UF_NCGROUP_accept_member (workp_tag, rough_eid);
/*
 * ask number of cut regions after first roughing operation
 */
        UF_TURN_ask_cut_regions_exist (rough_eid, &num_regs, &size, &loc, &mess);
/*
 * message to user
 */
        UF_UI_open_listing_window ();
        sprintf (mess_buf, "Number of cut regions found after first roughing oper: %d\n", num_regs);
        UF_UI_write_listing_window (mess_buf);
        sprintf (mess_buf, "Total size of cut regions: %f\n", size);
        UF_UI_write_listing_window (mess_buf);
/*
 * analyze size of cut regions
 */
        for (i=0;i<num_regs;i++)
        {
            UF_TURN_ask_cut_region_of_index (rough_eid, i+1, &size_arr[i], point_arr[i], &exi, &mess);
            sprintf (mess_buf, "Size of cut region %d: %f\n", i+1, size_arr[i]);
            UF_UI_write_listing_window (mess_buf);
/*
 * map absolut coordinates to spindle coordinates
 */
            UF_TURN_map_pnt3_from_acs (NULL_TAG, point_arr[i], point_arr2[i]);
            sprintf (mess_buf, "X -Coordinate of region %d: %f\n", i+1, point_arr2[i][0]);
            UF_UI_write_listing_window (mess_buf);
        }
/*
 * sort cut regions beginning with greatest X-coordinate
 */
        sort_flag = TRUE;
        for (i=0;i<num_regs;i++)
        {
            sort_arr[i] = i;
        }
        while (sort_flag)
        {
            sort_flag = FALSE;
            for (i=0;i<num_regs-1;i++)
            {
                if(point_arr2[sort_arr[i]][0] < point_arr2[sort_arr[i+1]][0])
                {
                    isort = sort_arr[i];
                    sort_arr[i] = sort_arr[i+1];
                    sort_arr[i+1] = isort;
                    sort_flag = TRUE;
                }
            }
        }
/*
 * generate roughing operations for larger cut regions
 */
        UF_PARAM_ask_double_value (tool_eid, UF_PARAM_TL_CUT_EDGE_LENGTH,
                                   &edge_length);
        UF_PARAM_ask_double_value (tool_eid, UF_PARAM_TL_NOSE_ANG,
                                   &nose_angle);
        cutter_size = edge_length * edge_length * sin(nose_angle);
        sprintf (mess_buf, "cutter size: %f\n", cutter_size);
        UF_UI_write_listing_window (mess_buf);
        
        for (i=0;i<num_regs;i++)
        {
            if (size_arr[sort_arr[i]] >= cutter_size * 10.)
            {
/*
 * set cut region selection point and generate operation
 */
                UF_CURVE_create_point (point_arr[sort_arr[i]], &point_tag);
                UF_PARAM_set_int_value (rough_eid, UF_PARAM_TURN_CUT_REG_SELECT_TOG, 1);
                UF_PARAM_set_tag_value (rough_eid, UF_PARAM_TURN_CUT_REG_SELECT_TAG,
                                        point_tag);
/*
 * set start point to cut region selection point + offset
 * set return point method to clear radial, set radial clearance
 */
                point[0] = point_arr[sort_arr[i]][0];
                point[1] = point_arr[sort_arr[i]][1];
                point[2] = point_arr[sort_arr[i]][2];
                UF_PARAM_ask_double_value (tool_eid, UF_PARAM_TL_CUT_EDGE_LENGTH,
                                           &insert_length);
/*
 * map offset vector to absolute coordinate system
 */
                vec2[0] = 0.0;
                vec2[1] = CLEARANCE_FACTOR * insert_length;
                UF_TURN_map_vec2_to_acs (NULL_TAG, vec2, vec3);
                point[0] += vec3[0];
                point[1] += vec3[1];
                point[2] += vec3[2];
                UF_CURVE_create_point (point, &point_tag);
                UF_PARAM_set_int_value (rough_eid, UF_PARAM_START_STATUS, 1);
                UF_PARAM_set_tag_value (rough_eid, UF_PARAM_START_POINT, point_tag);
                UF_PARAM_set_int_value (rough_eid, UF_PARAM_START_METHOD,
                                        UF_PARAM_turn_start_method_axial_then_radial);
                UF_PARAM_set_int_value (rough_eid, UF_PARAM_RETURN_STATUS, 1);
                UF_PARAM_set_int_value (rough_eid, UF_PARAM_RETURN_METHOD,
                                        UF_PARAM_turn_return_method_clear_radial_only);
                UF_PARAM_set_int_value (rough_eid, UF_PARAM_TURN_CLEAR_RADIAL_TOG, 1);
/*
 * map radial clearance to absolute coordinate system
 */
                pnt2[0] = 0.0;
                pnt2[1] = (blank_diameter / 2.0) + (CLEARANCE_FACTOR * insert_length);
                UF_TURN_map_pnt2_to_acs (NULL_TAG, pnt2, point);
                UF_CURVE_create_point (point, &point_tag);
                UF_PARAM_set_tag_value (rough_eid, UF_PARAM_TURN_CLEAR_RADIAL_TAG, point_tag);

                UF_PARAM_generate (rough_eid, &ret_val);
                last_eid = rough_eid;
                sprintf (mess_buf, "generate roughing oper for region %d\n", sort_arr[i]+1);
                UF_UI_write_listing_window (mess_buf);
                UF_OPER_create ("turning", "ROUGH_TURN_OD", &rough_eid);
/*
 * set reversal mode back to as_level
 */
                UF_PARAM_set_int_value (rough_eid, UF_PARAM_TURN_REVERSAL_MODE,
                                        UF_PARAM_turn_reversal_mode_as_level);
/*
 * add tool and workpiece to operation
 */
                UF_NCGROUP_accept_member (tool_eid, rough_eid);
                UF_NCGROUP_accept_member (workp_tag, rough_eid);
            }
        }
/*
 * delete last operation and create empty operation for grooving level
 */
        UF_OBJ_delete_object (rough_eid);
        UF_OPER_create ("turning", "GROOVE_OD", &groove_eid);
/*
 * create grooving tool for second level
 */
        UF_CUTTER_create ("turning", "OD_GROOVE_L", &tool_eid);
/*
 * set insert width, left and right corner radius
 */
        UF_PARAM_set_double_value (tool_eid, UF_PARAM_TL_INSERT_WIDTH, 0.2);
        UF_PARAM_set_double_value (tool_eid, UF_PARAM_TL_LEFT_COR_RAD, 0.06);
        UF_PARAM_set_double_value (tool_eid, UF_PARAM_TL_RIGHT_COR_RAD, 0.06);
/*
 * add tool to machine and operation, add operation to workpiece
 */
        UF_NCGROUP_accept_member (mct_root, tool_eid);
        UF_NCGROUP_accept_member (tool_eid, groove_eid);
        UF_NCGROUP_accept_member (workp_tag, groove_eid);
/*
 * ask number of cut regions after second level roughing operation
 */
        UF_TURN_ask_cut_regions_exist (groove_eid, &num_regs, &size, &loc, &mess);
        sprintf (mess_buf, "Number of cut regions found after first level roughing oper: %d\n", num_regs);
        UF_UI_write_listing_window (mess_buf);
        sprintf (mess_buf, "Total size of cut regions: %f\n", size);
        UF_UI_write_listing_window (mess_buf);
/*
 * analyse size of cut regions
 */
        for (i=0;i<num_regs;i++)
        {
            UF_TURN_ask_cut_region_of_index (groove_eid, i+1, &size_arr[i], point_arr[i], &exi, &mess);
            sprintf (mess_buf, "Size of cut region %d: %f\n", i+1, size_arr[i]);
            UF_UI_write_listing_window (mess_buf);
/*
 * map acs coordinates to spindle coordinates
 */
            UF_TURN_map_pnt3_from_acs (NULL_TAG, point_arr[i], point_arr2[i]);
            sprintf (mess_buf, "X -Coordinate of region %d: %f\n", i+1, point_arr2[i][0]);
            UF_UI_write_listing_window (mess_buf);
        }
/*
 * sort cut regions beginning with greatest X-coordinate
 */
        sort_flag = TRUE;
        for (i=0;i<num_regs;i++)
        {
            sort_arr[i] = i;
        }
        while (sort_flag)
        {
            sort_flag = FALSE;
            for (i=0;i<num_regs-1;i++)
            {
                if(point_arr2[sort_arr[i]][0] < point_arr2[sort_arr[i+1]][0])
                {
                    isort = sort_arr[i];
                    sort_arr[i] = sort_arr[i+1];
                    sort_arr[i+1] = isort;
                    sort_flag = TRUE;
                }
            }
        }
/*
 * generate grooving operations for larger cut regions
 */
        UF_PARAM_ask_double_value (tool_eid, UF_PARAM_TL_INSERT_LENGTH,
                                   &insert_length);
        UF_PARAM_ask_double_value (tool_eid, UF_PARAM_TL_INSERT_WIDTH,
                                   &insert_width);
        cutter_size = insert_length * insert_width;
        sprintf (mess_buf, "grooving cutter size: %f\n", cutter_size);
        UF_UI_write_listing_window (mess_buf);
        
        for (i=0;i<num_regs;i++)
        {
            if (size_arr[sort_arr[i]] > cutter_size * 20.)
            {
                UF_PARAM_set_int_value (groove_eid, UF_PARAM_TROPR_CUT_STRATEGY,
                                        UF_PARAM_tropr_cut_strategy_level_zig_zag);
/*
 * set display speed
 */
                UF_PARAM_ask_subobj_ptr_value (groove_eid, UF_PARAM_DISP_PATH, disp_ptr);
                disp_ptr->speed = 10;
                UF_PARAM_set_subobj_ptr_value (groove_eid, UF_PARAM_DISP_PATH, disp_ptr);
/*
 * set cut control save distance, cleanup off, minimum clearance from diameter
 */
                UF_PARAM_set_double_value (groove_eid, UF_PARAM_TURN_SAFE_DISTANCE, 0.0);
                UF_PARAM_set_int_value (groove_eid, UF_PARAM_TURN_CLEANUP,
                                        UF_PARAM_turn_cleanup_none);
                UF_PARAM_set_double_value (groove_eid, UF_PARAM_TURN_FROM_DIA, 0.0);
/*
 * set rough stock 0.03, profile stock 0.0, additional profiling on, down only profiling
 */
                UF_PARAM_set_double_value (groove_eid, UF_PARAM_STOCK_PART, 0.03);
                UF_PARAM_set_double_value (groove_eid, UF_PARAM_TURN_STOCK_F_EQUI, 0.0);
                UF_PARAM_set_int_value (groove_eid, UF_PARAM_TURN_PROFILING, 1);
                UF_PARAM_set_int_value (groove_eid, UF_PARAM_TFOPR_CUT_STRATEGY,
                                        UF_PARAM_tfopr_cut_strategy_down_only);
/*
 * set cut region selection point and generate operation
 */
                UF_CURVE_create_point (point_arr[sort_arr[i]], &point_tag);
                UF_PARAM_set_int_value (groove_eid, UF_PARAM_TURN_CUT_REG_SELECT_TOG, 1);
                UF_PARAM_set_tag_value (groove_eid, UF_PARAM_TURN_CUT_REG_SELECT_TAG,
                                        point_tag);
/*
 * set start point to cut region selection point + offset
 * set return point method to clear radial, set radial clearance
 */
                point[0] = point_arr[sort_arr[i]][0];
                point[1] = point_arr[sort_arr[i]][1];
                point[2] = point_arr[sort_arr[i]][2];
                UF_PARAM_ask_double_value (tool_eid, UF_PARAM_TL_INSERT_LENGTH,
                                           &insert_length);
/*
 * map offset to absolute coordinate system
 */
                vec2[0] = 0.0;
                vec2[1] = CLEARANCE_FACTOR * insert_length;
                UF_TURN_map_vec2_to_acs (NULL_TAG, vec2, vec3);
                point[0] += vec3[0];
                point[1] += vec3[1];
                point[2] += vec3[2];
                UF_CURVE_create_point (point, &point_tag);
                UF_PARAM_set_int_value (groove_eid, UF_PARAM_START_STATUS, 1);
                UF_PARAM_set_tag_value (groove_eid, UF_PARAM_START_POINT, point_tag);
                UF_PARAM_set_int_value (groove_eid, UF_PARAM_START_METHOD,
                                        UF_PARAM_turn_start_method_axial_then_radial);
                UF_PARAM_set_int_value (groove_eid, UF_PARAM_RETURN_STATUS, 1);
                UF_PARAM_set_int_value (groove_eid, UF_PARAM_RETURN_METHOD,
                                        UF_PARAM_turn_return_method_clear_radial_only);
                UF_PARAM_set_int_value (groove_eid, UF_PARAM_TURN_CLEAR_RADIAL_TOG, 1);
/*
 * map radial clearance to absolute coordinate system
 */
                pnt2[0] = 0.0;
                pnt2[1] = (blank_diameter / 2.0) + (CLEARANCE_FACTOR * insert_length);
                UF_TURN_map_pnt2_to_acs (NULL_TAG, pnt2, point);
                UF_CURVE_create_point (point, &point_tag);
                UF_PARAM_set_tag_value (groove_eid, UF_PARAM_TURN_CLEAR_RADIAL_TAG, point_tag);

                UF_PARAM_generate (groove_eid, &ret_val);
                last_eid = groove_eid;
                sprintf (mess_buf, "generate grooving oper for region %d\n", sort_arr[i]+1);
                UF_UI_write_listing_window (mess_buf);
                UF_OPER_create ("turning", "GROOVE_OD", &groove_eid);
/*
 * add tool and workpiece to subsequent operation
 */
                UF_NCGROUP_accept_member (tool_eid, groove_eid);
                UF_NCGROUP_accept_member (workp_tag, groove_eid);
            }
        }       
/*
 * generate grooving operations for smaller cut regions     
 */
        for (i=0;i<num_regs;i++)
        {
            if (size_arr[sort_arr[i]] <= cutter_size * 20.)
            {
                UF_PARAM_set_int_value (groove_eid, UF_PARAM_TROPR_CUT_STRATEGY,
                                        UF_PARAM_tropr_cut_strategy_plunge_zig_zag);
/*
 * set display speed
 */
                UF_PARAM_ask_subobj_ptr_value (groove_eid, UF_PARAM_DISP_PATH, disp_ptr);
                disp_ptr->speed = 10;
                UF_PARAM_set_subobj_ptr_value (groove_eid, UF_PARAM_DISP_PATH, disp_ptr);
/*
 * set cleanup off, additional profiling on, normal and shallow corner control to clear
 */
                UF_PARAM_set_int_value (groove_eid, UF_PARAM_TURN_CLEANUP,
                                        UF_PARAM_turn_cleanup_none);
                UF_PARAM_set_int_value (groove_eid, UF_PARAM_TURN_PROFILING, 1);
                UF_PARAM_set_int_value (groove_eid, UF_PARAM_TURN_NORMAL_TYPE,
                                        UF_PARAM_turn_corner_ctrl_extend_tang);
                UF_PARAM_set_int_value (groove_eid, UF_PARAM_TURN_SHALLOW_TYPE,
                                        UF_PARAM_turn_corner_ctrl_extend_tang);
/*
 * set cut region selection point and generate operation
 */
                UF_CURVE_create_point (point_arr[sort_arr[i]], &point_tag);
                UF_PARAM_set_int_value (groove_eid, UF_PARAM_TURN_CUT_REG_SELECT_TOG, 1);
                UF_PARAM_set_tag_value (groove_eid, UF_PARAM_TURN_CUT_REG_SELECT_TAG,
                                        point_tag);
/*
 * set start point to cut region selection point + offset
 * set return point method to clear radial, set radial clearance
 */
                point[0] = point_arr[sort_arr[i]][0];
                point[1] = point_arr[sort_arr[i]][1];
                point[2] = point_arr[sort_arr[i]][2];
                UF_PARAM_ask_double_value (tool_eid, UF_PARAM_TL_INSERT_LENGTH,
                                           &insert_length);
/*
 * map offset to absolute coordinate system
 */
                vec2[0] = 0.0;
                vec2[1] = CLEARANCE_FACTOR * insert_length;
                UF_TURN_map_vec2_to_acs (NULL_TAG, vec2, vec3);
                point[0] += vec3[0];
                point[1] += vec3[1];
                point[2] += vec3[2];
                UF_CURVE_create_point (point, &point_tag);
                UF_PARAM_set_int_value (groove_eid, UF_PARAM_START_STATUS, 1);
                UF_PARAM_set_tag_value (groove_eid, UF_PARAM_START_POINT, point_tag);
                UF_PARAM_set_int_value (groove_eid, UF_PARAM_START_METHOD,
                                        UF_PARAM_turn_start_method_axial_then_radial);
                UF_PARAM_set_int_value (groove_eid, UF_PARAM_RETURN_STATUS, 1);
                UF_PARAM_set_int_value (groove_eid, UF_PARAM_RETURN_METHOD,
                                        UF_PARAM_turn_return_method_clear_radial_only);
                UF_PARAM_set_int_value (groove_eid, UF_PARAM_TURN_CLEAR_RADIAL_TOG, 1);
/*
 * map radial clearance to absolute coordinate system
 */
                pnt2[0] = 0.0;
                pnt2[1] = (blank_diameter / 2.0) + (CLEARANCE_FACTOR * insert_length);
                UF_TURN_map_pnt2_to_acs (NULL_TAG, pnt2, point);
                UF_CURVE_create_point (point, &point_tag);
                UF_PARAM_set_tag_value (groove_eid, UF_PARAM_TURN_CLEAR_RADIAL_TAG, point_tag);
/*
 * generate operation
 */
                UF_PARAM_generate (groove_eid, &ret_val);
                last_eid = groove_eid;
                sprintf (mess_buf, "generate grooving oper for region %d\n", sort_arr[i]+1);
                UF_UI_write_listing_window (mess_buf);
                UF_OPER_create ("turning", "GROOVE_OD", &groove_eid);
/*
 * add tool and workpiece to operation
 */
                UF_NCGROUP_accept_member (tool_eid, groove_eid);
                UF_NCGROUP_accept_member (workp_tag, groove_eid);
            }
        }
/*
 * generate max min box of In Process Workpiece
 */
        sprintf (mess_buf, "generate bounding box for 2D In Process Workpiece\n");
        UF_UI_write_listing_window (mess_buf);
        return_value = UF_TURN_ipw_box (last_eid, &length, &diameter, bottom_left_scs, top_right_scs,
                                        bottom_left, bottom_right, top_left, top_right, &mess);
        if (return_value != 0) UF_get_fail_message (return_value, buffer);
        curve_ptr->start_point[0] = bottom_left[0];
        curve_ptr->start_point[1] = bottom_left[1];
        curve_ptr->start_point[2] = bottom_left[2];
        curve_ptr->end_point[0] = bottom_right[0];
        curve_ptr->end_point[1] = bottom_right[1];
        curve_ptr->end_point[2] = bottom_right[2];
        UF_CURVE_create_line (curve_ptr, &edge1);
        curve_ptr->start_point[0] = bottom_right[0];
        curve_ptr->start_point[1] = bottom_right[1];
        curve_ptr->start_point[2] = bottom_right[2];
        curve_ptr->end_point[0] = top_right[0];
        curve_ptr->end_point[1] = top_right[1];
        curve_ptr->end_point[2] = top_right[2];
        UF_CURVE_create_line (curve_ptr, &edge2);
        curve_ptr->start_point[0] = top_right[0];
        curve_ptr->start_point[1] = top_right[1];
        curve_ptr->start_point[2] = top_right[2];
        curve_ptr->end_point[0] = top_left[0];
        curve_ptr->end_point[1] = top_left[1];
        curve_ptr->end_point[2] = top_left[2];
        UF_CURVE_create_line (curve_ptr, &edge3);
        curve_ptr->start_point[0] = top_left[0];
        curve_ptr->start_point[1] = top_left[1];
        curve_ptr->start_point[2] = top_left[2];
        curve_ptr->end_point[0] = bottom_left[0];
        curve_ptr->end_point[1] = bottom_left[1];
        curve_ptr->end_point[2] = bottom_left[2];
        UF_CURVE_create_line (curve_ptr, &edge4);
/*
 * save In Process Workpiece as partfile
 * caution: file ipw_part.prt must not yet exist; otherwise ipw cannot be saved to disk.
 */
        sprintf (mess_buf, "save resulting In Process Workpiece\n");
        UF_UI_write_listing_window (mess_buf);
        UF_TURN_save_spinning_ipw_as_part (last_eid, "ipw_part", &mess);
/*
 * delete last operation
 */
        UF_OBJ_delete_object (groove_eid);
/*
 * start post processor
 */
        sprintf (mess_buf, "generate NC program using postprocessor event handler file LATHE_2_AXIS_TOOL_TIP\n");
        UF_UI_write_listing_window (mess_buf);
        return_value = UF_SETUP_generate_program (setup_tag, mct_root, "LATHE_2_AXIS_TOOL_TIP",
                                                  "auto_nc", UF_SETUP_OUTPUT_UNITS_INCH);
        if (return_value != 0) UF_get_fail_message (return_value, buffer);
    }
    
    return;
}



/*ARGSUSED*/
extern DllExport void ufusr(char *param, int *retcode, int param_len)
{
    UF_initialize();

    do_create_turning_oper_api();

    UF_terminate();
}

int ufusr_ask_unload(void)
{
 return (UF_UNLOAD_IMMEDIATELY);
}

