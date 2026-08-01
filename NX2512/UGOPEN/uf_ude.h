/*******************************************************************************
                Copyright (c) 2001 Unigraphics Solutions, Inc.
                      Unpublished - All rights reserved
================================================================================
 *
 * 
 *
 * File description:
 *
 * This module allows programmers in CAM to work with the User Defined Machine 
 * Control Events that can be specified for Operation and Group objects. The 
 * functions in this file provide the interface to interrogate and edit the
 * User Defined Machine Control Events.
 *
 *
 ******************************************************************************/
#ifndef UF_UDE_H_INCLUDED
#define UF_UDE_H_INCLUDED

/***************************** Include Files **********************************/
#include <uf_defs.h>
#include <uf_cam_errors.h>
#include <libufun_cam_exports.h>

#ifdef __cplusplus
extern "C" {
#endif

/***************************** Public Defines *********************************/

/***************************** Public Typedefs ********************************/

/* 
 * A User Defined Machine Control Event object.
 */
typedef void   *UF_UDE_t;

/* 
 * These are the possible type of Machine Control Sets.
 * the following set type is applicable only to Machine Control Operations 
 *        UF_UDE_MACH_CNTRL_OPER_SET
 * and the following are applicable to all other Operations and Group objects
 *        UF_UDE_START_SET
 *        UF_UDE_END_SET
 */
enum UF_UDE_set_type_e
{
   UF_UDE_START_SET,
   UF_UDE_END_SET,
   UF_UDE_MACH_CNTRL_OPER_SET
};

typedef enum UF_UDE_set_type_e UF_UDE_set_type_t;

/* 
 * These are the possible values that an optional parameter of a
 * User Defined Machine Control Event can have. 
 */
enum UF_UDE_param_toggle_e
{
   UF_UDE_PARAM_INACTIVE,
   UF_UDE_PARAM_ACTIVE
};

typedef enum UF_UDE_param_toggle_e UF_UDE_param_toggle_t;

/* 
 * A User Defined Machine Control Event parameter can 
 * be one of the following type. 
 *
 * NOTE: For asking or setting the value of a parameter of type 
 *       UF_UDE_PARAM_TYPE_OPTION use the UF_UDE_ask_string 
 *       and UF_UDE_set_string functions.
 */
enum UF_UDE_param_type_e
{
   UF_UDE_PARAM_TYPE_INT,
   UF_UDE_PARAM_TYPE_DOUBLE,
   UF_UDE_PARAM_TYPE_STRING,
   UF_UDE_PARAM_TYPE_BOOLEAN,
   UF_UDE_PARAM_TYPE_OPTION,
   UF_UDE_PARAM_TYPE_POINT,
   UF_UDE_PARAM_TYPE_VECTOR
};

typedef enum UF_UDE_param_type_e UF_UDE_param_type_t;

/**************************************************************************** 
 * In addition to all the User Defined Machine Control Events defined in the
 * 'ude' file, the system also has 8 Machine Control Events that are defined
 * in the same format as the User Defined Machine Control Events. They are
 * as described below
 *
 * 1) The System 'Goto' Machine Control Event
 *     This Event can be specified for all Operations
 *     ___________________________________________________________________
 *     Event Name: Goto
 *     __________________________________________________________________
 *     Parameter Names  Parameter Type               Possible Values
 *     ___________________________________________________________________
 *     point_x          UF_UDE_PARAM_TYPE_DOUBLE
 *     point_y          UF_UDE_PARAM_TYPE_DOUBLE
 *     point_z          UF_UDE_PARAM_TYPE_DOUBLE
 *     tl_axis_flag   UF_UDE_PARAM_TYPE_BOOLEAN TRUE/FALSE
 *     tl_axis_i      UF_UDE_PARAM_TYPE_DOUBLE
 *     tl_axis_j      UF_UDE_PARAM_TYPE_DOUBLE
 *     tl_axis_k      UF_UDE_PARAM_TYPE_DOUBLE
 *     feed_rate        UF_UDE_PARAM_TYPE_DOUBLE
 *     feed_unit        UF_UDE_PARAM_TYPE_OPTION  "NONE","Per Min","Per Rev"
 *     custom_feed_flag UF_UDE_PARAM_TYPE_BOOLEAN TRUE/FALSE 
 *
 * 2) The System From Machine Control Event
 *     This Event can be specified for Machine Control operations only
 *     ___________________________________________________________________
 *     Event Name: From
 *     __________________________________________________________________
 *     Parameter Names  Parameter Type               Possible Values
 *     ___________________________________________________________________
 *     point_x          UF_UDE_PARAM_TYPE_DOUBLE
 *     point_y          UF_UDE_PARAM_TYPE_DOUBLE
 *     point_z          UF_UDE_PARAM_TYPE_DOUBLE
 *     tl_axis_flag     UF_UDE_PARAM_TYPE_BOOLEAN TRUE/FALSE
 *     tl_axis_i        UF_UDE_PARAM_TYPE_DOUBLE
 *     tl_axis_j        UF_UDE_PARAM_TYPE_DOUBLE
 *     tl_axis_k        UF_UDE_PARAM_TYPE_DOUBLE
 *
 * 3) The System GoHome Machine Control Event
 *     This Event can be specified for Machine Control operations only
 *     ___________________________________________________________________
 *     Event Name: GoHome
 *     __________________________________________________________________
 *     Parameter Names  Parameter Type               Possible Values
 *     ___________________________________________________________________
 *     point_x          UF_UDE_PARAM_TYPE_DOUBLE
 *     point_y          UF_UDE_PARAM_TYPE_DOUBLE
 *     point_z          UF_UDE_PARAM_TYPE_DOUBLE
 *     tl_axis_flag     UF_UDE_PARAM_TYPE_BOOLEAN TRUE/FALSE
 *     tl_axis_i        UF_UDE_PARAM_TYPE_DOUBLE
 *     tl_axis_j        UF_UDE_PARAM_TYPE_DOUBLE
 *     tl_axis_k        UF_UDE_PARAM_TYPE_DOUBLE
 *
 * 4) The Marker 'From_Marker' Machine Control Event
 *     This Event can be specified for all Operations except
 *     Machine Control Operations. Also this is only valid when the 
 *     Machine Control Event set is UF_UDE_START_SET 
 *     ___________________________________________________________________
 *     Event Name: From_Marker
 *
 *     It has no Parameters
 *     __________________________________________________________________
 *
 * 5) The Marker 'Start_Marker' Machine Control Event
 *     This Event can be specified for all Operations except
 *     Machine Control Operations. Also this is only valid when the 
 *     Machine Control Event set is UF_UDE_START_SET 
 *     ___________________________________________________________________
 *     Event Name: Start_Marker
 *
 *     It has no Parameters
 *     __________________________________________________________________
 *
 * 6) The Marker 'Approach_Marker' Machine Control Event
 *     This Event can be specified for all Operations except
 *     Machine Control Operations. Also this is only valid when the 
 *     Machine Control Event set is UF_UDE_START_SET 
 *     ___________________________________________________________________
 *     Event Name: Approach_Marker
 *
 *     It has no Parameters
 *     __________________________________________________________________
 *
 * 5) The Marker 'Return_Marker' Machine Control Event
 *     This Event can be specified for all Operations except
 *     Machine Control Operations. Also this is only valid when the 
 *     Machine Control Event set is UF_UDE_END_SET 
 *     ___________________________________________________________________
 *     Event Name: Return_Marker
 *
 *     It has no Parameters
 *     __________________________________________________________________
 *
 * 5) The Marker 'GoHome_Marker' Machine Control Event
 *     This Event can be specified for all Operations except
 *     Machine Control Operations. Also this is only valid when the 
 *     Machine Control Event set is UF_UDE_END_SET 
 *     ___________________________________________________________________
 *     Event Name: GoHome_Marker
 *
 *     It has no Parameters
 *     __________________________________________________________________
 *
 * 6) The Marker 'Spindle_Marker' Machine Control Event
 *     This Event can be specified for all Operations. This marker 
 *     output the SPINDL post command . Using this marker we can change the
 *     location of output of Spindle post command
 *     ___________________________________________________________________
 *     Event Name: Spindle_Marker
 *
 *     It has no Parameters
 *     __________________________________________________________________
 *
 * 7) The Marker 'Tool_Change_Marker' Machine Control Event
 *     This Event can be specified for all Operations. This marker 
 *     output the  LOAD/ TOOL post command . Set the UF_PARAM_OUTPUT_LOAD_TOOL
 *     to TRUE. Then only Load tool will appear in the program.
 *     ___________________________________________________________________
 *     Event Name: Tool_Change_Marker
 *
 *     It has no Parameters
 *     __________________________________________________________________
 *
 *****************************************************************************/

/************************* Public Function Definitions ************************/

/*******************************************************************************
 This function returns the name of the User Defined Machine Control Event object
 'ude_obj' in 'ude_name'. 

Environment: Internal  and  External

See Also:

History: Originally released in V18.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_UDE_ask_name
(
   UF_UDE_t        ude_object,   /* <I>  see above */
   char          **ude_name      /* <OF> see above *
                                    NOTE: The memory allocated for ude_name
                                          has to be freed by calling UF_free
                                          on ude_name */
);

/*******************************************************************************
 This function returns the number and names of parameters of the User Defined 
 Machine Control Event object 'ude_obj'. 

 NOTE: The returned array must be freed by calling UF_free_string_array.

Environment: Internal  and  External

See Also:

History: Originally released in V18.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_UDE_ask_params
(
   UF_UDE_t      ude_obj,          /* <I> see above */
   int          *number_of_params, /* <O> Number of parameters */
   char       ***param_names       /* <OF,len:number_of_params>
                                        Names of the parameters 
                                        The returned array must be freed by 
                                        calling UF_free_string_array.
                                    */
);

/*******************************************************************************
 This function returns type of a parameter of name 'param_name' in the User 
 Defined Machine Control Event object 'ude_obj'. 

Environment: Internal  and  External

See Also:

History: Originally released in V18.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_UDE_ask_param_type
(
   UF_UDE_t             ude_obj,    /* <I> see above */
   char                *param_name, /* <I> see above */
   UF_UDE_param_type_t *param_type  /* <O> Type of the parameter*/
);

/*******************************************************************************
 This function returns TRUE in 'response' if the parameter of the User 
 Defined Machine Control Event object 'ude_obj' is optional and FALSE if not

Environment: Internal  and  External

See Also:

History: Originally released in V18.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_UDE_is_param_optional
(
   UF_UDE_t                ude_obj,    /* <I> see above */
   char                   *param_name, /* <I> see above */
   logical                *response    /* <I> see above */
);

/*******************************************************************************
 This function returns in 'toggle' the toggle status of the parameter specified
 by 'param_name' in the User Defined Machine Control Event object 'ude_obj'.

Environment: Internal  and  External

See Also:

History: Originally released in NX3
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_UDE_ask_param_toggle
(
   UF_UDE_t                ude_obj,    /* <I> see above */
   char                   *param_name, /* <I> see above */
   UF_UDE_param_toggle_t   *toggle     /* <O> see above */
);

/*******************************************************************************
 This function sets the parameter of name 'param_name' in the User 
 Defined Machine Control Event object 'ude_obj' to be active or inactive 
 as speicifed by the value of 'toggle'.

Environment: Internal  and  External

See Also:

History: Originally released in V18.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_UDE_set_param_toggle
(
   UF_UDE_t                ude_obj,    /* <I> see above */
   char                   *param_name, /* <I> see above */
   UF_UDE_param_toggle_t   toggle      /* <I> see above */
);

/*******************************************************************************
 This function assigns the value 'value' to the parameter specified by
 'param_name' for the object specified by 'ude_obj'.

Environment: Internal  and  External

See Also:

History: Originally released in V18.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_UDE_set_integer
(
   UF_UDE_t             ude_obj,    /* <I> see above */
   char                *param_name, /* <I> see above */
   int                  value       /* <I> see above */
);

/*******************************************************************************
 This function returns in 'value' the value of the parameter specified by
 'param_name'. It is the value of this parameter that is currently being
 used by the object specified by 'ude_obj'.

Environment: Internal  and  External

See Also:

History: Originally released in V18.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_UDE_ask_integer
(
   UF_UDE_t             ude_obj,    /* <I> see above */
   char                *param_name, /* <I> see above */
   int                 *value       /* <O> see above */
);

/*******************************************************************************
 This function assigns the value 'value' to the parameter specified by
 'param_name' for the object specified by 'ude_obj'.

Environment: Internal  and  External

See Also:

History: Originally released in V18.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_UDE_set_double
(
   UF_UDE_t             ude_obj,    /* <I> see above */
   char                *param_name, /* <I> see above */
   double               value       /* <I> see above */
);

/*******************************************************************************
 This function returns in 'value' the value of the parameter specified by
 'param_name'. It is the value of this parameter that is currently being
 used by the object specified by 'ude_obj'.

Environment: Internal  and  External

See Also:

History: Originally released in V18.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_UDE_ask_double
(
   UF_UDE_t             ude_obj,    /* <I> see above */
   char                *param_name, /* <I> see above */
   double              *value       /* <O> see above */
);

/*******************************************************************************
 This function assigns the value 'value' to the parameter specified by
 'param_name' for the object specified by 'ude_obj'.

Environment: Internal  and  External

See Also:

History: Originally released in V18.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_UDE_set_string
(
   UF_UDE_t             ude_obj,    /* <I> see above */
   char                *param_name, /* <I> see above */
   char                *value       /* <I> see above */
);

/*******************************************************************************
 This function returns in 'value' the value of the parameter specified by
 'param_name'. It is the value of this parameter that is currently being
 used by the object specified by 'ude_obj'.

Environment: Internal  and  External

See Also:

History: Originally released in V18.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_UDE_ask_string
(
   UF_UDE_t             ude_obj,    /* <I> see above */
   char                *param_name, /* <I> see above */
   char               **value       /* <OF> see above. 
                                       This should be freed with a call to
                                       UF_free on value */
);

/*******************************************************************************
 This function assigns the value 'value' to the parameter specified by
 'param_name' for the object specified by 'ude_obj'.

Environment: Internal  and  External

See Also:

History: Originally released in V18.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_UDE_set_boolean
(
   UF_UDE_t             ude_obj,    /* <I> see above */
   char                *param_name, /* <I> see above */
   logical              param_value /* <I> see above */
);

/*******************************************************************************
 This function returns in 'value' the value of the parameter specified by
 'param_name'. It is the value of this parameter that is currently being
 used by the object specified by 'ude_obj'.

Environment: Internal  and  External

See Also:

History: Originally released in V18.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_UDE_ask_boolean
(
   UF_UDE_t             ude_obj,    /* <I> see above */
   char                *param_name, /* <I> see above */
   logical             *value       /* <O> see above */
);

/*******************************************************************************
 This function assigns the value 'smart_point_tag' to the parameter specified by
 'param_name' for the object specified by 'ude_obj'.

 NOTE: The tag that is passed to this function has to be the tag of a 
       smart point

Environment: Internal  and  External

See Also:

History: Originally released in V18.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_UDE_set_point
(
   UF_UDE_t             ude_obj,        /* <I> see above */
   char                *param_name,     /* <I> see above */
   tag_t                smart_point_tag /* <I> see above */
);

/*******************************************************************************
 This function returns in 'smart_point_tag' the value of the parameter 
 specified by 'param_name'. It is the value of this parameter that is 
 currently being used by the object 'ude_obj'.

 NOTE: The 'smart_point_tag' is the tag of a smart point

Environment: Internal  and  External

See Also:

History: Originally released in V18.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_UDE_ask_point
(
   UF_UDE_t             ude_obj,        /* <I> see above */
   char                *param_name,     /* <I> see above */
   tag_t               *smart_point_tag /* <O> see above */
);

/*******************************************************************************
 This function assigns the value 'smart_vector_tag' to the parameter specified 
 by 'param_name' for the object specified by 'ude_obj'.

 NOTE: The tag that is passed to this function has to be the tag of a 
       smart vector (also known as a "smart direction" object

Environment: Internal  and  External

See Also:

History: Originally released in V18.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_UDE_set_vector
(
   UF_UDE_t             ude_obj,         /* <I> see above */
   char                *param_name,      /* <I> see above */
   tag_t                smart_vector_tag /* <I> see above */
);

/*******************************************************************************
 This function returns in 'smart_vector_tag' the value of the parameter 
 specified by 'param_name'. It is the value of this parameter that is 
 currently being used by the object 'ude_obj'.

 NOTE: The 'smart_vector_tag' is the tag of a smart vector

Environment: Internal  and  External

See Also:

History: Originally released in V18.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_UDE_ask_vector
(
   UF_UDE_t             ude__obj,        /* <I> see above */
   char                *param_name,      /* <I> see above */
   tag_t               *smart_vector_tag /* <O> see above */
);

#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif /*UF_UDE_H_INCLUDED*/
