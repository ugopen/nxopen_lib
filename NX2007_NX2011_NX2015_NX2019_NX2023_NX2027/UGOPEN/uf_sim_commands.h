/*******************************************************************************
 *            Copyright (c) 1998-2000 Unigraphics Solutions, Inc.
 *                      Unpublished - All Rights Reserved
 * File Name: uf_sim_commands.h
 *
 * 
 *
 * File description:
 *    This file contains the prototypes for the Simulation and Verification
 *    (S&V) commands. Those commands create simulation events that control
 *    the simulation of the machine tool.
 *
 *    One of the applications for those commands is an NC-Controller
 *    plugin that could call those commands to simulate the machine
 *    tool behavior (motion, mounting, feedback,...) according
 *    the NC-program code (e.g. G codes).
 *
 *    The functions in this file allow the following:
 *    o Move machine tool linear and rotary axis
 *    o Mount/unmount tool
 *    o Mount/unmount kinematics component
 *    o Set machine tool parameter
 *    o Issue feedback
 *
 ******************************************************************************/

#ifndef UF_SIM_COMMANDS_H_INCLUDED
#define UF_SIM_COMMANDS_H_INCLUDED

/*************************** Include Files ************************************/
#include <uf.h>
#include <uf_defs.h>
#include <uf_sim.h>
#include <uf_mom.h>
#include <uf_obj_types.h>
#include <libufun_cam_exports.h>

/******************************** Defines *************************************/

#ifdef __cplusplus
extern "C" {
#endif

/***************************** Public Typedefs ********************************/


/************************* Public Function Definitions ************************/

/*******************************************************************************
 * Returns the object id of the simulation engine that is linked to MOM object.
 *
 * Environment: Internal  and  External
 * See Also:
 * History: Originally released in NX2
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_SIM_ask_sim_engine
(
   UF_MOM_id_t          mom_id,      /* <I> - the MOM object ID     */
   UF_SIM_engine_p_t   *engine_id    /* <O> - the simulation engine */
);


/*******************************************************************************
 * Mount a specified component (source component) with a given coordinate
 * system (source junction) of the machine tool KIM model at a specified
 * location (destination component and destination junction).
 *
 * Environment: Internal  and  External
 * See Also:
 * History: Released in NX2
 ******************************************************************************/
extern UFUN_CAMEXPORT int UF_SIM_mount_kim_comp
(
   UF_SIM_engine_p_t engine,        /* <I> - the simulation engine object     */
   char*          source_comp,      /* <I> - the name of the source component */
   char*          source_jct,       /* <I> - the name of the source junction  */
   char*          destination_comp, /* <I> - the name of the destination cmp  */
   char*          destination_jct,  /* <I> - the name of the destination jct  */
   double         duration          /* <I> - the time in seconds to complete
                                             this mount on the machine tool   */
);


/*******************************************************************************
 * Un-mount a specified component (source component).
 *
 * Environment: Internal  and  External
 * See Also:
 * History: Released in NX2
 ******************************************************************************/
extern UFUN_CAMEXPORT int UF_SIM_unmount_kim_comp
(
   UF_SIM_engine_p_t engine,    /* <I> - the simulation engine object         */
   char*             component, /* <I> - the name of the component to un-mount*/
   double            duration   /* <I> - the time in seconds to complete
                                         this un-mount on the machine tool    */
);


/*******************************************************************************
 * Mount a specified tool by its tool_id on a specified component (destination
 * component and destination junction). The tool can be specified by different
 * classification types.
 *
 * Environment: Internal  and  External
 * See Also:
 * History: Released in NX2
 ******************************************************************************/
extern UFUN_CAMEXPORT int UF_SIM_mount_tool
(
   UF_SIM_engine_p_t engine,           /* <I> - the simulation engine object  */
   UF_SIM_tool_class_t  tool_class,    /* <I> - tool classification identifier*/
   char*             tool_id,          /* <I> - the tool_id of the tool       */
   char*             destination_comp, /* <I> - the name of the destin. cmp   */
   char*             destination_jct,  /* <I> - the name of the destin. jct   */
   double            duration,         /* <I> - time in seconds to complete
                                                this mount on the machine tool */
   char              tool_name[UF_OBJ_NAME_BUFSIZE]         /* <O> - name of the tool              */
);


/*******************************************************************************
 * Un-mount the tool.
 *
 * Environment: Internal  and  External
 * See Also:
 * History: Released in NX2
 ******************************************************************************/
extern UFUN_CAMEXPORT int UF_SIM_unmount_tool
(
   UF_SIM_engine_p_t engine,       /* <I> - the simulation engine object      */
   char*             tool_name,    /* <I> - the name of the tool to un-mount  */
   double            duration      /* <I> - the time in seconds to complete
                                            this un-mount on the machine tool */
);


/*******************************************************************************
 * Move the specified linear axis by the specified amount.
 *
 * Environment: Internal  and  External
 * See Also:
 * History: Released in NX2
 ******************************************************************************/
extern UFUN_CAMEXPORT int UF_SIM_move_linear_axis
(
   UF_SIM_engine_p_t engine_id,  /* <I> - the simulation engine object        */
   char*             axis,       /* <I> - the name of the linear NC-axis      */
   double            value,      /* <I> - the new position of the axis        */
   double            duration    /* <I> - the time in seconds to complete
                                          this move on the machine. This
                                          value is effected by the current
                                          feed rate.                          */
);


/*******************************************************************************
 * Move the specified rotary axis by the specified amount.
 *
 * Environment: Internal  and  External
 * See Also:
 * History: Released in NX2
 ******************************************************************************/
extern UFUN_CAMEXPORT int UF_SIM_move_rotary_axis
(
   UF_SIM_engine_p_t engine_id, /* <I> - the simulation engine object         */
   char*             axis,      /* <I> - the name of the linear NC-axis       */
   double            value,     /* <I> - the new position of the axis         */
   double            duration   /* <I> - the time in seconds to complete
                                         this move on the machine. This
                                         value is effected by the current
                                         feed rate.                           */
);


/*******************************************************************************
 * Set the given parameter and store the data into the model.
 *
 * Environment: Internal  and  External
 * See Also:
 * History: Released in NX2
 ******************************************************************************/
extern UFUN_CAMEXPORT int UF_SIM_set_parameter
(
   UF_SIM_engine_p_t  engine,  /* <I> - the simulation engine object          */
   char*              label,   /* <I> - the type of the parameter             */
   char*              text,    /* <I> - the value of the parameter            */
   UF_SIM_unit_type_t unit,    /* <I> - the unit of the parameter             */
   double             duration /* <I> - the duration in seconds to complete
                                        this action of the parameter setting  */
);


/*******************************************************************************
 * Issue the specified feedback message.
 *
 * Environment: Internal  and  External
 * See Also:
 * History: Released in NX2
 ******************************************************************************/
extern UFUN_CAMEXPORT int UF_SIM_feedback_message
(
   UF_SIM_engine_p_t engine, /* <I> - the simulation engine object            */
   char*             label,  /* <I> - the type of the feedback message        */
   char*             message /* <I> - the information of the feedback message */
);


/*******************************************************************************
 * Send an update command, which indicates the end of a movement.
 *
 * Environment: Internal  and  External
 * See Also:
 * History: Released in NX2
 ******************************************************************************/
extern UFUN_CAMEXPORT int UF_SIM_update
(
   UF_SIM_engine_p_t engine, /* <I> - the simulation engine object            */
   const char*       label   /* <I> - name of event                           */
);

/*******************************************************************************
 * Create a sub-step event, which indicates the end of an intermediate action.
 * Similar to a step event, all events prior to sub-step event are executed
 * simultaneously.
 *
 * Environment: Internal  and  External
 * See Also:
 * History: Released in NX2
 ******************************************************************************/
extern UFUN_CAMEXPORT int UF_SIM_step
(
   UF_SIM_engine_p_t engine, /* <I> - the simulation engine object            */
   const char*       label   /* <I> - name of event                           */
);


/*******************************************************************************
 * Set the active channel. All following commands write their data into the
 * chosen channel.
 *
 * Environment: Internal  and  External
 * See Also:
 * History: Released in NX2
 ******************************************************************************/
extern UFUN_CAMEXPORT int UF_SIM_set_channel
(
   UF_SIM_engine_p_t engine,        /* <I> - the simulation engine object     */
   int               channel_number /* <I> - the number of the active channel */
);


/*******************************************************************************
 * Initialize the MTD.
 *
 * Environment: Internal  and  External
 * See Also:
 * History: Released in NX2
 ******************************************************************************/
extern UFUN_CAMEXPORT int UF_SIM_mtd_init
(
   UF_SIM_engine_p_t engine   /* <I> - the simulation engine object           */
);


/*******************************************************************************
 * Reset the MTD of the simulation engine.
 *
 * Environment: Internal  and  External
 * See Also:
 * History: Released in NX2
 ******************************************************************************/
extern UFUN_CAMEXPORT int UF_SIM_mtd_reset
(
   UF_SIM_engine_p_t engine   /* <I> - the simulation engine object           */
);


/*******************************************************************************
 * Activate a mounted tool.
 *
 * Environment: Internal  and  External
 * See Also:
 * History: Released in NX2
 ******************************************************************************/
extern UFUN_CAMEXPORT int UF_SIM_activate_tool
(
   UF_SIM_engine_p_t engine,   /* <I> - the simulation engine object          */
   char*             tool_name /* <I> - the name of the tool to activate      */
);


/*******************************************************************************
 * Set the feed rate in the simulation scenario for multiple purposes
 * e.g., display.
 *
 * Environment: Internal  and  External
 * See Also:
 * History: Released in NX2
 ******************************************************************************/
extern UFUN_CAMEXPORT int UF_SIM_set_feed
(
   UF_SIM_engine_p_t  engine,  /* <I> - the simulation engine object          */
   double             value,   /* <I> - the feed rate value                   */
   UF_SIM_unit_type_t unit,    /* <I> - the unit of the feed rate             */
   double             duration /* <I> - the duration in seconds to complete
                                        setting the feed rate                 */
);


/*******************************************************************************
 * Set the speed in the simulation scenario for multiple purposes e.g., display.
 *
 * Environment: Internal  and  External
 * See Also:
 * History: Released in NX2
 ******************************************************************************/
extern UFUN_CAMEXPORT int UF_SIM_set_speed
(
   UF_SIM_engine_p_t  engine,  /* <I> - the simulation engine object          */
   double             value,   /* <I> - the speed value                       */
   UF_SIM_unit_type_t unit,    /* <I> - the unit of the speed                 */
   double             duration /* <I> - the duration in seconds to complete
                                        setting the speed                     */
);


/*******************************************************************************
 * Set the coolant mode in the simulation scenario for multiple purposes
 * e.g., display.
 *
 * Environment: Internal  and  External
 * See Also:
 * History: Released in NX2
 ******************************************************************************/
extern UFUN_CAMEXPORT int UF_SIM_set_coolant
(
   UF_SIM_engine_p_t  engine,   /* <I> - the simulation engine object         */
   int                value,    /* <I> - the value of coolant status
                                         0 is OFF 1 is ON                     */
   double             duration  /* <I> - the duration in seconds to complete
                                         setting the speed                    */
);


/*******************************************************************************
 * Set the cutting mode in the simulation scenario.
 *
 * Environment: Internal  and  External
 * See Also:
 * History: Released in NX2
 ******************************************************************************/
extern UFUN_CAMEXPORT int UF_SIM_set_cutting_mode
(
   UF_SIM_engine_p_t  engine,    /* <I> - the simulation engine object        */
   UF_SIM_cutting_mode_t mode    /* <I> - the cutting mode                    */
);


/*******************************************************************************
 * Request the offset between the two coordinates ACS and MTCS.
 *
 * Environment: Internal  and  External
 * See Also:
 * History: Released in NX2
 ******************************************************************************/
extern UFUN_CAMEXPORT int UF_SIM_transform_offset_acs_to_mtcs
(
   UF_SIM_engine_p_t engine,        /* <I> - simulation engine object         */
   double            acs_vector[3], /* <I> - vector of a c-system             */
   double*           xval,          /* <O> - offset value in x direction      */
   double*           yval,          /* <O> - offset value in y direction      */
   double*           zval           /* <O> - offset value in z direction      */
);


/*******************************************************************************
 * Request the matrix between the two coordinates ACS and MTCS.
 *
 * Environment: Internal  and  External
 * See Also:
 * History: Released in NX2
 ******************************************************************************/
extern UFUN_CAMEXPORT int UF_SIM_transform_matrix_acs_to_mtcs
(
   UF_SIM_engine_p_t engine,        /* <I> - simulation engine object         */
   double            acs_matrix[9], /* <I> - matrix of a c-system             */
   double*           matrix         /* <O> - matrix between ZCS and MTCS      */
);


/*******************************************************************************
 * Request the name of a component of the KIM structure by a given id.
 *
 * Environment: Internal  and  External
 * See Also:
 * History: Released in NX2
 ******************************************************************************/
extern UFUN_CAMEXPORT int UF_SIM_ask_kim_comp_name_by_id
(
   UF_SIM_engine_p_t engine,       /* <I> - simulation engine object          */
   int               system_class, /* <I> - system class of the searched comp */
   char*             comp_id,      /* <I> - the id of the component           */
   char              comp_name[UF_OBJ_NAME_BUFSIZE]     /* <O> - name of the component             */
);


/*******************************************************************************
 * Request the offset values for a given tool.
 *
 * Environment: Internal  and  External
 * See Also:
 * History: Released in NX2
 ******************************************************************************/
extern UFUN_CAMEXPORT int UF_SIM_ask_tool_offsets
(
   UF_SIM_engine_p_t engine,    /* <I> - simulation engine object             */
   char*             tool_name, /* <I> - the name of the tool                 */
   double*           xval,      /* <O> - value in x direction from tool offset*/
   double*           yval,      /* <O> - value in y direction from tool offset*/
   double*           zval       /* <O> - value in z direction from tool offset*/
);



/*******************************************************************************
 * Issue command messages mainly to the feedback processor to act according
 * to the command message. SIM_msg_nc_command is a message to the feedback
 * processor about the NC command that has been executed. The action field
 * contains the 'G codes'.
 *
 * Environment: Internal  and  External
 * See Also:
 * History: Released in NX2
 ******************************************************************************/
extern UFUN_CAMEXPORT int UF_SIM_msg_nc_command
(
   UF_SIM_engine_p_t engine, /* <I> - simulation engine object                */
   const char*       action  /* <I> - NC command                              */
);


/*******************************************************************************
 * Issue command messages mainly to the feedback processor to act according
 * to the command message. SIM_msg_user_feedback is a message to the feedback
 * processor to invoke the TCL procedure specified as the 'proc' argument.
 * Note: That the prefix MOM_ will be added to the procedure before invocation.
 *
 * Environment: Internal  and  External
 * See Also:
 * History: Released in NX2
 ******************************************************************************/
extern UFUN_CAMEXPORT int UF_SIM_msg_user_feedback
(
   UF_SIM_engine_p_t engine, /* <I> - simulation engine object                */
   const char*       proc    /* <I> - name of the a TCL procedure             */
);


/*******************************************************************************
 * Indicate start of simulation.
 *
 *
 * Environment: Internal  and  External
 * See Also:
 * History: Released in NX2
 ******************************************************************************/
extern UFUN_CAMEXPORT int UF_SIM_start_of_simulation
(
   UF_SIM_engine_p_t  engine /* <I> - simulation engine object                */
);


/*******************************************************************************
 * Indicate end of simulation.
 *
 *
 * Environment: Internal  and  External
 * See Also:
 * History: Released in NX2
 ******************************************************************************/
extern UFUN_CAMEXPORT int UF_SIM_end_of_simulation
(
   UF_SIM_engine_p_t  engine /* <I> - simulation engine object                */
);


/*******************************************************************************
 * Request and return the specified junction offset and transformation.
 * To be compatible with csys and msys structure an array with three vectors
 * (X,Y and Z) of the junction with respect to the ABS coordinate system is
 * returned. This means the matrix first has to be tranformed first.
 *
 * Environment: Internal  and  External
 * See Also:
 * History: Released in NX2
 ******************************************************************************/
extern UFUN_CAMEXPORT int UF_SIM_ask_junction_xform
(
   UF_SIM_engine_p_t engine,   /* <I> - simulation engine object              */
   const char*       jct_name, /* <I> - the name of the junction              */
   double*           xval,     /* <O> - offset value in x direction           */
   double*           yval,     /* <O> - offset value in y direction           */
   double*           zval,     /* <O> - offset value in z direction           */
   double*           matrix    /* <O> - matrix between ZCS and MTCS           */
);


/*******************************************************************************
 * Add new junction and attach it to specified component. Unlike some other
 * S&V commands, the creation is done right away. No events are created or
 * triggered to perform this action.
 *
 * Environment: Internal  and  External
 * See Also:
 * History: Released in NX2
 ******************************************************************************/
extern UFUN_CAMEXPORT int UF_SIM_create_junction
(
   UF_SIM_engine_p_t engine,           /* <I> - simulation engine object      */
   const char*       jct_name,         /* <I> - the name of the junction      */
   const char*       destination_comp, /* <I> - the name of the dest. cmp     */
   double            origin[3],        /* <I> - the vector of the origin      */
   double            matrix[9]         /* <I> - the matrix of the junction    */
);


/*******************************************************************************
 * Delete a junction. Unlike some other S&V commands, the deletion is done
 * right away. No events are created or triggered to perform this action.
 *
 * Environment: Internal  and  External
 * See Also:
 * History: Released in NX2
 ******************************************************************************/
extern UFUN_CAMEXPORT int UF_SIM_delete_junction
(
   UF_SIM_engine_p_t engine,     /* <I> - simulation engine object            */
   const char*       jct_name    /* <I> - the name of the junction            */
);


/*******************************************************************************
 * Return whether the specified junction exists or not.
 *
 * Environment: Internal  and  External
 * See Also:
 * History: Released in NX2
 ******************************************************************************/
extern UFUN_CAMEXPORT int UF_SIM_ask_is_junction_exist
(
   UF_SIM_engine_p_t engine,     /* <I> - simulation engine object            */
   const char*       jct_name,   /* <I> - the name of the junction            */
   logical*          jct_exists  /* <O> - existence of the junction           */
);


/*******************************************************************************
 * Set the current ZCS junction.
 *
 * Environment: Internal  and  External
 * See Also:
 * History: Released in NX2
 ******************************************************************************/
extern UFUN_CAMEXPORT int UF_SIM_set_current_zcs_junction
(
   UF_SIM_engine_p_t engine,        /* <I> - simulation engine object         */
   char*             junction_name  /* <I> - the name of the junction         */
);


/*******************************************************************************
 * Return the specified junction offset and transformation. To be compatible
 * with csys and msys structure an array with three vectors (X,Y and Z) of the
 * junction with respect to the ABS coordinate system is returned.
 * This means the matrix has to be transformed first. This is the INITIAL
 * transformation of the junction before the machine tool starts moving.
 *
 * Environment: Internal  and  External
 * See Also:
 * History: Released in NX2
 ******************************************************************************/
extern UFUN_CAMEXPORT int UF_SIM_ask_init_junction_xform
(
   UF_SIM_engine_p_t engine,     /* <I> - simulation engine object            */
   const char*       jct_name,   /* <I> - name of the junction                */
   double*           xval,       /* <O> - offset in x direction               */
   double*           yval,       /* <O> - offset in y direction               */
   double*           zval,       /* <O> - offset in z direction               */
   double*           matrix      /* <O> - matrix                              */
);


/*******************************************************************************
 * Set the machine tool driver units. Those will be the units to input/output
 * data from S&V commands.
 *
 * Environment: Internal  and  External
 * See Also:
 * History: Released in NX2
 ******************************************************************************/
extern UFUN_CAMEXPORT int UF_SIM_set_mtd_units
(
   UF_SIM_engine_p_t  engine,    /* <I> - simulation engine object            */
   UF_SIM_unit_type_t units      /* <I> - units to set                        */
);


/*******************************************************************************
 * Return the machine tool driver units. Those will be the units to input/output
 * data from S&V commands.
 *
 * Environment: Internal  and  External
 * See Also:
 * History: Released in NX2
 ******************************************************************************/
extern UFUN_CAMEXPORT int UF_SIM_ask_mtd_units
(
   UF_SIM_engine_p_t  engine,    /* <I> - simulation engine object            */
   UF_SIM_unit_type_t *units     /* <O> - units                               */
);


/*******************************************************************************
 * Return the current axis position. Axis can be linear or rotary. The
 * current position is the position of the axis after all input events prior
 * to this event have been processed. Coordinates are returned in axis
 * coordinates.
 *
 * Environment: Internal  and  External
 * See Also:
 * History: Released in NX2
 ******************************************************************************/
extern UFUN_CAMEXPORT int UF_SIM_ask_axis_position
(
   UF_SIM_engine_p_t  engine,    /* <I> - simulation engine object            */
   const char         *axis,     /* <I> - the name of the axis                */
   double             *position  /* <O> - the current axis position           */
);


/*******************************************************************************
 * Create an event to set a dialog item attributes. The item identifier is a
 * unique identifier of dialog item. The attributes defines the keyword that
 * identifies the attribute followed by the attribute value according to dialog
 * item attribute syntax. E.g. LABEL=<UGT0201_013> LIST=<X,Y,Z>.
 *
 * Environment: Internal  and  External
 * See Also:
 * History: Released in NX2
 ******************************************************************************/
extern UFUN_CAMEXPORT int UF_SIM_dialog_set_item
(
   UF_SIM_engine_p_t engine,   /* <I> - simulation engine object             */
   const char*      item_id,   /* <I> - the name of the item                 */
   const char*      attributes /* <I> - the value of the attribute           */
);


/*******************************************************************************
 * Returns the junction name that represents the machine tool coordinate system.
 * The jct_name character array has to be of length UF_OBJ_NAME_BUFSIZE.
 *
 * Environment: Internal  and  External
 * See Also:
 * History: Released in NX2
 ******************************************************************************/
extern UFUN_CAMEXPORT int UF_SIM_ask_mtcs_junction
(
   UF_SIM_engine_p_t engine,  /* <I> - simulation engine object               */
   char             jct_name[UF_OBJ_NAME_BUFSIZE] /* <O> - the name of the queried junction       */
);


/*******************************************************************************
 * Returns the full junction name (= <comp_name>@<junction_name> of the axis
 * that defines the degree of freedom.
 * Also, returns the direction of the degree of freedom axis. The jct_name
 * character array has to be of length 2*UF_OBJ_NAME_BUFSIZE.
 *
 * Environment: Internal  and  External
 * See Also:
 * History: Released in NX2
 ******************************************************************************/
extern UFUN_CAMEXPORT int UF_SIM_ask_axis_dof_junction
(
   UF_SIM_engine_p_t            engine,   /* <I> - simulation engine object  */
   const char*                  axis,     /* <I> - the name of the axis      */
   char                         jct_name[2*(UF_OBJ_NAME_BUFSIZE)], /* <O> - the name of the
                                                   corresponding junction    */
   UF_SV_KIM_degof_direction_t* direction /* <O> - the direction of the axis */
);


/*******************************************************************************
 * Returns the axis limits.
 *
 * Environment: Internal  and  External
 * See Also:
 * History: Released in NX2
 ******************************************************************************/
extern UFUN_CAMEXPORT int UF_SIM_ask_axis_limits
(
   UF_SIM_engine_p_t engine, /* <I> - simulation engine object                */
   const char*       axis,   /* <I> - the name of the axis                    */
   double*           min,    /* <O> - the minimum limit of the axis           */
   double*           max     /* <O> - the maximum limit of the axis           */
);


/*******************************************************************************
 * Cause the system to dwell and stop event execution for specified duration.
 *
 * Environment: Internal  and  External
 * See Also:
 * History: Released in NX2
 ******************************************************************************/
extern UFUN_CAMEXPORT int UF_SIM_delay
(
   UF_SIM_engine_p_t engine,  /* <I> - simulation engine object               */
   const char*       label,   /* <I> - label to identify the action           */
   double            duration /* <I> - the duration to stop in sec            */
);


/*******************************************************************************
 * Query and return the chordal tolerance.
 *
 * Environment: Internal  and  External
 * See Also:
 * History: Released in NX2
 ******************************************************************************/
extern UFUN_CAMEXPORT int UF_SIM_ask_cording_tol
(
   UF_SIM_engine_p_t engine,     /* <I> - simulation engine object            */
   double*           cording_tol /* <O> - the cording tolerance               */
);


/*******************************************************************************
 * Initialize S&V commands debugging tools. It also opens a listing device
 * where output debug messages are written.
 *
 * Environment: Internal  and  External
 * See Also:
 * History: Released in NX2
 ******************************************************************************/
extern UFUN_CAMEXPORT int UF_SIM_dbg_start
(
   UF_SIM_engine_p_t engine, /* <I> - simulation engine object                */
   const char*       title   /* <I> - titel of the debug listing window       */
);


/*******************************************************************************
 * End S&V commands debugging tools. It also closes the output listing device.
 *
 * Environment: Internal  and  External
 * See Also:
 * History: Released in NX2
 ******************************************************************************/
extern UFUN_CAMEXPORT int UF_SIM_dbg_end
(
   UF_SIM_engine_p_t engine /* <I> - simulation engine object                */
);


/*******************************************************************************
 * Write message in the debugging output listing. If debugging is not active,
 * no message will be written.
 *
 * Environment: Internal  and  External
 * See Also:
 * History: Released in NX2
 ******************************************************************************/
extern UFUN_CAMEXPORT int UF_SIM_dbg_write_message
(
   UF_SIM_engine_p_t engine, /* <I> - simulation engine object               */
   const char*       msg     /* <I> - the message string, which goes to the
                                      debug output window                    */
);


/*******************************************************************************
 * Activate or deactivate one of the following debugging tokens that controls
 * the output of the corresponding data to the listing device. If token not
 * specified then debugging is turned on or off according to on_off value.
 *
 *   UF_SIM_DBG_OUTPUT_ERROR              output warnings/errors
 *   UF_SIM_DBG_OUTPUT_NC_CMD             output the NC program (i.e. G codes )
 *   UF_SIM_DBG_OUTPUT_CEVENT             output CEvents (i.e. post events)
 *   UF_SIM_DBG_OUTPUT_INPUT_SV_EVENT     output S&V input events
 *   UF_SIM_DBG_OUTPUT_OUTPUT_SV_EVENT    output S&V output events
 *   UF_SIM_DBG_OUTPUT_PROCESSED_SV_EVENT output S&V processed events
 *                                        those includes the output events
 *                                        and those events created by the
 *                                        S&V processors
 *   UF_SIM_DBG_OUTPUT_SV_CMD             output ALL S&V commands that are
 *                                        called
 *   UF_SIM_DBG_OUTPUT_ALL                output all the above data
 *
 *   All tokens must be specified in upper case.
 *
 * Environment: Internal  and  External
 * See Also:
 * History: Released in NX2
 ******************************************************************************/
extern UFUN_CAMEXPORT int UF_SIM_dbg_set_output
(
   UF_SIM_engine_p_t engine, /* <I> - simulation engine object                */
   logical           on_off, /* <I> - switch to set the output on or off      */
   const char*       token   /* <I> - name of the token to switch on or off   */
);


/*******************************************************************************
 * Returns TRUE or FALSE whether the specified junction is dependent on
 * specified NC axis.
 *
 * Environment: Internal  and  External
 * See Also:
 * History: Released in NX2
 ******************************************************************************/
extern UFUN_CAMEXPORT int UF_SIM_ask_is_junction_dependent
(
   UF_SIM_engine_p_t engine,    /* <I> - simulation engine object             */
   const char*       jct_name,  /* <I> - name of the junction                 */
   const char*       axis_name, /* <I> - name of the axis                     */
   char              dependent[256]  /* <O> - dependency of the junction           */
);


/*******************************************************************************
 * Set the setting for sending NC command message to the feedback processor.
 * By default it is issued automatically by the system.
 *
 * Environment: Internal  and  External
 * See Also:
 * History: Released in NX2
 ******************************************************************************/
extern UFUN_CAMEXPORT int UF_SIM_set_status_send_nc_command_msg
(
   UF_SIM_engine_p_t engine,    /* <I> - simulation engine object             */
   logical           status      /* <I> - switch to set the status             */
);


/*******************************************************************************
 * Return the setting for sending NC command message to the feedback processor.
 * By default it is issued automatically by the system.
 *
 * Environment: Internal  and  External
 * See Also:
 * History: Released in NX2
 ******************************************************************************/
extern UFUN_CAMEXPORT int UF_SIM_ask_status_send_nc_command_msg
(
   UF_SIM_engine_p_t engine,   /* <I> - simulation engine object             */
   logical           *status    /* <O> - the status                           */
);


/*******************************************************************************
 * Set the direction of rotation mode for the specified NC axis. This setting
 * controls the path (CW or CCW) a rotary axis will follow when it goes to
 * target position. The possible rotation modes are:
 *
 *  UF_SIM_AXIS_ROT_MAGNITUDE_DETERMINES_DIRECTION
 *  The rotary axis behaves like a linear axis where if target position > 0
 *  then it rotate in CCW. If < 0 then it rotates CW. For example if current
 *  position is 355 and target position is 370 then it rotates in CCW 15
 *  degrees. If target position is 10 then it rotates in CW 345 degrees.
 *
 *  UF_SIM_AXIS_ROT_ALWAYS_SHORTEST
 *  Moves to the target position in shortest path where possible. This is the
 *  default behavior.
 *
 *  UF_SIM_AXIS_ROT_SIGN_DETERMINES_DIRECTION
 *  For positive target position the axis rotates CCW if negative it rotates CW.
 *
 *  UF_SIM_AXIS_ROT_ALWAYS_CLW
 *  Rotates in CW direction only.
 *
 *  UF_SIM_AXIS_ROT_ALWAYS_CCLW
 *  Rotates in CCW direction only.
 *
 * Environment: Internal  and  External
 * See Also:
 * History: Released in NX2
 ******************************************************************************/
extern UFUN_CAMEXPORT int UF_SIM_set_axis_rotary_dir_mode
(
   UF_SIM_engine_p_t          engine,    /* <I> - simulation engine object    */
   const char*                axis_name, /* <I> - name of the axis            */
   UF_SIM_axis_rot_dir_type_t rot_mode   /* <I> - rot mode to set for axis    */
);


/*******************************************************************************
 * Return the direction of rotation mode for the specified NC axis. This
 * setting controls the path (CW or CCW) a rotary axis will follow when it
 * goes to target position. The possible rotation modes are:
 *
 *  UF_SIM_AXIS_ROT_MAGNITUDE_DETERMINES_DIRECTION
 *  The rotary axis behaves like a linear axis where if target position > 0
 *  then it rotate in CCW. If < 0 then it rotates CW. For example if current
 *  position is 355 and target position is 370 then it rotates in CCW 15
 *  degrees. If target position is 10 then it rotates in CW 345 degrees.
 *
 *  UF_SIM_AXIS_ROT_ALWAYS_SHORTEST
 *  Moves to the target position in shortest path where possible. This is the
 *  default behavior.
 *
 *  UF_SIM_AXIS_ROT_SIGN_DETERMINES_DIRECTION
 *  For positive target position the axis rotates CCW if negative it rotates CW.
 *
 *  UF_SIM_AXIS_ROT_ALWAYS_CLW
 *  Rotates in CW direction only.
 *
 *  UF_SIM_AXIS_ROT_ALWAYS_CCLW
 *  Rotates in CCW direction only.
 *
 * Environment: Internal  and  External
 * See Also:
 * History: Released in NX2
 ******************************************************************************/
extern UFUN_CAMEXPORT int UF_SIM_ask_axis_rotary_dir_mode
(
   UF_SIM_engine_p_t          engine,    /* <I> - simulation engine object    */
   const char*                axis_name, /* <I> - name of the axis            */
   UF_SIM_axis_rot_dir_type_t *rot_mode  /* <O> - rot mode of the axis        */
);


/*******************************************************************************
 * Allow reversal mode for the given NC axis.
 *
 * Environment: Internal  and  External
 * See Also:
 * History: Released in NX2
 ******************************************************************************/
extern UFUN_CAMEXPORT int UF_SIM_set_axis_allow_reversal
(
   UF_SIM_engine_p_t engine,        /* <I> - simulation engine object         */
   const char*       axis_name,     /* <I> - name of the NC axis              */
   logical           allow_reversal /* <I> - switch to set the mode           */
);


/*******************************************************************************
 * Ask if the reversal mode for the given NC axis is allowed.
 *
 * Environment: Internal  and  External
 * See Also:
 * History: Released in NX2
 ******************************************************************************/
extern UFUN_CAMEXPORT int UF_SIM_ask_axis_is_reversal_allowed
(
   UF_SIM_engine_p_t   engine,         /* <I> - simulation engine object      */
   const char*         axis_name,      /* <I> - name of the NC axis           */
   logical             *allow_reversal /* <O> - switch of axis                */
);


/*******************************************************************************
 * Returns TRUE or FALSE whether the specified degree of freedom exists in the
 * KIM model.
 *
 * Environment: Internal  and  External
 * See Also:
 * History: Released in NX2
 ******************************************************************************/
extern UFUN_CAMEXPORT int UF_SIM_ask_if_degof_exists
(
   UF_SIM_engine_p_t engine,      /* <I> - simulation engine object           */
   const char*       degof_name,  /* <I> - name of the degree of freedom      */
   logical*          degof_exists /* <O> - existence of the degree of freedom */
);


/*******************************************************************************
 * Query the data for a given degree of freedom.
 *
 * Environment: Internal  and  External
 * See Also:
 * History: Released in NX2
 ******************************************************************************/
extern UFUN_CAMEXPORT int UF_SIM_ask_degof_data
(
   UF_SIM_engine_p_t          engine,     /* <I> - simulation engine object   */
   const char*                degof_name, /* <I> - name of the d. of freedom  */
   UF_SIM_KIM_degof_types_t*  degof_type, /* <O> - type of the d. of freedom  */
   double*                    lower_limit,/* <O> - lower limit                */
   double*                    upper_limit /* <O> - upper limit                */
);


/*******************************************************************************
 * Return the name of the KIM component where the given degree of freedom is
 * designed to.
 *
 * Environment: Internal  and  External
 * See Also:
 * History: Released in NX2
 ******************************************************************************/
extern UFUN_CAMEXPORT int UF_SIM_ask_comp_from_dof
(
   UF_SIM_engine_p_t engine,     /* <I> - simulation engine object            */
   char*             degof_name, /* <I> - name of the degree of freedom       */
   char              comp_name[UF_OBJ_NAME_BUFSIZE]   /* <O> - the name of the component           */
);


/*******************************************************************************
 * Return true if the given component name is found in the KIM tree hierachy.
 * Started by the given component name, false if the given name isn't found.
 *
 * Environment: Internal  and  External
 * See Also:
 * History: Released in NX2
 ******************************************************************************/
extern UFUN_CAMEXPORT int UF_SIM_find_comp_by_name
(
   UF_SIM_engine_p_t  engine,     /* <I> - simulation engine object           */
   char*           start_comp,    /* <I> - name of the base component         */
   char*           search_comp,   /* <I> - name of the component to search    */
   logical*        is_found       /* <O> - result of searching                */
);


/*******************************************************************************
 * Return the list of NC axes of the machine tool in the KIM structure.
 *
 * Environment: Internal  and  External
 * See Also:
 * History: Released in NX2
 ******************************************************************************/
extern UFUN_CAMEXPORT int UF_SIM_ask_nc_axes_of_mtool
(
   UF_SIM_engine_p_t engine,        /* <I> - simulation engine object         */
   int*              no_of_axes,    /* <O> - Number of NC axes                */
   char             axis_name_list[4096] /* <O> - list of NC axis names            */
);

/*******************************************************************************
 * Sets whether the processing the events that are put in the input buffer is
 * done right away or they are put in buffer for later processing. By default
 * this mode is control by the simulation engine and should be used very
 * carefully. When this is set to True some of the simulation functions such as
 * simulation speed control and stepping creteria control may not function the
 * same. This functionality is provided for cases where there is a need to
 * process the events as they are created with no delay of buffering. So, on
 * every call to UF_SIM_update all events will be processed.
 *
 *
 * Environment: Internal  and  External
 * See Also:
 * History: Released in NX2
 *
 ******************************************************************************/
extern UFUN_CAMEXPORT int UF_SIM_set_immediate_update
(
   UF_SIM_engine_p_t engine,          /* <I> - simulation engine object       */
   logical           immediate_update /* <I> - whether to process events as
                                               they are put in buffer         */
);

/*******************************************************************************
 * Returns the immediate update setting. See UF_SIM_set_immediate_update for
 * details.
 *
 * Environment: Internal  and  External
 * See Also:
 * History: Released in NX2
 *
 ******************************************************************************/
extern UFUN_CAMEXPORT int UF_SIM_ask_immediate_update
(
   UF_SIM_engine_p_t engine,         /* <I> - simulation engine object        */
   logical*          immediate_update/* <O> - return immediate update setting */
);

/*******************************************************************************
 * Send program mark message to message window. Next/Previous operation steps
 * to this mark.
 *
 * Environment: Internal  and  External
 * See Also:
 * History: Released in NX2
 *
 ******************************************************************************/
extern UFUN_CAMEXPORT int UF_SIM_msg_program_mark
(
   UF_SIM_engine_p_t engine,         /* <I> - simulation engine object        */
   const char*       program_mark    /* <I> - name of the program mark        */
);

/*******************************************************************************
 * Calculates based on the given parameters for NURBS an array of end-points of
 * linear segments. Based on the existing documentation of NURBS (Post) it
 * is expected, that points are 3 dimensional and knots are one dimensional.
 * Therefore knots has to have the length of knot_count and cntr_pnts has to
 * have the length of 3*cntr_pnt_count.
 *
 * Output
 *  point_count:      number of returned points in the array
 *  positions:        list of points
 *                    size of array is positions(point_count*3)
 *                    The order is point after point,
 *                    position(0) -> point-1-X
 *                    position(1) -> point-1-Y
 *                    position(2) -> point-1-Z
 *                    position(3) -> point-2-X
 *                    position(4) -> point-2-Y
 *                    ...
 *                    Memory of positions is allocated inside this function and
 *                    must be freed from the caller of this function
 *
 * Environment: Internal  and  External
 * See Also:
 * History: Released in NX2
 *
 ******************************************************************************/
extern UFUN_CAMEXPORT int UF_SIM_convert_nurbs_to_position_data
(
   UF_SIM_engine_p_t engine,           /* <I> - simulation engine object      */
   int               cntr_point_count, /* <I> - number of control points      */
   int               order,            /* <I> - order of the nurbs            */
   int               knot_count,       /* <I> - number of knot vectors        */
   double*           knots,            /* <I> - array of knot vectors         */
   double*           cntr_points,      /* <I> - array of control points       */
   int*              point_count,      /* <O> - number of points in the array */
   double**          positions         /* <OF,len:point_count> - return array of points        */
);


#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif /* UF_SIM_COMMANDS_H_INCLUDED */
