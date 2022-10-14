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


#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY
#endif /* UF_CAE_RETIRING */
