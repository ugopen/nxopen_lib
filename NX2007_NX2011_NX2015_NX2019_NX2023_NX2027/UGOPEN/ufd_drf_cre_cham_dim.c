/*-------------------------------------------------------------------------------------
  
             Copyright (c) 2002 Unigraphics Solutions Inc.
                      Unpublished - All rights reserved
  
  -------------------------------------------------------------------------------------

    Description:
     This program shows how to use the following User Function program:

           UF_DRF_create_chamfer_dim

 
  -------------------------------------------------------------------------------------*/

#include <stdio.h>
#include <uf.h>
#include <uf_defs.h>
#include <uf_drf.h>
#include <uf_curve.h>

void ufusr (char *param, int *retcod, int param_len)
{
    int status = 0;
    static double origin[3] = {-7.5, 1.0, 0.0};
    static char dimtxt[15+1] = " CHAMFER ";
    static char apptxt[3][132+1] = {"APPENDED TEXT",
                                    "APP TXT LINE 2",
                                    "APP TXT LINE 3"};
    tag_t line1_tag = 0, line2_tag = 0, dimension_tag;
    UF_CURVE_line_t line_coords;
    UF_DRF_object_t object1, object2;
    UF_DRF_text_t drf_text;

    status = UF_initialize ();

    if (!status)
    {
        /* initialize the object structures */
        UF_DRF_init_object_structure (&object1);
        UF_DRF_init_object_structure (&object2);
 
        /* load drf_text specification */
        drf_text.user_dim_text  = dimtxt;
        drf_text.lines_app_text = 3;
        drf_text.appended_text  =  apptxt;

        /* create the chamfer line */
        line_coords.start_point[0] = 0.0;
        line_coords.start_point[1] = 8.0;
        line_coords.end_point[0] = -8.0;
        line_coords.end_point[1] =  0.0;
        status = UF_CURVE_create_line (&line_coords, &line1_tag);
    }

    if (!status)
    {
        /* create the 45 degree line */
        line_coords.start_point[0] = 0.0;
        line_coords.start_point[1] = 8.0;
        line_coords.end_point[0] = 8.0;
        line_coords.end_point[1] = 8.0;
        status = UF_CURVE_create_line (&line_coords, &line2_tag);
    }

    if (!status)
    {
        /* create a chamfer dimension */
        object1.object_tag = line1_tag;
        object1.object_view_tag = NULL_TAG;
        object1.object_assoc_type = UF_DRF_end_point;
        object1.object_assoc_modifier = UF_DRF_last_end_point;
        object2.object_tag = line2_tag;
        object2.object_view_tag = NULL_TAG;
        object2.object_assoc_type = UF_DRF_end_point;
        object2.object_assoc_modifier = UF_DRF_first_end_point;
        status = UF_DRF_create_chamfer_dim
                     (&object1, &object2, &drf_text, origin, &dimension_tag);
    }

    printf ("UF_DRF_create_chamfer_dim ");
    if (status)
    {
        char status_message[133];

        UF_get_fail_message (status, status_message);
        printf ("has ERROR %d: %s.\n", status, status_message);
    }
    else
        printf ("is successful.\n");

    UF_terminate ();
}

/*-------------------------------------------------------------------------------------*/
