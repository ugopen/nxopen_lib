/*******************************************************************************
            Copyright (c) 1998-2000 Unigraphics Solutions, Inc.
                     Unpublished - All rights reserved
================================================================================



File description:

   This module allows the user to perform functions which are particular to
   Operations as compared to the functions which can be performed on Operations
   when an Operation is viewed as a UF_PARAM object (which it is). See the
   prototypes in this file for examples of what these functions are.

   UF_OPER items are found in templates. In particular, they are found in
   Groups contained inside of a Setup. They are typically accessed via their
   template or as a member of a Group.
*******************************************************************************/

#ifndef UF_OPER_H_INCLUDED
#define UF_OPER_H_INCLUDED

/***************************** Include Files **********************************/
#include <uf_defs.h>
#include <uf_oper_spec.h>
#include <uf_cam_errors.h>
#include <libufun_cam_exports.h>
#include <uf_cutter.h>


#ifdef __cplusplus
extern "C" {
#endif

/******************************** Defines *************************************/

/*
 UF_OPER_MAX_NAME_LEN is being deprecated because NX is moving to support 
 multibyte characters.  User written programs should start using the 
 new definitions:
   UF_OPER_MAX_NAME_BUFSIZE should be used for buffer allocations and memory 
                     allocations, e.g. char my_fspec[UF_OPER_MAX_NAME_BUFSIZE];
   UF_OPER_MAX_NAME_NCHARS  should be used to limit the number of characters in
                     a buffer.  NX code will enforce these limits.      
 New routines have been added which will help in this transition:       
    UF_TEXT_count_characters() will count the number of characters in a 
    buffer.                                                             
    UF_TEXT_terminate_chars() will terminate a C string after the given 
    number of characters.                                               

*/
#define UF_OPER_MAX_NAME_NCHARS   UF_OPER_OPNAME_NCHARS
#define UF_OPER_MAX_NAME_BUFSIZE NX_BUFSIZE(UF_OPER_MAX_NAME_NCHARS)

/*  */
#define UF_OPER_MAX_NAME_LEN   (UF_OPER_MAX_NAME_BUFSIZE-1)
/*  */

/***************************** Public Typedefs ********************************/

/* Operation Status: for all bit fields if the bit == 0 then the condition
 *                   represented by that bit is FALSE, otherwise it is TRUE
 */
struct UF_OPER_status_s
{
   unsigned int   is_edited         :1;  /* Has operation been edited ? */
   unsigned int   toolpath_exists   :1;  /* Does tool path exist ? */
   unsigned int   toolpath_edited   :1;  /* Has tool path been edited since
                                          * the last time it was posted ?
                                          */
   unsigned int   open              :29;
};

typedef struct UF_OPER_status_s UF_OPER_status_t, *UF_OPER_status_p_t;

/* 
Operation Status: for all structure fields if it is == 0 then the condition
 *                   represented by that field is FALSE, otherwise it is TRUE
 */
struct UF_OPER_status1_s
{
   unsigned int   is_edited;        /* Has operation been edited ? */
   unsigned int   toolpath_exists;  /* Does tool path exist ? */
   unsigned int   toolpath_edited ;  /* Has tool path been edited since
                                          * the last time it was posted ?
                                          */
};

typedef struct UF_OPER_status1_s UF_OPER_status1_t, *UF_OPER_status1_p_t;

/* 
 */

/* Machining Modes */
enum UF_OPER_mach_mode_e
{
   UF_OPER_MACH_MODE_UNDEF, /* Undefined */
   UF_OPER_MACH_MODE_MILL,
   UF_OPER_MACH_MODE_LATHE,
   UF_OPER_MACH_MODE_DRILL,
   UF_OPER_MACH_MODE_WEDM,
   UF_OPER_MACH_MODE_TURN,
   UF_OPER_MACH_MODE_LAST     /*** This must be the last item ***/
};

typedef enum UF_OPER_mach_mode_e UF_OPER_mach_mode_t;

/************************* Public Function Definitions ************************/

/*******************************************************************************
 This function returns in 'group' the tag of the program group object that the
 specified 'oper' is contained in.

Environment: Internal  and  External

See Also:

History: Originally released in V16.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_OPER_ask_program_group
(
   tag_t    oper, /* <I> - see above */
   tag_t   *group /* <O> - see above */
);


/*******************************************************************************
 This function returns in 'group' the tag of the method group object that the
 specified 'oper' is contained in.

Environment: Internal  and  External

See Also:

History: Originally released in V16.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_OPER_ask_method_group
(
   tag_t    oper, /* <I> - see above */
   tag_t   *group /* <O> - see above */
);


/*******************************************************************************
 This function returns in 'group' the tag of the geometry group object that the
 specified 'oper' is contained in.

Environment: Internal  and  External

See Also:

History: Originally released in V16.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_OPER_ask_geom_group
(
   tag_t    oper, /* <I> - see above */
   tag_t   *group /* <O> - see above */
);


/*******************************************************************************
 This function returns in 'group' the tag of the cutter group object that the
 specified 'oper' is contained in.

Environment: Internal  and  External

See Also:

History: Originally released in V16.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_OPER_ask_cutter_group
(
   tag_t    oper, /* <I> - see above */
   tag_t   *group /* <O> - see above */
);


/*******************************************************************************
 This function returns in 'status' the status of the specified Operation 'oper'.
 See the definition of UF_OPER_status_t in this file for a description of the
 status.

Environment: Internal  and  External

See Also:

History: Originally released in V16.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_OPER_ask_status
(
   tag_t               oper, /* <I> - see above */
   UF_OPER_status_t   *status /* <O> - see above */
);/*<RETIRE_NXOPEN>*/

/*******************************************************************************
In order to provide appropriate .NET binding for UF_OPER_ask_status, 
UF_OPER_ask_status1 is introduced.

Note: C/C++ users can continue to use UF_OPER_ask_status.

For documentation, refer to documentation of UF_OPER_ask_status.

Environment: Internal  and  External

See Also:

History: Originally released in NX10.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_OPER_ask_status1
(
   tag_t               oper, /* <I> - tag of the Operation */
   UF_OPER_status1_t   *status /* <O> - status of specified operation */
);

/*******************************************************************************
 This function returns the NX entity subtype (as found in uf_object_types.h)
 of the specified 'oper'. It is returned in 'type'.

Environment: Internal  and  External

See Also:

History: Originally released in V16.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_OPER_ask_oper_type
(
   tag_t   oper, /* <I> - see above */
   int    *type  /* <O> - see above */
);


/*******************************************************************************
 This function returns in 'mode' the machining mode of the specified 'oper'.

Environment: Internal  and  External

See Also:

History: Originally released in V16.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_OPER_ask_machining_mode
(
   tag_t                  oper, /* <I> - see above */
   UF_OPER_mach_mode_t   *mode  /* <O> - see above */
);


/*******************************************************************************
 This function determines if the tool path in the specified 'oper' gouges
 any geometry in the operation.

Environment: Internal  and  External

See Also:

History: Originally released in V16.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_OPER_is_path_gouged
(
   tag_t      oper,  /* <I> - see above */
   logical   *result /* <O> - TRUE if the if the tool path gouges any geometry.
                              FALSE otherwise.  */
);



/*******************************************************************************
 This function returns in 'name' the name of the specified 'oper'.

Environment: Internal  and  External

See Also:

History: Originally released in V16.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_OPER_ask_name_from_tag
(
   tag_t      oper, /* <I> - see above */
   char       name[UF_OPER_MAX_NAME_BUFSIZE+1] /* <O> - see above */
);


/******************************************************************************
Does the operation have an In-Process-Workpiece or not.

Environment: Internal  and  External

See Also:

History: Originally released in V16.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_OPER_has_self_ipw
(
   tag_t      oper, /* <I> The tag of the operation to be checked. */
   logical    *result /* <O> The result, TRUE if the operation has an
                             in-process-workpiece, FALSE otherwise.
                      */
);

/*******************************************************************************
 This function deletes the internal path associated with the specified 'oper'.

Environment: Internal  and  External

See Also:

History: Originally released in V16.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_OPER_delete_tool_path
(
   tag_t    oper /* <I> - see above */
);

/*******************************************************************************
 This function creates an operation based upon the specified operation template
 type and subtype. All parameters of the newly created operation are derived
 from the specified template object.

Environment: Internal  and  External

See Also:

History: Originally released in V16.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_OPER_create
(
   char    *type_name, /* <I> - the operation template type name */
   char    *subtype_name, /* <I> - the operation template subtype name */
   tag_t   *new_object  /* <O> - the tag of the newly created operation */
);

/***************************************************************
 *   Query the number of selected tracking points in an Operation.
 *
 * Return :
 *    UF_CUTTER_ERROR_TAG_NOT_CORRECT_TYPE
 *        The input tag is not an operation
 *
 * Environment: Internal  and  External
 *
 * See Also:
 * History: Released in NX2.0
 *************************************************************/
extern UFUN_CAMEXPORT int UF_OPER_ask_selected_tracking_point_count
(
    tag_t  object_tag,  /* <I> the tag of the operation of the points  */
    int *count          /* <O> the number of selected tracking points */
);

/***************************************************************
 *   Select a tracking point in an Operation
 *.
 *  Note:
 *      Specifying a tracking point for an operation will result in setting the Z-offset,
 *      Adjust and Cutcom data for the operation from that of the selected tracking
 *      point.  If a local override for this data is desired, it must be specified after
 *      selecting the tracking point.
 *
 * Return :
 *    UF_CUTTER_ERROR_TAG_NOT_CORRECT_TYPE
 *        The input tag is not an operation
 *
 * Environment: Internal  and  External
 *
 * See Also:
 * History: Released in NX2.0
 *************************************************************/
extern UFUN_CAMEXPORT int UF_OPER_select_tracking_point
(
    tag_t  object_tag,  /* <I> the tag of the operation  */
    char name[]         /* <I> the name of the selected tracking point */
);

/***************************************************************
 *   Deselect a tracking point in an Operation.
 *
 * Return :
 *    UF_CUTTER_ERROR_TAG_NOT_CORRECT_TYPE
 *        The input tag is not an operation
 *
 * Environment: Internal  and  External
 *
 * See Also:
 * History: Released in NX2.0
 *************************************************************/
extern UFUN_CAMEXPORT int UF_OPER_deselect_tracking_point
(
    tag_t  object_tag,  /* <I> the tag of the operation  */
    char name[]         /* <I> the name of the tracking point to deselect  */
);

/***************************************************************
 *   Query the data of a selected tracking point in an Operation.
 *
 * Return :
 *    UF_CUTTER_ERROR_TAG_NOT_CORRECT_TYPE
 *        The input tag is not an operation
 *
 * Environment: Internal  and  External
 *
 * See Also:
 * History: Released in NX2.0
 **************************************************************/
extern UFUN_CAMEXPORT int UF_OPER_ask_selected_point_data
(
    tag_t  object_tag,  /* <I> the tag of the operation of the points  */
    int  index,         /*  <I> index of tracking point in parent (from 0 to the
                                number of selected points - 1)  */
    UF_CUTTER_tracking_point_data_t *data /* <O> the data of the point  */
);

/***************************************************************
 *   Query the data of a selected turn tracking point in an Operation.
 *
 * Return :
 *    UF_CUTTER_ERROR_TAG_NOT_CORRECT_TYPE
 *        The input tag is not an operation
 *
 * Environment: Internal  and  External
 *
 * See Also:
 * History: Released in NX5.0
 **************************************************************/
extern UFUN_CAMEXPORT int UF_OPER_ask_selected_turn_point_data
(
    tag_t  object_tag,  /* <I> the tag of the operation of the points  */
    int  index,         /*  <I> index of turn tracking point in parent (from 0 to the
                                number of selected points - 1)  */
    UF_CUTTER_turn_tracking_point_data_t *data /* <O> the data of the point  */
);

/******************************************************************
 *
 * This function queries the reference cutter of an operation.
 *
 * Return :
 *           Return code :
 *           = 0 : sucessful
 *           > 0 : failing error number
 *           < 0 : failing error number
 *
 * Environment: Internal and External
 *
 * See Also: UF_OPER_set_ref_cutter
 *
 * History: Released in NX 2.0
 ******************************************************************/
extern UFUN_CAMEXPORT int UF_OPER_ask_ref_cutter
(
    tag_t  oper_tag,  /* <I> the operation tag */
    tag_t  *ref_cutter_tag /*<O>the tag of the reference cutter of the operation*/
);

/******************************************************************
 *
 * This function set the reference cutter for an operation. Currently,
 * only Cavity and Zlevel operations are allowed to set reference cutter.
 *
 * Return :
 *           Return code :
 *           = 0 : sucessful
 *           > 0 : failing error number
 *           < 0 : failing error number
 *
 * Environment: Internal and External
 *
 * See Also: UF_OPER_ask_ref_cutter
 *
 * History: Released in NX 2.0
 ******************************************************************/
extern UFUN_CAMEXPORT int UF_OPER_set_ref_cutter
(
    tag_t  oper_tag,  /* <I> the operation tag */
    tag_t  ref_cutter_tag /*<I>the tag of a reference cutter to the operation*/
);

/***************************************************************
 *   Set the Machining Data parameters in an operation.
 *
 * Return :
 *    UF_CAM_ERROR_TAG_NOT_CORRECT_TYPE
 *        The input tag is not an operation
 *
 *  UF_OPER_ERROR_QUERY_FAILED
 *      No match in the Machining Data library was found for the Cut Method,
 *          Part Material and Tool Material defined for this operation.
 *
 *  UF_CAM_ERROR_INSUFFICIENT_DATA
 *      At least one of the following is not defined for the operation:
 *          Cut Method, Part Material or Tool Material.
 *
 * Environment: Internal  and  External
 *
 * See Also:
 * History: Released in NX3.0
 *************************************************************/
 extern UFUN_CAMEXPORT int UF_OPER_set_machining_data
(
    tag_t      oper_tag                /* <I> tag of the operation */
);

/***************************************************************
 *   Reset the Feeds and Speeds data in an operation.
 *
 * Return :
 *    UF_CAM_ERROR_TAG_NOT_CORRECT_TYPE
 *        The input tag is not an operation
 *
 *  UF_OPER_ERROR_QUERY_FAILED
 *      No match in the Machining Data library was found for the Cut Method,
 *          Part Material and Tool Material defined for this operation.
 *
 *  UF_CAM_ERROR_INSUFFICIENT_DATA
 *      At least one of the following is not defined for the operation:
 *          Cut Method, Part Material or Tool Material.
 *
 * Environment: Internal  and  External
 *
 * See Also:
 * History: Released in NX3.0.3
 *************************************************************/
 extern UFUN_CAMEXPORT int UF_OPER_reset_from_table
(
    tag_t      oper_tag                /* <I> tag of the operation */
);
/***************************************************************
 *   Unload Tool Path of an Operation.
 *
 * Return :
 *      UF_CAM_ERROR_TAG_NOT_CORRECT_TYPE
 *         The input tag is not an operation 
 *
 * Environment: Internal  and  External
 *
 * See Also:
 * History: Released in NX5.0.2
 *************************************************************/
extern  UFUN_CAMEXPORT int UF_OPER_unload_path
(
   tag_t       oper_tag                          /* <I> tag of the operation */ 
);
#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif /* UF_OPER_H_INCLUDED */
