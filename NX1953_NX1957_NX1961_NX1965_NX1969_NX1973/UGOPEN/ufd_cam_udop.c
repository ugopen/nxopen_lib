/*===================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===================================================================*/

/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the udop entry point in the following      *
 *   UG/Open API program which uses functions from the following modules:     *
 *                                                                            *
 *   UF_CAM, UF_UDOP, UF_OPER, and UF_PATH                                    *
 *                                                                            *
 * PROGRAM DESCRIPTION -                                                      *
 *   To use this example program you must define a logical/environment        *
 *   variable to point to the shared library you created for this program.    *
 *   You must have a part open to run the example. For further information,   *
 *   see the "User Defined Operations" chapter of the Manufacturing User      *
 *   manual.
 *                                                                            *
              
 *                                                                            *
 ******************************************************************************/

#include <uf_defs.h>
#include <uf_cam.h>
#include <uf_udop.h>
#include <uf_oper.h>
#include <uf_path.h>
#include <uf.h>
#include <uf_exit.h>
#include <stdio.h>


/******************************************************************
  Internal user function to use the USER DEFINED operation
  The entry point name : udop
******************************************************************/
/*ARGSUSED*/
extern void udop(char *param, int *status, int parm_len)
{
  char   op_name[UF_OPER_OPNAME_BUFSIZE];
  UF_UDOP_id_t        udop_id;
  UF_UDOP_purpose_t    purpose;
  UF_OPER_id_t        oper_id;
  UF_PATH_id_t        path_id;
/***** Convert UG/Open API param to CAM exit id ******/
  UF_CAM_exit_id_t    exit_id = (UF_CAM_exit_id_t)param;
/***** Using the exit_id to get the udop identifier ******/
  UF_initialize();
  UF_UDOP_ask_udop( exit_id, &udop_id);
/***** Using the udop_id to get the oper identifier ******/
  UF_UDOP_ask_oper( udop_id, &oper_id);
/***** Using the udop_id to get the pupose of the call ******/
  UF_UDOP_ask_purpose( udop_id, &purpose);
/***** Using the oper_id to get the name of the oper ******/
  UF_OPER_ask_name( oper_id, op_name);
/***** Using the oper_id to get the path identifier ******/
  UF_OPER_ask_path( oper_id, &path_id);
  if( purpose == UF_UDOP_GENERATE )
  {
      
    /************  To input GOTO/ motion*************/
     {
      UF_PATH_linear_motion_t    motion,*motion_ptr = &motion;
      motion_ptr->feed_value = 0.0;
      motion_ptr->feed_unit = UF_PATH_FEED_UNIT_NONE;
      motion_ptr->type = UF_PATH_MOTION_TYPE_CUT;
      motion_ptr->tool_axis[0] =0.0;
      motion_ptr->tool_axis[1] =0.0;
      motion_ptr->tool_axis[2] =1.0;
        
      motion_ptr->position[0] =0.0;
      motion_ptr->position[1] =0.5;
      motion_ptr->position[2] =0.0;
      UF_PATH_create_linear_motion( path_id, motion_ptr);
     }
    /************  To input CIRCLE/ motion*************/
     {
      UF_PATH_circular_motion_t  cir_motion,
                         *cir_motion_ptr = &cir_motion;
      cir_motion_ptr->feed_value = 0.0;
      cir_motion_ptr->feed_unit = UF_PATH_FEED_UNIT_NONE;
      cir_motion_ptr->type = UF_PATH_MOTION_TYPE_CUT;
      cir_motion_ptr->start_tool_axis[0] =0.0;
      cir_motion_ptr->start_tool_axis[1] =0.0;
      cir_motion_ptr->start_tool_axis[2] =1.0;
      cir_motion_ptr->end_tool_axis[0] =0.0;
      cir_motion_ptr->end_tool_axis[1] =0.0;
      cir_motion_ptr->end_tool_axis[2] =1.0;
      cir_motion_ptr->start[0] = 0.0;
      cir_motion_ptr->start[1] = 0.5;
      cir_motion_ptr->start[2] = 0.0;
      cir_motion_ptr->arc_axis[0] = 0.0;
      cir_motion_ptr->arc_axis[1] = 0.0;
      cir_motion_ptr->arc_axis[2] = 1.0;
      cir_motion_ptr->arc_center[0] = 0.5;
      cir_motion_ptr->arc_center[1] = 0.5;
      cir_motion_ptr->arc_center[2] = 0.0;
      cir_motion_ptr->arc_radius = 0.5;
      cir_motion_ptr->tolerance = 0.01;
      cir_motion_ptr->shape = UF_PATH_SHAPE_CIRCULAR_CCW;
      cir_motion_ptr->material_side = UF_PATH_SIDE_RIGHT;
      cir_motion_ptr->end[0] = 0.5;
      cir_motion_ptr->end[1] = 0.0;
      cir_motion_ptr->end[2] = 0.0;
    UF_PATH_create_circular_motion( path_id, cir_motion_ptr);
     }
    /************  To input User Defined Text *************/
    {
     UF_PATH_create_text( path_id, "User Defined Text" );
    }
    /************  To input PPRINTS *************/
    {
     UF_PATH_create_pprint( path_id, "Text for pprint" );
    }
   /************  To input Opmessage *************/
    {
     UF_PATH_create_opmessage( path_id, 
                        "Any messages for the operator" );
    }
   /************  To input origin post command *************/
    {
     double  origin_coordinates[3];
     char    appended_text[] = {"Appended Text"};
     origin_coordinates[0] = 0.0;
     origin_coordinates[1] = 0.0;
     origin_coordinates[2] = 0.0;
     UF_PATH_create_origin( path_id, origin_coordinates,
                     appended_text );
    }
   /************  To input SEQNO/ post command *************/
    { 
     UF_PATH_seqno_t  seq_type = UF_PATH_SEQNO_N;
     int              seq_number = 1;
     int              seq_incr = 2;
     int              seq_freq = 3;
     UF_PATH_create_seqno( path_id, seq_type, seq_number, 
                     seq_incr, seq_freq, NULL );
     }
      /************  To input SET/ post command *************/
     { 
      UF_PATH_output_mode_t     
        output_mode =  UF_PATH_OUTPUT_MODE_ABSOLUTE;
      UF_PATH_feedrate_mode_t   
        feedrate_mode = UF_PATH_FEEDRATE_OUTPUT_IPM;
      UF_PATH_arc_mode_t        arc_mode = UF_PATH_ARC_LINEAR;
      UF_PATH_parallel_mode_t   
        parallel_mode = UF_PATH_PARALLEL_ZAXIS;
      UF_PATH_machine_mode_t   machine_mode = UF_PATH_MACHINE_MILL;
      UF_PATH_create_set_mode( path_id, output_mode, feedrate_mode,
                     arc_mode,  parallel_mode, machine_mode,
                     NULL );
      }
    /************  To input SELECT/HEAD post command *************/
      {
       UF_PATH_head_type_t head_type = UF_PATH_HEADTYPE_NONE; 
       UF_PATH_create_select_head( path_id, head_type, NULL );
      }
    /********  To input LOAD/TOOL or TURRET/ post command ********/
      {
       UF_PATH_tool_change_t tool_change_data;
       tool_change_data.xoffset_value = 0.0;
       tool_change_data.yoffset_value = 0.0;
       tool_change_data.zoffset_value = 1.0;
       tool_change_data.tool_number = 1;
       tool_change_data.adjust_register = 2;
       tool_change_data.head_type = UF_PATH_HEADTYPE_NONE;
       tool_change_data.adjust_flag = TRUE;
       tool_change_data.tool_offset_flag = TRUE;
       tool_change_data.tool_number_flag = TRUE;
     /**** if TRUE the values of tool_angle and radius must be 
        specified ****/
       tool_change_data.tool_angle_radius_flag = FALSE;
    /*** if TRUE outputs the string MANUAL in the post command ***/
       tool_change_data.manual_change_flag = TRUE;
       UF_PATH_create_tool_change( path_id, &tool_change_data, 
                           NULL );
       }
      /*******  To input TRACKING POINT CHANGE post command **********/
      {
         UF_PATH_tracking_point_change_t tracking_point_change_data;

         tracking_point_change_data.xoff = 0.0;
         tracking_point_change_data.yoff = 0.0;
         tracking_point_change_data.adjust_register = 0;
         tracking_point_change_data.cutcom_register = 0;

         UF_PATH_create_tracking_point_change( path_id, &tracking_point_change_data );
      }

      /************  To input SPINDLE/ post command *************/
      {
       UF_PATH_spindle_on_t spindle_data;
       spindle_data.speed = 200.0;
       spindle_data.maxrpm = 1000.0;
       spindle_data.mode = UF_PATH_SPINDLE_MODE_RPM;
       spindle_data.direction = UF_PATH_DIRECTION_CLOCKWISE;
       spindle_data.speed_flag = TRUE;
       spindle_data.maxrpm_flag = TRUE;
       spindle_data.range_flag = FALSE;
       UF_PATH_create_spindle_on( path_id, &spindle_data, NULL );
       }
      /************  To input SPINDLE/OFF post command *************/
       {
        UF_PATH_create_spindle_off( path_id, NULL );
       }
      /************  To input SPINDLE/REVERSE post command *************/
       {
        UF_PATH_create_spindle_reverse( path_id, NULL );
       }
      /************  To input COOLNT/ post command *************/
       {
        UF_PATH_coolant_type_t   
            coolant_type = UF_PATH_COOLANT_TYPE_ON;
        UF_PATH_create_coolant_on( path_id, coolant_type, NULL );
       }
      /**********  To input COOLNT/OFF post command ***********/
       {
        UF_PATH_create_coolant_off( path_id, NULL );
       }
      /************  To input OPSTOP post command *************/
       {
        UF_PATH_create_op_stop( path_id, NULL );
       }
      /************  To input OPSKIP/ post command *************/
       {
        UF_PATH_op_skip_t  op_skip_option = UF_PATH_OP_SKIP_ON;
        UF_PATH_create_op_skip( path_id, op_skip_option, NULL );
       }
      /************  To input STOP post command *************/
       {
        UF_PATH_create_stop( path_id, NULL );
       }
      /************  To input DELAY/ post command *************/
       {
        double               delay_value = 5.0;
        UF_PATH_dwell_unit_t delay_unit = UF_PATH_DWELL_SECONDS;
        UF_PATH_create_dwell( path_id, delay_value, delay_unit, 
                       NULL );
       }
      /************  To input AUXFUN/ post command *************/
       {
        int               auxfun = 1;
        UF_PATH_create_auxfun( path_id, auxfun, NULL );
       }
      /************  To input PREFUN/ post command *************/
       {
        int               prefun = 1;
        UF_PATH_create_prefun( path_id, prefun, NULL );
     }
        /************  To input CLAMP/ post command *************/
     {
        UF_PATH_clamp_status_t   
            clamp_status = UF_PATH_CLAMP_AXIS_ON;
        UF_PATH_axis_t           axis_type = UF_PATH_XAXIS;
        UF_PATH_create_clamp( path_id, clamp_status, axis_type, 
                       NULL );
       }
      /**********  To input TOOL/SELECT post command ***********/
       { 
        int   tool_number = 2;
      UF_PATH_create_tool_preselect( path_id, tool_number, NULL );
      }
    /************  To input ADJUST/ post command *************/
      { 
        int comp_register = 2;
        UF_PATH_create_tool_length_comp( path_id, comp_register, 
                               NULL );
      }
    /************  To input ROTATE/ post command *************/
     { 
      UF_PATH_rotate_t rotate_data;
      
      rotate_data.rotation_angle = 45.0;
      rotate_data.rotation_object = UF_PATH_ROTATION_OBJECT_TABLE;
      rotate_data.rotation_type = UF_PATH_ROTATION_ABSOLUTE;
      rotate_data.rotation_direction = UF_PATH_DIRECTION_CLOCKWISE;
      rotate_data.angle_flag = TRUE;
      rotate_data.rotref_flag = FALSE;
      UF_PATH_create_rotate( path_id, &rotate_data, NULL );
     }
    /************  To input LOAD/WIRE post command *************/
     { 
      UF_PATH_create_thread_wire( path_id, NULL );
     }
    /************  To input UNLOAD/WIRE post command *************/
     { 
      UF_PATH_create_cut_wire( path_id, NULL );
     }
      /************  To input FLUSH/ post command *************/
     {
      UF_PATH_flush_t flush_data;
      flush_data.flush_type = UF_PATH_FLUSH_ON;
      flush_data.flushing_guide =  UF_PATH_GUIDE_UPPER;
      flush_data.flushing_pressure = UF_PATH_PRESSURE_LOW;
      flush_data.flush_register = TRUE;
      flush_data.guide_flag = TRUE;
      flush_data.pressure_flag = TRUE;
      UF_PATH_create_flush( path_id, &flush_data, NULL );
     }
    /************  To input FLUSH/IN post command *************/
     { 
      UF_PATH_tank_type_t type = UF_PATH_TANK_IN;
      UF_PATH_create_flush_tank( path_id, type, NULL );
     }
      /************  To input POWER/ post command *************/
     { 
      double power = 2.0;
      UF_PATH_create_power( path_id, power, NULL );
     }
    /************  To input SET/UPPER post command *************/
     { 
      UF_PATH_create_wire_guides( path_id, NULL );
     }
    /************  To input FEDRAT/ post command *************/
     { 
      double feed_rate_value = 2.0;
      UF_PATH_create_fedrat( path_id, feed_rate_value, NULL );
     }
    /************  To input STAN/ post command *************/
     { 
      double  slope_value = 2.0;
      double  angle_value = 0.0;
      logical angle_flag = FALSE;
      UF_PATH_create_wire_angle( path_id, slope_value, angle_value,
                                 angle_flag, NULL );
     }
    /************  To input CUTCOM/ post command *************/
     { 
      UF_PATH_cutcom_mode_t  mode = UF_PATH_CUTCOM_ON;
      int                    adjust_register = 2;
      logical                cutcom_off_flag = FALSE;
      logical                adjust_flag = TRUE;
      UF_PATH_create_wire_cutcom( path_id, mode, adjust_register, 
                              cutcom_off_flag, adjust_flag, NULL );
     }
      /************  To input CUTCOM/ post command *************/
     { 
      UF_PATH_cutcom_t  cutcom_data;
      cutcom_data.cutcom_mode = UF_PATH_CUTCOM_ON;
      cutcom_data.plane_type = UF_PATH_PLANE_TYPE_XY;
      cutcom_data.cutcom_on_status = 
        UF_PATH_CUTCOM_ON_BEFORE_ENGAGE;
      cutcom_data.cutcom_off_status = 
        UF_PATH_CUTCOM_OFF_AFTER_RETRACT;
      cutcom_data.adjust_register = 2;
      cutcom_data.full_cutcom_output = TRUE;
      cutcom_data.adjust_flag = TRUE;
      UF_PATH_create_cutcom( path_id, &cutcom_data, NULL ); 
     }
      UF_PATH_end_tool_path( path_id ); 
   }
  UF_terminate();
}
