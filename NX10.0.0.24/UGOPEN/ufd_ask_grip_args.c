/*===================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===================================================================*/

/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following UG/Open API routine(s):      *
 *                                                                            *
 *         UF_ask_grip_args                                                   *
 *                                                                            *
 * PROGRAM DESCRIPTION -                                                      *
 *   The following example requires an open part that contains a solid such   *
 *   as a box. This program works in conjunction with a sample GRIP program   *
 *   named grip_calls_api.grs. Compile and link the GRIP program with GRADE.  *
 *   Compile and link this file as an internal UG/Open API. Both files should *
 *   be in the same directory. Open a part with a box and run the grip        *
 *   program. You select a face on the box and the GRIP program calls the     *
 *   UG/Open API program and creates a hole.                                  *
 *                                                                            *
              
 *                                                                            *
 ******************************************************************************/
#include <stdio.h>
#include <string.h>
#include <uf.h>
#include <uf_modl.h>
#define GRIP_ARG_COUNT 7

/*ARGSUSED*/
extern void ufusr (char *param, int *retcod, int param_len)
{
  /* Declarations */
    tag_t        hole_faces[2], hole_feature;
    double       hole_position[3], hole_direction[3];
    char         hole_diameter[133], hole_depth[133];
    char         hole_angle[133], error_string[133];
    UF_args_t    grip_arg_list[GRIP_ARG_COUNT];
    int          error_status;
  /* Define the argument list for UG/Open API calling GRIP */
    grip_arg_list[0].type    = UF_TYPE_DOUBLE_ARRAY;
    grip_arg_list[0].length  = 3;
    grip_arg_list[0].address = hole_position;
    grip_arg_list[1].type    = UF_TYPE_DOUBLE_ARRAY;
    grip_arg_list[1].length  = 3;
    grip_arg_list[1].address = hole_direction;
    grip_arg_list[2].type    = UF_TYPE_CHAR;
    grip_arg_list[2].length  = 0;
    grip_arg_list[2].address = hole_diameter;
    grip_arg_list[3].type    = UF_TYPE_CHAR;
    grip_arg_list[3].length  = 0;
    grip_arg_list[3].address = hole_depth;
    grip_arg_list[4].type    = UF_TYPE_CHAR;
    grip_arg_list[4].length  = 0;
    grip_arg_list[4].address = hole_angle;
    grip_arg_list[5].type    = UF_TYPE_TAG_T_ARRAY;
    grip_arg_list[5].length  = 2;
    grip_arg_list[5].address = hole_faces;
    grip_arg_list[6].type    = UF_TYPE_CHAR;
    grip_arg_list[6].length  = 0;
    grip_arg_list[6].address = error_string;
  /* Initialize UG/Open API */
    UF_initialize();
  /* Update the local arguments with the contents from the GRIP variables */
    error_status = UF_ask_grip_args (GRIP_ARG_COUNT, grip_arg_list);
    if (error_status != 0)
    {
        UF_get_fail_message (error_status, error_string);
        fprintf (stderr, "UF_ask_grip_args failed due to: %s\n", error_string);
        return;
    }
  /* Create the simple hole */
    error_status = UF_MODL_create_simple_hole (hole_position, hole_direction,
                                               hole_diameter, hole_depth,
                                               hole_angle, hole_faces[0],
                                               hole_faces[1], &hole_feature);
    if (error_status != 0)
        UF_get_fail_message (error_status, error_string);
    else
        strcpy (error_string, "No error.");
  /* Update the GRIP arguments with the contents from the local variables */
    error_status = UF_set_grip_args (GRIP_ARG_COUNT, grip_arg_list);
    if (error_status != 0)
    {
        UF_get_fail_message (error_status, error_string);
        fprintf (stderr, "UF_set_grip_args failed due to: %s\n", error_string);
        return;
    }
  /* Terminate UG/Open API */
    UF_terminate();
}
