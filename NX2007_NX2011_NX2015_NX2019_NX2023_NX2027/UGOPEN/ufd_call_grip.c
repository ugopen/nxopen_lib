/*===================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===================================================================*/

/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following UG/Open API routine(s):      *
 *                                                                            *
 *         UF_call_grip                                                       *
 *                                                                            *
 * PROGRAM DESCRIPTION -                                                      *
 *   The following example requires an open part that contains a point or a   *
 *   line. This program works in conjunction with a sample GRIP program named *
 *   grip_gets_call.grs. Compile and link the GRIP program using GRADE. Next, *
 *   compile and link this file, ufd_call_grip.c, as an internal UG/Open API. *
 *   Both of these files should be in the same directory.                     *
 *   Open a part that contains a line or point, then execute the internal     *
 *   program. The UG/Open API program calls the GRIP program.                 *
 *                                                                            *
              
 *                                                                            *
 ******************************************************************************/
#include <stdio.h>
#include <string.h>
#include <uf.h>
#include <uf_drf.h>
#include <uf_object_types.h>

#define UF_CALL(X) (report( __FILE__, __LINE__, #X, (X)))

static int report( char *file, int line, char *call, int irc)
{
    if (irc)
    {
        char    messg[133];
        printf("%s, line %d:  %s\n", file, line, call);
        (UF_get_fail_message(irc, messg)) ?
            printf("    returned a %d\n", irc) :
            printf("    returned error %d:  %s\n", irc, messg);
    }
    return(irc);
}

static void do_ugopen_api(void)
{
/******************************************************************
 *                                                                   
 * UG/Open API calling GRIP sample program                         
 *                                                                 
 * Define the argument structure needed for communication of
 * parameters to GRIP for this application. Pass the parameters for
 * masking and single selection. Receive the parameters concerning
 * the results of single selection. Use the results to create a
 * label.
 *
 ****************************************************************/
    double       masks[11], pick_point[3], user_response;
    tag_t        object;
    char         select_message[133], pick_view[133];
    char         *grip_exe = "grip_gets_call.grx";
    int          status;
    int          grip_arg_count = 6;
    UF_args_t    grip_arg_list[6];

    /* pick_view is passed to grip, and must be initialized, even
       though it is an output character string.
    */
    pick_view[0] = '\0';

  /* Define the argument list for UG/Open API calling GRIP */
    grip_arg_list[0].type    = UF_TYPE_DOUBLE_ARRAY;
    grip_arg_list[0].length  = 11;
    grip_arg_list[0].address = masks;
    grip_arg_list[1].type    = UF_TYPE_CHAR;
    grip_arg_list[1].length  = 0;
    grip_arg_list[1].address = select_message;
    grip_arg_list[2].type    = UF_TYPE_TAG_T;
    grip_arg_list[2].length  = 0;
    grip_arg_list[2].address = &object;
    grip_arg_list[3].type    = UF_TYPE_DOUBLE_ARRAY;
    grip_arg_list[3].length  = 3;
    grip_arg_list[3].address = pick_point;
    grip_arg_list[4].type    = UF_TYPE_CHAR;
    grip_arg_list[4].length  = 0;
    grip_arg_list[4].address = pick_view;
    grip_arg_list[5].type    = UF_TYPE_DOUBLE;
    grip_arg_list[5].length  = 0;
    grip_arg_list[5].address = &user_response;

  /* Initialize the input arguments to the GRIP program */
  /* masks[0] is the count of mask types */
    masks[0] = 2;
    masks[1] = UF_point_type;
    masks[2] = UF_line_type;
    strcpy (select_message, "Select A Point Or A Line.");

  /* Execute the GRIP program */
    status = UF_CALL(UF_call_grip (grip_exe, grip_arg_count,
                            grip_arg_list));

  /* Create a label if execution was successful and an
   * object was picked */
    if ( (status == 0) && (user_response >= 3) )
    {
        tag_t   label;
        double  label_origin[3];
        char    label_text[1][133];
        int     lines_of_text    = 1;
        int     leader_method    = 1;
        strcpy (label_text[0], pick_view);
        label_origin[0] = pick_point[0];
        label_origin[1] = pick_point[1] - 0.5;
        label_origin[2] = 0.0;
        uc5541(lines_of_text, label_text, label_origin,
               leader_method,object, pick_point, &label);
    }
}
/*ARGSUSED*/
void ufusr(char *param, int *retcode, int paramLen)
{
    if (!UF_CALL(UF_initialize()))
    {
        do_ugopen_api();
        UF_CALL(UF_terminate());
    }
}

int ufusr_ask_unload(void)
{
    return (UF_UNLOAD_IMMEDIATELY);
}
