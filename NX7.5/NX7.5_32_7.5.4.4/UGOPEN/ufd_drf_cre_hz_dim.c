/*===========================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===========================================================================*/
/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following User Function program:       *
 *                                                                            *
 *         UF_DRF_create_horizontal_dim                                       *
 *                                                                            *
 
 *                                                                            *
 ******************************************************************************/

#include <stdio.h>
#include <uf.h>
#include <uf_defs.h>
#include <uf_drf.h>
#include <uf_curve.h>

void ufusr(char *param, int *retcod, int param_len)
{
   int status = 0;
   static double origin[3] = {2.0, -1.0, 0.0};
   static char dimtxt[15+1] = "HORIZONTAL DIM ";
   static char apptxt[3][132+1] = {"APPENDED TEXT",
                                   "APP TXT LINE 2",
                                   "APP TXT LINE 3"};
   char  stat_msg[133];
   tag_t line_tag = 0, dimension_tag;
   UF_CURVE_line_t line_coords;
   UF_DRF_object_t object1, object2;
   UF_DRF_text_t   drf_text;

   status = UF_initialize();

   if (!status)
   {
      /* initialize the object structures */
      UF_DRF_init_object_structure(&object1);
      UF_DRF_init_object_structure(&object2);

      /* load drf_text specification */
      drf_text.user_dim_text  = dimtxt;
      drf_text.lines_app_text = 3;
      drf_text.appended_text  = apptxt;

      /* create a line */
      line_coords.start_point[0] = 0.0;
      line_coords.start_point[1] = 0.0;
      line_coords.start_point[2] = 0.0;
      line_coords.end_point[0] = 4.0;
      line_coords.end_point[1] = 0.0;
      line_coords.end_point[2] = 0.0;
      status = UF_CURVE_create_line(&line_coords, &line_tag);
   }

   if (!status)
   {
      /* create a horizontal dimension */
      object1.object_tag = line_tag;
      object1.object_view_tag = NULL_TAG;
      object1.object_assoc_type = UF_DRF_end_point;
      object1.object_assoc_modifier = UF_DRF_first_end_point;
      object2.object_tag = line_tag;
      object2.object_view_tag = NULL_TAG;
      object2.object_assoc_type = UF_DRF_end_point;
      object2.object_assoc_modifier = UF_DRF_last_end_point;
      status = UF_DRF_create_horizontal_dim(&object1, &object2,
               &drf_text, origin, &dimension_tag);
   }

   printf("UF_DRF_create_horizontal_dim ");
   if (status)
   {
      UF_get_fail_message(status, stat_msg);
      printf("has ERROR %d: %s.\n", status, stat_msg);
   }
   else
      printf("is successful.\n");

   UF_terminate();
}
