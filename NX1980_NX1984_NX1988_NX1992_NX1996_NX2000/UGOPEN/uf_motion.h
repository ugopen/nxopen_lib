/*****************************************************************************

               Copyright (c) 2001-2004 Unigraphics Solutions Inc. 
                        Unpublished - All rights reserved
==============================================================================



File description:

This is the Open API public interface to Scenario for Motion+.  The functions
in this file can be used to:

  - Simulate an existing motion model
  - Create, modify, and use packaging options
  - Obtain specific results about the motion model simulation


  Retired functions:
------------------
The following functions have been retired and replaced with newer NX Open classes and methods:

Retired in 2020.2
    UF_MOTION_create_crv_crv_constraint                     NXOpen.Motion.CurveOnCurveBuilder
    UF_MOTION_init_crv_crv_struct                            NXOpen.Motion.CurveOnCurveBuilder
    UF_MOTION_ask_crv_crv_constraint                        NXOpen.Motion.CurveOnCurveBuilder
    UF_MOTION_create_pt_crv_constraint                      NXOpen.Motion.PointOnCurveBuilder
    UF_MOTION_init_pt_crv_struct                            NXOpen.Motion.PointOnCurveBuilder
    UF_MOTION_ask_pt_crv_constraint                         NXOpen.Motion.PointOnCurveBuilder
    UF_MOTION_set_pt_crv_constraint                         NXOpen.Motion.PointOnCurveBuilder
    UF_MOTION_init_point_on_surface_constraint              NXOpen.Motion.PointOnSurfaceBuilder
    UF_MOTION_ask_point_on_surface_constraint               NXOpen.Motion.PointOnSurfaceBuilder
    UF_MOTION_create_point_on_surface_constraint            NXOpen.Motion.PointOnSurfaceBuilder
    UF_MOTION_set_point_on_surface_constraint               NXOpen.Motion.PointOnSurfaceBuilder

Retired in 2021.1
    UF_MOTION_init_measurement_struct                       NXOpen.Motion.PackagingMeasureBuilder
    UF_MOTION_create_measurement                            NXOpen.Motion.PackagingMeasureBuilder
    UF_MOTION_ask_measurement                               NXOpen.Motion.PackagingMeasureBuilder
    UF_MOTION_edit_measurement                              NXOpen.Motion.PackagingMeasureBuilder
    UF_MOTION_delete_measurement                            NXOpen.Session.UpdateManager

    UF_MOTION_init_trace_struct                             NXOpen.Motion.PackagingTraceBuilder
    UF_MOTION_create_trace                                  NXOpen.Motion.PackagingTraceBuilder
    UF_MOTION_ask_trace                                     NXOpen.Motion.PackagingTraceBuilder
    UF_MOTION_edit_trace                                    NXOpen.Motion.PackagingTraceBuilder
    UF_MOTION_delete_trace                                  NXOpen.Session.UpdateManager

    UF_MOTION_init_interference_struct                      NXOpen.Motion.PackagingInterference
    UF_MOTION_create_interference                           NXOpen.Motion.PackagingInterference
    UF_MOTION_ask_interference                              NXOpen.Motion.PackagingInterference
    UF_MOTION_edit_interference                             NXOpen.Motion.PackagingInterference
    UF_MOTION_delete_interference                           NXOpen.Session.UpdateManager

    UF_MOTION_init_2D_contact_struct                        NXOpen.Motion.CurveContactBuilder
    UF_MOTION_create_2D_contact                             NXOpen.Motion.CurveContactBuilder
    UF_MOTION_ask_2D_contact                                NXOpen.Motion.CurveContactBuilder
    UF_MOTION_set_2D_contact                                NXOpen.Motion.CurveContactBuilder

    UF_MOTION_init_3D_contact_struct                        NXOpen.Motion.BodyContactBuilder
    UF_MOTION_ask_3D_contact                                NXOpen.Motion.BodyContactBuilder
    UF_MOTION_set_3D_contact                                NXOpen.Motion.BodyContactBuilder
    UF_MOTION_create_3D_contact                             NXOpen.Motion.BodyContactBuilder

    UF_MOTION_ask_active_solution                           NXOpen.Motion.MotionSolutionCollection
    UF_MOTION_set_active_solution                           NXOpen.Motion.MotionSolutionCollection

    UF_MOTION_init_general_bushing_struct                   NXOpen.Motion.BushingBuilder
    UF_MOTION_ask_general_bushing                           NXOpen.Motion.BushingBuilder
    UF_MOTION_set_general_bushing                           NXOpen.Motion.BushingBuilder
    UF_MOTION_create_general_bushing                        NXOpen.Motion.BushingBuilder
    UF_MOTION_init_cylindrical_bushing_struct               NXOpen.Motion.BushingBuilder
    UF_MOTION_create_cylindrical_bushing                    NXOpen.Motion.BushingBuilder
    UF_MOTION_ask_cylindrical_bushing                       NXOpen.Motion.BushingBuilder
    UF_MOTION_set_cylindrical_bushing                       NXOpen.Motion.BushingBuilder

    UF_MOTION_ask_gruebler_count                            NXOpen.Motion.MotionSimulation.CalculateGrueblerCount, NXOpen.Motion.MotionSolution.CalculateGrueblerCount

    UF_MOTION_ask_solver_dof_count                          NXOpen.Motion.MotionSession.CalculateDof

    UF_MOTION_init_spring_damper_struct                     NXOpen.Motion.SpringBuilder, NXOpen.Motion.DamperBuilder
    UF_MOTION_create_spring                                 NXOpen.Motion.SpringBuilder
    UF_MOTION_ask_spring                                    NXOpen.Motion.SpringBuilder
    UF_MOTION_set_spring                                    NXOpen.Motion.SpringBuilder
    UF_MOTION_create_damper                                 NXOpen.Motion.DamperBuilder
    UF_MOTION_ask_damper                                    NXOpen.Motion.DamperBuilder
    UF_MOTION_set_damper                                    NXOpen.Motion.DamperBuilder

    UF_MOTION_init_joint_struct                             NXOpen::Motion::JointBuilder
    UF_MOTION_ask_joint                                     NXOpen::Motion::JointBuilder
    UF_MOTION_set_joint                                     NXOpen::Motion::JointBuilder
    UF_MOTION_create_joint                                  NXOpen::Motion::JointBuilder
    UF_MOTION_init_joint_limits_struct                      NXOpen.Motion.JointDefine
    UF_MOTION_ask_joint_limits                              NXOpen.Motion.JointDefine
    UF_MOTION_set_joint_limits                              NXOpen.Motion.JointDefine
    UF_MOTION_remove_joint_limits                           NXOpen.Motion.JointDefine

    UF_MOTION_init_joint_motion_input_struct                NXOpen.Motion.DriverMultiOperations
    UF_MOTION_ask_joint_motion_input                        NXOpen.Motion.DriverMultiOperations
    UF_MOTION_set_joint_motion_input                        NXOpen.Motion.DriverMultiOperations
    UF_MOTION_remove_joint_motion_input                     NXOpen.Motion.DriverMultiOperations

    UF_MOTION_init_joint_coupler_struct                     NXOpen.Motion.CouplerBuilder
    UF_MOTION_create_joint_coupler                          NXOpen.Motion.CouplerBuilder
    UF_MOTION_ask_joint_coupler                             NXOpen.Motion.CouplerBuilder
    UF_MOTION_set_joint_coupler                             NXOpen.Motion.CouplerBuilder

    UF_MOTION_init_link_struct                              NXOpen.Motion.LinkBuilder
    UF_MOTION_create_link                                   NXOpen.Motion.LinkBuilder
    UF_MOTION_ask_link                                      NXOpen.Motion.LinkBuilder
    UF_MOTION_set_link                                      NXOpen.Motion.LinkBuilder
    UF_MOTION_init_link_velocity_struct                     NXOpen.Motion.LinkBuilder
    UF_MOTION_ask_link_initial_velocity                     NXOpen.Motion.LinkBuilder
    UF_MOTION_set_link_initial_velocity                     NXOpen.Motion.LinkBuilder
    UF_MOTION_remove_link_initial_velocity                  NXOpen.Motion.LinkBuilder
    UF_MOTION_init_link_mass_struct                         NXOpen.Motion.LinkMassProperty
    UF_MOTION_ask_link_mass_properties                      NXOpen.Motion.LinkMassProperty
    UF_MOTION_set_link_mass_properties                      NXOpen.Motion.LinkMassProperty
    UF_MOTION_remove_link_mass_properties                   NXOpen.Motion.LinkMassProperty

    UF_MOTION_init_marker_struct                            NXOpen.Motion.MarkerBuilder
    UF_MOTION_create_marker                                 NXOpen.Motion.MarkerBuilder
    UF_MOTION_ask_marker                                    NXOpen.Motion.MarkerBuilder
    UF_MOTION_set_marker                                    NXOpen.Motion.MarkerBuilder

    UF_MOTION_init_scalar_force_torque_struct               NXOpen::Motion::ScalarForceBuilder, NXOpen::Motion::ScalarTorqueBuilder
    UF_MOTION_create_scalar_force                           NXOpen::Motion::ScalarForceBuilder
    UF_MOTION_ask_scalar_force                              NXOpen::Motion::ScalarForceBuilder
    UF_MOTION_set_scalar_force                              NXOpen::Motion::ScalarForceBuilder
    UF_MOTION_create_scalar_torque                          NXOpen::Motion::ScalarTorqueBuilder
    UF_MOTION_ask_scalar_torque                             NXOpen::Motion::ScalarTorqueBuilder
    UF_MOTION_set_scalar_torque                             NXOpen::Motion::ScalarTorqueBuilder

    UF_MOTION_init_vector_force_torque_struct               NXOpen::Motion::VectorForceBuilder, NXOpen::Motion::VectorTorqueBuilder
    UF_MOTION_create_vector_force_torque                    NXOpen::Motion::VectorForceBuilder, NXOpen::Motion::VectorTorqueBuilder
    UF_MOTION_ask_vector_force_torque                       NXOpen::Motion::VectorForceBuilder, NXOpen::Motion::VectorTorqueBuilder
    UF_MOTION_set_vector_force_torque                       NXOpen::Motion::VectorForceBuilder, NXOpen::Motion::VectorTorqueBuilder

    UF_MOTION_calculate_static_equilibrium                  NXOpen::Motion::MotionSolution

    UF_MOTION_init_stl_parameters_struct                    NXOpen.Motion.MotionSimulation.SetAdamsStlParams
    UF_MOTION_export_adams_anl_file                         NXOpen.Motion.MotionSimulation.WriteAdamsAnlFile

    UF_MOTION_init_articulation                             NXOpen.Motion.ArticulationControl 
    UF_MOTION_step_articulation                             NXOpen.Motion.ArticulationControl 
    UF_MOTION_terminate_articulation                        NXOpen.Motion.ArticulationControl 
*****************************************************************************/

#ifndef UF_MOTION_H_INCLUDED
#define UF_MOTION_H_INCLUDED


#include <uf_defs.h>
#include <uf_cae_retiring.h>
#include <uf_motion_types.h>
#include <libufun_cae_exports.h>

#ifdef __cplusplus
extern "C" {
#endif

/***************************************************************************

    Definitions and Prototypes for the Open API interface routines for
    Scenario for Motion+ projects.

    Note on Error Handling: All High level Motion Open API functions return
        a failure code of non zero if an error is encountered.  A descriptive
        message associated with a failure code can be obtained by calling
        UF_get_fail_message with the failure code as the argument.

*****************************************************************************/

/****************************************************************************

 **************************************************************************/
#define ERROR_UF_MOTION_base 3530000

#define UF_MOTION_not_initialized                   (ERROR_UF_MOTION_base)
#define UF_MOTION_null_tag_not_allowed              (ERROR_UF_MOTION_base + 2)
#define UF_MOTION_null_pointer_not_allowed          (ERROR_UF_MOTION_base + 3)
#define UF_MOTION_invalid_joint_scale_factor        (ERROR_UF_MOTION_base + 4)
#define UF_MOTION_invalid_icon_scale_factor         (ERROR_UF_MOTION_base + 5)
#define UF_MOTION_invalid_angular_units             (ERROR_UF_MOTION_base + 6)
#define UF_MOTION_invalid_file_name                 (ERROR_UF_MOTION_base + 7)
#define UF_MOTION_invalid_measure_type              (ERROR_UF_MOTION_base + 8)
#define UF_MOTION_invalid_input_data                (ERROR_UF_MOTION_base + 9)
#define UF_MOTION_input_not_driver                  (ERROR_UF_MOTION_base +10)
#define UF_MOTION_articulation_not_initialized      (ERROR_UF_MOTION_base +11)
#define UF_MOTION_object_belongs_to_another_link    (ERROR_UF_MOTION_base +12)
#define UF_MOTION_only_one_joint_driver_allowed     (ERROR_UF_MOTION_base +13)
#define UF_MOTION_joints_cause_circular_references  (ERROR_UF_MOTION_base +14)

/* Do not change the following without changing error_bases.h! */
#define UF_MOTION_max_error                         (ERROR_UF_MOTION_base +5000)
/****************************************************************************
 *          P R O T Y P E    D E F I N I T I O N S                          *
 ****************************************************************************/
/*****************************************************************************

This function performs a measurement between specific objects at a particular
step in the analysis results.  The measurement parameters must be set in the 
database prior to calling this function using UF_MOTION_create_measurement.  
There must also be a valid set of analysis results in the database before this
function is called.

Environment:  Internal and External

See Also:   UF_MOTION_solve_model
            UF_MOTION_trace
            UF_MOTION_interference

History:  Released in V18

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_measure(
    const tag_t measurement_tag,   /*<I>
                                     The tag of the measurement to be 
                                     performed. It was created using 
                                     UF_MOTION_create_measurement and stores all
                                     of the parameters needed to complete the 
                                     measurement.
                                   */
    const int animation_step,   /*<I>
                                  The step number of the analysis results 
                                  currently loaded in the database.  It cannot
                                  be negative and it cannot be greater than 
                                  the total number of steps in the analysis 
                                  results.
                                */
    double *measurement   /*<O>
                            The results of the measurement.  The units of this
                            result depends on the type of measurement and the 
                            system of units the model is currently in.
                          */
);

/*****************************************************************************

This function performs a trace of a specific object.  The object is copied at 
its position in the analysis step and the tag of the copied object is 
returned.  The trace parameters must first be stored in the model using 
UF_MOTION_create_trace or UF_MOTION_edit_trace.  Before this function can be 
called, valid analysis results must be present in the database.

Environment:  Internal and External

See Also:   UF_MOTION_solve_model
            UF_MOTION_measure
            UF_MOTION_interference

History:  Released in V18

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_trace(
    const tag_t trace_tag,   /*<I>
                               The tag of the trace object.  This tag was 
                               created using UF_MOTION_create_trace and contains
                               all of the parameters needed to perform the 
                               trace.
                             */
    const int step_number,   /*<I>
                               The step number of the analysis results that
                               are currently available in the database.  It
                               cannot be negative and it cannot be greater 
                               than the number of steps in the results.
                             */
    tag_t *new_object_tag   /*<O>
                              The tag of the new object copied from the traced
                              object.
                            */
);

/*****************************************************************************

This function is used to trace all of the links in the model at the input 
solution step.  This function cannot be called until after there is a valid 
solution in the database.  To create a solution, use UF_MOTION_solve_model, 
UF_MOTION_step_articulation, or UF_MOTION_calculate_static_equilibrium.  This 
function will copy all of the geometry of each link in the model and return 
the new geometry tags back.

Environment:  Internal and External

See Also:   UF_MOTION_trace
            UF_MOTION_solve_model

History:  Released in V18

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_trace_model(
    const int step_num,   /*<I>
                            The step number of the current analysis solution 
                            in the database.  It cannot be negative and it 
                            cannot exceed the number of valid steps in the 
                            solution.
                          */
    const int target_layer, /*<I>
                              The layer to place the new objects on.  It
                              must be a valid NX layer.
                            */
    int *num_tags,   /*<O>
                       The number of geometry tags copied and returned in the 
                       next argument.
                     */
    tag_t **geom_tags   /*<OF,len:num_tags>
                          The tags of the copied geometry of all the links.
                          The memory for this array of tags must be freed 
                          using UF_free().
                        */
);

/*****************************************************************************

This function is used to determine if two solid bodies interfere with each 
other at a particular step of the analysis results.  The interference 
parameters must be defined previously.  Also there must be a valid set of 
analysis results in the database.

Environment:  Internal and External

See Also:   UF_MOTION_trace
            UF_MOTION_measure
            UF_MOTION_solve_model
            UF_MOTION_create_interference_body

History:  Released in V18

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_interference(
    const tag_t interference_tag,   /*<I>
                                      The tag of the interference object that 
                                      contains the required parameters to 
                                      perform the interference check.  This 
                                      tag was created using the function
                                      UF_MOTION_create_interference.
                                    */
    const int step_num,   /*<I>
                            The step number to perform the interference 
                            check for.  It cannot be negative and it cannot
                            be greater than the total number of steps 
                            available in the analysis results stored in the
                            database.
                          */
    int *interference_result   /*<O>
                                 The results of the interference check are 
                                 returned as a boolean.  A value of TRUE means 
                                 the objects interfere while a value of false 
                                 means they do not interfere.
                               */
);

/*****************************************************************************

This function creates a new body from the intersection of two interference 
bodies at the input step of the analysis results.  The interference parameters
must be defined previously.  Also there must be a valid set of analysis 
results in the database.

Environment:  Internal and External

See Also:   UF_MOTION_trace
            UF_MOTION_measure
            UF_MOTION_solve_model
            UF_MOTION_interference

History:  Released in V18

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_create_interference_body(
    const tag_t interference_tag,   /*<I>
                                      The tag of the interference object that 
                                      contains the required parameters to 
                                      perform the interference check.  This 
                                      tag was created using the function
                                      UF_MOTION_create_interference.
                                    */
    const int analysis_step_num,   /*<I>
                                     The step number to perform the 
                                     interference check for.  It cannot be 
                                     negative and it cannot be greater than 
                                     the total number of steps available in 
                                     the analysis results stored in the
                                     database.
                                   */
    const UF_MOTION_reference_frame_t frame,   /*<I>
                                               The reference frame to place 
                                               the newly created body in.  If 
                                               the frame is UF_MOTION_absolute, 
                                               the new body will remain in the
                                               absolute position where it was 
                                               created.  If the frame is 
                                               UF_MOTION_first_link or 
                                               UF_MOTION_second_link, the new 
                                               body will be attached to the 
                                               links of the first or second 
                                               interference solid bodies as 
                                               defined in the interference 
                                               tag.  By attaching the new body
                                               to a link, it is in a position 
                                               to be subtracted from the link 
                                               geometry after it moves back to
                                               the design position.
                                             */
    int *num_interference_bodies, /*<O>
                                    The number of interference bodies created.
                                  */
    tag_t **interference_body_tags   /*<OF,len:num_interference_bodies>
                                       The newly created bodies made from the 
                                       intersection of the two interference 
                                       bodies.
                                       The memory for this array of tags
                                       must be freed using UF_free().
                                     */
);

/*****************************************************************************

This function initializes the Scenario for Motion+ application by initializing
the internal databases and solvers.  This function also performs the license
checking for Scenario for Motion+.  The application cannot be used unless a
valid license is found.

Environment:  Internal and External

See Also:   UF_MOTION_terminate
            UF_MOTION_is_initialized

History:  Released in V18

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_initialize( void );

/*****************************************************************************

This function is used to determine if the Scenario for Motion+ application has
been properly initialized.

Environment:  Internal and External

See Also:   UF_MOTION_initialize
            UF_MOTION_terminate

History:  Released in V18

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_is_initialized(
    logical *true_false  /*<O>
                           If Scenario for Motion is properly initialized, 
                           this value will be non-zero.  If Scenario for 
                           Motion is not initialized, this value will be zero.
                         */
);

/*****************************************************************************

This function closes all internal databases and solvers for Scenario for 
Motion and returns the memory to the system.

Environment:  Internal and External

See Also:   UF_MOTION_is_initialized
            UF_MOTION_initialize

History:  Released in V18

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_terminate( void );

/*****************************************************************************

This function initializes the input solver parameters structure with standard 
default values.  It is highly recommended that all solver parameters 
structures get initialized with this function before they are used.

Environment:  Internal and External

See Also:

History:  Released in V18

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_init_solver_parameters_struct(
    UF_MOTION_solver_parameters_t *solver_params_struct   /*<O>
                                                          The solver 
                                                          parameters structure
                                                          to be initialized.
                                                        */
);

/*****************************************************************************

This function gets the current solver parameters from Scenario for Motion+.

Environment:  Internal and External

See Also:   UF_MOTION_edit_solver_parameters

History:  Released in V18

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_ask_solver_parameters(
    UF_MOTION_solver_parameters_t *solver_params_struct   /*<O>
                                                          The current solver 
                                                          parameters in 
                                                          Scenario for Motion.
                                                        */
);

/*****************************************************************************

This function sets new solver parameters to Scenario for Motion+.

Environment:  Internal and External

See Also:   UF_MOTION_ask_solver_parameters

History:  Released in V18

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_edit_solver_parameters(
    const UF_MOTION_solver_parameters_t *solver_params   /*<I>
                                                         The new solver 
                                                         parameters for 
                                                         Scenario for Motion.
                                                       */
);

/*****************************************************************************

All joints that have a joint motion input defined can be articulated even 
though the motion input type might not be articulation.  This function returns
the articulation step size for the input joint tag.  The tag must belong to a 
joint that has a motion input defined or else an error condition is returned.

Environment:  Internal and External

See Also:   UF_MOTION_edit_artic_step_size

History:  Released in V18

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_ask_artic_step_size(
    const tag_t joint_tag,   /*<I>
                               The tag of the joint to return the step size 
                               for.  This tag is returned from the function
                               UF_MOTION_create_joint.  It can also be found 
                               using object cycle functions
                               (eg. UF_OBJ_cycle_objs_by_type).
                             */
    double *step_size   /*<O>
                          The size of the articulation joint step.  The units 
                          of the step are based on the units of the joint.
                        */
);

/*****************************************************************************

All joints that have a joint motion input defined can be articulated even 
though the motion input type might not be articulation.  This function sets 
the articulation step size for the input joint tag.  The tag must belong to a
joint that has a motion input defined or else an error condition is returned.

Environment:  Internal and External

See Also:   UF_MOTION_ask_artic_step_size

History:  Released in V18

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_edit_artic_step_size(
    const tag_t joint_tag,   /*<I>
                               The tag of the joint to set the articulation 
                               step size on.  This tag must belong to a joint 
                               that has a motion input defined or else an 
                               error condition is returned.  This tag is 
                               returned from UF_MOTION_create_joint.  It can 
                               also be found using cycle functions 
                               (eg. UF_OBJ_cycle_objs_by_type).
                             */
    const double step_size   /*<I>
                               The new size of the articulation joint step.  
                               The units of the step are based on the units of
                               the joint.
                             */
);

/*****************************************************************************

This function performs the analysis of the motion model.  Prior to calling 
this function the model must be completely ready to analyze.  This function is
a time-based analysis.  If the model has one or more degrees of freedom, this 
function performs a dynamic analysis.  If the model has no degrees of freedom 
(including redundant constraints) this function performs a kinematic analysis.
The results of the analysis are stored in the internal database until another 
analysis is performed or the model is changed.  To access the results, use 
any of the following:

      1) Packaging options, including measure, trace, and interference.
      2) Write the results to disk using UF_MOTION_export_adams_res_file.
      3) Get specific results from a joint or marker.

Environment:  Internal and External

See Also:   UF_MOTION_measure
            UF_MOTION_review_adams_res_file
            UF_MOTION_ask_velocity_results
            UF_MOTION_ask_force_results

History:  Released in V18

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_solve_model(
    const double time,   /*<I>
                           The total time for the analysis in the current time
                           units.
                         */
    int *num_steps   /*<I/O>
                       The number of steps for the solver to take during the 
                       analysis.  This parameter is used with the time 
                       parameter to determine the average step size for the 
                       analysis.  The total number of steps successfully saved
                       in the database is returned.
                     */
);

/*****************************************************************************
This function reviews the existing result file of the motion model. Prior to 
calling this function the model must be analyzed atleast once. 

Inputs:  Result file name (without path)

Outputs: None

Return:  Zero for success, non-zero is error code

Environment:  Internal and External

See Also:   UF_MOTION_solve_model
            UF_MOTION_export_adams_res_file
            UF_MOTION_ask_velocity_results
            UF_MOTION_ask_force_results

History:  Created in NX4
*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_review_adams_res_file(
    char *res_file  /*<I>
                         The filename (only) of the .res file to write.    
                         The filename should end with .res followed by a
                         terminating NULL character.
                       */
    );

/*****************************************************************************

This function writes the ADAMS .res file to disk.  This file contains the 
results of the latest solve-static equilirium, articulation, or a full 
simulation.  This is the only way to save the solver results; the results are
not saved in the part file.  However, the results file does not need to be 
written for any other purpose.  This file is only used to store results for 
later use.  If the model is not changed, these results can be read back in to
Scenario for Motion for further processing.

Environment:  Internal and External

See Also:   UF_MOTION_solve_model
            UF_MOTION_ask_velocity_results
            UF_MOTION_ask_force_results

History:  Released in V18

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_export_adams_res_file(
    char *file_name    /*<I>
                         The filename of the .res file to write.  It 
                         should include the entire path to the file.  
                         The filename should end with .res followed by a
                         terminating NULL character.
                       */
);

/*****************************************************************************

This function is used to get specific translational displacement results from
the analysis results stored in the database.  If this function is called when
no results are in the database, an error condition will be returned.  

Environment:  Internal and External

See Also:   UF_MOTION_solve_model
            UF_MOTION_export_adams_res_file
            UF_MOTION_ask_rot_displacement_results
            UF_MOTION_ask_velocity_results 

History:  Released in V18

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_ask_trans_displacement_results(
    const tag_t motion_object,   /*<I>
                                   The tag of the object to get the results
                                   for.  This is usually a joint, constraint,
                                   coupler, marker, or primitive.
                                 */
    const UF_MOTION_vector_component_t component,   /*<I>
                                                    The desired component of
                                                    the displacement (Example:
                                                    UF_MOTION_magnitude or
                                                    UF_MOTION_x_component).
                                                  */
    const UF_MOTION_reference_frame_t ref_frame,   /*<I>
                                                   The reference frame that
                                                   the results will be 
                                                   resolved in (Example:
                                                   UF_MOTION_absolute).
                                                 */
    int *number_of_results,   /*<O>
                                The number of results returned in the next
                                argument.  This will equal the number of 
                                steps in the solution.
                              */
    double **results   /*<OF,len:number_of_results>
                         The results requested.  This array must be freed by
                         the calling function using UF_free().
                       */
                         
);

/*****************************************************************************

This function is used to get specific rotational displacement results from 
the analysis results stored in the database.  If this function is called when
no results are in the database, an error condition will be returned.

Environment:  Internal and External

See Also:   UF_MOTION_solve_model
            UF_MOTION_export_adams_res_file
            UF_MOTION_ask_trans_displacement_results
            UF_MOTION_ask_torque_results

History:  Released in V18

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_ask_rot_displacement_results(
    const tag_t motion_object,   /*<I>
                                   The tag of the object to get the results
                                   for.  This is usually a joint, constraint,
                                   coupler, marker, or primitive.
                                 */
    const UF_MOTION_disp_angle_t component,   /*<I>
                                              The desired displacement angle.
                                              This can be the Euler angles 
                                              that follow the body 3-1-3 
                                              convention. See the enum 
                                              definition for more information.
                                            */
    const UF_MOTION_reference_frame_t ref_frame,   /*<I>
                                                     The reference frame that
                                                     the results will be 
                                                     resolved in (Example:
                                                     UF_MOTION_absolute).
                                                   */
    int *number_of_results,   /*<O>
                                The number of results returned in the next
                                argument.  This will equal the number of 
                                steps in the solution.
                              */
    double **results   /*<OF,len:number_of_results>
                         The results requested. The unit is radian.
                         This array must be freed
                         by the calling function using UF_free().
                       */
                         
);

/*****************************************************************************

This function is used to get specific velocity results from the analysis 
results stored in the database.  Both translational and rotational velocities
can be returned from this function.  If this function is called when no 
results are in the database, an error condition will be returned.

Environment:  Internal and External

See Also:   UF_MOTION_solve_model
            UF_MOTION_export_adams_res_file
            UF_MOTION_ask_trans_displacement_results
            UF_MOTION_ask_acceleration_results

History:  Released in V18

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_ask_velocity_results(
    const tag_t motion_object,   /*<I>
                                   The tag of the object to get the results
                                   for.  This is usually a joint, constraint,
                                   coupler, marker, or primitive.
                                 */
    const UF_MOTION_motion_type_t type,   /*<I>
                                          The velocity type: UF_MOTION_rotation 
                                          or UF_MOTION_translation.
                                        */
    const UF_MOTION_vector_component_t component,   /*<I>
                                                    The desired component of
                                                    the velocity (Example:
                                                    UF_MOTION_magnitude or
                                                    UF_MOTION_x_component).
                                                  */
    const UF_MOTION_reference_frame_t ref_frame,   /*<I>
                                                   The reference frame that
                                                   the results will be 
                                                   resolved in.
                                                 */
    int *number_of_results,   /*<O>
                                The number of results returned in the next
                                argument.  This will equal the number of 
                                steps in the solution.
                              */
    double **results   /*<OF,len:number_of_results>
                         The results requested. For angular velocity, the values
                         are in radian per second. This array must be freed by
                         the calling function using UF_free().
                       */
                         
);

/*****************************************************************************

This function is used to get specific acceleration results from the analysis 
results stored in the database.  It can return both translational and 
rotational accelerations.  If this function is called when no results are in 
the database, an error condition will be returned.  

Environment:  Internal and External

See Also:   UF_MOTION_solve_model
            UF_MOTION_export_adams_res_file
            UF_MOTION_ask_trans_displacement_results
            UF_MOTION_ask_velocity_results

History:  Released in V18

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_ask_acceleration_results(
    const tag_t motion_object,   /*<I>
                                   The tag of the object to get the results
                                   for.  This is usually a joint, constraint,
                                   coupler, marker, or primitive.
                                 */
    const UF_MOTION_motion_type_t type,   /*<I>
                                          The type of acceleration: 
                                          UF_MOTION_rotation or 
                                          UF_MOTION_translation.
                                        */
    const UF_MOTION_vector_component_t component,   /*<I>
                                                    The desired component of
                                                    the acceleration (Example:
                                                    UF_MOTION_magnitude or
                                                    UF_MOTION_x_component).
                                                  */
    const UF_MOTION_reference_frame_t ref_frame,   /*<I>
                                                   The reference frame that
                                                   the results will be 
                                                   resolved in.
                                                 */
    int *number_of_results,   /*<O>
                                The number of results returned in the next
                                argument.  This will equal the number of 
                                steps in the solution.
                              */
    double **results   /*<OF,len:number_of_results>
                         The results requested.  For angular acceleration,
                         the values are in radian per square second.
                         This array must be freed by
                         the calling function using UF_free().
                       */
                         
);

/*****************************************************************************

This function is used to get specific force results from the analysis results 
stored in the database.  If this function is called when no results are in the
database, an error condition will be returned.

Environment:  Internal and External

See Also:   UF_MOTION_solve_model
            UF_MOTION_export_adams_res_file
            UF_MOTION_ask_velocity_results
            UF_MOTION_ask_torque_results

History:  Released in V18

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_ask_force_results(
    const tag_t motion_object,   /*<I>
                                   The tag of the object to get the results
                                   for.  This is usually a joint, constraint,
                                   coupler, marker, or primitive.
                                 */
    const UF_MOTION_vector_component_t component,   /*<I>
                                                    The desired component of
                                                    the force (Example:
                                                    UF_MOTION_magnitude or
                                                    UF_MOTION_x_component).
                                                  */
    const UF_MOTION_reference_frame_t ref_frame,   /*<I>
                                                   The reference frame that
                                                   the results will be 
                                                   resolved in.
                                                 */
    int *number_of_results,   /*<O>
                                The number of results returned in the next
                                argument.  This will equal the number of 
                                steps in the solution.
                              */
    double **results   /*<OF,len:number_of_results>
                         The results requested.  This array must be freed by
                         the calling function using UF_free().
                       */
                         
);

/*****************************************************************************

This function is used to get specific torque results from the analysis results
in the database.  If this function is called when no results are in the 
database, an error condition will be returned.

Environment:  Internal and External

See Also:   UF_MOTION_solve_model
            UF_MOTION_export_adams_res_file
            UF_MOTION_ask_velocity_results
            UF_MOTION_ask_force_results

History:  Released in V18

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_ask_torque_results(
    const tag_t motion_object,   /*<I>
                                   The tag of the object to get the results
                                   for.  This is usually a joint, constraint,
                                   coupler, marker, or primitive.
                                 */
    const UF_MOTION_vector_component_t component,   /*<I>
                                                    The desired component of
                                                    the torque (Example:
                                                    UF_MOTION_magnitude or
                                                    UF_MOTION_x_component).
                                                  */
    const UF_MOTION_reference_frame_t ref_frame,   /*<I>
                                                   The reference frame that
                                                   the results will be 
                                                   resolved in.
                                                 */
    int *number_of_results,   /*<O>
                                The number of results returned in the next
                                argument.  This will equal the number of 
                                steps in the solution.
                              */
    double **results   /*<OF,len:number_of_results>
                         The results requested.  This array must be freed by
                         the calling function using UF_free().
                       */
                         
);

/*****************************************************************************

This function is used to export motion animation to product vision.
This function creates a VFM file which is the ProductVision format for
motion data. 
If this function is called when no results are in the 
database, an error condition will be returned.To populate the results
into the database the motion model has to be solved.

Environment:  Internal and External

See Also:   UF_MOTION_solve_model
          
History:  Released in V18

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_export_to_product_vision( 
    const char *full_file_name, /* <I>
                                  The full name of the VFM file to be 
                                  exported. The name should include 
                                  the directory where the newly created file
                                  needs to be placed. 
                                  (e.g., /users/test/file_name
                                  note: On windows use '\' instead of '/' )
                                  If the length of the string is zero then the 
                                  scenario directory will be the default directory 
                                   and the scenario name will be the default file
                                   name */
    UF_MOTION_PV_export_type_t export_option /* <I>
                                                The option to export VFM and JT file or
                                                only the VFM file */
    );

/***************************************************************************

This function gets the information of motion objects and writes it out
to a file.

Environment:  Internal and External

See Also:   UF_MOTION_list_connections

History:  Created in NX3

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_write_object_info
(
    int num_objects,  /* <I>
                         The number of motion objects in the tag array.
                      */
    tag_p_t object_tags,  /* <I,len:num_objects>
                             Tag array of motion objects to get info for.
                          */
    const char *info_file_name  /* <I>
                                   Name string (including full path) of
                                   output file that object information 
                                   will be written to.  This file should
                                   be new and not yet exist.
                                */
);

/****************************************************************************
Generate an ascii text file containing a listing of the Motion connections, 
degrees of freedom, etc.

Environment: Internal and External 

See Also:   UF_MOTION_write_object_info

History: Released in NX3

******************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_list_connections
(
    const char *output_file_with_path /* <I> 
                                         The full path to the file that the 
                                         listing should be written to. If 
                                         this file already exists it will
                                         be overwritten. 
                                      */

);

/*****************************************************************************

This function asks the mechanism parameters of the current mechanism in the
scenario part. 

Environment:  Internal and External

See Also:   UF_MOTION_set_articulation_stop_tolerance

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_ask_articulation_stop_tolerance
(
    double *stop_tolerance  /* <O> */
);

/*****************************************************************************

This function sets the articulation stop tolerance.  This is used by Adams to
calculate the stop positions for stop events in Articulation.

Environment:  Internal and External

See Also:   UF_MOTION_ask_articulation_stop_tolerance

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_set_articulation_stop_tolerance
(
    double stop_tolerance  /* <I> */
);

/*****************************************************************************

This function sets whether trace/explosion objects will get exported to the
master

Environment:  Internal and External

See Also:   UF_MOTION_ask_trace_explosion_to_master

History:  Released in NX3
*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_set_trace_explosion_to_master
(
    logical to_master /* <I> TRUE or FALSE */
);

/*****************************************************************************

This function returns whether trace/explosion objects will get exported to the
master

Environment:  Internal and External

See Also:   UF_MOTION_set_trace_explosion_to_master

History:  Released in NX3
*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_ask_trace_explosion_to_master
(
    logical *to_master /* <I> TRUE or FALSE */
);

/*****************************************************************************

This function sets the dislay of object names

Environment:  Internal and External

See Also:   UF_MOTION_ask_name_display

History:  Released in NX3
*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_set_name_display
(
    logical name_display /* <I> TRUE  if names should be displayed.
                                FALSE if names should not be displayed. */
);

/*****************************************************************************

This function returns the dislay of object names

Environment:  Internal and External

See Also:   UF_MOTION_set_name_display

History:  Released in NX3
*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_ask_name_display
(
    logical *name_display /* <O> TRUE  if names should be displayed.
                                 FALSE if names should not be displayed. */
);

/*****************************************************************************

This function sets the angular units for this mechanism

Environment:  Internal and External

See Also:   UF_MOTION_ask_angular_units

History:  Released in NX3
*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_set_angular_units
(
    UF_MOTION_angular_units_type_t angle_units /* <I> The new units */
);

/*****************************************************************************

This function return the angular units stored in this mechanism

Environment:  Internal and External

See Also:   UF_MOTION_set_angular_units

History:  Released in NX3
*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_ask_angular_units
(
    UF_MOTION_angular_units_type_t *angle_units /* <O> The new units */
);

/*****************************************************************************

This function sets the graviational constants in this mechanism

Environment:  Internal and External

See Also:   UF_MOTION_ask_gravitational_constants

History:  Released in NX3
*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_set_gravitational_constants
(
    double gravitational_constants[3]  /* <I>  Vector defining gravitational
                                               force */
);

/*****************************************************************************

This function return the graviational constants stored in this mechanism

Environment:  Internal and External

See Also:   sUF_MOTION_set_gravitational_constants

History:  Released in NX3
*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_ask_gravitational_constants
(
    double gravitational_constants[3]  /* <O>  Vector defining gravitational
                                               force */
);

/*****************************************************************************

This function sets the global icon scale.

Environment:  Internal and External

See Also:   UF_MOTION_ask_icon_scale_factor

History:  Released in NX3

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_set_icon_scale_factor
(
    double scale /*<I> */
);

/*****************************************************************************

This function returns the global icon scale.

Environment:  Internal and External

See Also:   UF_MOTION_set_icon_scale_factor

History:  Released in NX3

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_ask_icon_scale_factor
(
    double *scale /*<I>*/
);

/*****************************************************************************

This function returns the motion objects of a specified type that are
attached to the input motion object.  This function will check the
type/subtype requests for validity of attachment.  For example, asking
for contacts attached to a joint is not valid.  Note also, that the
subtype input is only needed for certain motion types, and is not
required for other motion types.  See following table:

  type requested                   subtype needed
  =====================            ==============
  UF_mdm_mechanism_type            NO
  UF_mdm_link_type                 NO
  UF_mdm_joint_type                OPTIONAL - If subtype not defined, all
                                   entities of this type will be returned.
  UF_mdm_marker_type               NO - UF_mdm_user_defined_marker_subtype
                                        will be only subtype returned.
  UF_mdm_spring_type               NO
  UF_mdm_damper_type               NO
  UF_mdm_force_type                NO
  UF_mdm_torque_type               NO
  UF_mdm_genforce_type             YES - Subtype must be defined.
  UF_mdm_curve_curve_contact_type  NO
  UF_mdm_contact_type              NO

Environment:  Internal and External

See Also:

History:  Released in NX3

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_ask_attachments_of_type
(
    tag_t entity_tag,      /* <I>
                              The motion entity to get attachments for.
                           */
    int type,              /* <I>
                              The type of attachments to retrieve.
                              See uf_object_types.h for definition
                              of motion object types.
                           */
    int subtype,           /* <I>
                              The subtype of attachments (if applicable)
                              to retrieve.  See uf_object_types.h for
                              definition of motion object subtypes.
                           */
    int *num_attachments,  /* <O>
                              The number of attachment objects.
                           */
    tag_p_t *attachments   /* <OF,len:num_attachments>
                              The array of attached objects.
                           */
);




/******************************************************************************************************************

This function asks the 3D contact method to be used.

Return:  Zero for success, non-zero is error code

Environment:  Internal and External

See Also:   UF_MOTION_set_3D_contact_method

History:  Released in NX3
******************************************************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_ask_3D_contact_method
(
    UF_MOTION_3d_contact_method_t *contact_method, /* <O>
                                                     the 3d contact method to be used 
                                                     by Adams
                                                   */
    int *facet_contact_tolerance                    /* <O> ignored unless
                                                         contact_method == UF_MOTION_faceted_contact
                                                         Must be a value 1 to 100.
                                                         1   means Fast but may not be accurate
                                                         100 means Accurate but may not be Fast
                                                   */
);

/******************************************************************************************************************

This function sets the 3D contact method to be used.

Return:  Zero for success, non-zero is error code

Environment:  Internal and External

See Also:   UF_MOTION_ask_3D_contact_method

History:  Released in NX3
*******************************************************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_set_3D_contact_method
(
    UF_MOTION_3d_contact_method_t contact_method, /* <I>
                                                     the 3d contact method to be used 
                                                     by Adams
                                                   */
    int facet_contact_tolerance                  /* <I> ignored unless
                                                          contact_method == UF_MOTION_faceted_contact
                                                          Must be a value 1 to 100.
                                                          1   means Fast but may not be accurate
                                                          100 means accurate but may not be fast
                                                    */
);

/*****************************************************************************

This function initializes the input function structure with standard default
values.  It is highly recommended that all function structures get initialized
with this function before they are used.

Environment:  Internal and External

History:  Released in NX2.0.5 and NX3.0.1

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_init_function_struct
(
    UF_MOTION_function_t *function_struct  /* <O> The function structure to be 
                                              initialized. */
);

/*****************************************************************************

This function creates a function object in the Scenario for Motion+ database
according to the parameters passed in through the function structure.
If successful, the tag of the new function object is returned.  It is highly
recommended that the function definition syntax is validated before
creating the function object.

Environment:  Internal and External

See Also:   UF_MOTION_ask_function
            UF_MOTION_set_function
            UF_MOTION_validate_function_syntax
            UF_MOTION_get_object_derived_function

History:  Released in NX2.0.5 and NX3.0.1

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_create_function
(
    const UF_MOTION_function_t *function_struct, /* <I> 
                                                    The required parameters
                                                    to create the function.
                                                 */
    tag_t *function_tag  /* <O> 
                            The new function tag.  This tag identifies
                            the function object in the database.
                         */
);

/*****************************************************************************

This function returns the function structure for an input function tag.

Environment:  Internal and External

See Also:   UF_MOTION_set_function
            UF_MOTION_find_all_functions
            UF_MOTION_ask_function_tag_from_name

History:  Released in NX2.0.5 and NX3.0.1

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_ask_function
(
    const tag_t function_tag,  /* <I>
                                  The tag of the function to query.
                                  This tag is the one returned from
                                  UF_MOTION_create_function.
                               */
    UF_MOTION_function_t *function_struct  /* <O>
                                              The function structure for the 
                                              input function tag.
                                           */
);

/*****************************************************************************

This function sets the input function parameters to the input function tag.

Environment:  Internal and External

See Also:   UF_MOTION_ask_function
            UF_MOTION_validate_function_syntax
            UF_MOTION_get_object_derived_function

History:  Released in NX2.0.5 and NX3.0.1

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_set_function
(
    const tag_t function_tag,  /* <I>
                                  The tag of the function to set.
                                  This tag is the one returned
                                  from UF_MOTION_create_function.
                               */
    const UF_MOTION_function_t *function_struct  /* <I>
                                                    The function structure 
                                                    for the input tag.
                                                 */
);

/*****************************************************************************

This function finds all the motion function objects in the current part.

Environment:  Internal and External

See Also:   UF_MOTION_ask_function_tag_from_name

History:  Released in NX2.0.5 and NX3.0.1

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_find_all_functions
(
    tag_t **function_tags, /* <OF,len:num_functions>
                              Tag array of all function objects in
                              current part.
                           */
    int *num_functions  /* <O>
                           Number of function tags.
                        */
);

/*****************************************************************************

This function finds the motion function tag for a given function name.

Environment:  Internal and External

See Also:   UF_MOTION_find_all_functions

History:  Released in NX2.0.5 and NX3.0.1

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_ask_function_tag_from_name
(
    char *function_name, /* <I>
                            Name string of function object to find.
                         */
    tag_t *function_tag  /* <O>
                            Tag of function object for input name.
                         */
);

/*****************************************************************************

This function deletes the motion function object from the database.
If the function object is still referenced by another motion object,
it will not be deleted and an error code will be returned.

Environment:  Internal and External

See Also:   UF_MOTION_ask_function_tag_from_name
            UF_MOTION_find_all_functions

History:  Released in NX2.0.5 and NX3.0.1

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_delete_function
(
    const tag_t function_tag   /* <I>
                                  Tag of function object to delete.
                               */
);

/*****************************************************************************

This function checks the syntax of a function definition string to verify
its validity.

Environment:  Internal and External

See Also:   UF_MOTION_get_object_derived_function
            UF_MOTION_create_function

History:  Released in NX2.0.5 and NX3.0.1

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_validate_function_syntax
(
    char **function_string, /* <I,len:num_lines>
                               Full string for a function definition.
                            */
    const int num_lines  /* <I>
                            Number of lines of function string.
                         */
);

/*****************************************************************************

This function returns the string of a derived function.  A derived function
references a motion object for a particular result type.  All motion objects
other than links are allowed for reference in a derived function.

Environment:  Internal and External

See Also:   UF_MOTION_validate_function_syntax
            UF_MOTION_create_function

History:  Released in NX2.0.5 and NX3.0.1

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_get_object_derived_function
(
    const tag_t motion_obj_tag, /* <I>
                                   The motion object being referenced
                                   for the derived function.
                                */
    UF_MOTION_func_result_type_t func_type, /* <I>
                                               The result type requested
                                               for the derived function.
                                               See uf_motion_types.h
                                            */
    UF_MOTION_func_component_type_t func_comp, /* <I>
                                                  The result component
                                                  requested for the
                                                  derived function.
                                                  See uf_motion_types.h
                                               */
    UF_MOTION_func_ref_frame_type_t ref_frame, /* <I>
                                                  The reference frame
                                                  for the derived function.
                                                  See uf_motion_types.h
                                               */
    char **derived_func_string  /* <OF>
                                   Formulated string of a derived function.
                                */
);

/*****************************************************************************

This function gets the number of frames for active solution.

Environment:  Internal and External

See Also:  

History:  Released in NX801
******************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_ask_number_of_animation_frames
( 
    int * numFrames      /* <O> Number of frames for current active solution result */
);

/*****************************************************************************

This function gets the transform matrix of the specified link object in given frame

Environment:  Internal and External

See Also: 

History:  Released in NX801
******************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_ask_link_transfrom_for_given_frame
( 
    tag_t linkTag,                  /*<I> Motion link object tag*/      
    int frame,                      /*<I> The given frame*/
    double transformMatrix[16]      /*<O> The transform matrix 1X16*/
);

/*****************************************************************************

This function will set transformation matrix for given link object

Environment:  Internal and External

See Also:

History:  Released in NX801
******************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_set_link_transform
( 
    tag_t linkTag,                  /*<I> Motion link object tag*/      
    double transformMatrix[16]      /*<I> The transform matrix 1X16*/
);

/*****************************************************************************

This function reviews the existing result file of the motion model. Prior to 
calling this function the model must be analyzed at least once. 

Inputs:  Result file name (without path)

Outputs: None

Return:  Zero for success, non-zero is error code

Environment:  Internal and External

See Also:   UF_MOTION_solve_model
            UF_MOTION_export_adams_res_file
            UF_MOTION_ask_velocity_results
            UF_MOTION_ask_force_results

History:  Created in NX801
*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_review_result_file
(
      const char *res_file  /*<I>
                         The filename should be *.rad for Recurdyn *.res for Adams.    
                         The filename should end with .rad or .res followed by a
                         terminating NULL character..
                       */
);

/*************************************************************************

Suppress warning messages for reparenting the master part when
open a scenario part.  

Environment: Internal or External

Input    :  logical flag = true will turn off the warnings

Returns  :  0  - Successful
            else Unsuccessful

See Also: 
History: Released in NX801
*************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_file_suppress_warnings
(
    logical flag    /*<I> The suppress flag, true will turn off the warnings */
);

#ifdef __cplusplus
}

#endif

#undef EXPORTLIBRARY

#endif /* UF_MOTION_H_INCLUDED */
