/*==================================================================================================

        Copyright 2020 Siemens Industry Software NV 
                All Rights Reserved

====================================================================================================



 File description:
          These routines are in the process of being removed from the NX Open API
          product.  Customers should use the designated replacement routines
          instead of the routines listed here.  Once a routine is placed
          here, it is eligible to be removed in the next release of NX.

====================================================================================================*/

#ifndef UF_CAE_RETIRING
#define UF_CAE_RETIRING

#include <uf_defs.h>
#include <uf_motion_types.h> 

#include <libufun_cae_exports.h>

/***************************************************************************

  ***************************************************************************/

#ifdef __cplusplus
extern "C" {
#endif


/*****************************************************************************

This function create curve curve constraint

Environment:  Internal and External

See Also:   UF_MOTION_ask_crv_crv_constraint
            UF_MOTION_create_crv_crv_constraint

History:  Created in NX2

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_create_crv_crv_constraint
(
    UF_MOTION_curve_curve_constraint_t* crv_crv_data, /* <I> input data */
    tag_t* crv_crv_tag /* <O> created constraint  */
);

/*****************************************************************************

This function initializes the input curve curve structure with standard
default values.  It is highly recommended that all curve curve structures
get initialized with this function before they are used.

Environment:  Internal and External

See Also:

History:  Created in NX2

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_init_crv_crv_struct
(
    UF_MOTION_curve_curve_constraint_t* crv_crv_struct
    /* <I/O> The curve curve structure to be initialized. */
);

/*****************************************************************************

This function returns the curve curve structure for an input curve
curve constraint tag.

Environment:  Internal and External

See Also:   UF_MOTION_create_crv_crv_constraint

History:  Created in NX2

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_ask_crv_crv_constraint
(
    const tag_t crv_crv_tag,/* <I>
                              The tag of the constraint to return.
                              This tag is the one returned from
                              the UF_MOTION_create_crv_crv_constraint
                              function. It can also be found using
                              object cycle functions.
                              (eg. UF_OBJ_cycle_objs_by_type)
                           */
    UF_MOTION_curve_curve_constraint_t* crv_crv_struct
    /* <O>
       The curve-curve  structure for the input tag.
    */
);




/*****************************************************************************

This function create point curve constraint

Environment:  Internal and External

See Also:   UF_MOTION_ask_pt_crv_constraint
            UF_MOTION_set_pt_crv_constraint

History:  Created in NX2

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_create_pt_crv_constraint
(
    UF_MOTION_point_curve_constraint_t* pt_crv_data,/* <I>*/
    tag_t* pt_crv_tag   /* <O> created constraint */
);


/*****************************************************************************

This function initializes the input point curve structure with standard
default values.  It is highly recommended that all point curve structures
get initialized with this function before they are used.

Environment:  Internal and External

See Also:

History:  Created in NX2

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_init_pt_crv_struct
(
    UF_MOTION_point_curve_constraint_t* pt_crv_struct
    /* <I/O> The point curve structure to be initialized. */
);

/*****************************************************************************

This function returns the point curve structure for an input point
curve constraint tag.

Environment:  Internal and External

See Also:   UF_MOTION_set_pt_crv_constraint

History:  Created in NX2

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_ask_pt_crv_constraint
(
    const tag_t pt_crv_tag,/* <I>
                              The tag of the constraint to return.
                              This tag is the one returned from
                              the UF_MOTION_create_pt_crv_constraint
                              function. It can also be found using
                              object cycle functions.
                              (eg. UF_OBJ_cycle_objs_by_type)
                           */
    UF_MOTION_point_curve_constraint_t* pt_crv_struct
    /* <O>
       The point-curve  structure for the input tag.
    */
);

/*****************************************************************************

This function edit point curve constraint

Environment:  Internal and External

See Also:   UF_MOTION_ask_pt_crv_constraint

History:  Created in NX2

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_set_pt_crv_constraint
(
    tag_t pt_crv_tag, /* <I> tag of the constraint */
    UF_MOTION_point_curve_constraint_t* pt_crv_data /* <I>
                                                       point curve
                                                       constraint data  */
);


/*****************************************************************************************************************************************

This function initializes the structures of point on surface constraint
parameters with standard default values.  It is highly recommended that all
point on surface parameters structures get initialized with this function
before they are used.

Return:  Zero for success, non-zero is error code

Environment:  Internal and External

See Also:   UF_MOTION_ask_point_on_surface_constraint
            UF_MOTION_create_point_on_surface_constraint
            UF_MOTION_set_point_on_surface_constraint

History:  Created in NX3

*****************************************************************************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_init_point_on_surface_constraint
(
    UF_MOTION_point_on_surface_data_p_t point_on_surf_data /* <O>
                                                              The empty struct
                                                              to retrieve the
                                                              default Point on
                                                              surface
                                                              parameters.
                                                           */
);

/*****************************************************************************************************************************************

This function asks the structures of point on surface constraint parameters
for a given point_on_surface_tag value.

Return:  Zero for success, non-zero is error code

Environment:  Internal and External

See Also:   UF_MOTION_init_point_on_surface_constraint
            UF_MOTION_create_point_on_surface_constraint
            UF_MOTION_set_point_on_surface_constraint

History:  Created in NX3

*****************************************************************************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_ask_point_on_surface_constraint
(
    tag_t point_on_surface_tag,                         /* <I>
                                                           tag of point on surface constraint
                                                           object to get the data for
                                                        */
    UF_MOTION_point_on_surface_data_p_t pt_on_surf_data /* <O>
                                                           The structure corresponding to the
                                                           input point on surface constraint tag
                                                        */
);

/***************************************************************************************************************************************

This function creates the structure of point on surface constraint with provided
values and returns the corresponding tag_t pointer.

Return:  Zero for success, non-zero is error code

Environment:  Internal and External

See Also:   UF_MOTION_ask_point_on_surface_constraint
            UF_MOTION_init_point_on_surface_constraint
            UF_MOTION_set_point_on_surface_constraint

History:  Created in NX3

****************************************************************************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_create_point_on_surface_constraint
(
    UF_MOTION_point_on_surface_data_p_t pt_on_surf_data, /* <I>
                                                            Input structures of point on surface
                                                            constraint data
                                                          */
    tag_p_t point_on_surface_tag                         /* <O>
                                                            tag of created point on surface
                                                            constraint
                                                         */
);

/*******************************************************************************************************************************************

This function sets the structures represented by the tag_t with new point on
surface constraint values.

Return:  Zero for success, non-zero is error code

Environment:  Internal and External

See Also:   UF_MOTION_init_point_on_surface_constraint
            UF_MOTION_create_point_on_surface_constraint
            UF_MOTION_ask_point_on_surface_constraint

History:  Created in NX3

*******************************************************************************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_set_point_on_surface_constraint
(
    tag_t point_on_surface_tag,                         /* <I>
                                                          tag of point on surface constraint
                                                          object
                                                       */
    UF_MOTION_point_on_surface_data_p_t pt_on_surf_data /* <I>
                                                            Structures of point on surface
                                                            constraint data
                                                          */
);

/*****************************************************************************

This function initializes the input measurement structure with standard
default values.  It is highly recommended that all measurement structures get
initialized with this function before they are used.

Environment:  Internal and External

See Also:   UF_MOTION_init_trace_struct
            UF_MOTION_init_interference_struct

History:  Released in V18

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_init_measurement_struct(
    UF_MOTION_measurement_t* measurement_struct   /*<O>
                                                  The measurement structure to
                                                  be initialized.
                                                */
);

/*****************************************************************************

This function creates a measurement object in the Scenario for Motion+
database according to the parameters passed in through the measurement
structure.  If successful, the tag of the new measurement object is returned.
The measurement object is used in the post processor to determine the distance
or angle between two objects at a particular time step.

Environment:  Internal and External

See Also:   UF_MOTION_ask_measurement
            UF_MOTION_edit_measurement
            UF_MOTION_measure

History:  Released in V18.

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_create_measurement(
    const UF_MOTION_measurement_t* meas_struct,   /*<I>
                                                  The required parameters to
                                                  create the measurement.
                                                */
    tag_t* meas_tag   /*<O>
                        The new measurement tag.  This tag identifies the
                        measurement in the database.
                      */
);

/*****************************************************************************

This function returns the measurement structure for an input measurement tag.

Environment:  Internal and External

See Also:   UF_MOTION_edit_measurement
            UF_MOTION_create_measurement
            UF_MOTION_measure

History:  Released in V18

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_ask_measurement(
    const tag_t meas_tag,   /*<I>
                              The tag of the measurement to return.  This tag
                              is the one returned from the creation function
                              (UF_MOTION_create_measurement).  It can also be
                              found using object cycle functions
                              (eg. UF_OBJ_cycle_objs_by_type).
                            */
    UF_MOTION_measurement_t* meas_struct   /*<O>
                                           The measurement structure
                                           for the input tag.
                                         */
);

/*****************************************************************************

This function sets the input measurement parameters to the input measurement
tag.

Environment:  Internal and External

See Also:   UF_MOTION_ask_measurement
            UF_MOTION_create_measurement
            UF_MOTION_measure

History:  Released in V18

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_edit_measurement(
    const tag_t meas_tag,   /*<I>
                              The tag of the measurement to edit.  This tag
                              is returned from UF_MOTION_create_measurement.
                              It can also be found using object cycle
                              functions (eg. UF_OBJ_cycle_objs_by_type).
                            */
    const UF_MOTION_measurement_t* meas_struct   /*<I>
                                                 The measurement structure
                                                 for the input tag.
                                               */
);

/*****************************************************************************

This function deletes the input measurement object.

Environment:  Internal and External

See Also:   UF_MOTION_ask_measurement
            UF_MOTION_create_measurement
            UF_MOTION_measure

History:  Released in V18

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_delete_measurement(
    const tag_t meas_tag    /*<I>
                              The tag of the measurement to delete.  This tag
                              is returned from UF_MOTION_create_measurement.
                              It can also be found using object cycle
                              functions (eg. UF_OBJ_cycle_objs_by_type).
                            */
);

/*****************************************************************************

This function initializes the input trace structure with standard default
values.  It is highly recommended that all trace structures get initialized
with this function before they are used.

Environment:  Internal and External

See Also:   UF_MOTION_init_measurement_struct
            UF_MOTION_init_interference_struct

History:  Released in V18

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_init_trace_struct(
    UF_MOTION_trace_t* trace_struct   /*<O>
                                      The trace structure to be initialized.
                                    */
);

/*****************************************************************************

This function creates a trace object in the Scenario for Motion+ database
according to the parameters passed in through the trace structure.  If
successful, the tag of the new trace object is returned.  The trace object is
used in the post processor to create a copy of a solid body in its simulated
position at a particular time step.

Environment:  Internal and External

See Also:   UF_MOTION_ask_trace
            UF_MOTION_edit_trace
            UF_MOTION_trace

History:  Released in V18.

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_create_trace(
    const UF_MOTION_trace_t* trace_struct,   /*<I>
                                             The required parameters to
                                             create the trace.
                                           */
    tag_t* trace_tag   /*<O>
                         The new trace tag.  This tag identifies the trace in
                         the database.
                       */
);

/*****************************************************************************

This function returns the trace structure from an input trace tag.

Environment:  Internal and External

See Also:   UF_MOTION_edit_trace
            UF_MOTION_create_trace
            UF_MOTION_trace

History:  Released in V18

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_ask_trace(
    const tag_t trace_tag,   /*<I>
                               The tag of the trace to return.  This tag is
                               the one returned from UF_MOTION_create_trace.  It
                               can also be found using object cycle functions
                               (eg. UF_OBJ_cycle_objs_by_type).
                             */
    UF_MOTION_trace_t* trace_struct   /*<O>
                                      The trace structure of the input tag.
                                    */
);

/*****************************************************************************

This function sets the input trace parameters to the input trace tag.

Environment:  Internal and External

See Also:   UF_MOTION_ask_trace
            UF_MOTION_create_trace
            UF_MOTION_trace

History:  Released in V18

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_edit_trace(
    const tag_t trace_tag,   /*<I>
                               The tag of the trace to edit.  This tag is the
                               one returned from UF_MOTION_create_trace.  It can
                               also be found using object cycle functions
                               (eg. UF_OBJ_cycle_objs_by_type).
                             */
    const UF_MOTION_trace_t* trace_struct   /*<I>
                                            The trace structure for the input
                                            tag.
                                          */
);

/*****************************************************************************

This function deletes the input trace object.

Environment:  Internal and External

See Also:   UF_MOTION_ask_trace
            UF_MOTION_create_trace
            UF_MOTION_trace

History:  Released in V18

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_delete_trace(
    const tag_t trace_tag   /*<I>
                              The tag of the trace to delete.  This tag
                              is returned from UF_MOTION_create_trace.
                              It can also be found using object cycle
                              functions (eg. UF_OBJ_cycle_objs_by_type).
                            */
);

/*****************************************************************************

This function initializes the input interference structure with standard
default values.  It is highly recommended that all interference structures get
initialized with this function before they are used.

Environment:  Internal and External

See Also:   UF_MOTION_init_trace_struct
            UF_MOTION_init_measurement_struct

History:  Released in V18

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_init_interference_struct(
    UF_MOTION_interference_t* interference_struct   /*<O>
                                                    The interference structure
                                                    to be initialized.
                                                  */
);

/*****************************************************************************

This function creates an interference object in the Scenario for Motion+
database according to the parameters passed in through the interference
structure.  If successful, the tag of the new interference object is returned.
The interference object is used in the post processor to determine if two
solid bodies interfere with each other at a particular time step.  The
interference object can then be used to create a new interference body of the
intersection volume.

Environment:  Internal and External

See Also:   UF_MOTION_ask_interference
            UF_MOTION_interference
            UF_MOTION_create_interference_body

History:  Released in V18.

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_create_interference(
    const UF_MOTION_interference_t* interfere_struct,   /*<I>
                                                        The parameters
                                                        required to create the
                                                        interference object.
                                                      */
    tag_t* interference_tag   /*<O>
                                The new interference tag.  This tag identifies
                                the interference object in the database.
                              */
);

/*****************************************************************************

This function returns the interference structure for an input interference
tag.

Environment:  Internal and External

See Also:   UF_MOTION_edit_interference
            UF_MOTION_create_interference
            UF_MOTION_interference

History:  Released in V18

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_ask_interference(
    const tag_t interfere_tag,   /*<I>
                                   The tag of the interference to return.
                                   This tag is the one returned from the
                                   UF_MOTION_create_interference function.
                                   It can also be found using object cycle
                                   functions (eg. UF_OBJ_cycle_objs_by_type).
                                 */
    UF_MOTION_interference_t* interference_struct   /*<O>
                                                    The interference structure
                                                    for the input tag.
                                                  */
);

/*****************************************************************************

This function sets the input interference parameters to the input interference
tag.

Environment:  Internal and External

See Also:   UF_MOTION_ask_interference
            UF_MOTION_create_interference
            UF_MOTION_interference

History:  Released in V18

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_edit_interference(
    const tag_t interfere_tag,   /*<I>
                                   The tag of the interference to edit.  This
                                   tag is returned from the function
                                   UF_MOTION_create_interference.  It can also
                                   be found using object cycle functions
                                   (eg. UF_OBJ_cycle_objs_by_type).
                                 */
    const UF_MOTION_interference_t* interfere_struct   /*<I>
                                                       The interference
                                                       structure for the input
                                                       tag.
                                                     */
);

/*****************************************************************************

This function deletes the input interference object.

Environment:  Internal and External

See Also:   UF_MOTION_ask_interference
            UF_MOTION_create_interference
            UF_MOTION_interference

History:  Released in V18

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_delete_interference(
    const tag_t interfere_tag   /*<I>
                                  The tag of the interference to delete.  This
                                  tag is returned from the function
                                  UF_MOTION_create_interference.  It can also
                                  be found using object cycle functions
                                  (eg. UF_OBJ_cycle_objs_by_type).
                                */
);
/*****************************************************************************

This function initializes the input 2D contact structure with standard
default values.  It is highly recommended that all 2D contact structures
get initialized with this function before they are used.

Environment:  Internal and External

History:  Created in NX2

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_init_2D_contact_struct
(
    UF_MOTION_2D_contact_t* contact_struct  /* <O>
                                          The 2D_contact structure to be
                                          initialized.
                                       */
);

/*****************************************************************************

This function creates a 2D contact in the Scenario for Motion+ database
according to the parameters passed in through the 2D contact structure.
If successful, the tag of the new 2D contact is returned.

Environment:  Internal and External

See Also:   UF_MOTION_ask_2D_contact
            UF_MOTION_set_2D_contact

History:  Created in NX2

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_create_2D_contact
(
    UF_MOTION_2D_contact_t* contact_struct,  /* <I>
                                                The required parameters
                                                to create the 2D contact.
                                             */
    tag_t* contact_tag   /* <O>
                            The new 2D contact tag.  This tag identifies
                            the 2D contact in the database.
                         */
);

/*****************************************************************************

This function returns the 2D contact structure for an input 2D contact tag.

Environment:  Internal and External

See Also:   UF_MOTION_set_2D_contact

History:  Created in NX2

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_ask_2D_contact
(
    const tag_t contact_tag,  /* <I>
                                The tag of the 2D contact to return.
                                This tag is the one returned from
                                UF_MOTION_create_2D_contact.
                                It can also be found using object cycle
                                functions. (eg. UF_OBJ_cycle_objs_by_type)
                             */
    UF_MOTION_2D_contact_t* contact_struct  /* <O>
                                               The 2D contact structure
                                               of the input tag.
                                            */
);

/*****************************************************************************

This function sets 2D contact properties for the input 2D contact tag.

Environment:  Internal and External

See Also:   UF_MOTION_ask_2D_contact

History:  Created in NX2

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_set_2D_contact
(
    const tag_t contact_tag,  /* <I>
                                 The tag of the 2D contact to set.  This tag
                                 is the one returned from
                                 UF_MOTION_create_2D_contact.  It can also
                                 be found using object cycle functions.
                                 (eg. UF_OBJ_cycle_objs_by_type)
                              */
    UF_MOTION_2D_contact_t* contact_struct  /* <I>
                                               The 2D contact structure
                                               for the input tag.
                                            */
);

/*****************************************************************************

This function initializes the input 3D contact structure with standard
default values.  It is highly recommended that all 3D contact structures
get initialized with this function before they are used.

Environment:  Internal and External

History:  Created in NX2

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_init_3D_contact_struct
(
    UF_MOTION_3D_contact_t* contact_struct  /* <O>
                                               The 3D_contact structure to be
                                               initialized.
                                            */
);


/*****************************************************************************

This function returns the 3D contact structure for an input 3D contact tag.

Environment:  Internal and External

See Also:   UF_MOTION_set_3D_contact

History:  Created in NX2

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_ask_3D_contact
(
    const tag_t contact_tag,  /* <I>
                                The tag of the 3D contact to return.
                                This tag is the one returned from
                                UF_MOTION_create_3D_contact.
                                It can also be found using object cycle
                                functions. (eg. UF_OBJ_cycle_objs_by_type)
                             */
    UF_MOTION_3D_contact_t* contact_struct  /* <O>
                                               The 3D contact structure
                                               of the input tag.
                                            */
);

/*****************************************************************************

This function sets 3D contact properties for the input 3D contact tag.

Environment:  Internal and External

See Also:   UF_MOTION_ask_3D_contact

History:  Created in NX2

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_set_3D_contact
(
    const tag_t contact_tag,  /* <I>
                                 The tag of the 3D contact to set.  This tag
                                 is the one returned from
                                 UF_MOTION_create_3D_contact.  It can also
                                 be found using object cycle functions.
                                 (eg. UF_OBJ_cycle_objs_by_type)
                              */
    UF_MOTION_3D_contact_t* contact_struct  /* <I>
                                               The 3D contact structure
                                               for the input tag.
                                            */
);
/*****************************************************************************

This function creates a 3D contact in the Scenario for Motion+ database
according to the parameters passed in through the 3D contact structure.
If successful, the tag of the new 3D contact is returned.

Environment:  Internal and External

See Also:   UF_MOTION_ask_3D_contact
            UF_MOTION_set_3D_contact

History:  Created in NX2

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_create_3D_contact
(
    UF_MOTION_3D_contact_t* contact_struct,  /* <I>
                                                The required parameters
                                                to create the 3D contact.
                                             */
    tag_t* contact_tag   /* <O>
                            The new 3D contact tag.  This tag identifies
                            the 3D contact in the database.
                         */
);
/*************************************************************************

Ask the active solution for current motion simulation

Environment: Internal or External

Onput    :  tag_t active_solution

Returns  :  0  - Successful
            else Unsuccessful

See Also:
History: Released in NX801
*************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_ask_active_solution
(
    tag_t* active_solution     /*<O> The active solution*/
);

/*************************************************************************

Set the active solution for current motion simulation

Environment: Internal or External

Input    :  tag_t active_solution

Returns  :  0  - Successful
            else Unsuccessful

See Also:
History: Released in NX801
*************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_set_active_solution
(
    tag_t active_solution       /*<I> The active solution*/
);
/*****************************************************************************

This function initializes the input general bushing structure with standard
default values.  It is highly recommended that all general bushing structures
get initialized with this function before they are used.

Environment:  Internal and External

History:  Created in NX2

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_init_general_bushing_struct
(
    UF_MOTION_general_bushing_t* bushing_struct  /* <O>
                                                    The bushing data
                                                    structure to be
                                                    initialized.
                                                 */
);
/*****************************************************************************

This function returns the general bushing structure for an input bushing tag.

Environment:  Internal and External

See Also:   UF_MOTION_set_general_bushing

History:  Created in NX2

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_ask_general_bushing
(
    const tag_t bushing_tag,  /* <I>
                                 The tag of the general bushing to return
                                 information about.  This tag is the one
                                 returned from the
                                 UF_MOTION_create_general_bushing function.
                                 It can also be found using object cycle
                                 functions.  (eg. UF_OBJ_cycle_objs_by_type)
                              */
    UF_MOTION_general_bushing_t* bushing_struct  /* <O>
                                                    The general bushing
                                                    structure for the
                                                    input tag.
                                                 */
);
/*****************************************************************************

This function sets the input general bushing parameters to the input
general bushing tag.

Environment:  Internal and External

See Also:   UF_MOTION_ask_general_bushing

History:  Created in NX2

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_set_general_bushing
(
    const tag_t bushing_tag,  /* <I>
                                 The tag of the general bushing to set.
                                 This tag is the one returned from the
                                 UF_MOTION_create_general_bushing function.
                                 It can also be found using object cycle
                                 functions. (eg. UF_OBJ_cycle_objs_by_type)
                             */
    const UF_MOTION_general_bushing_t* bushing_struct  /* <I>
                                                          The general bushing
                                                          structure for the
                                                          input tag.
                                                       */
);
/*****************************************************************************

This function creates a general bushing in the Scenario for Motion+ database
according to the parameters passed in through the general bushing structure.
If successful, the tag of the new general bushing is returned.

Environment:  Internal and External

See Also:   UF_MOTION_ask_general_bushing
            UF_MOTION_set_general_bushing

History:  Created in NX2.

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_create_general_bushing
(
    UF_MOTION_general_bushing_t* bushing_struct,  /* <I>
                                                     The required
                                                     parameters to create
                                                     the general bushing.
                                                  */
    tag_t* bushing_tag  /* <O>
                           The new bushing tag.  This tag identifies
                           the general bushing in the database.
                        */
);
/*****************************************************************************

This function initializes the input cylindrical bushing structure with
standard default values.  It is highly recommended that all cylindrical
bushing structures get initialized with this function before they are used.

Environment:  Internal and External

History:  Created in NX2

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_init_cylindrical_bushing_struct
(
    UF_MOTION_cylindrical_bushing_t* bushing_struct  /* <O>
                                                        The bushing data
                                                        structure to be
                                                        initialized.
                                                     */
);

/*****************************************************************************

This function creates a cylindrical bushing in the Scenario for Motion+
database according to the parameters passed in through the cylindrical
bushing structure.  If successful, the tag of the new cylindrical bushing
is returned.

Environment:  Internal and External

See Also:   UF_MOTION_ask_cylindrical_bushing
            UF_MOTION_set_cylindrical_bushing

History:  Created in NX2.

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_create_cylindrical_bushing
(
    UF_MOTION_cylindrical_bushing_t* bushing_struct,  /* <I>
                                                         The required
                                                         parameters to
                                                         create the
                                                         cylindrical bushing.
                                                      */
    tag_t* bushing_tag  /* <O>
                           The new bushing tag.  This tag identifies
                           the cylindrical bushing in the database.
                        */
);

/*****************************************************************************

This function returns the cylindrical bushing structure for an input
bushing tag.

Environment:  Internal and External

See Also:   UF_MOTION_set_cylindrical_bushing

History:  Created in NX2

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_ask_cylindrical_bushing
(
    const tag_t bushing_tag,  /* <I>
                                 The tag of the cylindrical bushing to
                                 return information about.  This tag is
                                 the one returned from the
                                 UF_MOTION_create_cylindrical_bushing
                                 function.  It can also be found using
                                 object cycle functions.
                                 (eg. UF_OBJ_cycle_objs_by_type)
                              */
    UF_MOTION_cylindrical_bushing_t* bushing_struct  /* <O>
                                                        The cylindrical
                                                        bushing structure
                                                        for the input tag.
                                                     */
);

/*****************************************************************************

This function sets the input cylindrical bushing parameters to the input
cylindrical bushing tag.

Environment:  Internal and External

See Also:   UF_MOTION_ask_cylindrical_bushing

History:  Created in NX2

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_set_cylindrical_bushing
(
    const tag_t bushing_tag,  /* <I>
                                 The tag of the cylindrical bushing to set.
                                 This tag is the one returned from the
                                 UF_MOTION_create_cylindrical_bushing function.
                                 It can also be found using object cycle
                                 functions. (eg. UF_OBJ_cycle_objs_by_type)
                             */
    const UF_MOTION_cylindrical_bushing_t* bushing_struct  /* <I>
                                                              The cylindrical
                                                              bushing structure
                                                              for the input tag.
                                                           */
);
/*****************************************************************************

This function gets the total Gruebler count for the current mechanism.

Environment:  Internal and External

See Also:   UF_MOTION_ask_solver_dof_count

History:  Created in NX2

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_ask_gruebler_count
(
    int* gruebler_count  /* <O>
                            The total Gruebler count.
                         */
);

/*****************************************************************************

This function gets the total degree of freedom count as calculated by the
motion solver for the current mechanism.

Environment:  Internal and External

See Also:   UF_MOTION_ask_gruebler_count

History:  Created in NX2

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_ask_solver_dof_count
(
    int* dof_count  /* <O>
                       The total degree of freedom count.
                    */
);

/*****************************************************************************

This function initializes the input spring/damper structure with
standard default values.  It is highly recommended that all spring/damper
structures get initialized with this function before they are used.

Environment:  Internal and External

History:  Created in NX2

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_init_spring_damper_struct
(
    UF_MOTION_spring_damper_t* spring_damper_struct  /* <O>
                                                        The spring/damper
                                                        data structure
                                                        to be initialized.
                                                     */
);

/*****************************************************************************

This function creates a spring in the Scenario for Motion+ database
according to the parameters passed in through the spring structure.
If successful, the tag of the new spring is returned.

Environment:  Internal and External

See Also:   UF_MOTION_ask_spring
            UF_MOTION_set_spring

History:  Created in NX2.

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_create_spring
(
    UF_MOTION_spring_damper_t* spring_struct,  /* <I>
                                                  The required parameters
                                                  to create the spring.
                                               */
    tag_t* spring_tag  /* <O>
                          The new spring tag.  This tag identifies the
                          spring in the database.
                       */
);

/*****************************************************************************

This function returns the spring structure for an input spring tag.

Environment:  Internal and External

See Also:   UF_MOTION_set_spring

History:  Created in NX2

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_ask_spring
(
    const tag_t spring_tag,  /* <I>
                                The tag of the spring to return information
                                about.  This tag is the one returned from the
                                UF_MOTION_create_spring function.  It can
                                also be found using object cycle functions.
                                (eg. UF_OBJ_cycle_objs_by_type)
                             */
    UF_MOTION_spring_damper_t* spring_struct  /* <O>
                                                 The spring structure
                                                 for the input tag.
                                              */
);

/*****************************************************************************

This function sets the input spring parameters to the input spring tag.
The spring parameters that can be set are the rate, the free length (linear)
or free angle (rotational), and the link attachment points.

Environment:  Internal and External

See Also:   UF_MOTION_ask_spring

History:  Created in NX2

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_set_spring
(
    const tag_t spring_tag,  /* <I>
                                The tag of the spring to set.  This tag is the
                                one returned from the UF_MOTION_create_spring
                                function.  It can also be found using object
                                cycle functions. (eg. UF_OBJ_cycle_objs_by_type)
                             */
    const UF_MOTION_spring_damper_t* spring_struct  /* <I>
                                                       The spring structure
                                                       for the input tag.
                                                    */
);

/*****************************************************************************

This function creates a damper in the Scenario for Motion+ database
according to the parameters passed in through the damper structure.
If successful, the tag of the new damper is returned.

Environment:  Internal and External

See Also:   UF_MOTION_ask_damper
            UF_MOTION_set_damper

History:  Created in NX2.

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_create_damper
(
    UF_MOTION_spring_damper_t* damper_struct,  /* <I>
                                                  The required parameters
                                                  to create the damper.
                                               */
    tag_t* damper_tag  /* <O>
                          The new damper tag.  This tag identifies the
                          damper in the database.
                       */
);

/*****************************************************************************

This function returns the damper structure for an input damper tag.

Environment:  Internal and External

See Also:   UF_MOTION_set_damper

History:  Created in NX2

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_ask_damper
(
    const tag_t damper_tag,  /* <I>
                                The tag of the damper to return information
                                about.  This tag is the one returned from the
                                UF_MOTION_create_damper function.  It can
                                also be found using object cycle functions.
                                (eg. UF_OBJ_cycle_objs_by_type)
                             */
    UF_MOTION_spring_damper_t* damper_struct  /* <O>
                                                 The damper structure
                                                 for the input tag.
                                              */
);

/*****************************************************************************

This function sets the input damper parameters to the input damper tag.
The damper parameters that can be set are the damping rate and the
link attachment points.

Environment:  Internal and External

See Also:   UF_MOTION_ask_damper

History:  Created in NX2

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_set_damper
(
    const tag_t damper_tag,  /* <I>
                                The tag of the damper to set.  This tag is the
                                one returned from the UF_MOTION_create_damper
                                function.  It can also be found using object
                                cycle functions. (eg. UF_OBJ_cycle_objs_by_type)
                             */
    const UF_MOTION_spring_damper_t* damper_struct  /* <I>
                                                       The damper structure
                                                       for the input tag.
                                                    */
);
/*****************************************************************************

This function initializes the input joint structure with standard default
values.  It is highly recommended that all joint structures get initialized
with this function before they are used.

Environment:  Internal and External

See Also:   UF_MOTION_init_joint_limits_struct
            UF_MOTION_init_joint_motion_input_struct

History:  Created in NX2

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_init_joint_struct
(
    UF_MOTION_joint_t* joint_struct   /* <O>
                                         The joint structure to be initialized.
                                      */
);
/*****************************************************************************

This function returns the joint structure for an input joint tag.

Environment:  Internal and External

See Also:   UF_MOTION_set_joint
            UF_MOTION_ask_joint_limits
            UF_MOTION_ask_joint_motion_input

History:  Created in NX2

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_ask_joint
(
    const tag_t joint_tag,  /* <I>
                               The tag of the joint to return information
                               about.  This tag is the one returned from the
                               UF_MOTION_create_joint function.  It can also
                               be found using object cycle functions.
                               (eg. UF_OBJ_cycle_objs_by_type)
                            */
    UF_MOTION_joint_t* joint_struct  /* <O>
                                        The joint structure for the input tag.
                                     */
);

/*****************************************************************************

This function sets the input joint parameters to the input joint tag.

Environment:  Internal and External

See Also:   UF_MOTION_ask_joint
            UF_MOTION_set_joint_limits
            UF_MOTION_set_joint_motion_input

History:  Created in NX2

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_set_joint
(
    const tag_t joint_tag,  /* <I>
                               The tag of the joint to set.  This tag is the
                               one returned from the UF_MOTION_create_joint
                               function.  It can also be found using object
                               cycle functions. (eg. UF_OBJ_cycle_objs_by_type)
                            */
    const UF_MOTION_joint_t* joint_struct  /* <I>
                                               The joint structure
                                               for the input tag.
                                           */
);
/*****************************************************************************

This function creates a joint in the Scenario for Motion+ database according
to the parameters passed in through the joint structure.  If successful, the
tag of the new joint is returned.  This function does not allow joint limits
or joint motion input to be created at this point.  To add these things to a
joint, use UF_MOTION_set_joint_limits and UF_MOTION_set_joint_motion_input after
creating the joint with this function.

Environment:  Internal and External

See Also:   UF_MOTION_ask_joint
            UF_MOTION_set_joint_limits
            UF_MOTION_set_joint_motion_input

History:  Created in NX2.

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_create_joint
(
    UF_MOTION_joint_t* joint_struct,   /* <I>
                                          The required parameters to
                                          create the joint.
                                       */
    tag_t* joint_tag  /* <O>
                         The new joint tag.  This tag identifies the
                         joint in the database.
                      */
);
/*****************************************************************************

This function initializes the input joint limits structure with standard
default values.  It is highly recommended that all joint limits structures
get initialized with this function before they are used.

Environment:  Internal and External

See Also:   UF_MOTION_init_joint_struct
            UF_MOTION_init_joint_motion_input_struct

History:  Created in NX2

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_init_joint_limits_struct
(
    UF_MOTION_joint_limits_t* joint_limits_struct   /* <O>
                                                       The joint limits
                                                       structure to be
                                                       initialized.
                                                    */
);
/*****************************************************************************

This function returns the joint limits structure for an input joint tag.  If
joint limits are not defined for the input joint tag, an error condition is
returned.

Environment:  Internal and External

See Also:   UF_MOTION_ask_joint
            UF_MOTION_set_joint_limits
            UF_MOTION_ask_joint_motion_input

History:  Created in NX2

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_ask_joint_limits
(
    const tag_t joint_tag,  /* <I>
                               The tag of the joint to return the joint
                               limits of.  This tag is the one returned
                               from the UF_MOTION_create_joint function.
                               It can also be found using object cycle
                               functions. (eg. UF_OBJ_cycle_objs_by_type)
                            */
    UF_MOTION_joint_limits_t* joint_limits_struct  /* <O>
                                                      The joint limits
                                                      structure for the
                                                      input tag.  If joint
                                                      limits are not defined
                                                      for the input joint,
                                                      zeros will be returned
                                                      in the structure and
                                                      an error will be
                                                      returned from the
                                                      function.
                                                   */
);

/*****************************************************************************

This function sets the joint limits for the input joint tag.  By default,
joint limits are undefined for all joints.  Joint limits can only be set for
revolute and slider joints.  If the input tag is another type of joint, an
error condition is returned.

Environment:  Internal and External

See Also:   UF_MOTION_set_joint
            UF_MOTION_ask_joint_limits
            UF_MOTION_remove_joint_limits

History:  Created in NX2

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_set_joint_limits
(
    const tag_t joint_tag,  /* <I>
                               The tag of the joint to set the joint
                               limits on.  This joint must be a revolute
                               or a slider.  This tag is the one returned
                               from the UF_MOTION_create_joint function.
                               It can also be found using object cycle
                               functions. (eg. UF_OBJ_cycle_objs_by_type)
                            */
    const UF_MOTION_joint_limits_t* joint_limits_struct  /* <I>
                                                            The joint limits
                                                            structure for the
                                                            input tag.  The
                                                            maximum joint limit
                                                            must be greater
                                                            than zero and the
                                                            minimum must be
                                                            less than zero.
                                                         */
);

/*****************************************************************************

This function removes the joint limits from the input joint tag.  If the input
joint does not have joint limits defined, an error condition is returned.

Environment:  Internal and External

See Also:   UF_MOTION_set_joint_limits
            UF_OBJ_delete_object

History:  Created in NX2

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_remove_joint_limits
(
    const tag_t joint_tag   /* <I>
                               The tag of the joint to remove the joint
                               limits from.
                            */
);
/*****************************************************************************

This function initializes the input joint motion input structure with standard
default values.  It is highly recommended that all joint motion input
structures get initialized with this function before they are used.

Environment:  Internal and External

See Also:   UF_MOTION_init_joint_struct
            UF_MOTION_init_joint_limits_struct

History:  Created in NX2

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_init_joint_motion_input_struct
(
    UF_MOTION_joint_motion_input_t* motion_input_struct   /* <O>
                                                             The joint motion
                                                             input structure
                                                             to be initialized.
                                                          */
);

/*****************************************************************************

This function returns the joint motion input structure for the input joint
tag.  If motion input has not been defined for the joint, then an error
condition is returned.

Environment:  Internal and External

See Also:   UF_MOTION_ask_joint
            UF_MOTION_ask_joint_limits
            UF_MOTION_set_joint_motion_input

History:  Created in NX2

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_ask_joint_motion_input
(
    const tag_t joint_tag,  /* <I>
                               The tag of the joint to return the
                               motion input info of.  This tag is the
                               one returned from the UF_MOTION_create_joint
                               function.  It can also be found using
                               object cycle functions.
                               (eg. UF_OBJ_cycle_objs_by_type)
                            */
    UF_MOTION_joint_motion_input_t* motion_input_struct  /* <O>
                                                            The joint motion
                                                            input structure
                                                            for the input
                                                            joint tag.
                                                         */
);

/*****************************************************************************

This function sets the joint motion input to the input joint tag.  By default
all joints are created without joint motion input defined.  Joint motion input
can only be defined for revolute and slider joints.  If another type of joint
tag is used, an error condition will be returned.

Environment:  Internal and External

See Also:   UF_MOTION_ask_joint
            UF_MOTION_ask_joint_motion_input
            UF_MOTION_remove_joint_motion_input

History:  Created in NX2

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_set_joint_motion_input
(
    const tag_t joint_tag,  /* <I>
                               The tag of the joint to set the motion
                               input info to.  This tag must belong to
                               either a revolute or a slider joint.
                               This tag is the one returned from the
                               UF_MOTION_create_joint function.  It can
                               also be found using object cycle
                               functions (eg. UF_OBJ_cycle_objs_by_type).
                            */
    const UF_MOTION_joint_motion_input_t* input_struct  /* <I>
                                                           The joint motion
                                                           input structure
                                                           to be set on the
                                                           input joint tag.
                                                        */
);

/*****************************************************************************

This function removes the joint motion input from the input joint tag.  If
the input joint tag does not have a joint input defined, an error condition
is returned.

Environment:  Internal and External

See Also:   UF_MOTION_set_joint_motion_input
            UF_OBJ_delete_object

History:  Created in NX2

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_remove_joint_motion_input
(
    const tag_t joint_tag  /* <I>
                              The tag to remove the joint motion inputs from.
                           */
);
/*****************************************************************************

This function initializes the input coupler structure with standard default
values.  It is highly recommended that all coupler structures get initialized
with this function before they are used.

Environment:  Internal and External

See Also:   UF_MOTION_init_link_struct
            UF_MOTION_init_joint_struct

History:  Created in NX2

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_init_joint_coupler_struct
(
    UF_MOTION_joint_coupler_t* coupler_struct  /* <O>
                                                  The coupler structure
                                                  to be initialized.
                                               */
);

/*****************************************************************************

This function creates a joint coupler in the Scenario for Motion+ database
according to the parameters passed in through the joint coupler structure.
If successful, the tag of the new joint coupler is returned.

Environment:  Internal and External

See Also:   UF_MOTION_ask_joint_coupler
            UF_MOTION_set_joint_coupler

History:  Created in NX2.

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_create_joint_coupler
(
    UF_MOTION_joint_coupler_t* coupler_struct,  /* <I>
                                                   The required
                                                   parameters to
                                                   create the
                                                   joint coupler.
                                                */
    tag_t* joint_coupler_tag  /* <O>
                                 The new joint coupler tag.  This tag
                                 identifies the joint coupler in the database.
                              */
);

/*****************************************************************************

This function returns the joint coupler structure for an input joint coupler
tag.

Environment:  Internal and External

See Also:   UF_MOTION_set_joint_coupler
            UF_MOTION_ask_joint

History:  Created in NX2

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_ask_joint_coupler
(
    const tag_t joint_coupler_tag,  /* <I>
                                       The tag of the joint coupler to return.
                                       This tag is the one returned from the
                                       UF_MOTION_create_joint_coupler function.
                                       It can also be found using object cycle
                                       functions. (eg. UF_OBJ_cycle_objs_by_type)
                                    */
    UF_MOTION_joint_coupler_t* coupler_struct  /* <O>
                                                  The joint coupler
                                                  structure for the
                                                  input joint coupler tag.
                                               */
);

/*****************************************************************************

This function sets the input joint coupler parameters to the input joint
coupler tag.

Environment:  Internal and External

See Also:   UF_MOTION_ask_joint_coupler
            UF_MOTION_create_joint_coupler

History:  Created in NX2

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_set_joint_coupler
(
    const tag_t joint_coupler_tag,  /* <I>
                                       The tag of the joint coupler to set.
                                       This tag is the one returned from the
                                       UF_MOTION_create_joint_coupler function.
                                       It can also be found using object cycle
                                       functions. (eg. UF_OBJ_cycle_objs_by_type)
                                    */
    UF_MOTION_joint_coupler_t* coupler_struct  /* <I>
                                                  The joint coupler structure
                                                  holding the parameters to
                                                  be set to the input tag.
                                               */
);
/*****************************************************************************

This function initializes the input link structure with standard default
values.  It is highly recommended that all link structures get initialized
with this function before they are used.

Environment:  Internal and External

See Also:   UF_MOTION_init_link_mass_struct
            UF_MOTION_init_link_velocity_struct

History:  Created in NX2

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_init_link_struct
(
    UF_MOTION_link_t* link_struct  /* <I/O>
                                   The link structure to be initialized. */
);
/*****************************************************************************

This function creates a link in the Scenario for Motion+ database according to
the parameters passed in through the link structure.  If successful, the tag
of the new link is returned.  This function does not create initial velocities
or mass properties.  To add initial velocities or mass properties to a link,
use UF_MOTION_set_link_initial_velocity and UF_MOTION_set_link_mass_properties
after creating the link with this function.

Environment:  Internal and External

See Also:   UF_MOTION_ask_link
            UF_MOTION_set_link_mass_properties
            UF_MOTION_set_link_initial_velocity

History:  Created in NX2.

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_create_link
(
    UF_MOTION_link_t* link_struct,  /* <I>
                                       The required parameters
                                       to create the link.
                                    */
    tag_t* link_tag   /* <O>
                         The new link tag.  This tag identifies the
                         link in the database.
                      */
);

/*****************************************************************************

This function returns the link structure for an input link tag.

Environment:  Internal and External

See Also:   UF_MOTION_set_link
            UF_MOTION_ask_link_mass_properties
            UF_MOTION_ask_link_initial_velocity

History:  Created in NX2

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_ask_link
(
    const tag_t link_tag,  /* <I>
                              The tag of the link to return.
                              This tag is the one returned from
                              the UF_MOTION_create_link function.
                              It can also be found using object
                              cycle functions.
                              (eg. UF_OBJ_cycle_objs_by_type)
                           */
    UF_MOTION_link_t* link_struct  /* <O>
                                      The link structure for the input tag.
                                   */
);

/*****************************************************************************

This function sets the input link parameters to the input link tag.

Environment:  Internal and External

See Also:   UF_MOTION_ask_link
            UF_MOTION_set_link_mass_properties
            UF_MOTION_set_link_initial_velocity

History:  Created in NX2

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_set_link
(
    const tag_t link_tag,  /* <I>
                              The tag of the link to set.
                              This tag is the one returned from the
                              UF_MOTION_create_link function.
                              It can also be found using object cycle
                              functions. (eg. UF_OBJ_cycle_objs_by_type)
                           */
    const UF_MOTION_link_t* link_struct  /* <I>
                                            The link structure for the input tag.
                                         */
);
/*****************************************************************************

This function initializes the input link initial velocity structure with
standard default values.  It is highly recommended that all link initial
velocity structures get initialized with this function before they are used.

Environment:  Internal and External

See Also:   UF_MOTION_init_link_struct
            UF_MOTION_init_link_mass_struct

History:  Created in NX2

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_init_link_velocity_struct
(
    UF_MOTION_link_initial_velocity_t* link_velocity_struct  /* <I/O>
                                                             The link
                                                                initial
                                                                velocity
                                                                structure
                                                                to be
                                                                initialized. */
);
/*****************************************************************************

This function returns the link initial velocity for an input link tag.
All velocities are based on the work coordinate system of the model.

Environment:  Internal and External

See Also:   UF_MOTION_ask_link
            UF_MOTION_ask_link_mass_properties
            UF_MOTION_set_link_initial_velocity

History:  Created in NX2

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_ask_link_initial_velocity
(
    const tag_t link_tag,   /* <I>
                               The tag of the link to return the initial
                               velocity of.  This tag is the one returned
                               from the UF_MOTION_create_link function.
                               It can also be found using object cycle
                               functions.  (eg. UF_OBJ_cycle_objs_by_type)
                            */
    UF_MOTION_link_initial_velocity_t* init_vel_struct  /* <O>
                                                           Data structure
                                                           containing the
                                                           initial velocities.
                                                        */
);
/*****************************************************************************

This function sets the link initial velocities for the input link tag.
All velocities are based on the work coordinate system of the model.
Do not define more velocities than what is necessary to define the system.
There should never be more initial velocities than degrees of freedom.

Environment:  Internal and External

See Also:   UF_MOTION_set_link
            UF_MOTION_ask_link_initial_velocity
            UF_MOTION_remove_link_initial_velocity

History:  Created in NX2

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_set_link_initial_velocity
(
    const tag_t link_tag,   /* <I>
                               The tag of the link to set the initial
                               velocity.  This tag is the one returned
                               from the UF_MOTION_create_link function.
                               It can also be found using object cycle
                               functions. (eg. UF_OBJ_cycle_objs_by_type)
                            */
    const UF_MOTION_link_initial_velocity_t* init_vel_struct  /* <O>
                                                                 Data structure
                                                                 containing the
                                                                 initial velocities
                                                                 to be defined.
                                                              */
);
/*****************************************************************************

This function removes all initial velocities from the input link tag.

Environment:  Internal and External

See Also:   UF_MOTION_set_link_initial_velocity

History:  Created in NX2

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_remove_link_initial_velocity
(
    const tag_t link_tag  /* <I>
                             The tag of the link to remove the initial
                             velocities from.
                          */
);
/*****************************************************************************

This function initializes the input link mass structure with standard default
values.  It is highly recommended that all link mass structures get
initialized with this function before they are used.

Environment:  Internal and External

See Also:   UF_MOTION_init_link_struct
            UF_MOTION_init_link_velocity_struct

History:  Created in NX2

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_init_link_mass_struct
(
    UF_MOTION_link_mass_properties_t* link_mass_struct  /* <O> The link mass
                                                           structure to be
                                                           initialized. */
);

/*****************************************************************************

This function returns the link mass properties structure for an input link
tag.  Default mass properties will be calculated for solid bodies if
UF_MOTION_set_link_mass_properties has been called previously.  If the input
link tag has no solid bodies and no mass properties have been set on the link,
an error condition will be returned during solve.

Environment:  Internal and External

See Also:   UF_MOTION_ask_link
            UF_MOTION_set_link_mass_properties
            UF_MOTION_remove_link_mass_properties

History:  Created in NX2

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_ask_link_mass_properties
(
    const tag_t link_tag,   /* <I>
                               The tag of the link to return mass properties.
                               This tag is the one returned from the
                               UF_MOTION_create_link function.  It can also
                               be found using object cycle functions.
                               (eg. UF_OBJ_cycle_objs_by_type)
                            */
    UF_MOTION_link_mass_properties_t* mass_prop_struct  /* <O>
                                                           The link mass
                                                           property structure
                                                           for the input tag.
                                                           If the mass
                                                           properties have been
                                                           set by the user, or
                                                           default properties
                                                           were calculated,
                                                           they will be
                                                           returned here.
                                                        */
);

/*****************************************************************************

This function sets the link mass properties to the input link tag.  If the
link contains solid bodies, default mass properties are calculated.  If there
are no solid bodies in the link, then this function must be used to set
valid mass properties before any dynamic analyses can be performed.
Any user defined mass properties passed through this function will overwrite
the default or existing mass properties.

Environment:  Internal and External

See Also:   UF_MOTION_set_link
            UF_MOTION_ask_link_mass_properties
            UF_MOTION_remove_link_mass_properties

History:  Created in NX2

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_set_link_mass_properties
(
    const tag_t link_tag,   /* <I>
                               The tag of the link to set mass properties.
                               This tag is the one returned from the
                               UF_MOTION_create_link function.  It can also
                               be found using object cycle functions.
                               (eg. UF_OBJ_cycle_objs_by_type)
                            */
    const UF_MOTION_link_mass_properties_t* mass_prop_struct  /* <I>
                                                                 The link mass
                                                                 propertiy
                                                                 structure for
                                                                 the input tag.
                                                                 These mass
                                                                 properties will
                                                                 overwrite the
                                                                 mass properties
                                                                 that may have
                                                                 been created
                                                                 automatically
                                                                 for the link.
                                                              */
);

/*****************************************************************************

This function removes mass properties from the input link tag,
To revert to the default calculated mass properties for solid bodies,
another call must be made to UF_MOTION_set_link_mass_properties.
All of the non-solid geometry will be massless.  If there are no mass
properties defined on the input link, an error condition will be returned
during solve time.  To treat solid bodies as massless, use the mass
property toggle in the solver parameters structure.

Environment:  Internal and External

See Also:   UF_MOTION_set_link_mass_properties
            UF_OBJ_delete_object
            UF_MOTION_edit_solver_parameters

History:  Created in NX2

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_remove_link_mass_properties
(
    const tag_t link_tag   /* <I>
                              The tag of the link to remove the user
                              defined mass properties from.
                           */
);
/*****************************************************************************

This function initializes the input marker structure with standard default
values.  It is highly recommended that all marker structures get initialized
with this function before they are used.

Environment:  Internal and External

See Also:   UF_MOTION_init_link_struct
            UF_MOTION_init_joint_struct

History:  Created in NX2

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_init_marker_struct
(
    UF_MOTION_marker_t* marker_struct  /* <O>
                                          The marker structure to be
                                          initialized.
                                       */
);

/*****************************************************************************

This function creates a marker in the Scenario for Motion+ database according
to the parameters passed in through the marker structure.  This function is
used only for the creation of user defined markers.  If successful, the tag
of the new marker is returned.

Environment:  Internal and External

See Also:   UF_MOTION_ask_marker
            UF_MOTION_set_marker

History:  Created in NX2.

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_create_marker
(
    UF_MOTION_marker_t* marker_struct,  /* <I>
                                           The required parameters
                                           to create the marker.
                                        */
    tag_t* marker_tag   /* <O>
                           The new marker tag.  This tag identifies
                           the marker in the database.
                        */
);

/*****************************************************************************

This function returns the marker structure for an input marker tag.

Environment:  Internal and External

See Also:   UF_MOTION_set_marker
            UF_MOTION_create_marker

History:  Created in NX2

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_ask_marker
(
    const tag_t marker_tag,  /* <I>
                                The tag of the marker to return.  This tag is
                                the one returned from UF_MOTION_create_marker.
                                It can also be found using object cycle
                                functions. (eg. UF_OBJ_cycle_objs_by_type)
                             */
    UF_MOTION_marker_t* marker_struct  /* <O>
                                          The marker structure of the
                                          input tag.
                                       */
);

/*****************************************************************************

This function sets a new marker origin and a new orientation matrix
to the input marker tag.

Environment:  Internal and External

See Also:   UF_MOTION_ask_marker
            UF_MOTION_set_marker

History:  Created in NX2

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_set_marker
(
    const tag_t marker_tag,  /* <I>
                                The tag of the marker to set.  This tag is the
                                one returned from UF_MOTION_create_marker.  It
                                can also be found using object cycle functions.
                                (eg. UF_OBJ_cycle_objs_by_type)
                             */
    UF_MOTION_marker_t* marker_struct  /* <I>
                                          The marker structure for the
                                          input tag.
                                       */
);
/*****************************************************************************

This function initializes the input scalar force/torque structure with
standard default values.  It is highly recommended that all scalar force/
torque structures get initialized with this function before they are used.

Environment:  Internal and External

History:  Created in NX2

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_init_scalar_force_torque_struct
(
    UF_MOTION_scalar_force_torque_t* scalar_struct  /* <O>
                                                       The scalar force/torque
                                                       data structure
                                                       to be initialized.
                                                    */
);

/*****************************************************************************

This function creates a scalar force in the Scenario for Motion+ database
according to the parameters passed in through the scalar force/torque
structure.  If successful, the tag of the new scalar force is returned.

Environment:  Internal and External

See Also:   UF_MOTION_ask_scalar_force
            UF_MOTION_set_scalar_force

History:  Created in NX2.

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_create_scalar_force
(
    UF_MOTION_scalar_force_torque_t* force_struct,  /* <I>
                                                       The required
                                                       parameters to
                                                       create the scalar
                                                       force.
                                                    */
    tag_t* force_tag  /* <O>
                         The new scalar force tag.  This tag identifies
                         the scalar force in the database.
                      */
);

/*****************************************************************************

This function returns the scalar force structure for an input scalar force tag.

Environment:  Internal and External

See Also:   UF_MOTION_set_scalar_force

History:  Created in NX2

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_ask_scalar_force
(
    const tag_t force_tag,  /* <I>
                               The tag of the scalar force to return
                               information about.  This tag is the one
                               returned from UF_MOTION_create_scalar_force.
                               It can also be found using object cycle
                               functions. (eg. UF_OBJ_cycle_objs_by_type)
                            */
    UF_MOTION_scalar_force_torque_t* force_struct  /* <O>
                                                      The scalar force
                                                      structure for the
                                                      input tag.
                                                   */
);

/*****************************************************************************

This function sets the input scalar force parameters to the input force tag.
The parameters that can be set are the origin locations and the force
function.

Environment:  Internal and External

See Also:   UF_MOTION_ask_scalar_force

History:  Created in NX2

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_set_scalar_force
(
    const tag_t force_tag,  /* <I>
                               The tag of the scalar force to set.
                               This tag is the one returned from
                               UF_MOTION_create_scalar_force.
                               It can also be found using object cycle
                               functions. (eg. UF_OBJ_cycle_objs_by_type)
                           */
    const UF_MOTION_scalar_force_torque_t* force_struct  /* <I>
                                                            The scalar force
                                                            structure for
                                                            the input tag.
                                                         */
);

/*****************************************************************************

This function creates a scalar torque in the Scenario for Motion+ database
according to the parameters passed in through the scalar force/torque
structure.  If successful, the tag of the new scalar torque is returned.

Environment:  Internal and External

See Also:   UF_MOTION_ask_scalar_torque
            UF_MOTION_set_scalar_torque

History:  Created in NX2.

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_create_scalar_torque
(
    UF_MOTION_scalar_force_torque_t* torque_struct,  /* <I>
                                                        The required
                                                        parameters to
                                                        create the scalar
                                                        torque.
                                                     */
    tag_t* torque_tag  /* <O>
                          The new scalar torque tag.  This tag identifies
                          the scalar torque in the database.
                       */
);

/*****************************************************************************

This function returns the scalar torque structure for an input scalar
torque tag.

Environment:  Internal and External

See Also:   UF_MOTION_set_scalar_torque

History:  Created in NX2

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_ask_scalar_torque
(
    const tag_t torque_tag,  /* <I>
                                The tag of the scalar torque to return
                                information about.  This tag is the one
                                returned from UF_MOTION_create_scalar_torque.
                                It can also be found using object cycle
                                functions. (eg. UF_OBJ_cycle_objs_by_type)
                             */
    UF_MOTION_scalar_force_torque_t* torque_struct  /* <O>
                                                       The scalar torque
                                                       structure for the
                                                       input tag.
                                                    */
);

/*****************************************************************************

This function sets the input scalar torque parameters to the input torque tag.
The only parameter that can be set is the torque function.

Environment:  Internal and External

See Also:   UF_MOTION_ask_scalar_torque

History:  Created in NX2

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_set_scalar_torque
(
    const tag_t torque_tag,  /* <I>
                                The tag of the scalar torque to set.
                                This tag is the one returned from
                                UF_MOTION_create_scalar_torque.
                                It can also be found using object cycle
                                functions. (eg. UF_OBJ_cycle_objs_by_type)
                           */
    const UF_MOTION_scalar_force_torque_t* torque_struct  /* <I>
                                                             The scalar torque
                                                             structure for
                                                             the input tag.
                                                          */
);
/*****************************************************************************

This function initializes the input vector force/torque structure with
standard default values.  It is highly recommended that all vector force/
torque structures get initialized with this function before they are used.

Environment:  Internal and External

History:  Created in NX2

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_init_vector_force_torque_struct
(
    UF_MOTION_vector_force_torque_t* vector_struct  /* <O>
                                                       The vector force/torque
                                                       data structure
                                                       to be initialized.
                                                    */
);

/*****************************************************************************

This function creates a vector force or torque in the Scenario for Motion+
database according to the parameters passed in through the vector
force/torque structure.  If successful, the tag of the new vector force
or torque is returned.

Environment:  Internal and External

See Also:   UF_MOTION_ask_vector_force_torque
            UF_MOTION_set_vector_force_torque

History:  Created in NX2.

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_create_vector_force_torque
(
    UF_MOTION_vector_force_torque_t* vector_struct,  /* <I>
                                                        The required
                                                        parameters to
                                                        create the vector
                                                        force or torque.
                                                     */
    tag_t* vobject_tag  /* <O>
                           The new vector force or torque tag.
                           This tag identifies the vector force
                           or torque in the database.
                        */
);

/*****************************************************************************

This function returns the vector force/torque structure for an input
vector force or torque tag.

Environment:  Internal and External

See Also:   UF_MOTION_set_vector_force_torque

History:  Created in NX2

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_ask_vector_force_torque
(
    const tag_t vobject_tag,  /* <I>
                                 The tag of the vector force or torque to
                                 return information about.  This tag is
                                 the one returned from
                                 UF_MOTION_create_vector_force_torque.
                                 It can also be found using object cycle
                                 functions. (eg. UF_OBJ_cycle_objs_by_type)
                             */
    UF_MOTION_vector_force_torque_t* vector_struct  /* <O>
                                                       The vector force/
                                                       torque structure
                                                       for the input tag.
                                                    */
);

/*****************************************************************************

This function sets the input vector force/torque parameters to the input
vector force or torque tag.

Environment:  Internal and External

See Also:   UF_MOTION_ask_vector_force_torque

History:  Created in NX2

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_set_vector_force_torque
(
    const tag_t vobject_tag,  /* <I>
                                 The tag of the vector force or torque
                                 to set.  This tag is the one returned from
                                 UF_MOTION_create_vector_force_torque.
                                 It can also be found using object cycle
                                 functions. (eg. UF_OBJ_cycle_objs_by_type)
                             */
    UF_MOTION_vector_force_torque_t* vector_struct  /* <I>
                                                       The vector force/
                                                       torque structure
                                                       for the input tag.
                                                    */
);
/*****************************************************************************

This function is used to calculate the static equilibrium of the motion model.
Following a successful completion of this function, there will be one results
step in the database.  Similar to UF_MOTION_solve_model, these database results
can be accessed by the following:

      1) Packaging options, including measure, trace, and interference.
      2) Write the results to disk using UF_MOTION_export_adams_res_file.
      3) Get specific results from a joint or marker.

Environment:  Internal and External

See Also:   UF_MOTION_step_articulation
            UF_MOTION_solve_model
            UF_MOTION_review_adams_res_file
            UF_MOTION_ask_velocity_results
            UF_MOTION_ask_force_results

History:  Released in V18

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_calculate_static_equilibrium(
    int* static_result_steps /*<O>
                               Total number of successful steps that are available in
                               the database.
                              */);
                              /*****************************************************************************************************************************
                              Exports the current Motion model as an ANL file which can then be read
                              into Adams or any other application which reads Adams ANL files.

                              Environment: Internal or External

                              See Also:     UF_MOTION_init_stl_parameters_struct
                                            UF_MOTION_solve_model
                                            UF_MOTION_calculate_static_equilibrium
                                            UF_MOTION_step_articulation
                                            UF_MOTION_export_adams_res_file

                              History: Released in NX3
                              ********************************************************************************************************************************/
                              /*************************************************************************
                              Initialize the UF_MOTION_stl_parameters_t structure with default values
                              in preparation to send to UF_MOTION_export_adams_anl_file.

                              Environment: Internal or External

                                 See Also:  UF_MOTION_export_adams_anl_file

                              History: Released in NX3
                              *************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_init_stl_parameters_struct
(
    UF_MOTION_stl_parameters_t* stl_params  /* <O>
                                              The empty struct to retrieve the
                                              default STL parameters.
                                              */
);
extern UFUN_CAEEXPORT int UF_MOTION_export_adams_anl_file
(
    const char* file_name,  /* <I>
                           The filename of the .anl file to write.  It
                           should include the entire path to the file.
                           The filename should end with .anl followed by a
                           terminating NULL character.
                           */
    UF_MOTION_anl_geometry_format_t geometry_format, /* <I>
                                                        The format to export the geometry.
                                                    */
    UF_MOTION_stl_parameters_p_t    stl_params      /* <I>
                                                       If geometry_format == UF_MOTION_stl, then
                                                       this arg contains the parameters to export
                                                       the geometry as STL data.  Ignored if
                                                       geometry_format != UF_MOTION_stl.
                                                    */
);
/*****************************************************************************

This function initializes the solver for an articulation run.  It must be
called prior to any calls to UF_MOTION_step_articulation and it must be paired
with a call to UF_MOTION_terminate_articulation.

Environment:  Internal and External

See Also:   UF_MOTION_step_articulation
            UF_MOTION_edit_artic_step_size
            UF_MOTION_terminate_articulation
            UF_MOTION_ask_velocity_results
            UF_MOTION_ask_force_results

History:  Created in V18

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_init_articulation(void);

/*****************************************************************************

This function solves the motion model for the number of steps of the
articulation model.  It is a position based analysis.  Multiple calls to this
function will be appended together to form the full analysis.  For example, if
this function is called successfully for seven times with a single step each time,
the analysis results in the database will have seven steps.
The exception case is when solver has locked-up, the number of total steps is not
equal to the number of calls.
The difference is it will not append results onto the end of a time-based simulation.
Instead, the first call to this function following a time-based simulation
or a static analysis will clear the database of those results.
Similar to UF_MOTION_solve_model, the database results can be accessed by the following:

      1) Packaging options, including measure, trace, and interference.
      2) Write the results to disk using UF_MOTION_export_adams_res_file.
      3) Get specific results from a joint or marker.

Environment:  Internal and External

See Also:   UF_MOTION_solve_model
            UF_MOTION_edit_artic_step_size
            UF_MOTION_ask_velocity_results
            UF_MOTION_ask_force_results

History:  Released in V18

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_step_articulation(
    const int num_steps,   /*<I>
                             The number of steps to take for the step sizes
                             currently stored on the articulation joints.
                           */
    int* total_steps   /*<O>
                         The number of successful steps that are available in
                         the database.
                       */
);

/*****************************************************************************

This function terminates the solver for an articulation run.  It must be
called after all calls to UF_MOTION_step_articulation and it must be paired
with a call to UF_MOTION_init_articulation.  Failure to terminate the solver
after an articulation run may corrupt the solver.

Environment:  Internal and External

See Also:   UF_MOTION_init_articulation
            UF_MOTION_step_articulation

History:  Created in V18

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_MOTION_terminate_articulation(void);
#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY
#endif /* UF_CAE_RETIRING */
